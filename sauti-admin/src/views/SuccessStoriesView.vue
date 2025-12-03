<template>
  <div class="p-6 space-y-6">
    <!-- Header -->
    <div class="flex justify-between items-start">
      <div>
        <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">Success Stories</h1>
        <p class="text-gray-600 mt-1">Share inspiring stories of impact and transformation</p>
      </div>
      <button
        @click="showCreateModal = true"
        class="btn-primary flex items-center"
      >
        <PlusIcon class="h-5 w-5 mr-2" />
        Add New Story
      </button>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total Stories</p>
            <p class="text-3xl font-bold text-gray-900 mt-2">{{ stats.total }}</p>
          </div>
          <div class="p-3 bg-blue-100 rounded-lg">
            <SparklesIcon class="h-8 w-8 text-blue-600" />
          </div>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Published</p>
            <p class="text-3xl font-bold text-green-600 mt-2">{{ stats.published }}</p>
          </div>
          <div class="p-3 bg-green-100 rounded-lg">
            <CheckCircleIcon class="h-8 w-8 text-green-600" />
          </div>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total Views</p>
            <p class="text-3xl font-bold text-purple-600 mt-2">{{ stats.views.toLocaleString() }}</p>
          </div>
          <div class="p-3 bg-purple-100 rounded-lg">
            <EyeIcon class="h-8 w-8 text-purple-600" />
          </div>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Featured</p>
            <p class="text-3xl font-bold text-orange-600 mt-2">{{ stats.featured }}</p>
          </div>
          <div class="p-3 bg-orange-100 rounded-lg">
            <HeartIcon class="h-8 w-8 text-orange-600" />
          </div>
        </div>
      </div>
    </div>

    <!-- Filters and Search -->
    <div class="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
      <div class="flex flex-col md:flex-row gap-4">
        <div class="flex-1 relative">
          <MagnifyingGlassIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search stories..."
            class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        </div>
        
        <select
          v-model="filterCategory"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Categories</option>
          <option v-for="cat in (Array.isArray(categories) ? categories : [])" :key="cat.id" :value="cat.slug">
            {{ cat.name }}
          </option>
        </select>

        <select
          v-model="filterStatus"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Status</option>
          <option value="PUBLISHED">Published</option>
          <option value="DRAFT">Draft</option>
        </select>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="text-center py-12">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
      <p class="mt-2 text-sm text-gray-500">Loading success stories...</p>
    </div>

    <!-- Stories Grid -->
    <div v-else class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <div
        v-for="story in filteredStories"
        :key="story.id"
        class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow duration-200"
      >
        <!-- Story Image -->
        <div class="relative h-56 bg-gradient-to-br from-orange-400 to-pink-500">
          <img
            v-if="story.featured_image"
            :src="story.featured_image"
            :alt="story.title"
            class="w-full h-full object-cover"
          />
          <div v-else class="w-full h-full flex items-center justify-center text-white">
            <PhotoIcon class="h-20 w-20 opacity-50" />
          </div>
          
          <!-- Status Badge -->
          <span
            class="absolute top-4 right-4 px-3 py-1 text-xs font-semibold rounded-full shadow-sm"
            :class="statusBadgeClass(story.status)"
          >
            {{ story.status }}
          </span>

          <!-- Category Badge -->
          <span class="absolute top-4 left-4 px-3 py-1 text-xs font-semibold rounded-full bg-white text-gray-700 shadow-sm">
            {{ story.category_name || 'Uncategorized' }}
          </span>
        </div>

        <!-- Story Content -->
        <div class="p-6">
          <div class="flex items-start justify-between mb-3">
            <h3 class="font-semibold text-xl text-gray-900 flex-1">
              {{ story.title }}
            </h3>
          </div>

          <p class="text-gray-600 mb-4 line-clamp-3">
            {{ story.excerpt || 'No excerpt available.' }}
          </p>

          <!-- Impact Stats -->
          <div class="grid grid-cols-2 gap-4 mb-4 py-4 border-y border-gray-100">
            <div class="text-center">
              <p class="text-2xl font-bold text-primary-600">{{ story.views_count || 0 }}</p>
              <p class="text-xs text-gray-500">Views</p>
            </div>
            <div class="text-center">
              <p class="text-2xl font-bold text-green-600">{{ story.is_featured ? 'Yes' : 'No' }}</p>
              <p class="text-xs text-gray-500">Featured</p>
            </div>
          </div>

          <!-- Meta Info -->
          <div class="flex items-center text-sm text-gray-500 mb-4">
            <CalendarIcon class="h-4 w-4 mr-1" />
            <span>{{ formatDate(story.published_at || story.created_at) }}</span>
            <span class="mx-2">•</span>
            <UserIcon class="h-4 w-4 mr-1" />
            <span>{{ story.author_name || story.author?.username || 'Unknown' }}</span>
          </div>

          <!-- Actions -->
          <div class="flex gap-2">
            <button
              @click="viewStory(story)"
              class="flex-1 px-3 py-2 bg-gray-100 text-gray-700 rounded-md hover:bg-gray-200 transition-colors duration-200 flex items-center justify-center text-sm font-medium"
            >
              <EyeIcon class="h-4 w-4 mr-1" />
              View
            </button>
            <button
              @click="editStory(story)"
              class="flex-1 px-3 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 transition-colors duration-200 flex items-center justify-center text-sm font-medium"
            >
              <PencilIcon class="h-4 w-4 mr-1" />
              Edit
            </button>
            <button
              v-if="story.status === 'PUBLISHED'"
              @click="shareStory(story)"
              class="px-3 py-2 bg-blue-100 text-blue-600 rounded-md hover:bg-blue-200 transition-colors duration-200"
            >
              <ShareIcon class="h-4 w-4" />
            </button>
            <button
              @click="deleteStory(story)"
              class="px-3 py-2 bg-red-100 text-red-600 rounded-md hover:bg-red-200 transition-colors duration-200"
            >
              <TrashIcon class="h-4 w-4" />
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-if="!loading && filteredStories.length === 0" class="bg-white rounded-lg shadow-sm border border-gray-200 p-12 text-center">
      <SparklesIcon class="mx-auto h-12 w-12 text-gray-400" />
      <h3 class="mt-2 text-sm font-medium text-gray-900">No stories found</h3>
      <p class="mt-1 text-sm text-gray-500">Start sharing inspiring success stories</p>
      <button
        @click="showCreateModal = true"
        class="mt-4 btn-primary"
      >
        Add New Story
      </button>
    </div>

    <!-- Create/Edit Success Story Modal -->
    <div v-if="showCreateModal || showEditModal" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full z-50">
      <div class="relative top-20 mx-auto p-5 border w-11/12 md:w-3/4 lg:w-1/2 shadow-lg rounded-md bg-white">
        <div class="mt-3">
          <h3 class="text-lg font-medium text-gray-900 mb-4">
            {{ showEditModal ? 'Edit Success Story' : 'Create New Success Story' }}
          </h3>
          
          <form @submit.prevent="submitStory" class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Title</label>
              <input
                v-model="form.title"
                type="text"
                required
                class="form-input"
                placeholder="Enter the story title..."
              />
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Excerpt</label>
              <textarea
                v-model="form.excerpt"
                rows="2"
                class="form-input"
                placeholder="Brief summary of the story..."
              ></textarea>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Content</label>
              <textarea
                v-model="form.content"
                required
                rows="6"
                class="form-input"
                placeholder="Full story content..."
              ></textarea>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Category</label>
                <select v-model="form.category" class="form-select" required>
                  <option value="">Select Category</option>
                  <option v-for="cat in (Array.isArray(categories) ? categories : [])" :key="cat.id" :value="cat.id">
                    {{ cat.name }}
                  </option>
                </select>
              </div>
              
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Status</label>
                <select v-model="form.status" class="form-select">
                  <option value="DRAFT">Draft</option>
                  <option value="PUBLISHED">Published</option>
                </select>
              </div>
            </div>

            <div class="flex items-center space-x-2">
              <input
                type="checkbox"
                id="featured"
                v-model="form.is_featured"
                class="h-4 w-4 text-primary-600 focus:ring-primary-500 border-gray-300 rounded"
              />
              <label for="featured" class="text-sm font-medium text-gray-700">Featured Story</label>
            </div>
            
            <div class="flex justify-end space-x-3 pt-4">
              <button
                type="button"
                @click="closeModal"
                class="btn-outline"
              >
                Cancel
              </button>
              <button
                type="submit"
                :disabled="loading"
                class="btn-primary"
              >
                {{ loading ? 'Saving...' : (showEditModal ? 'Update Story' : 'Create Story') }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useToast } from 'vue-toastification'
import { usePostsStore } from '@/stores/posts'
import {
  PlusIcon,
  MagnifyingGlassIcon,
  SparklesIcon,
  CheckCircleIcon,
  EyeIcon,
  HeartIcon,
  PhotoIcon,
  PencilIcon,
  TrashIcon,
  ShareIcon,
  CalendarIcon,
  UserIcon
} from '@heroicons/vue/24/outline'

const toast = useToast()
const postsStore = usePostsStore()

// Reactive data
const searchQuery = ref('')
const filterCategory = ref('')
const filterStatus = ref('')
const showCreateModal = ref(false)
const showEditModal = ref(false)
const editForm = ref({})

// Use store data
const stories = computed(() => postsStore.posts)
const loading = computed(() => postsStore.loading)
const categories = computed(() => postsStore.categories)

// Form data
const form = ref({
  title: '',
  excerpt: '',
  content: '',
  category: '',
  status: 'DRAFT',
  is_featured: false
})

// Computed properties
const stats = computed(() => {
  const storiesList = Array.isArray(stories.value) ? stories.value : []
  const total = storiesList.length
  const published = storiesList.filter(s => s.status === 'PUBLISHED').length
  const views = storiesList.reduce((sum, s) => sum + (s.views_count || 0), 0)
  const featured = storiesList.filter(s => s.is_featured).length
  
  return {
    total,
    published,
    views,
    featured
  }
})

const filteredStories = computed(() => {
  let filtered = Array.isArray(stories.value) ? stories.value : []

  // Filter by search query
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(story =>
      story.title.toLowerCase().includes(query) ||
      (story.excerpt && story.excerpt.toLowerCase().includes(query))
    )
  }

  // Filter by category
  if (filterCategory.value) {
    filtered = filtered.filter(story => story.category?.slug === filterCategory.value)
  }

  // Filter by status
  if (filterStatus.value) {
    filtered = filtered.filter(story => story.status === filterStatus.value)
  }

  return filtered
})

const statusBadgeClass = (status) => {
  const statusStr = status?.toUpperCase() || ''
  const classes = {
    PUBLISHED: 'bg-green-100 text-green-800',
    DRAFT: 'bg-yellow-100 text-yellow-800'
  }
  return classes[statusStr] || 'bg-gray-100 text-gray-800'
}

const formatDate = (date) => {
  if (!date) return 'Recently'
  try {
    return new Date(date).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    })
  } catch (error) {
    return 'Recently'
  }
}

const viewStory = (story) => {
  window.open(`http://localhost:5173/blog/${story.slug}`, '_blank')
}

const editStory = (story) => {
  editForm.value = { ...story }
  form.value = {
    title: story.title,
    excerpt: story.excerpt || '',
    content: story.content || '',
    category: story.category?.id || '',
    status: story.status,
    is_featured: story.is_featured || false
  }
  showEditModal.value = true
}

const shareStory = (story) => {
  const url = `http://localhost:5173/blog/${story.slug}`
  if (navigator.share) {
    navigator.share({
      title: story.title,
      text: story.excerpt,
      url: url
    }).catch(() => {
      copyToClipboard(url)
    })
  } else {
    copyToClipboard(url)
  }
}

const copyToClipboard = (text) => {
  navigator.clipboard.writeText(text).then(() => {
    toast.success('Link copied to clipboard!')
  }).catch(() => {
    toast.error('Failed to copy link')
  })
}

const deleteStory = async (story) => {
  if (!confirm(`Delete "${story.title}"?`)) {
    return
  }
  
  try {
    await postsStore.deletePost(story.slug)
    toast.success('Success story deleted successfully')
  } catch (err) {
    console.error('Delete error:', err)
    toast.error('Failed to delete success story')
  }
}

const submitStory = async () => {
  try {
    if (showEditModal.value) {
      await postsStore.updatePost(editForm.value.slug, form.value)
      toast.success('Success story updated successfully')
    } else {
      await postsStore.createPost(form.value)
      toast.success('Success story created successfully')
    }
    
    await fetchStories()
    closeModal()
  } catch (err) {
    console.error('Submit error:', err)
    toast.error(showEditModal.value ? 'Failed to update success story' : 'Failed to create success story')
  }
}

const closeModal = () => {
  showCreateModal.value = false
  showEditModal.value = false
  form.value = {
    title: '',
    excerpt: '',
    content: '',
    category: '',
    status: 'DRAFT',
    is_featured: false
  }
  editForm.value = {}
}

const fetchStories = async () => {
  try {
    // Fetch posts filtered by "Success Stories" category
    const successCategory = categories.value.find(cat => cat.slug === 'success-stories')
    if (successCategory) {
      await postsStore.fetchPosts({ category: 'success-stories' })
    } else {
      await postsStore.fetchPosts()
    }
    await postsStore.fetchCategories()
  } catch (err) {
    console.error('Failed to fetch success stories:', err)
    toast.error('Failed to load success stories')
  }
}

// Lifecycle
onMounted(() => {
  fetchStories()
})
</script>
