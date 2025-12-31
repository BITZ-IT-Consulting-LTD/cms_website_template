<template>
  <div class="py-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold">Manage Site Content</h1>
      <button @click="openCreateModal" class="btn-primary">
        <PlusIcon class="h-5 w-5 mr-2" />
        Create Content
      </button>
    </div>

    <div class="mb-8 border-b border-gray-200">
      <nav class="flex space-x-8" aria-label="Main Tabs">
        <button v-for="mainTab in mainNavTabs" :key="mainTab.value" @click="activeMainTab = mainTab.value" :class="[
          'px-3 py-2 font-medium text-sm rounded-md',
          activeMainTab === mainTab.value ? 'bg-blue-100 text-blue-700' : 'text-gray-500 hover:text-gray-700'
        ]">
          {{ mainTab.label }}
        </button>
      </nav>
    </div>

    <div v-if="currentSubTabs.length > 0" class="mb-8 border-b border-gray-200">
      <nav class="flex space-x-4" aria-label="Sub Tabs">
        <button v-for="subTab in currentSubTabs" :key="subTab.value" @click="activeSubTab = subTab.value" :class="[
          'px-3 py-2 font-medium text-xs rounded-md',
          activeSubTab === subTab.value ? 'bg-gray-200 text-gray-800' : 'text-gray-500 hover:text-gray-700'
        ]">
          {{ subTab.label }}
        </button>
      </nav>
    </div>

    <div v-if="contentStore.loading" class="text-center">
      <p>Loading content...</p>
    </div>

    <div v-if="contentStore.error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
      <strong class="font-bold">Error!</strong>
      <span class="block sm:inline">{{ contentStore.error }}</span>
    </div>

    <div v-if="!contentStore.loading && currentTabContent.length === 0"
      class="col-span-full text-center py-12 bg-gray-50 rounded-lg border-2 border-dashed border-gray-200">
      <p class="text-gray-500">No content items found for this section.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="(item, index) in currentTabContent" :key="item.id || item.key || index"
        class="bg-white rounded-lg shadow-md p-6 flex flex-col justify-between">
        <div>
          <h2 class="text-xl font-semibold mb-2">
            {{ formatKey(item.key) || item.name || item.title || item.label || 'N/A' }}
          </h2>
          <p v-if="item.description" class="text-gray-600 mb-4">{{ item.description }}</p>
          <div class="bg-gray-100 rounded-md p-4 text-gray-800">
            <p class="truncate">{{ item.value || 'N/A' }}</p>
          </div>
        </div>
        <button @click="openEditModal(item)"
          class="mt-6 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
          Edit
        </button>
      </div>
    </div>

    <div v-if="showCreateModal" class="fixed z-10 inset-0 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 transition-opacity" aria-hidden="true">
          <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
        </div>
        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
        <div
          class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <h3 class="text-lg leading-6 font-medium text-gray-900 mb-4">
              Create New Content
            </h3>
            <div class="mt-2">
              <div class="mb-4">
                <label for="new-content-key" class="block text-sm font-medium text-gray-700">Content Key</label>
                <input type="text" id="new-content-key" v-model="newContent.key"
                  class="w-full border border-gray-300 rounded-md p-2" placeholder="e.g., home_page_title">
              </div>
              <div>
                <label for="new-content-value" class="block text-sm font-medium text-gray-700">Content Value</label>
                <textarea id="new-content-value" v-model="newContent.value" rows="10"
                  class="w-full border border-gray-300 rounded-md p-2"></textarea>
              </div>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
            <button @click="createContent" type="button"
              class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm">
              Create
            </button>
            <button @click="closeCreateModal" type="button"
              class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Edit Modal -->
    <div v-if="showModal" class="fixed z-10 inset-0 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 transition-opacity" aria-hidden="true">
          <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
        </div>

        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>

        <div
          class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <h3 class="text-lg leading-6 font-medium text-gray-900 mb-4">
              Edit Content: {{ formatKey(currentContent.key) || currentContent.name || currentContent.label || 'N/A' }}
            </h3>
            <div class="mt-2">
              <textarea v-model="currentContent.value" rows="10"
                class="w-full border border-gray-300 rounded-md p-2"></textarea>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
            <button @click="saveContent" type="button"
              class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm">
              Save
            </button>
            <button @click="closeModal" type="button"
              class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
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
  import { PlusIcon } from '@heroicons/vue/24/outline'
  import { useToast } from 'vue-toastification'
  import { useContentStore } from '@/store/content'
  import { api } from '@/utils/api' // Assuming api is available for direct calls

  const toast = useToast()
  const contentStore = useContentStore()

  const showModal = ref(false)
  const showCreateModal = ref(false)
  const currentContent = ref(null)
  const newContent = ref({ key: '', value: '' })
  const activeMainTab = ref('home') // Default active main tab
  const activeSubTab = ref('') // Default active sub tab
  const globalSettings = ref({}) // Will hold the single GlobalSettings object
  const currentTabContent = ref([]) // Stores content for the active sub tab

  // Define Main Navigation Tabs
  const mainNavTabs = [
    { value: 'home', label: 'Home' },
    { value: 'about', label: 'About' },
    { value: 'resources', label: 'Resources' },
    { value: 'faqs', label: 'FAQs' },
    { value: 'partners', label: 'Partners' },
  ]

  // Define Sub-Tab Mapping for each Main Tab
  const subTabMapping = {
    home: [
      { value: 'hero-section', label: 'Hero Section', filterKeys: ['hero_title', 'hero_subtitle', 'hero_cta_call', 'hero_cta_report'] },
      { value: 'quick-access', label: 'Quick Access', filterKeys: ['quick_access_title', 'quick_access_description'] },
      { value: 'cards', label: 'Cards', filterKeys: ['card_report_title', 'card_report_text', 'card_services_title', 'card_services_text', 'card_faqs_title', 'card_faqs_text', 'card_partners_title', 'card_partners_text'] },
      { value: 'publications', label: 'Publications', filterKeys: ['publications_title', 'publications_description', 'publications_link'] },
      { value: 'trust-partners', label: 'Trust Partners', filterKeys: ['trust_partners_title', 'trust_partners_description'] },
      { value: 'final-cta', label: 'Final CTA', filterKeys: ['final_cta_title', 'final_cta_text', 'final_cta_call', 'final_cta_report', 'final_cta_contact'] },
    ],
    about: [
      { value: 'hero', label: 'Hero Section', filterKeys: ['about_hero_title', 'about_hero_description', 'about_hero_image', 'about_hero_cta_call', 'about_hero_cta_report', 'about_hero_badge1_text', 'about_hero_badge1_class', 'about_hero_badge2_text', 'about_hero_badge2_class', 'about_hero_badge3_text', 'about_hero_badge3_class'] },
      { value: 'identity', label: 'Identity (Stats)', filterKeys: ['about_identity_stat1_title', 'about_identity_stat1_text', 'about_identity_stat1_icon', 'about_identity_stat1_color_from', 'about_identity_stat1_color_to', 'about_identity_stat2_title', 'about_identity_stat2_text', 'about_identity_stat2_icon', 'about_identity_stat2_color_from', 'about_identity_stat2_color_to', 'about_identity_stat3_title', 'about_identity_stat3_text', 'about_identity_stat3_icon', 'about_identity_stat3_color_from', 'about_identity_stat3_color_to', 'about_identity_stat4_title', 'about_identity_stat4_text', 'about_identity_stat4_icon', 'about_identity_stat4_color_from', 'about_identity_stat4_color_to'] },
      { value: 'services', label: 'Services', filterKeys: ['about_services_title', 'about_services_description', 'about_services_item1_title', 'about_services_item1_text', 'about_services_item1_icon', 'about_services_item1_color', 'about_services_item2_title', 'about_services_item2_text', 'about_services_item2_icon', 'about_services_item2_color', 'about_services_item3_title', 'about_services_item3_text', 'about_services_item3_icon', 'about_services_item3_color', 'about_services_item4_title', 'about_services_item4_text', 'about_services_item4_icon', 'about_services_item4_color', 'about_services_item5_title', 'about_services_item5_text', 'about_services_item5_icon', 'about_services_item5_color'] },
      { value: 'core-values', label: 'Core Values', filterKeys: ['about_values_title'] },
      { value: 'trust-signals', label: 'Trust Signals', filterKeys: ['about_trust_signals_title', 'about_trust_signals_description', 'about_trust_signals_partner1', 'about_trust_signals_partner2', 'about_trust_signals_partner3', 'about_trust_signals_partner4'] },
      { value: 'call-to-action', label: 'Call to Action', filterKeys: ['about_call_to_action_title', 'about_call_to_action_text', 'about_call_to_action_cta_call', 'about_call_to_action_cta_report', 'about_call_to_action_cta_contact'] },
    ],
    resources: [
      { value: 'hero', label: 'Hero Section', filterKeys: ['resources_title', 'resources_subtitle'] },
      { value: 'stats', label: 'Statistics', filterKeys: ['resources_stats_title', 'resources_stats_updated', 'resources_stats_loading', 'resources_stats_error', 'resources_total_reports', 'resources_child_protection', 'resources_gbv_cases', 'resources_migrant_worker', 'resources_cases_by_category', 'resources_interactive', 'resources_reports_over_time', 'resources_last_6_months', 'resources_status_distribution', 'resources_pending', 'resources_in_progress', 'resources_resolved', 'resources_closed'] },
      { value: 'downloads', label: 'Downloads', filterKeys: ['resources_downloads_title', 'resources_downloads_subtitle', 'resources_available', 'resources_search_placeholder', 'resources_all_categories', 'resources_all_languages', 'resources_loading', 'resources_coming_soon', 'resources_no_results', 'resources_no_results_subtitle', 'resources_previous', 'resources_next'] },
    ],
    faqs: [
      { value: 'support', label: 'Support', filterKeys: ['faqs_support_title', 'faqs_support_subtitle'] },
      { value: 'quick-response', label: 'Quick Response', filterKeys: ['faqs_quick_response_title', 'faqs_quick_response_subtitle', 'faqs_quick_response_text'] },
      { value: 'immediate-help', label: 'Immediate Help', filterKeys: ['faqs_immediate_help_title', 'faqs_immediate_help_subtitle', 'faqs_call_button'] },
      { value: 'page-content', label: 'Page Content', filterKeys: ['faqs_page_title', 'faqs_page_subtitle', 'faqs_search_placeholder', 'faqs_all_categories_button', 'faqs_no_results', 'faqs_no_results_subtitle'] },
      { value: 'footer', label: 'Footer', filterKeys: ['faqs_privacy_policy', 'faqs_terms_of_service', 'faqs_contact_us', 'faqs_footer_text'] },
    ],
    partners: [
      { value: 'hero', label: 'Hero Section', filterKeys: ['partners_title', 'partners_subtitle'] },
      { value: 'cta', label: 'Call to Action', filterKeys: ['partners_cta_title', 'partners_cta_text', 'partners_cta_button'] },
    ],
    'social-media': [],
    timeline: [],
    contact: [],
    operations: [],
  }

  const currentSubTabs = computed(() => {
    return subTabMapping[activeMainTab.value] || []
  })

  function formatKey(key) {
    if (!key) return ''
    return key.replace(/_/g, ' ').split(' ').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join(' ')
  }

  const fetchGlobalSettings = async () => {
    contentStore.setLoading(true)
    contentStore.setError(null)
    try {
      const response = await api.get('/content/site-content/')
      // Ensure response.data is an array before reducing
      if (Array.isArray(response.data)) {
        globalSettings.value = response.data.reduce((obj, item) => {
          if (item && item.key) {
            obj[item.key] = item.value
          }
          return obj
        }, {})
      } else if (response.data && typeof response.data === 'object') {
        // If it's already an object, just use it
        globalSettings.value = response.data
      } else {
        console.warn('Unexpected data format from /content/site-content/:', response.data)
        globalSettings.value = {}
      }
      // Set initial active sub tab based on the first main tab's first sub tab
      if (mainNavTabs.length > 0 && subTabMapping[activeMainTab.value] && subTabMapping[activeMainTab.value].length > 0) {
        activeSubTab.value = subTabMapping[activeMainTab.value][0].value
      }
    } catch (err) {
      console.error('Error fetching global settings:', err)
      contentStore.setError('Failed to fetch global settings.')
    } finally {
      contentStore.setLoading(false)
    }
  }

  const fetchContentForActiveSubTab = async () => {
    const currentSubTabConfig = currentSubTabs.value.find(tab => tab.value === activeSubTab.value)

    if (!currentSubTabConfig || !globalSettings.value) {
      currentTabContent.value = []
      return
    }

    contentStore.setLoading(true)
    contentStore.setError(null)
    try {
      let data = []
      if (currentSubTabConfig.filterKeys) {
        data = currentSubTabConfig.filterKeys.map(key => ({
          key: key,
          value: globalSettings.value[key] || '',
          id: key // Use key as id for consistency in the UI
        }))
      }
      currentTabContent.value = data
    } catch (err) {
      console.error(`Error processing content for ${activeMainTab.value} - ${activeSubTab.value}:`, err)
      contentStore.setError(`Failed to load content for ${activeMainTab.value} - ${activeSubTab.value}.`)
      currentTabContent.value = []
    } finally {
      contentStore.setLoading(false)
    }
  }

  onMounted(async () => {
    await fetchGlobalSettings()
  })

  watch(activeMainTab, (newMainTab, oldMainTab) => {
    if (newMainTab !== oldMainTab) {
      // When main tab changes, reset active sub tab to the first one of the new main tab
      if (subTabMapping[newMainTab] && subTabMapping[newMainTab].length > 0) {
        activeSubTab.value = newMainTab === 'faqs' ? 'support' : subTabMapping[newMainTab][0].value
      } else {
        activeSubTab.value = ''
      }
    }
  })

  watch([activeSubTab, globalSettings], async ([newSubTab, newGlobalSettings]) => {
    if (newSubTab && newGlobalSettings) {
      await fetchContentForActiveSubTab()
    }
  }, { deep: true })

  function openEditModal(item) {
    console.log('Editing item:', item)
    currentContent.value = { ...item }
    showModal.value = true
  }

  function closeModal() {
    showModal.value = false
    currentContent.value = null
  }

  function openCreateModal() {
    console.log('Opening create modal')
    newContent.value = { key: '', value: '' }
    showCreateModal.value = true
  }

  function closeCreateModal() {
    showCreateModal.value = false
  }

  async function createContent() {
    if (!newContent.value.key) {
      alert('Content key cannot be empty.')
      return
    }

    contentStore.setLoading(true)
    contentStore.setError(null)
    try {
      console.log('Creating content:', newContent.value)
      await api.post('/content/site-content/', newContent.value)
      closeCreateModal()
      await fetchGlobalSettings() // Refetch all settings
      await fetchContentForActiveSubTab() // Refresh content after create
    } catch (err) {
      console.error('Error creating content:', err)
      contentStore.setError('Failed to create content.')
    } finally {
      contentStore.setLoading(false)
    }
  }

  async function saveContent() {
    if (!currentContent.value) {
      console.error('Cannot save content: No current content selected.')
      return
    }

    contentStore.setLoading(true)
    contentStore.setError(null)
    try {
      console.log('Saving content:', currentContent.value)

      // Prepare minimal payload expected by backend (key & value only)
      const payload = {
        key: currentContent.value.key,
        value: currentContent.value.value,
      }

      // Try to update existing content
      try {
        // Try with trailing slash first (Django default)
        await api.put(`/content/site-content/${currentContent.value.key}/`, payload)
      } catch (putErr) {
        // Fallback for different URL structures
        if (putErr.response && putErr.response.status === 404) {
          // Try without trailing slash
          try {
            await api.put(`/content/site-content/${currentContent.value.key}`, payload)
          } catch (putErr2) {
            if (putErr2.response && putErr2.response.status === 404) {
              console.log('Content not found, creating new:', currentContent.value.key)
              await api.post('/content/site-content/', payload)
            } else {
              throw putErr2
            }
          }
        } else {
          throw putErr
        }
      }

      closeModal()
      await fetchGlobalSettings()
      await fetchContentForActiveSubTab()
    } catch (err) {
      console.error('Error saving content:', err)
      const errorDetail = err.response?.data?.detail || err.response?.data?.non_field_errors || err.message
      contentStore.setError(`Failed to save content: ${errorDetail}`)
      toast.error(`Save failed: ${errorDetail}`)
    } finally {
      contentStore.setLoading(false)
    }
  }
</script>
