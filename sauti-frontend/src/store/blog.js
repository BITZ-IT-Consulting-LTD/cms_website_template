import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/axios'

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
  async function fetchPosts(params = {}) {
    loading.value = true
    error.value = null

    try {
      const response = await api.posts.list(params)
      const data = response.data

      // Ensure posts is always an array and normalize each post
      const rawPosts = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
      posts.value = rawPosts.map(normalizePost)

      // Handle pagination
      if (data.count !== undefined) {
        pagination.value = {
          count: data.count,
          next: data.next,
          previous: data.previous,
        }
      }

      return data
    } catch (err) {
      error.value = err.response?.data || 'Failed to fetch posts'
      console.error('Failed to fetch posts:', err)
      // Ensure posts is always an array even on error
      posts.value = []
      throw err
    } finally {
      loading.value = false
    }
  }

  async function fetchPost(slug) {
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

  async function fetchCategories() {
    try {
      const response = await api.posts.categories()
      const data = response.data
      // Ensure categories is always an array
      categories.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
      return categories.value
    } catch (err) {
      console.error('Failed to fetch categories:', err)
      // Always ensure categories is an array
      categories.value = []
      return []
    }
  }

  async function fetchTags() {
    try {
      const response = await api.posts.tags()
      const data = response.data
      // Ensure tags is always an array
      tags.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
      return tags.value
    } catch (err) {
      console.error('Failed to fetch tags:', err)
      // Always ensure tags is an array
      tags.value = []
      return []
    }
  }

  async function createPost(data) {
    loading.value = true
    error.value = null

    try {
      const response = await api.posts.create(data)
      posts.value.unshift(response.data)
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

      // Update in list
      const index = posts.value.findIndex(p => p.slug === slug)
      if (index !== -1) {
        posts.value[index] = response.data
      }

      // Update current post if it's the one being edited
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

  return {
    // State
    posts,
    currentPost,
    categories,
    tags,
    loading,
    error,
    pagination,

    // Actions
    fetchPosts,
    fetchPost,
    fetchCategories,
    fetchTags,
    createPost,
    updatePost,
    deletePost,
    clearError,
    clearCurrentPost,
  }
})
