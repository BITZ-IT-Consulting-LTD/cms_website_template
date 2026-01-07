<template>
  <div class="bg-neutral-white min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <h1 class="page-header-title">
          HELPLINE NEWS
        </h1>
        <p class="page-header-subtitle">
          {{ blogSubtitle || 'Official updates, impact reports, and protection news from the Sauti 116 Helpline.' }}
        </p>

        <!-- News in a Flash (Flash Pattern) -->
        <div
          class="mt-16 bg-neutral-white p-8 md:p-12 rounded-[3rem] border-2 border-primary/10 shadow-sm max-w-5xl mx-auto text-left">
          <h2 class="campaign-header text-xl text-primary mb-8 flex items-center gap-3">
            <ShieldCheckIcon class="w-6 h-6 text-primary" />
            Impact at a Glance
          </h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="space-y-2">
              <p class="text-black font-bold">Community Reach</p>
              <p class="text-black/60 text-sm">Active protection programs in **all districts** across Uganda.</p>
            </div>
            <div class="space-y-2">
              <p class="text-black font-bold">Verified Reports</p>
              <p class="text-black/60 text-sm">Over **1,000 cases** resolved through official channels this month.
              </p>
            </div>
            <div class="space-y-2">
              <p class="text-black font-bold">Emergency 116</p>
              <p class="text-black/60 text-sm">Response times for critical reports maintained at **under 5
                minutes**.</p>
            </div>
          </div>
        </div>
      </div>
    </header>

    <div class="container-custom section-padding">
      <!-- 2. Search & Filters -->
      <div class="bg-neutral-offwhite rounded-[2.5rem] p-8 mb-16 shadow-none max-w-5xl mx-auto">
        <div class="flex flex-col md:flex-row gap-8 items-center">
          <div class="relative flex-1 w-full group">
            <MagnifyingGlassIcon
              class="absolute left-6 top-1/2 -translate-y-1/2 w-6 h-6 text-primary group-focus-within:text-secondary transition-colors" />
            <input v-model="filters.search" @input="debouncedSearch" type="search" :placeholder="blogSearchPlaceholder"
              class="w-full pl-16 pr-6 py-4 bg-neutral-white rounded-2xl border-none shadow-sm focus:shadow-md outline-none transition-all font-bold text-secondary placeholder:text-primary/40" />
          </div>

          <div class="relative w-full md:w-64">
            <select v-model="filters.category" @change="fetchFilteredPosts"
              class="w-full appearance-none pl-6 pr-12 py-4 bg-neutral-white rounded-2xl border-none shadow-sm focus:shadow-md outline-none transition-all font-bold text-secondary uppercase tracking-widest text-xs cursor-pointer">
              <option value="">{{ blogCategoriesDropdown }}</option>
              <option v-for="cat in categories" :key="cat.id" :value="cat.slug">{{ cat.name }}</option>
            </select>
            <ChevronDownIcon
              class="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-primary pointer-events-none" />
          </div>
        </div>

        <div class="flex flex-wrap justify-center gap-4 mt-8 pt-8 border-t border-secondary/5">
          <button v-for="type in ['All', 'Articles']" :key="type" @click="setType(type)" :class="[
            'px-8 py-3 rounded-2xl font-bold uppercase tracking-widest text-[10px] transition-all border-none',
            filters.type === type
              ? 'bg-secondary text-neutral-white shadow-xl'
              : 'bg-neutral-white text-secondary shadow-sm hover:shadow-md'
          ]">
            {{ type === 'All' ? blogAllButton : blogArticlesButton }}
          </button>
        </div>
      </div>

      <!-- 3. Content Area -->
      <AppLoader v-if="loading" :message="blogLoading" />

      <div v-else-if="posts.length" class="space-y-16">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
          <BlogCard v-for="post in posts" :key="post.id" :post="post" />
        </div>

        <!-- Pagination -->
        <div class="flex items-center justify-center gap-4">
          <button @click="setPage('<')" class="btn btn-outline border-none shadow-sm hover:shadow-md !p-3">
            <ChevronLeftIcon class="w-5 h-5" />
          </button>

          <div class="flex items-center gap-2">
            <button v-for="n in pageNumbers" :key="n + '-pg'" @click="setPage(n)" :class="[
              'w-12 h-12 rounded-2xl flex items-center justify-center font-bold transition-all border-none',
              filters.page === n
                ? 'bg-primary text-neutral-white shadow-xl'
                : 'bg-neutral-white text-secondary shadow-sm hover:shadow-md'
            ]">
              {{ n }}
            </button>
          </div>

          <button @click="setPage('>')" class="btn btn-outline border-none shadow-sm hover:shadow-md !p-3">
            <ChevronRightIcon class="w-5 h-5" />
          </button>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="text-center py-24 bg-neutral-white rounded-[4rem] shadow-lg max-w-4xl mx-auto">
        <div
          class="w-24 h-24 bg-neutral-offwhite/10 rounded-3xl flex items-center justify-center mx-auto mb-8 shadow-sm">
          <ExclamationCircleIcon class="w-12 h-12 text-primary" />
        </div>
        <h3 class="text-3xl font-bold text-secondary mb-4">{{ blogNoResults }}</h3>
        <p class="text-xl text-black/50 font-bold max-w-2xl mx-auto">{{ blogNoResultsSubtitle }}</p>
        <button @click="filters.search = ''; filters.category = ''; fetchFilteredPosts()" class="btn btn-outline mt-10">
          Clear all filters
        </button>
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
  import {
    MagnifyingGlassIcon,
    ChevronDownIcon,
    ChevronLeftIcon,
    ChevronRightIcon,
    ExclamationCircleIcon,
    ShieldCheckIcon
  } from '@heroicons/vue/24/outline'

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
  const blogSubtitle = computed(() => settingsStore.settings.blog_subtitle || 'Insights, stories, and news from the front lines of child protection in Uganda.')
  const blogSearchPlaceholder = computed(() => settingsStore.settings.blog_search_placeholder || 'Search stories...')
  const blogAllButton = computed(() => settingsStore.settings.blog_all_button || 'All Posts')
  const blogArticlesButton = computed(() => settingsStore.settings.blog_articles_button || 'News Articles')
  const blogCategoriesDropdown = computed(() => settingsStore.settings.blog_categories_dropdown || 'All Categories')
  const blogLoading = computed(() => settingsStore.settings.blog_loading || 'Loading stories...')
  const blogNoResults = computed(() => settingsStore.settings.blog_no_results || 'No stories found')
  const blogNoResultsSubtitle = computed(() => settingsStore.settings.blog_no_results_subtitle || 'Try adjusting your filters or check back later for new content.')

  const filters = reactive({
    category: '',
    search: '',
    page: 1,
    type: 'All', // All | Articles
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
      const params = {
        status: 'PUBLISHED',
        page: filters.page,
        post_type: 'BLOG'
      }

      if (filters.category) {
        params.category = filters.category
      }

      if (filters.search) {
        params.search = filters.search
      }

      const response = await blogStore.fetchPosts(params)
      const data = response.results || response
      posts.value = Array.isArray(data) ? data : []

      if (response.count) {
        totalPages.value = Math.ceil(response.count / 12)
      } else {
        totalPages.value = 1
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
