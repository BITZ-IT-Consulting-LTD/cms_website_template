<template>
  <div class="p-6 space-y-6">
    <!-- Header -->
    <div class="flex justify-between items-start">
      <div>
        <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">Resources</h1>
        <p class="text-gray-600 mt-1">Manage downloadable resources and educational materials</p>
      </div>
      <button
        @click="showCreateModal = true"
        class="btn-primary flex items-center shadow-lg hover:shadow-xl"
      >
        <PlusIcon class="h-5 w-5 mr-2" />
        Add New Resource
      </button>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total Resources</p>
            <p class="text-3xl font-bold text-gray-900 mt-2">{{ stats.total }}</p>
          </div>
          <div class="p-3 bg-teal-100 rounded-lg">
            <FolderOpenIcon class="h-8 w-8 text-teal-600" />
          </div>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Published</p>
            <p class="text-3xl font-bold text-green-600 mt-2">{{ stats.published }}</p>
          </div>
          <div class="p-3 bg-green-100 rounded-lg">
            <CheckCircleIcon class="h-8 w-8 text-green-600" />
          </div>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total Downloads</p>
            <p class="text-3xl font-bold text-blue-600 mt-2">{{ stats.downloads }}</p>
          </div>
          <div class="p-3 bg-blue-100 rounded-lg">
            <ArrowDownTrayIcon class="h-8 w-8 text-blue-600" />
          </div>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">This Month</p>
            <p class="text-3xl font-bold text-purple-600 mt-2">{{ stats.thisMonth }}</p>
          </div>
          <div class="p-3 bg-purple-100 rounded-lg">
            <CalendarIcon class="h-8 w-8 text-purple-600" />
          </div>
        </div>
      </div>
    </div>

    <!-- Filters and Search -->
    <div class="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
      <div class="flex flex-col md:flex-row gap-4">
        <div class="flex-1 relative">
          <MagnifyingGlassIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search resources..."
            class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        </div>
        
        <select
          v-model="filterCategory"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Categories</option>
          <option value="guides">Guides & Manuals</option>
          <option value="posters">Posters & Infographics</option>
          <option value="training">Training Materials</option>
          <option value="research">Research Reports</option>
          <option value="policy">Policy Documents</option>
        </select>

        <select
          v-model="filterStatus"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Status</option>
          <option value="published">Published</option>
          <option value="draft">Draft</option>
        </select>

        <select
          v-model="filterLanguage"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Languages</option>
          <option value="en">English</option>
          <option value="lg">Luganda</option>
          <option value="sw">Swahili</option>
        </select>
      </div>
    </div>

    <!-- Resources Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div
        v-for="resource in filteredResources"
        :key="resource.id"
        class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow duration-200"
      >
        <!-- Resource Preview -->
        <div class="h-48 bg-gradient-to-br from-teal-400 to-blue-500 flex items-center justify-center relative">
          <div class="text-center text-white">
            <component :is="getFileIcon(resource.file_type || 'PDF')" class="h-16 w-16 mx-auto mb-2 opacity-90" />
            <p class="text-sm font-medium uppercase">{{ getFileTypeDisplay(resource.file_type) }}</p>
          </div>
          <span
            v-if="resource.status === 'draft' || resource.status === 'DRAFT'"
            class="absolute top-3 right-3 px-2 py-1 bg-yellow-100 text-yellow-800 text-xs font-semibold rounded-full"
          >
            Draft
          </span>
        </div>

        <!-- Resource Info -->
        <div class="p-5">
          <h3 class="font-semibold text-lg text-gray-900 mb-2 line-clamp-2">
            {{ resource.title }}
          </h3>
          <p class="text-sm text-gray-600 mb-4 line-clamp-2">
            {{ resource.description }}
          </p>

          <!-- Meta Info -->
          <div class="flex items-center justify-between text-xs text-gray-500 mb-4">
            <div class="flex items-center">
              <FolderIcon class="h-4 w-4 mr-1" />
              {{ resource.category?.name || 'Uncategorized' }}
            </div>
            <div class="flex items-center">
              <ArrowDownTrayIcon class="h-4 w-4 mr-1" />
              {{ resource.download_count || 0 }}
            </div>
          </div>

          <!-- Language Tag -->
          <div class="flex flex-wrap gap-1 mb-4">
            <span class="px-2 py-1 bg-gray-100 text-gray-700 text-xs rounded">
              {{ getLanguageName(resource.language) }}
            </span>
          </div>

          <!-- File Info -->
          <div class="flex items-center justify-between text-xs text-gray-500 mb-4 pt-4 border-t border-gray-100">
            <span>{{ resource.file_size }}</span>
            <span>{{ formatDate(resource.updated_at) }}</span>
          </div>

          <!-- Actions -->
          <div class="flex gap-2">
            <button
              @click="viewResource(resource)"
              class="flex-1 btn-outline text-sm"
            >
              <EyeIcon class="h-4 w-4 mr-1" />
              View
            </button>
            <button
              @click="editResource(resource)"
              class="flex-1 btn-primary text-sm"
            >
              <PencilIcon class="h-4 w-4 mr-1" />
              Edit
            </button>
            <button
              @click="deleteResource(resource)"
              class="btn-danger text-sm"
            >
              <TrashIcon class="h-4 w-4" />
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-if="filteredResources.length === 0" class="bg-white rounded-lg shadow-sm border border-gray-200 p-12 text-center">
      <FolderOpenIcon class="mx-auto h-12 w-12 text-gray-400" />
      <h3 class="mt-2 text-sm font-medium text-gray-900">No resources found</h3>
      <p class="mt-1 text-sm text-gray-500">Get started by adding a new resource</p>
      <button
        @click="showCreateModal = true"
        class="mt-4 btn-primary"
      >
        Add New Resource
      </button>
    </div>
  </div>

  <!-- Create Resource Modal -->
  <div v-if="showCreateModal" class="fixed inset-0 z-50 overflow-y-auto">
    <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
      <div class="fixed inset-0 transition-opacity" @click="showCreateModal = false">
        <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
      </div>
      
      <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
        <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
          <h3 class="text-lg font-medium text-gray-900 mb-4" style="font-family: 'Roboto', sans-serif;">Add New Resource</h3>
          <form @submit.prevent="createResource">
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700">Resource Title</label>
                <input v-model="createForm.title" type="text" required class="form-input" placeholder="Enter resource title">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Description</label>
                <textarea v-model="createForm.description" rows="3" class="form-input" placeholder="Enter resource description"></textarea>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Category</label>
                <select v-model="createForm.category" class="form-select" required>
                  <option value="">Select Category</option>
                  <option v-for="category in categories" :key="category.id" :value="category.id">
                    {{ category.name }}
                  </option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Language</label>
                <select v-model="createForm.language" class="form-select">
                  <option value="en">English</option>
                  <option value="lg">Luganda</option>
                  <option value="sw">Swahili</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">File Upload</label>
                <input 
                  type="file" 
                  @change="handleFileUpload"
                  accept=".pdf,.doc,.docx,.jpg,.jpeg,.png,.gif,.mp4,.avi,.mov"
                  class="form-input"
                  required
                >
                <p class="text-xs text-gray-500 mt-1">Supported formats: PDF, DOC, DOCX, JPG, PNG, MP4, AVI, MOV</p>
              </div>
            </div>
            <div class="mt-6 flex justify-end space-x-3">
              <button type="button" @click="showCreateModal = false" class="btn-outline">
                Cancel
              </button>
              <button type="submit" class="btn-primary">
                Create Resource
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>

  <!-- Edit Resource Modal -->
  <div v-if="showEditModal" class="fixed inset-0 z-50 overflow-y-auto">
    <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
      <div class="fixed inset-0 transition-opacity" @click="showEditModal = false">
        <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
      </div>
      
      <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
        <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
          <h3 class="text-lg font-medium text-gray-900 mb-4" style="font-family: 'Roboto', sans-serif;">Edit Resource</h3>
          <form @submit.prevent="updateResource">
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700">Resource Title</label>
                <input v-model="editForm.title" type="text" required class="form-input" placeholder="Enter resource title">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Description</label>
                <textarea v-model="editForm.description" rows="3" class="form-input" placeholder="Enter resource description"></textarea>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Category</label>
                <select v-model="editForm.category" class="form-select" required>
                  <option value="">Select Category</option>
                  <option v-for="category in categories" :key="category.id" :value="category.id">
                    {{ category.name }}
                  </option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Language</label>
                <select v-model="editForm.language" class="form-select">
                  <option value="en">English</option>
                  <option value="lg">Luganda</option>
                  <option value="sw">Swahili</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Update File (Optional)</label>
                <input 
                  type="file" 
                  @change="handleEditFileUpload"
                  accept=".pdf,.doc,.docx,.jpg,.jpeg,.png,.gif,.mp4,.avi,.mov"
                  class="form-input"
                >
                <p class="text-xs text-gray-500 mt-1">Leave empty to keep current file</p>
              </div>
            </div>
            <div class="mt-6 flex justify-end space-x-3">
              <button type="button" @click="showEditModal = false" class="btn-outline">
                Cancel
              </button>
              <button type="submit" class="btn-primary">
                Update Resource
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useResourcesStore } from '@/stores/resources'
import { useToast } from 'vue-toastification'
import {
  PlusIcon,
  MagnifyingGlassIcon,
  FolderOpenIcon,
  CheckCircleIcon,
  ArrowDownTrayIcon,
  CalendarIcon,
  EyeIcon,
  PencilIcon,
  TrashIcon,
  FolderIcon,
  DocumentTextIcon,
  PhotoIcon,
  FilmIcon
} from '@heroicons/vue/24/outline'

const resourcesStore = useResourcesStore()
const toast = useToast()

// Reactive data
const resources = computed(() => resourcesStore.resources)
const categories = computed(() => resourcesStore.categories)
const loading = computed(() => resourcesStore.loading)

const stats = ref({
  total: 0,
  published: 0,
  downloads: 0,
  thisMonth: 0
})

const searchQuery = ref('')
const filterCategory = ref('')
const filterStatus = ref('')
const filterLanguage = ref('')
const showCreateModal = ref(false)
const showEditModal = ref(false)
const editForm = ref({})
const createForm = ref({
  title: '',
  description: '',
  category: '',
  language: 'en',
  file: null
})

const filteredResources = computed(() => {
  return resources.value.filter(resource => {
    const matchesSearch = !searchQuery.value ||
      resource.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      resource.description.toLowerCase().includes(searchQuery.value.toLowerCase())
    
    const matchesCategory = !filterCategory.value || 
      (resource.category && resource.category.name === filterCategory.value)
    const matchesStatus = !filterStatus.value || 
      resource.status?.toLowerCase() === filterStatus.value.toLowerCase()
    const matchesLanguage = !filterLanguage.value || resource.language === filterLanguage.value

    return matchesSearch && matchesCategory && matchesStatus && matchesLanguage
  })
})

const getFileIcon = (type) => {
  const icons = {
    'PDF': DocumentTextIcon,
    'DOC': DocumentTextIcon,
    'DOCX': DocumentTextIcon,
    'IMAGE': PhotoIcon,
    'JPG': PhotoIcon,
    'JPEG': PhotoIcon,
    'PNG': PhotoIcon,
    'GIF': PhotoIcon,
    'VIDEO': FilmIcon,
    'MP4': FilmIcon,
    'AVI': FilmIcon,
    'MOV': FilmIcon
  }
  return icons[type] || DocumentTextIcon
}

const getFileTypeDisplay = (type) => {
  if (!type) return 'Document'
  return type.toUpperCase()
}

const getLanguageName = (code) => {
  const languages = {
    'en': 'English',
    'lg': 'Luganda',
    'sw': 'Swahili'
  }
  return languages[code] || 'English'
}

const formatDate = (date) => {
  if (!date) return 'Recently'
  try {
    return new Date(date).toLocaleDateString()
  } catch (error) {
    console.error('Date formatting error:', error, date)
    return 'Recently'
  }
}

const viewResource = (resource) => {
  console.log('View resource:', resource)
}

const editResource = (resource) => {
  editForm.value = {
    id: resource.id,
    slug: resource.slug,
    title: resource.title,
    description: resource.description,
    category: resource.category?.id || '',
    language: resource.language,
    file: null
  }
  showEditModal.value = true
}

const deleteResource = async (resource) => {
  if (confirm(`Delete "${resource.title}"?`)) {
    try {
      await resourcesStore.deleteResource(resource.slug)
      toast.success('Resource deleted successfully')
      await fetchResources()
    } catch (error) {
      console.error('Delete error:', error)
      toast.error('Failed to delete resource')
    }
  }
}

const createResource = async () => {
  try {
    await resourcesStore.createResource(createForm.value)
    toast.success('Resource created successfully')
    showCreateModal.value = false
    resetCreateForm()
    await fetchResources()
  } catch (error) {
    console.error('Create error:', error)
    toast.error('Failed to create resource')
  }
}

const updateResource = async () => {
  try {
    await resourcesStore.updateResource(editForm.value.slug, editForm.value)
    toast.success('Resource updated successfully')
    showEditModal.value = false
    await fetchResources()
  } catch (error) {
    console.error('Update error:', error)
    toast.error('Failed to update resource')
  }
}

const resetCreateForm = () => {
  createForm.value = {
    title: '',
    description: '',
    category: '',
    language: 'en',
    file: null
  }
}

const handleFileUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    createForm.value.file = file
  }
}

const handleEditFileUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    editForm.value.file = file
  }
}

const fetchResources = async () => {
  try {
    await resourcesStore.fetchResources()
    await resourcesStore.fetchCategories()
    console.log('Resources loaded:', resources.value)
    console.log('Categories loaded:', categories.value)
    updateStats()
  } catch (error) {
    console.error('Failed to fetch resources:', error)
    toast.error('Failed to load resources')
  }
}

const updateStats = () => {
  const total = resources.value.length
  const published = resources.value.filter(r => r.status === 'PUBLISHED' || r.status === 'published').length
  const downloads = resources.value.reduce((sum, r) => sum + (r.download_count || 0), 0)
  
  stats.value = {
    total,
    published,
    downloads,
    thisMonth: Math.floor(downloads * 0.3) // Mock calculation
  }
}

onMounted(() => {
  fetchResources()
})
</script>
