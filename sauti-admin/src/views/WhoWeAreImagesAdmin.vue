<template>
  <div class="p-6">
    <!-- Page Header -->
    <PageHeader title="Who We Are Images" description="Manage the hero grid images displayed on the About page."
      action-label="Add Image" :action-icon="PlusIcon" @action="openCreateModal" />

    <!-- Stats -->
    <StatsGrid>
      <StatCard label="Total Positions" :value="9" :icon="PhotoIcon" color="blue" />
      <StatCard label="Images Set" :value="stats.filled" :icon="CheckCircleIcon" color="green" />
      <StatCard label="Empty Positions" :value="stats.empty" :icon="ExclamationCircleIcon" color="amber" />
    </StatsGrid>

    <!-- Loading State -->
    <LoadingState v-if="loading" message="Loading images..." />

    <!-- Grid Preview -->
    <div v-else class="mt-6">
      <h3 class="text-lg font-bold text-gray-800 mb-4">About Page Hero Grid Preview</h3>
      <p class="text-sm text-gray-500 mb-6">Click on any position to add or edit the image for that slot.</p>

      <!-- Grid Layout matching About page structure -->
      <div class="bg-gray-100 rounded-3xl p-6 max-w-4xl mx-auto">
        <div class="grid grid-cols-[1fr_2fr_1fr] gap-3">
          <!-- Left Column -->
          <div class="flex flex-col gap-3">
            <ImageSlot
              v-for="pos in [1, 2, 3]"
              :key="pos"
              :position="pos"
              :image="getImageByPosition(pos)"
              :position-info="positionLabels[pos]"
              @click="openEditModal(pos)"
            />
          </div>

          <!-- Center Grid (2x2) -->
          <div class="grid grid-cols-2 grid-rows-2 gap-3">
            <ImageSlot
              v-for="pos in [4, 5, 6, 7]"
              :key="pos"
              :position="pos"
              :image="getImageByPosition(pos)"
              :position-info="positionLabels[pos]"
              @click="openEditModal(pos)"
            />
          </div>

          <!-- Right Column -->
          <div class="flex flex-col gap-3">
            <ImageSlot
              v-for="pos in [8, 9]"
              :key="pos"
              :position="pos"
              :image="getImageByPosition(pos)"
              :position-info="positionLabels[pos]"
              @click="openEditModal(pos)"
            />
            <!-- Placeholder for text box (position 10 visual only) -->
            <div class="aspect-[4/3] bg-blue-50 rounded-2xl flex items-center justify-center border-2 border-dashed border-blue-200">
              <p class="text-blue-600 text-xs font-bold text-center px-2">Text: "Every Child Matters"</p>
            </div>
          </div>
        </div>
      </div>

      <!-- List View -->
      <div class="mt-8">
        <h3 class="text-lg font-bold text-gray-800 mb-4">All Grid Positions</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div
            v-for="pos in 9"
            :key="pos"
            class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group hover:shadow-lg transition-all cursor-pointer"
            @click="openEditModal(pos)"
          >
            <div class="aspect-video relative overflow-hidden bg-gray-100">
              <img
                v-if="getImageByPosition(pos)?.image_url"
                :src="getImageByPosition(pos).image_url"
                :alt="getImageByPosition(pos)?.title || `Position ${pos}`"
                class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
              />
              <div v-else class="w-full h-full flex items-center justify-center text-gray-300 bg-gray-50">
                <PhotoIcon class="w-16 h-16" />
              </div>

              <!-- Overlay controls -->
              <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-2">
                <button
                  class="p-3 bg-white text-emerald-600 rounded-xl hover:scale-110 transition-transform shadow-lg"
                  @click.stop="openEditModal(pos)"
                >
                  <PencilIcon class="h-6 w-6" />
                </button>
                <button
                  v-if="getImageByPosition(pos)"
                  class="p-3 bg-white text-red-600 rounded-xl hover:scale-110 transition-transform shadow-lg"
                  @click.stop="confirmDelete(pos)"
                >
                  <TrashIcon class="h-6 w-6" />
                </button>
              </div>

              <!-- Position Badge -->
              <div class="absolute top-2 left-2 bg-black/60 text-white text-xs font-bold px-2 py-1 rounded-lg">
                #{{ pos }}
              </div>
            </div>

            <div class="p-4">
              <h3 class="font-bold text-gray-900 text-sm mb-1">{{ positionLabels[pos]?.name || `Position ${pos}` }}</h3>
              <p class="text-gray-500 text-xs">{{ positionLabels[pos]?.description }}</p>
              <div class="mt-2 flex items-center justify-between">
                <span
                  class="text-[10px] font-bold px-2 py-0.5 rounded-full"
                  :class="getImageByPosition(pos) ? 'bg-green-100 text-green-700' : 'bg-amber-100 text-amber-700'"
                >
                  {{ getImageByPosition(pos) ? 'Image Set' : 'Empty' }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Edit/Create Modal -->
    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-gray-900/50 backdrop-blur-sm" @click="closeModal"></div>
      <div class="bg-white rounded-3xl shadow-2xl w-full max-w-xl relative overflow-hidden transition-all">
        <div class="p-6 border-b border-gray-100 flex justify-between items-center">
          <div>
            <h3 class="text-xl font-bold">{{ editingImage ? 'Edit Image' : 'Add Image' }}</h3>
            <p class="text-sm text-gray-500">Position {{ selectedPosition }}: {{ positionLabels[selectedPosition]?.name }}</p>
          </div>
          <button @click="closeModal" class="p-2 hover:bg-gray-50 rounded-full transition-colors">
            <XMarkIcon class="h-6 w-6 text-gray-400" />
          </button>
        </div>

        <form @submit.prevent="handleSubmit" class="p-6 overflow-y-auto max-h-[80vh] space-y-4">
          <!-- Position Info -->
          <div class="bg-blue-50 rounded-xl p-4 mb-4">
            <p class="text-sm text-blue-800">
              <strong>{{ positionLabels[selectedPosition]?.name }}</strong>: {{ positionLabels[selectedPosition]?.description }}
            </p>
          </div>

          <!-- Image Upload Area -->
          <div class="flex flex-col items-center">
            <div @click="fileInput?.click()"
              class="w-full aspect-video rounded-2xl border-2 border-dashed border-gray-200 hover:border-emerald-400 transition-colors cursor-pointer relative overflow-hidden flex items-center justify-center bg-gray-50">
              <img v-if="imagePreview" :src="imagePreview" class="w-full h-full object-cover" alt="Preview" />
              <div v-else class="text-center p-4">
                <CloudArrowUpIcon class="h-12 w-12 mx-auto text-gray-400 mb-2" />
                <p class="text-sm font-bold text-gray-400">Click to upload image</p>
                <p class="text-xs text-gray-400 mt-1">Recommended: 800x600px</p>
              </div>
              <input type="file" ref="fileInput" class="hidden" accept="image/*" @change="handleImageChange" />
            </div>
            <p v-if="imageFile" class="text-xs text-emerald-600 mt-2 font-bold">{{ imageFile.name }}</p>
          </div>

          <div>
            <label class="block text-sm font-bold text-gray-700 mb-1">Title</label>
            <input v-model="form.title" type="text" required
              class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:ring-2 focus:ring-emerald-600 outline-none transition-all"
              placeholder="e.g., Community Support" />
          </div>

          <div>
            <label class="block text-sm font-bold text-gray-700 mb-1">Alt Text (for accessibility)</label>
            <input v-model="form.alt_text" type="text"
              class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:ring-2 focus:ring-emerald-600 outline-none transition-all"
              placeholder="Describe the image for screen readers" />
          </div>

          <div class="flex items-center gap-2">
            <input type="checkbox" v-model="form.is_active" id="is_active" class="rounded text-emerald-600" />
            <label for="is_active" class="text-sm font-bold text-gray-700">Show on website</label>
          </div>

          <div class="pt-6 flex gap-4">
            <button type="button" @click="closeModal"
              class="flex-1 px-6 py-3 rounded-xl border border-gray-200 font-bold text-gray-600 hover:bg-gray-50 transition-all">
              Cancel
            </button>
            <button type="submit"
              class="flex-1 px-6 py-3 rounded-xl bg-emerald-600 text-white font-bold hover:bg-emerald-700 shadow-lg shadow-emerald-200 transition-all flex items-center justify-center"
              :disabled="saving || (!imageFile && !editingImage)">
              <div v-if="saving" class="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
              {{ editingImage ? 'Update Image' : 'Add Image' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { api } from '@/utils/api'
import { useToast } from 'vue-toastification'
import { PageHeader, StatsGrid, StatCard, LoadingState } from '@/components/admin'
import {
  PlusIcon,
  PhotoIcon,
  PencilIcon,
  TrashIcon,
  XMarkIcon,
  CloudArrowUpIcon,
  CheckCircleIcon,
  ExclamationCircleIcon
} from '@heroicons/vue/24/outline'

// Image Slot Component
const ImageSlot = {
  props: ['position', 'image', 'positionInfo'],
  emits: ['click'],
  template: `
    <div
      class="aspect-[4/3] bg-white rounded-2xl overflow-hidden shadow-sm border border-gray-200 cursor-pointer hover:shadow-lg hover:border-emerald-300 transition-all relative group"
      @click="$emit('click')"
    >
      <img
        v-if="image?.image_url"
        :src="image.image_url"
        :alt="image.title"
        class="w-full h-full object-cover"
      />
      <div v-else class="w-full h-full flex flex-col items-center justify-center text-gray-400 bg-gray-50">
        <svg class="w-8 h-8 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
        </svg>
        <span class="text-[10px] font-bold">Add Image</span>
      </div>
      <div class="absolute top-1 left-1 bg-black/60 text-white text-[10px] font-bold px-1.5 py-0.5 rounded">
        #{{ position }}
      </div>
      <div class="absolute inset-0 bg-emerald-600/20 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
        <span class="bg-white px-3 py-1 rounded-full text-xs font-bold text-emerald-600">{{ image ? 'Edit' : 'Add' }}</span>
      </div>
    </div>
  `
}

const toast = useToast()
const images = ref([])
const loading = ref(true)
const showModal = ref(false)
const editingImage = ref(null)
const selectedPosition = ref(1)
const saving = ref(false)
const imageFile = ref(null)
const imagePreview = ref(null)
const fileInput = ref(null)

const positionLabels = {
  1: { name: 'Left Top', description: 'Community image - shows community engagement' },
  2: { name: 'Left Middle', description: 'Helpline image - shows call center operations' },
  3: { name: 'Left Bottom', description: 'Family image - shows family support' },
  4: { name: 'Center Top-Left', description: 'Team Photo - main organizational photo' },
  5: { name: 'Center Top-Right', description: 'Happy Students - shows positive outcomes' },
  6: { name: 'Center Bottom-Left', description: 'Action shot - shows active work' },
  7: { name: 'Center Bottom-Right', description: 'Protection - shows child protection work' },
  8: { name: 'Right Top', description: 'Operations - shows diverse operations' },
  9: { name: 'Right Middle', description: 'Inclusive - shows inclusive community work' }
}

const stats = computed(() => {
  const filled = images.value.length
  return {
    filled,
    empty: 9 - filled
  }
})

const form = ref({
  title: '',
  alt_text: '',
  is_active: true
})

const getImageByPosition = (position) => {
  return images.value.find(img => img.position === position)
}

const fetchImages = async () => {
  loading.value = true
  try {
    const res = await api.whoWeAreImages.list()
    images.value = Array.isArray(res.data) ? res.data : (res.data.results || [])
    console.log('Fetched Who We Are images:', images.value.length)
  } catch (err) {
    console.error('Error fetching images:', err)
    toast.error('Failed to load images')
  } finally {
    loading.value = false
  }
}

const openCreateModal = () => {
  // Find first empty position
  for (let i = 1; i <= 9; i++) {
    if (!getImageByPosition(i)) {
      openEditModal(i)
      return
    }
  }
  toast.info('All positions are filled. Click on an existing image to edit it.')
}

const openEditModal = (position) => {
  selectedPosition.value = position
  const existingImage = getImageByPosition(position)
  editingImage.value = existingImage
  imageFile.value = null
  imagePreview.value = existingImage?.image_url || null
  form.value = existingImage ? {
    title: existingImage.title,
    alt_text: existingImage.alt_text || '',
    is_active: existingImage.is_active
  } : {
    title: '',
    alt_text: '',
    is_active: true
  }
  showModal.value = true
}

const handleImageChange = (e) => {
  const file = e.target.files[0]
  if (file) {
    if (imagePreview.value && imagePreview.value.startsWith('blob:')) {
      URL.revokeObjectURL(imagePreview.value)
    }
    imageFile.value = file
    imagePreview.value = URL.createObjectURL(file)
  }
}

const closeModal = () => {
  if (imagePreview.value && imagePreview.value.startsWith('blob:')) {
    URL.revokeObjectURL(imagePreview.value)
  }
  showModal.value = false
  editingImage.value = null
  imageFile.value = null
  imagePreview.value = null
}

const handleSubmit = async () => {
  saving.value = true
  try {
    const payload = {
      position: selectedPosition.value,
      title: form.value.title,
      alt_text: form.value.alt_text,
      is_active: form.value.is_active
    }

    if (imageFile.value) {
      payload.image = imageFile.value
    }

    if (editingImage.value) {
      await api.whoWeAreImages.update(selectedPosition.value, payload)
      toast.success('Image updated successfully')
    } else {
      await api.whoWeAreImages.create(payload)
      toast.success('Image added successfully')
    }

    await fetchImages()
    closeModal()
  } catch (err) {
    console.error('Error saving image:', err)
    toast.error(err.response?.data?.detail || 'Failed to save image')
  } finally {
    saving.value = false
  }
}

const confirmDelete = async (position) => {
  const image = getImageByPosition(position)
  if (!image) return

  if (confirm(`Are you sure you want to delete the image for "${positionLabels[position]?.name}"?`)) {
    try {
      await api.whoWeAreImages.delete(position)
      toast.success('Image removed')
      await fetchImages()
    } catch (err) {
      console.error('Error deleting image:', err)
      toast.error('Failed to delete image')
    }
  }
}

onMounted(fetchImages)
</script>
