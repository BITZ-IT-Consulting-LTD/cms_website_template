<template>
  <div class="p-6 space-y-6">
    <!-- Header -->
    <div class="flex justify-between items-start">
      <div>
        <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">Frontend Content Management</h1>
        <p class="text-gray-600 mt-1">Manage photos, headings, text, and all frontend content</p>
      </div>
      <button
        @click="showCreateModal = true"
        class="btn-primary flex items-center shadow-lg hover:shadow-xl"
      >
        <PlusIcon class="h-5 w-5 mr-2" />
        Add New Content
      </button>
    </div>

    <!-- Filters -->
    <div class="bg-white p-4 rounded-lg shadow-sm">
      <div class="flex flex-col md:flex-row gap-4">
        <div class="flex-1 relative">
          <MagnifyingGlassIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search content..."
            class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        </div>
        
        <select
          v-model="filterPage"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Pages</option>
          <option v-for="page in pages" :key="page.id" :value="page.id">{{ page.name }}</option>
        </select>
      </div>
    </div>

    <!-- Content Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div
        v-for="upload in filteredUploads"
        :key="upload.id"
        class="bg-white rounded-lg shadow-sm border-transparent overflow-hidden hover:shadow-md transition-shadow duration-200"
      >
        <!-- Content Preview -->
        <div class="h-48 bg-gray-50 flex items-center justify-center relative">
          <!-- Photo Preview -->
          <img
            v-if="upload.type === 'photo' && upload.currentValue"
            :src="upload.currentValue"
            :alt="upload.label"
            class="max-w-full max-h-full object-contain"
            @error="handleImageError"
          />
          <!-- Heading Preview -->
          <div v-else-if="upload.type === 'heading'" class="text-center p-4">
            <h3 class="text-2xl font-bold text-gray-900">{{ upload.currentValue || upload.value }}</h3>
          </div>
          <!-- Text Preview -->
          <div v-else-if="upload.type === 'text'" class="text-center p-4">
            <p class="text-sm text-gray-600 line-clamp-3">{{ upload.currentValue || upload.value }}</p>
          </div>
          <!-- Button Preview -->
          <div v-else-if="upload.type === 'button'" class="text-center p-4">
            <button class="btn-primary">{{ upload.currentValue || upload.value }}</button>
          </div>
          <!-- Default Icon -->
          <div v-else class="text-center">
            <component :is="getTypeIcon(upload.type)" class="h-16 w-16 mx-auto text-gray-400" />
          </div>
          
          <!-- Type Badge -->
          <span class="absolute top-3 left-3 px-2 py-1 bg-white/90 text-gray-700 text-xs font-semibold rounded">
            {{ getTypeName(upload.type) }}
          </span>
          
          <!-- Page Badge -->
          <span class="absolute top-3 right-3 px-2 py-1 bg-white/90 text-gray-700 text-xs font-semibold rounded">
            {{ getPageName(upload.page) }}
          </span>
        </div>

        <!-- Content Info -->
        <div class="p-5">
          <h3 class="font-semibold text-lg text-gray-900 mb-2">{{ upload.label }}</h3>
          <p class="text-xs text-gray-500 mb-4">{{ upload.description }}</p>
          
          <!-- Key/Identifier -->
          <div class="flex items-center text-xs text-gray-500 mb-4">
            <CodeBracketIcon class="h-4 w-4 mr-1" />
            <span class="font-mono">{{ upload.key }}</span>
          </div>

          <!-- Actions -->
          <div class="flex gap-2">
            <button
              @click="editUpload(upload)"
              class="flex-1 btn-primary text-sm flex items-center justify-center"
            >
              <PencilIcon class="h-4 w-4 mr-1" />
              Edit
            </button>
            <button
              @click="previewUpload(upload)"
              class="flex-1 btn-outline text-sm flex items-center justify-center"
            >
              <EyeIcon class="h-4 w-4 mr-1" />
              Preview
            </button>
            <button
              @click="deleteUpload(upload)"
              class="btn-danger text-sm flex items-center justify-center px-3"
              title="Delete content"
            >
              <TrashIcon class="h-4 w-4" />
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-if="filteredUploads.length === 0" class="bg-white rounded-lg shadow-sm border-transparent p-12 text-center">
      <PhotoIcon class="mx-auto h-12 w-12 text-gray-400" />
      <h3 class="mt-2 text-sm font-medium text-gray-900">No content found</h3>
      <p class="mt-1 text-sm text-gray-500">Get started by adding new content</p>
      <button
        @click="showCreateModal = true"
        class="mt-4 btn-primary"
      >
        Add New Content
      </button>
    </div>

    <!-- Edit Modal -->
    <Teleport to="body">
      <Transition name="modal">
        <div
          v-if="showEditModal && selectedUpload"
          class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm"
          @click.self="closeEditModal"
        >
          <div class="relative w-full max-w-3xl bg-white rounded-xl shadow-2xl overflow-hidden max-h-[90vh] overflow-y-auto">
            <!-- Header -->
            <div class="flex items-center justify-between p-4 border-b border-gray-200 bg-gray-50">
              <h3 class="text-lg font-semibold text-gray-900">Edit {{ selectedUpload.label }}</h3>
              <button
                @click="closeEditModal"
                class="p-2 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-full transition-colors"
              >
                <XMarkIcon class="h-5 w-5" />
              </button>
            </div>

            <!-- Form -->
            <div class="p-6 space-y-6">
              <!-- Basic Info -->
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Label</label>
                <input
                  v-model="editForm.label"
                  type="text"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Key/Identifier</label>
                <input
                  v-model="editForm.key"
                  type="text"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 font-mono"
                  placeholder="e.g., hero_image, main_title"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Page</label>
                <select
                  v-model="editForm.page"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                >
                  <option v-for="page in pages" :key="page.id" :value="page.id">{{ page.name }}</option>
                </select>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Content Type</label>
                <select
                  v-model="editForm.type"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                >
                  <option v-for="type in contentTypes" :key="type.id" :value="type.id">{{ type.name }}</option>
                </select>
              </div>

              <!-- Photo Upload -->
              <div v-if="editForm.type === 'photo'">
                <label class="block text-sm font-medium text-gray-700 mb-2">Image</label>
                <div v-if="editForm.currentValue" class="mb-4">
                  <img :src="editForm.currentValue" :alt="editForm.label" class="max-w-full h-48 object-contain border border-gray-200 rounded-lg" />
                </div>
                <input
                  type="file"
                  accept="image/*"
                  @change="handleImageUpload"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                />
              </div>

              <!-- Heading Input -->
              <div v-else-if="editForm.type === 'heading'">
                <label class="block text-sm font-medium text-gray-700 mb-2">Heading Text</label>
                <input
                  v-model="editForm.value"
                  type="text"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 text-lg font-semibold"
                  placeholder="Enter heading text..."
                />
                <p class="mt-1 text-xs text-gray-500">Used for section titles, card titles, and other prominent headings.</p>
              </div>

              <!-- Text Input -->
              <div v-else-if="editForm.type === 'text'">
                <label class="block text-sm font-medium text-gray-700 mb-2">Text Content</label>
                <textarea
                  v-model="editForm.value"
                  rows="6"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 resize-y"
                  placeholder="Enter text content..."
                ></textarea>
                <p class="mt-1 text-xs text-gray-500">Supports multi-line text for descriptions, card content, and longer text blocks.</p>
              </div>

              <!-- Button Input -->
              <div v-else-if="editForm.type === 'button'">
                <label class="block text-sm font-medium text-gray-700 mb-2">Button Text</label>
                <input
                  v-model="editForm.value"
                  type="text"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                  placeholder="Enter button text..."
                />
                <p class="mt-1 text-xs text-gray-500">Text displayed on call-to-action buttons and links.</p>
              </div>

              <!-- Description -->
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Description</label>
                <textarea
                  v-model="editForm.description"
                  rows="2"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                  placeholder="Brief description of this content item"
                ></textarea>
              </div>

              <!-- Actions -->
              <div class="flex gap-3 pt-4 border-t border-gray-200">
                <button
                  @click="saveUpload"
                  :disabled="loading"
                  class="flex-1 btn-primary"
                >
                  <svg v-if="loading" class="animate-spin -ml-1 mr-3 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  {{ loading ? 'Saving...' : 'Save Changes' }}
                </button>
                <button
                  @click="closeEditModal"
                  class="px-6 py-2 text-gray-600 hover:text-gray-900 hover:bg-gray-50 rounded-lg transition-colors"
                >
                  Cancel
                </button>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>

    <!-- Create Modal -->
    <Teleport to="body">
      <Transition name="modal">
        <div
          v-if="showCreateModal"
          class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm"
          @click.self="closeCreateModal"
        >
          <div class="relative w-full max-w-3xl bg-white rounded-xl shadow-2xl overflow-hidden max-h-[90vh] overflow-y-auto">
            <!-- Header -->
            <div class="flex items-center justify-between p-4 border-b border-gray-200 bg-gray-50">
              <h3 class="text-lg font-semibold text-gray-900">Add New Content</h3>
              <button
                @click="closeCreateModal"
                class="p-2 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-full transition-colors"
              >
                <XMarkIcon class="h-5 w-5" />
              </button>
            </div>

            <!-- Form -->
            <div class="p-6 space-y-6">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Label</label>
                <input
                  v-model="createForm.label"
                  type="text"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                  placeholder="e.g., Hero Image, Main Title"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Key/Identifier</label>
                <input
                  v-model="createForm.key"
                  type="text"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 font-mono"
                  placeholder="e.g., hero_image, main_title"
                />
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Page</label>
                <select
                  v-model="createForm.page"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                >
                  <option value="">Select Page</option>
                  <option v-for="page in pages" :key="page.id" :value="page.id">{{ page.name }}</option>
                </select>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Content Type</label>
                <select
                  v-model="createForm.type"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                >
                  <option value="">Select Type</option>
                  <option v-for="type in contentTypes" :key="type.id" :value="type.id">{{ type.name }}</option>
                </select>
              </div>

              <!-- Dynamic Content Input based on type -->
              <div v-if="createForm.type === 'photo'">
                <label class="block text-sm font-medium text-gray-700 mb-2">Upload Image</label>
                <input
                  type="file"
                  accept="image/*"
                  @change="handleCreateImageUpload"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                />
              </div>

              <div v-else-if="createForm.type === 'heading'">
                <label class="block text-sm font-medium text-gray-700 mb-2">Heading Text</label>
                <input
                  v-model="createForm.value"
                  type="text"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 text-lg font-semibold"
                  placeholder="Enter heading text..."
                />
                <p class="mt-1 text-xs text-gray-500">Used for section titles, card titles, and other prominent headings.</p>
              </div>

              <div v-else-if="createForm.type === 'text'">
                <label class="block text-sm font-medium text-gray-700 mb-2">Text Content</label>
                <textarea
                  v-model="createForm.value"
                  rows="6"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 resize-y"
                  placeholder="Enter text content..."
                ></textarea>
                <p class="mt-1 text-xs text-gray-500">Supports multi-line text for descriptions, card content, and longer text blocks.</p>
              </div>

              <div v-else-if="createForm.type === 'button'">
                <label class="block text-sm font-medium text-gray-700 mb-2">Button Text</label>
                <input
                  v-model="createForm.value"
                  type="text"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                  placeholder="Enter button text..."
                />
                <p class="mt-1 text-xs text-gray-500">Text displayed on call-to-action buttons and links.</p>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Description</label>
                <textarea
                  v-model="createForm.description"
                  rows="2"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                  placeholder="Brief description of this content item"
                ></textarea>
              </div>

              <!-- Actions -->
              <div class="flex gap-3 pt-4 border-t border-gray-200">
                <button
                  @click="createNewUpload"
                  :disabled="loading"
                  class="flex-1 btn-primary"
                >
                  <svg v-if="loading" class="animate-spin -ml-1 mr-3 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  {{ loading ? 'Creating...' : 'Create Content' }}
                </button>
                <button
                  @click="closeCreateModal"
                  class="px-6 py-2 text-gray-600 hover:text-gray-900 hover:bg-gray-50 rounded-lg transition-colors"
                >
                  Cancel
                </button>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useUploadsStore } from '@/stores/uploads'
import { useToast } from 'vue-toastification'
import {
  PlusIcon,
  MagnifyingGlassIcon,
  PencilIcon,
  EyeIcon,
  TrashIcon,
  XMarkIcon,
  PhotoIcon,
  DocumentTextIcon,
  CodeBracketIcon
} from '@heroicons/vue/24/outline'

const uploadsStore = useUploadsStore()
const toast = useToast()

const searchQuery = ref('')
const filterPage = ref('')
const showEditModal = ref(false)
const showCreateModal = ref(false)
const selectedUpload = ref(null)
const imagePreview = ref(null)

const uploads = computed(() => uploadsStore.uploads)
const pages = computed(() => uploadsStore.pages)
const contentTypes = computed(() => uploadsStore.contentTypes)
const loading = computed(() => uploadsStore.loading)

const editForm = ref({
  id: null,
  label: '',
  key: '',
  page: '',
  type: '',
  value: '',
  currentValue: '',
  description: ''
})

const createForm = ref({
  label: '',
  key: '',
  page: '',
  type: '',
  value: '',
  description: ''
})

const filteredUploads = computed(() => {
  let filtered = uploads.value

  // Filter by search query
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(upload =>
      upload.label.toLowerCase().includes(query) ||
      upload.key.toLowerCase().includes(query) ||
      (upload.description && upload.description.toLowerCase().includes(query))
    )
  }

  // Filter by page
  if (filterPage.value) {
    filtered = filtered.filter(upload => upload.page === filterPage.value)
  }

  return filtered
})

const getTypeName = (type) => {
  const typeObj = contentTypes.value.find(t => t.id === type)
  return typeObj ? typeObj.name : type
}

const getPageName = (pageId) => {
  const pageObj = pages.value.find(p => p.id === pageId)
  return pageObj ? pageObj.name : pageId
}

const getTypeIcon = (type) => {
  const icons = {
    photo: PhotoIcon,
    heading: DocumentTextIcon,
    text: DocumentTextIcon,
    button: DocumentTextIcon,
    video: DocumentTextIcon,
    icon: DocumentTextIcon
  }
  return icons[type] || DocumentTextIcon
}

const handleImageError = (e) => {
  e.target.style.display = 'none'
}

const editUpload = (upload) => {
  selectedUpload.value = upload
  editForm.value = {
    id: upload.id,
    label: upload.label,
    key: upload.key,
    page: upload.page,
    type: upload.type,
    value: upload.currentValue || upload.value,
    currentValue: upload.currentValue || upload.value,
    description: upload.description || ''
  }
  imagePreview.value = upload.type === 'photo' ? (upload.currentValue || upload.value) : null
  showEditModal.value = true
}

const handleImageUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    if (file.size > 10 * 1024 * 1024) {
      toast.error('Image size must be less than 10MB')
      return
    }
    const reader = new FileReader()
    reader.onload = (e) => {
      imagePreview.value = e.target.result
      editForm.value.value = e.target.result
      editForm.value.currentValue = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

const handleCreateImageUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    if (file.size > 10 * 1024 * 1024) {
      toast.error('Image size must be less than 10MB')
      return
    }
    const reader = new FileReader()
    reader.onload = (e) => {
      createForm.value.value = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

const saveUpload = async () => {
  if (!editForm.value.label || !editForm.value.key) {
    toast.error('Please fill in all required fields')
    return
  }

  try {
    // Ensure we're passing the current value
    const updateData = {
      label: editForm.value.label,
      key: editForm.value.key,
      page: editForm.value.page,
      type: editForm.value.type,
      value: editForm.value.value || editForm.value.currentValue || '',
      currentValue: editForm.value.value || editForm.value.currentValue || '',
      description: editForm.value.description || ''
    }
    
    console.log('Saving upload:', updateData)
    
    await uploadsStore.updateUpload(editForm.value.id, updateData)
    toast.success('Content updated successfully')
    
    // Refresh the uploads list to show updated content
    await uploadsStore.fetchUploads()
    
    closeEditModal()
  } catch (error) {
    console.error('Update error:', error)
    toast.error('Failed to update content')
  }
}

const createNewUpload = async () => {
  if (!createForm.value.label || !createForm.value.key || !createForm.value.page || !createForm.value.type) {
    toast.error('Please fill in all required fields')
    return
  }

  try {
    await uploadsStore.createUpload({
      label: createForm.value.label,
      key: createForm.value.key,
      page: createForm.value.page,
      type: createForm.value.type,
      value: createForm.value.value || '',
      description: createForm.value.description || ''
    })
    toast.success('Content created successfully')
    closeCreateModal()
    resetCreateForm()
  } catch (error) {
    console.error('Create error:', error)
    toast.error('Failed to create content')
  }
}

const deleteUpload = async (upload) => {
  if (!confirm(`Are you sure you want to delete "${upload.label}"?`)) {
    return
  }

  try {
    await uploadsStore.deleteUpload(upload.id)
    toast.success('Content deleted successfully')
  } catch (error) {
    console.error('Delete error:', error)
    toast.error('Failed to delete content')
  }
}

const previewUpload = (upload) => {
  const frontendUrl = import.meta.env.VITE_FRONTEND_URL || 'http://localhost:3000'
  const pageSlug = pages.value.find(p => p.id === upload.page)?.slug || upload.page
  const url = `${frontendUrl}/${pageSlug}`
  window.open(url, '_blank')
  toast.info('Opening frontend page in new tab...')
}

const closeEditModal = () => {
  showEditModal.value = false
  selectedUpload.value = null
  imagePreview.value = null
  editForm.value = {
    id: null,
    label: '',
    key: '',
    page: '',
    type: '',
    value: '',
    currentValue: '',
    description: ''
  }
}

const closeCreateModal = () => {
  showCreateModal.value = false
  resetCreateForm()
}

const resetCreateForm = () => {
  createForm.value = {
    label: '',
    key: '',
    page: '',
    type: '',
    value: '',
    description: ''
  }
}

onMounted(async () => {
  await uploadsStore.fetchUploads()
})
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-active .relative,
.modal-leave-active .relative {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.modal-enter-from .relative,
.modal-leave-to .relative {
  transform: scale(0.9);
  opacity: 0;
}
</style>

