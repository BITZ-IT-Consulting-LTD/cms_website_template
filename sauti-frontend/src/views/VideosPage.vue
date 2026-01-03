<template>
  <div class="bg-sauti-neutral py-16 md:py-24 min-h-screen">
    <div class="container-custom">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6">
        <div>
          <h1 class="text-4xl md:text-5xl lg:text-7xl font-black text-sauti-darkGreen mb-4 tracking-tight">Official
            <span class="text-sauti-blue">Videos</span>
          </h1>
          <p class="text-xl text-sauti-darkGreen/70 font-medium max-w-2xl">Educational resources, success stories and
            official announcements.</p>
        </div>
        <router-link to="/resources"
          class="group flex items-center gap-3 bg-sauti-white px-6 py-3 rounded-2xl border-2 border-sauti-neutral font-black text-sauti-darkGreen hover:bg-sauti-blue hover:text-sauti-white transition-all">
          {{ videosResourcesLink }}
          <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor"
            viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M17 8l4 4m0 0l-4 4m4-4H3" />
          </svg>
        </router-link>
      </div>

      <!-- Search and filters -->
      <div class="bg-sauti-white rounded-[2.5rem] border-2 border-sauti-neutral p-6 md:p-8 mb-12 shadow-sm">
        <div class="flex flex-col md:flex-row items-center gap-4">
          <div class="flex-1 w-full bg-sauti-neutral/30 rounded-2xl p-2 flex items-center gap-3">
            <div class="w-10 h-10 bg-sauti-white rounded-xl flex items-center justify-center text-sauti-darkGreen/30">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3"
                  d="M21 21l-4.35-4.35M11 19a8 8 0 100-16 8 8 0 000 16z" />
              </svg>
            </div>
            <input
              class="flex-1 bg-transparent border-none focus:ring-0 font-bold text-sauti-darkGreen placeholder-sauti-darkGreen/30"
              :placeholder="videosSearchPlaceholder" v-model="query" />
          </div>
          <button
            class="w-full md:w-auto bg-sauti-blue text-sauti-white px-8 py-4 rounded-2xl font-black shadow-lg shadow-sauti-blue/30 hover:scale-105 transition-transform"
            @click="applySearch">{{ videosSearchButton }}</button>
        </div>
        <div class="mt-8 flex flex-wrap gap-2">
          <button
            v-for="chip in [videosChipAll, videosChipEducation, videosChipSafety, videosChipSupport, videosChipRecency, videosChipPopular]"
            :key="chip" @click="setChip(chip)" :class="[
              'px-6 py-2 rounded-xl text-sm font-black transition-all duration-300 border-2',
              activeChip === chip ? 'bg-sauti-darkGreen border-sauti-darkGreen text-sauti-white shadow-md' : 'bg-sauti-white border-sauti-neutral text-sauti-darkGreen/60 hover:border-sauti-darkGreen hover:text-sauti-darkGreen'
            ]">
            {{ chip }}
          </button>
        </div>
      </div>

      <!-- Video grid (YouTube-like) -->
      <div v-if="loading" class="flex justify-center py-24">
        <div class="animate-spin rounded-full h-12 w-12 border-4 border-sauti-blue/20 border-t-sauti-blue"></div>
      </div>

      <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
        <article v-for="video in filteredVideos" :key="video.id"
          class="group bg-sauti-white p-4 rounded-[2rem] border-2 border-sauti-neutral transition-all duration-500 hover:shadow-2xl hover:shadow-sauti-blue/10 hover:border-sauti-blue/30">
          <div class="relative rounded-2xl overflow-hidden aspect-video shadow-inner bg-sauti-neutral cursor-pointer"
            @click="openVideo(video)">
            <img :src="video.thumbnail" :alt="video.title"
              class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" loading="lazy"
              @error="useThumbPlaceholder($event)" />
            <div
              class="absolute inset-0 bg-sauti-darkGreen/0 group-hover:bg-sauti-darkGreen/40 transition-colors duration-500 flex items-center justify-center">
              <div class="transform scale-0 group-hover:scale-100 transition-transform duration-500">
                <div class="bg-sauti-white rounded-full p-5 shadow-2xl">
                  <svg class="w-8 h-8 text-sauti-blue" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M8 5v14l11-7z" />
                  </svg>
                </div>
              </div>
            </div>
            <span v-if="video.duration"
              class="absolute bottom-4 right-4 text-xs font-black bg-sauti-darkGreen/90 text-sauti-white px-2 py-1 rounded-lg backdrop-blur-sm">{{
                video.duration }}</span>
          </div>
          <div class="mt-6 flex gap-4 pr-2">
            <div
              class="h-12 w-12 rounded-2xl bg-sauti-blue/10 flex items-center justify-center text-sauti-blue font-black shadow-sm flex-shrink-0">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                  d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
              </svg>
            </div>
            <div class="min-w-0">
              <h3
                class="text-base font-black text-sauti-darkGreen leading-tight line-clamp-2 transition-colors duration-300 group-hover:text-sauti-blue">
                {{ video.title }}</h3>
              <p
                class="text-xs text-sauti-darkGreen/50 font-bold mt-2 uppercase tracking-widest flex items-center gap-2">
                {{ video.author_name }}
                <span class="w-1 h-1 bg-sauti-neutral rounded-full"></span>
                {{ formatDate(video.published_at) }}
              </p>
            </div>
          </div>
        </article>
      </div>
    </div>

    <!-- Video Player Modal -->
    <VideoPlayerModal :isOpen="isModalOpen" :video="selectedVideo" @close="closeModal" />
  </div>

</template>

<script setup>
  import { ref, computed, onMounted } from 'vue'
  import { useVideosStore } from '@/store/videos'
  import { useSettingsStore } from '@/store/settings'
  import VideoPlayerModal from '@/components/videos/VideoPlayerModal.vue'

  defineOptions({
    name: 'VideosPage'
  })

  const videosStore = useVideosStore()
  const settingsStore = useSettingsStore()
  const query = ref('')
  const activeChip = ref('All')
  const loading = ref(false)
  const isModalOpen = ref(false)
  const selectedVideo = ref(null)

  // Computed properties for content
  const videosTitle = computed(() => settingsStore.settings.videos_title || 'Videos')
  const videosResourcesLink = computed(() => settingsStore.settings.videos_resources_link || 'Resources →')
  const videosSearchPlaceholder = computed(() => settingsStore.settings.videos_search_placeholder || 'Search videos...')
  const videosSearchButton = computed(() => settingsStore.settings.videos_search_button || 'Search')
  const videosChipAll = computed(() => settingsStore.settings.videos_chip_all || 'All')
  const videosChipEducation = computed(() => settingsStore.settings.videos_chip_education || 'Education')
  const videosChipSafety = computed(() => settingsStore.settings.videos_chip_safety || 'Safety')
  const videosChipSupport = computed(() => settingsStore.settings.videos_chip_support || 'Support')
  const videosChipRecency = computed(() => settingsStore.settings.videos_chip_recency || 'Recency')
  const videosChipPopular = computed(() => settingsStore.settings.videos_chip_popular || 'Popular')

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
        video_file: video.video_file,
        video_type: video.video_type || 'YOUTUBE',
        views_count: video.views_count,
        author_name: video.author_name || 'Sauti Uganda',
        category: video.category,
        published_at: video.published_at,
        duration: video.duration || '5:00'
      }))
    } catch (error) {
      console.error('Failed to fetch videos:', error)
      videos.value = []
    } finally {
      loading.value = false
    }
  }

  function setChip(chip) {
    activeChip.value = chip
  }

  function applySearch() { }

  function useThumbPlaceholder(e) {
    e.target.src = 'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?q=80&w=640&auto=format&fit=crop'
  }

  function openVideo(video) {
    selectedVideo.value = video
    isModalOpen.value = true
  }

  function closeModal() {
    isModalOpen.value = false
    selectedVideo.value = null
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

  onMounted(async () => {
    await settingsStore.fetchGlobalSettings()
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
    padding-bottom: 56.25%;
    /* 16:9 */
  }

  .aspect-video>img,
  .aspect-video>video,
  .aspect-video>div {
    position: absolute;
    inset: 0;
  }
</style>
