<template>
  <div class="container mx-auto p-6">
    <div class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-3xl font-bold bg-gradient-to-r from-emerald-600 to-teal-600 bg-clip-text text-transparent">Organizational Team</h1>
        <p class="text-gray-500 mt-1">Manage public profiles for the members of Sauti 116.</p>
      </div>
      <button 
        @click="openCreateModal"
        class="bg-emerald-600 hover:bg-emerald-700 text-white px-4 py-2 rounded-lg flex items-center gap-2 transition-all shadow-lg shadow-emerald-200"
      >
        <PlusIcon class="h-5 w-5" />
        Add Member
      </button>
    </div>

    <!-- Team Grid -->
    <div v-if="loading" class="flex flex-col items-center justify-center py-20">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-emerald-600"></div>
      <p class="mt-4 text-gray-500">Loading team members...</p>
    </div>

    <div v-else-if="teamMembers.length === 0" class="bg-white rounded-3xl p-20 text-center border border-dashed border-gray-300">
      <div class="mx-auto w-20 h-20 bg-gray-50 rounded-full flex items-center justify-center mb-6 text-gray-300">
        <UserGroupIcon class="h-10 w-10" />
      </div>
      <h3 class="text-xl font-bold text-gray-900 mb-2">Build Your Team</h3>
      <p class="text-gray-500 max-w-sm mx-auto mb-8">Add members of your organization to show the faces behind the Sauti 116 mission.</p>
      <button @click="openCreateModal" class="bg-emerald-600 text-white px-6 py-2 rounded-full font-bold">Add First Member</button>
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div 
        v-for="member in teamMembers" 
        :key="member.id"
        class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group hover:shadow-xl transition-all"
      >
        <div class="aspect-[4/5] relative overflow-hidden bg-gray-100">
          <img 
            v-if="member.image" 
            :src="member.image" 
            :alt="member.name"
            class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
          />
          <div v-else class="w-full h-full flex items-center justify-center text-gray-300 bg-gray-50">
            <UserIcon class="w-20 h-20" />
          </div>
          
          <!-- Overlay controls -->
          <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-2">
            <button @click="editMember(member)" class="p-3 bg-white text-emerald-600 rounded-xl hover:scale-110 transition-transform shadow-lg">
              <PencilIcon class="h-6 w-6" />
            </button>
            <button @click="confirmDelete(member)" class="p-3 bg-white text-red-600 rounded-xl hover:scale-110 transition-transform shadow-lg">
              <TrashIcon class="h-6 w-6" />
            </button>
          </div>
        </div>
        
        <div class="p-5">
          <h3 class="font-bold text-gray-900 group-hover:text-emerald-600 transition-colors">{{ member.name }}</h3>
          <p class="text-emerald-600 text-sm font-semibold mb-3">{{ member.role }}</p>
          <p class="text-gray-500 text-xs line-clamp-2 leading-relaxed">{{ member.bio }}</p>
          
          <div class="mt-4 flex items-center justify-between">
            <span class="text-[10px] font-bold text-gray-300 uppercase">Order: {{ member.order }}</span>
            <span 
              class="w-2 h-2 rounded-full"
              :class="member.is_active ? 'bg-green-500' : 'bg-gray-300'"
              :title="member.is_active ? 'Public' : 'Hidden'"
            ></span>
          </div>
        </div>
      </div>
    </div>

    <!-- Edit/Create Modal -->
    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-gray-900/50 backdrop-blur-sm" @click="closeModal"></div>
      <div class="bg-white rounded-3xl shadow-2xl w-full max-w-xl relative overflow-hidden transition-all">
        <div class="p-6 border-b border-gray-100 flex justify-between items-center">
          <h3 class="text-xl font-bold">{{ editingMember ? 'Edit Team Member' : 'New Team Member' }}</h3>
          <button @click="closeModal" class="p-2 hover:bg-gray-50 rounded-full transition-colors">
            <XMarkIcon class="h-6 w-6 text-gray-400" />
          </button>
        </div>
        
        <form @submit.prevent="handleSubmit" class="p-6 overflow-y-auto max-h-[80vh] space-y-4">
          <!-- Image Upload Area -->
          <div class="flex flex-col items-center">
            <div 
              @click="$refs.fileInput.click()"
              class="w-40 h-40 rounded-3xl border-2 border-dashed border-gray-200 hover:border-emerald-400 transition-colors cursor-pointer relative overflow-hidden flex items-center justify-center bg-gray-50"
            >
              <img v-if="imagePreview" :src="imagePreview" class="w-full h-full object-cover" />
              <div v-else class="text-center p-4">
                <CloudArrowUpIcon class="h-10 w-10 mx-auto text-gray-400 mb-2" />
                <p class="text-xs font-bold text-gray-400 uppercase">Upload Photo</p>
              </div>
              <input 
                type="file" 
                ref="fileInput" 
                class="hidden" 
                accept="image/*"
                @change="handleImageChange"
              />
            </div>
            <p v-if="imageFile" class="text-xs text-emerald-600 mt-2 font-bold">{{ imageFile.name }}</p>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div class="col-span-2 sm:col-span-1">
              <label class="block text-sm font-bold text-gray-700 mb-1">Full Name</label>
              <input 
                v-model="form.name"
                type="text" 
                required
                class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:ring-2 focus:ring-emerald-600 outline-none transition-all"
                placeholder="John Doe"
              />
            </div>
            <div class="col-span-2 sm:col-span-1">
              <label class="block text-sm font-bold text-gray-700 mb-1">Role/Title</label>
              <input 
                v-model="form.role"
                type="text" 
                required
                class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:ring-2 focus:ring-emerald-600 outline-none transition-all"
                placeholder="Director of Operations"
              />
            </div>
          </div>

          <div>
            <label class="block text-sm font-bold text-gray-700 mb-1">Biography</label>
            <textarea 
              v-model="form.bio"
              rows="3"
              class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:ring-2 focus:ring-emerald-600 outline-none transition-all"
              placeholder="Short bio about the team member..."
            ></textarea>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-bold text-gray-700 mb-1">Display Order</label>
              <input 
                v-model="form.order"
                type="number" 
                class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:ring-2 focus:ring-emerald-600 outline-none transition-all"
              />
            </div>
            <div class="flex items-center gap-2 pt-6">
              <input type="checkbox" v-model="form.is_active" id="is_active" class="rounded text-emerald-600" />
              <label for="is_active" class="text-sm font-bold text-gray-700">Show on website</label>
            </div>
          </div>

          <div class="pt-6 flex gap-4">
            <button 
              type="button" 
              @click="closeModal"
              class="flex-1 px-6 py-3 rounded-xl border border-gray-200 font-bold text-gray-600 hover:bg-gray-50 transition-all"
            >
              Cancel
            </button>
            <button 
              type="submit" 
              class="flex-1 px-6 py-3 rounded-xl bg-emerald-600 text-white font-bold hover:bg-emerald-700 shadow-lg shadow-emerald-200 transition-all flex items-center justify-center"
              :disabled="saving"
            >
              <div v-if="saving" class="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
              {{ editingMember ? 'Update Profile' : 'Add Member' }}
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
  UserGroupIcon, 
  UserIcon, 
  PencilIcon, 
  TrashIcon, 
  XMarkIcon,
  CloudArrowUpIcon
} from '@heroicons/vue/24/outline'

const toast = useToast()
const teamMembers = ref([])
const loading = ref(true)
const showModal = ref(false)
const editingMember = ref(null)
const saving = ref(false)
const imageFile = ref(null)
const imagePreview = ref(null)

const form = ref({
  name: '',
  role: '',
  bio: '',
  order: 0,
  is_active: true
})

const fetchTeamMembers = async () => {
  loading.value = true
  try {
    const res = await api.teamMembers.list()
    teamMembers.value = Array.isArray(res.data) ? res.data : (res.data.results || [])
  } catch (err) {
    console.error('Error fetching team:', err)
    toast.error('Failed to load team members')
  } finally {
    loading.value = false
  }
}

const openCreateModal = () => {
  editingMember.value = null
  imageFile.value = null
  imagePreview.value = null
  form.value = {
    name: '',
    role: '',
    bio: '',
    order: teamMembers.value.length,
    is_active: true
  }
  showModal.value = true
}

const editMember = (member) => {
  editingMember.value = member
  imageFile.value = null
  imagePreview.value = member.image
  form.value = { ...member }
  showModal.value = true
}

const handleImageChange = (e) => {
  const file = e.target.files[0]
  if (file) {
    imageFile.value = file
    imagePreview.value = URL.createObjectURL(file)
  }
}

const closeModal = () => {
  showModal.value = false
  editingMember.value = null
  imageFile.value = null
  imagePreview.value = null
}

const handleSubmit = async () => {
  saving.value = true
  try {
    const payload = { ...form.value }
    if (imageFile.value) {
      payload.image = imageFile.value
    } else {
      // If we're updating and didn't pick a new image, don't send the string URL back
      delete payload.image
    }

    if (editingMember.value) {
      await api.teamMembers.update(editingMember.value.id, payload)
      toast.success('Team member updated')
    } else {
      await api.teamMembers.create(payload)
      toast.success('Team member added')
    }
    await fetchTeamMembers()
    closeModal()
  } catch (err) {
    console.error('Error saving team member:', err)
    toast.error('Failed to save team member')
  } finally {
    saving.value = false
  }
}

const confirmDelete = async (member) => {
  if (confirm(`Are you sure you want to delete ${member.name}?`)) {
    try {
      await api.teamMembers.delete(member.id)
      toast.success('Team member removed')
      await fetchTeamMembers()
    } catch (err) {
      console.error('Error deleting member:', err)
      toast.error('Failed to delete member')
    }
  }
}

onMounted(fetchTeamMembers)
</script>
