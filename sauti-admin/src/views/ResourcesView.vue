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
            <component :is="getFileIcon(resource.type)" class="h-16 w-16 mx-auto mb-2 opacity-90" />
            <p class="text-sm font-medium uppercase">{{ resource.type }}</p>
          </div>
          <span
            v-if="resource.status === 'draft'"
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
              {{ resource.category }}
            </div>
            <div class="flex items-center">
              <ArrowDownTrayIcon class="h-4 w-4 mr-1" />
              {{ resource.downloads }}
            </div>
          </div>

          <!-- Language Tags -->
          <div class="flex flex-wrap gap-1 mb-4">
            <span
              v-for="lang in resource.languages"
              :key="lang"
              class="px-2 py-1 bg-gray-100 text-gray-700 text-xs rounded"
            >
              {{ lang }}
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
                <select v-model="createForm.category" class="form-select">
                  <option value="Guides & Manuals">Guides & Manuals</option>
                  <option value="Posters & Infographics">Posters & Infographics</option>
                  <option value="Training Materials">Training Materials</option>
                  <option value="Research Reports">Research Reports</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">File Type</label>
                <select v-model="createForm.type" class="form-select">
                  <option value="PDF">PDF</option>
                  <option value="IMAGE">Image</option>
                  <option value="VIDEO">Video</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Languages</label>
                <div class="flex flex-wrap gap-2 mt-2">
                  <label class="flex items-center">
                    <input type="checkbox" v-model="createForm.languages" value="English" class="mr-2">
                    English
                  </label>
                  <label class="flex items-center">
                    <input type="checkbox" v-model="createForm.languages" value="Luganda" class="mr-2">
                    Luganda
                  </label>
                  <label class="flex items-center">
                    <input type="checkbox" v-model="createForm.languages" value="Swahili" class="mr-2">
                    Swahili
                  </label>
                </div>
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
</template>

<script setup>
import { ref, computed } from 'vue'
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

// Mock data
const resources = ref([
  {
    id: 1,
    title: 'Child Protection Guidelines 2024',
    description: 'Comprehensive guidelines for identifying and responding to child abuse cases',
    category: 'Guides & Manuals',
    type: 'PDF',
    status: 'published',
    languages: ['English', 'Luganda'],
    downloads: 1247,
    file_size: '2.5 MB',
    updated_at: '2024-10-15T10:00:00Z'
  },
  {
    id: 2,
    title: 'Signs of Child Abuse Poster',
    description: 'Infographic showing warning signs of different types of child abuse',
    category: 'Posters & Infographics',
    type: 'PDF',
    status: 'published',
    languages: ['English', 'Swahili'],
    downloads: 892,
    file_size: '1.2 MB',
    updated_at: '2024-10-10T14:30:00Z'
  },
  {
    id: 3,
    title: 'Sauti Helpline Training Manual',
    description: 'Training material for new helpline counselors and case workers',
    category: 'Training Materials',
    type: 'PDF',
    status: 'published',
    languages: ['English'],
    downloads: 543,
    file_size: '5.8 MB',
    updated_at: '2024-10-05T09:15:00Z'
  },
  {
    id: 4,
    title: 'Annual Impact Report 2023',
    description: 'Comprehensive report on Sauti\'s activities and impact in 2023',
    category: 'Research Reports',
    type: 'PDF',
    status: 'published',
    languages: ['English'],
    downloads: 326,
    file_size: '8.3 MB',
    updated_at: '2024-09-20T11:00:00Z'
  },
  {
    id: 5,
    title: 'Child Safety Video Series',
    description: 'Educational video series teaching children about personal safety',
    category: 'Training Materials',
    type: 'VIDEO',
    status: 'draft',
    languages: ['English', 'Luganda'],
    downloads: 0,
    file_size: '125 MB',
    updated_at: '2024-10-20T16:45:00Z'
  }
])

const stats = ref({
  total: 45,
  published: 38,
  downloads: 12456,
  thisMonth: 1834
})

const searchQuery = ref('')
const filterCategory = ref('')
const filterStatus = ref('')
const filterLanguage = ref('')
const showCreateModal = ref(false)
const createForm = ref({
  title: '',
  description: '',
  category: 'Guides & Manuals',
  type: 'PDF',
  languages: []
})

const filteredResources = computed(() => {
  return resources.value.filter(resource => {
    const matchesSearch = !searchQuery.value ||
      resource.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      resource.description.toLowerCase().includes(searchQuery.value.toLowerCase())
    
    const matchesCategory = !filterCategory.value || resource.category === filterCategory.value
    const matchesStatus = !filterStatus.value || resource.status === filterStatus.value
    const matchesLanguage = !filterLanguage.value || resource.languages.includes(filterLanguage.value)

    return matchesSearch && matchesCategory && matchesStatus && matchesLanguage
  })
})

const getFileIcon = (type) => {
  const icons = {
    'PDF': DocumentTextIcon,
    'IMAGE': PhotoIcon,
    'VIDEO': FilmIcon
  }
  return icons[type] || DocumentTextIcon
}

const formatDate = (date) => {
  return new Date(date).toLocaleDateString()
}

const viewResource = (resource) => {
  console.log('View resource:', resource)
}

const editResource = (resource) => {
  console.log('Edit resource:', resource)
}

const deleteResource = (resource) => {
  if (confirm(`Delete "${resource.title}"?`)) {
    const index = resources.value.findIndex(r => r.id === resource.id)
    if (index > -1) {
      resources.value.splice(index, 1)
      // Update stats
      stats.value.total--
      if (resource.status === 'published') stats.value.published--
      stats.value.downloads -= resource.downloads
    }
  }
}

const createResource = () => {
  const newResource = {
    id: Date.now(), // Simple ID generation
    title: createForm.value.title,
    description: createForm.value.description,
    category: createForm.value.category,
    type: createForm.value.type,
    status: 'published',
    languages: createForm.value.languages,
    downloads: 0,
    file_size: '1.0 MB',
    updated_at: new Date().toISOString()
  }
  
  resources.value.push(newResource)
  
  // Update stats
  stats.value.total++
  stats.value.published++
  
  // Reset form and close modal
  createForm.value = {
    title: '',
    description: '',
    category: 'Guides & Manuals',
    type: 'PDF',
    languages: []
  }
  showCreateModal.value = false
}
</script>
