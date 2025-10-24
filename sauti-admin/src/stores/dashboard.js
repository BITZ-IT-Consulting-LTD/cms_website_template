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
      
      // Fallback to mock data for development
      stats.value = {
        totalPosts: 12,
        totalVideos: 8,
        totalViews: 15420,
        totalEngagement: 2340
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
      const posts = postsResponse.data.results || postsResponse.data
      
      // Transform posts to content list format
      const transformedPosts = posts.map(post => ({
        id: post.id,
        title: post.title,
        excerpt: post.excerpt,
        type: 'blog',
        status: post.status === 'published' ? 'published' : 'draft',
        date: new Date(post.created_at).toLocaleDateString(),
        slug: post.slug,
        views: post.views_count || 0
      }))
      
      // TODO: Fetch videos from backend when video API is ready
      const mockVideos = [
        {
          id: 1,
          title: 'Child Safety Tips',
          excerpt: 'Important safety guidelines for children',
          type: 'video',
          status: 'published',
          date: '2024-01-15',
          views: 1200
        },
        {
          id: 2,
          title: 'Helpline Introduction',
          excerpt: 'Learn about our helpline services',
          type: 'video',
          status: 'published',
          date: '2024-01-10',
          views: 800
        }
      ]
      
      contentList.value = [...transformedPosts, ...mockVideos]
      return contentList.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch content'
      console.error('Failed to fetch content:', err)
      
      // Fallback to mock data for development
      contentList.value = [
        {
          id: 1,
          title: 'Understanding Child Protection in Uganda',
          excerpt: 'A comprehensive guide to child protection laws and services',
          type: 'blog',
          status: 'published',
          date: '2024-01-20',
          slug: 'understanding-child-protection-uganda',
          views: 450
        },
        {
          id: 2,
          title: 'How to Report Child Abuse',
          excerpt: 'Step-by-step guide for reporting child abuse cases',
          type: 'blog',
          status: 'published',
          date: '2024-01-18',
          slug: 'how-to-report-child-abuse',
          views: 320
        },
        {
          id: 3,
          title: 'Community Outreach Programs',
          excerpt: 'Learn about our community engagement initiatives',
          type: 'blog',
          status: 'draft',
          date: '2024-01-15',
          slug: 'community-outreach-programs',
          views: 0
        },
        {
          id: 4,
          title: 'Child Safety Tips',
          excerpt: 'Important safety guidelines for children',
          type: 'video',
          status: 'published',
          date: '2024-01-15',
          views: 1200
        },
        {
          id: 5,
          title: 'Helpline Introduction',
          excerpt: 'Learn about our helpline services',
          type: 'video',
          status: 'published',
          date: '2024-01-10',
          views: 800
        }
      ]
      
      return contentList.value
    } finally {
      loading.value = false
    }
  }
  
  async function fetchTopContent() {
    try {
      const response = await api.dashboard.topContent()
      topContent.value = response.data
      return topContent.value
    } catch (err) {
      console.error('Failed to fetch top content:', err)
      
      // Fallback to mock data
      topContent.value = [
        { title: 'Understanding Child Protection in Uganda', type: 'Blog', views: 450 },
        { title: 'Child Safety Tips', type: 'Video', views: 1200 },
        { title: 'How to Report Child Abuse', type: 'Blog', views: 320 },
        { title: 'Helpline Introduction', type: 'Video', views: 800 }
      ]
      
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