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
            <p class="text-sm font-medium text-gray-500">Draft</p>
            <p class="text-xl font-semibold text-gray-900">{{ stats.draft }}</p>
          </div>
        </div>
      </div>
      
      <div class="card p-4">
        <div class="flex items-center">
          <div class="p-2 bg-primary-100 rounded-lg">
            <EyeIcon class="h-6 w-6 text-primary-600" />
          </div>
          <div class="ml-3">
            <p class="text-sm font-medium text-gray-500">Total Views</p>
            <p class="text-xl font-semibold text-gray-900">{{ formatNumber(stats.views) }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Filters and Search -->
    <div class="card p-4 mb-6">
      <div class="flex flex-col sm:flex-row gap-4">
        <!-- Search -->
        <div class="flex-1">
          <div class="relative">
            <MagnifyingGlassIcon class="h-5 w-5 text-gray-400 absolute left-3 top-1/2 transform -translate-y-1/2" />
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search videos..."
              class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
        </div>
        
        <!-- Status Filter -->
        <select
          v-model="statusFilter"
          class="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
        >
          <option value="">All Status</option>
          <option value="published">Published</option>
          <option value="draft">Draft</option>
          <option value="private">Private</option>
        </select>
        
        <!-- Category Filter -->
        <select
          v-model="categoryFilter"
          class="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
        >
          <option value="">All Categories</option>
          <option v-for="category in categories" :key="category" :value="category">
            {{ category }}
          </option>
        </select>
      </div>
    </div>

    <!-- Videos Table -->
    <div class="card overflow-hidden">
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Video
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Status
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Category
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Duration
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Views
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Created
              </th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                Actions
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="video in filteredVideos" :key="video.id" class="hover:bg-gray-50">
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="flex items-center">
                  <div class="h-16 w-24 bg-gray-200 rounded-lg overflow-hidden mr-4">
                    <img
                      v-if="video.thumbnail"
                      :src="video.thumbnail"
                      :alt="video.title"
                      class="h-full w-full object-cover"
                    />
                    <div v-else class="h-full w-full flex items-center justify-center">
                      <VideoCameraIcon class="h-6 w-6 text-gray-400" />
                    </div>
                  </div>
                  <div>
                    <div class="text-sm font-medium text-gray-900">{{ video.title }}</div>
                    <div class="text-sm text-gray-500 max-w-xs truncate">{{ video.description }}</div>
                  </div>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span
                  class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
                  :class="{
                    'bg-green-100 text-green-800': video.status === 'published',
                    'bg-yellow-100 text-yellow-800': video.status === 'draft',
                    'bg-red-100 text-red-800': video.status === 'private'
                  }"
                >
                  {{ video.status }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ video.category }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ video.duration }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ formatNumber(video.views) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ formatDate(video.createdAt) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <div class="flex items-center justify-end space-x-2">
                  <button
                    @click="previewVideo(video)"
                    class="text-blue-600 hover:text-blue-900"
                  >
                    <EyeIcon class="h-4 w-4" />
                  </button>
                  <router-link
                    :to="`/videos/${video.id}/edit`"
                    class="text-primary-600 hover:text-primary-900"
                  >
                    <PencilIcon class="h-4 w-4" />
                  </router-link>
                  <button
                    @click="deleteVideo(video)"
                    class="text-red-600 hover:text-red-900"
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
import { ref, computed, onMounted } from 'vue'
import { useToast } from 'vue-toastification'
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

// Reactive data
const searchQuery = ref('')
const statusFilter = ref('')
const categoryFilter = ref('')

// Mock data
const videos = ref([
  {
    id: 1,
    title: "Sauti's Mission: A Video Overview",
    description: "This video provides a comprehensive overview of Sauti's mission to provide a safe and accessible helpline for children in Uganda.",
    thumbnail: null,
    status: 'published',
    category: 'About Sauti',
    duration: '00:05:32',
    views: 1247,
    createdAt: '2024-01-15T10:30:00Z'
  },
  {
    id: 2,
    title: 'Child Rights Awareness Campaign',
    description: 'Educational content about child rights and protection services available through Sauti.',
    thumbnail: null,
    status: 'published',
    category: 'Child Rights',
    duration: '00:03:45',
    views: 892,
    createdAt: '2024-01-10T14:20:00Z'
  },
  {
    id: 3,
    title: 'Success Story: Maria\'s Journey',
    description: 'A testimonial video showcasing how Sauti helped a young girl find safety and support.',
    thumbnail: null,
    status: 'draft',
    category: 'Success Stories',
    duration: '00:07:12',
    views: 0,
    createdAt: '2024-01-08T09:15:00Z'
  },
  {
    id: 4,
    title: 'How to Use the Sauti Helpline',
    description: 'Step-by-step guide on how children can access and use the Sauti helpline services.',
    thumbnail: null,
    status: 'published',
    category: 'Tutorials',
    duration: '00:04:28',
    views: 1564,
    createdAt: '2024-01-05T16:45:00Z'
  },
  {
    id: 5,
    title: 'Community Impact Report 2023',
    description: 'Annual report video highlighting the impact Sauti has made in communities across Uganda.',
    thumbnail: null,
    status: 'private',
    category: 'Reports',
    duration: '00:12:30',
    views: 156,
    createdAt: '2024-01-01T08:00:00Z'
  }
])

const categories = ref([
  'About Sauti',
  'Child Rights',
  'Success Stories',
  'Tutorials',
  'Reports',
  'Testimonials'
])

// Computed properties
const stats = computed(() => {
  const total = videos.value.length
  const published = videos.value.filter(v => v.status === 'published').length
  const draft = videos.value.filter(v => v.status === 'draft').length
  const views = videos.value.reduce((sum, v) => sum + v.views, 0)
  
  return { total, published, draft, views }
})

const filteredVideos = computed(() => {
  let filtered = videos.value

  // Search filter
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(video =>
      video.title.toLowerCase().includes(query) ||
      video.description.toLowerCase().includes(query)
    )
  }

  // Status filter
  if (statusFilter.value) {
    filtered = filtered.filter(video => video.status === statusFilter.value)
  }

  // Category filter
  if (categoryFilter.value) {
    filtered = filtered.filter(video => video.category === categoryFilter.value)
  }

  return filtered
})

// Methods
const formatNumber = (num) => {
  return new Intl.NumberFormat().format(num)
}

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}

const previewVideo = (video) => {
  toast.info(`Preview for "${video.title}" - Feature coming soon`)
}

const deleteVideo = (video) => {
  if (confirm(`Are you sure you want to delete "${video.title}"?`)) {
    const index = videos.value.findIndex(v => v.id === video.id)
    if (index > -1) {
      videos.value.splice(index, 1)
      toast.success('Video deleted successfully')
    }
  }
}

// Lifecycle
onMounted(() => {
  // Load videos data
  console.log('Videos page loaded')
})
</script>
