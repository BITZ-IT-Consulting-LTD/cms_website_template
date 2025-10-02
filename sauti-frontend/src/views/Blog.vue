<template>
  <div class="section-padding">
    <div class="container-custom">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="mb-4">News & Updates</h1>
        <p class="text-xl text-gray-600">
          Stay informed with the latest news, stories, and updates from Sauti
        </p>
      </div>

      <!-- Filters -->
      <div class="flex flex-wrap gap-4 mb-8">
        <select v-model="filters.category" @change="fetchFilteredPosts" class="form-select max-w-xs">
          <option value="">All Categories</option>
          <option v-for="cat in categories" :key="cat.id" :value="cat.slug">
            {{ cat.name }}
          </option>
        </select>

        <input
          v-model="filters.search"
          @input="debouncedSearch"
          type="search"
          placeholder="Search articles..."
          class="form-input max-w-md"
        />
      </div>

      <!-- Loading -->
      <Loader v-if="loading" message="Loading articles..." />

      <!-- Posts Grid -->
      <div v-else-if="posts.length" class="space-y-8">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <BlogCard v-for="post in posts" :key="post.id" :post="post" />
        </div>

        <!-- Pagination -->
        <div v-if="pagination.count > posts.length" class="flex justify-center gap-4">
          <button
            v-if="pagination.previous"
            @click="loadPreviousPage"
            class="btn-outline"
          >
            ← Previous
          </button>
          <button
            v-if="pagination.next"
            @click="loadNextPage"
            class="btn-primary"
          >
            Next →
          </button>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="text-center py-16">
        <svg class="w-24 h-24 mx-auto text-gray-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
        </svg>
        <h3 class="text-xl font-semibold text-gray-900 mb-2">No articles found</h3>
        <p class="text-gray-600">Try adjusting your filters or check back later for new content.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useBlogStore } from '@/store/blog'
import BlogCard from '@/components/blog/BlogCard.vue'
import Loader from '@/components/common/Loader.vue'

const blogStore = useBlogStore()

const posts = ref([])
const categories = ref([])
const loading = ref(false)
const pagination = ref({})

const filters = reactive({
  category: '',
  search: '',
  page: 1,
})

let debounceTimer = null

onMounted(async () => {
  await fetchCategories()
  await fetchFilteredPosts()
})

async function fetchCategories() {
  try {
    categories.value = await blogStore.fetchCategories()
  } catch (error) {
    console.error('Failed to load categories:', error)
  }
}

async function fetchFilteredPosts() {
  loading.value = true
  try {
    const params = {
      page: filters.page,
    }
    if (filters.category) params.category = filters.category
    if (filters.search) params.search = filters.search

    await blogStore.fetchPosts(params)
    posts.value = blogStore.posts
    pagination.value = blogStore.pagination
  } catch (error) {
    console.error('Failed to load posts:', error)
  } finally {
    loading.value = false
  }
}

function debouncedSearch() {
  clearTimeout(debounceTimer)
  debounceTimer = setTimeout(() => {
    filters.page = 1
    fetchFilteredPosts()
  }, 500)
}

function loadPreviousPage() {
  if (pagination.value.previous) {
    filters.page--
    fetchFilteredPosts()
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

function loadNextPage() {
  if (pagination.value.next) {
    filters.page++
    fetchFilteredPosts()
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}
</script>
