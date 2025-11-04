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
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- YouTube URL -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">YouTube URL</label>
              <input
                v-model="videoForm.youtube_url"
                type="url"
                placeholder="https://youtube.com/watch?v=..."
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
              />
              <p class="mt-1 text-xs text-gray-500">Enter YouTube video URL</p>
            </div>

            <!-- Thumbnail -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Thumbnail</label>
              
              <div v-if="thumbnailPreview || videoForm.thumbnail" class="mb-3">
                <img
                  :src="thumbnailPreview || videoForm.thumbnail"
                  alt="Video thumbnail"
                  class="w-full h-32 object-cover rounded-lg"
                />
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
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { useVideosStore } from '@/stores/videos'
import {
  EyeIcon,
  ArrowUpIcon,
  VideoCameraIcon,
  PhotoIcon
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

const videoForm = ref({
  title: '',
  description: '',
  youtube_url: '',
  category_id: null,
  status: 'DRAFT',
  language: 'en',
  is_featured: false,
  thumbnail: null
})

const videoCategories = computed(() => {
  const cats = videosStore.categories || []
  return cats.filter(c => c && c.id && c.name)
})

const isEditing = computed(() => !!route.params.slug)

// Methods

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

const previewVideo = () => {
  toast.info('Video preview functionality coming soon')
}

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
    
    // Handle YouTube URL - only include if it's not empty
    if (videoForm.value.youtube_url && videoForm.value.youtube_url.trim()) {
      videoData.youtube_url = videoForm.value.youtube_url.trim()
      videoData.video_type = 'YOUTUBE'
    } else {
      // If no YouTube URL, default to YOUTUBE type (backend default)
      // This allows for videos that will be added later
      videoData.video_type = 'YOUTUBE'
    }
    
    // Handle video file upload (if implemented)
    // Note: If both video_file and youtube_url are provided, video_file takes precedence
    if (videoForm.value.video_file instanceof File) {
      videoData.video_file = videoForm.value.video_file
      videoData.video_type = 'UPLOAD'
    }

    // Only include thumbnail if it's a File object (new upload)
    // If it's a string (existing URL), omit it - backend will keep existing thumbnail
    if (videoForm.value.thumbnail instanceof File) {
      videoData.thumbnail = videoForm.value.thumbnail
    }
    // For editing: if thumbnail is a string (existing URL), don't include it
    
    // Debug: Log the data being sent
    console.log('Video data being sent:', {
      ...videoData,
      thumbnail: videoData.thumbnail instanceof File ? `File: ${videoData.thumbnail.name}` : 'No file',
      video_file: videoData.video_file instanceof File ? `File: ${videoData.video_file.name}` : 'No file'
    })

    if (isEditing.value) {
      await videosStore.updateVideo(route.params.slug, videoData)
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
    console.error('Error response:', err.response?.data)
    console.error('Video data sent:', videoData)
    
    // Extract detailed error message
    let errorMessage = 'Failed to save video'
    
    if (err.response?.data) {
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
      const video = await videosStore.fetchVideo(route.params.slug)
      videoForm.value = {
        title: video.title || '',
        description: video.description || '',
        youtube_url: video.youtube_url || '',
        category_id: video.category?.id || null,
        status: video.status?.toUpperCase() || 'DRAFT',
        language: video.language || 'en',
        is_featured: video.is_featured || false,
        thumbnail: video.thumbnail || null
      }
    } catch (err) {
      console.error('Failed to load video:', err)
      toast.error('Failed to load video data')
      router.push('/videos')
    }
  }
})
</script>
