import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/axios'

export const useSettingsStore = defineStore('settings', () => {
  const settings = ref({})
  const loading = ref(false)
  const error = ref(null)

  async function fetchSettings() {
    // Legacy support: redirect to the new unified fetchGlobalSettings
    return await fetchGlobalSettings()
  }

  async function fetchGlobalSettings() {
    loading.value = true
    error.value = null
    try {
      // Fetch from both sources
      const [contentRes, settingsRes] = await Promise.all([
        api.get('/content/site-content/'),
        api.get('/sitesettings/').catch(() => ({ data: {} })) // Fallback if not available
      ])

      let contentData = contentRes.data
      if (contentData && contentData.results && Array.isArray(contentData.results)) {
        contentData = contentData.results
      }

      const mapped = {}

      // 1. Load from SiteContent (legacy/key-value)
      if (Array.isArray(contentData)) {
        contentData.forEach(item => {
          const key = item.key || item.name || item.slug
          if (key) {
            mapped[key] = item.value || item.content || ''
          }
        })
      }

      // 2. Load from GlobalSettings (new singleton) - Overwrite if keys conflict
      const globalData = Array.isArray(settingsRes.data) ? settingsRes.data[0] : settingsRes.data
      if (globalData && typeof globalData === 'object') {
        Object.keys(globalData).forEach(key => {
          // Only add non-internal keys
          if (!['id', 'created_at', 'updated_at'].includes(key) && globalData[key] !== null) {
            mapped[key] = globalData[key]
          }
        })
      }

      // Aliasing mapping for compatibility with existing templates
      if (mapped['card_services_title'] && !mapped['card_resources_title']) {
        mapped['card_resources_title'] = mapped['card_services_title']
      }
      if (mapped['card_services_text'] && !mapped['card_resources_text']) {
        mapped['card_resources_text'] = mapped['card_services_text']
      }

      settings.value = mapped
      console.log('Unified settings loaded:', Object.keys(settings.value).length, 'items')
    } catch (err) {
      error.value = err.message || 'Failed to fetch global settings'
      console.error('Failed to fetch global settings:', err)
    } finally {
      loading.value = false
    }
  }

  return { settings, loading, error, fetchSettings, fetchGlobalSettings }
})
