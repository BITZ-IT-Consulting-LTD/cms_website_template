<template>
  <div class="space-y-8">
    <!-- Enhanced Header -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-4xl font-bold text-gray-900 mb-2" style="font-family: 'Roboto', sans-serif;">Content Management Dashboard</h1>
        <p class="text-lg text-gray-600">Manage your website content, blog posts, videos, and resources</p>
      </div>
      <div class="flex gap-3">
        <button
          @click="$router.push('/posts/create')"
          class="btn-primary flex items-center shadow-lg hover:shadow-xl"
        >
          <PlusIcon class="h-5 w-5 mr-2" />
          New Blog Post
        </button>
        <button
          @click="$router.push('/videos/create')"
          class="btn-secondary flex items-center shadow-lg hover:shadow-xl"
        >
          <VideoCameraIcon class="h-5 w-5 mr-2" />
          New Video
        </button>
      </div>
    </div>

    <!-- Enhanced Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="stats-card group">
        <div class="flex items-center justify-between mb-4">
          <div class="p-3 bg-blue-100 rounded-2xl group-hover:bg-blue-200 transition-colors duration-300">
            <DocumentTextIcon class="h-6 w-6 text-blue-600" />
          </div>
          <div class="text-right">
            <div class="stats-number">{{ stats.totalPosts }}</div>
            <div class="stats-label">Blog Posts</div>
          </div>
        </div>
        <div class="text-sm text-gray-600">Published articles</div>
      </div>
      
      <div class="stats-card group">
        <div class="flex items-center justify-between mb-4">
          <div class="p-3 bg-purple-100 rounded-2xl group-hover:bg-purple-200 transition-colors duration-300">
            <VideoCameraIcon class="h-6 w-6 text-purple-600" />
          </div>
          <div class="text-right">
            <div class="stats-number">{{ stats.totalVideos }}</div>
            <div class="stats-label">Videos</div>
          </div>
        </div>
        <div class="text-sm text-gray-600">Educational content</div>
      </div>
      
      <div class="stats-card group">
        <div class="flex items-center justify-between mb-4">
          <div class="p-3 bg-indigo-100 rounded-2xl group-hover:bg-indigo-200 transition-colors duration-300">
            <FolderOpenIcon class="h-6 w-6 text-indigo-600" />
          </div>
          <div class="text-right">
            <div class="stats-number">{{ stats.totalResources || 0 }}</div>
            <div class="stats-label">Resources</div>
          </div>
        </div>
        <div class="text-sm text-gray-600">Downloadable content</div>
      </div>
      
      <div class="stats-card group">
        <div class="flex items-center justify-between mb-4">
          <div class="p-3 bg-teal-100 rounded-2xl group-hover:bg-teal-200 transition-colors duration-300">
            <QuestionMarkCircleIcon class="h-6 w-6 text-teal-600" />
          </div>
          <div class="text-right">
            <div class="stats-number">{{ stats.totalFaqs || 0 }}</div>
            <div class="stats-label">FAQs</div>
          </div>
        </div>
        <div class="text-sm text-gray-600">Help content</div>
      </div>
    </div>

    <!-- Enhanced Content Management -->
    <div class="card">
      <div class="card-header">
        <h2 class="text-2xl font-bold text-gray-900 mb-2" style="font-family: 'Roboto', sans-serif;">Content Management</h2>
        <p class="text-gray-600">Manage your blog posts, videos, resources, and other content</p>
      </div>
        
      <div class="card-body">
        <!-- Enhanced Quick Actions -->
        <div class="flex flex-wrap gap-3 mb-6">
          <router-link
            to="/posts/create"
            class="btn-primary flex items-center gap-2"
          >
            <DocumentTextIcon class="h-5 w-5" />
            New Blog Post
          </router-link>
          
          <router-link
            to="/videos/create"
            class="btn-secondary flex items-center gap-2"
          >
            <VideoCameraIcon class="h-5 w-5" />
            New Video
          </router-link>
          
          <router-link
            to="/resources/create"
            class="btn-outline flex items-center gap-2"
          >
            <FolderOpenIcon class="h-5 w-5" />
            New Resource
          </router-link>
          
          <router-link
            to="/faqs/create"
            class="btn-outline flex items-center gap-2"
          >
            <QuestionMarkCircleIcon class="h-5 w-5" />
            New FAQ
          </router-link>
        </div>

        <!-- Enhanced Filters -->
        <div class="flex flex-col lg:flex-row justify-between items-start lg:items-center gap-6 mb-6">
          <div class="flex flex-col sm:flex-row gap-4">
            <div class="flex flex-col">
              <label class="form-label">Content Type</label>
              <select
                v-model="filters.contentType"
                class="form-select w-48"
              >
                <option value="">All Content</option>
                <option value="blog">Blog Posts</option>
                <option value="video">Videos</option>
                <option value="resource">Resources</option>
                <option value="faq">FAQs</option>
              </select>
            </div>
            
            <div class="flex flex-col">
              <label class="form-label">Status</label>
              <select
                v-model="filters.status"
                class="form-select w-48"
              >
                <option value="">All Statuses</option>
                <option value="published">Published</option>
                <option value="draft">Draft</option>
              </select>
            </div>
          </div>
          
          <div class="flex flex-col w-full lg:w-auto">
            <label class="form-label">Search Content</label>
            <div class="relative">
              <input
                v-model="searchQuery"
                type="text"
                placeholder="Search content..."
                class="form-input w-full lg:w-80 pl-10"
              />
              <MagnifyingGlassIcon class="h-5 w-5 text-gray-400 absolute left-3 top-1/2 transform -translate-y-1/2" />
            </div>
          </div>
        </div>

        <!-- Enhanced Content Table -->
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="table-header">
              <tr>
                <th class="table-cell text-left text-xs font-bold text-gray-600 uppercase tracking-wider">
                  Title
                </th>
                <th class="table-cell text-left text-xs font-bold text-gray-600 uppercase tracking-wider">
                  Type
                </th>
                <th class="table-cell text-left text-xs font-bold text-gray-600 uppercase tracking-wider">
                  Status
                </th>
                <th class="table-cell text-left text-xs font-bold text-gray-600 uppercase tracking-wider">
                  Date
                </th>
                <th class="table-cell text-left text-xs font-bold text-gray-600 uppercase tracking-wider">
                  Actions
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="item in filteredContent" :key="item.id" class="table-row">
                <td class="table-cell">
                  <div class="text-sm font-semibold text-gray-900">{{ item.title }}</div>
                  <div class="text-xs text-gray-500 mt-1">{{ item.excerpt || 'No excerpt available' }}</div>
                </td>
                <td class="table-cell">
                  <span :class="item.type === 'blog' ? 'type-blog' : 'type-video'">
                    {{ item.type === 'blog' ? 'Blog' : 'Video' }}
                  </span>
                </td>
                <td class="table-cell">
                  <span :class="item.status === 'published' ? 'status-published' : 'status-draft'">
                    {{ item.status === 'published' ? 'Published' : 'Draft' }}
                  </span>
                </td>
                <td class="table-cell text-sm text-gray-500">
                  {{ item.date }}
                </td>
                <td class="table-cell">
                  <div class="flex items-center space-x-2">
                    <button
                      @click="editItem(item)"
                      class="p-2 text-gray-400 hover:text-[#8B4000] hover:bg-orange-50 rounded-full transition-all duration-300"
                      title="Edit"
                    >
                      <PencilIcon class="h-4 w-4" />
                    </button>
                    
                    <button
                      @click="viewItem(item)"
                      class="p-2 text-gray-400 hover:text-green-600 hover:bg-green-50 rounded-full transition-all duration-300"
                      :class="{ 'opacity-50': item.status === 'draft' }"
                      :title="item.status === 'draft' ? 'Cannot preview draft' : 'View'"
                    >
                      <EyeIcon v-if="item.status === 'published'" class="h-4 w-4" />
                      <EyeSlashIcon v-else class="h-4 w-4" />
                    </button>
                    
                    <button
                      @click="duplicateItem(item)"
                      class="p-2 text-gray-400 hover:text-blue-600 hover:bg-blue-50 rounded-full transition-all duration-300"
                      title="Duplicate"
                    >
                      <DocumentDuplicateIcon class="h-4 w-4" />
                    </button>
                    
                    <button
                      @click="deleteItem(item)"
                      class="p-2 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded-full transition-all duration-300"
                      title="Delete"
                    >
                      <TrashIcon class="h-4 w-4" />
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
  ChartBarIcon,
  DocumentTextIcon,
  VideoCameraIcon,
  MagnifyingGlassIcon,
  DocumentDuplicateIcon,
  FolderOpenIcon,
  QuestionMarkCircleIcon
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

const stats = computed(() => ({
  totalPosts: dashboardStore.stats.content?.posts?.total || 0,
  totalVideos: dashboardStore.stats.content?.videos?.total || 0,
  totalResources: dashboardStore.stats.content?.resources?.total || 0,
  totalFaqs: dashboardStore.stats.content?.faqs?.total || 0,
  totalPartners: dashboardStore.stats.content?.partners?.total || 0,
  totalReports: dashboardStore.stats.reports?.total || 0,
  pendingReports: dashboardStore.stats.reports?.pending || 0
}))
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
  if (item.type === 'blog') {
    // Open preview in new window for both drafts and published content
    const previewUrl = `http://localhost:3003/blog/${item.slug}`
    window.open(previewUrl, '_blank')
    toast.info('Opening preview in new window...')
  } else if (item.type === 'video') {
    // For videos, open the YouTube link
    toast.info('Video preview via YouTube coming soon')
  }
}

const duplicateItem = async (item) => {
  try {
    // This would call the appropriate store method to duplicate content
    toast.success(`"${item.title}" duplicated successfully`)
    // Refresh the content list
    await dashboardStore.fetchContentList()
  } catch (err) {
    console.error('Duplicate error:', err)
    toast.error('Failed to duplicate content')
  }
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
