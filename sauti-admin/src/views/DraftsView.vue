<template>
  <div class="p-6">
    <div class="flex items-center justify-between mb-6">
      <div>
        <h1 class="text-2xl font-bold text-gray-900">Drafts</h1>
        <p class="text-sm text-gray-600">Manage posts that are saved as drafts.</p>
      </div>
      <router-link
        to="/posts/create"
        class="inline-flex items-center px-4 py-2 rounded-md bg-primary-600 text-white hover:bg-primary-700"
      >
        New Post
      </router-link>
    </div>

    <div class="bg-white rounded-lg shadow-sm border border-gray-200">
      <div class="p-4 border-b border-gray-200">
        <div class="flex flex-col sm:flex-row gap-3 sm:items-center sm:justify-between">
          <div class="flex-1">
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search drafts..."
              class="w-full sm:w-80 px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
            />
          </div>
          <div class="flex gap-3">
            <select v-model="language" class="px-3 py-2 border rounded-md">
              <option value="">All languages</option>
              <option value="en">English</option>
              <option value="lg">Luganda</option>
              <option value="sw">Swahili</option>
            </select>
          </div>
        </div>
      </div>

      <div v-if="loading" class="p-6 text-center text-gray-500">Loading drafts...</div>
      <div v-else>
        <div v-if="drafts.length === 0" class="p-6 text-center text-gray-500">
          No drafts found.
        </div>
        <ul v-else class="divide-y divide-gray-200">
          <li v-for="post in drafts" :key="post.id" class="p-4 flex items-start justify-between">
            <div class="min-w-0">
              <h3 class="text-base font-semibold text-gray-900 truncate">{{ post.title }}</h3>
              <p class="text-sm text-gray-600 mt-1 line-clamp-2" v-html="post.excerpt" />
              <div class="mt-2 text-xs text-gray-500">
                <span class="uppercase">{{ post.language }}</span>
                <span class="mx-2">•</span>
                <span>Updated {{ formatDate(post.updated_at) }}</span>
              </div>
            </div>
            <div class="ml-4 flex-shrink-0 flex items-center gap-2">
              <router-link :to="`/posts/${post.slug}/edit`" class="px-3 py-1.5 text-sm rounded-md border hover:bg-gray-50">Edit</router-link>
            </div>
          </li>
        </ul>

        <div v-if="hasMore" class="p-4 border-t border-gray-200 flex justify-center">
          <button @click="loadMore" class="px-4 py-2 rounded-md border hover:bg-gray-50">Load more</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { usePostsStore } from '@/stores/posts'

const postsStore = usePostsStore()
const route = useRoute()
const router = useRouter()
const toast = useToast()

const drafts = ref([])
const loading = ref(false)
const page = ref(1)
const hasMore = ref(false)
const searchQuery = ref(route.query.search || '')
const language = ref(route.query.language || '')

const fetchDrafts = async (append = false) => {
  loading.value = true
  try {
    const params = {
      status: 'DRAFT',
      page: page.value,
    }
    if (searchQuery.value) params.search = searchQuery.value
    if (language.value) params.language = language.value

    const response = await postsStore.fetchPosts(params)
    const results = response?.results || []
    if (append) {
      drafts.value = drafts.value.concat(results)
    } else {
      drafts.value = results
    }
    hasMore.value = Boolean(response?.next)
  } catch (err) {
    console.error('Failed to fetch drafts', err)
    toast.error('Failed to load drafts')
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchDrafts()
})

watch([searchQuery, language], () => {
  page.value = 1
  router.replace({ query: {
    ...(searchQuery.value ? { search: searchQuery.value } : {}),
    ...(language.value ? { language: language.value } : {}),
  }})
  fetchDrafts()
})

const loadMore = () => {
  page.value += 1
  fetchDrafts(true)
}

const formatDate = (iso) => {
  try {
    return new Date(iso).toLocaleString()
  } catch {
    return iso
  }
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>


