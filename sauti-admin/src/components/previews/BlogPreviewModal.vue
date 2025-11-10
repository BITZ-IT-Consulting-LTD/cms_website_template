<template>
  <Teleport to="body">
    <Transition name="modal">
      <div
        v-if="isOpen"
        class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm"
        @click.self="close"
      >
        <div class="relative w-full max-w-6xl bg-white rounded-xl shadow-2xl overflow-hidden" style="height: 90vh;">
          <!-- Header -->
          <div class="flex items-center justify-between p-4 border-b border-gray-200 bg-gray-50">
            <div class="flex items-center space-x-3">
              <div class="w-3 h-3 rounded-full bg-red-500"></div>
              <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
              <div class="w-3 h-3 rounded-full bg-green-500"></div>
              <h3 class="ml-4 text-lg font-semibold text-gray-900">Blog Post Preview</h3>
            </div>
            <div class="flex items-center space-x-2">
              <button
                @click="openInNewTab"
                class="px-3 py-1.5 text-sm text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md transition-colors"
                title="Open in new tab"
              >
                <svg class="w-4 h-4 inline mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
                Open in Tab
              </button>
              <button
                @click="close"
                class="p-2 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-full transition-colors"
                aria-label="Close preview"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
          </div>

          <!-- Preview Content -->
          <div class="h-full overflow-hidden">
            <iframe
              v-if="previewUrl"
              :src="previewUrl"
              class="w-full h-full border-0"
              frameborder="0"
              allowfullscreen
              @load="handleLoad"
              @error="handleError"
            ></iframe>
            <div v-else class="flex items-center justify-center h-full bg-gray-50">
              <div class="text-center">
                <svg class="w-16 h-16 mx-auto mb-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                <p class="text-lg text-gray-600">Loading preview...</p>
              </div>
            </div>
          </div>

          <!-- Loading Indicator -->
          <div v-if="loading" class="absolute inset-0 flex items-center justify-center bg-white/80">
            <div class="text-center">
              <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-[#8B4000] mx-auto mb-4"></div>
              <p class="text-gray-600">Loading preview...</p>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { ref, watch, computed } from 'vue'

const props = defineProps({
  isOpen: {
    type: Boolean,
    default: false
  },
  slug: {
    type: String,
    default: ''
  },
  postId: {
    type: [String, Number],
    default: null
  }
})

const emit = defineEmits(['close'])

const loading = ref(true)

// Frontend URL - adjust port if needed
const frontendUrl = import.meta.env.VITE_FRONTEND_URL || 'http://localhost:3000'

const previewUrl = computed(() => {
  if (!props.slug && !props.postId) return ''
  
  // Use slug if available, otherwise use ID
  const identifier = props.slug || props.postId
  return `${frontendUrl}/blog/${identifier}?preview=true`
})

const close = () => {
  loading.value = true
  emit('close')
}

const openInNewTab = () => {
  if (previewUrl.value) {
    window.open(previewUrl.value, '_blank')
  }
}

const handleLoad = () => {
  loading.value = false
}

const handleError = () => {
  loading.value = false
  console.error('Failed to load preview')
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

