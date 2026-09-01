import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/axios'

const POSTS_TTL = 2 * 60 * 1000 // 2 minutes
const METADATA_TTL = 10 * 60 * 1000 // 10 minutes for categories/tags
const PREFETCH_TTL = 60 * 1000 // 1 minute -- a hover-prefetched post is only worth reusing if the click follows shortly after

function isCacheFresh(timestamp, ttl) {
  if (!timestamp) return false
  return Date.now() - timestamp < ttl
}

function paramsMatch(params1, params2) {
  return JSON.stringify(params1 || {}) === JSON.stringify(params2 || {})
}

export const useBlogStore = defineStore('blog', () => {
  // State
  const posts = ref([])
  const currentPost = ref(null)
  const categories = ref([])
  const tags = ref([])
  const loading = ref(false)
  const error = ref(null)
  const pagination = ref({
    count: 0,
    next: null,
    previous: null,
  })

  // Cache metadata
  const lastFetchedPosts = ref(null)
  const lastFetchedCategories = ref(null)
  const lastFetchedTags = ref(null)
  const cachedPostsParams = ref(null)

  // De-duplication (not persisted)
  let fetchingPostsPromise = null
  let fetchingCategoriesPromise = null
  let fetchingTagsPromise = null

  // Hover/intent prefetch cache: slug -> { data, timestamp }. Deliberately a
  // plain Map, not a ref -- this is a short-lived side cache a click reads
  // synchronously from, not something a template needs to react to. Kept
  // separate from `currentPost` and never touches `loading`/`error`, so
  // prefetching on hover can never flash an unrelated loading state
  // elsewhere in the app that happens to watch this store's `loading`.
  const prefetchedPosts = new Map()
  const prefetchingPromises = new Map()

  // Helper to normalize post data (fix broken URLs etc)
  function normalizePost(post) {
    if (!post) return post

    // Fix broken featured_image URLs (improperly prefixed external URLs)
    if (post.featured_image && typeof post.featured_image === 'string') {
      if (post.featured_image.includes('https%3A') || post.featured_image.includes('http%3A')) {
        try {
          const decoded = decodeURIComponent(post.featured_image)
          const match = decoded.match(/https?:\/\/[^\s"'<>]+/)
          if (match) {
            post.featured_image = match[0]
          }
        } catch (e) { /* ignore */ }
      }
    }

    return post
  }

  // Actions
  async function fetchPosts(params = {}, forceRefresh = false) {
    // Check cache freshness AND param match
    if (!forceRefresh &&
        isCacheFresh(lastFetchedPosts.value, POSTS_TTL) &&
        paramsMatch(params, cachedPostsParams.value) &&
        posts.value.length > 0) {
      console.log('[BlogStore] Using cached posts')
      return { results: posts.value }
    }

    // De-duplicate concurrent requests
    if (fetchingPostsPromise) {
      console.log('[BlogStore] Deduplicating concurrent fetch')
      return fetchingPostsPromise
    }

    loading.value = true
    error.value = null

    fetchingPostsPromise = (async () => {
      try {
        const response = await api.posts.list(params)
        const data = response.data

        // Ensure posts is always an array and normalize each post
        const rawPosts = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
        posts.value = rawPosts.map(normalizePost)

        // Update cache metadata
        cachedPostsParams.value = params
        lastFetchedPosts.value = Date.now()

        // Handle pagination
        if (data.count !== undefined) {
          pagination.value = {
            count: data.count,
            next: data.next,
            previous: data.previous,
          }
        }

        console.log('[BlogStore] Posts cached:', posts.value.length, 'items')
        return data
      } catch (err) {
        error.value = err.response?.data || 'Failed to fetch posts'
        console.error('Failed to fetch posts:', err)
        posts.value = []
        throw err
      } finally {
        loading.value = false
        fetchingPostsPromise = null
      }
    })()

    return fetchingPostsPromise
  }

  async function fetchPost(slug) {
    // A hover-prefetch already in flight or freshly resolved for this exact
    // slug means the click that triggered this call can skip the network
    // round-trip entirely -- this is what actually makes prefetching pay off,
    // not just the earlier hover request on its own.
    const prefetching = prefetchingPromises.get(slug)
    if (prefetching) {
      loading.value = true
      try {
        const result = await prefetching
        // A prefetch failure resolves to null (see prefetchPost's .catch) --
        // fall through to a real fetch below rather than treating that as a
        // genuine "not found", so a flaky background prefetch never breaks
        // the actual navigation.
        if (result) {
          currentPost.value = result
          return currentPost.value
        }
      } finally {
        loading.value = false
      }
    }

    const cached = prefetchedPosts.get(slug)
    if (cached && isCacheFresh(cached.timestamp, PREFETCH_TTL)) {
      currentPost.value = cached.data
      return currentPost.value
    }

    loading.value = true
    error.value = null

    try {
      const response = await api.posts.get(slug)
      currentPost.value = normalizePost(response.data)
      return currentPost.value
    } catch (err) {
      error.value = err.response?.data || 'Failed to fetch post'
      throw err
    } finally {
      loading.value = false
    }
  }

  // Fire-and-forget prefetch for a post a reader is likely about to open
  // (hover/focus intent on a card link). Deliberately does not touch
  // `loading`/`error`/`currentPost` -- those are for the actual navigation,
  // and mutating them here would flash loading state for a request the user
  // may never follow through on. De-dupes repeated hovers on the same card
  // and silently swallows failures (a failed prefetch just means the real
  // navigation fetch runs normally, same as if no prefetch had happened).
  function prefetchPost(slug) {
    if (!slug) return
    if (prefetchingPromises.has(slug)) return
    const cached = prefetchedPosts.get(slug)
    if (cached && isCacheFresh(cached.timestamp, PREFETCH_TTL)) return

    const promise = api.posts.get(slug)
      .then((response) => {
        const data = normalizePost(response.data)
        prefetchedPosts.set(slug, { data, timestamp: Date.now() })
        return data
      })
      .catch(() => null)
      .finally(() => {
        prefetchingPromises.delete(slug)
      })

    prefetchingPromises.set(slug, promise)
  }

  async function fetchCategories(forceRefresh = false) {
    if (!forceRefresh && isCacheFresh(lastFetchedCategories.value, METADATA_TTL) && categories.value.length > 0) {
      console.log('[BlogStore] Using cached categories')
      return categories.value
    }

    if (fetchingCategoriesPromise) return fetchingCategoriesPromise

    fetchingCategoriesPromise = (async () => {
      try {
        const response = await api.posts.categories()
        const data = response.data
        categories.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
        lastFetchedCategories.value = Date.now()
        return categories.value
      } catch (err) {
        console.error('Failed to fetch categories:', err)
        categories.value = []
        return []
      } finally {
        fetchingCategoriesPromise = null
      }
    })()

    return fetchingCategoriesPromise
  }

  async function fetchTags(forceRefresh = false) {
    if (!forceRefresh && isCacheFresh(lastFetchedTags.value, METADATA_TTL) && tags.value.length > 0) {
      console.log('[BlogStore] Using cached tags')
      return tags.value
    }

    if (fetchingTagsPromise) return fetchingTagsPromise

    fetchingTagsPromise = (async () => {
      try {
        const response = await api.posts.tags()
        const data = response.data
        tags.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
        lastFetchedTags.value = Date.now()
        return tags.value
      } catch (err) {
        console.error('Failed to fetch tags:', err)
        tags.value = []
        return []
      } finally {
        fetchingTagsPromise = null
      }
    })()

    return fetchingTagsPromise
  }

  async function createPost(data) {
    loading.value = true
    error.value = null

    try {
      const response = await api.posts.create(data)
      posts.value.unshift(response.data)
      lastFetchedPosts.value = null // Invalidate cache
      return response.data
    } catch (err) {
      error.value = err.response?.data || 'Failed to create post'
      throw err
    } finally {
      loading.value = false
    }
  }

  async function updatePost(slug, data) {
    loading.value = true
    error.value = null

    try {
      const response = await api.posts.update(slug, data)

      const index = posts.value.findIndex(p => p.slug === slug)
      if (index !== -1) {
        posts.value[index] = response.data
      }

      if (currentPost.value?.slug === slug) {
        currentPost.value = response.data
      }

      return response.data
    } catch (err) {
      error.value = err.response?.data || 'Failed to update post'
      throw err
    } finally {
      loading.value = false
    }
  }

  async function deletePost(slug) {
    loading.value = true
    error.value = null

    try {
      await api.posts.delete(slug)
      posts.value = posts.value.filter(p => p.slug !== slug)
      lastFetchedPosts.value = null // Invalidate cache

      if (currentPost.value?.slug === slug) {
        currentPost.value = null
      }
    } catch (err) {
      error.value = err.response?.data || 'Failed to delete post'
      throw err
    } finally {
      loading.value = false
    }
  }

  function clearError() {
    error.value = null
  }

  function clearCurrentPost() {
    currentPost.value = null
  }

  function invalidateCache() {
    lastFetchedPosts.value = null
    lastFetchedCategories.value = null
    lastFetchedTags.value = null
    cachedPostsParams.value = null
  }

  return {
    posts,
    currentPost,
    categories,
    tags,
    loading,
    error,
    pagination,
    fetchPosts,
    fetchPost,
    prefetchPost,
    fetchCategories,
    fetchTags,
    createPost,
    updatePost,
    deletePost,
    clearError,
    clearCurrentPost,
    invalidateCache,
  }
}, {
  persist: {
    key: 'sauti-blog',
    storage: sessionStorage,
    paths: ['posts', 'categories', 'tags', 'lastFetchedPosts', 'lastFetchedCategories', 'lastFetchedTags', 'cachedPostsParams', 'pagination']
  }
})
