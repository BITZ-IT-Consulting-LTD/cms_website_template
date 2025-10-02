import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/axios'

export const usePartnersStore = defineStore('partners', () => {
  // State
  const partners = ref([])
  const loading = ref(false)
  const error = ref(null)
  
  // Actions
  async function fetchPartners() {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.partners.list()
      partners.value = response.data.results || response.data
      return response.data
    } catch (err) {
      error.value = err.response?.data || 'Failed to fetch partners'
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
