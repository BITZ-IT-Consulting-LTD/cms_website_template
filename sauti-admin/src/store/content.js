import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/api'
import { useToast } from 'vue-toastification'

const toast = useToast()

export const useContentStore = defineStore('content', () => {
  // State
  const loading = ref(false)
  const error = ref(null)

  // Actions
  function setLoading(isLoading) {
    loading.value = isLoading
  }

  function setError(err) {
    error.value = err
  }

  async function fetchContent(url) {
    setLoading(true)
    setError(null)
    try {
      const response = await api.get(url)
      return response.data
    } catch (err) {
      const errorMessage = err.message || 'Failed to fetch content'
      setError(errorMessage)
      toast.error(errorMessage)
      throw err // Re-throw to allow component to handle
    } finally {
      setLoading(false)
    }
  }

  async function updateContent(url, data) {
    setLoading(true)
    setError(null)
    try {
      const response = await api.put(url, data)
      toast.success('Content updated successfully')
      return response.data
    } catch (err) {
      const errorMessage = err.response?.data?.detail || err.message || 'Failed to update content'
      setError(errorMessage)
      toast.error(errorMessage)
      console.error('Update error:', err.response?.data || err.message)
      throw err // Re-throw to allow component to handle
    } finally {
      setLoading(false)
    }
  }

  return {
    loading,
    error,
    setLoading,
    setError,
    fetchContent,
    updateContent,
  }
})