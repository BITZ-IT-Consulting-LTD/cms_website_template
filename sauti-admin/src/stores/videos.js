import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/api'

export const useVideosStore = defineStore('videos', () => {
  // State
  const videos = ref([])
  const currentVideo = ref(null)
  const categories = ref([])
  const loading = ref(false)
  const error = ref(null)
  
  // Actions
  async function fetchVideos(params = {}) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.videos.list(params)
      const data = response.data
      // Ensure videos is always an array
      videos.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
      return videos.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch videos'
      console.error('Failed to fetch videos:', err)
      
      // Ensure videos is always an array even on error
      videos.value = []
      return videos.value
    } finally {
      loading.value = false
    }
  }
  
  async function fetchVideo(slug) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.videos.get(slug)
      currentVideo.value = response.data
      return currentVideo.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch video'
      console.error('Failed to fetch video:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function createVideo(videoData) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.videos.create(videoData)
      const newVideo = response.data
      videos.value.unshift(newVideo)
      return newVideo
    } catch (err) {
      error.value = err.message || 'Failed to create video'
      console.error('Failed to create video:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function updateVideo(slug, videoData) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.videos.update(slug, videoData)
      const updatedVideo = response.data
      const index = videos.value.findIndex(v => v.slug === slug)
      if (index !== -1) {
        videos.value[index] = updatedVideo
      }
      currentVideo.value = updatedVideo
      return updatedVideo
    } catch (err) {
      error.value = err.message || 'Failed to update video'
      console.error('Failed to update video:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function deleteVideo(slug) {
    loading.value = true
    error.value = null
    
    try {
      await api.videos.delete(slug)
      videos.value = videos.value.filter(v => v.slug !== slug)
      if (currentVideo.value?.slug === slug) {
        currentVideo.value = null
      }
    } catch (err) {
      error.value = err.message || 'Failed to delete video'
      console.error('Failed to delete video:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function fetchCategories() {
    try {
      const response = await api.get('/videos/categories/')
      // Ensure categories is always an array
      const data = response.data
      categories.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
      return categories.value
    } catch (err) {
      console.error('Failed to fetch video categories:', err)
      // Always ensure categories is an array
      categories.value = []
      return categories.value
    }
  }
  
  return {
    // State
    videos,
    currentVideo,
    categories,
    loading,
    error,
    
    // Actions
    fetchVideos,
    fetchVideo,
    createVideo,
    updateVideo,
    deleteVideo,
    fetchCategories,
  }
})
