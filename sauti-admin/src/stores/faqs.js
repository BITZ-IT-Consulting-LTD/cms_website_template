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
  const pagination = ref({
    count: 0,
    next: null,
    previous: null,
  })
  
  // Actions
  async function fetchFaqs(params = {}) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.faqs.list(params)
      faqs.value = response.data.results || response.data
      
      // Handle pagination
      if (response.data.count !== undefined) {
        pagination.value = {
          count: response.data.count,
          next: response.data.next,
          previous: response.data.previous,
        }
      }
      
      return faqs.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch FAQs'
      console.error('Failed to fetch FAQs:', err)
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
      const response = await api.post('/faqs/', faqData)
      
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
      const response = await api.put(`/faqs/${id}/`, faqData)
      
      const updatedFaq = response.data
      
      // Update in list
      const index = faqs.value.findIndex(f => f.id === id)
      if (index !== -1) {
        faqs.value[index] = updatedFaq
      }
      
      // Update current if it's the same
      if (currentFaq.value?.id === id) {
        currentFaq.value = updatedFaq
      }
      
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
      await api.delete(`/faqs/${id}/`)
      
      // Remove from list
      faqs.value = faqs.value.filter(f => f.id !== id)
      
      // Clear current if it's the same
      if (currentFaq.value?.id === id) {
        currentFaq.value = null
      }
      
      return true
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
      categories.value = response.data
      return categories.value
    } catch (err) {
      console.error('Failed to fetch categories:', err)
      return []
    }
  }
  
  async function togglePublished(id) {
    loading.value = true
    error.value = null
    
    try {
      const faq = faqs.value.find(f => f.id === id)
      if (!faq) throw new Error('FAQ not found')
      
      const response = await api.patch(`/faqs/${id}/`, {
        is_published: !faq.is_published
      })
      
      const updatedFaq = response.data
      
      // Update in list
      const index = faqs.value.findIndex(f => f.id === id)
      if (index !== -1) {
        faqs.value[index] = updatedFaq
      }
      
      return updatedFaq
    } catch (err) {
      error.value = err.message || 'Failed to toggle FAQ status'
      console.error('Failed to toggle FAQ status:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  return {
    // State
    faqs,
    currentFaq,
    categories,
    loading,
    error,
    pagination,
    
    // Actions
    fetchFaqs,
    fetchFaq,
    createFaq,
    updateFaq,
    deleteFaq,
    fetchCategories,
    togglePublished,
  }
})
