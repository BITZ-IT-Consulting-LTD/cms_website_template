<template>
  <div class="bg-neutral py-16 md:py-24 min-h-screen">
    <div class="container-custom">
      <!-- Header -->
      <div class="text-center mb-16">
        <h1 class="text-4xl md:text-5xl lg:text-7xl font-black text-darkGreen mb-4 tracking-tight">
          Official <span class="text-blue">News</span>
        </h1>
        <p class="text-xl text-darkGreen/70 font-medium max-w-2xl mx-auto">Latest official updates, press releases
          and announcements from Sauti 116.</p>
      </div>

      <!-- Filters -->
      <div class="mb-12 max-w-4xl mx-auto">
        <div class="flex flex-col md:flex-row gap-4">
          <div
            class="flex-1 bg-white rounded-3xl shadow-sm border-2 border-neutral p-2 flex items-center gap-3">
            <div
              class="w-12 h-12 bg-neutral/50 rounded-2xl flex items-center justify-center text-darkGreen/40">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3"
                  d="M21 21l-4.35-4.35M11 19a8 8 0 100-16 8 8 0 000 16z" />
              </svg>
            </div>
            <input v-model="filters.search" @input="debouncedSearch" type="search" placeholder="Search news archives..."
              class="flex-1 bg-transparent border-none focus:ring-0 font-bold text-darkGreen placeholder-darkGreen/30" />
          </div>
          <div class="md:w-64">
            <select v-model="filters.category" @change="fetchFilteredPosts"
              class="w-full bg-white rounded-3xl border-2 border-neutral py-4 px-6 font-black text-darkGreen focus:border-blue focus:ring-4 focus:ring-blue/10 appearance-none">
              <option value="">All Categories</option>
              <option v-for="cat in categories" :key="cat.id" :value="cat.slug">{{ cat.name }}</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Loading -->
      <AppLoader v-if="loading" message="Loading news..." />

      <div v-else-if="posts.length" class="space-y-16">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
          <BlogCard v-for="post in posts" :key="post.id" :post="post" />
        </div>
        <!-- Pagination -->
        <div
          class="flex items-center justify-center gap-2 select-none bg-white p-3 rounded-full border border-neutral w-fit mx-auto shadow-sm">
          <button
            class="w-10 h-10 rounded-full flex items-center justify-center text-darkGreen hover:bg-neutral transition-colors"
            @click="setPage('<')">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M15 19l-7-7 7-7" />
            </svg>
          </button>
          <div class="flex gap-1">
            <button v-for="n in pageNumbers" :key="n + '-pg'" @click="setPage(n)" :class="[
              'w-10 h-10 rounded-full flex items-center justify-center text-sm font-black transition-all duration-300',
              filters.page === n ? 'bg-blue text-white shadow-lg shadow-blue/30' : 'text-darkGreen/60 hover:bg-neutral'
            ]">
              {{ n }}
            </button>
          </div>
          <button
            class="w-10 h-10 rounded-full flex items-center justify-center text-darkGreen hover:bg-neutral transition-colors"
            @click="setPage('>')">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M9 5l7 7-7 7" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="text-center py-24 bg-white rounded-[3.5rem] border-2 border-dashed border-neutral">
        <div
          class="w-24 h-24 bg-neutral/30 rounded-full flex items-center justify-center mx-auto mb-6 text-darkGreen/20">
          <svg class="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
        </div>
        <h3 class="text-3xl font-black text-darkGreen mb-4">No news items found</h3>
        <p class="text-darkGreen/50 font-bold max-w-sm mx-auto">Try adjusting your filters or search keywords to
          find what you're looking for.</p>
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
    name: 'NewsPage'
  })

  const blogStore = useBlogStore()
  const settingsStore = useSettingsStore()

  const posts = ref([])
  const categories = ref([])
  const loading = ref(false)
  const totalPages = ref(1)

  // Computed properties for content (Keeping defaults or simple overrides since separate page)
  // Use settings if you added specific settings for news, otherwise hardcode or reuse logic.
  // For now, simpler to hardcode News specific titles to differentiate.

  const filters = reactive({
    category: '',
    search: '',
    page: 1,
    post_type: 'NEWS'
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
        post_type: 'NEWS'
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
