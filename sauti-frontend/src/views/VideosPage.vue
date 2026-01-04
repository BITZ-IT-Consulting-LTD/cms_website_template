<template>
  <div class="bg-sauti-white min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-10">
          <div class="flex-1">
            <h1 class="page-header-title">
              Official <span class="text-sauti-blue">Videos</span>
            </h1>
            <p class="page-header-subtitle">
              Educational resources, success stories and official announcements from the National Helpline.
            </p>
          </div>
          <div class="shrink-0 pb-2">
            <BaseCTA href="/resources" variant="outline" class="group gap-3">
              {{ videosResourcesLink }}
              <ArrowRightIcon class="w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </BaseCTA>
          </div>
        </div>
      </div>
    </header>

    <div class="container-custom section-padding section-rhythm">
      <!-- 2. Search & Filter System -->
      <section aria-labelledby="filters-heading">
        <div class="bg-sauti-neutral rounded-[3rem] p-8 md:p-12 shadow-none max-w-6xl mx-auto">
          <div class="flex flex-col md:flex-row items-center gap-8">
            <div
              class="flex-1 w-full bg-white shadow-sm border-none rounded-2xl p-2 flex items-center gap-4 group focus-within:shadow-md transition-all">
              <div
                class="w-12 h-12 bg-sauti-blue/5 rounded-xl flex items-center justify-center text-sauti-blue group-focus-within:bg-sauti-blue group-focus-within:text-white transition-all">
                <MagnifyingGlassIcon class="w-6 h-6" />
              </div>
              <input
                class="flex-1 bg-transparent border-none focus:ring-0 font-bold text-sauti-darkGreen placeholder-sauti-blue/40"
                :placeholder="videosSearchPlaceholder" v-model="query" @input="applySearch" />
            </div>
            <button class="btn btn-info !px-12 w-full md:w-auto" @click="applySearch">
              {{ videosSearchButton }}
            </button>
          </div>

          <!-- Tag Cloud -->
          <div class="mt-12 flex flex-wrap gap-3">
            <button
              v-for="chip in [videosChipAll, videosChipEducation, videosChipSafety, videosChipSupport, videosChipRecency, videosChipPopular]"
              :key="chip" @click="setChip(chip)" :class="[
                'px-6 py-2.5 rounded-full text-xs font-bold uppercase tracking-widest transition-all duration-300 border-2',
                activeChip === chip ? 'bg-sauti-darkGreen border-sauti-darkGreen text-sauti-white shadow-xl scale-105' : 'bg-sauti-white border-sauti-neutral text-sauti-darkGreen/50 hover:border-sauti-blue hover:text-sauti-blue'
              ]">
              {{ chip }}
            </button>
          </div>
        </div>
      </section>

      <!-- 3. Video Grid -->
      <section aria-label="Video Gallery">
        <div v-if="loading" class="flex justify-center py-24">
          <div class="spinner"></div>
        </div>

        <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
          <article v-for="video in filteredVideos" :key="video.id"
            class="card-base group overflow-hidden !p-4 transition-all duration-500 hover:shadow-2xl">
            <!-- Thumbnail Wrapper -->
            <div class="relative rounded-[1.5rem] overflow-hidden aspect-video bg-sauti-neutral cursor-pointer"
              @click="openVideo(video)">
              <img :src="video.thumbnail" :alt="video.title"
                class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
                loading="lazy" @error="useThumbPlaceholder($event)" />
              <div
                class="absolute inset-0 bg-sauti-darkGreen/0 group-hover:bg-sauti-darkGreen/40 transition-colors duration-500 flex items-center justify-center">
                <div class="transform scale-0 group-hover:scale-100 transition-transform duration-500">
                  <div class="bg-sauti-white rounded-full p-5 shadow-2xl">
                    <PlayIcon class="w-10 h-10 text-sauti-blue" />
                  </div>
                </div>
              </div>
              <span v-if="video.duration"
                class="absolute bottom-4 right-4 text-[10px] font-bold bg-sauti-darkGreen/90 text-sauti-white px-2 py-1 rounded-lg backdrop-blur-sm campaign-header">
                {{ video.duration }}
              </span>
            </div>

            <!-- Content -->
            <div class="mt-6 flex gap-4">
              <div
                class="h-12 w-12 rounded-2xl bg-sauti-blue/10 flex items-center justify-center text-sauti-blue border border-sauti-blue/20 shrink-0">
                <VideoCameraIcon class="w-6 h-6" />
              </div>
              <div class="min-w-0">
                <h3
                  class="campaign-header text-sm text-sauti-darkGreen leading-tight line-clamp-2 transition-colors duration-300 group-hover:text-sauti-blue normal-case tracking-normal font-bold">
                  {{ video.title }}
                </h3>
                <div class="flex items-center gap-2 mt-2">
                  <p class="campaign-header text-[10px] text-sauti-darkGreen/40 truncate">
                    {{ video.author_name }}
                  </p>
                  <span class="w-1 h-1 bg-sauti-neutral rounded-full shrink-0"></span>
                  <p class="campaign-header text-[10px] text-sauti-darkGreen/40 shrink-0">
                    {{ formatDate(video.published_at) }}
                  </p>
                </div>
              </div>
            </div>
          </article>
        </div>
      </section>
    </div>

    <!-- Video Player Modal Component -->
    <VideoPlayerModal :isOpen="isModalOpen" :video="selectedVideo" @close="closeModal" />
  </div>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue'
  import { useVideosStore } from '@/store/videos'
  import { useSettingsStore } from '@/store/settings'
  import VideoPlayerModal from '@/components/videos/VideoPlayerModal.vue'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import {
    ArrowRightIcon,
    MagnifyingGlassIcon,
    PlayIcon,
    VideoCameraIcon
  } from '@heroicons/vue/24/outline'

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

  const videosResourcesLink = computed(() => settingsStore.settings.videos_resources_link || 'Browse Resources')
  const videosSearchPlaceholder = computed(() => settingsStore.settings.videos_search_placeholder || 'Search video archive...')
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
    } finally {
      loading.value = false
    }
  }

  const setChip = (chip) => activeChip.value = chip
  const applySearch = () => { }
  const useThumbPlaceholder = (e) => e.target.src = 'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?q=80&w=640&auto=format&fit=crop'

  const openVideo = (video) => {
    selectedVideo.value = video
    isModalOpen.value = true
  }

  const closeModal = () => {
    isModalOpen.value = false
    selectedVideo.value = null
  }

  function formatDate(dateString) {
    if (!dateString) return 'Recently'
    const date = new Date(dateString)
    const now = new Date()
    const diffTime = Math.abs(now - date)
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
    if (diffDays === 1) return 'Yesterday'
    if (diffDays < 7) return `${diffDays} days ago`
    if (diffDays < 30) return `${Math.ceil(diffDays / 7)} weeks ago`
    return `${Math.ceil(diffDays / 30)} months ago`
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
  }

  .aspect-video>* {
    position: absolute;
    inset: 0;
  }
</style>
