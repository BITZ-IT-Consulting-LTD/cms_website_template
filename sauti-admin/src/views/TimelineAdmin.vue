<template>
  <div class="container mx-auto p-6">
    <h1 class="text-3xl font-bold mb-6">Manage Timeline Events</h1>

    <!-- Create/Edit Form -->
    <div class="bg-white shadow-md rounded-lg p-6 mb-8">
      <h2 class="text-2xl font-semibold mb-4">{{ editingEvent ? 'Edit Timeline Event' : 'Create New Timeline Event' }}</h2>
      <form @submit.prevent="saveEvent">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label for="year" class="block text-sm font-medium text-gray-700">Year/Date</label>
            <input type="text" id="year" v-model="form.year" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" required>
          </div>
          <div>
            <label for="title" class="block text-sm font-medium text-gray-700">Title</label>
            <input type="text" id="title" v-model="form.title" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" required>
          </div>
        </div>
        <div class="mt-4">
          <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
          <textarea id="description" v-model="form.description" rows="3" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" required></textarea>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
          <div>
            <label for="order" class="block text-sm font-medium text-gray-700">Order</label>
            <input type="number" id="order" v-model="form.order" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" required>
          </div>
          <div class="flex items-center mt-5">
            <input type="checkbox" id="is_visible" v-model="form.is_visible" class="h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500">
            <label for="is_visible" class="ml-2 block text-sm text-gray-900">Is Visible</label>
          </div>
        </div>
        <div class="mt-6">
          <button type="submit" class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            {{ editingEvent ? 'Update Event' : 'Create Event' }}
          </button>
          <button type="button" @click="cancelEdit" v-if="editingEvent" class="ml-3 inline-flex justify-center py-2 px-4 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Cancel
          </button>
        </div>
      </form>
    </div>

    <!-- Timeline Events List -->
    <div class="bg-white shadow-md rounded-lg p-6">
      <h2 class="text-2xl font-semibold mb-4">Existing Timeline Events</h2>
      <div v-if="loading" class="text-center py-4">Loading events...</div>
      <div v-else-if="timelineEvents.length === 0" class="text-center py-4">No timeline events found.</div>
      <div v-else class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Year</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Title</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Description</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Order</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Visible</th>
              <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="event in timelineEvents" :key="event.id">
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ event.year }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ event.title }}</td>
              <td class="px-6 py-4 text-sm text-gray-500 max-w-xs truncate">{{ event.description }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ event.order }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                <span :class="{'px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800': event.is_visible, 'px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800': !event.is_visible}">
                  {{ event.is_visible ? 'Yes' : 'No' }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <button @click="editEvent(event)" class="text-indigo-600 hover:text-indigo-900 mr-4">Edit</button>
                <button @click="deleteEvent(event.id)" class="text-red-600 hover:text-red-900">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const timelineEvents = ref([]);
const loading = ref(true);
const form = ref({
  year: '',
  title: '',
  description: '',
  order: 0,
  is_visible: true,
});
const editingEvent = ref(null); // Stores the event being edited

const API_URL = '/api/timeline/';

const fetchEvents = async () => {
  loading.value = true;
  try {
    const response = await axios.get(API_URL);
    timelineEvents.value = response.data.results;
  } catch (error) {
    console.error('Error fetching timeline events:', error);
  } finally {
    loading.value = false;
  }
};

const saveEvent = async () => {
  try {
    if (editingEvent.value) {
      // Update existing event
      await axios.put(`${API_URL}${editingEvent.value.id}/`, form.value);
      console.log('Event updated successfully!');
    } else {
      // Create new event
      await axios.post(API_URL, form.value);
      console.log('Event created successfully!');
    }
    resetForm();
    await fetchEvents(); // Refresh the list
  } catch (error) {
    console.error('Error saving event:', error);
  }
};

const editEvent = (event) => {
  editingEvent.value = event;
  form.value = { ...event }; // Populate form with event data
};

const cancelEdit = () => {
  resetForm();
  editingEvent.value = null;
};

const deleteEvent = async (id) => {
  if (confirm('Are you sure you want to delete this event?')) {
    try {
      await axios.delete(`${API_URL}${id}/`);
      console.log('Event deleted successfully!');
      await fetchEvents(); // Refresh the list
    } catch (error) {
      console.error('Error deleting event:', error);
    }
  }
};

const resetForm = () => {
  form.value = {
    year: '',
    title: '',
    description: '',
    order: 0,
    is_visible: true,
  };
};

onMounted(fetchEvents);
</script>

<style scoped>
/* Add Tailwind CSS or custom styles here */
</style>
