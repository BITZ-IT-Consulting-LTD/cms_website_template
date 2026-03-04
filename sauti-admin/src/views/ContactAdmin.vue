<template>
  <div class="container mx-auto p-6">
    <h1 class="text-3xl font-bold mb-6">Manage Contact Information</h1>

    <!-- Create/Edit Form -->
    <div class="bg-white shadow-md rounded-lg p-6 mb-8">
      <h2 class="text-2xl font-semibold mb-4">{{ editingContact ? 'Edit Contact Item' : 'Create New Contact Item' }}</h2>
      <form @submit.prevent="saveContact">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
            <input type="text" id="name" v-model="form.name" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" required>
          </div>
          <div>
            <label for="value" class="block text-sm font-medium text-gray-700">Value</label>
            <input type="text" id="value" v-model="form.value" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" required>
          </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
          <div>
            <label for="type" class="block text-sm font-medium text-gray-700">Type</label>
            <select id="type" v-model="form.type" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" required>
              <option value="phone">Phone Number</option>
              <option value="email">Email Address</option>
              <option value="location">Physical Location</option>
              <option value="social">Social Media Link</option>
              <option value="other">Other</option>
            </select>
          </div>
          <div>
            <label for="icon" class="block text-sm font-medium text-gray-700">Icon Name (e.g., 'phone', 'envelope')</label>
            <input type="text" id="icon" v-model="form.icon" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
          </div>
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
            {{ editingContact ? 'Update Contact' : 'Create Contact' }}
          </button>
          <button type="button" @click="cancelEdit" v-if="editingContact" class="ml-3 inline-flex justify-center py-2 px-4 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Cancel
          </button>
        </div>
      </form>
    </div>

    <!-- Contact List -->
    <div class="bg-white shadow-md rounded-lg p-6">
      <h2 class="text-2xl font-semibold mb-4">Existing Contact Items</h2>
      <div v-if="loading" class="text-center py-4">Loading contacts...</div>
      <div v-else-if="contacts.length === 0" class="text-center py-4">No contact items found.</div>
      <div v-else class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Value</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Type</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Icon</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Order</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Visible</th>
              <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="contact in contacts" :key="contact.id">
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ contact.name }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ contact.value }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ contact.type }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ contact.icon }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ contact.order }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                <span :class="{'px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800': contact.is_visible, 'px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800': !contact.is_visible}">
                  {{ contact.is_visible ? 'Yes' : 'No' }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <button @click="editContact(contact)" class="text-indigo-600 hover:text-indigo-900 mr-4">Edit</button>
                <button @click="deleteContact(contact.id)" class="text-red-600 hover:text-red-900">Delete</button>
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

const contacts = ref([]);
const loading = ref(true);
const form = ref({
  name: '',
  value: '',
  type: 'phone',
  icon: '',
  order: 0,
  is_visible: true,
});
const editingContact = ref(null); // Stores the contact being edited

const API_URL = '/api/content/contacts/'; // API endpoint for contacts

const fetchContacts = async () => {
  loading.value = true;
  try {
    const response = await axios.get(API_URL);
    contacts.value = response.data; // Correctly access the results array
  } catch (error) {
    console.error('Error fetching contact items:', error);
  } finally {
    loading.value = false;
  }
};

const saveContact = async () => {
  try {
    if (editingContact.value) {
      // Update existing contact
      await axios.put(`${API_URL}${editingContact.value.id}/`, form.value);
      console.log('Contact updated successfully!');
    } else {
      // Create new contact
      await axios.post(API_URL, form.value);
      console.log('Contact created successfully!');
    }
    resetForm();
    await fetchContacts(); // Refresh the list
  } catch (error) {
    console.error('Error saving contact item:', error);
  }
};

const editContact = (contact) => {
  editingContact.value = contact;
  form.value = { ...contact }; // Populate form with contact data
};

const cancelEdit = () => {
  resetForm();
  editingContact.value = null;
};

const deleteContact = async (id) => {
  if (confirm('Are you sure you want to delete this contact item?')) {
    try {
      await axios.delete(`${API_URL}${id}/`);
      console.log('Contact deleted successfully!');
      await fetchContacts(); // Refresh the list
    } catch (error) {
      console.error('Error deleting contact item:', error);
    }
  }
};

const resetForm = () => {
  form.value = {
    name: '',
    value: '',
    type: 'phone',
    icon: '',
    order: 0,
    is_visible: true,
  };
};

onMounted(fetchContacts);
</script>

<style scoped>
/* Add Tailwind CSS or custom styles here */
</style>
