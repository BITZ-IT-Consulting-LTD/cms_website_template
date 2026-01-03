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

    <!-- Video Grid - Bento Grid Layout -->
    <div v-else class="relative w-full px-4 md:px-8">
      <div class="max-w-7xl mx-auto">
        <!-- Bento Grid Layout - Dynamic based on number of posts -->
        <div
          class="bento-grid gap-4"
          :class="{
            'bento-1': allPosts.length === 1,
            'bento-2': allPosts.length === 2,
            'bento-3': allPosts.length === 3,
            'bento-4': allPosts.length === 4,
            'bento-5': allPosts.length === 5,
            'bento-6-plus': allPosts.length >= 6
          }"
        >
          <div
            v-for="(post, index) in allPosts"
            :key="post.id"
            class="relative bg-white rounded-2xl shadow-xl overflow-hidden group bento-item"
            :class="getBentoItemClass(index, allPosts.length)"
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

            <!-- Twitter (X) Embed -->
            <div v-else-if="post.platform === 'Twitter (X)'" class="relative w-full bg-gray-50 p-4" style="min-height: 500px;">
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
import { ref, onMounted } from 'vue'
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
  if (lowerUrl.includes('twitter.com') || lowerUrl.includes('x.com')) return 'Twitter (X)'
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
    case 'Twitter (X)': return '#000000'
    case 'TikTok': return '#000000'
    case 'Instagram': return '#E4405F'
    case 'YouTube': return '#FF0000'
    case 'LinkedIn': return '#0A66C2'
    default: return '#6B7280'
  }
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

// Get bento grid item classes based on position and total count
const getBentoItemClass = (index, total) => {
  if (total === 1) return 'col-span-full row-span-2'

  if (total === 2) return 'col-span-1 row-span-2'

  if (total === 3) {
    // First item takes 2 rows, others are normal
    return index === 0 ? 'col-span-1 md:col-span-2 row-span-2' : 'col-span-1 row-span-1'
  }

  if (total === 4) {
    // 2x2 grid
    return 'col-span-1 row-span-1'
  }

  if (total === 5) {
    // First item is large (2x2), others normal
    return index === 0 ? 'col-span-1 md:col-span-2 row-span-2' : 'col-span-1 row-span-1'
  }

  // 6 or more: Mix of large and small tiles
  if (total >= 6) {
    // Make some items larger for visual interest
    const largeIndices = [0, 3, 7] // First, 4th, and 8th items are large
    if (largeIndices.includes(index)) {
      return 'col-span-1 md:col-span-2 row-span-2'
    }
    return 'col-span-1 row-span-1'
  }

  return 'col-span-1 row-span-1'
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

/* Bento Grid Base Styles */
.bento-grid {
  display: grid;
  grid-auto-rows: minmax(250px, auto);
  width: 100%;
}

/* Single Item - Centered large */
.bento-1 {
  grid-template-columns: 1fr;
  max-width: 600px;
  margin: 0 auto;
}

/* Two Items - Side by side */
.bento-2 {
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .bento-2 {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Three Items - One large, two small */
.bento-3 {
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .bento-3 {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Four Items - 2x2 Grid */
.bento-4 {
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .bento-4 {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .bento-4 {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Five Items - One large hero, four smaller */
.bento-5 {
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .bento-5 {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .bento-5 {
    grid-template-columns: repeat(4, 1fr);
  }
}

/* Six or More - Full bento grid with varied sizes */
.bento-6-plus {
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .bento-6-plus {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .bento-6-plus {
    grid-template-columns: repeat(4, 1fr);
  }
}

/* Bento Item Transitions */
.bento-item {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  min-height: 250px;
}

.bento-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}

/* Ensure embeds fill their containers */
.bento-item iframe,
.bento-item .fb-post,
.bento-item .twitter-tweet,
.bento-item .instagram-media {
  height: 100%;
  min-height: 100%;
}
</style>
