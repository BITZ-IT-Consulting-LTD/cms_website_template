<template>
  <div class="p-6">
    <!-- Header Actions -->
    <div class="flex items-center justify-between mb-6">
      <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">
        {{ isEditing ? 'Edit Video' : 'Create Video' }}
      </h1>
      
      <div class="flex items-center space-x-3">
        <button
          @click="previewVideo"
          class="btn-secondary flex items-center"
        >
          <EyeIcon class="h-4 w-4 mr-2" />
          Preview
        </button>
        
        <button
          @click="publishVideo"
          class="btn-success flex items-center"
        >
          <ArrowUpIcon class="h-4 w-4 mr-2" />
          Publish
        </button>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- Main Content Area -->
      <div class="lg:col-span-2 space-y-6">
        <!-- Video Title -->
        <div class="card p-6">
          <label for="video-title" class="block text-sm font-medium text-gray-700 mb-2">
            Video Title
          </label>
          <input
            id="video-title"
            v-model="videoForm.title"
            type="text"
            class="w-full px-3 py-2 border border-gray-300 rounded-md text-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            placeholder="Enter video title..."
          />
        </div>

        <!-- Description -->
        <div class="card p-6">
          <label for="description" class="block text-sm font-medium text-gray-700 mb-2">
            Description
          </label>
          <textarea
            id="description"
            v-model="videoForm.description"
            rows="6"
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            placeholder="Enter video description..."
          ></textarea>
        </div>

        <!-- Video & Thumbnail -->
        <div class="card p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Video & Thumbnail</h3>
          
          <!-- Video Source Selection -->
          <div class="mb-6">
            <label class="block text-sm font-medium text-gray-700 mb-3">Video Source</label>
            <div class="flex gap-4">
              <label class="flex items-center cursor-pointer">
                <input
                  v-model="videoForm.video_type"
                  type="radio"
                  value="YOUTUBE"
                  class="mr-2 text-[#8B4000] focus:ring-[#8B4000]"
                />
                <span class="text-sm text-gray-700">YouTube URL</span>
              </label>
              <label class="flex items-center cursor-pointer">
                <input
                  v-model="videoForm.video_type"
                  type="radio"
                  value="UPLOAD"
                  class="mr-2 text-[#8B4000] focus:ring-[#8B4000]"
                />
                <span class="text-sm text-gray-700">Upload Video File</span>
              </label>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- YouTube URL (shown when YOUTUBE is selected) -->
            <div v-if="videoForm.video_type === 'YOUTUBE'">
              <label class="block text-sm font-medium text-gray-700 mb-2">YouTube URL</label>
              <input
                v-model="videoForm.youtube_url"
                type="url"
                placeholder="https://youtube.com/watch?v=..."
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
              />
              <p class="mt-1 text-xs text-gray-500">Enter YouTube video URL</p>

              <!-- Lightweight preview (thumbnail + play) so editors can confirm the link is correct -->
              <div v-if="youtubePreviewEmbedUrl" class="mt-3 rounded-lg overflow-hidden border border-gray-200 bg-black/5">
                <iframe
                  :src="youtubePreviewEmbedUrl"
                  class="w-full h-40 bg-black"
                  frameborder="0"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowfullscreen
                ></iframe>
              </div>
            </div>

            <!-- Video File Upload (shown when UPLOAD is selected) -->
            <div v-if="videoForm.video_type === 'UPLOAD'">
              <label class="block text-sm font-medium text-gray-700 mb-2">Video File</label>
              
              <div v-if="videoPreview || videoForm.video_file" class="mb-3">
                <video
                  v-if="videoPreview"
                  :src="videoPreview"
                  controls
                  class="w-full h-48 object-contain rounded-lg bg-black"
                ></video>
                <div v-else class="w-full h-48 bg-gray-100 rounded-lg flex items-center justify-center">
                  <p class="text-sm text-gray-600">Video file selected</p>
                </div>
              </div>
              
              <div v-else class="w-full h-48 bg-gray-100 rounded-lg flex flex-col items-center justify-center mb-3 border-2 border-dashed border-gray-300">
                <VideoCameraIcon class="h-12 w-12 text-gray-400 mb-2" />
                <p class="text-sm text-gray-500">No video selected</p>
                <p class="text-xs text-gray-400 mt-1">MP4, AVI, MOV, etc.</p>
              </div>
              
              <input
                ref="videoInput"
                type="file"
                accept="video/*"
                @change="handleVideoUpload"
                class="hidden"
              />
              
              <button
                @click="videoInput.click()"
                class="w-full px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
              >
                {{ videoForm.video_file ? 'Change Video' : 'Upload Video' }}
              </button>
              <p class="mt-1 text-xs text-gray-500">Max file size: 500MB</p>
            </div>

            <!-- Thumbnail -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Thumbnail</label>
              
              <div v-if="thumbnailPreview || videoForm.thumbnail" class="mb-3 relative">
                <img
                  :src="thumbnailPreview || videoForm.thumbnail"
                  alt="Video thumbnail"
                  class="w-full h-32 object-cover rounded-lg"
                />
                <button
                  @click="removeThumbnail"
                  title="Remove thumbnail"
                  class="absolute top-2 right-2 p-1 bg-red-500 text-white rounded-full hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500 transition-all duration-200 shadow-lg"
                >
                  <XMarkIcon class="h-3 w-3" />
                </button>
              </div>
              
              <div v-else class="w-full h-32 bg-gray-100 rounded-lg flex items-center justify-center mb-3">
                <PhotoIcon class="h-8 w-8 text-gray-400" />
              </div>
              
              <input
                ref="thumbnailInput"
                type="file"
                accept="image/*"
                @change="handleThumbnailUpload"
                class="hidden"
              />
              
              <button
                @click="thumbnailInput.click()"
                class="w-full px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
              >
                Change Thumbnail
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Metadata Sidebar -->
      <div class="space-y-6">
        <!-- Metadata -->
        <div class="card p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Metadata</h3>
          
          <!-- Category -->
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">Category</label>
            <select
              v-model="videoForm.category_id"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            >
              <option :value="null">Select category</option>
              <option v-for="cat in videoCategories" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
            </select>
          </div>
          
          <!-- Language -->
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">Language</label>
            <select
              v-model="videoForm.language"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            >
              <option value="en">English</option>
              <option value="lg">Luganda</option>
              <option value="sw">Swahili</option>
            </select>
          </div>
          
          <!-- Featured -->
          <div class="mb-4">
            <label class="flex items-center">
              <input
                v-model="videoForm.is_featured"
                type="checkbox"
                class="rounded border-gray-300 text-primary-500 focus:ring-primary-500"
              />
              <span class="ml-2 text-sm text-gray-700">Feature on homepage</span>
            </label>
          </div>
        </div>

        <!-- Settings -->
        <div class="card p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Publishing</h3>

          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">Status</label>
            <select
              v-model="videoForm.status"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            >
              <option value="DRAFT">⏳ Draft</option>
              <option value="PUBLISHED">✅ Published</option>
            </select>
            <p class="mt-2 text-xs text-gray-500">Published videos are visible on the frontend</p>
          </div>

          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">
              <svg class="w-4 h-4 inline mr-1 text-primary-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              Schedule Publishing
            </label>
            <input
              v-model="videoForm.scheduled_publish_at"
              type="datetime-local"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
            <p class="mt-2 text-xs text-gray-500">
              Set a date and time to automatically publish this video. It will stay as draft until then.
            </p>
            <button
              v-if="videoForm.scheduled_publish_at"
              @click="videoForm.scheduled_publish_at = null"
              type="button"
              class="mt-2 text-xs text-red-600 hover:text-red-800"
            >
              Clear schedule
            </button>
          </div>
        </div>

        <!-- Actions -->
        <div class="card p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Actions</h3>
          
          <div class="space-y-3">
            <button
              v-if="isEditing"
              @click="saveChanges"
              :disabled="loading"
              class="w-full btn-primary"
            >
              {{ loading ? 'Saving...' : 'Save Changes' }}
            </button>
            
            <button
              @click="$router.go(-1)"
              class="w-full px-4 py-2 text-gray-700 hover:text-gray-900 focus:outline-none"
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { useVideosStore } from '@/stores/videos'
import {
  EyeIcon,
  ArrowUpIcon,
  VideoCameraIcon,
  PhotoIcon,
  XMarkIcon
} from '@heroicons/vue/24/outline'

const route = useRoute()
const router = useRouter()
const toast = useToast()
const videosStore = useVideosStore()

// Refs
const videoInput = ref(null)
const thumbnailInput = ref(null)
const loading = ref(false)
const thumbnailPreview = ref(null)
const videoPreview = ref(null)
const videoPreviewObjectUrl = ref(null)

const videoForm = ref({
  title: '',
  description: '',
  youtube_url: '',
  video_file: null,
  video_type: 'YOUTUBE',
  category_id: null,
  status: 'DRAFT',
  language: 'en',
  is_featured: false,
  thumbnail: null,
  scheduled_publish_at: null
})

const videoCategories = computed(() => {
  const cats = videosStore.categories || []
  return cats.filter(c => c && c.id && c.name)
})

const videoKey = computed(() => route.params.slug || route.params.id)
const isEditing = computed(() => !!videoKey.value)

// Methods

const youtubePreviewEmbedUrl = computed(() => {
  const url = (videoForm.value.youtube_url || '').trim()
  if (!url) return ''

  const patterns = [
    /(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)/,
    /youtube\.com\/v\/([^&\n?#]+)/
  ]

  for (const pattern of patterns) {
    const match = url.match(pattern)
    if (match) {
      // No autoplay in admin preview
      return `https://www.youtube.com/embed/${match[1]}?rel=0`
    }
  }

  return ''
})

const removeThumbnail = () => {
  thumbnailPreview.value = null
  videoForm.value.thumbnail = null
  if (thumbnailInput.value) {
    thumbnailInput.value.value = ''
  }
  toast.info('Thumbnail removed. Save changes to make it permanent.')
}

const handleThumbnailUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    // Validate file type
    if (!file.type.startsWith('image/')) {
      toast.error('Please select an image file')
      return
    }
    
    // Validate file size (max 5MB)
    if (file.size > 5 * 1024 * 1024) {
      toast.error('Image size must be less than 5MB')
      return
    }
    
    const reader = new FileReader()
    reader.onload = (e) => {
      thumbnailPreview.value = e.target.result
      videoForm.value.thumbnail = file
    }
    reader.readAsDataURL(file)
    toast.success('Thumbnail updated')
  }
}

const handleVideoUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    // Validate file type
    if (!file.type.startsWith('video/')) {
      toast.error('Please select a video file')
      return
    }
    
    // Validate file size (max 500MB)
    if (file.size > 500 * 1024 * 1024) {
      toast.error('Video size must be less than 500MB')
      return
    }
    
    // Use object URLs for preview to avoid huge base64 strings (large videos can freeze/fail with FileReader).
    if (videoPreviewObjectUrl.value) {
      URL.revokeObjectURL(videoPreviewObjectUrl.value)
      videoPreviewObjectUrl.value = null
    }
    videoPreviewObjectUrl.value = URL.createObjectURL(file)
    videoPreview.value = videoPreviewObjectUrl.value
    videoForm.value.video_file = file
    videoForm.value.video_type = 'UPLOAD'
    // Clear YouTube URL if video file is uploaded
    videoForm.value.youtube_url = ''
    toast.success('Video file ready')
  }
}

const previewVideo = () => {
  toast.info('Video preview functionality coming soon')
}

onBeforeUnmount(() => {
  if (videoPreviewObjectUrl.value) {
    URL.revokeObjectURL(videoPreviewObjectUrl.value)
    videoPreviewObjectUrl.value = null
  }
})

const publishVideo = () => {
  saveChanges('PUBLISHED')
}

const saveChanges = async (status = 'DRAFT') => {
  if (!videoForm.value.title.trim()) {
    toast.error('Please enter a video title')
    return
  }

  loading.value = true

  let videoData = {}
  
  try {
    // Build video data object, only including defined values
    videoData = {
      title: videoForm.value.title.trim(),
      description: videoForm.value.description?.trim() || '',
      status: status || videoForm.value.status || 'DRAFT',
      language: videoForm.value.language || 'en',
      is_featured: videoForm.value.is_featured || false
    }
    
    // Add category_id only if selected (ensure it's a number)
    if (videoForm.value.category_id) {
      const categoryId = typeof videoForm.value.category_id === 'number' 
        ? videoForm.value.category_id 
        : parseInt(videoForm.value.category_id, 10)
      if (!isNaN(categoryId) && categoryId > 0) {
        videoData.category_id = categoryId
      }
    }
    
    // Handle video source based on video_type
    if (videoForm.value.video_type === 'UPLOAD') {
      videoData.video_type = 'UPLOAD'
      videoData.youtube_url = '' // Clear youtube_url
      // For uploaded videos, include video_file
      if (videoForm.value.video_file instanceof File) {
        videoData.video_file = videoForm.value.video_file
      }
    } else { // YOUTUBE
      videoData.video_type = 'YOUTUBE'
      if (videoForm.value.youtube_url && videoForm.value.youtube_url.trim()) {
        videoData.youtube_url = videoForm.value.youtube_url.trim()
      } else {
        videoData.youtube_url = ''
      }
      // If switching to YouTube, signal to backend to delete the stored video file
      if (isEditing.value) {
        videoData.video_file = null
      }
    }

    // Add scheduled publish date if set
    if (videoForm.value.scheduled_publish_at) {
      // Convert local datetime to ISO format for backend
      videoData.scheduled_publish_at = new Date(videoForm.value.scheduled_publish_at).toISOString()
      // If scheduling, ensure status is DRAFT
      if (videoData.scheduled_publish_at) {
        videoData.status = 'DRAFT'
      }
    } else {
      videoData.scheduled_publish_at = null
    }

    // Handle thumbnail
    if (videoForm.value.thumbnail instanceof File) {
      videoData.thumbnail = videoForm.value.thumbnail
    } else if (isEditing.value && videoForm.value.thumbnail === null) {
      // If thumbnail was removed, send null to delete it
      videoData.thumbnail = null
    }
    // If it's an existing URL (string), we don't send anything, backend keeps the old image.
    
    // Debug: Log the data being sent (without file objects for cleaner console)
    const debugData = {
      ...videoData,
      thumbnail: videoData.thumbnail instanceof File ? `File: ${videoData.thumbnail.name} (${(videoData.thumbnail.size / 1024 / 1024).toFixed(2)}MB)` : (videoData.thumbnail || 'No file'),
      video_file: videoData.video_file instanceof File ? `File: ${videoData.video_file.name} (${(videoData.video_file.size / 1024 / 1024).toFixed(2)}MB)` : (videoData.video_file || 'No file')
    }
    console.log('Video data being sent:', debugData)

    if (isEditing.value) {
      const updatedVideo = await videosStore.updateVideo(videoKey.value, videoData)
      // Update form with new thumbnail URL from response
      if (updatedVideo.thumbnail) {
        videoForm.value.thumbnail = updatedVideo.thumbnail
      }
      // Clear thumbnailPreview so the actual image URL is displayed
      thumbnailPreview.value = null
      toast.success('Video updated successfully')
    } else {
      await videosStore.createVideo(videoData)
      toast.success('Video created successfully')
      // Wait a bit before navigating to ensure store is updated
      await new Promise(resolve => setTimeout(resolve, 100))
      router.push('/videos')
    }
  } catch (err) {
    console.error('Save error:', err)
    
    // Extract detailed error message
    let errorMessage = 'Failed to save video'
    
    // Handle network errors
    if (err.code === 'ERR_NETWORK' || err.message?.includes('Network Error') || err.message?.includes('Connection refused')) {
      errorMessage = 'Cannot connect to server. Please ensure the backend server is running on http://localhost:8000'
      console.error('Network error - backend server may not be running')
    } else if (err.response?.data) {
      const data = err.response.data
      
      // Handle Django REST Framework validation errors
      if (data.detail) {
        errorMessage = data.detail
      } else if (typeof data === 'object') {
        // Collect all field errors
        const fieldErrors = []
        Object.keys(data).forEach(field => {
          if (Array.isArray(data[field])) {
            fieldErrors.push(`${field}: ${data[field].join(', ')}`)
          } else if (typeof data[field] === 'string') {
            fieldErrors.push(`${field}: ${data[field]}`)
          } else {
            fieldErrors.push(`${field}: ${JSON.stringify(data[field])}`)
          }
        })
        if (fieldErrors.length > 0) {
          errorMessage = fieldErrors.join('; ')
        }
      } else if (typeof data === 'string') {
        errorMessage = data
      }
    } else if (err.message) {
      errorMessage = err.message
    }
    
    toast.error(errorMessage)
  } finally {
    loading.value = false
  }
}

onMounted(async () => {
  await videosStore.fetchCategories()
  
  if (isEditing.value) {
    try {
      const video = await videosStore.fetchVideo(videoKey.value)
      videoForm.value = {
        title: video.title || '',
        description: video.description || '',
        youtube_url: video.youtube_url || '',
        video_file: null, // Don't load existing file, just URL reference
        video_type: video.video_type || 'YOUTUBE',
        category_id: video.category?.id || null,
        status: video.status?.toUpperCase() || 'DRAFT',
        language: video.language || 'en',
        is_featured: video.is_featured || false,
        thumbnail: video.thumbnail || null,
        scheduled_publish_at: video.scheduled_publish_at ? new Date(video.scheduled_publish_at).toISOString().slice(0, 16) : null
      }
    } catch (err) {
      console.error('Failed to load video:', err)
      toast.error('Failed to load video data')
      router.push('/videos')
    }
  }
})
</script>
