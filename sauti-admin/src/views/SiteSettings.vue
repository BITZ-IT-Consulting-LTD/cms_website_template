<template>
  <div class="p-8">
    <h1 class="text-3xl font-bold mb-8">Manage Site Settings</h1>

    <div class="mb-8 border-b border-gray-200">
      <nav class="flex space-x-8" aria-label="Tabs">
        <button
          v-for="page in pages"
          :key="page.value"
          @click="activePage = page.value"
          :class="[
            'px-3 py-2 font-medium text-sm rounded-md',
            activePage === page.value ? 'bg-blue-100 text-blue-700' : 'text-gray-500 hover:text-gray-700'
          ]"
        >
          {{ page.label }}
        </button>
      </nav>
    </div>

    <div v-if="loading" class="text-center">
      <p>Loading settings...</p>
    </div>

    <div v-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
      <strong class="font-bold">Error!</strong>
      <span class="block sm:inline">{{ error }}</span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="setting in filteredSettings" :key="setting.key" class="bg-white rounded-lg shadow-md p-6 flex flex-col justify-between">
        <div>
          <h2 class="text-xl font-semibold mb-2">{{ setting.key.replace(/_/g, ' ').split(' ').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join(' ') }}</h2>
          <p class="text-gray-600 mb-4">{{ setting.description }}</p>
          <div class="bg-gray-100 rounded-md p-4 text-gray-800">
            <p class="truncate">{{ setting.value }}</p>
          </div>
        </div>
        <button @click="openEditModal(setting)" class="mt-6 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
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
            <h3 class="text-lg leading-6 font-medium text-gray-900 mb-4">Edit Setting: {{ currentSetting.key.replace(/_/g, ' ').split(' ').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join(' ') }}</h3>
            <div class="mt-2">
              <textarea v-model="currentSetting.value" rows="10" class="w-full border border-gray-300 rounded-md p-2"></textarea>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
            <button @click="saveSetting" type="button" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm">
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
import { ref, onMounted, computed } from 'vue'
import { api } from '@/utils/api' // Assuming api is available for direct calls

const loading = ref(false)
const error = ref(null)
const showModal = ref(false)
const currentSetting = ref(null)
const activePage = ref('home') // Default active page
const allSettings = ref([]) // Stores all settings fetched from the API

const pages = [
  { value: 'home', label: 'Home Page' },
  { value: 'about', label: 'About Page' },
  { value: 'contact', label: 'Contact Page' },
  // Add more pages as needed, matching the backend PAGE_CHOICES
]

const filteredSettings = computed(() => {
  return allSettings.value.filter(setting => setting.page === activePage.value)
})

const fetchSettings = async () => {
  loading.value = true
  error.value = null
  try {
    const response = await api.get('/sitesettings/') // Fetch all settings
    allSettings.value = response.data
  } catch (err) {
    console.error('Error fetching site settings:', err)
    error.value = 'Failed to load site settings.'
  } finally {
    loading.value = false
  }
}

onMounted(async () => {
  await fetchSettings()
})

function openEditModal(setting) {
  currentSetting.value = { ...setting } // Create a copy to avoid direct mutation
  showModal.value = true
}

function closeModal() {
  showModal.value = false
  currentSetting.value = null
}

async function saveSetting() {
  if (currentSetting.value && currentSetting.value.id) {
    loading.value = true
    error.value = null
    try {
      await api.put(`/sitesettings/${currentSetting.value.id}/`, currentSetting.value)
      closeModal()
      await fetchSettings() // Refresh settings after save
    } catch (err) {
      console.error('Error saving setting:', err)
      error.value = 'Failed to save setting.'
    } finally {
      loading.value = false
    }
  }
}
</script>
