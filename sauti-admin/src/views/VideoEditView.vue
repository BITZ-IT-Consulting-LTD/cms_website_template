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
            <!-- Video File -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Current Video File</label>
              <div class="flex items-center space-x-3 mb-3">
                <VideoCameraIcon class="h-5 w-5 text-gray-400" />
                <span class="text-sm text-gray-900">{{ videoForm.filename || 'No file selected' }}</span>
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
                Change Video File
              </button>
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
          
          <!-- Categories -->
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">Categories</label>
            <div class="space-y-2 max-h-32 overflow-y-auto">
              <label v-for="category in videoCategories" :key="category" class="flex items-center">
                <input
                  v-model="videoForm.categories"
                  :value="category"
                  type="checkbox"
                  class="rounded border-gray-300 text-primary-500 focus:ring-primary-500"
                />
                <span class="ml-2 text-sm text-gray-700">{{ category }}</span>
              </label>
            </div>
            <p class="mt-1 text-xs text-gray-500">Select one or more categories</p>
          </div>
          
          <!-- Tags -->
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">Tags</label>
            <input
              v-model="videoForm.tags"
              type="text"
              placeholder="helpline, uganda, child safety"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
            <p class="mt-1 text-xs text-gray-500">Separate tags with commas</p>
          </div>
          
          <!-- Video Duration -->
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">Video Duration</label>
            <input
              v-model="videoForm.duration"
              type="text"
              placeholder="00:05:32"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
          
          <!-- Source URL -->
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">Source URL (optional)</label>
            <input
              v-model="videoForm.sourceUrl"
              type="url"
              placeholder="e.g., https://youtube.com/watch..."
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
        </div>

        <!-- Settings -->
        <div class="card p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Settings</h3>
          
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">Privacy</label>
            <select
              v-model="videoForm.privacy"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            >
              <option value="public">Public</option>
              <option value="private">Private</option>
              <option value="unlisted">Unlisted</option>
            </select>
          </div>
        </div>

        <!-- Actions -->
        <div class="card p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Actions</h3>
          
          <div class="space-y-3">
            <button
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
import {
  EyeIcon,
  ArrowUpIcon,
  VideoCameraIcon,
  PhotoIcon
} from '@heroicons/vue/24/outline'

const route = useRoute()
const router = useRouter()
const toast = useToast()

// Refs
const videoInput = ref(null)
const thumbnailInput = ref(null)
const loading = ref(false)
const thumbnailPreview = ref(null)

// Form data
const videoForm = ref({
  title: "Sauti's Mission: A Video Overview",
  description: "This video provides a comprehensive overview of Sauti's mission to provide a safe and accessible helpline for children in Uganda. It covers our history, services, and the impact we've made.",
  filename: 'sauti_mission_final.mp4',
  thumbnail: null,
  categories: ['About Sauti', 'Child Rights'],
  tags: 'helpline, uganda, child safety',
  duration: '00:05:32',
  sourceUrl: '',
  privacy: 'public'
})

// Mock data
const videoCategories = [
  'About Sauti',
  'Child Rights',
  'Testimonials',
  'Success Stories'
]

// Computed
const isEditing = computed(() => !!route.params.id)

// Methods
const handleVideoUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    // Validate file type
    if (!file.type.startsWith('video/')) {
      toast.error('Please select a video file')
      return
    }
    
    // Validate file size (max 100MB)
    if (file.size > 100 * 1024 * 1024) {
      toast.error('Video size must be less than 100MB')
      return
    }
    
    videoForm.value.filename = file.name
    videoForm.value.videoFile = file
    toast.success('Video file selected')
  }
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

const previewVideo = () => {
  toast.info('Video preview functionality coming soon')
}

const publishVideo = () => {
  saveChanges('published')
}

const saveChanges = async (status = 'draft') => {
  if (!videoForm.value.title.trim()) {
    toast.error('Please enter a video title')
    return
  }

  loading.value = true

  try {
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    toast.success(`Video ${status === 'published' ? 'published' : 'saved'} successfully`)
    
    if (!isEditing.value) {
      router.push('/videos')
    }
  } catch (err) {
    console.error('Save error:', err)
    toast.error('Failed to save video')
  } finally {
    loading.value = false
  }
}

// Lifecycle
onMounted(() => {
  if (isEditing.value) {
    // Load video data if editing
    console.log('Loading video data for ID:', route.params.id)
  }
})
</script>
