<template>
  <div class="p-6">
    <!-- Page Header -->
    <PageHeader title="Partners" description="Manage partner organizations and collaborations"
      action-label="Add New Partner" :action-icon="PlusIcon" @action="showCreateModal = true" />

    <!-- Mini Dashboard -->
    <StatsGrid>
      <StatCard label="Total Partners" :value="stats.total" :icon="UserGroupIcon" color="blue" />
      <StatCard label="Active" :value="stats.active" :icon="CheckCircleIcon" color="green" />
      <StatCard label="NGO Partners" :value="stats.ngo" :icon="BuildingOfficeIcon" color="purple" />
      <StatCard label="Government" :value="stats.government" :icon="BuildingLibraryIcon" color="orange" />
    </StatsGrid>

    <!-- Filters -->
    <FilterBar v-model="filters" search-placeholder="Search partners..." :status-options="statusOptions"
      status-label="All Status" :custom-options="typeOptions" custom-label="All Types" />

    <!-- Loading State -->
    <LoadingState v-if="loading" message="Loading partners..." />

    <!-- Partners Grid -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="partner in filteredPartners" :key="partner.id"
        class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow">
        <div class="flex items-start justify-between mb-4">
          <div class="flex items-center space-x-3">
            <div
              class="h-12 w-12 bg-gray-50 rounded-lg flex items-center justify-center overflow-hidden border border-gray-100">
              <img v-if="partner.logo_url || partner.logo" :src="partner.logo_url || partner.logo" class="h-full w-full object-contain" :alt="partner.name" />
              <UserGroupIcon v-else class="h-6 w-6 text-gray-400" />
            </div>
            <div>
              <h3 class="text-lg font-semibold text-gray-900 line-clamp-2">{{ partner.name }}</h3>
              <span class="inline-flex px-2 py-1 text-xs font-semibold rounded-full mt-1"
                :class="statusBadgeClass(partner.status)">
                {{ partner.status }}
              </span>
            </div>
          </div>

          <div class="flex items-center space-x-2">
            <button @click="viewPartner(partner)" class="text-blue-600 hover:text-blue-900 p-2" title="View">
              <EyeIcon class="h-4 w-4" />
            </button>
            <button @click="editPartner(partner)" class="text-primary-600 hover:text-primary-900 p-2" title="Edit">
              <PencilIcon class="h-4 w-4" />
            </button>
            <button @click="duplicatePartner(partner)" class="text-green-600 hover:text-green-900 p-2" title="Duplicate">
              <DocumentDuplicateIcon class="h-4 w-4" />
            </button>
            <button @click="deletePartner(partner)" class="text-red-600 hover:text-red-900 p-2" title="Delete">
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

          <div v-if="partner.phone_numbers?.length || partner.phone" class="flex items-center">
            <PhoneIcon class="h-4 w-4 mr-2" />
            <span>{{ (partner.phone_numbers?.length ? partner.phone_numbers : [partner.phone]).join(', ') }}</span>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <EmptyState v-if="filteredPartners.length === 0" :icon="UserGroupIcon" title="No partners found"
        :message="searchQuery || filters.status || filters.custom ? 'Try adjusting your search criteria.' : 'Start building your network by adding partner organizations.'"
        :action-label="!searchQuery && !filters.status && !filters.custom ? 'Add Your First Partner' : null"
        :action-icon="PlusIcon" @action="showCreateModal = true" class="col-span-full" />
    </div>

    <!-- Create Partner Modal -->
    <div v-if="showCreateModal" class="fixed inset-0 z-50 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 transition-opacity" @click="showCreateModal = false">
          <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
        </div>

        <div
          class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <h3 class="text-lg font-medium text-gray-900 mb-4" style="font-family: 'Roboto', sans-serif;">Add New
              Partner</h3>
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
                  <select v-model="createForm.partner_type" class="form-select">
                    <option value="GOVERNMENT">Government Agency</option>
                    <option value="UN_AGENCY">UN Agency</option>
                    <option value="NGO">NGO/CSO</option>
                    <option value="EMBASSY">Embassy / Diplomatic Mission</option>
                    <option value="PRIVATE">Private Sector</option>
                    <option value="OTHER">Other</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Website</label>
                  <input v-model="createForm.website_url" type="url" class="form-input">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Email</label>
                  <input v-model="createForm.email" type="email" class="form-input">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Phone Number(s)</label>
                  <div v-for="(number, index) in createForm.phone_numbers" :key="index"
                    class="flex items-center space-x-2 mt-1">
                    <input v-model="createForm.phone_numbers[index]" type="tel" class="form-input flex-1"
                      placeholder="e.g. +256 700 123 456">
                    <button v-if="createForm.phone_numbers.length > 1" type="button"
                      @click="removeCreatePhone(index)" class="text-red-600 hover:text-red-800 px-2"
                      title="Remove">&times;</button>
                  </div>
                  <button type="button" @click="addCreatePhone" class="text-primary-600 hover:text-primary-800 text-sm mt-2">
                    + Add phone
                  </button>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Logo</label>
                  <input ref="createLogoInput" type="file" @change="handleCreateLogoUpload" accept="image/*"
                    class="form-input-file">
                  <div v-if="createForm.logoPreview" class="mt-2">
                    <img :src="createForm.logoPreview" alt="Logo Preview" class="max-w-xs h-auto">
                    <button @click="removeCreateLogo" type="button"
                      class="text-red-600 hover:text-red-800 text-sm mt-1">Remove</button>
                  </div>
                </div>
                <div class="flex items-center space-x-6">
                  <label class="flex items-center space-x-2">
                    <input v-model="createForm.is_featured" type="checkbox" class="form-checkbox">
                    <span class="text-sm text-gray-700">Show on homepage</span>
                  </label>
                  <label class="flex items-center space-x-2">
                    <input v-model="createForm.is_active" type="checkbox" class="form-checkbox">
                    <span class="text-sm text-gray-700">Active</span>
                  </label>
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

        <div
          class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <h3 class="text-lg font-medium text-gray-900 mb-4" style="font-family: 'Roboto', sans-serif;">Edit Partner
            </h3>
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
                  <select v-model="editForm.partner_type" class="form-select">
                    <option value="GOVERNMENT">Government Agency</option>
                    <option value="UN_AGENCY">UN Agency</option>
                    <option value="NGO">NGO/CSO</option>
                    <option value="EMBASSY">Embassy / Diplomatic Mission</option>
                    <option value="PRIVATE">Private Sector</option>
                    <option value="OTHER">Other</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Website</label>
                  <input v-model="editForm.website_url" type="url" class="form-input">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Email</label>
                  <input v-model="editForm.email" type="email" class="form-input">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Phone Number(s)</label>
                  <div v-for="(number, index) in editForm.phone_numbers" :key="index"
                    class="flex items-center space-x-2 mt-1">
                    <input v-model="editForm.phone_numbers[index]" type="tel" class="form-input flex-1"
                      placeholder="e.g. +256 700 123 456">
                    <button v-if="editForm.phone_numbers.length > 1" type="button"
                      @click="removeEditPhone(index)" class="text-red-600 hover:text-red-800 px-2"
                      title="Remove">&times;</button>
                  </div>
                  <button type="button" @click="addEditPhone" class="text-primary-600 hover:text-primary-800 text-sm mt-2">
                    + Add phone
                  </button>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700">Logo</label>
                  <input ref="editLogoInput" type="file" @change="handleEditLogoUpload" accept="image/*"
                    class="form-input-file">
                  <div v-if="editForm.logoPreview || editForm.logo" class="mt-2">
                    <img :src="editForm.logoPreview || editForm.logo" alt="Logo Preview" class="max-w-xs h-auto">
                    <button v-if="editForm.logoPreview" @click="removeEditLogo" type="button"
                      class="text-red-600 hover:text-red-800 text-sm mt-1">Remove</button>
                  </div>
                </div>
                <div class="flex items-center space-x-6">
                  <label class="flex items-center space-x-2">
                    <input v-model="editForm.is_featured" type="checkbox" class="form-checkbox">
                    <span class="text-sm text-gray-700">Show on homepage</span>
                  </label>
                  <label class="flex items-center space-x-2">
                    <input v-model="editForm.is_active" type="checkbox" class="form-checkbox">
                    <span class="text-sm text-gray-700">Active</span>
                  </label>
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

    <!-- View Partner Modal -->
    <div v-if="showViewModal" class="fixed inset-0 z-50 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 transition-opacity" @click="showViewModal = false">
          <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
        </div>

        <div
          class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-lg font-medium text-gray-900" style="font-family: 'Roboto', sans-serif;">Partner Details</h3>
              <button @click="showViewModal = false" class="text-gray-400 hover:text-gray-600">
                <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>

            <div v-if="viewedPartner" class="space-y-4">
              <div class="flex items-center space-x-4">
                <div class="h-16 w-16 bg-gray-50 rounded-lg flex items-center justify-center overflow-hidden border border-gray-100">
                  <img v-if="viewedPartner.logo_url || viewedPartner.logo" :src="viewedPartner.logo_url || viewedPartner.logo" class="h-full w-full object-contain" :alt="viewedPartner.name" />
                  <UserGroupIcon v-else class="h-8 w-8 text-gray-400" />
                </div>
                <div>
                  <h4 class="text-xl font-semibold text-gray-900">{{ viewedPartner.name }}</h4>
                  <span class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
                    :class="viewedPartner.is_active ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'">
                    {{ viewedPartner.is_active ? 'Active' : 'Inactive' }}
                  </span>
                </div>
              </div>

              <div v-if="viewedPartner.description" class="text-sm text-gray-600">{{ viewedPartner.description }}</div>

              <div class="grid grid-cols-2 gap-4 text-sm">
                <div>
                  <span class="font-medium text-gray-700">Type:</span>
                  <span class="ml-1 text-gray-600">{{ viewedPartner.partner_type }}</span>
                </div>
                <div v-if="viewedPartner.website_url">
                  <span class="font-medium text-gray-700">Website:</span>
                  <a :href="viewedPartner.website_url" target="_blank" class="ml-1 text-blue-600 hover:text-blue-800">{{ viewedPartner.website_url }}</a>
                </div>
                <div v-if="viewedPartner.email">
                  <span class="font-medium text-gray-700">Email:</span>
                  <span class="ml-1 text-gray-600">{{ viewedPartner.email }}</span>
                </div>
                <div v-if="viewedPartner.phone_numbers?.length || viewedPartner.phone">
                  <span class="font-medium text-gray-700">Phone:</span>
                  <span class="ml-1 text-gray-600">{{ (viewedPartner.phone_numbers?.length ? viewedPartner.phone_numbers : [viewedPartner.phone]).join(', ') }}</span>
                </div>
              </div>
            </div>

            <div class="mt-6 flex justify-end">
              <button @click="showViewModal = false" class="btn-outline">Close</button>
            </div>
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
  import { PageHeader, StatsGrid, StatCard, FilterBar, LoadingState, EmptyState } from '@/components/admin'
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
    PhoneIcon,
    DocumentDuplicateIcon
  } from '@heroicons/vue/24/outline'

  const toast = useToast()
  const partnersStore = usePartnersStore()

  // Filters using FilterBar pattern
  const filters = ref({
    search: '',
    status: '',
    custom: ''
  })

  // Backward compatibility
  const searchQuery = computed({
    get: () => filters.value.search,
    set: (val) => { filters.value.search = val }
  })
  const filterStatus = computed({
    get: () => filters.value.status,
    set: (val) => { filters.value.status = val }
  })
  const filterType = computed({
    get: () => filters.value.custom,
    set: (val) => { filters.value.custom = val }
  })

  // Filter Options
  const statusOptions = [
    { value: 'active', label: 'Active' },
    { value: 'pending', label: 'Pending' },
    { value: 'inactive', label: 'Inactive' }
  ]

  // Values must match the backend PartnerType enum codes — the filter compares
  // against partner.partner_type (the code), so label-text values never matched.
  const typeOptions = [
    { value: 'GOVERNMENT', label: 'Government Agency' },
    { value: 'UN_AGENCY', label: 'UN Agency' },
    { value: 'NGO', label: 'NGO/CSO' },
    { value: 'EMBASSY', label: 'Embassy / Diplomatic Mission' },
    { value: 'PRIVATE', label: 'Private Sector' },
    { value: 'OTHER', label: 'Other' }
  ]

  const showCreateModal = ref(false)
  const showEditModal = ref(false)
  const showViewModal = ref(false)
  const viewedPartner = ref(null)
  const editForm = ref({})
  const createLogoInput = ref(null)
  const editLogoInput = ref(null)
  const createForm = ref({
    name: '',
    description: '',
    partner_type: 'NGO', // Corrected to partner_type
    website_url: '', // Corrected to website_url
    email: '',
    phone_numbers: [''],
    logoFile: null,
    logoPreview: null, // Add logoPreview
    is_active: true,
    is_featured: false,
  })

  // Use store data
  const partners = computed(() => partnersStore.partners)
  const loading = computed(() => partnersStore.loading)
  const error = computed(() => partnersStore.error)

  // Computed properties
  const stats = computed(() => {
    const partnersList = Array.isArray(partners.value) ? partners.value : []
    const total = partnersList.length
    const active = partnersList.filter(p => p.is_active).length
    const ngo = partnersList.filter(p => p.partner_type === 'NGO').length
    const government = partnersList.filter(p => p.partner_type === 'GOVERNMENT').length

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

      const matchesType = !filterType.value || partner.partner_type === filterType.value
      const matchesStatus = !filterStatus.value ||
        (filterStatus.value === 'active' && partner.is_active) ||
        (filterStatus.value === 'inactive' && !partner.is_active)

      return matchesSearch && matchesType && matchesStatus
    })
  })

  // Methods
  const statusBadgeClass = (is_active) => {
    const classes = {
      true: 'bg-green-100 text-green-800',
      false: 'bg-gray-100 text-gray-800'
    }
    return classes[is_active] || 'bg-gray-100 text-gray-800'
  }

  const viewPartner = (partner) => {
    viewedPartner.value = partner
    showViewModal.value = true
  }

  const duplicatePartner = async (partner) => {
    try {
      const duplicateData = {
        name: `${partner.name} (Copy)`,
        description: partner.description || '',
        partner_type: partner.partner_type || 'NGO',
        website_url: partner.website_url || '',
        email: partner.email || '',
        phone_numbers: partner.phone_numbers?.length ? partner.phone_numbers : (partner.phone ? [partner.phone] : []),
        is_active: false,
        is_featured: false,
      }

      await partnersStore.createPartner(duplicateData)
      toast.success(`"${partner.name}" duplicated successfully`)
      await fetchPartners()
    } catch (err) {
      console.error('Duplicate error:', err)
      toast.error('Failed to duplicate partner')
    }
  }

  const editPartner = (partner) => {
    const phoneNumbers = partner.phone_numbers?.length
      ? [...partner.phone_numbers]
      : (partner.phone ? [partner.phone] : [''])
    editForm.value = {
      ...partner,
      phone_numbers: phoneNumbers,
      logoFile: null,
      logoPreview: partner.logo_url || partner.logo || null,
    }
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

  const addCreatePhone = () => {
    createForm.value.phone_numbers.push('')
  }

  const removeCreatePhone = (index) => {
    if (createForm.value.phone_numbers.length > 1) {
      createForm.value.phone_numbers.splice(index, 1)
    }
  }

  const addEditPhone = () => {
    editForm.value.phone_numbers.push('')
  }

  const removeEditPhone = (index) => {
    if (editForm.value.phone_numbers.length > 1) {
      editForm.value.phone_numbers.splice(index, 1)
    }
  }

  const createPartner = async () => {
    try {
      const excludeKeys = ['logoFile', 'logoPreview', 'phone_numbers']
      const formData = new FormData()
      for (const key in createForm.value) {
        if (key === 'logoFile' && createForm.value[key]) {
          formData.append('logo', createForm.value[key])
        } else if (!excludeKeys.includes(key) && createForm.value[key] != null) {
          formData.append(key, createForm.value[key])
        }
      }
      const phoneNumbers = (createForm.value.phone_numbers || []).map(p => p.trim()).filter(Boolean)
      formData.append('phone_numbers', JSON.stringify(phoneNumbers))
      await partnersStore.createPartner(formData)
      toast.success('Partner created successfully')
      showCreateModal.value = false
      createForm.value = {
        name: '',
        description: '',
        partner_type: 'NGO',
        website_url: '',
        email: '',
        phone_numbers: [''],
        logoFile: null,
        logoPreview: null,
        is_active: true,
        is_featured: false,
      }
    } catch (err) {
      console.error('Create error:', err)
      toast.error('Failed to create partner')
    }
  }

  const updatePartner = async () => {
    try {
      const excludeKeys = ['logoFile', 'logoPreview', 'logo', 'logo_url', 'created_at', 'updated_at', 'created_by', 'last_updated_by', 'history', 'phone_numbers']
      const formData = new FormData()
      for (const key in editForm.value) {
        if (key === 'logoFile' && editForm.value[key]) {
          formData.append('logo', editForm.value[key])
        } else if (!excludeKeys.includes(key) && editForm.value[key] != null && typeof editForm.value[key] !== 'object') {
          formData.append(key, editForm.value[key])
        }
      }
      const phoneNumbers = (editForm.value.phone_numbers || []).map(p => p.trim()).filter(Boolean)
      formData.append('phone_numbers', JSON.stringify(phoneNumbers))
      await partnersStore.updatePartner(editForm.value.slug || editForm.value.id, formData)
      toast.success('Partner updated successfully')
      showEditModal.value = false
      editForm.value = {}
    } catch (err) {
      console.error('Update error:', err)
      toast.error('Failed to update partner')
    }
  }

  const handleCreateLogoUpload = (event) => {
    const file = event.target.files[0]
    if (file) {
      createForm.value.logoFile = file
      createForm.value.logoPreview = URL.createObjectURL(file)
    } else {
      createForm.value.logoFile = null
      createForm.value.logoPreview = null
    }
  }

  const removeCreateLogo = () => {
    createForm.value.logoFile = null
    createForm.value.logoPreview = null
    if (createLogoInput.value) {
      createLogoInput.value.value = ''
    }
  }

  const handleEditLogoUpload = (event) => {
    const file = event.target.files[0]
    if (file) {
      editForm.value.logoFile = file
      editForm.value.logoPreview = URL.createObjectURL(file)
    } else {
      editForm.value.logoFile = null
      editForm.value.logoPreview = null
    }
  }

  const removeEditLogo = () => {
    editForm.value.logoFile = null
    editForm.value.logoPreview = null
    if (editLogoInput.value) {
      editLogoInput.value.value = ''
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