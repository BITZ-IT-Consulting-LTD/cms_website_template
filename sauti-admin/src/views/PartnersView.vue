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
              <img v-if="partner.logo" :src="partner.logo" class="h-full w-full object-contain" :alt="partner.name" />
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

          <div v-if="partner.phone" class="flex items-center">
            <PhoneIcon class="h-4 w-4 mr-2" />
            <span>{{ partner.phone }}</span>
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
                  <label class="block text-sm font-medium text-gray-700">Phone</label>
                  <input v-model="createForm.phone" type="tel" class="form-input">
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
                  <label class="block text-sm font-medium text-gray-700">Phone</label>
                  <input v-model="editForm.phone" type="tel" class="form-input">
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
    PhoneIcon
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

  const typeOptions = [
    { value: 'NGO', label: 'NGO' },
    { value: 'Government Agency', label: 'Government Agency' },
    { value: 'International Organization', label: 'International Organization' },
    { value: 'Private Sector', label: 'Private Sector' }
  ]

  const showCreateModal = ref(false)
  const showEditModal = ref(false)
  const editForm = ref({})
  const createLogoInput = ref(null)
  const editLogoInput = ref(null)
  const createForm = ref({
    name: '',
    description: '',
    partner_type: 'NGO', // Corrected to partner_type
    website_url: '', // Corrected to website_url
    email: '',
    phone: '',
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
    console.log('View partner:', partner)
    toast.info('Partner details view coming soon')
  }

  const editPartner = (partner) => {
    editForm.value = { ...partner, logoFile: null, logoPreview: partner.logo || null } // Reset logoFile and set logoPreview
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
      const formData = new FormData()
      for (const key in createForm.value) {
        if (key === 'logoFile' && createForm.value[key]) {
          formData.append('logo', createForm.value[key])
        } else if (key !== 'logoFile') {
          formData.append(key, createForm.value[key])
        }
      }
      await partnersStore.createPartner(formData)
      toast.success('Partner created successfully')
      showCreateModal.value = false
      createForm.value = {
        name: '',
        description: '',
        partner_type: 'NGO',
        website_url: '',
        email: '',
        phone: '',
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
      const formData = new FormData()
      for (const key in editForm.value) {
        if (key === 'logoFile' && editForm.value[key]) {
          formData.append('logo', editForm.value[key])
        } else if (key !== 'logoFile' && key !== 'logo') { // Exclude existing logo URL
          formData.append(key, editForm.value[key])
        }
      }
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