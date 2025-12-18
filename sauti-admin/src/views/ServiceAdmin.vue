<template>
  <div class="container mx-auto p-6">
    <h1 class="text-3xl font-bold mb-6">Manage Services</h1>

    <!-- Create/Edit Form -->
    <div class="bg-white shadow-md rounded-lg p-6 mb-8">
      <h2 class="text-2xl font-semibold mb-4">{{ editingService ? 'Edit Service' : 'Create New Service' }}</h2>
      <form @submit.prevent="saveService">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label for="title" class="block text-sm font-medium text-gray-700">Title</label>
            <input type="text" id="title" v-model="form.title" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" required>
          </div>
          <div>
            <label for="icon" class="block text-sm font-medium text-gray-700">Icon Name (e.g., 'phone', 'walk')</label>
            <input type="text" id="icon" v-model="form.icon" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
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
            {{ editingService ? 'Update Service' : 'Create Service' }}
          </button>
          <button type="button" @click="cancelEdit" v-if="editingService" class="ml-3 inline-flex justify-center py-2 px-4 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Cancel
          </button>
        </div>
      </form>
    </div>

    <!-- Services List -->
    <div class="bg-white shadow-md rounded-lg p-6">
      <h2 class="text-2xl font-semibold mb-4">Existing Services</h2>
      <div v-if="loading" class="text-center py-4">Loading services...</div>
      <div v-else-if="services.length === 0" class="text-center py-4">No services found.</div>
      <div v-else class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Title</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Description</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Icon</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Order</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Visible</th>
              <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="service in services" :key="service.id">
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ service.title }}</td>
              <td class="px-6 py-4 text-sm text-gray-500 max-w-xs truncate">{{ service.description }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ service.icon }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ service.order }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                <span :class="{'px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800': service.is_visible, 'px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800': !service.is_visible}">
                  {{ service.is_visible ? 'Yes' : 'No' }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <button @click="editService(service)" class="text-indigo-600 hover:text-indigo-900 mr-4">Edit</button>
                <button @click="deleteService(service.id)" class="text-red-600 hover:text-red-900">Delete</button>
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

const services = ref([]);
const loading = ref(true);
const form = ref({
  title: '',
  description: '',
  icon: '',
  order: 0,
  is_visible: true,
});
const editingService = ref(null); // Stores the service being edited

const API_URL = '/api/services/'; // API endpoint for services

const fetchServices = async () => {
  loading.value = true;
  try {
    const response = await axios.get(API_URL);
    services.value = response.data.results; // Correctly access the results array
  } catch (error) {
    console.error('Error fetching services:', error);
  } finally {
    loading.value = false;
  }
};

const saveService = async () => {
  try {
    if (editingService.value) {
      // Update existing service
      await axios.put(`${API_URL}${editingService.value.id}/`, form.value);
      console.log('Service updated successfully!');
    } else {
      // Create new service
      await axios.post(API_URL, form.value);
      console.log('Service created successfully!');
    }
    resetForm();
    await fetchServices(); // Refresh the list
  } catch (error) {
    console.error('Error saving service:', error);
  }
};

const editService = (service) => {
  editingService.value = service;
  form.value = { ...service }; // Populate form with service data
};

const cancelEdit = () => {
  resetForm();
  editingService.value = null;
};

const deleteService = async (id) => {
  if (confirm('Are you sure you want to delete this service?')) {
    try {
      await axios.delete(`${API_URL}${id}/`);
      console.log('Service deleted successfully!');
      await fetchServices(); // Refresh the list
    } catch (error) {
      console.error('Error deleting service:', error);
    }
  }
};

const resetForm = () => {
  form.value = {
    title: '',
    description: '',
    icon: '',
    order: 0,
    is_visible: true,
  };
};

onMounted(fetchServices);
</script>

<style scoped>
/* Add Tailwind CSS or custom styles here */
</style>
