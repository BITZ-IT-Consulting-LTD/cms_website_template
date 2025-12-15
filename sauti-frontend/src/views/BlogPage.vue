<template>
  <div class="section-padding">
    <div class="container-custom">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="mb-2 text-4xl md:text-5xl font-extrabold text-gray-900">{{ blogTitle }}</h1>
        <p class="text-gray-600 max-w-3xl mx-auto">{{ blogSubtitle }}</p>
      </div>

      <!-- Filters -->
      <div class="mb-8">
        <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-4 flex items-center gap-3 max-w-3xl mx-auto">
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35M11 19a8 8 0 100-16 8 8 0 000 16z"/></svg>
          <input v-model="filters.search" @input="debouncedSearch" type="search" :placeholder="blogSearchPlaceholder" class="flex-1 focus:outline-none" />
        </div>
        <div class="flex flex-wrap justify-center gap-3 mt-4">
          <button class="pill pill-primary" @click="setType('All')">{{ blogAllButton }}</button>
          <button class="px-3 py-1 rounded-full bg-gray-100" @click="setType('Articles')">{{ blogArticlesButton }}</button>
          <select v-model="filters.category" @change="fetchFilteredPosts" class="form-select max-w-xs">
            <option value="">{{ blogCategoriesDropdown }}</option>
            <option v-for="cat in categories" :key="cat.id" :value="cat.slug">{{ cat.name }}</option>
          </select>
        </div>
      </div>

      <!-- Loading -->
      <AppLoader v-if="loading" :message="blogLoading" />

      <!-- Posts Grid (YouTube-style like Videos) -->
      <div v-else-if="posts.length" class="space-y-10">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          <BlogCard v-for="post in posts" :key="post.id" :post="post" />
        </div>
        <!-- Pagination -->
        <div class="flex items-center justify-center gap-4 select-none">
          <button class="px-2 text-gray-600 hover:text-gray-900" @click="setPage('<')">‹</button>
          <button
            v-for="n in pageNumbers"
            :key="n + '-pg'"
            @click="setPage(n)"
            :class="[
              'w-9 h-9 rounded-full flex items-center justify-center text-sm',
              filters.page === n ? 'bg-secondary-500 text-white' : 'text-gray-700 hover:bg-gray-100'
            ]"
          >
            {{ n }}
          </button>
          <button class="px-2 text-gray-600 hover:text-gray-900" @click="setPage('>')">›</button>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="text-center py-16">
        <svg class="w-24 h-24 mx-auto text-gray-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
        </svg>
        <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ blogNoResults }}</h3>
        <p class="text-gray-600">{{ blogNoResultsSubtitle }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed } from 'vue'
import BlogCard from '@/components/blog/BlogCard.vue'
import AppLoader from '@/components/common/AppLoader.vue'
import { useBlogStore } from '@/store/blog'
import { useContentStore } from '@/store/content'

defineOptions({
  name: 'BlogPage'
})

const blogStore = useBlogStore()
const contentStore = useContentStore()

const posts = ref([])
const categories = ref([])
const loading = ref(false)
const totalPages = ref(1)

// Computed properties for content
const blogTitle = computed(() => contentStore.getContent('blog_title', 'Blogs'))
const blogSubtitle = computed(() => contentStore.getContent('blog_subtitle', 'Insights, stories, and news from the front lines of child protection in Uganda.'))
const blogSearchPlaceholder = computed(() => contentStore.getContent('blog_search_placeholder', 'Search stories...'))
const blogAllButton = computed(() => contentStore.getContent('blog_all_button', 'All'))
const blogArticlesButton = computed(() => contentStore.getContent('blog_articles_button', 'Articles'))
const blogCategoriesDropdown = computed(() => contentStore.getContent('blog_categories_dropdown', 'Categories'))
const blogLoading = computed(() => contentStore.getContent('blog_loading', 'Loading stories...'))
const blogNoResults = computed(() => contentStore.getContent('blog_no_results', 'No stories found'))
const blogNoResultsSubtitle = computed(() => contentStore.getContent('blog_no_results_subtitle', 'Try adjusting your filters or check back later for new content.'))

const filters = reactive({
  category: '',
  search: '',
  page: 1,
  type: 'All', // All | Articles | Videos
})

let debounceTimer = null

onMounted(async () => {
  await Promise.all([
    fetchCategories(),
    fetchFilteredPosts()
  ])
})

async function fetchCategories() {
  try {
    const data = await blogStore.fetchCategories()
    categories.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
  } catch (error) {
    console.error('Failed to fetch categories:', error)
    categories.value = []
  }
}

async function fetchFilteredPosts() {
  loading.value = true
  
  try {
    // Fetch posts from backend
    const params = {
      status: 'PUBLISHED', // Only show published posts
      page: filters.page
    }
    
    // Add category filter if selected
    if (filters.category) {
      params.category = filters.category
    }
    
    // Add search filter if entered
    if (filters.search) {
      params.search = filters.search
    }
    
    const response = await blogStore.fetchPosts(params)
    
    // Handle paginated response
    const data = response.results || response
    posts.value = Array.isArray(data) ? data : []
    
    // Calculate total pages
    if (response.count) {
      totalPages.value = Math.ceil(response.count / 12) // Assuming 12 posts per page
    } else {
      totalPages.value = 1
    }
    
    // If no posts found and not using filters, show fallback message
    if (posts.value.length === 0 && !filters.search && !filters.category) {
      console.log('No posts found in database - you can create posts in the admin panel')
    }
    
  } catch (error) {
    console.error('Failed to fetch posts:', error)
    posts.value = []
  } finally {
    loading.value = false
  }
}

function debouncedSearch() {
  clearTimeout(debounceTimer)
  debounceTimer = setTimeout(() => {
    filters.page = 1
    fetchFilteredPosts()
  }, 400)
}

// Update type filter to trigger fetch
function setType(t) {
  filters.type = t
  fetchFilteredPosts()
}

const pageNumbers = computed(() => {
  if (totalPages.value <= 5) {
    return Array.from({ length: totalPages.value }, (_, i) => i + 1)
  }
  return [1, 2, 3, '…', totalPages.value]
})

function setPage(p) {
  if (p === '…') return
  if (p === '<') filters.page = Math.max(1, filters.page - 1)
  else if (p === '>') filters.page = Math.min(totalPages.value, filters.page + 1)
  else filters.page = p
  fetchFilteredPosts()
  window.scrollTo({ top: 0, behavior: 'smooth' })
}
</script>
