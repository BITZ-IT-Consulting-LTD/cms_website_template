<template>
  <div class="p-6 space-y-6">
    <!-- Header -->
    <div class="flex justify-between items-start">
      <div>
        <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">FAQs</h1>
        <p class="text-gray-600 mt-1">Manage frequently asked questions</p>
      </div>
      <button
        @click="showCreateModal = true"
        class="btn-primary flex items-center"
      >
        <PlusIcon class="h-5 w-5 mr-2" />
        Add New FAQ
      </button>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
      <div class="stats-card">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total FAQs</p>
            <p class="text-3xl font-bold text-gray-900 mt-2">{{ stats.total }}</p>
          </div>
          <div class="p-3 bg-blue-100 rounded-lg">
            <QuestionMarkCircleIcon class="h-8 w-8 text-blue-600" />
          </div>
        </div>
      </div>

      <div class="stats-card">
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

      <div class="stats-card">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total Views</p>
            <p class="text-3xl font-bold text-purple-600 mt-2">{{ formatNumber(stats.views) }}</p>
          </div>
          <div class="p-3 bg-purple-100 rounded-lg">
            <EyeIcon class="h-8 w-8 text-purple-600" />
          </div>
        </div>
      </div>

      <div class="stats-card">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Helpful Votes</p>
            <p class="text-3xl font-bold text-orange-600 mt-2">{{ formatNumber(stats.helpful) }}</p>
          </div>
          <div class="p-3 bg-orange-100 rounded-lg">
            <HandThumbUpIcon class="h-8 w-8 text-orange-600" />
          </div>
        </div>
      </div>
    </div>

    <!-- Search and Filters -->
    <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <!-- Search -->
        <div class="relative">
          <MagnifyingGlassIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search FAQs..."
            class="form-input pl-10"
          />
        </div>
        
        <!-- Category Filter -->
        <select v-model="categoryFilter" class="form-select">
          <option value="">All Categories</option>
          <option v-for="category in categories" :key="category.id" :value="category.name">
            {{ category.name }}
          </option>
        </select>
        
        <!-- Status Filter -->
        <select v-model="statusFilter" class="form-select">
          <option value="">All Status</option>
          <option value="PUBLISHED">✅ Published</option>
          <option value="DRAFT">⏳ Draft</option>
        </select>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="text-center py-12">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
      <p class="mt-2 text-sm text-gray-500">Loading FAQs...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="text-center py-12">
      <div class="text-red-600 mb-4">
        <QuestionMarkCircleIcon class="h-12 w-12 mx-auto mb-2" />
        <h3 class="text-lg font-medium">Failed to load FAQs</h3>
        <p class="text-sm text-gray-500">{{ error }}</p>
      </div>
      <button @click="fetchFaqs" class="btn-primary">
        Try Again
      </button>
    </div>

    <!-- FAQs List -->
    <div v-else class="space-y-4">
      <div v-for="faq in filteredFaqs" :key="faq.id" class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div class="flex items-start justify-between">
          <div class="flex-1">
            <div class="flex items-center space-x-3 mb-2">
              <h3 class="text-lg font-semibold text-gray-900 line-clamp-2">{{ faq.question }}</h3>
              <span
                class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
                :class="{
                  'bg-green-100 text-green-800': faq.status === 'published',
                  'bg-yellow-100 text-yellow-800': faq.status === 'draft'
                }"
              >
                {{ faq.status }}
              </span>
            </div>
            
            <p class="text-gray-600 mb-4 line-clamp-3">{{ faq.answer }}</p>
            
            <div class="flex items-center space-x-6 text-sm text-gray-500">
              <span class="flex items-center">
                <EyeIcon class="h-4 w-4 mr-1" />
                {{ formatNumber(faq.views_count || 0) }} views
              </span>
              <span class="flex items-center">
                <HandThumbUpIcon class="h-4 w-4 mr-1" />
                {{ formatNumber(faq.helpful_count || 0) }} helpful
              </span>
              <span>{{ faq.category?.name || 'Uncategorized' }}</span>
              <span>{{ formatDate(faq.updated_at || faq.created_at) }}</span>
            </div>
          </div>
          
          <div class="flex items-center space-x-2 ml-4">
            <button
              @click="previewFaq(faq)"
              class="text-blue-600 hover:text-blue-900 p-2"
              title="Preview"
            >
              <EyeIcon class="h-4 w-4" />
            </button>
            <button
              @click="editFaq(faq)"
              class="text-primary-600 hover:text-primary-900 p-2"
              title="Edit"
            >
              <PencilIcon class="h-4 w-4" />
            </button>
            <button
              @click="duplicateFaq(faq)"
              class="text-green-600 hover:text-green-900 p-2"
              title="Duplicate"
            >
              <DocumentDuplicateIcon class="h-4 w-4" />
            </button>
            <button
              @click="deleteFaq(faq)"
              class="text-red-600 hover:text-red-900 p-2"
              title="Delete"
            >
              <TrashIcon class="h-4 w-4" />
            </button>
          </div>
        </div>
      </div>
      
      <!-- Empty State -->
      <div v-if="filteredFaqs.length === 0" class="text-center py-12">
        <QuestionMarkCircleIcon class="mx-auto h-12 w-12 text-gray-400" />
        <h3 class="mt-2 text-sm font-medium text-gray-900">No FAQs found</h3>
        <p class="mt-1 text-sm text-gray-500">
          {{ searchQuery ? 'Try adjusting your search criteria.' : 'Get started by creating your first FAQ.' }}
        </p>
        <div class="mt-6" v-if="!searchQuery">
          <button @click="showCreateModal = true" class="btn-primary">
            <PlusIcon class="h-4 w-4 mr-2" />
            Add New FAQ
          </button>
        </div>
      </div>
    </div>

    <!-- Create/Edit FAQ Modal -->
    <div v-if="showCreateModal || showEditModal" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full z-50">
      <div class="relative top-20 mx-auto p-5 border w-11/12 md:w-3/4 lg:w-1/2 shadow-lg rounded-md bg-white">
        <div class="mt-3">
          <h3 class="text-lg font-medium text-gray-900 mb-4">
            {{ showEditModal ? 'Edit FAQ' : 'Create New FAQ' }}
          </h3>
          
          <form @submit.prevent="submitFaq" class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Question</label>
              <input
                v-model="form.question"
                type="text"
                required
                class="form-input"
                placeholder="Enter the question..."
              />
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Answer</label>
              <textarea
                v-model="form.answer"
                required
                rows="4"
                class="form-input"
                placeholder="Enter the answer..."
              ></textarea>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Category</label>
                <select v-model="form.category" class="form-select">
                  <option value="">Select Category</option>
                  <option v-for="category in categories" :key="category.id" :value="category.id">
                    {{ category.name }}
                  </option>
                </select>
              </div>
              
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Status</label>
                <select v-model="form.status" class="form-select">
                  <option value="draft">Draft</option>
                  <option value="published">Published</option>
                </select>
              </div>
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
                {{ loading ? 'Saving...' : (showEditModal ? 'Update FAQ' : 'Create FAQ') }}
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
import { useFaqsStore } from '@/stores/faqs'
import {
  PlusIcon,
  MagnifyingGlassIcon,
  QuestionMarkCircleIcon,
  CheckCircleIcon,
  EyeIcon,
  HandThumbUpIcon,
  PencilIcon,
  DocumentDuplicateIcon,
  TrashIcon
} from '@heroicons/vue/24/outline'

const toast = useToast()
const faqsStore = useFaqsStore()

// Reactive data
const searchQuery = ref('')
const categoryFilter = ref('')
const statusFilter = ref('')
const showCreateModal = ref(false)
const showEditModal = ref(false)
const editForm = ref({})

// Use store data
const faqs = computed(() => faqsStore.faqs)
const loading = computed(() => faqsStore.loading)
const error = computed(() => faqsStore.error)
const categories = computed(() => faqsStore.categories)

// Form data
const form = ref({
  question: '',
  answer: '',
  category: '',
  status: 'draft'
})

// Computed properties
const stats = computed(() => {
  const total = faqs.value.length
  const published = faqs.value.filter(f => f.status === 'published').length
  const views = faqs.value.reduce((sum, f) => sum + (f.views_count || 0), 0)
  const helpful = faqs.value.reduce((sum, f) => sum + (f.helpful_count || 0), 0)
  
  return {
    total,
    published,
    views,
    helpful
  }
})

const filteredFaqs = computed(() => {
  let filtered = faqs.value

  // Filter by search query
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(faq =>
      faq.question.toLowerCase().includes(query) ||
      faq.answer.toLowerCase().includes(query)
    )
  }

  // Filter by category
  if (categoryFilter.value) {
    filtered = filtered.filter(faq => faq.category?.name === categoryFilter.value)
  }

  // Filter by status
  if (statusFilter.value) {
    filtered = filtered.filter(faq => faq.status === statusFilter.value)
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

const previewFaq = (faq) => {
  if (faq.status === 'draft') {
    toast.warning('Cannot preview draft content')
    return
  }
  
  // For now, just show a message
  toast.info('Preview functionality coming soon')
}

const editFaq = (faq) => {
  editForm.value = { ...faq }
  form.value = {
    question: faq.question,
    answer: faq.answer,
    category: faq.category?.id || '',
    status: faq.status
  }
  showEditModal.value = true
}

const duplicateFaq = async (faq) => {
  try {
    const duplicateData = {
      question: `${faq.question} (Copy)`,
      answer: faq.answer,
      category: faq.category?.id,
      status: 'draft'
    }
    
    await faqsStore.createFaq(duplicateData)
    toast.success(`"${faq.question}" duplicated successfully`)
  } catch (err) {
    console.error('Duplicate error:', err)
    toast.error('Failed to duplicate FAQ')
  }
}

const deleteFaq = async (faq) => {
  if (!confirm(`Are you sure you want to delete "${faq.question}"?`)) {
    return
  }
  
  try {
    await faqsStore.deleteFaq(faq.id)
    toast.success('FAQ deleted successfully')
  } catch (err) {
    console.error('Delete error:', err)
    toast.error('Failed to delete FAQ')
  }
}

const submitFaq = async () => {
  try {
    if (showEditModal.value) {
      await faqsStore.updateFaq(editForm.value.id, form.value)
      toast.success('FAQ updated successfully')
    } else {
      await faqsStore.createFaq(form.value)
      toast.success('FAQ created successfully')
    }
    
    closeModal()
  } catch (err) {
    console.error('Submit error:', err)
    toast.error(showEditModal.value ? 'Failed to update FAQ' : 'Failed to create FAQ')
  }
}

const closeModal = () => {
  showCreateModal.value = false
  showEditModal.value = false
  form.value = {
    question: '',
    answer: '',
    category: '',
    status: 'draft'
  }
  editForm.value = {}
}

const fetchFaqs = async () => {
  try {
    await faqsStore.fetchFaqs()
    await faqsStore.fetchCategories()
  } catch (err) {
    console.error('Failed to fetch FAQs:', err)
    toast.error('Failed to load FAQs')
  }
}

// Lifecycle
onMounted(() => {
  fetchFaqs()
})
</script>