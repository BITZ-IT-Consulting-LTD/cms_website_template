<template>
  <div class="p-6">
    <!-- Page Header -->
    <PageHeader title="Timeline Events" description="Manage the timeline events of Sauti 116." action-label="Add Event"
      :action-icon="PlusIcon" @action="openCreateModal" />

    <!-- Stats -->
    <StatsGrid>
      <StatCard label="Total Events" :value="stats.total" :icon="CalendarDaysIcon" color="blue" />
      <StatCard label="Visible Events" :value="stats.visible" :icon="CheckCircleIcon" color="green" />
      <StatCard label="Hidden Events" :value="stats.hidden" :icon="EyeSlashIcon" color="gray" />
    </StatsGrid>

    <!-- Loading State -->
    <LoadingState v-if="loading" message="Loading timeline events..." />

    <!-- Empty State -->
    <EmptyState v-else-if="timelineEvents.length === 0" title="No Events Found"
      message="Create your first timeline event to get started." action-label="Add Event" :action-icon="PlusIcon"
      :icon="ClockIcon" @action="openCreateModal" />

    <!-- Timeline Grid -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="event in timelineEvents" :key="event.id"
        class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden group hover:shadow-xl transition-all relative">
        <div class="p-6">
          <div class="flex justify-between items-start mb-4">
            <span
              class="px-3 py-1 bg-indigo-50 text-indigo-700 rounded-full text-sm font-bold border border-indigo-100">
              {{ event.year }}
            </span>
            <div class="flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
              <button @click="editEvent(event)" class="text-gray-400 hover:text-indigo-600 transition-colors">
                <PencilIcon class="h-5 w-5" />
              </button>
              <button @click="deleteEvent(event.id)" class="text-gray-400 hover:text-red-600 transition-colors">
                <TrashIcon class="h-5 w-5" />
              </button>
            </div>
          </div>

          <h3 class="font-bold text-gray-900 text-lg mb-2">{{ event.title }}</h3>
          <p class="text-gray-500 text-sm line-clamp-3 mb-4 leading-relaxed">{{ event.description }}</p>

          <div class="flex items-center justify-between pt-4 border-t border-gray-50">
            <span class="text-xs font-medium text-gray-400 uppercase tracking-wider">Order: {{ event.order }}</span>
            <span class="flex items-center gap-1.5 text-xs font-semibold px-2 py-1 rounded-md"
              :class="event.is_visible ? 'bg-green-50 text-green-700' : 'bg-gray-100 text-gray-600'">
              <span class="w-1.5 h-1.5 rounded-full" :class="event.is_visible ? 'bg-green-500' : 'bg-gray-400'"></span>
              {{ event.is_visible ? 'Visible' : 'Hidden' }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Create/Edit Modal -->
    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-gray-900/50 backdrop-blur-sm" @click="closeModal"></div>
      <div class="bg-white rounded-3xl shadow-2xl w-full max-w-lg relative overflow-hidden transition-all transform">
        <div class="p-6 border-b border-gray-100 flex justify-between items-center bg-gray-50/50">
          <h3 class="text-xl font-bold text-gray-900">{{ editingEvent ? 'Edit Event' : 'New Event' }}</h3>
          <button @click="closeModal"
            class="p-2 hover:bg-white rounded-full transition-all shadow-sm text-gray-400 hover:text-gray-600">
            <XMarkIcon class="h-6 w-6" />
          </button>
        </div>

        <form @submit.prevent="saveEvent" class="p-6 space-y-5">
          <div class="grid grid-cols-2 gap-5">
            <div>
              <label class="block text-sm font-bold text-gray-700 mb-1.5">Year</label>
              <input v-model="form.year" type="text" required placeholder="2024"
                class="w-full px-4 py-2.5 rounded-xl border border-gray-200 focus:ring-2 focus:ring-indigo-600 focus:border-indigo-600 outline-none transition-all" />
            </div>
            <div>
              <label class="block text-sm font-bold text-gray-700 mb-1.5">Sort Order</label>
              <input v-model="form.order" type="number" required
                class="w-full px-4 py-2.5 rounded-xl border border-gray-200 focus:ring-2 focus:ring-indigo-600 focus:border-indigo-600 outline-none transition-all" />
            </div>
          </div>

          <div>
            <label class="block text-sm font-bold text-gray-700 mb-1.5">Title</label>
            <input v-model="form.title" type="text" required placeholder="Event title..."
              class="w-full px-4 py-2.5 rounded-xl border border-gray-200 focus:ring-2 focus:ring-indigo-600 focus:border-indigo-600 outline-none transition-all" />
          </div>

          <div>
            <label class="block text-sm font-bold text-gray-700 mb-1.5">Description</label>
            <textarea v-model="form.description" rows="4" required placeholder="Describe what happened..."
              class="w-full px-4 py-2.5 rounded-xl border border-gray-200 focus:ring-2 focus:ring-indigo-600 focus:border-indigo-600 outline-none transition-all resize-none"></textarea>
          </div>

          <div class="flex items-center gap-3 p-3 bg-gray-50 rounded-xl border border-gray-100">
            <input type="checkbox" id="is_visible" v-model="form.is_visible"
              class="w-5 h-5 rounded text-indigo-600 focus:ring-indigo-600 border-gray-300" />
            <label for="is_visible" class="text-sm font-semibold text-gray-700 cursor-pointer select-none">
              Visible on website
            </label>
          </div>

          <div class="pt-4 flex gap-3">
            <button type="button" @click="closeModal"
              class="flex-1 px-6 py-3 rounded-xl border border-gray-200 font-bold text-gray-600 hover:bg-gray-50 transition-all focus:ring-2 focus:ring-gray-200 focus:outline-none">
              Cancel
            </button>
            <button type="submit" :disabled="saving"
              class="flex-1 px-6 py-3 rounded-xl bg-indigo-600 text-white font-bold hover:bg-indigo-700 shadow-lg shadow-indigo-200 transition-all flex items-center justify-center focus:ring-2 focus:ring-indigo-600 focus:ring-offset-2 focus:outline-none">
              <div v-if="saving" class="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
              {{ editingEvent ? 'Update Event' : 'Create Event' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue';
  import { api } from '@/utils/api';
  import { useToast } from 'vue-toastification';
  import { PageHeader, StatsGrid, StatCard, LoadingState, EmptyState } from '@/components/admin';
  import {
    PlusIcon,
    ClockIcon,
    CheckCircleIcon,
    EyeSlashIcon,
    PencilIcon,
    TrashIcon,
    XMarkIcon,
    CalendarDaysIcon
  } from '@heroicons/vue/24/outline';

  const timelineEvents = ref([]);
  const loading = ref(true);
  const toast = useToast();
  const showModal = ref(false);
  const editingEvent = ref(null);
  const saving = ref(false);

  const form = ref({
    year: '',
    title: '',
    description: '',
    order: 0,
    is_visible: true,
  });

  const stats = computed(() => {
    const events = timelineEvents.value || [];
    const total = events.length;
    const visible = events.filter(e => e.is_visible).length;
    const hidden = total - visible;

    return {
      total,
      visible,
      hidden
    };
  });

  const fetchEvents = async () => {
    loading.value = true;
    try {
      const response = await api.timeline.list();
      timelineEvents.value = response.data.results || response.data;
    } catch (error) {
      console.error('Error fetching timeline events:', error);
      toast.error('Failed to load timeline events');
    } finally {
      loading.value = false;
    }
  };

  const openCreateModal = () => {
    editingEvent.value = null;
    form.value = {
      year: '',
      title: '',
      description: '',
      order: timelineEvents.value.length + 1,
      is_visible: true,
    };
    showModal.value = true;
  };

  const closeModal = () => {
    showModal.value = false;
    editingEvent.value = null;
    form.value = {
      year: '',
      title: '',
      description: '',
      order: 0,
      is_visible: true,
    };
  };

  const saveEvent = async () => {
    saving.value = true;
    try {
      if (editingEvent.value) {
        await api.timeline.update(editingEvent.value.id, form.value);
        toast.success('Timeline event updated successfully');
      } else {
        await api.timeline.create(form.value);
        toast.success('Timeline event created successfully');
      }
      await fetchEvents();
      closeModal();
    } catch (error) {
      console.error('Error saving event:', error);
      toast.error(error.response?.data?.detail || 'Error saving event');
    } finally {
      saving.value = false;
    }
  };

  const editEvent = (event) => {
    editingEvent.value = event;
    form.value = { ...event };
    showModal.value = true;
  };

  const deleteEvent = async (id) => {
    if (confirm('Are you sure you want to delete this event?')) {
      try {
        await api.timeline.delete(id);
        toast.success('Timeline event deleted successfully');
        await fetchEvents();
      } catch (error) {
        console.error('Error deleting event:', error);
        toast.error('Failed to delete timeline event');
      }
    }
  };

  onMounted(fetchEvents);
</script>

<style scoped>
  /* Add Tailwind CSS or custom styles here */
</style>
