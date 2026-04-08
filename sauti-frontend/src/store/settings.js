import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/axios'

const SETTINGS_TTL = 5 * 60 * 1000 // 5 minutes
const ORG_PROFILE_TTL = 5 * 60 * 1000 // 5 minutes

function isCacheFresh(timestamp, ttl) {
  if (!timestamp) return false
  return Date.now() - timestamp < ttl
}

export const useSettingsStore = defineStore('settings', () => {
  const settings = ref({})
  const orgProfile = ref({})
  const loading = ref(false)
  const error = ref(null)

  // Cache metadata
  const lastFetchedSettings = ref(null)
  const lastFetchedOrgProfile = ref(null)

  // De-duplication promises (not persisted)
  let fetchingSettingsPromise = null
  let fetchingOrgProfilePromise = null

  async function fetchSettings() {
    // Legacy support: redirect to the new unified fetchGlobalSettings
    await fetchOrganizationProfile()
    return await fetchGlobalSettings()
  }

  async function fetchGlobalSettings(forceRefresh = false) {
    // Return cached data if fresh
    if (!forceRefresh && isCacheFresh(lastFetchedSettings.value, SETTINGS_TTL) && Object.keys(settings.value).length > 0) {
      console.log('[SettingsStore] Using cached settings')
      return settings.value
    }

    // De-duplicate concurrent requests
    if (fetchingSettingsPromise) {
      console.log('[SettingsStore] Deduplicating concurrent fetch')
      return fetchingSettingsPromise
    }

    loading.value = true
    error.value = null

    fetchingSettingsPromise = (async () => {
      try {
        // Ensure organization profile is also fetched
        await fetchOrganizationProfile(forceRefresh)
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

        // 1. Load from GlobalSettings (base)
        const globalData = Array.isArray(settingsRes.data) ? settingsRes.data[0] : settingsRes.data
        if (globalData && typeof globalData === 'object') {
          Object.keys(globalData).forEach(key => {
            if (!['id', 'created_at', 'updated_at'].includes(key) && globalData[key] !== null) {
              // Parse JSON fields if they come as strings (e.g. hero_badges, footer_links, impact_stats)
              if ((key === 'hero_badges' || key === 'footer_links' || key === 'impact_stats') && typeof globalData[key] === 'string') {
                try {
                  mapped[key] = JSON.parse(globalData[key])
                } catch (e) {
                  console.warn(`Failed to parse ${key}:`, e)
                  mapped[key] = []
                }
              } else {
                mapped[key] = globalData[key]
              }
            }
          })
        }

        // 2. Load from SiteContent (overrides)
        if (Array.isArray(contentData)) {
          contentData.forEach(item => {
            const key = item.key || item.name || item.slug
            if (key) {
              mapped[key] = item.value || item.content || ''
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
        lastFetchedSettings.value = Date.now()
        console.log('[SettingsStore] Settings cached:', Object.keys(settings.value).length, 'items')
      } catch (err) {
        error.value = err.message || 'Failed to fetch global settings'
        console.error('Failed to fetch global settings:', err)
      } finally {
        loading.value = false
        fetchingSettingsPromise = null
      }
    })()

    return fetchingSettingsPromise
  }

  async function fetchOrganizationProfile(forceRefresh = false) {
    // Return cached if fresh
    if (!forceRefresh && isCacheFresh(lastFetchedOrgProfile.value, ORG_PROFILE_TTL) && Object.keys(orgProfile.value).length > 0) {
      console.log('[SettingsStore] Using cached organization profile')
      return orgProfile.value
    }

    // De-duplicate
    if (fetchingOrgProfilePromise) {
      return fetchingOrgProfilePromise
    }

    fetchingOrgProfilePromise = (async () => {
      try {
        const response = await api.get('/sitesettings/organization/')
        orgProfile.value = response.data

        // Also inject into settings for easier access in legacy components if needed
        if (orgProfile.value) {
          settings.value.org_name = orgProfile.value.name
          settings.value.org_logo = orgProfile.value.logo
          settings.value.org_favicon = orgProfile.value.favicon
          settings.value.org_team_photo = orgProfile.value.team_photo
          settings.value.primary_color = orgProfile.value.primary_color
          settings.value.secondary_color = orgProfile.value.secondary_color
          // About hero images
          settings.value.about_hero_image_1 = orgProfile.value.about_hero_image_1_url
          settings.value.about_hero_image_2 = orgProfile.value.about_hero_image_2_url
          settings.value.about_hero_image_3 = orgProfile.value.about_hero_image_3_url
          settings.value.about_hero_image_4 = orgProfile.value.about_hero_image_4_url
          settings.value.about_hero_image_5 = orgProfile.value.about_hero_image_5_url
          settings.value.about_hero_image_6 = orgProfile.value.about_hero_image_6_url
          settings.value.about_hero_image_7 = orgProfile.value.about_hero_image_7_url
          settings.value.about_hero_image_8 = orgProfile.value.about_hero_image_8_url

          // Inject all brand colors for easier access
          if (orgProfile.value.brand_colors && Array.isArray(orgProfile.value.brand_colors)) {
            orgProfile.value.brand_colors.forEach(c => {
              settings.value[c.id] = c.value
            })
          }
        }

        lastFetchedOrgProfile.value = Date.now()
        return response.data
      } catch (err) {
        console.error('Failed to fetch organization profile:', err)
        return null
      } finally {
        fetchingOrgProfilePromise = null
      }
    })()

    return fetchingOrgProfilePromise
  }

  function invalidateCache() {
    lastFetchedSettings.value = null
    lastFetchedOrgProfile.value = null
  }

  return { settings, orgProfile, loading, error, lastFetchedSettings, lastFetchedOrgProfile, fetchSettings, fetchGlobalSettings, fetchOrganizationProfile, invalidateCache }
}, {
  persist: {
    key: 'sauti-settings',
    storage: localStorage,
    paths: ['settings', 'orgProfile', 'lastFetchedSettings', 'lastFetchedOrgProfile']
  }
})
