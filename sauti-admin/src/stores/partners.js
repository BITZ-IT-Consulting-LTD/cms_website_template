import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/api'

export const usePartnersStore = defineStore('partners', () => {
  // State
  const partners = ref([])
  const currentPartner = ref(null)
  const loading = ref(false)
  const error = ref(null)
  
  // Actions
  async function fetchPartners(params = {}) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.partners.list(params)
      partners.value = response.data.results || response.data
      return partners.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch partners'
      console.error('Failed to fetch partners:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function fetchPartner(slug) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.partners.get(slug)
      currentPartner.value = response.data
      return currentPartner.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch partner'
      console.error('Failed to fetch partner:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function createPartner(partnerData) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.partners.create(partnerData)
      const newPartner = response.data
      partners.value.unshift(newPartner)
      return newPartner
    } catch (err) {
      error.value = err.message || 'Failed to create partner'
      console.error('Failed to create partner:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function updatePartner(slug, partnerData) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.partners.update(slug, partnerData)
      const updatedPartner = response.data
      
      // Update in list
      const index = partners.value.findIndex(p => p.slug === slug)
      if (index !== -1) {
        partners.value[index] = updatedPartner
      }
      currentPartner.value = updatedPartner
      return updatedPartner
    } catch (err) {
      error.value = err.message || 'Failed to update partner'
      console.error('Failed to update partner:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function deletePartner(slug) {
    loading.value = true
    error.value = null
    
    try {
      await api.partners.delete(slug)
      partners.value = partners.value.filter(p => p.slug !== slug)
      if (currentPartner.value?.slug === slug) {
        currentPartner.value = null
      }
    } catch (err) {
      error.value = err.message || 'Failed to delete partner'
      console.error('Failed to delete partner:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  return {
    // State
    partners,
    currentPartner,
    loading,
    error,
    
    // Actions
    fetchPartners,
    fetchPartner,
    createPartner,
    updatePartner,
    deletePartner,
  }
})