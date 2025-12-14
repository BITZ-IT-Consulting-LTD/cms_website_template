import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/axios'

export const useVideosStore = defineStore('videos', () => {
  // State
  const videos = ref([])
  const loading = ref(false)
  const error = ref(null)

  // Actions
  async function fetchVideos(params = {}) {
    loading.value = true
    error.value = null
    try {
      const response = await api.get('/videos/', { params })
      videos.value = response.data.results || []
    } catch (err) {
      error.value = err.message || 'Failed to fetch videos'
      console.error('Failed to fetch videos:', err)
    } finally {
      loading.value = false
    }
  }

  return {
    // State
    videos,
    loading,
    error,

    // Actions
    fetchVideos,
  }
})
