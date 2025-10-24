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
        class="px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 transition-colors duration-200 flex items-center font-medium shadow-sm"
      >
        <PlusIcon class="h-5 w-5 mr-2" />
        Add New Partner
      </button>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
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

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
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

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
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

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Government</p>
            <p class="text-3xl font-bold text-teal-600 mt-2">{{ stats.government }}</p>
          </div>
          <div class="p-3 bg-teal-100 rounded-lg">
            <BuildingLibraryIcon class="h-8 w-8 text-teal-600" />
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
            placeholder="Search partners..."
            class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        </div>
        
        <select
          v-model="filterType"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Types</option>
          <option value="ngo">NGO</option>
          <option value="government">Government Agency</option>
          <option value="corporate">Corporate</option>
          <option value="international">International Organization</option>
          <option value="community">Community Group</option>
        </select>

        <select
          v-model="filterStatus"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Status</option>
          <option value="active">Active</option>
          <option value="pending">Pending</option>
          <option value="inactive">Inactive</option>
        </select>
      </div>
    </div>

    <!-- Partners Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div
        v-for="partner in filteredPartners"
        :key="partner.id"
        class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow duration-200"
      >
        <!-- Partner Logo/Header -->
        <div class="h-32 bg-gradient-to-br from-blue-400 to-purple-500 flex items-center justify-center relative">
          <div v-if="partner.logo" class="w-24 h-24 bg-white rounded-lg flex items-center justify-center">
            <img :src="partner.logo" :alt="partner.name" class="max-w-full max-h-full object-contain p-2" />
          </div>
          <div v-else class="text-white text-4xl font-bold">
            {{ partner.name.substring(0, 2).toUpperCase() }}
          </div>
          <span
            class="absolute top-3 right-3 px-2 py-1 text-xs font-semibold rounded-full"
            :class="statusBadgeClass(partner.status)"
          >
            {{ partner.status }}
          </span>
        </div>

        <!-- Partner Info -->
        <div class="p-5">
          <h3 class="font-semibold text-lg text-gray-900 mb-2">
            {{ partner.name }}
          </h3>
          
          <p class="text-sm text-gray-600 mb-4 line-clamp-2">
            {{ partner.description }}
          </p>

          <!-- Type Badge -->
          <div class="mb-4">
            <span class="px-2 py-1 bg-gray-100 text-gray-700 text-xs rounded-full">
              {{ partner.type }}
            </span>
          </div>

          <!-- Contact Info -->
          <div class="space-y-2 mb-4">
            <div v-if="partner.website" class="flex items-center text-sm text-gray-600">
              <GlobeAltIcon class="h-4 w-4 mr-2 text-gray-400" />
              <a :href="partner.website" target="_blank" class="hover:text-primary-600 truncate">
                {{ partner.website }}
              </a>
            </div>
            <div v-if="partner.email" class="flex items-center text-sm text-gray-600">
              <EnvelopeIcon class="h-4 w-4 mr-2 text-gray-400" />
              <span class="truncate">{{ partner.email }}</span>
            </div>
            <div v-if="partner.phone" class="flex items-center text-sm text-gray-600">
              <PhoneIcon class="h-4 w-4 mr-2 text-gray-400" />
              <span>{{ partner.phone }}</span>
            </div>
          </div>

          <!-- Meta Info -->
          <div class="flex items-center justify-between text-xs text-gray-500 mb-4 pt-4 border-t border-gray-100">
            <span>Since {{ new Date(partner.partnership_start).getFullYear() }}</span>
            <span>{{ partner.projects || 0 }} projects</span>
          </div>

          <!-- Actions -->
          <div class="flex gap-2">
            <button
              @click="viewPartner(partner)"
              class="flex-1 px-3 py-2 bg-gray-100 text-gray-700 rounded-md hover:bg-gray-200 transition-colors duration-200 flex items-center justify-center text-sm font-medium"
            >
              <EyeIcon class="h-4 w-4 mr-1" />
              View
            </button>
            <button
              @click="editPartner(partner)"
              class="flex-1 px-3 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 transition-colors duration-200 flex items-center justify-center text-sm font-medium"
            >
              <PencilIcon class="h-4 w-4 mr-1" />
              Edit
            </button>
            <button
              @click="deletePartner(partner)"
              class="px-3 py-2 bg-red-100 text-red-600 rounded-md hover:bg-red-200 transition-colors duration-200"
            >
              <TrashIcon class="h-4 w-4" />
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-if="filteredPartners.length === 0" class="bg-white rounded-lg shadow-sm border border-gray-200 p-12 text-center">
      <UserGroupIcon class="mx-auto h-12 w-12 text-gray-400" />
      <h3 class="mt-2 text-sm font-medium text-gray-900">No partners found</h3>
      <p class="mt-1 text-sm text-gray-500">Get started by adding a new partner</p>
      <button
        @click="showCreateModal = true"
        class="mt-4 px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 transition-colors duration-200"
      >
        Add New Partner
      </button>
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
                <input v-model="createForm.name" type="text" required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Description</label>
                <textarea v-model="createForm.description" rows="3" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"></textarea>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Type</label>
                <select v-model="createForm.type" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500">
                  <option value="NGO">NGO</option>
                  <option value="Government Agency">Government Agency</option>
                  <option value="International Organization">International Organization</option>
                  <option value="Private Sector">Private Sector</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Website</label>
                <input v-model="createForm.website" type="url" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Email</label>
                <input v-model="createForm.email" type="email" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Phone</label>
                <input v-model="createForm.phone" type="tel" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500">
              </div>
            </div>
            <div class="mt-6 flex justify-end space-x-3">
              <button type="button" @click="showCreateModal = false" class="px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50">
                Cancel
              </button>
              <button type="submit" class="px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700">
                Create Partner
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
                <input v-model="editForm.name" type="text" required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Description</label>
                <textarea v-model="editForm.description" rows="3" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"></textarea>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Type</label>
                <select v-model="editForm.type" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500">
                  <option value="NGO">NGO</option>
                  <option value="Government Agency">Government Agency</option>
                  <option value="International Organization">International Organization</option>
                  <option value="Private Sector">Private Sector</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Website</label>
                <input v-model="editForm.website" type="url" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Email</label>
                <input v-model="editForm.email" type="email" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Phone</label>
                <input v-model="editForm.phone" type="tel" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500">
              </div>
            </div>
            <div class="mt-6 flex justify-end space-x-3">
              <button type="button" @click="showEditModal = false" class="px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50">
                Cancel
              </button>
              <button type="submit" class="px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700">
                Update Partner
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

// Mock data
const partners = ref([
  {
    id: 1,
    name: 'UNICEF Uganda',
    description: 'United Nations Children\'s Fund working to protect children\'s rights and provide humanitarian assistance across Uganda',
    type: 'International Organization',
    status: 'active',
    logo: null,
    website: 'https://www.unicef.org/uganda',
    email: 'kampala@unicef.org',
    phone: '+256 417 171 000',
    partnership_start: '2018-03-15',
    projects: 12
  },
  {
    id: 2,
    name: 'Ministry of Gender, Labour and Social Development',
    description: 'Government ministry responsible for child protection and social welfare policies in Uganda',
    type: 'Government Agency',
    status: 'active',
    logo: null,
    website: 'https://www.mglsd.go.ug',
    email: 'info@mglsd.go.ug',
    phone: '+256 414 347 854',
    partnership_start: '2017-01-10',
    projects: 8
  },
  {
    id: 3,
    name: 'Save the Children Uganda',
    description: 'International NGO focused on improving children\'s lives through better education, healthcare, and economic opportunities',
    type: 'NGO',
    status: 'active',
    logo: null,
    website: 'https://uganda.savethechildren.net',
    email: 'uganda@savethechildren.org',
    phone: '+256 312 258 230',
    partnership_start: '2019-06-20',
    projects: 15
  },
  {
    id: 4,
    name: 'Plan International Uganda',
    description: 'Working to advance children\'s rights and equality for girls across Uganda',
    type: 'NGO',
    status: 'active',
    logo: null,
    website: 'https://plan-international.org/uganda',
    email: 'uganda.co@plan-international.org',
    phone: '+256 414 345 123',
    partnership_start: '2020-02-01',
    projects: 10
  },
  {
    id: 5,
    name: 'Uganda Police Child and Family Protection Unit',
    description: 'Specialized police unit handling cases of child abuse, domestic violence, and family-related crimes',
    type: 'Government Agency',
    status: 'active',
    logo: null,
    website: 'https://www.upf.go.ug',
    email: 'cfpu@upf.go.ug',
    phone: '0800 123 456',
    partnership_start: '2017-08-15',
    projects: 6
  },
  {
    id: 6,
    name: 'African Network for Prevention of Child Abuse',
    description: 'Regional network working to prevent and respond to child abuse and neglect across Africa',
    type: 'NGO',
    status: 'active',
    logo: null,
    website: 'https://anppcan.org',
    email: 'info@anppcan.org',
    phone: '+256 414 534 271',
    partnership_start: '2021-04-10',
    projects: 7
  }
])

const stats = ref({
  total: 24,
  active: 21,
  ngo: 14,
  government: 6
})

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

const filteredPartners = computed(() => {
  return partners.value.filter(partner => {
    const matchesSearch = !searchQuery.value ||
      partner.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      partner.description.toLowerCase().includes(searchQuery.value.toLowerCase())
    
    const matchesType = !filterType.value || partner.type === filterType.value
    const matchesStatus = !filterStatus.value || partner.status === filterStatus.value

    return matchesSearch && matchesType && matchesStatus
  })
})

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
}

const editPartner = (partner) => {
  editForm.value = { ...partner }
  showEditModal.value = true
}

const deletePartner = (partner) => {
  if (confirm(`Delete "${partner.name}"?`)) {
    const index = partners.value.findIndex(p => p.id === partner.id)
    if (index > -1) {
      partners.value.splice(index, 1)
      // Update stats
      stats.value.total--
      if (partner.type === 'NGO') stats.value.ngo--
      if (partner.type === 'Government Agency') stats.value.government--
      if (partner.status === 'active') stats.value.active--
    }
  }
}

const createPartner = () => {
  const newPartner = {
    id: Date.now(), // Simple ID generation
    ...createForm.value,
    status: 'active',
    logo: null,
    partnership_start: new Date().toISOString().split('T')[0],
    projects: 0
  }
  partners.value.push(newPartner)
  
  // Update stats
  stats.value.total++
  stats.value.active++
  if (newPartner.type === 'NGO') stats.value.ngo++
  if (newPartner.type === 'Government Agency') stats.value.government++
  
  // Reset form and close modal
  createForm.value = {
    name: '',
    description: '',
    type: 'NGO',
    website: '',
    email: '',
    phone: ''
  }
  showCreateModal.value = false
}

const updatePartner = () => {
  const index = partners.value.findIndex(p => p.id === editForm.value.id)
  if (index > -1) {
    partners.value[index] = { ...editForm.value }
    showEditModal.value = false
  }
}
</script>
