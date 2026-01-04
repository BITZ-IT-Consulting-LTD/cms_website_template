<template>
  <div class="p-6">
    <!-- Page Header -->
    <PageHeader title="FAQs" description="Manage frequently asked questions" action-label="Add New FAQ"
      :action-icon="PlusIcon" @action="showCreateModal = true" />

    <!-- Mini Dashboard -->
    <StatsGrid>
      <StatCard label="Total FAQs" :value="stats.total" :icon="QuestionMarkCircleIcon" color="blue" />
      <StatCard label="Published" :value="stats.published" :icon="CheckCircleIcon" color="green" />
      <StatCard label="Total Views" :value="formatNumber(stats.views)" :icon="EyeIcon" color="purple" />
      <StatCard label="Helpful Votes" :value="formatNumber(stats.helpful)" :icon="HandThumbUpIcon" color="orange" />
    </StatsGrid>

    <!-- Filters -->
    <FilterBar v-model="filters" search-placeholder="Search FAQs..." :status-options="statusOptions"
      status-label="All Status" :custom-options="categoryOptions" custom-label="All Categories" />

    <!-- Loading State -->
    <LoadingState v-if="loading" message="Loading FAQs..." />

    <!-- FAQs List -->
    <div v-else class="space-y-4">
      <div v-for="faq in filteredFaqs" :key="faq.id" class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div class="flex items-start justify-between">
          <div class="flex-1">
            <div class="flex items-center space-x-3 mb-2">
              <h3 class="text-lg font-semibold text-gray-900 line-clamp-2">{{ faq.question }}</h3>
              <span class="inline-flex px-2 py-1 text-xs font-semibold rounded-full" :class="{
                'bg-green-100 text-green-800': faq.status === 'published',
                'bg-yellow-100 text-yellow-800': faq.status === 'draft'
              }">
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
            <button @click="previewFaq(faq)" class="text-blue-600 hover:text-blue-900 p-2" title="Preview">
              <EyeIcon class="h-4 w-4" />
            </button>
            <button @click="editFaq(faq)" class="text-primary-600 hover:text-primary-900 p-2" title="Edit">
              <PencilIcon class="h-4 w-4" />
            </button>
            <button @click="duplicateFaq(faq)" class="text-green-600 hover:text-green-900 p-2" title="Duplicate">
              <DocumentDuplicateIcon class="h-4 w-4" />
            </button>
            <button @click="deleteFaq(faq)" class="text-red-600 hover:text-red-900 p-2" title="Delete">
              <TrashIcon class="h-4 w-4" />
            </button>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <EmptyState v-if="filteredFaqs.length === 0" :icon="QuestionMarkCircleIcon" title="No FAQs found"
        :message="searchQuery || filters.status || filters.custom ? 'Try adjusting your search criteria.' : 'Get started by creating your first FAQ.'"
        :action-label="!searchQuery && !filters.status && !filters.custom ? 'Add New FAQ' : null"
        :action-icon="PlusIcon" @action="showCreateModal = true" />
    </div>

    <!-- Create/Edit FAQ Modal -->
    <div v-if="showCreateModal || showEditModal"
      class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full z-50">
      <div class="relative top-20 mx-auto p-5 border w-11/12 md:w-3/4 lg:w-1/2 shadow-lg rounded-md bg-white">
        <div class="mt-3">
          <h3 class="text-lg font-medium text-gray-900 mb-4">
            {{ showEditModal ? 'Edit FAQ' : 'Create New FAQ' }}
          </h3>

          <form @submit.prevent="submitFaq" class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Question</label>
              <input v-model="form.question" type="text" required class="form-input"
                placeholder="Enter the question..." />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Answer</label>
              <textarea v-model="form.answer" required rows="4" class="form-input"
                placeholder="Enter the answer..."></textarea>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Category</label>
                <select v-model="form.category" class="form-select">
                  <option value="">Select Category</option>
                  <option v-for="category in (Array.isArray(categories) ? categories : [])" :key="category.id"
                    :value="category.id">
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
              <button type="button" @click="closeModal" class="btn-outline">
                Cancel
              </button>
              <button type="submit" :disabled="loading" class="btn-primary">
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
  import { useRoute } from 'vue-router'
  import { useToast } from 'vue-toastification'
  import { useFaqsStore } from '@/stores/faqs'
  import { PageHeader, StatsGrid, StatCard, FilterBar, LoadingState, EmptyState } from '@/components/admin'
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

  const route = useRoute()
  const toast = useToast()
  const faqsStore = useFaqsStore()

  // Filters using FilterBar pattern
  const filters = ref({
    search: '',
    status: '',
    custom: ''
  })

  // Backward compatibility
  const searchQuery = computed({
    get: () => filters.value.search,
    set: (val) => { filters.value.search = val }
  })
  const statusFilter = computed({
    get: () => filters.value.status,
    set: (val) => { filters.value.status = val }
  })
  const categoryFilter = computed({
    get: () => filters.value.custom,
    set: (val) => { filters.value.custom = val }
  })

  const showCreateModal = ref(false)
  const showEditModal = ref(false)
  const editForm = ref({})

  // Use store data
  const faqs = computed(() => faqsStore.faqs)
  const loading = computed(() => faqsStore.loading)
  const error = computed(() => faqsStore.error)
  const categories = computed(() => faqsStore.categories)

  // Filter options
  const statusOptions = [
    { value: 'PUBLISHED', label: '✅ Published' },
    { value: 'DRAFT', label: '⏳ Draft' }
  ]

  const categoryOptions = computed(() => {
    if (!Array.isArray(categories.value)) return []
    return categories.value.map(c => ({ value: c.name, label: c.name }))
  })

  // Form data
  const form = ref({
    question: '',
    answer: '',
    category: '',
    status: 'draft'
  })

  // Computed properties
  const stats = computed(() => {
    const faqsList = Array.isArray(faqs.value) ? faqs.value : []
    const total = faqsList.length
    const published = faqsList.filter(f => f.status === 'published').length
    const views = faqsList.reduce((sum, f) => sum + (f.views_count || 0), 0)
    const helpful = faqsList.reduce((sum, f) => sum + (f.helpful_count || 0), 0)

    return {
      total,
      published,
      views,
      helpful
    }
  })

  const filteredFaqs = computed(() => {
    let filtered = Array.isArray(faqs.value) ? faqs.value : []

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
    if (route.query.create === 'true') {
      showCreateModal.value = true
    }
  })
</script>