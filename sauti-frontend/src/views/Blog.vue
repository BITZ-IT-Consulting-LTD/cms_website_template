<template>
  <div class="section-padding">
    <div class="container-custom">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="mb-2 text-4xl md:text-5xl font-extrabold text-gray-900">Sauti Blog</h1>
        <p class="text-gray-600 max-w-3xl mx-auto">Insights, stories, and news from the front lines of child protection in Uganda.</p>
      </div>

      <!-- Filters -->
      <div class="mb-8">
        <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-4 flex items-center gap-3 max-w-3xl mx-auto">
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35M11 19a8 8 0 100-16 8 8 0 000 16z"/></svg>
          <input v-model="filters.search" @input="debouncedSearch" type="search" placeholder="Search articles..." class="flex-1 focus:outline-none" />
        </div>
        <div class="flex flex-wrap justify-center gap-3 mt-4">
          <button class="pill pill-primary" @click="setType('All')">All</button>
          <button class="px-3 py-1 rounded-full bg-gray-100" @click="setType('Articles')">Articles</button>
          <select v-model="filters.category" @change="fetchFilteredPosts" class="form-select max-w-xs">
            <option value="">Categories</option>
            <option v-for="cat in categories" :key="cat.id" :value="cat.slug">{{ cat.name }}</option>
          </select>
        </div>
      </div>

      <!-- Loading -->
      <Loader v-if="loading" message="Loading articles..." />

      <!-- Posts Grid -->
      <div v-else-if="posts.length" class="space-y-10">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <BlogCard v-for="post in posts" :key="post.id" :post="post" />
        </div>
        <!-- Pagination (mock to match design) -->
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
        <h3 class="text-xl font-semibold text-gray-900 mb-2">No articles found</h3>
        <p class="text-gray-600">Try adjusting your filters or check back later for new content.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed } from 'vue'
import BlogCard from '@/components/blog/BlogCard.vue'
import Loader from '@/components/common/Loader.vue'

// Toggle to false to use real API via store later
const useMock = true

const posts = ref([])
const categories = ref([])
const loading = ref(false)
const totalPages = ref(8)

const filters = reactive({
  category: '',
  search: '',
  page: 1,
  type: 'All', // All | Articles | Videos
})

let debounceTimer = null

onMounted(() => {
  fetchCategories()
  // Prime with mock content immediately
  posts.value = mockPosts()
})

async function fetchCategories() {
  if (useMock) {
    categories.value = [
      { id: 1, slug: 'child-protection', name: 'Child Protection' },
      { id: 2, slug: 'gbv', name: 'GBV' },
      { id: 3, slug: 'migrants', name: 'Migrant Workers' },
    ]
    return
  }
}

async function fetchFilteredPosts() {
  loading.value = true
  try {
    if (useMock) {
      const all = mockPosts()
      const byCat = filters.category ? all.filter(p => p.category?.slug === filters.category) : all
      const byType = filters.type === 'All' ? byCat : byCat.filter(p => (filters.type === 'Videos' ? p.is_video : !p.is_video))
      const bySearch = filters.search ? byType.filter(p => p.title.toLowerCase().includes(filters.search.toLowerCase())) : byType
      posts.value = bySearch
      totalPages.value = 8
      return
    }
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
  const pages = [1, 2, 3, '…', totalPages.value, '>']
  return pages
})

function setType(t) {
  filters.type = t
  fetchFilteredPosts()
}

function setPage(p) {
  if (p === '…') return
  if (p === '<') filters.page = Math.max(1, filters.page - 1)
  else if (p === '>') filters.page = Math.min(totalPages.value, filters.page + 1)
  else filters.page = p
  fetchFilteredPosts()
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function mockPosts() {
  return [
    {
      id: 1,
      slug: 'empowering-youth-voices',
      title: 'Empowering Youth Voices: A New Initiative',
      excerpt: 'Learn about our new youth empowerment program.',
      featured_image: 'https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?q=80&w=1200&auto=format&fit=crop',
      published_at: '2024-07-15',
      author: { username: 'Dr. Aisha Nakato' },
      category: { name: 'Child Protection', slug: 'child-protection' },
      is_video: false,
    },
    {
      id: 2,
      slug: 'a-day-at-the-helpline',
      title: 'A Day at the Helpline',
      excerpt: 'Go behind the scenes with our helpline operators.',
      featured_image: 'https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?q=80&w=1200&auto=format&fit=crop',
      published_at: '2024-07-12',
      author: { username: 'Sauti Team' },
      category: { name: 'GBV', slug: 'gbv' },
      is_video: true,
    },
    {
      id: 3,
      slug: 'child-protection-in-digital-age',
      title: 'Child Protection in the Digital Age',
      excerpt: 'Navigating the online world safely.',
      featured_image: 'https://images.unsplash.com/photo-1600880292203-757bb62b4baf?q=80&w=1200&auto=format&fit=crop',
      published_at: '2024-07-10',
      author: { username: 'Jane' },
      category: { name: 'Child Protection', slug: 'child-protection' },
      is_video: false,
    },
    {
      id: 4,
      slug: 'success-story-victory',
      title: 'Success Story: From Vulnerability to Victory',
      excerpt: "A child's journey to safety and success.",
      featured_image: 'https://images.unsplash.com/flagged/photo-1556746834-1cb5b3a8d7e4?q=80&w=1200&auto=format&fit=crop',
      published_at: '2024-07-05',
      author: { username: 'John' },
      category: { name: 'Migrant Workers', slug: 'migrants' },
      is_video: false,
    },
  ]
}
</script>
