import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/axios'

export const useFaqsStore = defineStore('faqs', () => {
  // State
  const faqs = ref([])
  const categories = ref([])
  const loading = ref(false)
  const error = ref(null)
  
  // Actions
  async function fetchFaqs(params = {}) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.faqs.list(params)
      faqs.value = response.data.results || response.data
      return response.data
    } catch (err) {
      error.value = err.response?.data || 'Failed to fetch FAQs'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function fetchCategories() {
    try {
      const response = await api.faqs.categories()
      categories.value = response.data
      return response.data
    } catch (err) {
      console.error('Failed to fetch categories:', err)
      return []
    }
  }
  
  function clearError() {
    error.value = null
  }
  
  return {
    faqs,
    categories,
    loading,
    error,
    fetchFaqs,
    fetchCategories,
    clearError,
  }
})
