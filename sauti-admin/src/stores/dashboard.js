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
      
      // Fallback to mock data for development
      stats.value = {
        content: {
          posts: { total: 12, published: 8, draft: 4, recent: 3 },
          videos: { total: 8, published: 6, recent: 2 },
          resources: { total: 15, recent: 1 },
          faqs: { total: 25 },
          partners: { total: 8 }
        },
        reports: { total: 45, pending: 12 },
        activity: { recent_posts: 3, recent_videos: 2, recent_resources: 1 }
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