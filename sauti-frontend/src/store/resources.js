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
      
      return data
    } catch (err) {
      error.value = err.response?.data || 'Failed to fetch resources'
      console.error('Failed to fetch resources:', err)
      // Ensure resources is always an array even on error
      resources.value = []
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
      const response = await api.resources.categories.list()
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
