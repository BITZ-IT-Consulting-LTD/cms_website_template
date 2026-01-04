<template>
  <div class="p-6">
    <!-- Page Header -->
    <PageHeader title="Resources" description="Manage downloadable resources and educational materials"
      action-label="Add New Resource" :action-icon="PlusIcon" @action="createModal.open()" />

    <!-- Mini Dashboard -->
    <StatsGrid>
      <StatCard label="Total Resources" :value="stats.total" :icon="FolderOpenIcon" color="blue" />
      <StatCard label="Published" :value="stats.published" :icon="CheckCircleIcon" color="green" />
      <StatCard label="Total Downloads" :value="stats.downloads" :icon="ArrowDownTrayIcon" color="purple" />
      <StatCard label="This Month" :value="stats.thisMonth" :icon="CalendarIcon" color="orange" />
    </StatsGrid>

    <!-- Filters -->
    <FilterBar v-model="filters" search-placeholder="Search resources..." :status-options="statusOptions"
      status-label="All Status" :custom-options="categoryOptions" custom-label="All Categories">
      <template #custom-filter>
        <select v-model="filterLanguage"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500">
          <option value="">All Languages</option>
          <option value="en">English</option>
          <option value="lg">Luganda</option>
          <option value="sw">Swahili</option>
        </select>
      </template>
    </FilterBar>

    <!-- Resources Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="resource in filteredResources" :key="resource.id"
        class="bg-white rounded-lg shadow-sm border-transparent overflow-hidden hover:shadow-md transition-shadow duration-200">
        <!-- Resource Preview -->
        <div class="h-48 bg-white flex items-center justify-center relative border-b border-transparent">
          <div class="text-center text-gray-700">
            <component :is="getFileIcon(resource.file_type || 'PDF')" class="h-16 w-16 mx-auto mb-2 opacity-90" />
            <p class="text-sm font-medium uppercase">{{ getFileTypeDisplay(resource.file_type) }}</p>
          </div>
          <span v-if="resource.status === 'draft' || resource.status === 'DRAFT'"
            class="absolute top-3 right-3 px-2 py-1 bg-yellow-100 text-yellow-800 text-xs font-semibold rounded-full">
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
          <div class="flex items-center justify-between text-xs text-gray-500 mb-4 pt-4 border-t border-transparent">
            <span>{{ resource.file_size }}</span>
            <span>{{ formatDate(resource.updated_at) }}</span>
          </div>

          <!-- Actions -->
          <div class="flex gap-2">
            <button @click="viewResource(resource)" class="flex-1 btn-outline text-sm flex items-center justify-center">
              <EyeIcon class="h-4 w-4 mr-1" />
              View
            </button>
            <button @click="downloadResource(resource)"
              class="flex-1 btn-outline text-sm flex items-center justify-center" title="Download file">
              <ArrowDownTrayIcon class="h-4 w-4 mr-1" />
              Download
            </button>
            <button @click="editResource(resource)" class="flex-1 btn-primary text-sm flex items-center justify-center">
              <PencilIcon class="h-4 w-4 mr-1" />
              Edit
            </button>
            <button @click="deleteResource(resource)" class="btn-danger text-sm flex items-center justify-center px-3"
              title="Delete resource">
              <TrashIcon class="h-4 w-4" />
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <EmptyState v-if="filteredResources.length === 0" :icon="FolderOpenIcon" title="No resources found"
      message="Get started by adding a new resource" action-label="Add New Resource" :action-icon="PlusIcon"
      @action="createModal.open()" />
  </div>

  <!-- Create Resource Modal -->
  <div v-if="showCreateModal" class="fixed inset-0 z-50 overflow-y-auto">
    <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
      <div class="fixed inset-0 transition-opacity" @click="showCreateModal = false">
        <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
      </div>

      <div
        class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
        <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
          <h3 class="text-lg font-medium text-gray-900 mb-4" style="font-family: 'Roboto', sans-serif;">Add New Resource
          </h3>
          <form @submit.prevent="createResource">
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700">Resource Title</label>
                <input v-model="createForm.title" type="text" required class="form-input"
                  placeholder="Enter resource title">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Description</label>
                <textarea v-model="createForm.description" rows="3" class="form-input"
                  placeholder="Enter resource description"></textarea>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Category</label>
                <select v-model="createForm.category" class="form-select" required>
                  <option value="">Select Category</option>
                  <option v-for="category in (Array.isArray(categories) ? categories : [])" :key="category.id"
                    :value="category.id">
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
                <input type="file" @change="handleFileUpload"
                  accept=".pdf,.doc,.docx,.jpg,.jpeg,.png,.gif,.mp4,.avi,.mov,.mp3,.m4a,.wav,.ogg" class="form-input"
                  required>
                <p class="text-xs text-gray-500 mt-1">Supported: PDF, DOC/DOCX, Images (JPG/PNG), Video (MP4/AVI/MOV),
                  Audio (MP3/M4A/WAV/OGG)</p>
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

      <div
        class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
        <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
          <h3 class="text-lg font-medium text-gray-900 mb-4" style="font-family: 'Roboto', sans-serif;">Edit Resource
          </h3>
          <form @submit.prevent="updateResource">
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700">Resource Title</label>
                <input v-model="editForm.title" type="text" required class="form-input"
                  placeholder="Enter resource title">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Description</label>
                <textarea v-model="editForm.description" rows="3" class="form-input"
                  placeholder="Enter resource description"></textarea>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Category</label>
                <select v-model="editForm.category" class="form-select" required>
                  <option value="">Select Category</option>
                  <option v-for="category in (Array.isArray(categories) ? categories : [])" :key="category.id"
                    :value="category.id">
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
                <input type="file" @change="handleEditFileUpload"
                  accept=".pdf,.doc,.docx,.jpg,.jpeg,.png,.gif,.mp4,.avi,.mov,.mp3,.m4a,.wav,.ogg" class="form-input">
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

    <!-- Resource Preview Modal -->
    <ResourcePreviewModal v-if="selectedResource" :isOpen="isPreviewOpen" :slug="selectedResource.slug || ''"
      :resourceId="selectedResource.id || null" :fileType="selectedResource.file_type || ''"
      :fileUrl="selectedResource.file || ''" :resourceTitle="selectedResource.title || 'Resource'"
      @close="closePreview" />
  </div>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import { useResourcesStore } from '@/stores/resources'
  import { useToast } from 'vue-toastification'
  import { useModal } from '@/composables'
  import { PageHeader, StatsGrid, StatCard, FilterBar, EmptyState } from '@/components/admin'
  import ResourcePreviewModal from '@/components/previews/ResourcePreviewModal.vue'
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
    FilmIcon,
    MusicalNoteIcon
  } from '@heroicons/vue/24/outline'

  const route = useRoute()
  const resourcesStore = useResourcesStore()
  const toast = useToast()

  // Modals
  const createModal = useModal()
  const editModal = useModal()

  // Reactive data
  const resources = computed(() => resourcesStore.resources)
  const categories = computed(() => resourcesStore.categories)

  const stats = ref({
    total: 0,
    published: 0,
    downloads: 0,
    thisMonth: 0
  })

  // Filters using FilterBar pattern
  const filters = ref({
    search: '',
    status: '',
    custom: ''
  })

  // Backward compatibility refs
  const searchQuery = computed({
    get: () => filters.value.search,
    set: (val) => { filters.value.search = val }
  })
  const filterStatus = computed({
    get: () => filters.value.status,
    set: (val) => { filters.value.status = val }
  })
  const filterCategory = computed({
    get: () => filters.value.custom,
    set: (val) => { filters.value.custom = val }
  })

  const filterLanguage = ref('')

  // Filter options
  const statusOptions = [
    { value: 'published', label: 'Published' },
    { value: 'draft', label: 'Draft' }
  ]

  const categoryOptions = computed(() => {
    const predefined = [
      { value: 'guides', label: 'Guides & Manuals' },
      { value: 'posters', label: 'Posters & Infographics' },
      { value: 'training', label: 'Training Materials' },
      { value: 'research', label: 'Research Reports' },
      { value: 'policy', label: 'Policy Documents' }
    ]

    // Add categories from store if available
    if (Array.isArray(categories.value) && categories.value.length > 0) {
      return categories.value.map(c => ({ value: c.name, label: c.name }))
    }

    return predefined
  })

  // Legacy modal state for existing modals
  const showCreateModal = computed({
    get: () => createModal.isOpen.value,
    set: (val) => { if (val) createModal.open(); else createModal.close() }
  })
  const showEditModal = computed({
    get: () => editModal.isOpen.value,
    set: (val) => { if (val) editModal.open(); else editModal.close() }
  })

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
      'MOV': FilmIcon,
      'AUDIO': MusicalNoteIcon,
      'MP3': MusicalNoteIcon,
      'M4A': MusicalNoteIcon,
      'WAV': MusicalNoteIcon,
      'OGG': MusicalNoteIcon
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

  const isPreviewOpen = ref(false)
  const selectedResource = ref(null)

  const viewResource = (resource) => {
    console.log('View resource clicked:', resource)
    if (!resource) {
      console.error('Resource is null or undefined')
      toast.error('Resource not found')
      return
    }

    if (!resource.file) {
      console.warn('Resource has no file:', resource)
      toast.warning('This resource has no file to preview')
      return
    }

    selectedResource.value = resource
    isPreviewOpen.value = true
    console.log('Preview modal should open:', {
      isOpen: isPreviewOpen.value,
      resource: selectedResource.value,
      fileUrl: resource.file
    })
  }

  const closePreview = () => {
    isPreviewOpen.value = false
    selectedResource.value = null
  }

  const downloadResource = (resource) => {
    if (!resource.file) {
      toast.error('No file available for download')
      return
    }

    // Handle both relative paths (/media/...) and full URLs
    let fileUrl = resource.file
    if (fileUrl && !fileUrl.startsWith('http://') && !fileUrl.startsWith('https://')) {
      // Ensure it's a relative path
      fileUrl = fileUrl.startsWith('/') ? fileUrl : `/${fileUrl}`
    }

    // Open in new tab to trigger download
    window.open(fileUrl, '_blank')
    toast.success('Downloading file...')
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
      // Validate file size (max 50MB)
      if (file.size > 50 * 1024 * 1024) {
        toast.error('File size must be less than 50MB')
        return
      }

      createForm.value.file = file
      toast.success('File selected successfully')
    }
  }

  const handleEditFileUpload = (event) => {
    const file = event.target.files[0]
    if (file) {
      // Validate file size (max 50MB)
      if (file.size > 50 * 1024 * 1024) {
        toast.error('File size must be less than 50MB')
        return
      }

      editForm.value.file = file
      toast.success('File selected successfully')
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
    if (route.query.create === 'true') {
      showCreateModal.value = true
    }
  })
</script>
