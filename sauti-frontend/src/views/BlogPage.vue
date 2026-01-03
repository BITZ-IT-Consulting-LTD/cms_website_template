<template>
  <div class="bg-sauti-neutral min-h-screen py-16 md:py-24">
    <div class="container-custom">
      <!-- Header -->
      <div class="text-center mb-16 max-w-4xl mx-auto">
        <h1 class="text-4xl md:text-5xl lg:text-7xl font-black text-sauti-darkGreen mb-6 tracking-tight">
          Sauti <span class="text-sauti-blue">Stories</span>
        </h1>
        <p class="text-xl md:text-2xl text-sauti-darkGreen/70 max-w-3xl mx-auto font-bold leading-relaxed">{{
          blogSubtitle }}</p>
      </div>

      <!-- Filters -->
      <div
        class="bg-sauti-white rounded-[2.5rem] border-2 border-sauti-neutral p-6 md:p-8 mb-12 shadow-sm max-w-5xl mx-auto">
        <div class="flex flex-col md:flex-row gap-6 items-center">
          <div class="relative flex-1 w-full group">
            <svg
              class="absolute left-6 top-1/2 -translate-y-1/2 w-6 h-6 text-sauti-darkGreen/30 group-focus-within:text-sauti-blue transition-colors"
              fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                d="M21 21l-4.35-4.35M11 19a8 8 0 100-16 8 8 0 000 16z" />
            </svg>
            <input v-model="filters.search" @input="debouncedSearch" type="search" :placeholder="blogSearchPlaceholder"
              class="w-full pl-16 pr-6 py-4 bg-sauti-neutral rounded-2xl border-2 border-transparent focus:border-sauti-blue focus:bg-sauti-white outline-none transition-all font-bold text-sauti-darkGreen placeholder:text-sauti-darkGreen/30" />
          </div>

          <div class="flex items-center gap-4 w-full md:w-auto">
            <div class="relative flex-1 md:w-64">
              <select v-model="filters.category" @change="fetchFilteredPosts"
                class="w-full appearance-none pl-6 pr-12 py-4 bg-sauti-neutral rounded-2xl border-2 border-transparent focus:border-sauti-blue focus:bg-sauti-white outline-none transition-all font-black text-sauti-darkGreen uppercase tracking-widest text-xs cursor-pointer">
                <option value="">{{ blogCategoriesDropdown }}</option>
                <option v-for="cat in categories" :key="cat.id" :value="cat.slug">{{ cat.name }}</option>
              </select>
              <svg class="absolute right-4 top-1/2 -translate-y-1/2 w-5 h-5 text-sauti-darkGreen/40 pointer-events-none"
                fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M19 9l-7 7-7-7" />
              </svg>
            </div>
          </div>
        </div>

        <div class="flex flex-wrap justify-center gap-3 mt-8">
          <button v-for="type in ['All', 'Articles']" :key="type" @click="setType(type)" :class="[
            'px-8 py-2 rounded-full font-black uppercase tracking-widest text-xs transition-all border-2',
            filters.type === type
              ? 'bg-sauti-darkGreen border-sauti-darkGreen text-sauti-white shadow-lg shadow-sauti-darkGreen/20'
              : 'bg-sauti-white border-sauti-neutral text-sauti-darkGreen/60 hover:border-sauti-darkGreen hover:text-sauti-darkGreen'
          ]">
            {{ type === 'All' ? blogAllButton : blogArticlesButton }}
          </button>
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
          <button class="px-2 text-sauti-darkGreen font-black hover:text-sauti-blue" @click="setPage('<')">‹</button>
          <button v-for="n in pageNumbers" :key="n + '-pg'" @click="setPage(n)" :class="[
            'w-9 h-9 rounded-full flex items-center justify-center text-sm font-bold transition-all',
            filters.page === n ? 'bg-sauti-blue text-sauti-white shadow-lg' : 'text-sauti-darkGreen hover:bg-sauti-neutral'
          ]">
            {{ n }}
          </button>
          <button class="px-2 text-sauti-darkGreen font-black hover:text-sauti-blue" @click="setPage('>')">›</button>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else
        class="text-center py-24 bg-sauti-white rounded-[3.5rem] border-2 border-dashed border-sauti-neutral max-w-4xl mx-auto">
        <div class="w-24 h-24 bg-sauti-neutral/30 rounded-3xl flex items-center justify-center mx-auto mb-8">
          <svg class="w-12 h-12 text-sauti-darkGreen/30" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
              d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
        </div>
        <h3 class="text-2xl font-black text-sauti-darkGreen mb-4">{{ blogNoResults }}</h3>
        <p class="text-lg text-sauti-darkGreen/50 font-bold">{{ blogNoResultsSubtitle }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, reactive, onMounted, computed } from 'vue'
  import BlogCard from '@/components/blog/BlogCard.vue'
  import AppLoader from '@/components/common/AppLoader.vue'
  import { useBlogStore } from '@/store/blog'
  import { useSettingsStore } from '@/store/settings'

  defineOptions({
    name: 'BlogPage'
  })

  const blogStore = useBlogStore()
  const settingsStore = useSettingsStore()

  const posts = ref([])
  const categories = ref([])
  const loading = ref(false)
  const totalPages = ref(1)

  // Computed properties for content
  const blogTitle = computed(() => settingsStore.settings.blog_title || 'Blogs')
  const blogSubtitle = computed(() => settingsStore.settings.blog_subtitle || 'Insights, stories, and news from the front lines of child protection in Uganda.')
  const blogSearchPlaceholder = computed(() => settingsStore.settings.blog_search_placeholder || 'Search stories...')
  const blogAllButton = computed(() => settingsStore.settings.blog_all_button || 'All')
  const blogArticlesButton = computed(() => settingsStore.settings.blog_articles_button || 'Articles')
  const blogCategoriesDropdown = computed(() => settingsStore.settings.blog_categories_dropdown || 'Categories')
  const blogLoading = computed(() => settingsStore.settings.blog_loading || 'Loading stories...')
  const blogNoResults = computed(() => settingsStore.settings.blog_no_results || 'No stories found')
  const blogNoResultsSubtitle = computed(() => settingsStore.settings.blog_no_results_subtitle || 'Try adjusting your filters or check back later for new content.')

  const filters = reactive({
    category: '',
    search: '',
    page: 1,
    type: 'All', // All | Articles | Videos
  })

  let debounceTimer = null

  onMounted(async () => {
    await settingsStore.fetchGlobalSettings()
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
        page: filters.page,
        post_type: 'BLOG' // Only show blog posts
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
