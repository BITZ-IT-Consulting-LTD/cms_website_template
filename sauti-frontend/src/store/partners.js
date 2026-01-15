import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/axios'

export const usePartnersStore = defineStore('partners', () => {
  // State
  const partners = ref([])
  const loading = ref(false)
  const error = ref(null)

  function normalizeLogoUrl(logo) {
    if (!logo) return logo

    // If it's already an absolute URL that doesn't use the internal Docker host, keep it
    if (logo.startsWith('http://') || logo.startsWith('https://')) {
      try {
        const url = new URL(logo)
        // If host is "backend" (internal), rewrite to the public origin
        if (url.hostname === 'backend') {
          url.hostname = window.location.hostname || 'localhost'
          // Dev nginx proxy exposes media on port 8080
          url.port = window.location.port === '5173' ? '8080' : url.port
        }
        return url.toString()
      } catch {
        return logo
      }
    }

    // Relative path from backend (e.g. "/sauti/media/...") – prefix with current origin
    if (logo.startsWith('/')) {
      const origin = window.location.origin || 'http://localhost:8080'
      return `${origin}${logo}`
    }

    // Fallback: leave unchanged
    return logo
  }

  // Actions
  async function fetchPartners() {
    loading.value = true
    error.value = null

    try {
      const response = await api.partners.list()
      const data = response.data.results || response.data || []

      partners.value = Array.isArray(data)
        ? data.map(p => ({ ...p, logo: normalizeLogoUrl(p.logo) }))
        : []

      return partners.value
    } catch (err) {
      error.value = err.response?.data || 'Failed to fetch partners'
      console.error('Failed to fetch partners:', err)
      partners.value = []
      throw err
    } finally {
      loading.value = false
    }
  }

  function clearError() {
    error.value = null
  }

  return {
    partners,
    loading,
    error,
    fetchPartners,
    clearError,
  }
})
