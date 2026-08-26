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

    <section class="bg-warm">
      <div class="container-custom section-padding !pt-10 md:!pt-14">
        <!-- Search -->
        <div class="max-w-3xl mx-auto mb-8 md:mb-10">
          <div class="search-shell relative flex items-center gap-2 bg-neutral-white rounded-2xl lg:rounded-[1.75rem] border border-black/5 shadow-sm focus-within:ring-2 focus-within:ring-primary/25 transition-all">
            <div class="pl-5 lg:pl-6 flex items-center pointer-events-none">
              <Search class="h-5 w-5 text-primary/40" />
            </div>
            <input
              v-model="filters.search"
              @input="debouncedSearch"
              type="search"
              :placeholder="searchPlaceholder"
              class="flex-1 min-w-0 py-4 lg:py-5 pr-2 bg-transparent text-secondary font-semibold placeholder:text-black/30 focus:outline-none text-sm lg:text-base border-none"
            />
            <button
              type="button"
              class="shrink-0 mr-2 lg:mr-3 px-5 lg:px-6 py-2.5 lg:py-3 bg-primary text-neutral-white rounded-full font-bold text-xs lg:text-sm uppercase tracking-wider hover:brightness-110 transition-all"
              @click="fetchFilteredPosts"
            >
              {{ searchButtonText }}
            </button>
          </div>
        </div>

        <!-- Category filters -->
        <div v-if="showFilters" class="mb-8 md:mb-10">
          <div class="filter-tabs-wrapper hide-scrollbar">
            <button
              type="button"
              @click="clearCategoryFilter"
              :class="!filters.category ? 'chip-active' : 'chip-idle'"
              class="chip"
            >
              {{ allFilterText }}
            </button>

            <button
              v-for="category in categories"
              :key="category.id"
              type="button"
              @click="setCategoryFilter(category.slug)"
              :class="filters.category === category.slug ? 'chip-active' : 'chip-idle'"
              class="chip"
            >
              {{ category.name }}
            </button>

            <div v-if="categories.length > 5" class="relative ml-auto shrink-0">
              <select
                v-model="filters.category"
                @change="onDropdownChange"
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

        <!-- Content -->
        <AppLoader v-if="loading" :message="loadingMessage" />

        <div v-else-if="posts.length" class="space-y-12 lg:space-y-14">
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 sm:gap-6 lg:gap-8">
            <BlogCard v-for="post in posts" :key="post.id" :post="post" />
          </div>

          <!-- Pagination -->
          <div class="flex items-center justify-center gap-2 sm:gap-3 pt-2">
            <button
              type="button"
              @click="setPage('<')"
              :disabled="filters.page <= 1"
              class="page-nav"
              aria-label="Previous page"
            >
              <ChevronLeft class="w-5 h-5" />
            </button>

            <div class="flex items-center gap-1.5 sm:gap-2">
              <button
                v-for="n in pageNumbers"
                :key="n + '-pg'"
                type="button"
                @click="setPage(n)"
                :class="[
                  'page-btn',
                  filters.page === n ? 'page-btn--active' : 'page-btn--idle'
                ]"
              >
                {{ n }}
              </button>
            </div>

            <button
              type="button"
              @click="setPage('>')"
              :disabled="filters.page >= totalPages"
              class="page-nav"
              aria-label="Next page"
            >
              <ChevronRight class="w-5 h-5" />
            </button>
          </div>
        </div>

        <!-- Empty -->
        <div v-else class="empty-state text-center py-14 lg:py-20 px-6 rounded-3xl bg-neutral-white border border-dashed border-black/10 max-w-2xl mx-auto">
          <div class="w-16 h-16 lg:w-20 lg:h-20 mx-auto bg-primary/10 rounded-2xl flex items-center justify-center mb-6">
            <AlertCircle class="w-8 h-8 text-primary/70" />
          </div>
          <h3 class="text-xl lg:text-2xl font-bold text-secondary mb-3">{{ emptyTitle }}</h3>
          <p class="text-sm lg:text-base text-black/50 font-semibold mb-8 max-w-md mx-auto">{{ emptySubtitle }}</p>
          <button
            type="button"
            @click="clearAllFilters"
            class="px-8 py-3.5 bg-secondary text-neutral-white rounded-full font-bold uppercase tracking-wider text-xs shadow-lg shadow-secondary/20 hover:brightness-110 transition-all"
          >
            {{ clearFiltersText }}
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
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

const route = useRoute()

const filters = reactive({
  category: '',
  // Seeded from ?search= so a search started elsewhere (e.g. the article page's
  // search box) arrives here already applied.
  search: typeof route.query.search === 'string' ? route.query.search : '',
  page: 1
})

// Landing here again with a different ?search= should re-run the search.
watch(() => route.query.search, (term) => {
  const next = typeof term === 'string' ? term : ''
  if (next === filters.search) return
  filters.search = next
  filters.page = 1
  fetchFilteredPosts()
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

function onDropdownChange() {
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
.chip {
  @apply px-5 py-2.5 rounded-full text-[11px] font-bold uppercase tracking-wider whitespace-nowrap transition-all duration-300 flex-shrink-0 border-2;
}

.chip-active {
  @apply bg-secondary border-secondary text-neutral-white shadow-md;
}

.chip-idle {
  @apply bg-neutral-white border-transparent text-secondary/60 hover:border-primary/30 hover:text-primary;
}

.filter-tabs-wrapper {
  display: flex;
  gap: 0.625rem;
  overflow-x: auto;
  scrollbar-width: none;
  -ms-overflow-style: none;
  -webkit-overflow-scrolling: touch;
  align-items: center;
  padding-bottom: 0.25rem;
}

.filter-tabs-wrapper::-webkit-scrollbar {
  display: none;
}

.hide-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.category-dropdown {
  appearance: none;
  background: white;
  border: 2px solid rgb(var(--color-secondary) / 0.12);
  border-radius: 9999px;
  padding: 0.625rem 2.5rem 0.625rem 1.25rem;
  font-size: 0.6875rem;
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

.page-nav {
  @apply min-w-[48px] min-h-[48px] w-12 h-12 rounded-2xl flex items-center justify-center bg-neutral-white text-secondary shadow-sm border border-black/5 hover:shadow-md hover:text-primary transition-all disabled:opacity-40 disabled:pointer-events-none;
}

.page-btn {
  @apply min-w-[48px] min-h-[48px] w-12 h-12 rounded-2xl flex items-center justify-center font-bold transition-all border-none touch-manipulation;
}

.page-btn--active {
  @apply bg-primary text-neutral-white shadow-lg shadow-primary/25;
}

.page-btn--idle {
  @apply bg-neutral-white text-secondary shadow-sm border border-black/5 hover:shadow-md;
}

@media (max-width: 640px) {
  .chip {
    @apply px-4 py-2 text-[10px];
  }
}
</style>
