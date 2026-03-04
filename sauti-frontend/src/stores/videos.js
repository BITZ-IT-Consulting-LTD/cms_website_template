import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/axios'

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
      const response = await api.get('/videos/', { params })
      videos.value = response.data.results || response.data
      return videos.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch videos'
      console.error('Failed to fetch videos:', err)
      throw err
    } finally {
      loading.value = false
    }
  }

  async function fetchVideo(slug) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.get(`/videos/${slug}/`)
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

  async function fetchCategories() {
    try {
      const response = await api.get('/videos/categories/')
      categories.value = response.data
      return categories.value
    } catch (err) {
      console.error('Failed to fetch video categories:', err)
      throw err
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
    fetchCategories
  }
})
