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
  
  // Actions
  async function fetchPosts(params = {}) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.posts.list(params)
      posts.value = response.data.results || response.data
      
      // Handle pagination
      if (response.data.count !== undefined) {
        pagination.value = {
          count: response.data.count,
          next: response.data.next,
          previous: response.data.previous,
        }
      }
      
      return response.data
    } catch (err) {
      error.value = err.response?.data || 'Failed to fetch posts'
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
      currentPost.value = response.data
      return response.data
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
      categories.value = response.data
      return response.data
    } catch (err) {
      console.error('Failed to fetch categories:', err)
      return []
    }
  }
  
  async function fetchTags() {
    try {
      const response = await api.posts.tags()
      tags.value = response.data
      return response.data
    } catch (err) {
      console.error('Failed to fetch tags:', err)
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
