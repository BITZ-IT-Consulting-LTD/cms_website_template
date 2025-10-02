<template>
  <div class="space-y-6">
    <!-- Filters Section -->
    <div class="bg-white rounded-lg shadow-md p-6">
      <h2 class="text-lg font-bold text-gray-900 mb-4">Filter Resources</h2>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <!-- Category Filter -->
        <div>
          <label for="category-filter" class="form-label">Category</label>
          <select
            id="category-filter"
            v-model="filters.category"
            @change="$emit('filter-change', filters)"
            class="form-input"
          >
            <option value="">All Categories</option>
            <option v-for="cat in categories" :key="cat.slug" :value="cat.slug">
              {{ cat.name }}
            </option>
          </select>
        </div>

        <!-- Language Filter -->
        <div>
          <label for="language-filter" class="form-label">Language</label>
          <select
            id="language-filter"
            v-model="filters.language"
            @change="$emit('filter-change', filters)"
            class="form-input"
          >
            <option value="">All Languages</option>
            <option value="en">English</option>
            <option value="lg">Luganda</option>
            <option value="sw">Swahili</option>
          </select>
        </div>

        <!-- Search -->
        <div>
          <label for="search-filter" class="form-label">Search</label>
          <input
            id="search-filter"
            type="text"
            v-model="filters.search"
            @input="debouncedSearch"
            placeholder="Search resources..."
            class="form-input"
          />
        </div>
      </div>

      <!-- Active Filters -->
      <div v-if="hasActiveFilters" class="mt-4 flex items-center space-x-2">
        <span class="text-sm text-gray-600">Active filters:</span>
        
        <button
          v-if="filters.category"
          @click="clearFilter('category')"
          class="inline-flex items-center space-x-1 px-2 py-1 bg-teal-100 text-teal-700 text-sm rounded-full hover:bg-teal-200"
        >
          <span>Category: {{ getCategoryName(filters.category) }}</span>
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
          </svg>
        </button>

        <button
          v-if="filters.language"
          @click="clearFilter('language')"
          class="inline-flex items-center space-x-1 px-2 py-1 bg-teal-100 text-teal-700 text-sm rounded-full hover:bg-teal-200"
        >
          <span>Language: {{ getLanguageName(filters.language) }}</span>
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
          </svg>
        </button>

        <button
          @click="clearAllFilters"
          class="text-sm text-gray-600 hover:text-gray-900 underline"
        >
          Clear all
        </button>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="text-center py-12">
      <Loader />
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="bg-red-50 border border-red-200 rounded-lg p-6 text-center">
      <p class="text-red-700">{{ error }}</p>
      <button @click="$emit('retry')" class="mt-4 btn-primary">
        Try Again
      </button>
    </div>

    <!-- Empty State -->
    <div v-else-if="resources.length === 0" class="bg-gray-50 border border-gray-200 rounded-lg p-12 text-center">
      <svg class="w-16 h-16 mx-auto text-gray-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
      </svg>
      <h3 class="text-lg font-semibold text-gray-700 mb-2">No Resources Found</h3>
      <p class="text-gray-500">Try adjusting your filters or check back later for new resources.</p>
    </div>

    <!-- Resources Grid -->
    <div v-else>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <ResourceCard
          v-for="resource in resources"
          :key="resource.slug"
          :resource="resource"
          @download="handleDownload"
        />
      </div>

      <!-- Pagination -->
      <div v-if="showPagination" class="mt-8 flex justify-center items-center space-x-2">
        <button
          @click="$emit('previous')"
          :disabled="!hasPrevious"
          :class="[
            'px-4 py-2 rounded-md transition-colors',
            hasPrevious
              ? 'bg-teal-500 text-white hover:bg-teal-600'
              : 'bg-gray-200 text-gray-400 cursor-not-allowed'
          ]"
          aria-label="Previous page"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
        </button>

        <span class="px-4 py-2 text-gray-700">
          Page {{ currentPage }} of {{ totalPages }}
        </span>

        <button
          @click="$emit('next')"
          :disabled="!hasNext"
          :class="[
            'px-4 py-2 rounded-md transition-colors',
            hasNext
              ? 'bg-teal-500 text-white hover:bg-teal-600'
              : 'bg-gray-200 text-gray-400 cursor-not-allowed'
          ]"
          aria-label="Next page"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import ResourceCard from './ResourceCard.vue'
import Loader from '../common/Loader.vue'

const props = defineProps({
  resources: {
    type: Array,
    default: () => []
  },
  categories: {
    type: Array,
    default: () => []
  },
  loading: {
    type: Boolean,
    default: false
  },
  error: {
    type: String,
    default: null
  },
  currentPage: {
    type: Number,
    default: 1
  },
  totalPages: {
    type: Number,
    default: 1
  },
  hasPrevious: {
    type: Boolean,
    default: false
  },
  hasNext: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['filter-change', 'retry', 'previous', 'next', 'download'])

// Filters state
const filters = ref({
  category: '',
  language: '',
  search: ''
})

// Computed properties
const hasActiveFilters = computed(() => {
  return filters.value.category || filters.value.language || filters.value.search
})

const showPagination = computed(() => {
  return props.totalPages > 1 && !props.loading
})

// Methods
const getCategoryName = (slug) => {
  const category = props.categories.find(cat => cat.slug === slug)
  return category ? category.name : slug
}

const getLanguageName = (code) => {
  const languages = {
    en: 'English',
    lg: 'Luganda',
    sw: 'Swahili'
  }
  return languages[code] || code
}

const clearFilter = (filterName) => {
  filters.value[filterName] = ''
  emit('filter-change', filters.value)
}

const clearAllFilters = () => {
  filters.value = {
    category: '',
    language: '',
    search: ''
  }
  emit('filter-change', filters.value)
}

// Debounced search
let searchTimeout
const debouncedSearch = () => {
  clearTimeout(searchTimeout)
  searchTimeout = setTimeout(() => {
    emit('filter-change', filters.value)
  }, 500)
}

const handleDownload = (resource) => {
  emit('download', resource)
}
</script>

<style scoped>
/* Component-specific styles if needed */
</style>
