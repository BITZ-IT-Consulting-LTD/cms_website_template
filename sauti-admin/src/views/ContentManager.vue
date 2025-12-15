<template>
  <div class="p-8">
    <h1 class="text-3xl font-bold mb-8">Manage Site Content</h1>

    <div class="mb-8 border-b border-gray-200">
      <nav class="flex space-x-8" aria-label="Main Tabs">
        <button
          v-for="mainTab in mainNavTabs"
          :key="mainTab.value"
          @click="activeMainTab = mainTab.value"
          :class="[
            'px-3 py-2 font-medium text-sm rounded-md',
            activeMainTab === mainTab.value ? 'bg-blue-100 text-blue-700' : 'text-gray-500 hover:text-gray-700'
          ]"
        >
          {{ mainTab.label }}
        </button>
      </nav>
    </div>

    <div v-if="currentSubTabs.length > 0" class="mb-8 border-b border-gray-200">
      <nav class="flex space-x-4" aria-label="Sub Tabs">
        <button
          v-for="subTab in currentSubTabs"
          :key="subTab.value"
          @click="activeSubTab = subTab.value"
          :class="[
            'px-3 py-2 font-medium text-xs rounded-md',
            activeSubTab === subTab.value ? 'bg-gray-200 text-gray-800' : 'text-gray-500 hover:text-gray-700'
          ]"
        >
          {{ subTab.label }}
        </button>
      </nav>
    </div>

    <div v-if="loading" class="text-center">
      <p>Loading content...</p>
    </div>

    <div v-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
      <strong class="font-bold">Error!</strong>
      <span class="block sm:inline">{{ error }}</span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="(item, index) in currentTabContent" :key="item.id || item.key || index" class="bg-white rounded-lg shadow-md p-6 flex flex-col justify-between">
        <div>
          <h2 class="text-xl font-semibold mb-2">
            {{ item.key ? item.key.replace(/_/g, ' ').split(' ').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join(' ') : item.name || item.title || item.label || 'N/A' }}
          </h2>
          <p v-if="item.description" class="text-gray-600 mb-4">{{ item.description }}</p>
          <div class="bg-gray-100 rounded-md p-4 text-gray-800">
            <p class="truncate">{{ item.value || 'N/A' }}</p>
          </div>
        </div>
        <button @click="openEditModal(item)" class="mt-6 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
          Edit
        </button>
      </div>
    </div>

    <!-- Edit Modal -->
    <div v-if="showModal" class="fixed z-10 inset-0 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 transition-opacity" aria-hidden="true">
          <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
        </div>

        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>

        <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <h3 class="text-lg leading-6 font-medium text-gray-900 mb-4">
              Edit Content: {{ currentContent.key ? currentContent.key.replace(/_/g, ' ').split(' ').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join(' ') : currentContent.name || currentContent.label || 'N/A' }}
            </h3>
            <div class="mt-2">
              <textarea v-model="currentContent.value" rows="10" class="w-full border border-gray-300 rounded-md p-2"></textarea>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
            <button @click="saveContent" type="button" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm">
              Save
            </button>
            <button @click="closeModal" type="button" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import { useContentStore } from '@/store/content'
import { api } from '@/utils/api' // Assuming api is available for direct calls

const contentStore = useContentStore()
const { loading, error, setLoading, setError, updateContent } = contentStore // Destructure actions from store

const showModal = ref(false)
const currentContent = ref(null)
const activeMainTab = ref('home') // Default active main tab
const activeSubTab = ref('') // Default active sub tab
const contentTypesApiMap = ref({}) // Stores the map from /api/content/ (e.g., { 'site-content': 'url' })
const currentTabContent = ref([]) // Stores content for the active sub tab

// Define Main Navigation Tabs
const mainNavTabs = [
  { value: 'home', label: 'Home' },
  { value: 'about', label: 'About' },
  { value: 'services', label: 'Services' },
  { value: 'blog', label: 'Blog' },
  { value: 'videos', label: 'Videos' },
  { value: 'resources', label: 'Resources' },
  { value: 'faqs', label: 'FAQs' },
  { value: 'partners', label: 'Partners' },
  { value: 'social-media', label: 'Social Media' },
  { value: 'timeline', label: 'Timeline' },
  { value: 'contact', label: 'Contact' },
  { value: 'operations', label: 'Operations' },
]

// Define Sub-Tab Mapping for each Main Tab
const subTabMapping = {
  home: [
    { value: 'hero-section', label: 'Hero Section', contentType: 'site-content', filterKeys: ['hero_title', 'hero_subtitle', 'hero_button_text'], apiUrlKey: 'site-content' },
    { value: 'about-overview', label: 'About Overview', contentType: 'site-content', filterKeys: ['about_section_title', 'about_section_content'], apiUrlKey: 'site-content' },
    // Add more sub-tabs for Home page
  ],
  about: [
    { value: 'hero', label: 'Hero Section', contentType: 'site-content', filterKeys: ['about_hero_title', 'about_hero_subtitle', 'about_image', 'about_title'], apiUrlKey: 'site-content' },
    { value: 'mission-values', label: 'Mission & Values', contentType: 'site-content', filterKeys: ['about_mission_text', 'about_mission_title', 'about_values_title'], apiUrlKey: 'site-content' },
    { value: 'stats', label: 'Stats', contentType: 'site-content', filterKeys: ['about_stat_1_text', 'about_stat_1_title', 'about_stat_2_text', 'about_stat_2_title', 'about_stat_3_text', 'about_stat_3_title', 'about_stat_4_text', 'about_stat_4_title'], apiUrlKey: 'site-content' },
    { value: 'services', label: 'Services', contentType: 'site-content', filterKeys: ['about_service_1_text', 'about_service_1_title', 'about_service_2_text', 'about_service_2_title', 'about_service_3_text', 'about_service_3_title', 'about_service_4_text', 'about_service_4_title', 'about_service_5_text', 'about_service_5_title'], apiUrlKey: 'site-content' },
    { value: 'background', label: 'Background', contentType: 'site-content', filterKeys: ['about_background_item_1', 'about_background_item_2', 'about_background_item_3', 'about_background_item_4', 'about_background_item_5', 'about_background_item_6', 'about_background_note', 'about_background_title'], apiUrlKey: 'site-content' },
    { value: 'journey', label: 'Journey', contentType: 'site-content', filterKeys: ['about_journey_item_1_text', 'about_journey_item_1_title', 'about_journey_item_1_year', 'about_journey_item_2_text', 'about_journey_item_2_title', 'about_journey_item_2_year', 'about_journey_item_3_text', 'about_journey_item_3_title', 'about_journey_item_3_year', 'about_journey_item_4_text', 'about_journey_item_4_title', 'about_journey_item_4_year', 'about_journey_item_5_text', 'about_journey_item_5_title', 'about_journey_item_5_year', 'about_journey_item_6_text', 'about_journey_item_6_title', 'about_journey_item_6_year', 'about_journey_subtitle', 'about_journey_title'], apiUrlKey: 'site-content' },
    { value: 'operations', label: 'Operations', contentType: 'site-content', filterKeys: ['about_operations_item_1', 'about_operations_item_2', 'about_operations_item_3', 'about_operations_item_4', 'about_operations_title'], apiUrlKey: 'site-content' },
    { value: 'resolution', label: 'Path to Resolution', contentType: 'site-content', filterKeys: ['about_resolution_card_1_text', 'about_resolution_card_1_title', 'about_resolution_card_2_title', 'about_resolution_card_3_title', 'about_resolution_card_4_text', 'about_resolution_card_4_title', 'about_resolution_card_5_text', 'about_resolution_card_5_title', 'about_resolution_title'], apiUrlKey: 'site-content' },
    { value: 'partners-cta', label: 'Partners & CTA', contentType: 'site-content', filterKeys: ['about_partner_1', 'about_partner_2', 'about_partner_3', 'about_partner_4', 'about_partners_text', 'about_partners_title', 'about_cta_text', 'about_cta_title'], apiUrlKey: 'site-content' },
  ],
  services: [
    { value: 'page-content', label: 'Page Content', contentType: 'site-content', filterKeys: ['services_page_title', 'services_intro_text'], apiUrlKey: 'site-content' },
    { value: 'all-services', label: 'All Services', contentType: 'services', apiUrlKey: 'services' },
  ],
  blog: [
    { value: 'page-content', label: 'Page Content', contentType: 'site-content', filterKeys: ['blog_page_title', 'blog_intro_text'], apiUrlKey: 'site-content' },
    { value: 'blog-posts', label: 'Blog Posts', contentType: 'posts', apiUrlKey: 'posts' },
  ],
  videos: [
    { value: 'hero', label: 'Hero Section', contentType: 'site-content', filterKeys: ['videos_title'], apiUrlKey: 'site-content' },
    { value: 'search-filters', label: 'Search & Filters', contentType: 'site-content', filterKeys: ['videos_search_placeholder', 'videos_search_button', 'videos_resources_link', 'videos_chip_all', 'videos_chip_education', 'videos_chip_safety', 'videos_chip_support', 'videos_chip_recency', 'videos_chip_popular'], apiUrlKey: 'site-content' },
    { value: 'all-videos', label: 'All Videos', contentType: 'videos', apiUrlKey: 'videos' },
  ],
  resources: [
    { value: 'hero', label: 'Hero Section', contentType: 'site-content', filterKeys: ['resources_title'], apiUrlKey: 'site-content' },
    { value: 'search-filters', label: 'Search & Filters', contentType: 'site-content', filterKeys: ['resources_search_placeholder', 'resources_search_button', 'resources_chip_all', 'resources_chip_guides', 'resources_chip_infographics', 'resources_chip_reports', 'resources_chip_tools'], apiUrlKey: 'site-content' },
    { value: 'all-resources', label: 'All Resources', contentType: 'resources', apiUrlKey: 'resources' },
  ],
  faqs: [
    { value: 'support', label: 'Support', contentType: 'site-content', filterKeys: ['faqs_support_title', 'faqs_support_subtitle'], apiUrlKey: 'site-content' },
    { value: 'quick-response', label: 'Quick Response', contentType: 'site-content', filterKeys: ['faqs_quick_response_title', 'faqs_quick_response_subtitle', 'faqs_quick_response_text'], apiUrlKey: 'site-content' },
    { value: 'immediate-help', label: 'Immediate Help', contentType: 'site-content', filterKeys: ['faqs_immediate_help_title', 'faqs_immediate_help_subtitle', 'faqs_call_button'], apiUrlKey: 'site-content' },
    { value: 'page-content', label: 'Page Content', contentType: 'site-content', filterKeys: ['faqs_page_title', 'faqs_page_subtitle', 'faqs_search_placeholder', 'faqs_all_categories_button', 'faqs_no_results', 'faqs_no_results_subtitle'], apiUrlKey: 'site-content' },
    { value: 'footer', label: 'Footer', contentType: 'site-content', filterKeys: ['faqs_privacy_policy', 'faqs_terms_of_service', 'faqs_contact_us', 'faqs_footer_text'], apiUrlKey: 'site-content' },
    { value: 'all-faqs', label: 'All FAQs', contentType: 'faqs', apiUrlKey: 'faqs' },
  ],
  partners: [
    { value: 'hero', label: 'Hero Section', contentType: 'site-content', filterKeys: ['partners_title', 'partners_subtitle'], apiUrlKey: 'site-content' },
    { value: 'cta', label: 'Call to Action', contentType: 'site-content', filterKeys: ['partners_cta_title', 'partners_cta_text', 'partners_cta_button'], apiUrlKey: 'site-content' },
    { value: 'all-partners', label: 'All Partners', contentType: 'partners', apiUrlKey: 'partners' },
  ],
  'social-media': [
    { value: 'hero', label: 'Hero Section', contentType: 'site-content', filterKeys: ['social_media_title', 'social_media_subtitle'], apiUrlKey: 'site-content' },
    { value: 'links', label: 'Social Links', contentType: 'site-content', filterKeys: ['social_media_facebook_link', 'social_media_twitter_link', 'social_media_instagram_link', 'social_media_linkedin_link'], apiUrlKey: 'site-content' },
    { value: 'social-posts', label: 'Social Posts', contentType: 'social_media', apiUrlKey: 'social-media' },
  ],
  timeline: [
    { value: 'hero', label: 'Hero Section', contentType: 'site-content', filterKeys: ['timeline_title', 'timeline_subtitle'], apiUrlKey: 'site-content' },
    { value: 'timeline-events', label: 'Timeline Events', contentType: 'timeline', apiUrlKey: 'timeline' },
  ],
  contact: [
    { value: 'hero', label: 'Hero Section', contentType: 'site-content', filterKeys: ['contact_title', 'contact_subtitle'], apiUrlKey: 'site-content' },
    { value: 'hotline', label: 'Hotline', contentType: 'site-content', filterKeys: ['contact_hotline_title', 'contact_hotline_number', 'contact_hotline_subtitle', 'contact_hotline_text'], apiUrlKey: 'site-content' },
    { value: 'email', label: 'Email', contentType: 'site-content', filterKeys: ['contact_email_title', 'contact_email_address', 'contact_email_text'], apiUrlKey: 'site-content' },
    { value: 'whatsapp', label: 'WhatsApp', contentType: 'site-content', filterKeys: ['contact_whatsapp_title', 'contact_whatsapp_number', 'contact_whatsapp_text'], apiUrlKey: 'site-content' },
    { value: 'location', label: 'Location', contentType: 'site-content', filterKeys: ['contact_location_title', 'contact_location_text_1', 'contact_location_text_2'], apiUrlKey: 'site-content' },
    { value: 'follow-us', label: 'Follow Us', contentType: 'site-content', filterKeys: ['contact_follow_us'], apiUrlKey: 'site-content' },
    { value: 'contact-forms', label: 'Contact Forms', contentType: 'contacts', apiUrlKey: 'contacts' },
  ],
  operations: [
    { value: 'hero', label: 'Hero Section', contentType: 'site-content', filterKeys: ['operations_title', 'operations_subtitle', 'operations_image'], apiUrlKey: 'site-content' },
    { value: 'path-to-resolution', label: 'Path to Resolution', contentType: 'site-content', filterKeys: ['operations_path_title', 'operations_path_subtitle'], apiUrlKey: 'site-content' },
    { value: 'step-1', label: 'Step 1: Initial Contact', contentType: 'site-content', filterKeys: ['operations_step_1_title', 'operations_step_1_text', 'operations_step_1_tag'], apiUrlKey: 'site-content' },
    { value: 'step-2', label: 'Step 2: Counselor Support', contentType: 'site-content', filterKeys: ['operations_step_2_title', 'operations_step_2_text', 'operations_step_2_tag'], apiUrlKey: 'site-content' },
    { value: 'step-3', label: 'Step 3: Case Assessment', contentType: 'site-content', filterKeys: ['operations_step_3_title', 'operations_step_3_text', 'operations_step_3_tag'], apiUrlKey: 'site-content' },
    { value: 'step-4', label: 'Step 4: Referral & Follow-up', contentType: 'site-content', filterKeys: ['operations_step_4_title', 'operations_step_4_text', 'operations_step_4_tag'], apiUrlKey: 'site-content' },
    { value: 'metrics', label: 'Metrics', contentType: 'site-content', filterKeys: ['operations_metrics_1_title', 'operations_metrics_1_text', 'operations_metrics_2_title', 'operations_metrics_2_text', 'operations_metrics_3_title', 'operations_metrics_3_text'], apiUrlKey: 'site-content' },
    { value: 'highlights', label: 'Highlights', contentType: 'site-content', filterKeys: ['operations_highlights_title', 'operations_highlight_1_title', 'operations_highlight_1_text', 'operations_highlight_2_title', 'operations_highlight_2_text', 'operations_highlight_3_title', 'operations_highlight_3_text', 'operations_highlight_4_title', 'operations_highlight_4_text', 'operations_highlight_5_title', 'operations_highlight_5_text', 'operations_highlight_6_title', 'operations_highlight_6_text'], apiUrlKey: 'site-content' },
  ],
}

const currentSubTabs = computed(() => {
  return subTabMapping[activeMainTab.value] || []
})

const fetchContentTypesApiMap = async () => {
  try {
    const response = await api.get('/content/')
    contentTypesApiMap.value = response.data
    // Set initial active sub tab based on the first main tab's first sub tab
    if (mainNavTabs.length > 0 && subTabMapping[activeMainTab.value] && subTabMapping[activeMainTab.value].length > 0) {
      activeSubTab.value = subTabMapping[activeMainTab.value][0].value
    }
  } catch (err) {
    console.error('Error fetching content types API map:', err)
    // Handle error
  }
}

const fetchContentForActiveSubTab = async () => {
  const currentSubTabConfig = currentSubTabs.value.find(tab => tab.value === activeSubTab.value)

  if (!currentSubTabConfig || !contentTypesApiMap.value[currentSubTabConfig.apiUrlKey]) {
    currentTabContent.value = []
    return
  }

      setLoading(true)
      setError(null)
      try {
    const url = contentTypesApiMap.value[currentSubTabConfig.apiUrlKey]
    console.log('Fetching from URL:', url)
    const response = await api.get(url)
    console.log('API Response for', currentSubTabConfig.apiUrlKey, ':', response.data)
    let data = Array.isArray(response.data) ? response.data : response.data.results || []

    // If it's 'site-content' and filterKeys are defined, filter the data
    if (currentSubTabConfig.contentType === 'site-content' && currentSubTabConfig.filterKeys) {
      console.log('Filtering site-content with keys:', currentSubTabConfig.filterKeys)
      data = data.filter(item => currentSubTabConfig.filterKeys.includes(item.key))
      console.log('Filtered site-content data:', data)
    }
    currentTabContent.value = data
    console.log('currentTabContent after fetch:', currentTabContent.value)
  } catch (err) {
    console.error(`Error fetching content for ${activeMainTab.value} - ${activeSubTab.value}:`, err)
    setError(`Failed to load content for ${activeMainTab.value} - ${activeSubTab.value}.`)
    currentTabContent.value = []
  } finally {
    setLoading(false)
  }
}

onMounted(async () => {
  await fetchContentTypesApiMap()
  if (activeSubTab.value) {
    await fetchContentForActiveSubTab()
  }
})

watch(activeMainTab, (newMainTab, oldMainTab) => {
  if (newMainTab !== oldMainTab) {
    // When main tab changes, reset active sub tab to the first one of the new main tab
    if (subTabMapping[newMainTab] && subTabMapping[newMainTab].length > 0) {
      activeSubTab.value = subTabMapping[newMainTab][0].value
    } else {
      activeSubTab.value = ''
    }
  }
})

watch(activeSubTab, async (newSubTab, oldSubTab) => {
  if (newSubTab !== oldSubTab && newSubTab) {
    await fetchContentForActiveSubTab()
  }
})

function openEditModal(item) {
  currentContent.value = { ...item }
  showModal.value = true
}

function closeModal() {
  showModal.value = false
  currentContent.value = null
}

async function saveContent() {
  const currentSubTabConfig = currentSubTabs.value.find(tab => tab.value === activeSubTab.value)
  if (!currentSubTabConfig) {
    console.error('Cannot save content: No active sub-tab configuration found.')
    return
  }

  if (currentContent.value && currentSubTabConfig.apiUrlKey && contentTypesApiMap.value[currentSubTabConfig.apiUrlKey]) {
    const baseUrl = contentTypesApiMap.value[currentSubTabConfig.apiUrlKey]
    const url = baseUrl.endsWith('/') ? baseUrl.slice(0, -1) : baseUrl; // Remove trailing slash if present

    setLoading(true)
    setError(null)
    try {
      let updateUrl = '';
      if (currentSubTabConfig.contentType === 'site-content' && currentContent.value.key) {
        updateUrl = `${url}/${currentContent.value.key}/`;
      } else if (currentContent.value.id) {
        updateUrl = `${url}/${currentContent.value.id}/`;
      } else {
        console.error('Cannot save content: Missing identifier (id or key).')
        return
      }
      await updateContent(updateUrl, currentContent.value)
      closeModal()
      await fetchContentForActiveSubTab() // Refresh content after save
    } catch (err) {
      console.error('Error saving content:', err)
      setError('Failed to save content.')
    } finally {
      setLoading(false)
    }
  }
}
</script>