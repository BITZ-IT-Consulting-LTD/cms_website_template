import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/api'

export const useDashboardStore = defineStore('dashboard', () => {
  // State
  const stats = ref({
    content: {
      posts: { total: 0, published: 0, draft: 0, recent: 0 },
      videos: { total: 0, published: 0, recent: 0 },
      resources: { total: 0, recent: 0 },
      faqs: { total: 0 },
      partners: { total: 0 }
    },
    reports: { total: 0, pending: 0 },
    activity: { recent_posts: 0, recent_videos: 0, recent_resources: 0 }
  })
  
  const contentList = ref([])
  const topContent = ref([])
  const loading = ref(false)
  const error = ref(null)
  
  // Actions
  async function fetchStats() {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.dashboard.stats()
      stats.value = response.data
      return stats.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch stats'
      console.error('Failed to fetch stats:', err)
      
      // Return default empty stats instead of mock data
      stats.value = {
        content: {
          posts: { total: 0, published: 0, draft: 0, recent: 0 },
          videos: { total: 0, published: 0, recent: 0 },
          resources: { total: 0, recent: 0 },
          faqs: { total: 0 },
          partners: { total: 0 }
        },
        reports: { total: 0, pending: 0 },
        activity: { recent_posts: 0, recent_videos: 0, recent_resources: 0 }
      }
      
      return stats.value
    } finally {
      loading.value = false
    }
  }
  
  async function fetchContentList() {
    loading.value = true
    error.value = null
    
    try {
      // Fetch posts from backend
      const postsResponse = await api.posts.list()
      const postsData = postsResponse.data
      const posts = Array.isArray(postsData) ? postsData : (postsData.results && Array.isArray(postsData.results) ? postsData.results : [])
      
      // Transform posts to content list format
      const transformedPosts = posts.map(post => ({
        id: post.id,
        title: post.title,
        excerpt: post.excerpt,
        type: 'blog',
        status: post.status?.toUpperCase() === 'PUBLISHED' ? 'published' : 'draft',
        date: new Date(post.created_at).toLocaleDateString(),
        slug: post.slug,
        views: post.views_count || 0
      }))
      
      // Fetch videos from backend
      const videosResponse = await api.videos.list()
      const videosData = videosResponse.data
      const videos = Array.isArray(videosData) ? videosData : (videosData.results && Array.isArray(videosData.results) ? videosData.results : [])
      
      // Transform videos to content list format
      const transformedVideos = videos.map(video => ({
        id: video.id,
        title: video.title,
        excerpt: video.description,
        type: 'video',
        status: video.status?.toUpperCase() === 'PUBLISHED' ? 'published' : 'draft',
        date: new Date(video.created_at).toLocaleDateString(),
        slug: video.slug,
        views: video.views_count || 0
      }))
      
      contentList.value = [...transformedPosts, ...transformedVideos]
      return contentList.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch content'
      console.error('Failed to fetch content:', err)
      
      // Ensure contentList is always an array even on error
      contentList.value = []
      return contentList.value
    } finally {
      loading.value = false
    }
  }
  
  async function fetchTopContent() {
    try {
      const response = await api.dashboard.topContent()
      const data = response.data
      // Ensure topContent is always an array
      topContent.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
      return topContent.value
    } catch (err) {
      console.error('Failed to fetch top content:', err)
      
      // Ensure topContent is always an array even on error
      topContent.value = []
      return topContent.value
    }
  }
  
  return {
    // State
    stats,
    contentList,
    topContent,
    loading,
    error,
    
    // Actions
    fetchStats,
    fetchContentList,
    fetchTopContent,
  }
})