<template>
  <div class="p-6">
    <!-- Page Header -->
    <PageHeader title="Core Values" description="Manage the foundational principles displayed on the About page."
      action-label="Add Core Value" :action-icon="PlusIcon" @action="openCreateModal" />

    <!-- Stats -->
    <StatsGrid>
      <StatCard label="Total Values" :value="stats.total" :icon="HeartIcon" color="blue" />
      <StatCard label="Active" :value="stats.active" :icon="CheckCircleIcon" color="green" />
      <StatCard label="Hidden" :value="stats.hidden" :icon="EyeSlashIcon" color="gray" />
    </StatsGrid>

    <!-- Loading State -->
    <LoadingState v-if="loading" message="Loading core values..." />

    <!-- Empty State -->
    <EmptyState v-else-if="coreValues.length === 0" title="No Core Values Yet"
      message="Start by adding your organization's core values that define your mission and identity."
      action-label="Add Your First Value" :action-icon="PlusIcon" :icon="HeartIcon" @action="openCreateModal" />

    <!-- Values Grid -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="value in coreValues" :key="value.id"
        class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group hover:shadow-lg transition-all">
        <div class="h-2" :class="`bg-${value.color_from || 'blue-500'}`"></div>
        <div class="p-6">
          <div class="flex justify-between items-start mb-4">
            <div
              class="p-3 rounded-xl bg-gray-50 text-gray-600 group-hover:bg-blue-50 group-hover:text-blue-600 transition-colors">
              <span v-if="value.icon" v-html="renderIcon(value.icon)"></span>
              <HeartIcon v-else class="h-6 w-6" />
            </div>
            <div class="flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
              <button @click="editValue(value)"
                class="p-2 hover:bg-gray-50 rounded-lg text-gray-400 hover:text-blue-600 transition-colors">
                <PencilIcon class="h-5 w-5" />
              </button>
              <button @click="confirmDelete(value)"
                class="p-2 hover:bg-red-50 rounded-lg text-gray-400 hover:text-red-600 transition-colors">
                <TrashIcon class="h-5 w-5" />
              </button>
            </div>
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-2">{{ value.title }}</h3>
          <p class="text-gray-600 text-sm line-clamp-3 mb-4">{{ value.description }}</p>
          <div class="flex items-center justify-between pt-4 border-t border-gray-50 mt-auto">
            <span class="text-xs font-bold uppercase tracking-wider text-gray-400">Order: {{ value.order }}</span>
            <span class="flex items-center gap-1.5 text-xs font-bold px-2 py-1 rounded-md"
              :class="value.is_active ? 'bg-green-50 text-green-600' : 'bg-gray-100 text-gray-500'">
              <span class="w-1.5 h-1.5 rounded-full" :class="value.is_active ? 'bg-green-500' : 'bg-gray-400'"></span>
              {{ value.is_active ? 'Active' : 'Hidden' }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Edit/Create Modal -->
    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-gray-900/50 backdrop-blur-sm" @click="closeModal"></div>
      <div class="bg-white rounded-3xl shadow-2xl w-full max-w-lg relative overflow-hidden transition-all">
        <div class="p-6 border-b border-gray-100 flex justify-between items-center">
          <h3 class="text-xl font-bold">{{ editingItem ? 'Edit Core Value' : 'Add Core Value' }}</h3>
          <button @click="closeModal" class="p-2 hover:bg-gray-50 rounded-full transition-colors">
            <XMarkIcon class="h-6 w-6 text-gray-400" />
          </button>
        </div>

        <form @submit.prevent="handleSubmit" class="p-6 space-y-4">
          <div>
            <label class="block text-sm font-bold text-gray-700 mb-1">Title</label>
            <input v-model="form.title" type="text" required
              class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:ring-2 focus:ring-blue-600 outline-none transition-all"
              placeholder="e.g., Confidentiality" />
          </div>

          <div>
            <label class="block text-sm font-bold text-gray-700 mb-1">Icon Name/Path</label>
            <input v-model="form.icon" type="text"
              class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:ring-2 focus:ring-blue-600 outline-none transition-all"
              placeholder="e.g., heart, shield, scale" />
          </div>

          <div>
            <label class="block text-sm font-bold text-gray-700 mb-1">Description</label>
            <textarea v-model="form.description" required rows="4"
              class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:ring-2 focus:ring-blue-600 outline-none transition-all"
              placeholder="Describe this core value..."></textarea>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-bold text-gray-700 mb-1">Order</label>
              <input v-model="form.order" type="number"
                class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:ring-2 focus:ring-blue-600 outline-none transition-all" />
            </div>
            <div class="flex items-end pb-2">
              <label class="flex items-center gap-2 cursor-pointer group">
                <input type="checkbox" v-model="form.is_active" class="hidden" />
                <div class="w-12 h-6 rounded-full relative transition-colors duration-200"
                  :class="form.is_active ? 'bg-blue-600' : 'bg-gray-200'">
                  <div class="absolute top-1 left-1 bg-white w-4 h-4 rounded-full transition-transform duration-200"
                    :style="form.is_active ? 'transform: translateX(24px)' : ''"></div>
                </div>
                <span class="text-sm font-bold text-gray-700">Live Item</span>
              </label>
            </div>
          </div>

          <div class="pt-4 flex gap-4">
            <button type="button" @click="closeModal"
              class="flex-1 px-6 py-3 rounded-xl border border-gray-200 font-bold text-gray-600 hover:bg-gray-50 transition-all">
              Cancel
            </button>
            <button type="submit"
              class="flex-1 px-6 py-3 rounded-xl bg-blue-600 text-white font-bold hover:bg-blue-700 shadow-lg shadow-blue-200 transition-all flex items-center justify-center"
              :disabled="saving">
              <div v-if="saving" class="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
              {{ editingItem ? 'Save Changes' : 'Create Value' }}
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
  import { PageHeader, StatsGrid, StatCard, LoadingState, EmptyState } from '@/components/admin'
  import {
    PlusIcon,
    HeartIcon,
    EyeIcon,
    PencilIcon,
    TrashIcon,
    XMarkIcon,
    CheckCircleIcon,
    EyeSlashIcon
  } from '@heroicons/vue/24/outline'

  const toast = useToast()
  const coreValues = ref([])
  const loading = ref(true)
  const showModal = ref(false)
  const editingItem = ref(null)
  const saving = ref(false)

  const stats = computed(() => {
    const values = coreValues.value || []
    const total = values.length
    const active = values.filter(v => v.is_active).length
    const hidden = total - active

    return {
      total,
      active,
      hidden
    }
  })

  const form = ref({
    title: '',
    description: '',
    icon: '',
    order: 0,
    is_active: true,
    color_from: 'blue-500',
    color_to: 'blue-600',
    border_color: 'blue-100'
  })

  const fetchCoreValues = async () => {
    loading.value = true
    try {
      const res = await api.coreValues.list()
      // Handle paginated or direct array response
      coreValues.value = Array.isArray(res.data) ? res.data : (res.data.results || [])
    } catch (err) {
      console.error('Error fetching core values:', err)
      toast.error('Failed to load core values')
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
      order: coreValues.value.length,
      is_active: true,
      color_from: 'blue-500',
      color_to: 'blue-600',
      border_color: 'blue-100'
    }
    showModal.value = true
  }

  const editValue = (value) => {
    editingItem.value = value
    form.value = { ...value }
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
        await api.coreValues.update(editingItem.value.id, form.value)
        toast.success('Core value updated')
      } else {
        await api.coreValues.create(form.value)
        toast.success('Core value created')
      }
      await fetchCoreValues()
      closeModal()
    } catch (err) {
      console.error('Error saving core value:', err)
      toast.error('Failed to save core value')
    } finally {
      saving.value = false
    }
  }

  const confirmDelete = async (value) => {
    if (confirm(`Are you sure you want to delete "${value.title}"?`)) {
      try {
        await api.coreValues.delete(value.id)
        toast.success('Core value deleted')
        await fetchCoreValues()
      } catch (err) {
        console.error('Error deleting core value:', err)
        toast.error('Failed to delete core value')
      }
    }
  }

  const renderIcon = (iconName) => {
    // Simple check for SVG or icon name
    if (iconName && iconName.startsWith('<svg')) return iconName
    return `<span class="text-xs uppercase font-bold">${iconName || ''}</span>`
  }

  onMounted(fetchCoreValues)
</script>

<style scoped>
  .line-clamp-3 {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
</style>
