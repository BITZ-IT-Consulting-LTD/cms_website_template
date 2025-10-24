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
      videos.value = response.data.results || response.data
      return videos.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch videos'
      console.error('Failed to fetch videos:', err)
      
      // Fallback to mock data for development
      videos.value = [
        {
          id: 1,
          title: 'Child Safety Tips',
          description: 'Important safety guidelines for children and parents',
          video_url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
          thumbnail_url: 'https://via.placeholder.com/400x225/3B82F6/FFFFFF?text=Child+Safety+Tips',
          duration: '5:30',
          category: 'Safety',
          status: 'published',
          views_count: 1200,
          created_at: '2024-01-15T10:00:00Z',
          updated_at: '2024-01-15T10:00:00Z'
        },
        {
          id: 2,
          title: 'Helpline Introduction',
          description: 'Learn about our helpline services and how to access them',
          video_url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
          thumbnail_url: 'https://via.placeholder.com/400x225/10B981/FFFFFF?text=Helpline+Introduction',
          duration: '3:45',
          category: 'Services',
          status: 'published',
          views_count: 800,
          created_at: '2024-01-10T10:00:00Z',
          updated_at: '2024-01-10T10:00:00Z'
        },
        {
          id: 3,
          title: 'Community Outreach',
          description: 'Our community engagement initiatives and programs',
          video_url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
          thumbnail_url: 'https://via.placeholder.com/400x225/8B5CF6/FFFFFF?text=Community+Outreach',
          duration: '7:20',
          category: 'Community',
          status: 'draft',
          views_count: 0,
          created_at: '2024-01-05T10:00:00Z',
          updated_at: '2024-01-05T10:00:00Z'
        }
      ]
      
      return videos.value
    } finally {
      loading.value = false
    }
  }
  
  async function fetchVideo(id) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.videos.get(id)
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
  
  async function updateVideo(id, videoData) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.videos.update(id, videoData)
      const updatedVideo = response.data
      const index = videos.value.findIndex(v => v.id === id)
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
  
  async function deleteVideo(id) {
    loading.value = true
    error.value = null
    
    try {
      await api.videos.delete(id)
      videos.value = videos.value.filter(v => v.id !== id)
      if (currentVideo.value?.id === id) {
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
      // Mock categories for now
      categories.value = [
        { id: 1, name: 'Safety', slug: 'safety' },
        { id: 2, name: 'Services', slug: 'services' },
        { id: 3, name: 'Community', slug: 'community' },
        { id: 4, name: 'Education', slug: 'education' }
      ]
      return categories.value
    } catch (err) {
      console.error('Failed to fetch video categories:', err)
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
