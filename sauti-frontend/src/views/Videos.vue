<template>
  <div class="section-padding">
    <div class="container-custom">
      <div class="flex items-center justify-between mb-6">
        <h2 class="text-2xl font-bold">Videos</h2>
        <router-link to="/resources" class="text-primary-600 hover:text-primary-700">Resources →</router-link>
      </div>

      <!-- Search and filters -->
      <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-4 mb-6">
        <div class="flex items-center gap-3">
          <div class="flex-1">
            <input class="form-input" placeholder="Search videos..." v-model="query" />
          </div>
          <button class="pill pill-primary" @click="applySearch">Search</button>
        </div>
        <div class="mt-3 flex flex-wrap gap-2">
          <button v-for="chip in chips" :key="chip" class="px-3 py-1 rounded-full text-sm bg-gray-100 hover:bg-gray-200" @click="setChip(chip)">{{ chip }}</button>
        </div>
      </div>

      <!-- Video grid (YouTube-like) -->
      <div v-if="loading" class="flex justify-center py-8">
        <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-[#8B4000]"></div>
      </div>
      
      <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        <article v-for="video in filteredVideos" :key="video.id" class="group">
          <div class="relative bg-gray-200 rounded-xl overflow-hidden aspect-video cursor-pointer" @click="openVideo(video)">
            <img :src="video.thumbnail" :alt="video.title" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy" @error="useThumbPlaceholder($event)" />
            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors duration-300 flex items-center justify-center">
              <div class="opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                <div class="bg-white/90 rounded-full p-3">
                  <svg class="w-6 h-6 text-[#8B4000]" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M8 5v14l11-7z"/>
                  </svg>
                </div>
              </div>
            </div>
            <span class="absolute bottom-2 right-2 text-xs font-bold bg-black/80 text-white px-1.5 py-0.5 rounded">{{ video.duration }}</span>
          </div>
          <div class="mt-3 flex gap-3">
            <div class="h-9 w-9 rounded-full bg-[#8B4000] flex items-center justify-center text-white font-bold text-sm">
              S
            </div>
            <div class="min-w-0">
              <h3 class="text-sm font-semibold text-gray-900 leading-5 line-clamp-2 group-hover:text-[#8B4000]">{{ video.title }}</h3>
              <p class="text-xs text-gray-600 mt-1">{{ video.author_name }}</p>
              <p class="text-xs text-gray-500">{{ formatViews(video.views_count) }} • {{ formatDate(video.published_at) }}</p>
            </div>
          </div>
        </article>
      </div>
    </div>
  </div>
  
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useVideosStore } from '@/stores/videos'

const videosStore = useVideosStore()
const query = ref('')
const chips = ['All', 'Education', 'Safety', 'Support', 'Recency', 'Popular']
const activeChip = ref('All')
const loading = ref(false)

const videos = ref([])

const filteredVideos = computed(() => {
  const q = query.value.trim().toLowerCase()
  return videos.value.filter(v => {
    const matchQuery = !q || v.title.toLowerCase().includes(q) || (v.author_name && v.author_name.toLowerCase().includes(q))
    const matchChip = activeChip.value === 'All' || 
      (v.category && v.category.name === activeChip.value) || 
      (activeChip.value === 'Popular' && v.views_count > 1000)
    return matchQuery && matchChip
  })
})

async function fetchVideos() {
  loading.value = true
  try {
    await videosStore.fetchVideos({ status: 'PUBLISHED' })
    videos.value = videosStore.videos.map(video => ({
      id: video.id,
      title: video.title,
      description: video.description,
      thumbnail: video.thumbnail || video.youtube_thumbnail_url || 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?q=80&w=1200&auto=format&fit=crop',
      youtube_url: video.youtube_url,
      views_count: video.views_count,
      author_name: video.author_name || 'Sauti Uganda',
      category: video.category,
      published_at: video.published_at,
      duration: video.duration || '5:00'
    }))
  } catch (error) {
    console.error('Failed to fetch videos:', error)
    // Fallback to mock data
    videos.value = [
      {
        id: 1,
        title: 'Understanding Child Rights',
        description: 'Learn about child rights in Uganda',
        thumbnail: 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?q=80&w=1200&auto=format&fit=crop',
        youtube_url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        views_count: 1200,
        author_name: 'Sauti Uganda',
        category: { name: 'Education' },
        published_at: '2024-01-15T10:00:00Z',
        duration: '12:45'
      }
    ]
  } finally {
    loading.value = false
  }
}

function setChip(chip) {
  activeChip.value = chip
}

function applySearch() {}

function useThumbPlaceholder(e) {
  e.target.src = 'https://picsum.photos/640/360?blur=2'
}

function useAvatarPlaceholder(e) {
  e.target.src = 'https://i.pravatar.cc/48'
}

function openVideo(video) {
  if (video.youtube_url) {
    window.open(video.youtube_url, '_blank')
  }
}

function formatViews(views) {
  if (views >= 1000000) {
    return `${(views / 1000000).toFixed(1)}M views`
  } else if (views >= 1000) {
    return `${(views / 1000).toFixed(1)}K views`
  }
  return `${views} views`
}

function formatDate(dateString) {
  if (!dateString) return 'Recently'
  const date = new Date(dateString)
  const now = new Date()
  const diffTime = Math.abs(now - date)
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
  
  if (diffDays === 1) return '1 day ago'
  if (diffDays < 7) return `${diffDays} days ago`
  if (diffDays < 30) return `${Math.ceil(diffDays / 7)} weeks ago`
  if (diffDays < 365) return `${Math.ceil(diffDays / 30)} months ago`
  return `${Math.ceil(diffDays / 365)} years ago`
}

onMounted(() => {
  fetchVideos()
})
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.aspect-video {
  position: relative;
  width: 100%;
  padding-bottom: 56.25%; /* 16:9 */
}
.aspect-video > img,
.aspect-video > video,
.aspect-video > div {
  position: absolute;
  inset: 0;
}
</style>

