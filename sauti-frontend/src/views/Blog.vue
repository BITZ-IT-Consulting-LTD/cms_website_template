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
import { useBlogStore } from '@/store/blog'

const blogStore = useBlogStore()

// Now using real API data from backend
const useMock = false

const posts = ref([])
const categories = ref([])
const loading = ref(false)
const totalPages = ref(1)

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
  if (useMock) {
    categories.value = [
      { id: 1, slug: 'child-protection', name: 'Child Protection' },
      { id: 2, slug: 'gbv', name: 'GBV' },
      { id: 3, slug: 'migrants', name: 'Migrant Workers' },
    ]
    return
  }
  
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
    if (useMock) {
      const all = mockPosts()
      const byCat = filters.category ? all.filter(p => p.category?.slug === filters.category) : all
      const byType = filters.type === 'All' ? byCat : byCat.filter(p => (filters.type === 'Videos' ? p.is_video : !p.is_video))
      const bySearch = filters.search ? byType.filter(p => p.title.toLowerCase().includes(filters.search.toLowerCase())) : byType
      posts.value = bySearch
      totalPages.value = 8
      return
    }
    
    // Fetch real posts from backend
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
    console.warn('Backend not available, using mock data as fallback')
    
    // Fallback to mock data if backend is not available
    posts.value = mockPosts()
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
  if (!useMock) {
    fetchFilteredPosts()
  }
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

function mockPosts() {
  return [
    {
      id: 1,
      slug: 'empowering-youth-voices',
      title: 'Empowering Youth Voices: A New Initiative',
      excerpt: 'Learn about our new youth empowerment program.',
      featured_image: 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?q=80&w=1200&auto=format&fit=crop',
      published_at: '2024-07-15',
      author: { username: 'Dr. Aisha Nakato' },
      author_name: 'Dr. Aisha Nakato',
      views_count: 1250,
      category: { name: 'Child Protection', slug: 'child-protection' },
      is_video: false,
    },
    {
      id: 2,
      slug: 'a-day-at-the-helpline',
      title: 'A Day at the Helpline',
      excerpt: 'Go behind the scenes with our helpline operators.',
      featured_image: 'https://images.unsplash.com/photo-1544717305-2782549b5136?q=80&w=1200&auto=format&fit=crop',
      published_at: '2024-07-12',
      author: { username: 'Sauti Team' },
      author_name: 'Sauti Team',
      views_count: 890,
      category: { name: 'GBV', slug: 'gbv' },
      is_video: true,
    },
    {
      id: 3,
      slug: 'child-protection-in-digital-age',
      title: 'Child Protection in the Digital Age',
      excerpt: 'Navigating the online world safely.',
      featured_image: 'https://images.unsplash.com/photo-1503676260728-1c00da094a0b?q=80&w=1200&auto=format&fit=crop',
      published_at: '2024-07-10',
      author: { username: 'Jane Mukasa' },
      author_name: 'Jane Mukasa',
      views_count: 2340,
      category: { name: 'Child Protection', slug: 'child-protection' },
      is_video: false,
    },
    {
      id: 4,
      slug: 'success-story-victory',
      title: 'Success Story: From Vulnerability to Victory',
      excerpt: "A child's journey to safety and success.",
      featured_image: 'https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?q=80&w=1200&auto=format&fit=crop',
      published_at: '2024-07-05',
      author: { username: 'John Okello' },
      author_name: 'John Okello',
      views_count: 1580,
      category: { name: 'Migrant Workers', slug: 'migrants' },
      is_video: false,
    },
    {
      id: 5,
      slug: 'understanding-child-rights',
      title: 'Understanding Child Rights in Uganda',
      excerpt: 'A comprehensive guide to child rights and protection laws.',
      featured_image: 'https://images.unsplash.com/photo-1497486751825-1233686d5d80?q=80&w=1200&auto=format&fit=crop',
      published_at: '2024-06-28',
      author: { username: 'Sarah Nambi' },
      author_name: 'Sarah Nambi',
      views_count: 3200,
      category: { name: 'Child Protection', slug: 'child-protection' },
      is_video: false,
    },
    {
      id: 6,
      slug: 'preventing-gbv-communities',
      title: 'Preventing GBV in Communities',
      excerpt: 'Community-based approaches to preventing gender-based violence.',
      featured_image: 'https://images.unsplash.com/photo-1529390079861-591de354faf5?q=80&w=1200&auto=format&fit=crop',
      published_at: '2024-06-20',
      author: { username: 'Dr. Aisha Nakato' },
      author_name: 'Dr. Aisha Nakato',
      views_count: 1890,
      category: { name: 'GBV', slug: 'gbv' },
      is_video: false,
    },
    {
      id: 7,
      slug: 'safe-migration-guide',
      title: 'Safe Migration: What You Need to Know',
      excerpt: 'Essential information for safe and legal migration.',
      featured_image: 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?q=80&w=1200&auto=format&fit=crop',
      published_at: '2024-06-15',
      author: { username: 'Moses Wanjala' },
      author_name: 'Moses Wanjala',
      views_count: 2150,
      category: { name: 'Migrant Workers', slug: 'migrants' },
      is_video: false,
    },
    {
      id: 8,
      slug: 'hotline-impact-report',
      title: 'Annual Hotline Impact Report 2024',
      excerpt: 'See how your calls have made a difference this year.',
      featured_image: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=1200&auto=format&fit=crop',
      published_at: '2024-06-10',
      author: { username: 'Sauti Uganda' },
      author_name: 'Sauti Uganda',
      views_count: 4500,
      category: { name: 'Child Protection', slug: 'child-protection' },
      is_video: false,
    },
  ]
}
</script>
