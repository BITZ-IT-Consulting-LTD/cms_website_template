import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/api'

const POSTS_TTL = 1 * 60 * 1000 // 1 minute (admin needs fresher data)
const METADATA_TTL = 5 * 60 * 1000 // 5 minutes for categories/tags

function isCacheFresh(timestamp, ttl) {
  if (!timestamp) return false
  return Date.now() - timestamp < ttl
}

function paramsMatch(params1, params2) {
  return JSON.stringify(params1 || {}) === JSON.stringify(params2 || {})
}

export const usePostsStore = defineStore('posts', () => {
  // State
  const posts = ref([])
  const currentPost = ref(null)
  const categories = ref([])
  const tags = ref([])
  const loading = ref(false)
  const error = ref(null)

  // Cache metadata
  const lastFetchedPosts = ref(null)
  const lastFetchedCategories = ref(null)
  const lastFetchedTags = ref(null)
  const cachedPostsParams = ref(null)

  // De-duplication
  let fetchingPostsPromise = null
  let fetchingCategoriesPromise = null
  let fetchingTagsPromise = null

  // Actions
  async function fetchPosts(params = {}, forceRefresh = false) {
    if (!forceRefresh &&
        isCacheFresh(lastFetchedPosts.value, POSTS_TTL) &&
        paramsMatch(params, cachedPostsParams.value) &&
        posts.value.length > 0) {
      console.log('[AdminPostsStore] Using cached posts')
      return posts.value
    }

    if (fetchingPostsPromise) return fetchingPostsPromise

    loading.value = true
    error.value = null

    fetchingPostsPromise = (async () => {
      try {
        const response = await api.posts.list(params)
        const data = response.data
        posts.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
        cachedPostsParams.value = params
        lastFetchedPosts.value = Date.now()
        console.log('[AdminPostsStore] Posts cached:', posts.value.length, 'items')
        return posts.value
      } catch (err) {
        error.value = err.message || 'Failed to fetch posts'
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
    loading.value = true
    error.value = null

    try {
      const response = await api.posts.get(slug)
      currentPost.value = response.data
      return currentPost.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch post'
      console.error('Failed to fetch post:', err)
      throw err
    } finally {
      loading.value = false
    }
  }

  async function createPost(postData) {
    loading.value = true
    error.value = null

    try {
      const response = await api.posts.create(postData)
      const newPost = response.data
      posts.value.unshift(newPost)
      lastFetchedPosts.value = null // Invalidate cache
      return newPost
    } catch (err) {
      error.value = err.message || 'Failed to create post'
      console.error('Failed to create post:', err)
      throw err
    } finally {
      loading.value = false
    }
  }

  async function updatePost(slug, postData) {
    loading.value = true
    error.value = null

    try {
      const response = await api.posts.update(slug, postData)
      const updatedPost = response.data
      const index = posts.value.findIndex(p => p.slug === slug)
      if (index !== -1) {
        posts.value[index] = updatedPost
      }
      currentPost.value = updatedPost
      return updatedPost
    } catch (err) {
      error.value = err.message || 'Failed to update post'
      console.error('Failed to update post:', err)
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
      error.value = err.message || 'Failed to delete post'
      console.error('Failed to delete post:', err)
      throw err
    } finally {
      loading.value = false
    }
  }

  async function fetchCategories(forceRefresh = false) {
    if (!forceRefresh && isCacheFresh(lastFetchedCategories.value, METADATA_TTL) && categories.value.length > 0) {
      console.log('[AdminPostsStore] Using cached categories')
      return categories.value
    }

    if (fetchingCategoriesPromise) return fetchingCategoriesPromise

    fetchingCategoriesPromise = (async () => {
      try {
        const response = await api.posts.categories.list()
        const data = response.data
        categories.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
        lastFetchedCategories.value = Date.now()
        return categories.value
      } catch (err) {
        console.error('Failed to fetch categories:', err)
        categories.value = []
        return categories.value
      } finally {
        fetchingCategoriesPromise = null
      }
    })()

    return fetchingCategoriesPromise
  }

  async function fetchTags(forceRefresh = false) {
    if (!forceRefresh && isCacheFresh(lastFetchedTags.value, METADATA_TTL) && tags.value.length > 0) {
      console.log('[AdminPostsStore] Using cached tags')
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
        return tags.value
      } finally {
        fetchingTagsPromise = null
      }
    })()

    return fetchingTagsPromise
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
    fetchPosts,
    fetchPost,
    createPost,
    updatePost,
    deletePost,
    fetchCategories,
    fetchTags,
    invalidateCache,
  }
}, {
  persist: {
    key: 'sauti-admin-posts',
    storage: sessionStorage,
    paths: ['posts', 'categories', 'tags', 'lastFetchedPosts', 'lastFetchedCategories', 'lastFetchedTags', 'cachedPostsParams']
  }
})
