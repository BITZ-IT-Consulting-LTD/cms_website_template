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
      const data = response.data
      // Ensure faqs is always an array
      faqs.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
      return data
    } catch (err) {
      error.value = err.response?.data || 'Failed to fetch FAQs'
      console.error('Failed to fetch FAQs:', err)
      // Ensure faqs is always an array even on error
      faqs.value = []
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function fetchCategories() {
    try {
      const response = await api.faqs.categories()
      const data = response.data
      // Ensure categories is always an array
      categories.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
      return categories.value
    } catch (err) {
      console.error('Failed to fetch categories:', err)
      // Always ensure categories is an array
      categories.value = []
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
