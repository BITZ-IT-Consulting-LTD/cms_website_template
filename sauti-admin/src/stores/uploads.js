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

  // Mock data structure - in production, this would come from API
  const mockUploads = ref([
    // Home Page - Hero Section
    { id: 1, page: 'home', type: 'photo', key: 'hero_image', label: 'Hero Image', value: '/src/assets/sauti-homepage.avif', currentValue: '/src/assets/sauti-homepage.avif', description: 'Main hero image on homepage' },
    { id: 2, page: 'home', type: 'heading', key: 'hero_title', label: 'Hero Title', value: 'Every child deserves a safe voice.', currentValue: 'Every child deserves a safe voice.', description: 'Main heading on homepage' },
    { id: 3, page: 'home', type: 'text', key: 'hero_subtitle', label: 'Hero Subtitle', value: 'Sauti 116 is free, confidential and available 24/7 across all telecoms. Report abuse, seek guidance, or get urgent help in your language.', currentValue: 'Sauti 116 is free, confidential and available 24/7 across all telecoms. Report abuse, seek guidance, or get urgent help in your language.', description: 'Subtitle text under hero heading' },
    { id: 4, page: 'home', type: 'button', key: 'hero_cta_call', label: 'Hero Call Button', value: 'Call 116 Now', currentValue: 'Call 116 Now', description: 'Call-to-action button text' },
    { id: 5, page: 'home', type: 'button', key: 'hero_cta_report', label: 'Hero Report Button', value: 'Report a Case', currentValue: 'Report a Case', description: 'Report button text' },
    { id: 6, page: 'home', type: 'text', key: 'hero_stats', label: 'Hero Stats Text', value: '1M+ Children Helped', currentValue: '1M+ Children Helped', description: 'Statistics text in hero section' },
    { id: 7, page: 'home', type: 'text', key: 'hero_trust_badge', label: 'Hero Trust Badge', value: 'Trusted by UNICEF', currentValue: 'Trusted by UNICEF', description: 'Trust badge text' },
    { id: 8, page: 'home', type: 'text', key: 'hero_overlay_title', label: 'Hero Overlay Title', value: 'Safe Spaces for Every Child', currentValue: 'Safe Spaces for Every Child', description: 'Overlay text on hero image' },
    { id: 9, page: 'home', type: 'text', key: 'hero_overlay_subtitle', label: 'Hero Overlay Subtitle', value: '24/7 support across Uganda', currentValue: '24/7 support across Uganda', description: 'Overlay subtitle text' },
    
    // Home Page - Quick Access Section
    { id: 10, page: 'home', type: 'heading', key: 'quick_access_title', label: 'Quick Access Section Title', value: 'Get Help & Information', currentValue: 'Get Help & Information', description: 'Section heading for quick access cards' },
    { id: 11, page: 'home', type: 'text', key: 'quick_access_description', label: 'Quick Access Description', value: 'Access our comprehensive support services and resources designed to protect and empower children across Uganda.', currentValue: 'Access our comprehensive support services and resources designed to protect and empower children across Uganda.', description: 'Description text for quick access section' },
    { id: 12, page: 'home', type: 'heading', key: 'card_report_title', label: 'Report Card Title', value: 'Report a Case', currentValue: 'Report a Case', description: 'Title for Report a Case card' },
    { id: 13, page: 'home', type: 'text', key: 'card_report_text', label: 'Report Card Text', value: 'Confidential, fast, and supportive reporting system.', currentValue: 'Confidential, fast, and supportive reporting system.', description: 'Text for Report a Case card' },
    { id: 14, page: 'home', type: 'heading', key: 'card_resources_title', label: 'Resources Card Title', value: 'Resources', currentValue: 'Resources', description: 'Title for Resources card' },
    { id: 15, page: 'home', type: 'text', key: 'card_resources_text', label: 'Resources Card Text', value: 'Guides, policies, and educational toolkits.', currentValue: 'Guides, policies, and educational toolkits.', description: 'Text for Resources card' },
    { id: 16, page: 'home', type: 'heading', key: 'card_faqs_title', label: 'FAQs Card Title', value: 'FAQs', currentValue: 'FAQs', description: 'Title for FAQs card' },
    { id: 17, page: 'home', type: 'text', key: 'card_faqs_text', label: 'FAQs Card Text', value: 'Answers to common questions and concerns.', currentValue: 'Answers to common questions and concerns.', description: 'Text for FAQs card' },
    { id: 18, page: 'home', type: 'heading', key: 'card_partners_title', label: 'Partners Card Title', value: 'Partners', currentValue: 'Partners', description: 'Title for Partners card' },
    { id: 19, page: 'home', type: 'text', key: 'card_partners_text', label: 'Partners Card Text', value: 'MGLSD, UNICEF, UCRNN, ITU collaboration.', currentValue: 'MGLSD, UNICEF, UCRNN, ITU collaboration.', description: 'Text for Partners card' },
    
    // Home Page - Journey Timeline Section
    { id: 20, page: 'home', type: 'heading', key: 'journey_title', label: 'Journey Section Title', value: 'Our Journey', currentValue: 'Our Journey', description: 'Section heading for timeline' },
    { id: 21, page: 'home', type: 'text', key: 'journey_description', label: 'Journey Description', value: 'Key milestones in our history of child advocacy, including international recommendations and national designation of 116.', currentValue: 'Key milestones in our history of child advocacy, including international recommendations and national designation of 116.', description: 'Description for journey section' },
    { id: 22, page: 'home', type: 'heading', key: 'timeline_2005_title', label: 'Timeline 2005 Title', value: 'Launch of Child Helpline Initiative', currentValue: 'Launch of Child Helpline Initiative', description: 'Timeline card title for 2005' },
    { id: 23, page: 'home', type: 'text', key: 'timeline_2005_text', label: 'Timeline 2005 Text', value: 'Inception of the national child protection helpline in partnership with NGOs and international agencies.', currentValue: 'Inception of the national child protection helpline in partnership with NGOs and international agencies.', description: 'Timeline card text for 2005' },
    { id: 24, page: 'home', type: 'heading', key: 'timeline_2010_title', label: 'Timeline 2010 Title', value: 'Launch of Sauti Helpline', currentValue: 'Launch of Sauti Helpline', description: 'Timeline card title for 2010' },
    { id: 25, page: 'home', type: 'text', key: 'timeline_2010_text', label: 'Timeline 2010 Text', value: 'Established as a national child helpline, providing a critical first point of contact.', currentValue: 'Established as a national child helpline, providing a critical first point of contact.', description: 'Timeline card text for 2010' },
    { id: 26, page: 'home', type: 'heading', key: 'timeline_2015_title', label: 'Timeline 2015 Title', value: 'Expansion of Services', currentValue: 'Expansion of Services', description: 'Timeline card title for 2015' },
    { id: 27, page: 'home', type: 'text', key: 'timeline_2015_text', label: 'Timeline 2015 Text', value: 'Introduced counseling and legal support to offer more comprehensive assistance.', currentValue: 'Introduced counseling and legal support to offer more comprehensive assistance.', description: 'Timeline card text for 2015' },
    { id: 28, page: 'home', type: 'heading', key: 'timeline_2016_title', label: 'Timeline 2016 Title', value: 'Legal & Regulatory Backing', currentValue: 'Legal & Regulatory Backing', description: 'Timeline card title for 2016' },
    { id: 29, page: 'home', type: 'text', key: 'timeline_2016_text', label: 'Timeline 2016 Text', value: '116 designated by UCC; strengthened by national child protection policies and frameworks.', currentValue: '116 designated by UCC; strengthened by national child protection policies and frameworks.', description: 'Timeline card text for 2016' },
    { id: 30, page: 'home', type: 'heading', key: 'timeline_2020_title', label: 'Timeline 2020 Title', value: 'Reaching 1 Million Children', currentValue: 'Reaching 1 Million Children', description: 'Timeline card title for 2020' },
    { id: 31, page: 'home', type: 'text', key: 'timeline_2020_text', label: 'Timeline 2020 Text', value: 'A landmark achievement, having provided assistance to over a million children across Uganda.', currentValue: 'A landmark achievement, having provided assistance to over a million children across Uganda.', description: 'Timeline card text for 2020' },
    { id: 32, page: 'home', type: 'text', key: 'timeline_footer', label: 'Timeline Footer Text', value: 'Aligned with ITU recommendation for 116 child helplines; operated under MGLSD in collaboration with NGOs and UN partners.', currentValue: 'Aligned with ITU recommendation for 116 child helplines; operated under MGLSD in collaboration with NGOs and UN partners.', description: 'Footer text below timeline' },
    
    // Home Page - Publications Section
    { id: 33, page: 'home', type: 'heading', key: 'publications_title', label: 'Publications Section Title', value: 'Recent Publications', currentValue: 'Recent Publications', description: 'Section heading for publications' },
    { id: 34, page: 'home', type: 'text', key: 'publications_description', label: 'Publications Description', value: 'Latest articles, videos and resources to help children, families, and communities stay safe and informed.', currentValue: 'Latest articles, videos and resources to help children, families, and communities stay safe and informed.', description: 'Description for publications section' },
    { id: 35, page: 'home', type: 'button', key: 'publications_link', label: 'Publications Link', value: 'View all posts', currentValue: 'View all posts', description: 'Link text to view all posts' },
    
    // Home Page - Trust Partners Section
    { id: 36, page: 'home', type: 'heading', key: 'trust_partners_title', label: 'Trust Partners Title', value: 'Trusted by Leading Organizations', currentValue: 'Trusted by Leading Organizations', description: 'Title for trust partners section' },
    { id: 37, page: 'home', type: 'text', key: 'trust_partners_description', label: 'Trust Partners Description', value: 'Working in partnership with government and international agencies', currentValue: 'Working in partnership with government and international agencies', description: 'Description for trust partners' },
    { id: 38, page: 'home', type: 'heading', key: 'partner_mglsd', label: 'MGLSD Partner', value: 'MGLSD', currentValue: 'MGLSD', description: 'MGLSD partner name' },
    { id: 39, page: 'home', type: 'text', key: 'partner_mglsd_desc', label: 'MGLSD Description', value: 'Ministry of Gender, Labour & Social Development', currentValue: 'Ministry of Gender, Labour & Social Development', description: 'MGLSD description' },
    { id: 40, page: 'home', type: 'heading', key: 'partner_unicef', label: 'UNICEF Partner', value: 'UNICEF', currentValue: 'UNICEF', description: 'UNICEF partner name' },
    { id: 41, page: 'home', type: 'text', key: 'partner_unicef_desc', label: 'UNICEF Description', value: 'United Nations Children\'s Fund', currentValue: 'United Nations Children\'s Fund', description: 'UNICEF description' },
    { id: 42, page: 'home', type: 'heading', key: 'partner_ucrnn', label: 'UCRNN Partner', value: 'UCRNN', currentValue: 'UCRNN', description: 'UCRNN partner name' },
    { id: 43, page: 'home', type: 'text', key: 'partner_ucrnn_desc', label: 'UCRNN Description', value: 'Uganda Child Rights NGO Network', currentValue: 'Uganda Child Rights NGO Network', description: 'UCRNN description' },
    { id: 44, page: 'home', type: 'heading', key: 'partner_itu', label: 'ITU Partner', value: 'ITU 116', currentValue: 'ITU 116', description: 'ITU partner name' },
    { id: 45, page: 'home', type: 'text', key: 'partner_itu_desc', label: 'ITU Description', value: 'International Telecommunication Union', currentValue: 'International Telecommunication Union', description: 'ITU description' },
    
    // Home Page - Final CTA Section
    { id: 46, page: 'home', type: 'heading', key: 'final_cta_title', label: 'Final CTA Title', value: 'Need Help Right Now?', currentValue: 'Need Help Right Now?', description: 'Final CTA section title' },
    { id: 47, page: 'home', type: 'text', key: 'final_cta_text', label: 'Final CTA Text', value: 'Accessible 24/7 across all telecom networks. Support in multiple local languages. All services are free and confidential.', currentValue: 'Accessible 24/7 across all telecom networks. Support in multiple local languages. All services are free and confidential.', description: 'Final CTA section text' },
    { id: 48, page: 'home', type: 'button', key: 'final_cta_call', label: 'Final CTA Call Button', value: 'Call 116 Now', currentValue: 'Call 116 Now', description: 'Final CTA call button' },
    { id: 49, page: 'home', type: 'button', key: 'final_cta_report', label: 'Final CTA Report Button', value: 'Report a Case', currentValue: 'Report a Case', description: 'Final CTA report button' },
    { id: 50, page: 'home', type: 'button', key: 'final_cta_contact', label: 'Final CTA Contact Button', value: 'Contact Us', currentValue: 'Contact Us', description: 'Final CTA contact button' },
    
    // About Page
    { id: 51, page: 'about', type: 'photo', key: 'about_image', label: 'About Page Image', value: '/src/assets/sauti-aboutpage.webp', currentValue: '/src/assets/sauti-aboutpage.webp', description: 'Main image on about page' },
    { id: 52, page: 'about', type: 'heading', key: 'about_title', label: 'About Page Title', value: 'About Sauti', currentValue: 'About Sauti', description: 'Main heading on about page' },
    
    // Operations Page
    { id: 53, page: 'operations', type: 'photo', key: 'operations_image', label: 'Operations Image', value: '/src/assets/our operations and case flow.jpg', currentValue: '/src/assets/our operations and case flow.jpg', description: 'Operations flowchart image' },
    
    // Header
    { id: 54, page: 'header', type: 'photo', key: 'logo', label: 'Site Logo', value: '/src/assets/sauti-logo.jpeg', currentValue: '/src/assets/sauti-logo.jpeg', description: 'Main site logo' },
    { id: 55, page: 'header', type: 'text', key: 'site_name', label: 'Site Name', value: 'Sauti 116 helpline', currentValue: 'Sauti 116 helpline', description: 'Website name in header' },
    
    // Footer
    { id: 56, page: 'footer', type: 'text', key: 'footer_phone', label: 'Footer Phone', value: '116', currentValue: '116', description: 'Helpline phone number' },
    { id: 57, page: 'footer', type: 'text', key: 'footer_email', label: 'Footer Email', value: 'info@sauti.mglsd.go.ug', currentValue: 'info@sauti.mglsd.go.ug', description: 'Contact email' },
    { id: 58, page: 'footer', type: 'text', key: 'footer_address', label: 'Footer Address', value: 'Ministry of Gender, Labour & Social Development, Kampala, Uganda', currentValue: 'Ministry of Gender, Labour & Social Development, Kampala, Uganda', description: 'Physical address' }
  ])

  // Actions
  async function fetchUploads() {
    loading.value = true
    error.value = null
    
    try {
      // In production, this would call: const response = await api.uploads.list()
      // For now, use mock data
      uploads.value = [...mockUploads.value]
      
      // Sync to localStorage on initial load
      syncToLocalStorage()
      
      return uploads.value
    } catch (err) {
      error.value = err.message || 'Failed to fetch uploads'
      console.error('Failed to fetch uploads:', err)
      // Fallback to mock data
      uploads.value = [...mockUploads.value]
      syncToLocalStorage()
      return uploads.value
    } finally {
      loading.value = false
    }
  }

  async function fetchUpload(id) {
    loading.value = true
    error.value = null
    
    try {
      // In production: const response = await api.uploads.get(id)
      const upload = mockUploads.value.find(u => u.id === id)
      if (upload) {
        currentUpload.value = upload
        return upload
      }
      throw new Error('Upload not found')
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
      // In production: const response = await api.uploads.update(id, uploadData)
      const index = uploads.value.findIndex(u => u.id === id)
      if (index !== -1) {
        // Update the upload with new data, ensuring currentValue is set
        const updatedUpload = { 
          ...uploads.value[index], 
          ...uploadData, 
          currentValue: uploadData.value || uploadData.currentValue || uploads.value[index].currentValue || uploads.value[index].value
        }
        uploads.value[index] = updatedUpload
        if (currentUpload.value?.id === id) {
          currentUpload.value = updatedUpload
        }
        
        // Sync to localStorage so frontend can access it
        const syncedContent = syncToLocalStorage()
        
        // Force a refresh by dispatching a custom event
        window.dispatchEvent(new CustomEvent('content-updated'))
        window.dispatchEvent(new CustomEvent('sauti-content-updated', {
          detail: { content: syncedContent }
        }))
        
        return uploads.value[index]
      }
      throw new Error('Upload not found')
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
      
      console.log('Synced to localStorage:', Object.keys(contentMap).length, 'items')
      console.log('Sample key (hero_title):', contentMap['hero_title']?.currentValue || contentMap['hero_title']?.value)
      
      // Trigger storage event for same-window listeners
      // Note: StorageEvent only works across tabs, not same window
      // So we'll rely on polling for same-window updates
      window.dispatchEvent(new CustomEvent('sauti-content-updated', {
        detail: { content: contentMap }
      }))
      
      // Also try to trigger a storage event (won't work in same window but good for cross-tab)
      try {
        window.dispatchEvent(new StorageEvent('storage', {
          key: 'sauti_content',
          newValue: jsonString,
          oldValue: localStorage.getItem('sauti_content'),
          storageArea: localStorage
        }))
      } catch (e) {
        // StorageEvent might not work in all browsers for same-window
        // That's okay, polling will catch it
      }
      
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
      // In production: const response = await api.uploads.create(uploadData)
      const newUpload = {
        id: Date.now(),
        ...uploadData,
        currentValue: uploadData.value
      }
      uploads.value.unshift(newUpload)
      
      // Sync to localStorage so frontend can access it
      syncToLocalStorage()
      
      return newUpload
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
      // In production: await api.uploads.delete(id)
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

