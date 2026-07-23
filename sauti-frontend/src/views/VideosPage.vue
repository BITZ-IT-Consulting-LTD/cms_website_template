<template>
  <div class="min-h-screen bg-white">
    <!-- Hero Banner -->
    <header class="hero-banner" style="padding-top: clamp(70px, 15vw, 90px);">
      <div class="hero-overlay"></div>
      <div class="container-custom hero-content-wrapper">
        <div class="hero-text">
          <h1 class="hero-title">
            {{ siteContent.getContent('videos_page_title', 'Video Gallery') }}
            <span class="text-accent-yellow">{{ siteContent.getContent('videos_page_title_highlight', 'Audio-Visuals') }}</span>
          </h1>
          <p class="hero-subtitle">
            {{ siteContent.getContent('videos_page_description', 'Explore our archive of official media content, awareness videos, and community stories.') }}
          </p>
        </div>
      </div>
    </header>

    <section class="bg-warm">
      <div class="container-custom section-padding !pt-10 md:!pt-14">
        <!-- Search -->
        <div class="max-w-3xl mx-auto mb-6 md:mb-8">
          <h2 class="text-center text-sm lg:text-base font-bold text-secondary/70 mb-4 tracking-tight">
            {{ siteContent.getContent('videos_search_heading', 'Search Official Media') }}
          </h2>
          <div class="search-shell relative flex items-center gap-2 bg-neutral-white rounded-2xl lg:rounded-[1.75rem] border border-black/5 shadow-sm focus-within:ring-2 focus-within:ring-primary/25 transition-all">
            <div class="pl-5 lg:pl-6 flex items-center pointer-events-none">
              <Search class="h-5 w-5 text-primary/40" />
            </div>
            <input
              v-model="query"
              @input="applySearch"
              type="search"
              :placeholder="siteContent.getContent('videos_search_placeholder', videosSearchPlaceholder)"
              class="flex-1 min-w-0 py-4 lg:py-5 pr-2 bg-transparent text-secondary font-semibold placeholder:text-black/30 focus:outline-none text-sm lg:text-base border-none"
            />
            <button
              type="button"
              class="shrink-0 mr-2 lg:mr-3 px-5 lg:px-6 py-2.5 lg:py-3 bg-primary text-neutral-white rounded-full font-bold text-xs lg:text-sm uppercase tracking-wider hover:brightness-110 transition-all"
              @click="applySearch"
            >
              {{ siteContent.getContent('videos_search_button', videosSearchButton) }}
            </button>
          </div>
        </div>

        <!-- Section jump chips -->
        <div class="mb-8 md:mb-10 sticky top-[70px] z-30 -mx-4 px-4 py-3 bg-warm/95 backdrop-blur-md sm:static sm:bg-transparent sm:backdrop-blur-none sm:p-0 sm:mx-0">
          <div class="flex flex-wrap gap-2.5 justify-center sm:justify-start">
            <button
              v-for="chip in filterChips"
              :key="chip.value"
              type="button"
              @click="scrollToSection(chip.value)"
              class="chip chip-idle"
            >
              {{ chip.label }}
            </button>
          </div>
        </div>

        <!-- Loading -->
        <div v-if="loading" class="space-y-8 sm:space-y-12">
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5 sm:gap-6">
            <div v-for="n in 8" :key="n" class="skeleton-card">
              <div class="skeleton-thumbnail"></div>
              <div class="skeleton-content">
                <div class="skeleton-title"></div>
                <div class="skeleton-meta"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Content -->
        <div v-else class="space-y-14 lg:space-y-16">
          <!-- Videos -->
          <section ref="videosSectionRef" class="scroll-section" aria-label="Video Gallery">
            <div class="section-header">
              <div class="section-badge" aria-hidden="true"></div>
              <h2 class="section-title">{{ siteContent.getContent('videos_section_title', 'Videos') }}</h2>
            </div>

            <div v-if="videoItems.length === 0" class="empty-state">
              <Video class="empty-icon" />
              <h3 class="empty-title">{{ siteContent.getContent('videos_empty_title', 'No videos found') }}</h3>
              <p class="empty-subtitle">{{ siteContent.getContent('videos_empty_subtitle', 'Check back later for new content') }}</p>
            </div>

            <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5 sm:gap-6">
              <article
                v-for="video in videoItems"
                :key="video.id"
                class="video-card group cursor-pointer"
                @click="openVideo(video)"
              >
                <div class="video-thumbnail-wrapper">
                  <img
                    :src="video.thumbnail"
                    :alt="video.title"
                    class="video-thumbnail"
                    loading="lazy"
                    @error="useThumbPlaceholder($event)"
                  />
                  <div class="video-overlay"></div>
                  <div class="play-button-wrapper">
                    <div class="play-button">
                      <Play class="play-icon" />
                    </div>
                  </div>
                  <span v-if="video.duration" class="duration-badge">{{ video.duration }}</span>
                </div>

                <div class="video-info">
                  <h3 class="video-title">{{ video.title }}</h3>
                  <p class="video-date">
                    {{ formatDate(video.updated_at || video.published_at || video.created_at) }}
                  </p>
                </div>
              </article>
            </div>
          </section>

          <!-- Audio -->
          <section ref="audioSectionRef" class="scroll-section" aria-label="Audio Gallery">
            <div class="section-header">
              <div class="section-badge" aria-hidden="true"></div>
              <h2 class="section-title">{{ siteContent.getContent('videos_audio_section_title', 'Audio') }}</h2>
            </div>

            <div v-if="audioItems.length === 0" class="empty-state">
              <Play class="empty-icon" />
              <h3 class="empty-title">{{ siteContent.getContent('videos_audio_empty_title', 'No audio content found') }}</h3>
              <p class="empty-subtitle">{{ siteContent.getContent('videos_audio_empty_subtitle', 'Check back later for new content') }}</p>
            </div>

            <div v-else class="audio-list">
              <article v-for="audio in audioItems" :key="audio.id" class="audio-card">
                <div class="audio-icon-wrapper">
                  <div class="waveform-icon" aria-hidden="true">
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                  </div>
                </div>

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
    </section>

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
  const loading = ref(false)
  const isModalOpen = ref(false)
  const selectedVideo = ref(null)
  const videosSectionRef = ref(null)
  const audioSectionRef = ref(null)

  const videosSearchPlaceholder = computed(() => settingsStore.settings.videos_search_placeholder || 'Search video archive...')
  const videosSearchButton = computed(() => settingsStore.settings.videos_search_button || 'Search')

  const filterChips = computed(() => [
    { value: 'VIDEOS', label: siteContent.getContent('videos_filter_videos', 'VIDEOS') },
    { value: 'AUDIO', label: siteContent.getContent('videos_filter_audio', 'AUDIO') }
  ])

  const videos = ref([])

  const isAudio = (v) => {
    return v.video_type === 'AUDIO' || (v.video_file && (v.video_file.toLowerCase().endsWith('.mp3') || v.video_file.toLowerCase().endsWith('.m4a') || v.video_file.toLowerCase().endsWith('.wav')))
  }

  const filteredVideos = computed(() => {
    const q = query.value.trim().toLowerCase()
    return videos.value.filter(v => {
      return !q || v.title.toLowerCase().includes(q) || (v.author_name && v.author_name.toLowerCase().includes(q))
    })
  })

  const videoItems = computed(() => filteredVideos.value.filter(v => !isAudio(v)))
  const audioItems = computed(() => filteredVideos.value.filter(v => isAudio(v)))

  async function fetchVideos() {
    loading.value = true
    try {
      await videosStore.fetchVideos({ status: 'PUBLISHED' })
      videos.value = videosStore.videos.map(video => ({
        id: video.id,
        title: video.title,
        thumbnail: video.thumbnail || video.youtube_thumbnail_url || 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?q=80&w=1200&auto=format&fit=crop',
        youtube_url: video.youtube_url,
        youtube_id: video.youtube_id,
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

  const applySearch = () => { }

  const scrollToSection = (section) => {
    const target = section === 'AUDIO' ? audioSectionRef.value : videosSectionRef.value
    target?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }

  const useThumbPlaceholder = (e) => {
    e.target.src = 'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?q=80&w=640&auto=format&fit=crop'
  }

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
  .chip {
    @apply px-5 py-2.5 rounded-full text-[11px] font-bold uppercase tracking-wider whitespace-nowrap transition-all duration-300 flex-shrink-0 border-2;
  }

  .chip-idle {
    @apply bg-neutral-white border-transparent text-secondary/60 hover:border-primary/30 hover:text-primary shadow-sm;
  }

  .scroll-section {
    scroll-margin-top: 150px;
  }

  .section-header {
    display: flex;
    align-items: center;
    gap: 0.875rem;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid rgb(var(--color-neutral-white) / 0.8);
  }

  .section-badge {
    width: 4px;
    height: 1.75rem;
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

  .video-card {
    transition: transform 0.3s ease;
  }

  .video-card:hover {
    transform: translateY(-6px);
  }

  .video-thumbnail-wrapper {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    background: rgb(var(--color-neutral-offwhite));
    border-radius: 1.25rem;
    margin-bottom: 0.875rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.06);
  }

  .video-thumbnail {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease, filter 0.3s ease;
  }

  .video-card:hover .video-thumbnail {
    transform: scale(1.05);
    filter: brightness(1.08);
  }

  .video-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(0, 0, 0, 0.45) 0%, transparent 55%);
    opacity: 0.65;
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
    transform: scale(0.85);
    opacity: 0;
    transition: all 0.3s ease;
  }

  .video-card:hover .play-button-wrapper {
    transform: scale(1);
    opacity: 1;
  }

  .play-button {
    background: white;
    width: 3.25rem;
    height: 3.25rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
  }

  .play-icon {
    width: 1.5rem;
    height: 1.5rem;
    color: rgb(var(--color-primary));
    fill: rgb(var(--color-primary));
    margin-left: 0.15rem;
  }

  .duration-badge {
    position: absolute;
    bottom: 0.625rem;
    right: 0.625rem;
    background: rgba(0, 0, 0, 0.8);
    color: white;
    font-size: 0.6875rem;
    font-weight: 700;
    padding: 0.3rem 0.55rem;
    border-radius: 0.5rem;
    backdrop-filter: blur(4px);
  }

  .video-info {
    padding: 0 0.25rem;
    display: flex;
    flex-direction: column;
    gap: 0.375rem;
  }

  .video-title {
    font-size: clamp(0.9375rem, 1.25vw, 1.0625rem);
    font-weight: 700;
    color: rgb(var(--color-secondary));
    line-height: 1.35;
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
    color: rgba(0, 0, 0, 0.45);
    font-weight: 600;
  }

  .audio-list {
    display: flex;
    flex-direction: column;
    gap: 0.875rem;
  }

  .audio-card {
    display: flex;
    align-items: center;
    gap: 1rem;
    background: white;
    padding: 1.25rem 1.5rem;
    border-radius: 1.5rem;
    border: 1px solid rgba(0, 0, 0, 0.04);
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
    transition: all 0.3s ease;
  }

  .audio-card:hover {
    box-shadow: 0 10px 28px rgba(0, 104, 55, 0.1);
    border-color: rgb(var(--color-primary) / 0.2);
    transform: translateY(-2px);
  }

  .audio-icon-wrapper {
    flex-shrink: 0;
    width: 3.5rem;
    height: 3.5rem;
    background: rgb(var(--color-secondary) / 0.08);
    border-radius: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
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
    margin-bottom: 0.375rem;
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
    color: rgba(0, 0, 0, 0.65);
    font-weight: 600;
  }

  .audio-date,
  .audio-duration {
    color: rgba(0, 0, 0, 0.45);
    font-weight: 500;
  }

  .meta-divider {
    color: rgba(0, 0, 0, 0.25);
  }

  .audio-player-wrapper {
    flex-shrink: 0;
    width: 100%;
    max-width: 320px;
  }

  .audio-player {
    width: 100%;
    height: 2.5rem;
    border-radius: 0.75rem;
  }

  .skeleton-card {
    background: transparent;
  }

  .skeleton-thumbnail {
    width: 100%;
    aspect-ratio: 16 / 9;
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
    background-size: 200% 100%;
    animation: shimmer 1.5s infinite;
    border-radius: 1.25rem;
    margin-bottom: 0.875rem;
  }

  .skeleton-content {
    padding: 0 0.25rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .skeleton-title {
    height: 1rem;
    width: 85%;
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
    background-size: 200% 100%;
    border-radius: 0.25rem;
    animation: shimmer 1.5s infinite;
  }

  .skeleton-meta {
    height: 0.75rem;
    width: 45%;
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
    background-size: 200% 100%;
    border-radius: 0.25rem;
    animation: shimmer 1.5s infinite;
  }

  @keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
  }

  .empty-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 3.5rem 2rem;
    text-align: center;
    background: white;
    border-radius: 1.75rem;
    border: 1px dashed rgba(0, 0, 0, 0.1);
  }

  .empty-icon {
    width: 3.5rem;
    height: 3.5rem;
    color: rgb(var(--color-primary) / 0.35);
    margin-bottom: 1.25rem;
  }

  .empty-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: rgb(var(--color-secondary));
    margin-bottom: 0.5rem;
  }

  .empty-subtitle {
    font-size: 0.9375rem;
    color: rgba(0, 0, 0, 0.45);
    font-weight: 600;
  }

  @media (max-width: 768px) {
    .audio-card {
      flex-direction: column;
      align-items: flex-start;
      gap: 0.875rem;
      border-radius: 1.25rem;
      padding: 1.125rem;
    }

    .audio-player-wrapper {
      max-width: 100%;
    }

    .audio-title {
      white-space: normal;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
    }
  }

  @media (max-width: 480px) {
    .audio-icon-wrapper {
      display: none;
    }

    .audio-duration {
      display: none;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .video-card,
    .audio-card,
    .waveform-bar,
    .play-button-wrapper,
    .video-thumbnail {
      transition: none !important;
      animation: none !important;
    }

    .video-card:hover,
    .audio-card:hover {
      transform: none;
    }
  }
</style>
