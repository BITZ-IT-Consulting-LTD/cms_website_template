<template>
  <div class="min-h-screen bg-white">
    <!-- Hero Banner -->
    <header class="hero-banner" style="padding-top: clamp(70px, 15vw, 90px);">
      <div class="hero-overlay"></div>
      <div class="container-custom hero-content-wrapper">
        <div class="hero-text">
          <h1 class="hero-title">
            {{ titlePrefix }} <span class="text-accent-yellow">{{ titleHighlight }}</span>
          </h1>
          <p class="hero-subtitle">{{ subtitle }}</p>
        </div>
      </div>
    </header>

    <!-- Search Bar -->
    <div class="bg-white border-b border-gray-100">
      <div class="container-custom py-4">
        <div class="search-box">
          <Search class="search-icon-inline" />
          <input
            v-model="filters.search"
            @input="debouncedSearch"
            type="search"
            :placeholder="searchPlaceholder"
            class="search-input-inline"
          />
          <button class="search-btn-inline" @click="fetchFilteredPosts">
            {{ searchButtonText }}
          </button>
        </div>
      </div>
    </div>

    <!-- Filter Section -->
    <div v-if="showFilters" class="sticky top-[70px] z-30 bg-white/95 backdrop-blur-md border-b border-gray-100 shadow-sm">
      <div class="container-custom">
        <div class="filter-tabs-wrapper">
          <!-- All Button -->
          <button
            @click="clearCategoryFilter"
            :class="[
              'filter-chip',
              !filters.category ? 'filter-chip-active' : 'filter-chip-inactive'
            ]"
          >
            {{ allFilterText }}
          </button>

          <!-- Category Chips -->
          <button
            v-for="category in categories"
            :key="category.id"
            @click="setCategoryFilter(category.slug)"
            :class="[
              'filter-chip',
              filters.category === category.slug ? 'filter-chip-active' : 'filter-chip-inactive'
            ]"
          >
            {{ category.name }}
          </button>

          <!-- Category Dropdown (for many categories) -->
          <div v-if="categories.length > 5" class="relative ml-auto">
            <select
              v-model="filters.category"
              @change="fetchFilteredPosts"
              class="category-dropdown"
            >
              <option value="">{{ allCategoriesText }}</option>
              <option v-for="category in categories" :key="category.id" :value="category.slug">
                {{ category.name }}
              </option>
            </select>
            <ChevronDown class="dropdown-icon" />
          </div>
        </div>
      </div>
    </div>

    <div class="container-custom section-padding !pt-8 sm:!pt-12">
      <!-- Content Area -->
      <AppLoader v-if="loading" :message="loadingMessage" />

      <div v-else-if="posts.length" class="space-y-16">
        <div class="grid grid-cols-2 xs:grid-cols-3 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-2 sm:gap-3">
          <BlogCard v-for="post in posts" :key="post.id" :post="post" />
        </div>

        <!-- Pagination -->
        <div class="flex items-center justify-center gap-2 sm:gap-4">
          <button
            @click="setPage('<')"
            :disabled="filters.page <= 1"
            class="btn btn-outline border-none shadow-sm hover:shadow-md !p-3 !min-h-[48px] !min-w-[48px] disabled:opacity-50"
          >
            <ChevronLeft class="w-5 h-5" />
          </button>

          <div class="flex items-center gap-1 sm:gap-2">
            <button
              v-for="n in pageNumbers"
              :key="n + '-pg'"
              @click="setPage(n)"
              :class="[
                'min-w-[48px] min-h-[48px] w-12 h-12 rounded-2xl flex items-center justify-center font-bold transition-all border-none touch-manipulation',
                filters.page === n
                  ? 'bg-primary text-neutral-white shadow-xl'
                  : 'bg-neutral-white text-secondary shadow-sm hover:shadow-md'
              ]"
            >
              {{ n }}
            </button>
          </div>

          <button
            @click="setPage('>')"
            :disabled="filters.page >= totalPages"
            class="btn btn-outline border-none shadow-sm hover:shadow-md !p-3 !min-h-[48px] !min-w-[48px] disabled:opacity-50"
          >
            <ChevronRight class="w-5 h-5" />
          </button>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="text-center py-24 max-w-4xl mx-auto">
        <div class="w-24 h-24 bg-neutral-offwhite/10 rounded-3xl flex items-center justify-center mx-auto mb-8 shadow-sm">
          <AlertCircle class="w-12 h-12 text-primary" />
        </div>
        <h3 class="text-3xl font-bold text-secondary mb-4">{{ emptyTitle }}</h3>
        <p class="text-xl text-black/50 font-bold max-w-2xl mx-auto">{{ emptySubtitle }}</p>
        <button @click="clearAllFilters" class="btn btn-outline mt-10">
          {{ clearFiltersText }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed, watch } from 'vue'
import BlogCard from '@/components/blog/BlogCard.vue'
import AppLoader from '@/components/common/AppLoader.vue'
import { useBlogStore } from '@/store/blog'
import {
  Search,
  ChevronDown,
  ChevronLeft,
  ChevronRight,
  AlertCircle
} from 'lucide-vue-next'

const props = defineProps({
  postType: {
    type: String,
    required: true,
    validator: (value) => ['BLOG', 'NEWS'].includes(value)
  },
  titlePrefix: {
    type: String,
    default: 'Latest'
  },
  titleHighlight: {
    type: String,
    default: 'Posts'
  },
  subtitle: {
    type: String,
    default: 'Stay informed with the latest stories and updates.'
  },
  searchPlaceholder: {
    type: String,
    default: 'Search articles...'
  },
  showFilters: {
    type: Boolean,
    default: true
  },
  loadingMessage: {
    type: String,
    default: 'Loading posts...'
  },
  emptyTitle: {
    type: String,
    default: 'No posts found'
  },
  emptySubtitle: {
    type: String,
    default: 'Try adjusting your filters or check back later for new content.'
  },
  searchButtonText: {
    type: String,
    default: 'Search'
  },
  allFilterText: {
    type: String,
    default: 'ALL'
  },
  allCategoriesText: {
    type: String,
    default: 'All Categories'
  },
  clearFiltersText: {
    type: String,
    default: 'Clear all filters'
  }
})

const blogStore = useBlogStore()

const posts = ref([])
const categories = ref([])
const loading = ref(false)
const totalPages = ref(1)

const filters = reactive({
  category: '',
  search: '',
  page: 1
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
    const params = {
      status: 'PUBLISHED',
      page: filters.page,
      post_type: props.postType
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

function setCategoryFilter(categorySlug) {
  filters.category = categorySlug
  filters.page = 1
  fetchFilteredPosts()
}

function clearCategoryFilter() {
  filters.category = ''
  filters.page = 1
  fetchFilteredPosts()
}

function clearAllFilters() {
  filters.search = ''
  filters.category = ''
  filters.page = 1
  fetchFilteredPosts()
}

const pageNumbers = computed(() => {
  if (totalPages.value <= 5) {
    return Array.from({ length: totalPages.value }, (_, i) => i + 1)
  }
  return [1, 2, 3, '...', totalPages.value]
})

function setPage(p) {
  if (p === '...') return
  if (p === '<') filters.page = Math.max(1, filters.page - 1)
  else if (p === '>') filters.page = Math.min(totalPages.value, filters.page + 1)
  else filters.page = p
  fetchFilteredPosts()
  window.scrollTo({ top: 0, behavior: 'smooth' })
}
</script>

<style scoped>
/* Hero Banner */
.hero-banner {
  position: relative;
  background: linear-gradient(135deg, rgb(var(--color-secondary)) 0%, rgb(var(--color-primary-dark)) 100%);
  min-height: clamp(200px, 25vh, 300px);
  display: flex;
  align-items: center;
  overflow: hidden;
  margin-top: 0;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800"><defs><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1"/></pattern></defs><rect width="1200" height="800" fill="url(%23grid)"/></svg>');
  opacity: 0.5;
}

.hero-content-wrapper {
  position: relative;
  z-index: 2;
  padding: clamp(1.25rem, 3vh, 2.5rem) 0;
}

.hero-text {
  text-align: center;
  margin-bottom: clamp(0.75rem, 2vw, 1rem);
}

.hero-title {
  font-size: clamp(1rem, 2vw, 1.75rem);
  font-weight: 900;
  color: white;
  margin-bottom: 0.375rem;
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.text-accent-yellow {
  color: rgb(var(--color-accent-yellow));
}

.hero-subtitle {
  font-size: clamp(0.75rem, 0.9vw, 0.875rem);
  color: rgba(255, 255, 255, 0.85);
  max-width: 600px;
  margin: 0 auto;
  font-weight: 400;
  line-height: 1.4;
  padding: 0 1rem;
}

/* Search Box */
.search-box {
  max-width: 600px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  background: rgb(var(--color-neutral-offwhite));
  border-radius: 9999px;
  padding: 0.5rem 0.75rem;
  gap: 0.5rem;
}

.search-icon-inline {
  width: 1.125rem;
  height: 1.125rem;
  color: rgb(var(--color-primary));
  flex-shrink: 0;
}

.search-input-inline {
  flex: 1;
  border: none;
  outline: none;
  font-size: 0.875rem;
  font-weight: 500;
  color: rgb(var(--color-secondary));
  background: transparent;
  padding: 0.25rem 0.5rem;
  min-width: 0;
}

.search-input-inline::placeholder {
  color: rgba(0, 0, 0, 0.4);
}

.search-btn-inline {
  background: rgb(var(--color-primary));
  color: white;
  font-weight: 600;
  border: none;
  border-radius: 9999px;
  padding: 0.5rem 1.25rem;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
  flex-shrink: 0;
}

.search-btn-inline:hover {
  background: rgb(var(--color-primary-dark));
}

/* Filter Tabs */
.filter-tabs-wrapper {
  display: flex;
  gap: 0.75rem;
  padding: 1rem 0;
  overflow-x: auto;
  scrollbar-width: none;
  -ms-overflow-style: none;
  -webkit-overflow-scrolling: touch;
  align-items: center;
}

.filter-tabs-wrapper::-webkit-scrollbar {
  display: none;
}

.filter-chip {
  padding: 0.75rem 1.5rem;
  border-radius: 2rem;
  font-weight: 700;
  font-size: 0.75rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  border: 2px solid transparent;
  transition: all 0.3s ease;
  cursor: pointer;
  white-space: nowrap;
  min-height: 44px;
  touch-action: manipulation;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.filter-chip-active {
  background: rgb(var(--color-primary));
  color: white;
  box-shadow: 0 4px 12px rgba(0, 135, 207, 0.3);
}

.filter-chip-inactive {
  background: white;
  color: rgb(var(--color-secondary));
  border-color: rgb(var(--color-secondary) / 0.2);
}

.filter-chip-inactive:hover {
  border-color: rgb(var(--color-primary));
  background: rgb(var(--color-primary) / 0.05);
}

/* Category Dropdown */
.category-dropdown {
  appearance: none;
  background: white;
  border: 2px solid rgb(var(--color-secondary) / 0.2);
  border-radius: 2rem;
  padding: 0.75rem 2.5rem 0.75rem 1.25rem;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: rgb(var(--color-secondary));
  cursor: pointer;
  min-height: 44px;
  transition: all 0.3s ease;
}

.category-dropdown:hover,
.category-dropdown:focus {
  border-color: rgb(var(--color-primary));
  outline: none;
}

.dropdown-icon {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  width: 1rem;
  height: 1rem;
  color: rgb(var(--color-secondary));
  pointer-events: none;
}

@media (max-width: 640px) {
  .search-btn-inline {
    padding: 0.5rem 1rem;
    font-size: 0.8125rem;
  }

  .filter-tabs-wrapper {
    gap: 0.5rem;
    padding: 0.75rem 0;
  }

  .filter-chip {
    padding: 0.625rem 1rem;
    font-size: 0.6875rem;
  }
}
</style>
