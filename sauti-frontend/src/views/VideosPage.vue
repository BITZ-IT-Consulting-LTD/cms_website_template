<template>
  <div class="min-h-screen bg-white">
    <!-- Hero Banner -->
    <header class="hero-banner" style="padding-top: clamp(70px, 15vw, 90px);">
      <div class="hero-overlay"></div>
      <div class="container-custom hero-content-wrapper">
        <div class="hero-text">
          <h1 class="hero-title">
            {{ siteContent.getContent('videos_page_title', 'Sauti') }} <span class="text-accent-yellow">{{ siteContent.getContent('videos_page_title_highlight', 'Audio-Visuals') }}</span>
          </h1>
          <p class="hero-subtitle">
            {{ siteContent.getContent('videos_page_subtitle', 'Explore our archive of official media content, awareness videos, and community stories.') }}
          </p>
        </div>
      </div>
    </header>

    <!-- Search Bar -->
    <div class="bg-white border-b border-gray-100">
      <div class="container-custom py-4">
        <div class="search-box">
          <Search class="search-icon-inline" />
          <input
            v-model="query"
            @input="applySearch"
            type="search"
            :placeholder="siteContent.getContent('videos_search_placeholder', videosSearchPlaceholder)"
            class="search-input-inline"
          />
          <button class="search-btn-inline" @click="applySearch">
            {{ siteContent.getContent('videos_search_button', videosSearchButton) }}
          </button>
        </div>
      </div>
    </div>

    <!-- Sticky Filter Tabs -->
    <div class="sticky top-[70px] z-30 bg-white/95 backdrop-blur-md border-b border-gray-100 shadow-sm">
      <div class="container-custom">
        <div class="filter-tabs-wrapper">
          <button
            v-for="chip in filterChips"
            :key="chip.value"
            @click="activeFilter = chip.value"
            :class="[
              'filter-chip',
              activeFilter === chip.value ? 'filter-chip-active' : 'filter-chip-inactive'
            ]"
          >
            {{ chip.label }}
          </button>
        </div>
      </div>
    </div>

    <div class="container-custom section-padding !pt-8 sm:!pt-12">

      <!-- Loading Skeleton -->
      <div v-if="loading" class="space-y-8 sm:space-y-12">
        <div class="grid grid-cols-2 xs:grid-cols-3 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-2 sm:gap-3">
          <div v-for="n in 12" :key="n" class="skeleton-card">
            <div class="skeleton-thumbnail"></div>
            <div class="skeleton-content">
              <div class="skeleton-title"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Content -->
      <div v-else class="space-y-8">
        <!-- Videos Section -->
        <section v-if="activeFilter === 'VIDEOS'" aria-label="Video Gallery">
          <!-- Empty State -->
          <div v-if="videos.filter(v => !isAudio(v)).length === 0" class="empty-state">
            <Video class="empty-icon" />
            <h3 class="empty-title">{{ siteContent.getContent('videos_empty_title', 'No videos found') }}</h3>
            <p class="empty-subtitle">{{ siteContent.getContent('videos_empty_subtitle', 'Check back later for new content') }}</p>
          </div>

          <!-- Video Grid -->
          <div v-else class="grid grid-cols-2 xs:grid-cols-3 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-2 sm:gap-3">
            <article v-for="video in videos.filter(v => !isAudio(v))" :key="video.id"
              class="video-card group cursor-pointer"
              @click="openVideo(video)">

              <!-- Video Thumbnail -->
              <div class="video-thumbnail-wrapper">
                <img :src="video.thumbnail" :alt="video.title"
                  class="video-thumbnail"
                  loading="lazy" @error="useThumbPlaceholder($event)" />

                <!-- Gradient Overlay -->
                <div class="video-overlay"></div>

                <!-- Play Button Overlay -->
                <div class="play-button-wrapper">
                  <div class="play-button">
                    <Play class="play-icon" />
                  </div>
                </div>

                <!-- Duration Badge -->
                <span v-if="video.duration" class="duration-badge">
                  {{ video.duration }}
                </span>
              </div>

              <!-- Video Info -->
              <div class="video-info">
                <h3 class="video-title">
                  {{ video.title }}
                </h3>

                <p class="video-date">
                  {{ formatDate(video.updated_at || video.published_at || video.created_at) }}
                </p>
              </div>
            </article>
          </div>
        </section>

        <!-- Audio Section - Podcast Style -->
        <section v-if="activeFilter === 'AUDIO'" aria-label="Audio Gallery">
          <!-- Empty State -->
          <div v-if="videos.filter(v => isAudio(v)).length === 0" class="empty-state">
            <Play class="empty-icon" />
            <h3 class="empty-title">{{ siteContent.getContent('videos_audio_empty_title', 'No audio content found') }}</h3>
            <p class="empty-subtitle">{{ siteContent.getContent('videos_audio_empty_subtitle', 'Check back later for new content') }}</p>
          </div>

          <!-- Audio List - Podcast Style -->
          <div v-else class="audio-list">
            <article v-for="audio in videos.filter(v => isAudio(v))" :key="audio.id"
              class="audio-card">

              <!-- Waveform Icon Placeholder -->
              <div class="audio-icon-wrapper">
                <div class="waveform-icon">
                  <div class="waveform-bar"></div>
                  <div class="waveform-bar"></div>
                  <div class="waveform-bar"></div>
                  <div class="waveform-bar"></div>
                  <div class="waveform-bar"></div>
                </div>
              </div>

              <!-- Audio Info -->
              <div class="audio-info">
                <h3 class="audio-title">{{ audio.title }}</h3>
                <div class="audio-meta">
                  <span class="audio-author">{{ audio.author_name }}</span>
                  <span class="meta-divider">•</span>
                  <span class="audio-date">
                    {{ formatDate(audio.updated_at || audio.published_at || audio.created_at) }}
                  </span>
                  <span v-if="audio.duration" class="meta-divider">•</span>
                  <span v-if="audio.duration" class="audio-duration">{{ audio.duration }}</span>
                </div>
              </div>

              <!-- Inline Audio Player -->
              <div class="audio-player-wrapper">
                <audio controls class="audio-player">
                  <source :src="audio.video_file" type="audio/mpeg">
                </audio>
              </div>
            </article>
          </div>
        </section>

      </div>
    </div>

    <VideoPlayerModal :isOpen="isModalOpen" :video="selectedVideo" @close="closeModal" />
  </div>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue'
  import { useVideosStore } from '@/store/videos'
  import { useSettingsStore } from '@/store/settings'
  import { useSiteContent } from '@/composables/useSiteContent'
  import VideoPlayerModal from '@/components/videos/VideoPlayerModal.vue'
  import {
    Search,
    Play,
    Video
  } from 'lucide-vue-next'

  defineOptions({
    name: 'VideosPage'
  })

  const videosStore = useVideosStore()
  const settingsStore = useSettingsStore()
  const siteContent = useSiteContent('videos')
  const query = ref('')
  const activeFilter = ref('VIDEOS') // Filter: VIDEOS, AUDIO
  const loading = ref(false)
  const isModalOpen = ref(false)
  const selectedVideo = ref(null)

  const videosSearchPlaceholder = computed(() => settingsStore.settings.videos_search_placeholder || 'Search video archive...')
  const videosSearchButton = computed(() => settingsStore.settings.videos_search_button || 'Search')

  // Filter chips - customizable via CMS
  const filterChips = computed(() => [
    { value: 'VIDEOS', label: siteContent.getContent('videos_filter_videos', 'VIDEOS') },
    { value: 'AUDIO', label: siteContent.getContent('videos_filter_audio', 'AUDIO') }
  ])

  const videos = ref([])

  // Helper function to separate media types for the display logic
  const isAudio = (v) => {
    return v.video_type === 'AUDIO' || (v.video_file && (v.video_file.toLowerCase().endsWith('.mp3') || v.video_file.toLowerCase().endsWith('.m4a') || v.video_file.toLowerCase().endsWith('.wav')))
  }

  // Default to VIDEOS filter
  if (activeFilter.value === 'ALL') {
    activeFilter.value = 'VIDEOS'
  }

  // Filtered computed property still exists for search functionality
  const filteredVideos = computed(() => {
    const q = query.value.trim().toLowerCase()
    return videos.value.filter(v => {
      return !q || v.title.toLowerCase().includes(q) || (v.author_name && v.author_name.toLowerCase().includes(q))
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
        youtube_id: video.youtube_id, // Pass youtube_id directly from API
        video_file: video.video_file,
        video_type: video.video_type || 'YOUTUBE',
        views_count: video.views_count,
        author_name: video.author_name || 'Sauti Uganda',
        category: video.category,
        published_at: video.published_at,
        updated_at: video.updated_at,
        created_at: video.created_at,
        duration: video.duration || null,
        description: video.description || ''
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

    const diffMinutes = Math.floor(diffTime / (1000 * 60))
    const diffHours = Math.floor(diffTime / (1000 * 60 * 60))
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24))

    if (diffMinutes < 1) return 'Just now'
    if (diffMinutes < 60) return `${diffMinutes} minute${diffMinutes !== 1 ? 's' : ''} ago`
    if (diffHours < 24) return `${diffHours} hour${diffHours !== 1 ? 's' : ''} ago`
    if (diffDays === 1) return 'Yesterday'
    if (diffDays < 7) return `${diffDays} days ago`
    if (diffDays < 30) return `${Math.floor(diffDays / 7)} week${Math.floor(diffDays / 7) !== 1 ? 's' : ''} ago`
    if (diffDays < 365) return `${Math.floor(diffDays / 30)} month${Math.floor(diffDays / 30) !== 1 ? 's' : ''} ago`
    return `${Math.floor(diffDays / 365)} year${Math.floor(diffDays / 365) !== 1 ? 's' : ''} ago`
  }

  onMounted(async () => {
    await siteContent.fetchContent()
    await settingsStore.fetchGlobalSettings()
    fetchVideos()
  })
</script>

<style scoped>
  /* ===== HERO BANNER ===== */
  .hero-banner {
    position: relative;
    background: linear-gradient(135deg, rgb(var(--color-secondary)) 0%, rgb(var(--color-primary-dark)) 100%);
    min-height: clamp(200px, 25vh, 300px);
    display: flex;
    align-items: center;
    overflow: hidden;
    margin-top: 0;
  }

  .hero-overlay {
    position: absolute;
    inset: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800"><defs><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1"/></pattern></defs><rect width="1200" height="800" fill="url(%23grid)"/></svg>');
    opacity: 0.5;
  }

  .hero-content-wrapper {
    position: relative;
    z-index: 2;
    padding: clamp(1.25rem, 3vh, 2.5rem) 0;
  }

  .hero-text {
    text-align: center;
    margin-bottom: clamp(0.75rem, 2vw, 1rem);
  }

  .hero-title {
    font-size: clamp(1rem, 2vw, 1.75rem);
    font-weight: 900;
    color: white;
    margin-bottom: 0.375rem;
    line-height: 1.1;
    letter-spacing: -0.02em;
  }

  .text-accent-yellow {
    color: rgb(var(--color-accent-yellow));
  }

  .hero-subtitle {
    font-size: clamp(0.75rem, 0.9vw, 0.875rem);
    color: rgba(255, 255, 255, 0.85);
    max-width: 600px;
    margin: 0 auto;
    font-weight: 400;
    line-height: 1.4;
    padding: 0 1rem;
  }

  /* ===== INLINE SEARCH ===== */
  .search-box {
    max-width: 600px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    background: rgb(var(--color-neutral-offwhite));
    border-radius: 9999px;
    padding: 0.5rem 0.75rem;
    gap: 0.5rem;
  }

  .search-icon-inline {
    width: 1.125rem;
    height: 1.125rem;
    color: rgb(var(--color-primary));
    flex-shrink: 0;
  }

  .search-input-inline {
    flex: 1;
    border: none;
    outline: none;
    font-size: 0.875rem;
    font-weight: 500;
    color: rgb(var(--color-secondary));
    background: transparent;
    padding: 0.25rem 0.5rem;
    min-width: 0;
  }

  .search-input-inline::placeholder {
    color: rgba(0, 0, 0, 0.4);
  }

  .search-btn-inline {
    background: rgb(var(--color-primary));
    color: white;
    font-weight: 600;
    border: none;
    border-radius: 9999px;
    padding: 0.5rem 1.25rem;
    font-size: 0.875rem;
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
    flex-shrink: 0;
  }

  .search-btn-inline:hover {
    background: rgb(var(--color-primary-dark));
  }

  @media (max-width: 640px) {
    .search-btn-inline {
      padding: 0.5rem 1rem;
      font-size: 0.8125rem;
    }
  }

  /* ===== FILTER TABS ===== */
  .filter-tabs-wrapper {
    display: flex;
    gap: 0.75rem;
    padding: 1rem 0;
    overflow-x: auto;
    scrollbar-width: none;
    -ms-overflow-style: none;
    -webkit-overflow-scrolling: touch;
  }

  .filter-tabs-wrapper::-webkit-scrollbar {
    display: none;
  }

  .filter-chip {
    padding: 0.75rem 2rem;
    border-radius: 2rem;
    font-weight: 700;
    font-size: 0.875rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    border: 2px solid transparent;
    transition: all 0.3s ease;
    cursor: pointer;
    white-space: nowrap;
    min-height: 44px;
    min-width: 80px;
    touch-action: manipulation;
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }

  @media (max-width: 640px) {
    .filter-tabs-wrapper {
      gap: 0.5rem;
      padding: 0.75rem 0;
    }

    .filter-chip {
      padding: 0.625rem 1.25rem;
      font-size: 0.8125rem;
      min-width: 70px;
    }
  }

  .filter-chip-active {
    background: rgb(var(--color-primary));
    color: white;
    box-shadow: 0 4px 12px rgba(0, 135, 207, 0.3);
  }

  .filter-chip-inactive {
    background: white;
    color: rgb(var(--color-secondary));
    border-color: rgb(var(--color-secondary) / 0.2);
  }

  .filter-chip-inactive:hover {
    border-color: rgb(var(--color-primary));
    background: rgb(var(--color-primary) / 0.05);
  }

  /* ===== SECTION HEADERS ===== */
  .section-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid rgb(var(--color-neutral-offwhite));
  }

  .section-badge {
    width: 4px;
    height: 2rem;
    background: rgb(var(--color-primary));
    border-radius: 1rem;
  }

  .section-title {
    font-size: clamp(1.125rem, 1.75vw, 1.5rem);
    font-weight: 800;
    color: rgb(var(--color-secondary));
    text-transform: uppercase;
    letter-spacing: 0.02em;
  }

  /* ===== VIDEO CARDS - BLOG STYLE ===== */
  .video-card {
    background: transparent;
    border-radius: 0;
    overflow: visible;
    transition: transform 0.2s ease;
    cursor: pointer;
  }

  .video-card:hover {
    transform: translateY(-4px);
  }

  .video-thumbnail-wrapper {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    background: rgb(var(--color-neutral-offwhite));
    border-radius: 0.75rem;
    margin-bottom: 0.75rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  }

  @media (max-width: 640px) {
    .video-card:hover {
      transform: translateY(-2px);
    }

    .video-thumbnail-wrapper {
      border-radius: 0.5rem;
      margin-bottom: 0.5rem;
    }
  }

  .video-thumbnail {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: all 0.3s ease;
  }

  .video-card:hover .video-thumbnail {
    transform: scale(1.05);
    filter: brightness(1.1);
  }

  .video-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(0, 0, 0, 0.4) 0%, transparent 50%);
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .video-card:hover .video-overlay {
    opacity: 1;
  }

  .play-button-wrapper {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    transform: scale(0.8);
    opacity: 0;
    transition: all 0.3s ease;
  }

  .video-card:hover .play-button-wrapper {
    transform: scale(1);
    opacity: 1;
  }

  .play-button {
    background: white;
    width: 3rem;
    height: 3rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
  }

  .play-icon {
    width: 1.5rem;
    height: 1.5rem;
    color: rgb(var(--color-primary));
    fill: rgb(var(--color-primary));
    margin-left: 0.15rem;
  }

  @media (max-width: 640px) {
    .play-button {
      width: 2.5rem;
      height: 2.5rem;
    }

    .play-icon {
      width: 1.25rem;
      height: 1.25rem;
    }
  }

  .duration-badge {
    position: absolute;
    bottom: 0.5rem;
    right: 0.5rem;
    background: rgba(0, 0, 0, 0.85);
    color: white;
    font-size: 0.6875rem;
    font-weight: 600;
    padding: 0.25rem 0.5rem;
    border-radius: 0.25rem;
    backdrop-filter: blur(4px);
  }

  .video-info {
    padding: 0 0.25rem;
    display: flex;
    flex-direction: column;
    gap: 0.375rem;
  }

  .video-title {
    font-size: clamp(0.875rem, 1.25vw, 1rem);
    font-weight: 700;
    color: rgb(var(--color-secondary));
    line-height: 1.3;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    transition: color 0.2s ease;
  }

  .video-card:hover .video-title {
    color: rgb(var(--color-primary));
  }

  .video-date {
    font-size: 0.75rem;
    color: rgba(0, 0, 0, 0.6);
    font-weight: 500;
  }

  @media (max-width: 640px) {
    .video-info {
      padding: 0 0.125rem;
      gap: 0.25rem;
    }

    .video-title {
      font-size: 0.8125rem;
      -webkit-line-clamp: 1;
    }

    .video-date {
      font-size: 0.6875rem;
    }

    .duration-badge {
      font-size: 0.625rem;
      padding: 0.2rem 0.4rem;
    }
  }

  .video-card:hover .video-title {
    color: rgb(var(--color-primary));
  }


  /* ===== AUDIO CARDS - PODCAST STYLE ===== */
  .audio-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .audio-card {
    display: flex;
    align-items: center;
    gap: 1rem;
    background: white;
    padding: 1.25rem;
    border-radius: 1rem;
    border: 1px solid rgb(var(--color-neutral-offwhite));
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    transition: all 0.3s ease;
  }

  .audio-card:hover {
    box-shadow: 0 8px 24px rgba(0, 104, 55, 0.15);
    border-color: rgb(var(--color-secondary) / 0.3);
    transform: translateX(4px);
  }

  .audio-icon-wrapper {
    flex-shrink: 0;
    width: 3.5rem;
    height: 3.5rem;
    background: rgb(var(--color-secondary) / 0.1);
    border-radius: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  @media (max-width: 640px) {
    .audio-list {
      gap: 0.75rem;
    }

    .audio-card {
      padding: 1rem;
      gap: 0.75rem;
    }

    .audio-icon-wrapper {
      width: 3rem;
      height: 3rem;
    }
  }

  @media (max-width: 480px) {
    .audio-icon-wrapper {
      display: none;
    }
  }

  .waveform-icon {
    display: flex;
    align-items: center;
    gap: 0.25rem;
    height: 2rem;
  }

  .waveform-bar {
    width: 0.25rem;
    background: rgb(var(--color-secondary));
    border-radius: 0.125rem;
    animation: wave 1s ease-in-out infinite;
  }

  .waveform-bar:nth-child(1) { height: 40%; animation-delay: 0s; }
  .waveform-bar:nth-child(2) { height: 70%; animation-delay: 0.1s; }
  .waveform-bar:nth-child(3) { height: 100%; animation-delay: 0.2s; }
  .waveform-bar:nth-child(4) { height: 60%; animation-delay: 0.3s; }
  .waveform-bar:nth-child(5) { height: 80%; animation-delay: 0.4s; }

  @keyframes wave {
    0%, 100% { transform: scaleY(1); }
    50% { transform: scaleY(0.5); }
  }

  .audio-info {
    flex: 1;
    min-width: 0;
  }

  .audio-title {
    font-size: clamp(0.9375rem, 1.5vw, 1.125rem);
    font-weight: 700;
    color: rgb(var(--color-secondary));
    line-height: 1.4;
    margin-bottom: 0.5rem;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    transition: color 0.3s ease;
  }

  .audio-card:hover .audio-title {
    color: rgb(var(--color-primary));
  }

  .audio-meta {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-wrap: wrap;
    font-size: clamp(0.75rem, 1.25vw, 0.875rem);
  }

  .audio-author {
    color: rgba(0, 0, 0, 0.7);
    font-weight: 600;
  }

  .audio-date,
  .audio-duration {
    color: rgba(0, 0, 0, 0.5);
    font-weight: 500;
  }

  @media (max-width: 480px) {
    .audio-duration {
      display: none;
    }
  }

  .audio-player-wrapper {
    flex-shrink: 0;
    width: 100%;
    max-width: 320px;
  }

  .audio-player {
    width: 100%;
    height: 2.5rem;
    border-radius: 0.5rem;
  }

  @media (max-width: 768px) {
    .audio-card {
      flex-direction: column;
      align-items: flex-start;
      gap: 0.875rem;
    }

    .audio-player-wrapper {
      max-width: 100%;
    }

    .audio-player {
      width: 100%;
    }

    .audio-title {
      white-space: normal;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
    }
  }

  @media (max-width: 480px) {
    .audio-card {
      gap: 0.75rem;
    }
  }

  /* ===== SKELETON LOADERS ===== */
  .skeleton-card {
    background: transparent;
    border-radius: 0;
    overflow: visible;
  }

  .skeleton-thumbnail {
    width: 100%;
    aspect-ratio: 16 / 9;
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
    background-size: 200% 100%;
    animation: shimmer 1.5s infinite;
    border-radius: 0.75rem;
    margin-bottom: 0.75rem;
  }

  .skeleton-content {
    padding: 0 0.25rem;
  }

  .skeleton-title {
    height: 1rem;
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
    background-size: 200% 100%;
    border-radius: 0.25rem;
    animation: shimmer 1.5s infinite;
  }

  @media (max-width: 640px) {
    .skeleton-thumbnail {
      border-radius: 0.5rem;
      margin-bottom: 0.5rem;
    }
  }

  @keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
  }

  /* ===== EMPTY STATE ===== */
  .empty-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 4rem 2rem;
    text-align: center;
    background: rgb(var(--color-neutral-offwhite));
    border-radius: 2rem;
  }

  .empty-icon {
    width: 4rem;
    height: 4rem;
    color: rgb(var(--color-primary) / 0.3);
    margin-bottom: 1.5rem;
  }

  .empty-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: rgb(var(--color-secondary));
    margin-bottom: 0.5rem;
  }

  .empty-subtitle {
    font-size: 1rem;
    color: rgba(0, 0, 0, 0.5);
  }
</style>