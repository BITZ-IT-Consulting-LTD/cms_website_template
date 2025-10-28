<template>
  <div class="p-6">
    <!-- Header -->
    <div class="flex items-center justify-between mb-6">
      <div>
        <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">Videos</h1>
        <p class="text-gray-600 mt-1">Manage video content for the Sauti platform</p>
      </div>
      
      <router-link
        to="/videos/create"
        class="btn-primary flex items-center"
      >
        <PlusIcon class="h-4 w-4 mr-2" />
        Add New Video
      </router-link>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
      <div class="card p-4">
        <div class="flex items-center">
          <div class="p-2 bg-blue-100 rounded-lg">
            <VideoCameraIcon class="h-6 w-6 text-blue-600" />
          </div>
          <div class="ml-3">
            <p class="text-sm font-medium text-gray-500">Total Videos</p>
            <p class="text-xl font-semibold text-gray-900">{{ stats.total }}</p>
          </div>
        </div>
      </div>
      
      <div class="card p-4">
        <div class="flex items-center">
          <div class="p-2 bg-green-100 rounded-lg">
            <CheckCircleIcon class="h-6 w-6 text-green-600" />
          </div>
          <div class="ml-3">
            <p class="text-sm font-medium text-gray-500">Published</p>
            <p class="text-xl font-semibold text-gray-900">{{ stats.published }}</p>
          </div>
        </div>
      </div>
      
      <div class="card p-4">
        <div class="flex items-center">
          <div class="p-2 bg-yellow-100 rounded-lg">
            <ClockIcon class="h-6 w-6 text-yellow-600" />
          </div>
          <div class="ml-3">
            <p class="text-sm font-medium text-gray-500">Drafts</p>
            <p class="text-xl font-semibold text-gray-900">{{ stats.draft }}</p>
          </div>
        </div>
      </div>
      
      <div class="card p-4">
        <div class="flex items-center">
          <div class="p-2 bg-purple-100 rounded-lg">
            <EyeIcon class="h-6 w-6 text-purple-600" />
          </div>
          <div class="ml-3">
            <p class="text-sm font-medium text-gray-500">Total Views</p>
            <p class="text-xl font-semibold text-gray-900">{{ formatNumber(stats.totalViews) }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Search and Filters -->
    <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <!-- Search -->
        <div class="relative">
          <MagnifyingGlassIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search videos..."
            class="form-input pl-10"
          />
        </div>
        
        <!-- Status Filter -->
        <select v-model="statusFilter" class="form-select">
          <option value="">All Status</option>
          <option value="published">Published</option>
          <option value="draft">Draft</option>
        </select>
        
        <!-- Category Filter -->
        <select v-model="categoryFilter" class="form-select">
          <option value="">All Categories</option>
          <option v-for="category in categories.filter(c => c && c.id)" :key="category.id" :value="category.name">
            {{ category.name }}
          </option>
        </select>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="text-center py-12">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
      <p class="mt-2 text-sm text-gray-500">Loading videos...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="text-center py-12">
      <div class="text-red-600 mb-4">
        <VideoCameraIcon class="h-12 w-12 mx-auto mb-2" />
        <h3 class="text-lg font-medium">Failed to load videos</h3>
        <p class="text-sm text-gray-500">{{ error }}</p>
      </div>
      <button @click="fetchVideos" class="btn-primary">
        Try Again
      </button>
    </div>

    <!-- Videos Table -->
    <div v-else class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="table-header">
            <tr>
              <th class="table-cell">Video</th>
              <th class="table-cell">Category</th>
              <th class="table-cell">Status</th>
              <th class="table-cell">Views</th>
              <th class="table-cell">Duration</th>
              <th class="table-cell">Date</th>
              <th class="table-cell">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="video in filteredVideos" :key="video.id" class="table-row hover:bg-gray-50">
              <td class="px-6 py-4">
                <div class="flex items-center">
                  <div class="flex-shrink-0 h-12 w-12">
                    <div v-if="video.thumbnail" class="h-12 w-12 rounded-lg overflow-hidden">
                      <img :src="video.thumbnail" :alt="video.title" class="h-full w-full object-cover">
                    </div>
                    <div v-else-if="video.youtube_thumbnail_url" class="h-12 w-12 rounded-lg overflow-hidden">
                      <img :src="video.youtube_thumbnail_url" :alt="video.title" class="h-full w-full object-cover">
                    </div>
                    <div v-else class="h-12 w-12 bg-gray-100 rounded-lg flex items-center justify-center">
                      <VideoCameraIcon class="h-6 w-6 text-gray-400" />
                    </div>
                  </div>
                  <div class="ml-4">
                    <div class="text-sm font-medium text-gray-900 line-clamp-2">
                      {{ video.title }}
                    </div>
                    <div class="text-sm text-gray-500 line-clamp-1">
                      {{ video.description || 'No description' }}
                    </div>
                  </div>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ video.category?.name || 'Uncategorized' }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span
                  class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
                  :class="{
                    'bg-green-100 text-green-800': video.status === 'published',
                    'bg-yellow-100 text-yellow-800': video.status === 'draft'
                  }"
                >
                  {{ video.status }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ formatNumber(video.views_count || 0) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ video.duration || 'N/A' }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ formatDate(video.published_at || video.created_at) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <div class="flex items-center justify-end space-x-2">
                  <button
                    @click="previewVideo(video)"
                    class="text-blue-600 hover:text-blue-900"
                    title="Preview"
                  >
                    <EyeIcon class="h-4 w-4" />
                  </button>
                  <router-link
                    :to="`/videos/${video.slug || video.id}/edit`"
                    class="text-primary-600 hover:text-primary-900"
                    title="Edit"
                  >
                    <PencilIcon class="h-4 w-4" />
                  </router-link>
                  <button
                    @click="deleteVideo(video)"
                    class="text-red-600 hover:text-red-900"
                    title="Delete"
                  >
                    <TrashIcon class="h-4 w-4" />
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <!-- Empty State -->
      <div v-if="filteredVideos.length === 0" class="text-center py-12">
        <VideoCameraIcon class="mx-auto h-12 w-12 text-gray-400" />
        <h3 class="mt-2 text-sm font-medium text-gray-900">No videos found</h3>
        <p class="mt-1 text-sm text-gray-500">
          {{ searchQuery ? 'Try adjusting your search criteria.' : 'Get started by creating your first video.' }}
        </p>
        <div class="mt-6" v-if="!searchQuery">
          <router-link to="/videos/create" class="btn-primary">
            <PlusIcon class="h-4 w-4 mr-2" />
            Add New Video
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useToast } from 'vue-toastification'
import { useVideosStore } from '@/stores/videos'
import {
  PlusIcon,
  VideoCameraIcon,
  CheckCircleIcon,
  ClockIcon,
  EyeIcon,
  MagnifyingGlassIcon,
  PencilIcon,
  TrashIcon
} from '@heroicons/vue/24/outline'

const toast = useToast()
const router = useRouter()
const route = useRoute()
const videosStore = useVideosStore()

// Reactive data
const searchQuery = ref('')
const statusFilter = ref('')
const categoryFilter = ref('')

// Use store data
const videos = computed(() => videosStore.videos)
const loading = computed(() => videosStore.loading)
const error = computed(() => videosStore.error)
const categories = computed(() => videosStore.categories)

// Computed properties
const stats = computed(() => {
  const total = videos.value.length
  const published = videos.value.filter(v => v.status === 'published').length
  const draft = videos.value.filter(v => v.status === 'draft').length
  const totalViews = videos.value.reduce((sum, v) => sum + (v.views_count || 0), 0)
  
  return {
    total,
    published,
    draft,
    totalViews
  }
})

const filteredVideos = computed(() => {
  let filtered = videos.value

  // Filter by search query
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(video =>
      video.title.toLowerCase().includes(query) ||
      (video.description && video.description.toLowerCase().includes(query))
    )
  }

  // Filter by status
  if (statusFilter.value) {
    filtered = filtered.filter(video => video.status === statusFilter.value)
  }

  // Filter by category
  if (categoryFilter.value) {
    filtered = filtered.filter(video => video.category?.name === categoryFilter.value)
  }

  return filtered
})

// Methods
const formatNumber = (num) => {
  if (num >= 1000000) {
    return (num / 1000000).toFixed(1) + 'M'
  } else if (num >= 1000) {
    return (num / 1000).toFixed(1) + 'K'
  }
  return num.toString()
}

const formatDate = (date) => {
  if (!date) return 'Recently'
  try {
    return new Date(date).toLocaleDateString()
  } catch (error) {
    return 'Recently'
  }
}

const previewVideo = (video) => {
  if (video.status === 'draft') {
    toast.warning('Cannot preview draft content')
    return
  }
  
  if (video.youtube_url) {
    window.open(video.youtube_url, '_blank')
  } else {
    toast.info('No video URL available')
  }
}

const deleteVideo = async (video) => {
  if (!confirm(`Are you sure you want to delete "${video.title}"?`)) {
    return
  }
  
  try {
    await videosStore.deleteVideo(video.slug || video.id)
    toast.success('Video deleted successfully')
  } catch (err) {
    console.error('Delete error:', err)
    toast.error('Failed to delete video')
  }
}

const fetchVideos = async () => {
  try {
    // Fetch categories first, then videos
    await videosStore.fetchCategories()
    await videosStore.fetchVideos()
  } catch (err) {
    console.error('Failed to fetch videos:', err)
    toast.error('Failed to load videos')
  }
}

// Watch for route changes to refresh data
watch(() => route.path, (newPath) => {
  if (newPath === '/videos') {
    fetchVideos()
  }
})

// Lifecycle
onMounted(() => {
  fetchVideos()
})
</script>