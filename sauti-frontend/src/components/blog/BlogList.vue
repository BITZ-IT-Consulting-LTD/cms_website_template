<template>
  <div class="space-y-6">
    <!-- Loading State -->
    <div v-if="loading" class="text-center py-12">
      <AppLoader />
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="bg-red-50 border border-red-200 rounded-lg p-6 text-center">
      <p class="text-red-700">{{ error }}</p>
      <button @click="$emit('retry')" class="mt-4 btn-primary">
        Try Again
      </button>
    </div>

    <!-- Empty State -->
    <div v-else-if="posts.length === 0" class="bg-gray-50 border border-gray-200 rounded-lg p-12 text-center">
      <svg class="w-16 h-16 mx-auto text-gray-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z" />
      </svg>
      <h3 class="text-lg font-semibold text-gray-700 mb-2">No Posts Found</h3>
      <p class="text-gray-500">Check back later for new content.</p>
    </div>

    <!-- Blog Posts Grid -->
    <div v-else>
      <!-- Featured Post (if exists) -->
      <div v-if="featuredPost" class="mb-8">
        <h2 class="text-xl font-bold text-gray-900 mb-4 flex items-center">
          <svg class="w-6 h-6 mr-2 text-secondary" fill="currentColor" viewBox="0 0 20 20">
            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
          </svg>
          Featured Story
        </h2>
        <BlogCard :post="featuredPost" featured class="shadow-lg" />
      </div>

      <!-- Regular Posts Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <BlogCard 
          v-for="post in regularPosts" 
          :key="post.slug" 
          :post="post" 
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
              ? 'bg-primary text-white hover:bg-blue-600'
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
              ? 'bg-primary text-white hover:bg-blue-600'
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
import { computed } from 'vue'
import BlogCard from './BlogCard.vue'
import AppLoader from '../common/AppLoader.vue'

const props = defineProps({
  posts: {
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

defineEmits(['retry', 'previous', 'next'])

// Computed properties
const featuredPost = computed(() => {
  return props.posts.find(post => post.is_featured)
})

const regularPosts = computed(() => {
  return props.posts.filter(post => !post.is_featured)
})

const showPagination = computed(() => {
  return props.totalPages > 1 && !props.loading
})
</script>

<style scoped>
/* Component-specific styles if needed */
</style>
