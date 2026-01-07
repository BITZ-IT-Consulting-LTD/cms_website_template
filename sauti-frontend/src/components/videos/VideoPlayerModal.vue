<template>
  <Teleport to="body">
    <Transition name="modal">
      <div
        v-if="isOpen"
        class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm"
        @click.self="close"
      >
        <div class="relative w-full max-w-5xl bg-white rounded-xl shadow-2xl overflow-hidden">
          <!-- Close Button -->
          <button
            @click="close"
            class="absolute top-4 right-4 z-10 p-2 bg-black/50 hover:bg-black/70 rounded-full text-white transition-colors"
            aria-label="Close video player"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>

          <!-- Video Player -->
          <div class="relative bg-black aspect-video">
            <!-- YouTube Video -->
            <div v-if="video.youtube_url && video.video_type === 'YOUTUBE'" class="w-full h-full">
              <iframe
                :src="getYouTubeEmbedUrl(video.youtube_url)"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
                class="w-full h-full"
              ></iframe>
            </div>

            <!-- Uploaded Video File -->
            <video
              v-else-if="video.video_file || (video.video_type === 'UPLOAD' && video.id)"
              :src="getVideoFileUrl(video)"
              controls
              class="w-full h-full"
              @loadstart="handleVideoLoad"
              @error="handleVideoError"
            >
              Your browser does not support the video tag.
            </video>

            <!-- Fallback Message -->
            <div v-else class="flex items-center justify-center h-full text-white">
              <div class="text-center">
                <svg class="w-16 h-16 mx-auto mb-4 text-secondary/40" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
                </svg>
                <p class="text-lg">Video not available</p>
              </div>
            </div>
          </div>

          <!-- Video Info -->
          <div class="p-6">
            <h2 class="text-2xl font-bold text-secondary mb-2">{{ video.title }}</h2>
            <div class="flex items-center gap-4 text-sm text-secondary/60 mb-4">
              <span v-if="video.views_count">{{ formatViews(video.views_count) }}</span>
              <span v-if="video.published_at">{{ formatDate(video.published_at) }}</span>
              <span v-if="video.author_name">by {{ video.author_name }}</span>
            </div>
            <p v-if="video.description" class="text-secondary/70 leading-relaxed">{{ video.description }}</p>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { watch } from 'vue'

const props = defineProps({
  isOpen: {
    type: Boolean,
    default: false
  },
  video: {
    type: Object,
    default: () => ({})
  }
})

const emit = defineEmits(['close'])

const close = () => {
  emit('close')
}

const getYouTubeEmbedUrl = (url) => {
  if (!url) return ''
  
  // Extract YouTube video ID from various URL formats
  const patterns = [
    /(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)/,
    /youtube\.com\/v\/([^&\n?#]+)/
  ]
  
  for (const pattern of patterns) {
    const match = url.match(pattern)
    if (match) {
      return `https://www.youtube.com/embed/${match[1]}?autoplay=1&rel=0`
    }
  }
  
  return url
}

const getVideoFileUrl = (video) => {
  // If video_file is a URL string, use it directly
  if (typeof video.video_file === 'string') {
    // If it's already a full URL, use it
    if (video.video_file.startsWith('http://') || video.video_file.startsWith('https://')) {
      return video.video_file
    }
    // If it's a relative path, prepend the API URL
    const apiUrl = import.meta.env.VITE_API_URL || '/api'
    // Remove leading slash if present to avoid double slashes
    const path = video.video_file.startsWith('/') ? video.video_file.slice(1) : video.video_file
    return `${apiUrl}/${path}`
  }
  
  // If we have video_file URL from backend response
  if (video.video_file_url) {
    return video.video_file_url
  }
  
  // Fallback: construct URL from video ID (if backend supports this)
  if (video.id) {
    const apiUrl = import.meta.env.VITE_API_URL || '/api'
    return `${apiUrl}/videos/${video.id}/video/`
  }
  
  return ''
}

const formatViews = (views) => {
  if (!views) return '0 views'
  if (views >= 1000000) {
    return `${(views / 1000000).toFixed(1)}M views`
  } else if (views >= 1000) {
    return `${(views / 1000).toFixed(1)}K views`
  }
  return `${views} views`
}

const formatDate = (dateString) => {
  if (!dateString) return ''
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

const handleVideoLoad = () => {
  console.log('Video loading...')
}

const handleVideoError = (error) => {
  console.error('Video load error:', error)
}

// Close on Escape key
watch(() => props.isOpen, (isOpen) => {
  if (isOpen) {
    const handleEscape = (e) => {
      if (e.key === 'Escape') {
        close()
      }
    }
    document.addEventListener('keydown', handleEscape)
    // Prevent body scroll when modal is open
    document.body.style.overflow = 'hidden'
    
    return () => {
      document.removeEventListener('keydown', handleEscape)
      document.body.style.overflow = ''
    }
  } else {
    document.body.style.overflow = ''
  }
})
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-active .relative,
.modal-leave-active .relative {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.modal-enter-from .relative,
.modal-leave-to .relative {
  transform: scale(0.9);
  opacity: 0;
}
</style>

