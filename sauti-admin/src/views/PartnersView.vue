<template>
  <div class="p-6 space-y-6">
    <!-- Header -->
    <div class="flex justify-between items-start">
      <div>
        <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">Partners</h1>
        <p class="text-gray-600 mt-1">Manage partner organizations and collaborations</p>
      </div>
      <button
        @click="showCreateModal = true"
        class="btn-primary flex items-center"
      >
        <PlusIcon class="h-5 w-5 mr-2" />
        Add New Partner
      </button>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
      <div class="stats-card">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total Partners</p>
            <p class="text-3xl font-bold text-gray-900 mt-2">{{ stats.total }}</p>
          </div>
          <div class="p-3 bg-blue-100 rounded-lg">
            <UserGroupIcon class="h-8 w-8 text-blue-600" />
          </div>
        </div>
      </div>

      <div class="stats-card">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Active</p>
            <p class="text-3xl font-bold text-green-600 mt-2">{{ stats.active }}</p>
          </div>
          <div class="p-3 bg-green-100 rounded-lg">
            <CheckCircleIcon class="h-8 w-8 text-green-600" />
          </div>
        </div>
      </div>

      <div class="stats-card">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">NGO Partners</p>
            <p class="text-3xl font-bold text-purple-600 mt-2">{{ stats.ngo }}</p>
          </div>
          <div class="p-3 bg-purple-100 rounded-lg">
            <BuildingOfficeIcon class="h-8 w-8 text-purple-600" />
          </div>
        </div>
      </div>

      <div class="stats-card">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Government</p>
            <p class="text-3xl font-bold text-orange-600 mt-2">{{ stats.government }}</p>
          </div>
          <div class="p-3 bg-orange-100 rounded-lg">
            <BuildingLibraryIcon class="h-8 w-8 text-orange-600" />
          </div>
        </div>
      </div>
    </div>

    <!-- Search and Filters -->
    <div class="bg-white rounded-lg shadow-sm p-6">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <!-- Search -->
        <div class="relative">
          <MagnifyingGlassIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search partners..."
            class="form-input pl-10"
          />
        </div>
        
        <!-- Type Filter -->
        <select v-model="filterType" class="form-select">
          <option value="">All Types</option>
          <option value="NGO">NGO</option>
          <option value="Government Agency">Government Agency</option>
          <option value="International Organization">International Organization</option>
          <option value="Private Sector">Private Sector</option>
        </select>
        
        <!-- Status Filter -->
        <select v-model="filterStatus" class="form-select">
          <option value="">All Status</option>
          <option value="active">Active</option>
          <option value="pending">Pending</option>
          <option value="inactive">Inactive</option>
        </select>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="text-center py-12">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
      <p class="mt-2 text-sm text-gray-500">Loading partners...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="text-center py-12">
      <div class="text-red-600 mb-4">
        <UserGroupIcon class="h-12 w-12 mx-auto mb-2" />
        <h3 class="text-lg font-medium">Failed to load partners</h3>
        <p class="text-sm text-gray-500">{{ error }}</p>
      </div>
      <button @click="fetchPartners" class="btn-primary">
        Try Again
      </button>
    </div>

    <!-- Partners Grid -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="partner in filteredPartners" :key="partner.id" class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow">
        <div class="flex items-start justify-between mb-4">
          <div class="flex items-center space-x-3">
            <div class="h-12 w-12 bg-gray-100 rounded-lg flex items-center justify-center">
              <UserGroupIcon class="h-6 w-6 text-gray-400" />
            </div>
            <div>
              <h3 class="text-lg font-semibold text-gray-900 line-clamp-2">{{ partner.name }}</h3>
              <span
                class="inline-flex px-2 py-1 text-xs font-semibold rounded-full mt-1"
                :class="statusBadgeClass(partner.status)"
              >
                {{ partner.status }}
              </span>
            </div>
          </div>
          
          <div class="flex items-center space-x-2">
            <button
              @click="viewPartner(partner)"
              class="text-blue-600 hover:text-blue-900 p-2"
              title="View"
            >
              <EyeIcon class="h-4 w-4" />
            </button>
            <button
              @click="editPartner(partner)"
              class="text-primary-600 hover:text-primary-900 p-2"
              title="Edit"
            >
              <PencilIcon class="h-4 w-4" />
            </button>
            <button
              @click="deletePartner(partner)"
              class="text-red-600 hover:text-red-900 p-2"
              title="Delete"
            >
              <TrashIcon class="h-4 w-4" />
            </button>
          </div>
        </div>
        
        <p class="text-gray-600 text-sm mb-4 line-clamp-3">{{ partner.description }}</p>
        
        <div class="space-y-2 text-sm text-gray-500">
          <div class="flex items-center">
            <span class="font-medium text-gray-700 mr-2">Type:</span>
            <span>{{ partner.type }}</span>
          </div>
          
          <div v-if="partner.website" class="flex items-center">
            <GlobeAltIcon class="h-4 w-4 mr-2" />
            <a :href="partner.website" target="_blank" class="text-blue-600 hover:text-blue-800 truncate">
              {{ partner.website }}
            </a>
          </div>
          
          <div v-if="partner.email" class="flex items-center">
            <EnvelopeIcon class="h-4 w-4 mr-2" />
            <span class="truncate">{{ partner.email }}</span>
          </div>
          
          <div v-if="partner.phone" class="flex items-center">
            <PhoneIcon class="h-4 w-4 mr-2" />
            <span>{{ partner.phone }}</span>
          </div>
        </div>
      </div>
      
      <!-- Empty State -->
      <div v-if="filteredPartners.length === 0" class="col-span-full text-center py-12 bg-white rounded-lg shadow-sm border border-gray-200">
        <UserGroupIcon class="mx-auto h-16 w-16 text-gray-400 mb-4" />
        <h3 class="text-lg font-medium text-gray-900 mb-2">No partners found</h3>
        <p class="text-gray-600 mb-4 max-w-md mx-auto">
          {{ searchQuery || filterType || filterStatus ? 'Try adjusting your search criteria.' : 'Start building your network by adding partner organizations.' }}
        </p>
        <p v-if="!searchQuery && !filterType && !filterStatus" class="text-sm text-gray-500 mb-6">
          Add NGOs, government agencies, and other organizations you collaborate with.
        </p>
        <div v-if="!searchQuery && !filterType && !filterStatus">
          <button @click="showCreateModal = true" class="btn-primary inline-flex items-center">
            <PlusIcon class="h-5 w-5 mr-2" />
            Add Your First Partner
          </button>
        </div>
      </div>
    </div>

    <!-- Create Partner Modal -->
    <div v-if="showCreateModal" class="fixed inset-0 z-50 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 transition-opacity" @click="showCreateModal = false">
          <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
        </div>
        
        <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <h3 class="text-lg font-medium text-gray-900 mb-4" style="font-family: 'Roboto', sans-serif;">Add New Partner</h3>
            <form @submit.prevent="createPartner">
              <div class="space-y-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700">Partner Name</label>
                  <input v-model="createForm.name" type="text" required class="form-input">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Description</label>
                  <textarea v-model="createForm.description" rows="3" class="form-input"></textarea>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Type</label>
                  <select v-model="createForm.type" class="form-select">
                    <option value="NGO">NGO</option>
                    <option value="Government Agency">Government Agency</option>
                    <option value="International Organization">International Organization</option>
                    <option value="Private Sector">Private Sector</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Website</label>
                  <input v-model="createForm.website" type="url" class="form-input">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Email</label>
                  <input v-model="createForm.email" type="email" class="form-input">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Phone</label>
                  <input v-model="createForm.phone" type="tel" class="form-input">
                </div>
              </div>
              <div class="mt-6 flex justify-end space-x-3">
                <button type="button" @click="showCreateModal = false" class="btn-outline">
                  Cancel
                </button>
                <button type="submit" :disabled="loading" class="btn-primary">
                  {{ loading ? 'Creating...' : 'Create Partner' }}
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>

    <!-- Edit Partner Modal -->
    <div v-if="showEditModal" class="fixed inset-0 z-50 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 transition-opacity" @click="showEditModal = false">
          <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
        </div>
        
        <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <h3 class="text-lg font-medium text-gray-900 mb-4" style="font-family: 'Roboto', sans-serif;">Edit Partner</h3>
            <form @submit.prevent="updatePartner">
              <div class="space-y-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700">Partner Name</label>
                  <input v-model="editForm.name" type="text" required class="form-input">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Description</label>
                  <textarea v-model="editForm.description" rows="3" class="form-input"></textarea>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Type</label>
                  <select v-model="editForm.type" class="form-select">
                    <option value="NGO">NGO</option>
                    <option value="Government Agency">Government Agency</option>
                    <option value="International Organization">International Organization</option>
                    <option value="Private Sector">Private Sector</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Website</label>
                  <input v-model="editForm.website" type="url" class="form-input">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Email</label>
                  <input v-model="editForm.email" type="email" class="form-input">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Phone</label>
                  <input v-model="editForm.phone" type="tel" class="form-input">
                </div>
              </div>
              <div class="mt-6 flex justify-end space-x-3">
                <button type="button" @click="showEditModal = false" class="btn-outline">
                  Cancel
                </button>
                <button type="submit" :disabled="loading" class="btn-primary">
                  {{ loading ? 'Updating...' : 'Update Partner' }}
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useToast } from 'vue-toastification'
import { usePartnersStore } from '@/stores/partners'
import {
  PlusIcon,
  MagnifyingGlassIcon,
  UserGroupIcon,
  CheckCircleIcon,
  BuildingOfficeIcon,
  BuildingLibraryIcon,
  EyeIcon,
  PencilIcon,
  TrashIcon,
  GlobeAltIcon,
  EnvelopeIcon,
  PhoneIcon
} from '@heroicons/vue/24/outline'

const toast = useToast()
const partnersStore = usePartnersStore()

// Reactive data
const searchQuery = ref('')
const filterType = ref('')
const filterStatus = ref('')
const showCreateModal = ref(false)
const showEditModal = ref(false)
const editForm = ref({})
const createForm = ref({
  name: '',
  description: '',
  type: 'NGO',
  website: '',
  email: '',
  phone: ''
})

// Use store data
const partners = computed(() => partnersStore.partners)
const loading = computed(() => partnersStore.loading)
const error = computed(() => partnersStore.error)

// Computed properties
const stats = computed(() => {
  const partnersList = Array.isArray(partners.value) ? partners.value : []
  const total = partnersList.length
  const active = partnersList.filter(p => p.status === 'active').length
  const ngo = partnersList.filter(p => p.type === 'NGO').length
  const government = partnersList.filter(p => p.type === 'Government Agency').length
  
  return {
    total,
    active,
    ngo,
    government
  }
})

const filteredPartners = computed(() => {
  const partnersList = Array.isArray(partners.value) ? partners.value : []
  return partnersList.filter(partner => {
    const matchesSearch = !searchQuery.value ||
      partner.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      partner.description.toLowerCase().includes(searchQuery.value.toLowerCase())
    
    const matchesType = !filterType.value || partner.type === filterType.value
    const matchesStatus = !filterStatus.value || partner.status === filterStatus.value

    return matchesSearch && matchesType && matchesStatus
  })
})

// Methods
const statusBadgeClass = (status) => {
  const classes = {
    active: 'bg-green-100 text-green-800',
    pending: 'bg-yellow-100 text-yellow-800',
    inactive: 'bg-gray-100 text-gray-800'
  }
  return classes[status] || 'bg-gray-100 text-gray-800'
}

const viewPartner = (partner) => {
  console.log('View partner:', partner)
  toast.info('Partner details view coming soon')
}

const editPartner = (partner) => {
  editForm.value = { ...partner }
  showEditModal.value = true
}

const deletePartner = async (partner) => {
  if (!confirm(`Delete "${partner.name}"?`)) {
    return
  }
  
  try {
    await partnersStore.deletePartner(partner.slug || partner.id)
    toast.success('Partner deleted successfully')
  } catch (err) {
    console.error('Delete error:', err)
    toast.error('Failed to delete partner')
  }
}

const createPartner = async () => {
  try {
    await partnersStore.createPartner(createForm.value)
    toast.success('Partner created successfully')
    showCreateModal.value = false
    createForm.value = {
      name: '',
      description: '',
      type: 'NGO',
      website: '',
      email: '',
      phone: ''
    }
  } catch (err) {
    console.error('Create error:', err)
    toast.error('Failed to create partner')
  }
}

const updatePartner = async () => {
  try {
    await partnersStore.updatePartner(editForm.value.slug || editForm.value.id, editForm.value)
    toast.success('Partner updated successfully')
    showEditModal.value = false
    editForm.value = {}
  } catch (err) {
    console.error('Update error:', err)
    toast.error('Failed to update partner')
  }
}

const fetchPartners = async () => {
  try {
    await partnersStore.fetchPartners()
  } catch (err) {
    console.error('Failed to fetch partners:', err)
    toast.error('Failed to load partners')
  }
}

// Lifecycle
onMounted(() => {
  fetchPartners()
})
</script>