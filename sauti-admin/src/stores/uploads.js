import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/api'

export const useUploadsStore = defineStore('uploads', () => {
  // State
  const uploads = ref([])
  const currentUpload = ref(null)
  const loading = ref(false)
  const error = ref(null)
  const pages = ref([
    { id: 'home', name: 'Home', slug: 'home' },
    { id: 'about', name: 'About', slug: 'about' },
    { id: 'operations', name: 'Operations', slug: 'operations' },
    { id: 'blog', name: 'Blog', slug: 'blog' },
    { id: 'resources', name: 'Resources', slug: 'resources' },
    { id: 'faqs', name: 'FAQs', slug: 'faqs' },
    { id: 'partners', name: 'Partners', slug: 'partners' },
    { id: 'contact', name: 'Contact', slug: 'contact' },
    { id: 'donate', name: 'Donate', slug: 'donate' },
    { id: 'reports', name: 'Reports', slug: 'reports' },
    { id: 'header', name: 'Header', slug: 'header' },
    { id: 'footer', name: 'Footer', slug: 'footer' }
  ])

  const contentTypes = ref([
    { id: 'photo', name: 'Photos/Images', icon: 'PhotoIcon' },
    { id: 'heading', name: 'Headings', icon: 'HeadingIcon' },
    { id: 'text', name: 'Text Content', icon: 'DocumentTextIcon' },
    { id: 'button', name: 'Buttons/Links', icon: 'CursorArrowRaysIcon' },
    { id: 'video', name: 'Videos', icon: 'VideoCameraIcon' },
    { id: 'icon', name: 'Icons', icon: 'SparklesIcon' }
  ])

  // Actions
  async function fetchUploads() {
    loading.value = true
    error.value = null

    try {
      const response = await api.get('/content/')
      uploads.value = response.data.results || response.data

      // Sync to localStorage on initial load
      syncToLocalStorage()

      return uploads.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch uploads'
      console.error('Failed to fetch uploads:', err)
      return []
    } finally {
      loading.value = false
    }
  }

  async function fetchUpload(key) {
    loading.value = true
    error.value = null

    try {
      const response = await api.get(`/content/${key}/`)
      currentUpload.value = response.data
      return response.data
    } catch (err) {
      error.value = err.message || 'Failed to fetch upload'
      throw err
    } finally {
      loading.value = false
    }
  }

  async function updateUpload(id, uploadData) {
    loading.value = true
    error.value = null

    try {
      // Find the upload to get its key
      const upload = uploads.value.find(u => u.id === id)
      if (!upload) throw new Error('Upload not found')

      const response = await api.patch(`/content/${upload.key}/`, uploadData)

      const index = uploads.value.findIndex(u => u.id === id)
      if (index !== -1) {
        uploads.value[index] = response.data
        if (currentUpload.value?.id === id) {
          currentUpload.value = response.data
        }

        // Sync to localStorage so frontend can access it
        const syncedContent = syncToLocalStorage()

        // Force a refresh by dispatching a custom event
        window.dispatchEvent(new CustomEvent('content-updated'))
        window.dispatchEvent(new CustomEvent('sauti-content-updated', {
          detail: { content: syncedContent }
        }))

        return response.data
      }
    } catch (err) {
      error.value = err.message || 'Failed to update upload'
      throw err
    } finally {
      loading.value = false
    }
  }

  function syncToLocalStorage() {
    try {
      // Convert uploads array to object keyed by content key
      const contentMap = {}
      uploads.value.forEach(upload => {
        contentMap[upload.key] = {
          key: upload.key,
          value: upload.value,
          currentValue: upload.currentValue || upload.value,
          page: upload.page,
          type: upload.type,
          label: upload.label,
          description: upload.description
        }
      })
      const jsonString = JSON.stringify(contentMap)
      localStorage.setItem('sauti_content', jsonString)

      // Trigger storage event for same-window listeners
      window.dispatchEvent(new CustomEvent('sauti-content-updated', {
        detail: { content: contentMap }
      }))

      return contentMap
    } catch (err) {
      console.error('Failed to sync to localStorage:', err)
      return {}
    }
  }

  async function createUpload(uploadData) {
    loading.value = true
    error.value = null

    try {
      const response = await api.post('/content/', uploadData)
      uploads.value.unshift(response.data)

      // Sync to localStorage so frontend can access it
      syncToLocalStorage()

      return response.data
    } catch (err) {
      error.value = err.message || 'Failed to create upload'
      throw err
    } finally {
      loading.value = false
    }
  }

  async function deleteUpload(id) {
    loading.value = true
    error.value = null

    try {
      const upload = uploads.value.find(u => u.id === id)
      if (!upload) throw new Error('Upload not found')

      await api.delete(`/content/${upload.key}/`)

      uploads.value = uploads.value.filter(u => u.id !== id)
      if (currentUpload.value?.id === id) {
        currentUpload.value = null
      }
      return true
    } catch (err) {
      error.value = err.message || 'Failed to delete upload'
      throw err
    } finally {
      loading.value = false
    }
  }

  function getUploadsByPage(page) {
    return uploads.value.filter(u => u.page === page)
  }

  function getUploadsByType(type) {
    return uploads.value.filter(u => u.type === type)
  }

  return {
    // State
    uploads,
    currentUpload,
    pages,
    contentTypes,
    loading,
    error,

    // Actions
    fetchUploads,
    fetchUpload,
    updateUpload,
    createUpload,
    deleteUpload,
    getUploadsByPage,
    getUploadsByType
  }
})

