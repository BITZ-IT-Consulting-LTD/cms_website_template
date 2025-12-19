import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/axios'

// DEPRECATED: This store is deprecated and will be removed in a future version.
// Global site settings are now managed by the `useSettingsStore`.
export const useContentStore = defineStore('content', () => {
  // State
  const content = ref({})
  const loading = ref(false)
  const error = ref(null)

  // Get content by key (reactive function)
  // Accessing content.value inside makes it reactive
  function getContent(key, defaultValue = '') {
    const item = content.value[key]
    const value = item?.currentValue || item?.value

    if (value) {
      return value
    }

    const defaultItem = getDefaultContent()[key]
    const defaultValueFromContent = defaultItem?.currentValue || defaultItem?.value

    return defaultValueFromContent || defaultValue
  }

  // Get content by page and key
  const getContentByPage = (page, key, defaultValue = '') => {
    const item = Object.values(content.value).find(
      item => item.page === page && item.key === key
    )
    return item?.currentValue || item?.value || defaultValue
  }

  // Actions
  async function fetchContent() {
    loading.value = true
    error.value = null

    try {
      // Try to fetch from API first (but don't fail if it doesn't exist)
      try {
        const response = await api.get('/content/site-content/') // Corrected endpoint
        const data = response.data

        // Convert array to object keyed by content key
        const contentMap = {}
        if (Array.isArray(data)) {
          data.forEach(item => {
            contentMap[item.key] = item
          })
        } else if (data.results && Array.isArray(data.results)) {
          data.results.forEach(item => {
            contentMap[item.key] = item
          })
        }
        const defaultContent = getDefaultContent()
        content.value = { ...defaultContent, ...contentMap }
        // Also save to localStorage as backup
        localStorage.setItem('sauti_content', JSON.stringify(content.value))
        console.log('Content loaded from API:', Object.keys(content.value).length, 'items')
        return content.value
      } catch (apiError) {
        // If API fails (404 is expected), try localStorage as fallback
        if (apiError.response?.status !== 404) {
          console.warn('API fetch failed, using localStorage:', apiError)
        }
        const stored = localStorage.getItem('sauti_content')
        if (stored) {
          const parsed = JSON.parse(stored)
          content.value = parsed
          console.log('Content loaded from localStorage:', Object.keys(content.value).length, 'items')
          return content.value
        }
        // If no stored data, use default content
        content.value = getDefaultContent()
        console.log('Using default content:', Object.keys(content.value).length, 'items')
        // Save defaults to localStorage
        localStorage.setItem('sauti_content', JSON.stringify(content.value))
        return content.value
      }
    } catch (err) {
      error.value = err.message || 'Failed to fetch content'
      console.error('Failed to fetch content:', err)
      // Fallback to localStorage
      const stored = localStorage.getItem('sauti_content')
      if (stored) {
        try {
          content.value = JSON.parse(stored)
          console.log('Content loaded from localStorage (fallback):', Object.keys(content.value).length, 'items')
        } catch (parseErr) {
          console.error('Failed to parse localStorage:', parseErr)
          content.value = getDefaultContent()
        }
      } else {
        content.value = getDefaultContent()
      }
      return content.value
    } finally {
      loading.value = false
    }
  }

  // Get default content (fallback)
  function getDefaultContent() {
    return {
      hero_title: { key: 'hero_title', value: 'Every One Deserves to Be Heard.', currentValue: 'Every One Deserves to Be Heard.', page: 'home', type: 'heading' },
      hero_subtitle: { key: 'hero_subtitle', value: 'Sauti 116 is free, confidential and available 24/7 across all telecoms. Report abuse, seek guidance, or get urgent help in your language.', currentValue: 'Sauti 116 is free, confidential and available 24/7 across all telecoms. Report abuse, seek guidance, or get urgent help in your language.', page: 'home', type: 'text' },
      hero_cta_call: { key: 'hero_cta_call', value: 'Call 116 Now', currentValue: 'Call 116 Now', page: 'home', type: 'button' },
      hero_cta_report: { key: 'hero_cta_report', value: 'Report a Case', currentValue: 'Report a Case', page: 'home', type: 'button' },
      quick_access_title: { key: 'quick_access_title', value: 'Get Help & Information', currentValue: 'Get Help & Information', page: 'home', type: 'heading' },
      quick_access_description: { key: 'quick_access_description', value: 'Access our comprehensive support services and resources designed to protect and empower children across Uganda.', currentValue: 'Access our comprehensive support services and resources designed to protect and empower children across Uganda.', page: 'home', type: 'text' },
      card_report_title: { key: 'card_report_title', value: 'Report a Case', currentValue: 'Report a Case', page: 'home', type: 'heading' },
      card_report_text: { key: 'card_report_text', value: 'Report abuse confidentially. Our trained counselors are available 24/7 to listen and support you.', currentValue: 'Report abuse confidentially. Our trained counselors are available 24/7 to listen and support you.', page: 'home', type: 'text' },
      card_resources_title: { key: 'card_resources_title', value: 'Resources', currentValue: 'Resources', page: 'home', type: 'heading' },
      card_resources_text: { key: 'card_resources_text', value: 'Access vital information, safety guides, and educational materials to protect children.', currentValue: 'Access vital information, safety guides, and educational materials to protect children.', page: 'home', type: 'text' },
      card_faqs_title: { key: 'card_faqs_title', value: 'FAQs', currentValue: 'FAQs', page: 'home', type: 'heading' },
      card_faqs_text: { key: 'card_faqs_text', value: 'Find quick answers to common questions about our services, reporting process, and safety.', currentValue: 'Find quick answers to common questions about our services, reporting process, and safety.', page: 'home', type: 'text' },
      card_partners_title: { key: 'card_partners_title', value: 'Partners', currentValue: 'Partners', page: 'home', type: 'heading' },
      card_partners_text: { key: 'card_partners_text', value: 'Collaborating with government and international organizations to ensure child safety.', currentValue: 'Collaborating with government and international organizations to ensure child safety.', page: 'home', type: 'text' },
      journey_title: { key: 'journey_title', value: 'Our Journey', currentValue: 'Our Journey', page: 'home', type: 'heading' },
      journey_description: { key: 'journey_description', value: 'Key milestones in our history of child advocacy, including international recommendations and national designation of 116.', currentValue: 'Key milestones in our history of child advocacy, including international recommendations and national designation of 116.', page: 'home', type: 'text' },
      publications_title: { key: 'publications_title', value: 'Recent Publications', currentValue: 'Recent Publications', page: 'home', type: 'heading' },
      publications_description: { key: 'publications_description', value: 'Latest articles, videos and resources to help children, families, and communities stay safe and informed.', currentValue: 'Latest articles, videos and resources to help children, families, and communities stay safe and informed.', page: 'home', type: 'text' },
      publications_link: { key: 'publications_link', value: 'View all posts', currentValue: 'View all posts', page: 'home', type: 'button' },
      trust_partners_title: { key: 'trust_partners_title', value: 'Trusted by Leading Organizations', currentValue: 'Trusted by Leading Organizations', page: 'home', type: 'heading' },
      trust_partners_description: { key: 'trust_partners_description', value: 'Working in partnership with government and international agencies', currentValue: 'Working in partnership with government and international agencies', page: 'home', type: 'text' },
      final_cta_title: { key: 'final_cta_title', value: 'Need Help Right Now?', currentValue: 'Need Help Right Now?', page: 'home', type: 'heading' },
      final_cta_text: { key: 'final_cta_text', value: 'Accessible 24/7 across all telecom networks. Support in multiple local languages. All services are free and confidential.', currentValue: 'Accessible 24/7 across all telecom networks. Support in multiple local languages. All services are free and confidential.', page: 'home', type: 'text' },
      final_cta_call: { key: 'final_cta_call', value: 'Call 116 Now', currentValue: 'Call 116 Now', page: 'home', type: 'button' },
      final_cta_report: { key: 'final_cta_report', value: 'Report a Case', currentValue: 'Report a Case', page: 'home', type: 'button' },
      final_cta_contact: { key: 'final_cta_contact', value: 'Contact Us', currentValue: 'Contact Us', page: 'home', type: 'button' },

      // Social Media & External Links
      social_facebook: { key: 'social_facebook', value: 'https://www.facebook.com/Sauti116Helpline', currentValue: 'https://www.facebook.com/Sauti116Helpline', page: 'footer', type: 'text' },
      social_twitter: { key: 'social_twitter', value: 'https://x.com/sauti116', currentValue: 'https://x.com/sauti116', page: 'footer', type: 'text' },
      social_whatsapp: { key: 'social_whatsapp', value: 'https://wa.me/256743889999', currentValue: 'https://wa.me/256743889999', page: 'footer', type: 'text' },
      social_ureport: { key: 'social_ureport', value: 'https://ureport.in', currentValue: 'https://ureport.in', page: 'footer', type: 'text' },
      social_safepal: { key: 'social_safepal', value: 'https://www.unicef.org/uganda/safepal-app', currentValue: 'https://www.unicef.org/uganda/safepal-app', page: 'footer', type: 'text' },

      // Contact Info
      contact_email_info: { key: 'contact_email_info', value: 'info@sauti.mglsd.go.ug', currentValue: 'info@sauti.mglsd.go.ug', page: 'contact', type: 'text' },
      contact_email_sautichl: { key: 'contact_email_sautichl', value: 'sautichl@mglsd.go.ug', currentValue: 'sautichl@mglsd.go.ug', page: 'contact', type: 'text' },
      contact_website: { key: 'contact_website', value: 'https://sauti.mglsd.go.ug', currentValue: 'https://sauti.mglsd.go.ug', page: 'contact', type: 'text' },
      contact_phone_main: { key: 'contact_phone_main', value: '116', currentValue: '116', page: 'contact', type: 'text' }
    }
  }



  // Initial fetch
  fetchContent().then(() => {
    console.log('Content store initialized with', Object.keys(content.value).length, 'items')
  })

  // Also listen for same-window storage events (for admin updates)
  window.addEventListener('storage', (e) => {
    if (e.key === 'sauti_content') {
      try {
        const parsed = JSON.parse(e.newValue || '{}')
        content.value = { ...parsed } // Create new object for reactivity
        console.log('Content updated from storage event:', Object.keys(parsed).length, 'items')
      } catch (err) {
        console.error('Failed to parse storage content:', err)
      }
    }
  })

  // Listen for custom content-updated event from admin
  window.addEventListener('sauti-content-updated', (e) => {
    if (e.detail && e.detail.content) {
      // Create a new object to trigger Vue reactivity
      content.value = { ...e.detail.content }
      console.log('✅ Content updated from custom event:', Object.keys(content.value).length, 'items')
      if (content.value['hero_title']) {
        console.log('📝 hero_title from event:', content.value['hero_title'].currentValue || content.value['hero_title'].value)
      }
    } else {
      // Fallback: refetch from localStorage
      fetchContent()
    }
  })

  // Also listen for the generic content-updated event
  window.addEventListener('content-updated', () => {
    fetchContent()
  })

  // Watch for localStorage changes (works across tabs)
  window.addEventListener('storage', (e) => {
    if (e.key === 'sauti_content' && e.newValue) {
      try {
        const parsed = JSON.parse(e.newValue)
        content.value = parsed
        console.log('Content updated from storage event (cross-tab):', Object.keys(parsed).length, 'items')
      } catch (err) {
        console.error('Failed to parse storage event content:', err)
      }
    }
  })

  return {
    // State
    content,
    loading,
    error,

    // Computed
    getContent,
    getContentByPage,

    // Actions
    fetchContent,
  }
})
