// Resources store - updated with caching and persistence
import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/axios'

const RESOURCES_TTL = 5 * 60 * 1000 // 5 minutes
const CATEGORIES_TTL = 10 * 60 * 1000 // 10 minutes

function isCacheFresh(timestamp, ttl) {
  if (!timestamp) return false
  return Date.now() - timestamp < ttl
}

export const useResourcesStore = defineStore('resources', () => {
  // State
  const resources = ref([])
  const currentResource = ref(null)
  const categories = ref([])
  const loading = ref(false)
  const error = ref(null)
  const pagination = ref({
    count: 0,
    next: null,
    previous: null,
  })

  // Cache metadata
  const lastFetchedResources = ref(null)
  const lastFetchedCategories = ref(null)
  const lastResourceParams = ref(null)

  // De-duplication promises
  let fetchingResourcesPromise = null
  let fetchingCategoriesPromise = null

  // Actions
  async function fetchResources(params = {}, forceRefresh = false) {
    const paramsKey = JSON.stringify(params)

    // Return cached data if fresh and same params
    if (!forceRefresh &&
        isCacheFresh(lastFetchedResources.value, RESOURCES_TTL) &&
        lastResourceParams.value === paramsKey &&
        resources.value.length > 0) {
      console.log('[ResourcesStore] Using cached resources')
      return { results: resources.value, ...pagination.value }
    }

    // De-duplicate concurrent requests with same params
    if (fetchingResourcesPromise && lastResourceParams.value === paramsKey) {
      console.log('[ResourcesStore] Deduplicating concurrent fetch')
      return fetchingResourcesPromise
    }

    loading.value = true
    error.value = null
    lastResourceParams.value = paramsKey

    fetchingResourcesPromise = (async () => {
      try {
        const response = await api.resources.list(params)
        const data = response.data

        // Ensure resources is always an array
        resources.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])

        if (data.count !== undefined) {
          pagination.value = {
            count: data.count,
            next: data.next,
            previous: data.previous,
          }
        }

        lastFetchedResources.value = Date.now()
        console.log('[ResourcesStore] Resources cached:', resources.value.length, 'items')
        return data
      } catch (err) {
        error.value = err.response?.data || 'Failed to fetch resources'
        console.error('Failed to fetch resources:', err)
        resources.value = []
        throw err
      } finally {
        loading.value = false
        fetchingResourcesPromise = null
      }
    })()

    return fetchingResourcesPromise
  }

  async function fetchResource(slug) {
    loading.value = true
    error.value = null

    try {
      const response = await api.resources.get(slug)
      currentResource.value = response.data
      return response.data
    } catch (err) {
      error.value = err.response?.data || 'Failed to fetch resource'
      throw err
    } finally {
      loading.value = false
    }
  }

  // Fetch resource categories from API with caching
  async function fetchCategories(forceRefresh = false) {
    // Return cached if fresh
    if (!forceRefresh && isCacheFresh(lastFetchedCategories.value, CATEGORIES_TTL) && categories.value.length > 0) {
      console.log('[ResourcesStore] Using cached categories')
      return categories.value
    }

    // De-duplicate
    if (fetchingCategoriesPromise) {
      return fetchingCategoriesPromise
    }

    fetchingCategoriesPromise = (async () => {
      try {
        const response = await api.resources.categories()
        const data = response.data
        categories.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
        lastFetchedCategories.value = Date.now()
        console.log('[ResourcesStore] Categories cached:', categories.value.length)
        return categories.value
      } catch (err) {
        console.error('Failed to fetch categories:', err)
        categories.value = []
        return []
      } finally {
        fetchingCategoriesPromise = null
      }
    })()

    return fetchingCategoriesPromise
  }

  function clearError() {
    error.value = null
  }

  function invalidateCache() {
    lastFetchedResources.value = null
    lastFetchedCategories.value = null
    lastResourceParams.value = null
  }

  return {
    resources,
    currentResource,
    categories,
    loading,
    error,
    pagination,
    lastFetchedResources,
    lastFetchedCategories,
    fetchResources,
    fetchResource,
    fetchCategories,
    clearError,
    invalidateCache,
  }
}, {
  persist: {
    key: 'sauti-resources',
    storage: localStorage,
    paths: ['resources', 'categories', 'pagination', 'lastFetchedResources', 'lastFetchedCategories', 'lastResourceParams']
  }
})
