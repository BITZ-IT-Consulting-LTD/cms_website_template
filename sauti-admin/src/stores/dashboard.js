import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/api'

export const useDashboardStore = defineStore('dashboard', () => {
  // State
  const stats = ref({
    totalPosts: 0,
    totalVideos: 0,
    totalViews: 0,
    totalEngagement: 0
  })
  const contentList = ref([])
  const topContent = ref([])
  const analytics = ref({})
  const loading = ref(false)
  const error = ref(null)
  
  // Actions
  async function fetchStats() {
    loading.value = true
    error.value = null
    
    try {
      // Since dashboard endpoints might not exist yet, we'll simulate with existing data
      const [postsResponse] = await Promise.all([
        api.posts.list({ page_size: 1 })
      ])
      
      // For now, we'll use mock data that matches the design
      stats.value = {
        totalPosts: 128,
        totalVideos: 42,
        totalViews: '24.5k',
        totalEngagement: '3.2k'
      }
      
      return stats.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch stats'
      // Use mock data on error
      stats.value = {
        totalPosts: 128,
        totalVideos: 42,
        totalViews: '24.5k',
        totalEngagement: '3.2k'
      }
      console.error('Failed to fetch stats:', err)
    } finally {
      loading.value = false
    }
  }
  
  async function fetchContentList(params = {}) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.posts.list(params)
      contentList.value = response.data.results || response.data
      return contentList.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch content'
      // Mock data for development
      contentList.value = [
        {
          id: 1,
          title: 'The Importance of Child Helplines',
          type: 'blog',
          status: 'published',
          date: 'Oct 26, 2023',
          slug: 'importance-child-helplines'
        },
        {
          id: 2,
          title: "Sauti's Mission: A Video Overview",
          type: 'video',
          status: 'published',
          date: 'Oct 24, 2023',
          slug: 'sautis-mission-video'
        },
        {
          id: 3,
          title: 'Draft: Understanding Child Rights',
          type: 'blog',
          status: 'draft',
          date: 'Oct 22, 2023',
          slug: 'understanding-child-rights'
        }
      ]
      console.error('Failed to fetch content list:', err)
    } finally {
      loading.value = false
    }
  }
  
  async function fetchTopContent() {
    try {
      // Mock data that matches the design
      topContent.value = [
        {
          title: 'The Importance of Child Helpli...',
          type: 'Blog Post',
          views: '10.2k Views'
        },
        {
          title: "Sauti's Mission: A Video Over...",
          type: 'Video',
          views: '8.1k Views'
        },
        {
          title: 'How to Report an Issue',
          type: 'Blog Post',
          views: '6.4k Views'
        }
      ]
      return topContent.value
    } catch (err) {
      console.error('Failed to fetch top content:', err)
    }
  }
  
  async function fetchAnalytics(params = {}) {
    try {
      // Mock analytics data
      analytics.value = {
        contentPerformance: {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
          datasets: [{
            label: 'Views',
            data: [1200, 1900, 3000, 5000, 4200, 6000],
            borderColor: '#E65100',
            backgroundColor: 'rgba(230, 81, 0, 0.1)'
          }]
        }
      }
      return analytics.value
    } catch (err) {
      console.error('Failed to fetch analytics:', err)
    }
  }
  
  return {
    // State
    stats,
    contentList,
    topContent,
    analytics,
    loading,
    error,
    
    // Actions
    fetchStats,
    fetchContentList,
    fetchTopContent,
    fetchAnalytics,
  }
})
