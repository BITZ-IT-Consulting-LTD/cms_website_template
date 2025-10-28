import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/api'

export const usePostsStore = defineStore('posts', () => {
  // State
  const posts = ref([])
  const currentPost = ref(null)
  const categories = ref([])
  const tags = ref([])
  const loading = ref(false)
  const error = ref(null)
  
  // Actions
  async function fetchPosts(params = {}) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.posts.list(params)
      const data = response.data
      // Ensure posts is always an array
      posts.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
      return posts.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch posts'
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
  
  async function fetchCategories() {
    try {
      const response = await api.posts.categories()
      // Ensure categories is always an array
      const data = response.data
      categories.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
      return categories.value
    } catch (err) {
      console.error('Failed to fetch categories:', err)
      // Always ensure categories is an array
      categories.value = []
      return categories.value
    }
  }
  
  async function fetchTags() {
    try {
      const response = await api.posts.tags()
      // Ensure tags is always an array
      const data = response.data
      tags.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
      return tags.value
    } catch (err) {
      console.error('Failed to fetch tags:', err)
      // Always ensure tags is an array
      tags.value = []
      return tags.value
    }
  }
  
  return {
    // State
    posts,
    currentPost,
    categories,
    tags,
    loading,
    error,
    
    // Actions
    fetchPosts,
    fetchPost,
    createPost,
    updatePost,
    deletePost,
    fetchCategories,
    fetchTags,
  }
})
