import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/axios'

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
  
  // Actions
  async function fetchResources(params = {}) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.resources.list(params)
      resources.value = response.data.results || response.data
      
      if (response.data.count !== undefined) {
        pagination.value = {
          count: response.data.count,
          next: response.data.next,
          previous: response.data.previous,
        }
      }
      
      return response.data
    } catch (err) {
      error.value = err.response?.data || 'Failed to fetch resources'
      throw err
    } finally {
      loading.value = false
    }
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
  
  async function fetchCategories() {
    try {
      const response = await api.resources.categories()
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
    resources,
    currentResource,
    categories,
    loading,
    error,
    pagination,
    fetchResources,
    fetchResource,
    fetchCategories,
    clearError,
  }
})
