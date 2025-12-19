<template>
  <div class="container mx-auto p-6">
    <div class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-3xl font-bold bg-gradient-to-r from-orange-600 to-red-600 bg-clip-text text-transparent">Protection Approach</h1>
        <p class="text-gray-500 mt-1">Define the steps and methodology for protecting the vulnerable.</p>
      </div>
      <button 
        @click="openCreateModal"
        class="bg-orange-600 hover:bg-orange-700 text-white px-4 py-2 rounded-lg flex items-center gap-2 transition-all shadow-lg shadow-orange-100"
      >
        <PlusIcon class="h-5 w-5" />
        Add Approach Step
      </button>
    </div>

    <!-- Approaches Table/List -->
    <div v-if="loading" class="flex flex-col items-center justify-center py-20">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-orange-600"></div>
      <p class="mt-4 text-gray-500">Loading approaches...</p>
    </div>

    <div v-else-if="approaches.length === 0" class="bg-white rounded-3xl p-20 text-center border border-dashed border-gray-300">
      <div class="mx-auto w-20 h-20 bg-gray-50 rounded-full flex items-center justify-center mb-6 text-gray-300">
        <ShieldCheckIcon class="h-10 w-10" />
      </div>
      <h3 class="text-xl font-bold text-gray-900 mb-2">No Protection Steps Defined</h3>
      <p class="text-gray-500 max-w-sm mx-auto mb-8">Outline the organization's protection strategy and systematic steps taken for interventions.</p>
      <button @click="openCreateModal" class="bg-orange-600 text-white px-6 py-2 rounded-full font-bold">Define First Step</button>
    </div>

    <div v-else class="space-y-4">
      <div 
        v-for="(approach, index) in approaches" 
        :key="approach.id"
        class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6 flex flex-col md:flex-row items-center gap-6 group hover:border-orange-200 transition-all"
      >
        <div class="w-16 h-16 flex-shrink-0 bg-orange-50 text-orange-600 rounded-2xl flex items-center justify-center font-bold text-2xl border border-orange-100 group-hover:bg-orange-600 group-hover:text-white transition-all">
          {{ index + 1 }}
        </div>
        
        <div class="flex-1 text-center md:text-left">
          <h3 class="text-xl font-bold text-gray-900 mb-1">{{ approach.title }}</h3>
          <p class="text-gray-600 line-clamp-2">{{ approach.description }}</p>
        </div>

        <div class="flex items-center gap-4">
          <span class="text-xs font-bold px-3 py-1 bg-gray-100 text-gray-400 rounded-full uppercase">Order: {{ approach.order }}</span>
          <div class="flex gap-2">
            <button @click="editApproach(approach)" class="p-2 hover:bg-orange-50 rounded-lg text-gray-400 hover:text-orange-600 transition-colors">
              <PencilIcon class="h-5 w-5" />
            </button>
            <button @click="confirmDelete(approach)" class="p-2 hover:bg-red-50 rounded-lg text-gray-400 hover:text-red-600 transition-colors">
              <TrashIcon class="h-5 w-5" />
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Edit/Create Modal -->
    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-gray-900/50 backdrop-blur-sm" @click="closeModal"></div>
      <div class="bg-white rounded-3xl shadow-2xl w-full max-w-lg relative overflow-hidden transition-all">
        <div class="p-6 border-b border-gray-100 flex justify-between items-center">
          <h3 class="text-xl font-bold">{{ editingItem ? 'Edit Step' : 'Add Protection Step' }}</h3>
          <button @click="closeModal" class="p-2 hover:bg-gray-50 rounded-full transition-colors">
            <XMarkIcon class="h-6 w-6 text-gray-400" />
          </button>
        </div>
        
        <form @submit.prevent="handleSubmit" class="p-6 space-y-4">
          <div>
            <label class="block text-sm font-bold text-gray-700 mb-1">Title</label>
            <input 
              v-model="form.title"
              type="text" 
              required
              class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:ring-2 focus:ring-orange-600 outline-none transition-all"
              placeholder="e.g., Initial Contact & Triage"
            />
          </div>

          <div>
            <label class="block text-sm font-bold text-gray-700 mb-1">Methodology Icon</label>
            <input 
              v-model="form.icon"
              type="text" 
              class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:ring-2 focus:ring-orange-600 outline-none transition-all"
              placeholder="e.g., phone, clipboard, user-group"
            />
          </div>

          <div>
            <label class="block text-sm font-bold text-gray-700 mb-1">Description</label>
            <textarea 
              v-model="form.description"
              required
              rows="4"
              class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:ring-2 focus:ring-orange-600 outline-none transition-all"
              placeholder="Detailed description of what happens in this step..."
            ></textarea>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-bold text-gray-700 mb-1">Execution Order</label>
              <input 
                v-model="form.order"
                type="number" 
                class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:ring-2 focus:ring-orange-600 outline-none transition-all"
              />
            </div>
            <div class="flex items-center gap-2 pt-6">
              <input type="checkbox" v-model="form.is_active" id="is_active" class="rounded text-orange-600" />
              <label for="is_active" class="text-sm font-bold text-gray-700">Step is Active</label>
            </div>
          </div>

          <div class="pt-4 flex gap-4">
            <button 
              type="button" 
              @click="closeModal"
              class="flex-1 px-6 py-3 rounded-xl border border-gray-200 font-bold text-gray-600 hover:bg-gray-50 transition-all"
            >
              Cancel
            </button>
            <button 
              type="submit" 
              class="flex-1 px-6 py-3 rounded-xl bg-orange-600 text-white font-bold hover:bg-orange-700 shadow-lg shadow-orange-200 transition-all flex items-center justify-center"
              :disabled="saving"
            >
              <div v-if="saving" class="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
              {{ editingItem ? 'Save Step' : 'Create Step' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { api } from '@/utils/api'
import { useToast } from 'vue-toastification'
import { 
  PlusIcon, 
  ShieldCheckIcon,
  PencilIcon, 
  TrashIcon, 
  XMarkIcon 
} from '@heroicons/vue/24/outline'

const toast = useToast()
const approaches = ref([])
const loading = ref(true)
const showModal = ref(false)
const editingItem = ref(null)
const saving = ref(false)

const form = ref({
  title: '',
  description: '',
  icon: '',
  order: 0,
  is_active: true,
  color: 'orange'
})

const fetchApproaches = async () => {
  loading.value = true
  try {
    const res = await api.protectionApproaches.list()
    const data = Array.isArray(res.data) ? res.data : (res.data.results || [])
    approaches.value = data.sort((a, b) => a.order - b.order)
  } catch (err) {
    console.error('Error fetching approaches:', err)
    toast.error('Failed to load protection approaches')
  } finally {
    loading.value = false
  }
}

const openCreateModal = () => {
  editingItem.value = null
  form.value = {
    title: '',
    description: '',
    icon: '',
    order: approaches.value.length + 1,
    is_active: true,
    color: 'orange'
  }
  showModal.value = true
}

const editApproach = (approach) => {
  editingItem.value = approach
  form.value = { ...approach }
  showModal.value = true
}

const closeModal = () => {
  showModal.value = false
  editingItem.value = null
}

const handleSubmit = async () => {
  saving.value = true
  try {
    if (editingItem.value) {
      await api.protectionApproaches.update(editingItem.value.id, form.value)
      toast.success('Approach updated')
    } else {
      await api.protectionApproaches.create(form.value)
      toast.success('Approach created')
    }
    await fetchApproaches()
    closeModal()
  } catch (err) {
    console.error('Error saving approach:', err)
    toast.error('Failed to save approach')
  } finally {
    saving.value = false
  }
}

const confirmDelete = async (approach) => {
  if (confirm(`Are you sure you want to delete "${approach.title}"?`)) {
    try {
      await api.protectionApproaches.delete(approach.id)
      toast.success('Approach deleted')
      await fetchApproaches()
    } catch (err) {
      console.error('Error deleting approach:', err)
      toast.error('Failed to delete approach')
    }
  }
}

onMounted(fetchApproaches)
</script>
