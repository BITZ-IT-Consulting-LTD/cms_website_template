import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/axios'

export const useSettingsStore = defineStore('settings', () => {
  const settings = ref({})
  const loading = ref(false)
  const error = ref(null)

  async function fetchSettings() {
    loading.value = true
    error.value = null
    try {
      const response = await api.get('/sitesettings/settings/')
      settings.value = response.data
    } catch (err) {
      error.value = err.message || 'Failed to fetch settings'
      console.error('Failed to fetch settings:', err)
    } finally {
      loading.value = false
    }
  }

  return { settings, loading, error, fetchSettings }
})
