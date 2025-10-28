<template>
  <div class="p-6">
    <!-- Enhanced Header -->
    <div class="flex items-center justify-between mb-8">
      <div>
        <h1 class="text-3xl font-bold text-gray-900 mb-2" style="font-family: 'Roboto', sans-serif;">Blog Posts Management</h1>
        <p class="text-lg text-gray-600">Create, edit, and manage blog posts and articles for the Sauti platform</p>
      </div>
      
      <div class="flex gap-3">
        <router-link
          to="/drafts"
          class="btn-outline flex items-center gap-2"
        >
          <PencilSquareIcon class="h-5 w-5" />
          View Drafts
        </router-link>
        
        <router-link
          to="/posts/create"
          class="btn-primary flex items-center gap-2"
        >
          <PlusIcon class="h-5 w-5" />
          Create New Post
        </router-link>
      </div>
    </div>

    <!-- Enhanced Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
      <div class="stats-card group">
        <div class="flex items-center justify-between mb-4">
          <div class="p-3 bg-blue-100 rounded-2xl group-hover:bg-blue-200 transition-colors duration-300">
            <DocumentTextIcon class="h-6 w-6 text-blue-600" />
          </div>
          <div class="text-right">
            <div class="stats-number">{{ stats.total }}</div>
            <div class="stats-label">Total Posts</div>
          </div>
        </div>
        <div class="text-sm text-gray-600">All blog posts</div>
      </div>
      
      <div class="stats-card group">
        <div class="flex items-center justify-between mb-4">
          <div class="p-3 bg-green-100 rounded-2xl group-hover:bg-green-200 transition-colors duration-300">
            <CheckCircleIcon class="h-6 w-6 text-green-600" />
          </div>
          <div class="text-right">
            <div class="stats-number">{{ stats.published }}</div>
            <div class="stats-label">Published</div>
          </div>
        </div>
        <div class="text-sm text-gray-600">Live on website</div>
      </div>
      
      <div class="stats-card group">
        <div class="flex items-center justify-between mb-4">
          <div class="p-3 bg-yellow-100 rounded-2xl group-hover:bg-yellow-200 transition-colors duration-300">
            <ClockIcon class="h-6 w-6 text-yellow-600" />
          </div>
          <div class="text-right">
            <div class="stats-number">{{ stats.draft }}</div>
            <div class="stats-label">Drafts</div>
          </div>
        </div>
        <div class="text-sm text-gray-600">Work in progress</div>
      </div>
      
      <div class="stats-card group">
        <div class="flex items-center justify-between mb-4">
          <div class="p-3 bg-purple-100 rounded-2xl group-hover:bg-purple-200 transition-colors duration-300">
            <EyeIcon class="h-6 w-6 text-purple-600" />
          </div>
          <div class="text-right">
            <div class="stats-number">{{ formatNumber(stats.totalViews) }}</div>
            <div class="stats-label">Total Views</div>
          </div>
        </div>
        <div class="text-sm text-gray-600">All time views</div>
      </div>
    </div>

    <!-- Search and Filters -->
    <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
        <!-- Search -->
        <div class="relative">
          <MagnifyingGlassIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search posts..."
            class="form-input pl-10"
          />
        </div>
        
        <!-- Status Filter -->
        <select v-model="statusFilter" class="form-select">
          <option value="">All Status</option>
          <option value="published">Published</option>
          <option value="draft">Draft</option>
          <option value="archived">Archived</option>
        </select>
        
        <!-- Category Filter -->
        <select v-model="categoryFilter" class="form-select">
          <option value="">All Categories</option>
          <option v-for="category in (Array.isArray(categories) ? categories : [])" :key="category.id" :value="category.name">
            {{ category.name }}
          </option>
        </select>
        
        <!-- Author Filter -->
        <select v-model="authorFilter" class="form-select">
          <option value="">All Authors</option>
          <option v-for="author in authors" :key="author" :value="author">
            {{ author }}
          </option>
        </select>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="text-center py-12">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
      <p class="mt-2 text-sm text-gray-500">Loading posts...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="text-center py-12">
      <div class="text-red-600 mb-4">
        <DocumentTextIcon class="h-12 w-12 mx-auto mb-2" />
        <h3 class="text-lg font-medium">Failed to load posts</h3>
        <p class="text-sm text-gray-500">{{ error }}</p>
      </div>
      <button @click="fetchPosts" class="btn-primary">
        Try Again
      </button>
    </div>

    <!-- Posts Table -->
    <div v-else class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="table-header">
            <tr>
              <th class="table-cell">Post</th>
              <th class="table-cell">Author</th>
              <th class="table-cell">Category</th>
              <th class="table-cell">Status</th>
              <th class="table-cell">Views</th>
              <th class="table-cell">Date</th>
              <th class="table-cell">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="post in filteredPosts" :key="post.id" class="table-row hover:bg-gray-50">
              <td class="px-6 py-4">
                <div class="flex items-center">
                  <div class="flex-shrink-0 h-12 w-12">
                    <div v-if="post.featured_image" class="h-12 w-12 rounded-lg overflow-hidden">
                      <img :src="post.featured_image" :alt="post.title" class="h-full w-full object-cover">
                    </div>
                    <div v-else class="h-12 w-12 bg-gray-100 rounded-lg flex items-center justify-center">
                      <DocumentTextIcon class="h-6 w-6 text-gray-400" />
                    </div>
                  </div>
                  <div class="ml-4">
                    <div class="text-sm font-medium text-gray-900 line-clamp-2">
                      {{ post.title }}
                    </div>
                    <div class="text-sm text-gray-500 line-clamp-1">
                      {{ post.excerpt || post.content?.substring(0, 100) + '...' }}
                    </div>
                  </div>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ post.author_name || 'Unknown' }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ post.category?.name || 'Uncategorized' }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span
                  class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
                  :class="{
                    'bg-green-100 text-green-800': post.status === 'published',
                    'bg-yellow-100 text-yellow-800': post.status === 'draft',
                    'bg-gray-100 text-gray-800': post.status === 'archived'
                  }"
                >
                  {{ post.status }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ formatNumber(post.views_count || 0) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ formatDate(post.published_at || post.created_at) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <div class="flex items-center justify-end space-x-2">
                  <button
                    @click="previewPost(post)"
                    class="text-blue-600 hover:text-blue-900"
                    title="Preview"
                  >
                    <EyeIcon class="h-4 w-4" />
                  </button>
                  <router-link
                    :to="`/posts/${post.slug || post.id}/edit`"
                    class="text-primary-600 hover:text-primary-900"
                    title="Edit"
                  >
                    <PencilIcon class="h-4 w-4" />
                  </router-link>
                  <button
                    @click="duplicatePost(post)"
                    class="text-green-600 hover:text-green-900"
                    title="Duplicate"
                  >
                    <DocumentDuplicateIcon class="h-4 w-4" />
                  </button>
                  <button
                    @click="deletePost(post)"
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
      <div v-if="filteredPosts.length === 0" class="text-center py-12">
        <DocumentTextIcon class="mx-auto h-12 w-12 text-gray-400" />
        <h3 class="mt-2 text-sm font-medium text-gray-900">No posts found</h3>
        <p class="mt-1 text-sm text-gray-500">
          {{ searchQuery ? 'Try adjusting your search criteria.' : 'Get started by creating your first post.' }}
        </p>
        <div class="mt-6" v-if="!searchQuery">
          <router-link to="/posts/create" class="btn-primary">
            <PlusIcon class="h-4 w-4 mr-2" />
            Create New Post
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
import { usePostsStore } from '@/stores/posts'
import {
  PlusIcon,
  DocumentTextIcon,
  CheckCircleIcon,
  ClockIcon,
  EyeIcon,
  MagnifyingGlassIcon,
  PencilIcon,
  TrashIcon,
  DocumentDuplicateIcon,
  PencilSquareIcon
} from '@heroicons/vue/24/outline'

const toast = useToast()
const router = useRouter()
const route = useRoute()
const postsStore = usePostsStore()

// Reactive data
const searchQuery = ref('')
const statusFilter = ref('')
const categoryFilter = ref('')
const authorFilter = ref('')

// Use store data
const posts = computed(() => postsStore.posts)
const loading = computed(() => postsStore.loading)
const error = computed(() => postsStore.error)
const categories = computed(() => postsStore.categories)
const authors = ref([])

// Computed properties
const stats = computed(() => {
  const total = posts.value.length
  const published = posts.value.filter(p => p.status === 'published').length
  const draft = posts.value.filter(p => p.status === 'draft').length
  const totalViews = posts.value.reduce((sum, p) => sum + (p.views_count || 0), 0)
  
  return {
    total,
    published,
    draft,
    totalViews
  }
})

const filteredPosts = computed(() => {
  let filtered = posts.value

  // Filter by search query
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(post =>
      post.title.toLowerCase().includes(query) ||
      (post.excerpt && post.excerpt.toLowerCase().includes(query)) ||
      (post.content && post.content.toLowerCase().includes(query))
    )
  }

  // Filter by status
  if (statusFilter.value) {
    filtered = filtered.filter(post => post.status === statusFilter.value)
  }

  // Filter by category
  if (categoryFilter.value) {
    filtered = filtered.filter(post => post.category?.name === categoryFilter.value)
  }

  // Filter by author
  if (authorFilter.value) {
    filtered = filtered.filter(post => post.author_name === authorFilter.value)
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

const previewPost = (post) => {
  if (post.status === 'draft') {
    toast.warning('Cannot preview draft content')
    return
  }
  
  // Open in new tab
  const url = `/blog/${post.slug}`
  window.open(url, '_blank')
}

const duplicatePost = async (post) => {
  try {
    const duplicateData = {
      ...post,
      title: `${post.title} (Copy)`,
      slug: `${post.slug}-copy-${Date.now()}`,
      status: 'draft'
    }
    
    await postsStore.createPost(duplicateData)
    toast.success(`"${post.title}" duplicated successfully`)
  } catch (err) {
    console.error('Duplicate error:', err)
    toast.error('Failed to duplicate post')
  }
}

const deletePost = async (post) => {
  if (!confirm(`Are you sure you want to delete "${post.title}"?`)) {
    return
  }
  
  try {
    await postsStore.deletePost(post.slug || post.id)
    toast.success('Post deleted successfully')
  } catch (err) {
    console.error('Delete error:', err)
    toast.error('Failed to delete post')
  }
}

const fetchPosts = async () => {
  try {
    await postsStore.fetchPosts()
    await postsStore.fetchCategories()
    
    // Extract unique authors
    const uniqueAuthors = [...new Set(posts.value.map(p => p.author_name).filter(Boolean))]
    authors.value = uniqueAuthors
  } catch (err) {
    console.error('Failed to fetch posts:', err)
    toast.error('Failed to load posts')
  }
}

// Watch for route changes to refresh data
watch(() => route.path, (newPath) => {
  if (newPath === '/posts') {
    fetchPosts()
  }
})

// Lifecycle
onMounted(() => {
  fetchPosts()
})
</script>