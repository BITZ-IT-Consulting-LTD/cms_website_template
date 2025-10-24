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
      const formData = new FormData()
      Object.keys(partnerData).forEach(key => {
        if (partnerData[key] !== null && partnerData[key] !== undefined) {
          formData.append(key, partnerData[key])
        }
      })
      
      const response = await api.post('/partners/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      
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
      const formData = new FormData()
      Object.keys(partnerData).forEach(key => {
        if (partnerData[key] !== null && partnerData[key] !== undefined) {
          formData.append(key, partnerData[key])
        }
      })
      
      const response = await api.put(`/partners/${slug}/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      
      const updatedPartner = response.data
      
      // Update in list
      const index = partners.value.findIndex(p => p.slug === slug)
      if (index !== -1) {
        partners.value[index] = updatedPartner
      }
      
      // Update current if it's the same
      if (currentPartner.value?.slug === slug) {
        currentPartner.value = updatedPartner
      }
      
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
      await api.delete(`/partners/${slug}/`)
      
      // Remove from list
      partners.value = partners.value.filter(p => p.slug !== slug)
      
      // Clear current if it's the same
      if (currentPartner.value?.slug === slug) {
        currentPartner.value = null
      }
      
      return true
    } catch (err) {
      error.value = err.message || 'Failed to delete partner'
      console.error('Failed to delete partner:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function toggleActive(slug) {
    loading.value = true
    error.value = null
    
    try {
      const partner = partners.value.find(p => p.slug === slug)
      if (!partner) throw new Error('Partner not found')
      
      const response = await api.patch(`/partners/${slug}/`, {
        is_active: !partner.is_active
      })
      
      const updatedPartner = response.data
      
      // Update in list
      const index = partners.value.findIndex(p => p.slug === slug)
      if (index !== -1) {
        partners.value[index] = updatedPartner
      }
      
      return updatedPartner
    } catch (err) {
      error.value = err.message || 'Failed to toggle partner status'
      console.error('Failed to toggle partner status:', err)
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
    toggleActive,
  }
})
