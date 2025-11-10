<template>
  <div class="section-padding">
    <div class="container-custom">
      <h1 class="text-center mb-3">Resources</h1>
      <p class="text-center text-gray-600 max-w-3xl mx-auto mb-10">Downloadable guides, policies, and toolkits. Accessible 24/7 and available in multiple languages.</p>

      <!-- Filters -->
      <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-4 md:p-6 mb-8">
        <div class="flex flex-col md:flex-row gap-3 md:items-center md:justify-between">
          <div class="flex-1">
            <label class="sr-only" for="search">Search resources</label>
            <input
              id="search"
              v-model="search"
              type="text"
              placeholder="Search by title or description..."
              class="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
            />
          </div>
          <div class="flex flex-wrap gap-3">
            <label class="sr-only" for="category">Category</label>
            <select id="category" v-model="category" class="px-3 py-2 border rounded-md min-w-[12rem]">
              <option value="">All categories</option>
              <option v-for="cat in categories" :key="cat.slug || cat.id" :value="cat.slug || cat.id">{{ cat.name }}</option>
            </select>

            <label class="sr-only" for="language">Language</label>
            <select id="language" v-model="language" class="px-3 py-2 border rounded-md">
              <option value="">All languages</option>
              <option value="en">English</option>
              <option value="lg">Luganda</option>
              <option value="sw">Swahili</option>
            </select>
          </div>
        </div>
      </div>

      <Loader v-if="loading" message="Loading resources..." />

      <!-- Grid -->
      <div v-else-if="resources.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <article v-for="resource in resources" :key="resource.id" class="group bg-white rounded-xl shadow-sm border border-gray-100 p-5 hover:shadow-md transition-shadow relative" :class="{ 'ring-2 ring-[#8B4000] ring-opacity-20': resource.is_featured }">
          <!-- Featured Badge -->
          <div v-if="resource.is_featured" class="absolute -top-2 -right-2 bg-[#8B4000] text-white text-xs font-semibold px-2 py-1 rounded-full">
            Featured
          </div>
          <div class="flex items-start gap-4">
            <div class="h-12 w-12 rounded-lg bg-teal-100 text-teal-700 flex items-center justify-center">
              <svg v-if="isAudio(resource)" class="w-6 h-6" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path d="M9 19V6l12-2v13"/>
                <circle cx="6" cy="18" r="3"/>
                <circle cx="18" cy="18" r="3"/>
              </svg>
              <svg v-else class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clip-rule="evenodd" />
              </svg>
            </div>
            <div class="min-w-0 flex-1">
              <h3 class="text-base font-semibold text-gray-900 group-hover:text-primary-600 truncate">{{ resource.title }}</h3>
              <p class="text-sm text-gray-600 mt-1 line-clamp-2">{{ resource.description }}</p>
              <div class="mt-2 text-xs text-gray-500 flex flex-wrap gap-3">
                <span v-if="resource.category_name" class="inline-flex items-center gap-1"><span class="h-1.5 w-1.5 rounded-full bg-gray-400"></span>{{ resource.category_name }}</span>
                <span v-if="resource.language" class="uppercase">{{ getLanguageName(resource.language) }}</span>
                <span v-if="resource.file_type">{{ resource.file_type }}</span>
                <span v-else class="text-gray-400">Document</span>
                <span v-if="resource.published_at">{{ formatDate(resource.published_at) }}</span>
              </div>
              <div class="mt-4 flex items-center gap-3">
                <template v-if="isAudio(resource) && resource.file">
                  <audio :src="resource.file" controls class="w-full"></audio>
                </template>
                <a v-if="resource.file" :href="resource.file" target="_blank" rel="noopener" class="pill pill-primary">Download</a>
                <span v-else class="pill pill-light">Coming Soon</span>
                <a v-if="resource.thumbnail" :href="resource.thumbnail" target="_blank" rel="noopener" class="pill pill-light">Preview</a>
                <span class="text-xs text-gray-500">{{ resource.download_count }} downloads</span>
              </div>
            </div>
          </div>
        </article>
      </div>

      <!-- Empty -->
      <div v-else class="text-center py-16">
        <p class="text-gray-600">No resources found. Try a different search or category.</p>
      </div>

      <!-- Pagination -->
      <div v-if="pagination.next || pagination.previous" class="mt-8 flex justify-center gap-3">
        <button :disabled="!pagination.previous || loading" @click="prevPage" class="px-4 py-2 rounded-md border hover:bg-gray-50 disabled:opacity-50">Previous</button>
        <button :disabled="!pagination.next || loading" @click="nextPage" class="px-4 py-2 rounded-md border hover:bg-gray-50 disabled:opacity-50">Next</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { useResourcesStore } from '@/store/resources'
import Loader from '@/components/common/Loader.vue'

const resourcesStore = useResourcesStore()
const resources = ref([])
const loading = ref(true)
const search = ref('')
const category = ref('')
const language = ref('')
const categories = ref([])
const pagination = ref({ count: 0, next: null, previous: null })

onMounted(async () => {
  try {
    const [cats] = await Promise.all([
      resourcesStore.fetchCategories(),
      fetchList(),
    ])
    // Ensure categories is always an array
    categories.value = Array.isArray(cats) ? cats : []
  } catch (error) {
    console.error('Error initializing resources:', error)
    categories.value = []
  } finally {
    loading.value = false
  }
})

watch([search, category, language], () => {
  // Debounce-like behavior could be added; for now refetch immediately
  fetchList()
})

async function fetchList(pageUrl = null) {
  loading.value = true
  try {
    const params = {
      status: 'PUBLISHED' // Only show published resources
    }
    if (search.value) params.search = search.value
    if (category.value) params.category = category.value
    if (language.value) params.language = language.value
    const data = await resourcesStore.fetchResources(params)
    // Ensure resources is always an array
    resources.value = Array.isArray(resourcesStore.resources) ? resourcesStore.resources : []
    pagination.value = resourcesStore.pagination || { count: 0, next: null, previous: null }
    console.log('Fetched resources:', resources.value)
    console.log('Resources count:', resources.value.length)
    return data
  } catch (error) {
    console.error('Error fetching resources:', error)
    resources.value = []
  } finally {
    loading.value = false
  }
}

function nextPage() {
  if (!pagination.value.next) return
  // Fallback simple increment approach: request next via page param if server supports page
  const url = new URL(pagination.value.next)
  const page = url.searchParams.get('page')
  fetchList({ page })
}

function prevPage() {
  if (!pagination.value.previous) return
  const url = new URL(pagination.value.previous)
  const page = url.searchParams.get('page')
  fetchList({ page })
}

function formatDate(iso) {
  try { return new Date(iso).toLocaleDateString() } catch { return iso }
}

function getLanguageName(code) {
  const languages = {
    'en': 'English',
    'lg': 'Luganda', 
    'sw': 'Swahili'
  }
  return languages[code] || code.toUpperCase()
}

function isAudio(resource) {
  const type = (resource.file_type || '').toLowerCase()
  const url = (resource.file || '').toLowerCase()
  const exts = ['mp3', 'm4a', 'wav', 'ogg']
  return exts.some(ext => type.includes(ext) || url.endsWith(`.${ext}`))
}
</script>
