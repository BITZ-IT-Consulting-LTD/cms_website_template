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
              <h3 class="ml-4 text-lg font-semibold text-gray-900">{{ resourceTitle || 'Resource Preview' }}</h3>
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
            <!-- PDF Viewer -->
            <iframe
              v-if="isPdf && previewUrl"
              :src="previewUrl"
              class="w-full h-full border-0"
              frameborder="0"
              type="application/pdf"
              @load="handleLoad"
              @error="handleError"
            ></iframe>
            
            <!-- Image Viewer -->
            <div v-else-if="isImage && previewUrl" class="h-full flex items-center justify-center bg-gray-50 overflow-auto">
              <img
                :src="previewUrl"
                :alt="resourceTitle || 'Resource Preview'"
                class="max-w-full max-h-full object-contain"
                @load="handleLoad"
                @error="handleError"
              />
            </div>

            <!-- Audio Player -->
            <div v-else-if="isAudio && previewUrl" class="h-full flex items-center justify-center bg-gray-50">
              <audio :src="previewUrl" controls class="w-11/12" @canplay="handleLoad" @error="handleError"></audio>
            </div>
            
            <!-- Text/HTML Viewer -->
            <iframe
              v-else-if="isText && previewUrl"
              :src="previewUrl"
              class="w-full h-full border-0"
              frameborder="0"
              @load="handleLoad"
              @error="handleError"
            ></iframe>
            
            <!-- Office Documents (DOCX, DOC, XLSX, etc.) -->
            <div v-else-if="isOfficeDocument && previewUrl" class="h-full flex items-center justify-center bg-gray-50">
              <div class="text-center p-8">
                <svg class="w-16 h-16 mx-auto mb-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                </svg>
                <p class="text-lg text-gray-600 mb-2">Office Document Preview</p>
                <p class="text-sm text-gray-500 mb-4">This document type cannot be previewed directly in the browser</p>
                <div class="flex gap-3 justify-center">
                  <button
                    @click="downloadFile"
                    class="px-4 py-2 bg-[#8B4000] text-white rounded-lg hover:bg-[#A0522D] transition-colors flex items-center"
                  >
                    <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                    </svg>
                    Download File
                  </button>
                  <button
                    @click="openInNewTab"
                    class="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-colors flex items-center"
                  >
                    <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                    </svg>
                    Open in New Tab
                  </button>
                </div>
              </div>
            </div>
            
            <!-- Other file types - try to show in iframe -->
            <iframe
              v-else-if="previewUrl"
              :src="previewUrl"
              class="w-full h-full border-0"
              frameborder="0"
              @load="handleLoad"
              @error="handleError"
            ></iframe>
            
            <!-- Fallback -->
            <div v-else class="flex items-center justify-center h-full bg-gray-50">
              <div class="text-center">
                <svg class="w-16 h-16 mx-auto mb-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                </svg>
                <p class="text-lg text-gray-600 mb-2">Preview not available</p>
                <p class="text-sm text-gray-500 mb-4">This file type cannot be previewed in the browser</p>
                <button
                  v-if="resourceFile"
                  @click="downloadFile"
                  class="px-4 py-2 bg-[#8B4000] text-white rounded-lg hover:bg-[#A0522D] transition-colors"
                >
                  <svg class="w-4 h-4 inline mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                  </svg>
                  Download File
                </button>
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
import { ref, watch, computed, onMounted } from 'vue'

const props = defineProps({
  isOpen: {
    type: Boolean,
    default: false,
    required: true
  },
  slug: {
    type: String,
    default: ''
  },
  resourceId: {
    type: [String, Number],
    default: null
  },
  fileType: {
    type: String,
    default: ''
  },
  fileUrl: {
    type: String,
    default: ''
  },
  resourceTitle: {
    type: String,
    default: 'Resource'
  }
})

const emit = defineEmits(['close'])

const loading = ref(true)

// Watch props.isOpen to ensure reactivity
const isOpen = computed(() => props.isOpen)

const backendUrl = import.meta.env.VITE_BACKEND_URL || ''



const isPdf = computed(() => {
  return props.fileType?.toLowerCase() === 'pdf' || props.fileUrl?.toLowerCase().endsWith('.pdf')
})

const isImage = computed(() => {
  const imageTypes = ['jpg', 'jpeg', 'png', 'gif', 'webp', 'svg']
  return imageTypes.some(type => 
    props.fileType?.toLowerCase().includes(type) || 
    props.fileUrl?.toLowerCase().includes(`.${type}`)
  )
})

const isText = computed(() => {
  const textTypes = ['txt', 'html', 'htm', 'md', 'csv']
  return textTypes.some(type => 
    props.fileType?.toLowerCase().includes(type) || 
    props.fileUrl?.toLowerCase().includes(`.${type}`)
  )
})

const isOfficeDocument = computed(() => {
  const officeTypes = ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx']
  return officeTypes.some(type => 
    props.fileType?.toLowerCase().includes(type) || 
    props.fileUrl?.toLowerCase().includes(`.${type}`)
  )
})

const isAudio = computed(() => {
  const audioTypes = ['mp3', 'm4a', 'wav', 'ogg']
  return audioTypes.some(type =>
    props.fileType?.toLowerCase().includes(type) ||
    props.fileUrl?.toLowerCase().includes(`.${type}`)
  )
})

const resourceFile = computed(() => {
  return props.fileUrl
})

const previewUrl = computed(() => {
  // Always prioritize showing the actual file if available
  if (props.fileUrl) {
    // If it's already a full URL, use it directly
    if (props.fileUrl.startsWith('http://') || props.fileUrl.startsWith('https://')) {
      console.log('Using full URL:', props.fileUrl)
      return props.fileUrl
    }
    
    // Construct full URL from relative path
    // File paths are typically like /media/resources/files/...
    const filePath = props.fileUrl.startsWith('/') ? props.fileUrl : `/${props.fileUrl}`
    console.log('Constructed preview URL:', { fileUrl: props.fileUrl, filePath })
    return filePath
  }
  
  // Fallback: if no file URL, this shouldn't happen but handle gracefully
  console.warn('No file URL provided for preview')
  return ''
})

const close = () => {
  loading.value = true
  emit('close')
}

const openInNewTab = () => {
  if (previewUrl.value) {
    window.open(previewUrl.value, '_blank')
  } else if (props.fileUrl) {
    window.open(props.fileUrl, '_blank')
  }
}

const downloadFile = () => {
  if (previewUrl.value) {
    window.open(previewUrl.value, '_blank')
  } else if (props.fileUrl) {
    // Construct full URL if needed
    let url = props.fileUrl
    if (url && !url.startsWith('http://') && !url.startsWith('https://')) {
      const filePath = url.startsWith('/') ? url : `/${url}`
      url = `${backendUrl}${filePath}`
    }
    window.open(url, '_blank')
  }
}

const handleLoad = () => {
  loading.value = false
}

const handleError = () => {
  loading.value = false
  console.error('Failed to load preview')
}

// Watch for isOpen changes and log
watch(() => props.isOpen, (isOpen) => {
  console.log('Preview modal isOpen changed:', isOpen, {
    fileUrl: props.fileUrl,
    fileType: props.fileType,
    slug: props.slug,
    previewUrl: previewUrl.value
  })
  
  // Reset loading when opening
  if (isOpen) {
    loading.value = true
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
    loading.value = true
  }
}, { immediate: true })

// Log when component mounts
onMounted(() => {
  console.log('ResourcePreviewModal mounted with props:', {
    isOpen: props.isOpen,
    fileUrl: props.fileUrl,
    fileType: props.fileType,
    slug: props.slug
  })
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

