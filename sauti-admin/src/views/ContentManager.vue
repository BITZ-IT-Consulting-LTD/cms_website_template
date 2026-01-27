<template>
  <div class="py-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold">Manage Site Content</h1>
      <button @click="openCreateModal" class="btn-primary">
        <PlusIcon class="h-5 w-5 mr-2" />
        Add Content
      </button>
    </div>

    <!-- Main Tabs (Pages) -->
    <div class="mb-8 border-b border-gray-200 overflow-x-auto">
      <nav class="flex space-x-8" aria-label="Main Tabs">
        <button v-for="page in pages" :key="page.value" @click="activePage = page.value" :class="[
          'px-3 py-2 font-medium text-sm rounded-md whitespace-nowrap',
          activePage === page.value ? 'bg-blue-100 text-blue-700' : 'text-gray-500 hover:text-gray-700'
        ]">
          {{ page.label }}
        </button>
      </nav>
    </div>

    <!-- Filters Section -->
    <div class="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
        <!-- Search by Key/Label -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Search</label>
          <input v-model="searchQuery" type="text" placeholder="Search key or label..."
            class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 text-sm" />
        </div>

        <!-- Filter by Type -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Content Type</label>
          <select v-model="filterType" class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 text-sm">
            <option value="">All Types</option>
            <option value="text">Text</option>
            <option value="heading">Heading</option>
            <option value="button">Button</option>
            <option value="photo">Photo</option>
            <option value="video">Video</option>
            <option value="icon">Icon</option>
          </select>
        </div>

        <!-- Filter by Status -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Publication Status</label>
          <select v-model="filterStatus" class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 text-sm">
            <option value="">All Status</option>
            <option value="published">Published</option>
            <option value="unpublished">Unpublished</option>
          </select>
        </div>

        <!-- Clear Filters -->
        <div class="flex items-end">
          <button @click="clearFilters" class="w-full px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50">
            Clear Filters
          </button>
        </div>
      </div>

      <!-- Filter Results Info -->
      <div v-if="searchQuery || filterType || filterStatus !== ''" class="mt-3 text-sm text-gray-600">
        <span class="inline-block px-2 py-1 bg-blue-100 text-blue-800 rounded">
          Showing {{ filteredContent.length }} of {{ allContent.length }} items
        </span>
      </div>
    </div>

    <!-- Loading/Error -->
    <div v-if="contentStore.loading" class="text-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500 mx-auto"></div>
      <p class="mt-4 text-gray-500">Loading content...</p>
    </div>

    <div v-else-if="contentStore.error"
      class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-6">
      <strong class="font-bold">Error! </strong>
      <span class="block sm:inline">{{ contentStore.error }}</span>
    </div>

    <!-- Content Grid -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-if="filteredContent.length === 0"
        class="col-span-full text-center py-12 bg-gray-50 rounded-lg border-2 border-dashed border-gray-200">
        <p class="text-gray-500">No content found for this page.</p>
        <button @click="openCreateModal" class="mt-4 text-blue-600 hover:text-blue-800 font-medium">Create new content
          item</button>
      </div>

      <div v-for="item in filteredContent" :key="item.key"
        class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 flex flex-col hover:shadow-md transition-shadow">
        <div class="flex justify-between items-start mb-4">
          <div class="flex-1">
            <h3 class="font-bold text-gray-900 text-lg">{{ item.label || item.key }}</h3>
            <p class="text-xs text-mono text-gray-500 mt-1">{{ item.key }}</p>
          </div>
          <div class="flex gap-2 items-start">
            <span :class="getTypeBadgeClass(item.type)" class="px-2 py-1 text-xs font-semibold rounded-full capitalize">
              {{ item.type }}
            </span>
            <span v-if="item.is_published" class="px-2 py-1 text-xs font-semibold rounded-full bg-green-100 text-green-800">
              Published
            </span>
            <span v-else class="px-2 py-1 text-xs font-semibold rounded-full bg-gray-100 text-gray-800">
              Draft
            </span>
          </div>
        </div>

        <p v-if="item.description" class="text-sm text-gray-600 mb-4 italic">{{ item.description }}</p>

        <div
          class="bg-gray-50 rounded p-3 text-sm text-gray-800 mb-4 flex-grow overflow-hidden max-h-48 relative group">
          <div v-if="item.type === 'photo'" class="flex justify-center">
            <img :src="item.value" alt="Content Image" class="max-h-32 object-contain"
              @error="$event.target.src = '/placeholder-image.png'" />
          </div>
          <div v-else class="whitespace-pre-wrap">{{ item.value || '(Empty)' }}</div>

          <!-- Gradient overlay for long text -->
          <div class="absolute bottom-0 left-0 right-0 h-8 bg-gradient-to-t from-gray-50 to-transparent"></div>
        </div>

        <div class="mt-auto flex gap-2">
          <button @click="openEditModal(item)"
            class="flex-1 py-2 px-4 bg-gray-50 hover:bg-gray-100 text-gray-700 rounded border border-gray-200 font-medium transition-colors text-sm">
            Edit Content
          </button>
          <button @click="togglePublish(item)"
            :class="[
              'flex-1 py-2 px-4 rounded border font-medium transition-colors text-sm',
              item.is_published
                ? 'bg-green-50 hover:bg-green-100 text-green-700 border-green-200'
                : 'bg-gray-50 hover:bg-gray-100 text-gray-700 border-gray-200'
            ]">
            {{ item.is_published ? 'Unpublish' : 'Publish' }}
          </button>
        </div>
      </div>
    </div>

    <!-- Create/Edit Modal -->
    <div v-if="showModal" class="fixed z-50 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog"
      aria-modal="true">
      <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true" @click="closeModal">
        </div>
        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>

        <div
          class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-2xl sm:w-full">
          <form @submit.prevent="saveContent" class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <div class="flex justify-between items-center mb-5 pb-2 border-b border-gray-100">
              <h3 class="text-lg leading-6 font-bold text-gray-900" id="modal-title">
                {{ isEditing ? 'Edit Content' : 'Create New Content' }}
              </h3>
              <button type="button" @click="closeModal" class="text-gray-400 hover:text-gray-500">
                <span class="sr-only">Close</span>
                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
              <!-- Key (Read-only if editing) -->
              <div class="col-span-1 md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-1">Key (Identifier)</label>
                <input v-if="!isEditing" v-model="form.key" type="text" required
                  class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                  placeholder="e.g. home_hero_title">
                <input v-else :value="form.key" type="text" disabled
                  class="w-full bg-gray-100 border-gray-300 rounded-md shadow-sm text-gray-500 cursor-not-allowed sm:text-sm">
                <p class="mt-1 text-xs text-gray-500">Unique identifier used by the application.</p>
              </div>

              <!-- Label -->
              <div class="col-span-1">
                <label class="block text-sm font-medium text-gray-700 mb-1">Label</label>
                <input v-model="form.label" type="text"
                  class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                  placeholder="Human readable name">
              </div>

              <!-- Page & Type -->
              <div class="col-span-1 grid grid-cols-2 gap-2">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Page</label>
                  <select v-model="form.page"
                    class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                    <option v-for="p in pages" :key="p.value" :value="p.value">{{ p.label }}</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Type</label>
                  <select v-model="form.type"
                    class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                    <option value="text">Text</option>
                    <option value="heading">Heading</option>
                    <option value="photo">Photo URL</option>
                    <option value="button">Button Label</option>
                    <option value="video">Video URL</option>
                    <option value="icon">Icon Name</option>
                  </select>
                </div>
              </div>

              <!-- Description -->
              <div class="col-span-1 md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-1">Description (Internal)</label>
                <input v-model="form.description" type="text"
                  class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                  placeholder="Where does this appear?">
              </div>

              <!-- Value -->
              <div class="col-span-1 md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-1">Content Value</label>
                <div v-if="form.type === 'photo'" class="mb-2">
                  <img v-if="form.value" :src="form.value"
                    class="h-32 object-contain border rounded p-1 bg-gray-50 mb-2" />
                </div>
                <textarea v-model="form.value" rows="6"
                  class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm font-mono"
                  placeholder="Enter content here..."></textarea>
              </div>
            </div>

            <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:-mx-6 sm:-mb-4 flex flex-row-reverse rounded-b-lg">
              <button type="submit" :disabled="contentStore.loading"
                class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm disabled:opacity-50">
                {{ contentStore.loading ? 'Saving...' : 'Save Changes' }}
              </button>
              <button type="button" @click="closeModal"
                class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
                Cancel
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted, computed, reactive, watch } from 'vue'
  import { useContentStore } from '@/store/content'
  import { api } from '@/utils/api'
  import { PlusIcon } from '@heroicons/vue/24/outline'
  import { useToast } from 'vue-toastification'

  const toast = useToast()
  const contentStore = useContentStore()

  // State
  const allContent = ref([])
  const activePage = ref('home')
  const showModal = ref(false)
  const isEditing = ref(false)
  const searchQuery = ref('')
  const filterType = ref('')
  const filterStatus = ref('')

  const form = reactive({
    key: '',
    label: '',
    value: '',
    type: 'text',
    page: 'home',
    description: ''
  })

  // Constants
  const pages = [
    { value: 'home', label: 'Home' },
    { value: 'about', label: 'About' },
    { value: 'operations', label: 'Operations' },
    { value: 'services', label: 'Services' }, // Note: mapped to Service model usually, but site content might exist
    { value: 'resources', label: 'Resources' },
    { value: 'faqs', label: 'FAQs' },
    { value: 'partners', label: 'Partners' },
    { value: 'contact', label: 'Contact' },
    { value: 'footer', label: 'Footer' },
    { value: 'header', label: 'Header' },
    { value: 'reports_insights', label: 'Reports Info' },
    { value: 'videos', label: 'Videos Info' },
    { value: 'global', label: 'Global Settings' },
  ]

  // Computed
  const filteredContent = computed(() => {
    let result = allContent.value.filter(item => item.page === activePage.value || (!item.page && activePage.value === 'home'))

    // Filter by search query (key or label)
    if (searchQuery.value) {
      const query = searchQuery.value.toLowerCase()
      result = result.filter(item =>
        (item.key && item.key.toLowerCase().includes(query)) ||
        (item.label && item.label.toLowerCase().includes(query)) ||
        (item.description && item.description.toLowerCase().includes(query))
      )
    }

    // Filter by content type
    if (filterType.value) {
      result = result.filter(item => item.type === filterType.value)
    }

    // Filter by publication status
    if (filterStatus.value === 'published') {
      result = result.filter(item => item.is_published === true)
    } else if (filterStatus.value === 'unpublished') {
      result = result.filter(item => item.is_published === false)
    }

    return result
  })

  // Methods
  function getTypeBadgeClass(type) {
    const map = {
      text: 'bg-gray-100 text-gray-800',
      heading: 'bg-purple-100 text-purple-800',
      photo: 'bg-green-100 text-green-800',
      button: 'bg-blue-100 text-blue-800',
      video: 'bg-red-100 text-red-800',
      icon: 'bg-yellow-100 text-yellow-800'
    }
    return map[type] || 'bg-gray-100 text-gray-800'
  }

  async function fetchAllContent() {
    contentStore.setLoading(true)
    contentStore.setError(null)
    try {
      const response = await api.get('/content/site-content/')
      if (Array.isArray(response.data)) {
        allContent.value = response.data
      } else {
        console.warn('Unexpected API response format', response.data)
        // Fallback if it returns object map (legacy)
        allContent.value = Object.entries(response.data).map(([key, val]) => {
          // If val is object, use it; else make minimal object
          if (typeof val === 'object' && val !== null) return val
          return { key, value: val, page: 'home', type: 'text', label: key }
        })
      }
    } catch (err) {
      console.error('Fetch error:', err)
      contentStore.setError('Failed to load content.')
    } finally {
      contentStore.setLoading(false)
    }
  }

  function openCreateModal() {
    isEditing.value = false
    // Reset form
    Object.assign(form, {
      key: '',
      label: '',
      value: '',
      type: 'text',
      page: activePage.value,
      description: ''
    })
    showModal.value = true
  }

  function openEditModal(item) {
    isEditing.value = true
    Object.assign(form, {
      key: item.key,
      label: item.label || item.key,
      value: item.value || '',
      type: item.type || 'text',
      page: item.page || activePage.value,
      description: item.description || ''
    })
    showModal.value = true
  }

  function closeModal() {
    showModal.value = false
  }

  function clearFilters() {
    searchQuery.value = ''
    filterType.value = ''
    filterStatus.value = ''
  }

  async function togglePublish(item) {
    contentStore.setLoading(true)
    try {
      const updatedItem = { ...item, is_published: !item.is_published }
      await api.put(`/content/site-content/${item.key}/`, updatedItem)
      toast.success(`Content ${updatedItem.is_published ? 'published' : 'unpublished'} successfully`)
      await fetchAllContent()
    } catch (err) {
      console.error('Toggle publish error:', err)
      const msg = err.response?.data?.detail || err.message || 'Failed to update'
      toast.error(msg)
      contentStore.setError(msg)
    } finally {
      contentStore.setLoading(false)
    }
  }

  async function saveContent() {
    contentStore.setLoading(true)
    try {
      const payload = { ...form }

      if (isEditing.value) {
        // Update
        await api.put(`/content/site-content/${form.key}/`, payload)
        toast.success('Content updated successfully')
      } else {
        // Create
        await api.post('/content/site-content/', payload)
        toast.success('Content created successfully')
      }

      await fetchAllContent()
      closeModal()
    } catch (err) {
      console.error('Save error:', err)
      const msg = err.response?.data?.detail || err.message || 'Failed to save'
      toast.error(msg)
      contentStore.setError(msg)
    } finally {
      contentStore.setLoading(false)
    }
  }

  onMounted(() => {
    fetchAllContent()
  })
</script>
