import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/api'

const STATS_TTL = 2 * 60 * 1000 // 2 minutes
const CONTENT_TTL = 1 * 60 * 1000 // 1 minute

function isCacheFresh(timestamp, ttl) {
  if (!timestamp) return false
  return Date.now() - timestamp < ttl
}

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

  // Cache metadata
  const lastFetchedStats = ref(null)
  const lastFetchedContent = ref(null)

  // De-duplication
  let fetchingStatsPromise = null
  let fetchingContentPromise = null

  // Actions
  async function fetchStats(forceRefresh = false) {
    if (!forceRefresh && isCacheFresh(lastFetchedStats.value, STATS_TTL) && stats.value.reports) {
      console.log('[DashboardStore] Using cached stats')
      return stats.value
    }

    if (fetchingStatsPromise) return fetchingStatsPromise

    loading.value = true
    error.value = null

    fetchingStatsPromise = (async () => {
      try {
        const response = await api.dashboard.stats()
        stats.value = response.data
        lastFetchedStats.value = Date.now()
        console.log('[DashboardStore] Stats cached')
        return stats.value
      } catch (err) {
        error.value = err.message || 'Failed to fetch stats'
        console.error('Failed to fetch stats:', err)

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
        fetchingStatsPromise = null
      }
    })()

    return fetchingStatsPromise
  }

  async function fetchContentList(forceRefresh = false) {
    if (!forceRefresh && isCacheFresh(lastFetchedContent.value, CONTENT_TTL) && contentList.value.length > 0) {
      console.log('[DashboardStore] Using cached content list')
      return contentList.value
    }

    if (fetchingContentPromise) return fetchingContentPromise

    loading.value = true
    error.value = null

    fetchingContentPromise = (async () => {
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
        lastFetchedContent.value = Date.now()
        console.log('[DashboardStore] Content list cached:', contentList.value.length, 'items')
        return contentList.value
      } catch (err) {
        error.value = err.message || 'Failed to fetch content'
        console.error('Failed to fetch content:', err)
        contentList.value = []
        return contentList.value
      } finally {
        loading.value = false
        fetchingContentPromise = null
      }
    })()

    return fetchingContentPromise
  }

  async function fetchTopContent() {
    try {
      const response = await api.dashboard.topContent()
      const data = response.data
      topContent.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
      return topContent.value
    } catch (err) {
      console.error('Failed to fetch top content:', err)
      topContent.value = []
      return topContent.value
    }
  }

  function invalidateCache() {
    lastFetchedStats.value = null
    lastFetchedContent.value = null
  }

  return {
    stats,
    contentList,
    topContent,
    loading,
    error,
    lastFetchedStats,
    lastFetchedContent,
    fetchStats,
    fetchContentList,
    fetchTopContent,
    invalidateCache,
  }
}, {
  persist: {
    key: 'sauti-admin-dashboard',
    storage: sessionStorage,
    paths: ['stats', 'contentList', 'lastFetchedStats', 'lastFetchedContent']
  }
})
