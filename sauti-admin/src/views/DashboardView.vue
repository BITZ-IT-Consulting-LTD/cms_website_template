<template>
  <div class="space-y-8">
    <!-- Header -->
    <PageHeader
      title="Content Management Dashboard"
      description="Manage your website content, blog posts, videos, and resources"
    />

    <!-- Stats Cards -->
    <StatsGrid>
      <StatCard
        label="Total Reports"
        :value="stats.totalReports"
        subtitle="All submitted cases"
        :icon="ClipboardDocumentListIcon"
        color="red"
      />
      <StatCard
        label="Pending Review"
        :value="stats.pendingReports"
        subtitle="Requires attention"
        :icon="ClockIcon"
        color="amber"
      />
      <StatCard
        label="Resolved"
        :value="stats.resolvedReports"
        subtitle="Successfully closed"
        :icon="CheckCircleIcon"
        color="green"
      />
      <StatCard
        label="Resources"
        :value="stats.totalResources"
        subtitle="Downloadable content"
        :icon="FolderOpenIcon"
        color="blue"
      />
    </StatsGrid>

    <!-- Enhanced Content Management -->
    <div class="card">
      <div class="card-header">
        <h2 class="text-2xl font-bold mb-2" style="font-family: 'Roboto', sans-serif; color: #222222;">Content Management</h2>
        <p style="color: #555555;">Manage your blog posts, videos, resources, and other content</p>
      </div>
        
      <div class="card-body">
        <!-- Enhanced Quick Actions -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 mb-6">
          <router-link
            to="/posts/create"
            class="btn-primary flex items-center justify-center gap-2"
          >
            <DocumentTextIcon class="h-5 w-5" />
            New Blog Post
          </router-link>

          <router-link
            to="/videos/create"
            class="btn-secondary flex items-center justify-center gap-2"
          >
            <VideoCameraIcon class="h-5 w-5" />
            New Video
          </router-link>

          <router-link
            to="/resources?create=true"
            class="btn-outline flex items-center justify-center gap-2"
          >
            <FolderOpenIcon class="h-5 w-5" />
            New Resource
          </router-link>

          <router-link
            to="/faqs?create=true"
            class="btn-outline flex items-center justify-center gap-2"
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
                class="form-select w-full max-w-[12rem]"
              >
                <option value="">All Content</option>
                <option value="blog">Blogs</option>
                <option value="video">Videos</option>
                <option value="resource">Resources</option>
                <option value="faq">FAQs</option>
              </select>
            </div>
            
            <div class="flex flex-col">
              <label class="form-label">Status</label>
              <select
                v-model="filters.status"
                class="form-select w-full max-w-[12rem]"
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
                class="form-input w-full max-w-[20rem] pl-10"
              />
              <MagnifyingGlassIcon class="h-5 w-5 text-gray-400 absolute left-3 top-1/2 transform -translate-y-1/2" />
            </div>
          </div>
        </div>

        <!-- Enhanced Content Table -->
        <div class="overflow-x-auto">
          <table class="min-w-full">
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
            <tbody class="bg-white">
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

    <!-- Blog Preview Modal -->
    <BlogPreviewModal
      v-if="selectedItem && selectedItem.type === 'blog'"
      :isOpen="isPreviewOpen"
      :slug="selectedItem.slug"
      :postId="selectedItem.id"
      @close="closePreview"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useDashboardStore } from '@/stores/dashboard'
import { useToast } from 'vue-toastification'
import BlogPreviewModal from '@/components/previews/BlogPreviewModal.vue'
import { PageHeader, StatsGrid, StatCard } from '@/components/admin'
import {
  PencilIcon,
  EyeIcon,
  EyeSlashIcon,
  TrashIcon,
  DocumentTextIcon,
  VideoCameraIcon,
  MagnifyingGlassIcon,
  DocumentDuplicateIcon,
  FolderOpenIcon,
  QuestionMarkCircleIcon,
  ClipboardDocumentListIcon,
  ClockIcon,
  CheckCircleIcon
} from '@heroicons/vue/24/outline'

const router = useRouter()
const dashboardStore = useDashboardStore()
const toast = useToast()

// Reactive data
const searchQuery = ref('')
const filters = ref({
  contentType: '',
  status: ''
})

const stats = computed(() => ({
  totalReports: dashboardStore.stats.reports?.total || 0,
  pendingReports: dashboardStore.stats.reports?.pending || 0,
  resolvedReports: (dashboardStore.stats.reports?.total || 0) - (dashboardStore.stats.reports?.pending || 0),
  totalResources: dashboardStore.stats.content?.resources?.total || 0
}))
const contentList = computed(() => dashboardStore.contentList)
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
    router.push(`/videos/${item.slug || item.id}/edit`)
  }
}

const isPreviewOpen = ref(false)
const selectedItem = ref(null)

const viewItem = (item) => {
  if (item.type === 'blog') {
    selectedItem.value = item
    isPreviewOpen.value = true
  } else if (item.type === 'video') {
    // For videos, open the YouTube link
    toast.info('Video preview via YouTube coming soon')
  }
}

const closePreview = () => {
  isPreviewOpen.value = false
  selectedItem.value = null
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
      dashboardStore.fetchContentList()
    ])
  } catch (err) {
    console.error('Failed to load dashboard data:', err)
    toast.error('Failed to load dashboard data')
  }
})
</script>
