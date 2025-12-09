<template>
  <div class="social-carousel-container relative w-full min-h-[600px] bg-transparent overflow-hidden flex flex-col items-center py-8">
    <!-- Title -->
    <div class="text-center mb-8 z-10">
      <h2 class="text-3xl font-bold text-gray-900 mb-2">Follow Us on Social Media</h2>
      <p class="text-gray-600">Stay connected with our latest updates</p>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex-1 flex items-center justify-center min-h-[400px]">
      <div class="text-center">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
        <p class="text-gray-600">Loading social media posts...</p>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else-if="allPosts.length === 0" class="flex-1 flex items-center justify-center text-gray-500 min-h-[400px]">
      <div class="text-center">
        <svg class="w-16 h-16 text-gray-300 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
        <p class="text-lg font-medium">No posts found for this category</p>
        <p class="text-sm text-gray-400 mt-2">Try selecting a different filter</p>
      </div>
    </div>

    <!-- Video Grid - Flexible Layout -->
    <div v-else class="relative w-full px-4 md:px-8">
      <div class="max-w-7xl mx-auto">
        <!-- Dynamic grid based on number of posts -->
        <div
          class="grid gap-6"
          :class="{
            'grid-cols-1 md:grid-cols-2 lg:grid-cols-4': allPosts.length === 4,
            'grid-cols-1 md:grid-cols-3': allPosts.length === 3,
            'grid-cols-1 md:grid-cols-2': allPosts.length === 2,
            'grid-cols-1 max-w-2xl mx-auto': allPosts.length === 1
          }"
        >
          <div
            v-for="post in allPosts"
            :key="post.id"
            class="relative bg-white rounded-2xl shadow-xl overflow-hidden group"
          >
            <!-- TikTok Embed -->
            <div v-if="post.platform === 'TikTok'" class="relative w-full" style="padding-bottom: 177.78%;">
              <iframe
                :src="getTikTokEmbedUrl(post.post_url)"
                class="absolute top-0 left-0 w-full h-full"
                frameborder="0"
                allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
              ></iframe>
            </div>

            <!-- YouTube Embed -->
            <div v-else-if="post.platform === 'YouTube'" class="relative w-full" style="padding-bottom: 177.78%;">
              <iframe
                :src="`https://www.youtube.com/embed/${getYouTubeVideoId(post.post_url)}?rel=0&modestbranding=1`"
                class="absolute top-0 left-0 w-full h-full"
                frameborder="0"
                allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
              ></iframe>
            </div>

            <!-- Facebook Embed -->
            <div v-else-if="post.platform === 'Facebook'" class="relative w-full bg-gray-100 flex items-center justify-center" style="min-height: 500px;">
              <div class="fb-post" :data-href="post.post_url" data-width="auto" data-show-text="true"></div>
            </div>

            <!-- Twitter Embed -->
            <div v-else-if="post.platform === 'Twitter'" class="relative w-full bg-gray-50 p-4" style="min-height: 500px;">
              <blockquote class="twitter-tweet" data-theme="light">
                <a :href="post.post_url"></a>
              </blockquote>
            </div>

            <!-- Instagram Embed -->
            <div v-else-if="post.platform === 'Instagram'" class="relative w-full bg-white flex items-center justify-center p-4" style="min-height: 600px;">
              <blockquote
                class="instagram-media"
                :data-instgrm-permalink="post.post_url"
                data-instgrm-version="14"
                style="max-width: 540px; width: 100%;"
              ></blockquote>
            </div>

            <!-- Fallback for Unknown Platform -->
            <div v-else class="relative w-full aspect-video bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center">
              <a :href="post.post_url" target="_blank" class="text-center p-8">
                <div class="text-gray-400 mb-4">
                  <svg class="w-16 h-16 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
                  </svg>
                </div>
                <p class="text-gray-600 font-medium">View Post</p>
                <p class="text-sm text-gray-400 mt-2">{{ post.platform }}</p>
              </a>
            </div>

            <!-- Platform Badge -->
            <div class="absolute top-4 left-4 z-10">
              <div
                class="px-3 py-1 rounded-full text-white text-sm font-semibold shadow-lg flex items-center gap-2"
                :style="{ backgroundColor: getPlatformColor(post.platform) }"
              >
                <span>{{ post.platform }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { api } from '@/utils/axios'

const loading = ref(true)
const allPosts = ref([])

// Fetch channel URLs and convert them to posts
const fetchPosts = async () => {
  loading.value = true

  try {
    console.log('Fetching social media channels')
    const response = await api.get('/social/channels/')

    console.log('API Response:', response)
    console.log('Response data:', response.data)

    // Convert channel URLs to post objects
    const channels = response.data
    const posts = []

    // Process each channel URL
    const channelUrls = [
      channels.channel_1_url,
      channels.channel_2_url,
      channels.channel_3_url,
      channels.channel_4_url
    ].filter(url => url) // Remove empty URLs

    for (const url of channelUrls) {
      const platform = detectPlatform(url)
      posts.push({
        id: url, // Use URL as unique ID
        platform,
        post_url: url,
        handle: '@sauti116',
        content: '',
        image: null,
        likes_count: '',
        comments_count: '',
        shares_count: '',
        is_active: true
      })
    }

    allPosts.value = posts
    console.log(`Successfully loaded ${posts.length} channel URLs`)
    console.log('Posts:', allPosts.value)
  } catch (error) {
    console.error('Failed to fetch social channels:', error)
    console.error('Error details:', error.response?.data)
    allPosts.value = []
  } finally {
    loading.value = false
  }
}

// Detect platform from URL
const detectPlatform = (url) => {
  if (!url) return 'Unknown'
  const lowerUrl = url.toLowerCase()
  if (lowerUrl.includes('tiktok.com')) return 'TikTok'
  if (lowerUrl.includes('youtube.com') || lowerUrl.includes('youtu.be')) return 'YouTube'
  if (lowerUrl.includes('twitter.com') || lowerUrl.includes('x.com')) return 'Twitter'
  if (lowerUrl.includes('facebook.com')) return 'Facebook'
  if (lowerUrl.includes('instagram.com')) return 'Instagram'
  return 'Unknown'
}

// Get TikTok embed URL from video URL
const getTikTokEmbedUrl = (url) => {
  if (!url) return ''
  // Extract video ID from TikTok URL
  // Format: https://www.tiktok.com/@username/video/1234567890
  const match = url.match(/\/video\/(\d+)/)
  if (match) {
    return `https://www.tiktok.com/embed/v2/${match[1]}`
  }
  return url
}

const getPlatformColor = (platform) => {
  switch (platform) {
    case 'Facebook': return '#1877F2'
    case 'Twitter': return '#1DA1F2'
    case 'TikTok': return '#000000'
    case 'Instagram': return '#E4405F'
    case 'YouTube': return '#FF0000'
    case 'LinkedIn': return '#0A66C2'
    default: return '#6B7280'
  }
}

const handleImageError = (e) => {
  // Use a beautiful gradient placeholder instead of trying another image
  e.target.style.display = 'none'
  const parent = e.target.parentElement
  if (parent) {
    parent.innerHTML = `
      <div class="w-full h-full bg-gradient-to-br from-blue-500 via-purple-500 to-pink-500 flex items-center justify-center relative overflow-hidden">
        <div class="absolute inset-0 opacity-30">
          <div class="absolute top-0 left-0 w-full h-full">
            <div class="absolute top-1/4 left-1/4 w-32 h-32 bg-white rounded-full blur-3xl"></div>
            <div class="absolute bottom-1/4 right-1/4 w-40 h-40 bg-white rounded-full blur-3xl"></div>
          </div>
        </div>
        <div class="relative z-10 text-center">
          <svg class="w-24 h-24 text-white mx-auto mb-4" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
          </svg>
          <p class="text-white font-bold text-lg">Social Media</p>
        </div>
      </div>
    `
  }
}

const openPost = (url) => {
  if (!url || url === '#') return
  window.open(url, '_blank')
}

// Extract TikTok video ID from URL
const getTikTokVideoId = (url) => {
  if (!url) return null
  const match = url.match(/\/video\/(\d+)/)
  return match ? match[1] : null
}

// Extract YouTube video ID from URL
const getYouTubeVideoId = (url) => {
  if (!url) return null
  const patterns = [
    /(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&\n?#]+)/,
    /youtube\.com\/embed\/([^&\n?#]+)/
  ]
  for (const pattern of patterns) {
    const match = url.match(pattern)
    if (match) return match[1]
  }
  return null
}

// Load social media embed scripts
const loadEmbedScripts = () => {
  // Twitter
  if (!window.twttr) {
    const twitterScript = document.createElement('script')
    twitterScript.src = 'https://platform.twitter.com/widgets.js'
    twitterScript.async = true
    twitterScript.charset = 'utf-8'
    document.body.appendChild(twitterScript)
  } else {
    window.twttr.widgets.load()
  }

  // Facebook
  if (!window.FB) {
    const facebookScript = document.createElement('script')
    facebookScript.src = 'https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v18.0'
    facebookScript.async = true
    facebookScript.defer = true
    facebookScript.crossOrigin = 'anonymous'
    document.body.appendChild(facebookScript)

    // Add FB root div if not exists
    if (!document.getElementById('fb-root')) {
      const fbRoot = document.createElement('div')
      fbRoot.id = 'fb-root'
      document.body.insertBefore(fbRoot, document.body.firstChild)
    }
  } else {
    window.FB.XFBML.parse()
  }

  // Instagram
  if (!window.instgrm) {
    const instagramScript = document.createElement('script')
    instagramScript.src = 'https://www.instagram.com/embed.js'
    instagramScript.async = true
    document.body.appendChild(instagramScript)
  } else {
    window.instgrm.Embeds.process()
  }
}

onMounted(async () => {
  await fetchPosts()
  // Load embed scripts after posts are loaded
  setTimeout(() => {
    loadEmbedScripts()
  }, 500)
})
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
