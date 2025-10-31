import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/api'

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
      
      // Handle pagination
      if (data.count !== undefined) {
        pagination.value = {
          count: data.count,
          next: data.next,
          previous: data.previous,
        }
      }
      
      return resources.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch resources'
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
      return currentResource.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch resource'
      console.error('Failed to fetch resource:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function createResource(resourceData) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.resources.create(resourceData)
      
      const newResource = response.data
      resources.value.unshift(newResource)
      return newResource
    } catch (err) {
      error.value = err.message || 'Failed to create resource'
      console.error('Failed to create resource:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function updateResource(slug, resourceData) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.resources.update(slug, resourceData)
      
      const updatedResource = response.data
      
      // Update in list
      const index = resources.value.findIndex(r => r.slug === slug)
      if (index !== -1) {
        resources.value[index] = updatedResource
      }
      
      // Update current if it's the same
      if (currentResource.value?.slug === slug) {
        currentResource.value = updatedResource
      }
      
      return updatedResource
    } catch (err) {
      error.value = err.message || 'Failed to update resource'
      console.error('Failed to update resource:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function deleteResource(slug) {
    loading.value = true
    error.value = null
    
    try {
      await api.resources.delete(slug)
      
      // Remove from list
      resources.value = resources.value.filter(r => r.slug !== slug)
      
      // Clear current if it's the same
      if (currentResource.value?.slug === slug) {
        currentResource.value = null
      }
      
      return true
    } catch (err) {
      error.value = err.message || 'Failed to delete resource'
      console.error('Failed to delete resource:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function fetchCategories() {
    try {
      const response = await api.resources.categories.list()
      // Ensure categories is always an array
      const data = response.data
      categories.value = Array.isArray(data) ? data : (data.results && Array.isArray(data.results) ? data.results : [])
      return categories.value
    } catch (err) {
      console.error('Failed to fetch categories:', err)
      // Always ensure categories is an array
      categories.value = []
      return []
    }
  }
  
  return {
    // State
    resources,
    currentResource,
    categories,
    loading,
    error,
    pagination,
    
    // Actions
    fetchResources,
    fetchResource,
    createResource,
    updateResource,
    deleteResource,
    fetchCategories,
  }
})
