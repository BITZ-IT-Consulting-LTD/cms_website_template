import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/axios'

const CACHE_TTL = 10 * 60 * 1000 // 10 minutes (partners change rarely)

function isCacheFresh(timestamp) {
  if (!timestamp) return false
  return Date.now() - timestamp < CACHE_TTL
}

function paramsMatch(params1, params2) {
  return JSON.stringify(params1 || {}) === JSON.stringify(params2 || {})
}

export const usePartnersStore = defineStore('partners', () => {
  // State
  const partners = ref([])
  const loading = ref(false)
  const error = ref(null)

  // Cache metadata
  const lastFetched = ref(null)
  const cachedParams = ref(null)

  // De-duplication
  let fetchingPromise = null

  function normalizeLogoUrl(logo) {
    if (!logo) return logo

    // If it's already an absolute URL that doesn't use the internal Docker host, keep it
    if (logo.startsWith('http://') || logo.startsWith('https://')) {
      try {
        const url = new URL(logo)
        // "backend" is the internal Docker hostname and isn't reachable from the
        // browser - fall back to just the path, resolved against the current origin
        // (whatever host/port the user is actually browsing on).
        if (url.hostname === 'backend') {
          return `${window.location.origin}${url.pathname}`
        }
        return logo
      } catch {
        return logo
      }
    }

    // Relative path from backend (e.g. "/sauti/media/...") - prefix with current origin
    if (logo.startsWith('/')) {
      return `${window.location.origin}${logo}`
    }

    // Fallback: leave unchanged
    return logo
  }

  // Actions
  async function fetchPartners(params = {}, forceRefresh = false) {
    // Return cached if fresh and params match
    if (!forceRefresh &&
        isCacheFresh(lastFetched.value) &&
        paramsMatch(params, cachedParams.value) &&
        partners.value.length > 0) {
      console.log('[PartnersStore] Using cached partners')
      return partners.value
    }

    // De-duplicate
    if (fetchingPromise) {
      console.log('[PartnersStore] Deduplicating concurrent fetch')
      return fetchingPromise
    }

    loading.value = true
    error.value = null

    fetchingPromise = (async () => {
      try {
        const response = await api.partners.list(params)
        const data = response.data.results || response.data || []

        partners.value = Array.isArray(data)
          ? data.map(p => ({ ...p, logo: normalizeLogoUrl(p.logo) }))
          : []

        lastFetched.value = Date.now()
        cachedParams.value = params
        console.log('[PartnersStore] Partners cached:', partners.value.length, 'items')
        return partners.value
      } catch (err) {
        error.value = err.response?.data || 'Failed to fetch partners'
        console.error('Failed to fetch partners:', err)
        partners.value = []
        throw err
      } finally {
        loading.value = false
        fetchingPromise = null
      }
    })()

    return fetchingPromise
  }

  function clearError() {
    error.value = null
  }

  function invalidateCache() {
    lastFetched.value = null
  }

  return {
    partners,
    loading,
    error,
    lastFetched,
    cachedParams,
    fetchPartners,
    clearError,
    invalidateCache,
  }
}, {
  persist: {
    key: 'sauti-partners',
    storage: localStorage,
    paths: ['partners', 'lastFetched', 'cachedParams']
  }
})
