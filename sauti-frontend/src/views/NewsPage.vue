<template>
  <div class="bg-neutral-white min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <h1 class="page-header-title">
          Official <span class="text-primary">News</span>
        </h1>
        <p class="page-header-subtitle">
          Latest official updates, press releases and announcements from the Sauti 116 Helpline.
        </p>
      </div>
    </header>

    <div class="container-custom section-padding section-rhythm">
      <!-- 2. Filters Wrapper -->
      <section aria-labelledby="filters-heading">
        <div class="bg-neutral-offwhite rounded-[3rem] p-8 md:p-12 shadow-none max-w-5xl mx-auto">
          <h2 id="filters-heading" class="campaign-header text-sm text-secondary mb-10 opacity-50">Filter News
            Archives</h2>

          <div class="flex flex-col md:flex-row gap-8 items-end">
            <div class="flex-1 w-full">
              <label class="form-label">Search Keywords</label>
              <div class="relative group">
                <input v-model="filters.search" @input="debouncedSearch"
                  class="form-input !pl-14 !border-none !shadow-sm focus:!shadow-md !bg-neutral-white"
                  placeholder="e.g. Press Release, Event..." />
                <MagnifyingGlassIcon
                  class="w-6 h-6 text-primary absolute left-5 top-1/2 -translate-y-1/2 group-focus-within:text-secondary transition-colors" />
              </div>
            </div>

            <div class="w-full md:w-64">
              <label class="form-label">Category</label>
              <div class="relative">
                <select v-model="filters.category" @change="fetchFilteredPosts"
                  class="w-full appearance-none bg-neutral-white shadow-sm focus:shadow-md border-none focus:ring-0 py-4 px-6 rounded-2xl outline-none transition-all font-bold text-secondary uppercase tracking-widest text-xs cursor-pointer">
                  <option value="">All Categories</option>
                  <option v-for="cat in categories" :key="cat.id" :value="cat.slug">{{ cat.name }}</option>
                </select>
                <ChevronDownIcon
                  class="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-primary pointer-events-none" />
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 3. Content Area -->
      <section aria-label="News Feed">
        <AppLoader v-if="loading" message="Locating official updates..." />

        <div v-else-if="posts.length" class="space-y-24">
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-10">
            <BlogCard v-for="post in posts" :key="post.id" :post="post" />
          </div>

          <!-- Pagination -->
          <div
            class="flex items-center justify-center gap-4 bg-neutral-offwhite/30 p-4 rounded-full border-2 border-neutral-offwhite w-fit mx-auto">
            <button @click="setPage('<')"
              class="w-12 h-12 rounded-full flex items-center justify-center bg-neutral-white border-2 border-neutral-offwhite text-secondary hover:bg-primary hover:text-neutral-white transition-all shadow-sm">
              <ChevronLeftIcon class="w-6 h-6" />
            </button>
            <div class="flex gap-3">
              <button v-for="n in pageNumbers" :key="n + '-pg'" @click="setPage(n)" :class="[
                'w-12 h-12 rounded-full flex items-center justify-center text-sm font-bold transition-all duration-300',
                filters.page === n ? 'bg-primary text-neutral-white shadow-xl scale-110' : 'bg-neutral-white border-2 border-neutral-offwhite text-muted hover:text-primary'
              ]">
                {{ n }}
              </button>
            </div>
            <button @click="setPage('>')"
              class="w-12 h-12 rounded-full flex items-center justify-center bg-neutral-white border-2 border-neutral-offwhite text-secondary hover:bg-primary hover:text-neutral-white transition-all shadow-sm">
              <ChevronRightIcon class="w-6 h-6" />
            </button>
          </div>
        </div>

        <!-- Empty State -->
        <div v-else
          class="text-center py-24 bg-neutral-offwhite/10 rounded-[4rem] border-2 border-dashed border-neutral-offwhite">
          <div
            class="w-24 h-24 bg-neutral-white border-2 border-primary rounded-[2rem] flex items-center justify-center mx-auto mb-8 text-primary shadow-sm">
            <DocumentTextIcon class="w-12 h-12 opacity-30" />
          </div>
          <h3 class="campaign-header text-3xl text-secondary mb-4">No archives found</h3>
          <p class="text-xl font-bold text-black/40 max-w-md mx-auto">Adjust your filters or search keywords
            to find specific official news items.</p>
        </div>
      </section>
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
    DocumentTextIcon
  } from '@heroicons/vue/24/outline'

  defineOptions({
    name: 'NewsPage'
  })

  const blogStore = useBlogStore()
  const settingsStore = useSettingsStore()

  const posts = ref([])
  const categories = ref([])
  const loading = ref(false)
  const totalPages = ref(1)

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
    }
  }

  async function fetchFilteredPosts() {
    loading.value = true
    try {
      const params = {
        status: 'PUBLISHED',
        page: filters.page,
        post_type: 'NEWS'
      }
      if (filters.category) params.category = filters.category
      if (filters.search) params.search = filters.search

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
