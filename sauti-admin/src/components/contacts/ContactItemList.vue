<template>
  <div class="space-y-8">
    <!-- Create/Edit Form -->
    <div class="bg-white shadow-sm border border-gray-200 rounded-lg p-6">
      <h2 class="text-xl font-bold text-gray-900 mb-4">{{ editingContact ? 'Edit Contact Item' : 'Add New Contact Item' }}</h2>
      <form @submit.prevent="saveContact">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label for="name" class="block text-sm font-medium text-gray-700 mb-2">Label/Name</label>
            <input 
              type="text" 
              id="name" 
              v-model="form.name" 
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent cursor-text" 
              placeholder="e.g. Kampala Office"
              required
            >
          </div>
          <div>
            <label for="value" class="block text-sm font-medium text-gray-700 mb-2">Value (Phone/Email/Link)</label>
            <input 
              type="text" 
              id="value" 
              v-model="form.value" 
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent cursor-text" 
              placeholder="e.g. +256..."
              required
            >
          </div>
          <div>
            <label for="type" class="block text-sm font-medium text-gray-700 mb-2">Type</label>
            <select 
              id="type" 
              v-model="form.type" 
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent cursor-pointer" 
              required
            >
              <option value="phone">Phone Number</option>
              <option value="email">Email Address</option>
              <option value="location">Physical Location</option>
              <option value="social">Social Media Link</option>
              <option value="other">Other</option>
            </select>
          </div>
          <div>
            <label for="icon" class="block text-sm font-medium text-gray-700 mb-2">Icon (Heroicon name)</label>
            <input 
              type="text" 
              id="icon" 
              v-model="form.icon" 
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent cursor-text" 
              placeholder="e.g. PhoneIcon, EnvelopeIcon"
            >
          </div>
          <div>
            <label for="order" class="block text-sm font-medium text-gray-700 mb-2">Display Order</label>
            <input 
              type="number" 
              id="order" 
              v-model="form.order" 
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent cursor-text" 
              required
            >
          </div>
          <div class="flex items-center mt-8">
            <input 
              type="checkbox" 
              id="is_visible" 
              v-model="form.is_visible" 
              class="h-5 w-5 text-blue-600 border-gray-300 rounded focus:ring-blue-500 cursor-pointer"
            >
            <label for="is_visible" class="ml-3 block text-sm font-medium text-gray-700 cursor-pointer">Show on website</label>
          </div>
        </div>
        
        <div class="mt-8 flex justify-end gap-3">
          <button 
            v-if="editingContact"
            type="button" 
            @click="cancelEdit" 
            class="px-6 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 font-medium"
          >
            Cancel
          </button>
          <button 
            type="submit" 
            class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium disabled:opacity-50"
            :disabled="saving"
          >
            {{ saving ? 'Saving...' : (editingContact ? 'Update Item' : 'Add Item') }}
          </button>
        </div>
      </form>
    </div>

    <!-- Contact List -->
    <div class="bg-white shadow-sm border border-gray-200 rounded-lg overflow-hidden">
      <div class="px-6 py-4 border-b border-gray-200 bg-gray-50 flex justify-between items-center">
        <h2 class="text-lg font-bold text-gray-900">Registered Contact Items</h2>
        <span class="text-xs font-medium px-2 py-1 bg-gray-200 text-gray-600 rounded-full">{{ contacts.length }} Items</span>
      </div>
      
      <div v-if="loading" class="p-12 text-center text-gray-500 italic">
        Loading contacts...
      </div>
      <div v-else-if="contacts.length === 0" class="p-12 text-center text-gray-500 italic">
        No additional contact items found.
      </div>
      <div v-else class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th scope="col" class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider">Label</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider">Value</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider">Type</th>
              <th scope="col" class="px-6 py-3 text-center text-xs font-bold text-gray-500 uppercase tracking-wider">Order</th>
              <th scope="col" class="px-6 py-3 text-center text-xs font-bold text-gray-500 uppercase tracking-wider">Status</th>
              <th scope="col" class="px-6 py-3 text-right text-xs font-bold text-gray-500 uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="contact in sortedContacts" :key="contact.id" class="hover:bg-gray-50 transition-colors">
              <td class="px-6 py-4 whitespace-nowrap text-sm font-semibold text-gray-900">{{ contact.name }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-600">{{ contact.value }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 capitalize">
                <span class="px-2 py-1 bg-gray-100 rounded text-xs">{{ contact.type }}</span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-center text-gray-500">{{ contact.order }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-center">
                <span :class="{'bg-green-100 text-green-700': contact.is_visible, 'bg-red-100 text-red-700': !contact.is_visible}" class="px-2.5 py-0.5 rounded-full text-xs font-bold uppercase tracking-wider">
                  {{ contact.is_visible ? 'Visible' : 'Hidden' }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <div class="flex items-center justify-end gap-3">
                  <button @click="editContact(contact)" class="text-blue-600 hover:text-blue-900 font-bold transition-colors">Edit</button>
                  <button @click="deleteContact(contact.id)" class="text-red-500 hover:text-red-700 font-bold transition-colors">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { api } from '@/utils/api';
import { useToast } from 'vue-toastification';

const toast = useToast();
const contacts = ref([]);
const loading = ref(true);
const saving = ref(false);
const editingContact = ref(null);

const form = ref({
  name: '',
  value: '',
  type: 'phone',
  icon: '',
  order: 0,
  is_visible: true,
});

const sortedContacts = computed(() => {
  return [...contacts.value].sort((a, b) => a.order - b.order);
});

const fetchContacts = async () => {
  loading.value = true;
  try {
    // Note: We need to make sure this endpoint exists in our api settings
    const response = await api.get('/content/contacts/');
    contacts.value = response.data;
  } catch (error) {
    console.error('Error fetching contact items:', error);
    toast.error('Failed to load contact items');
  } finally {
    loading.value = false;
  }
};

const saveContact = async () => {
  saving.value = true;
  try {
    if (editingContact.value) {
      await api.put(`/content/contacts/${editingContact.value.id}/`, form.value);
      toast.success('Contact item updated!');
    } else {
      await api.post('/content/contacts/', form.value);
      toast.success('New contact item added!');
    }
    resetForm();
    await fetchContacts();
  } catch (error) {
    console.error('Error saving contact item:', error);
    toast.error('Failed to save contact item');
  } finally {
    saving.value = false;
  }
};

const editContact = (contact) => {
  editingContact.value = contact;
  form.value = { ...contact };
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

const cancelEdit = () => {
  resetForm();
  editingContact.value = null;
};

const deleteContact = async (id) => {
  if (confirm('Are you sure you want to delete this contact item?')) {
    try {
      await api.delete(`/content/contacts/${id}/`);
      toast.success('Contact item deleted');
      await fetchContacts();
    } catch (error) {
      console.error('Error deleting contact item:', error);
      toast.error('Failed to delete contact item');
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
  editingContact.value = null;
};

onMounted(fetchContacts);
</script>
