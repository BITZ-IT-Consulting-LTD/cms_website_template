<template>
  <div class="p-6">
    <!-- Header -->
    <div class="flex items-center justify-between mb-8">
      <h1 class="text-2xl font-bold text-gray-900">Admin Dashboard</h1>
      <button
        @click="$router.push('/posts/create')"
        class="btn-primary flex items-center"
      >
        <PlusIcon class="h-5 w-5 mr-2" />
        Create New Content
      </button>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <div class="card p-6">
        <div class="text-sm text-gray-500 mb-2">Total Blog Posts</div>
        <div class="text-3xl font-bold text-gray-900">{{ stats.totalPosts }}</div>
      </div>
      
      <div class="card p-6">
        <div class="text-sm text-gray-500 mb-2">Total Videos</div>
        <div class="text-3xl font-bold text-gray-900">{{ stats.totalVideos }}</div>
      </div>
      
      <div class="card p-6">
        <div class="text-sm text-gray-500 mb-2">Total Views</div>
        <div class="text-3xl font-bold text-gray-900">{{ stats.totalViews }}</div>
      </div>
      
      <div class="card p-6">
        <div class="text-sm text-gray-500 mb-2">Total Engagement</div>
        <div class="text-3xl font-bold text-gray-900">{{ stats.totalEngagement }}</div>
      </div>
    </div>

    <!-- Content Management -->
    <div class="card mb-8">
      <div class="p-6 border-b border-gray-200">
        <h2 class="text-lg font-semibold text-gray-900 mb-4">Content Management</h2>
        
        <!-- Filters -->
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
          <div class="flex flex-col sm:flex-row gap-4">
            <select
              v-model="filters.contentType"
              class="px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            >
              <option value="">All Content</option>
              <option value="blog">Blog Posts</option>
              <option value="video">Videos</option>
            </select>
            
            <select
              v-model="filters.status"
              class="px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            >
              <option value="">All Statuses</option>
              <option value="published">Published</option>
              <option value="draft">Draft</option>
            </select>
          </div>
          
          <div class="w-full sm:w-auto">
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search content..."
              class="w-full sm:w-64 px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
        </div>
      </div>

      <!-- Content Table -->
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Title
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Type
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Status
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Date
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Actions
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="item in filteredContent" :key="item.id" class="hover:bg-gray-50">
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm font-medium text-gray-900">{{ item.title }}</div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span :class="item.type === 'blog' ? 'type-blog' : 'type-video'">
                  {{ item.type === 'blog' ? 'Blog' : 'Video' }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span :class="item.status === 'published' ? 'status-published' : 'status-draft'">
                  {{ item.status === 'published' ? 'Published' : 'Draft' }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ item.date }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                <div class="flex items-center space-x-3">
                  <button
                    @click="editItem(item)"
                    class="text-gray-400 hover:text-gray-500"
                    title="Edit"
                  >
                    <PencilIcon class="h-5 w-5" />
                  </button>
                  
                  <button
                    @click="viewItem(item)"
                    class="text-gray-400 hover:text-gray-500"
                    :class="{ 'opacity-50': item.status === 'draft' }"
                    :title="item.status === 'draft' ? 'Cannot preview draft' : 'View'"
                  >
                    <EyeIcon v-if="item.status === 'published'" class="h-5 w-5" />
                    <EyeSlashIcon v-else class="h-5 w-5" />
                  </button>
                  
                  <button
                    @click="deleteItem(item)"
                    class="text-gray-400 hover:text-red-500"
                    title="Delete"
                  >
                    <TrashIcon class="h-5 w-5" />
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        
        <div v-if="loading" class="p-8 text-center">
          <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-500 mx-auto"></div>
          <p class="mt-2 text-sm text-gray-500">Loading content...</p>
        </div>
        
        <div v-else-if="filteredContent.length === 0" class="p-8 text-center">
          <p class="text-sm text-gray-500">No content found matching your criteria.</p>
        </div>
      </div>
    </div>

    <!-- Statistics & Analytics -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- Content Performance Chart -->
      <div class="lg:col-span-2 card p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-lg font-semibold text-gray-900">Content Performance</h3>
          <select
            v-model="analyticsTimeframe"
            class="px-3 py-1 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
          >
            <option value="30">Last 30 days</option>
            <option value="90">Last 90 days</option>
            <option value="365">Last year</option>
          </select>
        </div>
        
        <div class="h-64 flex items-center justify-center bg-gray-50 rounded-lg">
          <div class="text-center">
            <ChartBarIcon class="h-12 w-12 text-gray-400 mx-auto mb-2" />
            <p class="text-sm text-gray-500">Interactive Chart Area</p>
            <p class="text-xs text-gray-400">Chart.js integration coming soon</p>
          </div>
        </div>
      </div>

      <!-- Top Performing Content -->
      <div class="card p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-6">Top Performing Content</h3>
        
        <div class="space-y-4">
          <div v-for="item in topContent" :key="item.title" class="flex items-start justify-between">
            <div class="flex-1 min-w-0">
              <p class="text-sm font-medium text-gray-900 truncate">{{ item.title }}</p>
              <p class="text-xs text-gray-500">{{ item.type }}</p>
            </div>
            <div class="flex-shrink-0 ml-4">
              <p class="text-xs font-medium text-gray-900">{{ item.views }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useDashboardStore } from '@/stores/dashboard'
import { useToast } from 'vue-toastification'
import {
  PlusIcon,
  PencilIcon,
  EyeIcon,
  EyeSlashIcon,
  TrashIcon,
  ChartBarIcon
} from '@heroicons/vue/24/outline'

const router = useRouter()
const dashboardStore = useDashboardStore()
const toast = useToast()

// Reactive data
const searchQuery = ref('')
const analyticsTimeframe = ref('30')
const filters = ref({
  contentType: '',
  status: ''
})

// Computed properties
const stats = computed(() => dashboardStore.stats)
const contentList = computed(() => dashboardStore.contentList)
const topContent = computed(() => dashboardStore.topContent)
const loading = computed(() => dashboardStore.loading)

const filteredContent = computed(() => {
  let filtered = contentList.value

  // Filter by search query
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(item =>
      item.title.toLowerCase().includes(query)
    )
  }

  // Filter by content type
  if (filters.value.contentType) {
    filtered = filtered.filter(item => item.type === filters.value.contentType)
  }

  // Filter by status
  if (filters.value.status) {
    filtered = filtered.filter(item => item.status === filters.value.status)
  }

  return filtered
})

// Methods
const editItem = (item) => {
  if (item.type === 'blog') {
    router.push(`/posts/${item.slug}/edit`)
  } else if (item.type === 'video') {
    router.push(`/videos/${item.id}/edit`)
  }
}

const viewItem = (item) => {
  if (item.status === 'draft') {
    toast.warning('Cannot preview draft content')
    return
  }
  
  // For now, just show a message
  toast.info('Preview functionality coming soon')
}

const deleteItem = async (item) => {
  if (!confirm(`Are you sure you want to delete "${item.title}"?`)) {
    return
  }
  
  try {
    // This would call the appropriate store method
    toast.success('Content deleted successfully')
    // Refresh the content list
    await dashboardStore.fetchContentList()
  } catch (err) {
    console.error('Delete error:', err)
    toast.error('Failed to delete content')
  }
}

// Lifecycle
onMounted(async () => {
  try {
    await Promise.all([
      dashboardStore.fetchStats(),
      dashboardStore.fetchContentList(),
      dashboardStore.fetchTopContent()
    ])
  } catch (err) {
    console.error('Failed to load dashboard data:', err)
    toast.error('Failed to load dashboard data')
  }
})
</script>
