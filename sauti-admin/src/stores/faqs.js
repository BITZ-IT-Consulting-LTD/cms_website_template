import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/api'

export const useFaqsStore = defineStore('faqs', () => {
  // State
  const faqs = ref([])
  const currentFaq = ref(null)
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
      return faqs.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch FAQs'
      console.error('Failed to fetch FAQs:', err)
      // Ensure faqs is always an array even on error
      faqs.value = []
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function fetchFaq(id) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.faqs.get(id)
      currentFaq.value = response.data
      return currentFaq.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch FAQ'
      console.error('Failed to fetch FAQ:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function createFaq(faqData) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.faqs.create(faqData)
      const newFaq = response.data
      faqs.value.unshift(newFaq)
      return newFaq
    } catch (err) {
      error.value = err.message || 'Failed to create FAQ'
      console.error('Failed to create FAQ:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function updateFaq(id, faqData) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.faqs.update(id, faqData)
      const updatedFaq = response.data
      
      // Update in list
      const index = faqs.value.findIndex(f => f.id === id)
      if (index !== -1) {
        faqs.value[index] = updatedFaq
      }
      currentFaq.value = updatedFaq
      return updatedFaq
    } catch (err) {
      error.value = err.message || 'Failed to update FAQ'
      console.error('Failed to update FAQ:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function deleteFaq(id) {
    loading.value = true
    error.value = null
    
    try {
      await api.faqs.delete(id)
      faqs.value = faqs.value.filter(f => f.id !== id)
      if (currentFaq.value?.id === id) {
        currentFaq.value = null
      }
    } catch (err) {
      error.value = err.message || 'Failed to delete FAQ'
      console.error('Failed to delete FAQ:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function fetchCategories() {
    try {
      const response = await api.faqs.categories()
      // Ensure categories is always an array
      const data = response.data
      categories.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
      return categories.value
    } catch (err) {
      console.error('Failed to fetch FAQ categories:', err)
      // Always ensure categories is an array
      categories.value = []
      return categories.value
    }
  }
  
  return {
    // State
    faqs,
    currentFaq,
    categories,
    loading,
    error,
    
    // Actions
    fetchFaqs,
    fetchFaq,
    createFaq,
    updateFaq,
    deleteFaq,
    fetchCategories,
  }
})