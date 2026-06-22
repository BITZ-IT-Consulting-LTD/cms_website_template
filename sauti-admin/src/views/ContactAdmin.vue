<template>
  <div class="p-6">
    <PageHeader
      title="Contact Channels"
      description="Manage the contact methods shown on the public Contact page"
      :action-label="editingContact ? 'New Contact' : null"
      :action-icon="PlusIcon"
      @action="cancelEdit"
    />

    <!-- Create/Edit Form -->
    <div class="card mb-8">
      <div class="card-header">
        <h2 class="text-lg font-bold text-gray-900">{{ editingContact ? 'Edit Contact Channel' : 'Add Contact Channel' }}</h2>
      </div>
      <div class="card-body">
        <form @submit.prevent="saveContact">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label for="name" class="form-label">Name</label>
              <input type="text" id="name" v-model="form.name" class="form-input" placeholder="e.g., WhatsApp" required>
            </div>
            <div>
              <label for="value" class="form-label">Value</label>
              <input type="text" id="value" v-model="form.value" class="form-input" placeholder="e.g., 0800-100-200" required>
            </div>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
            <div>
              <label for="type" class="form-label">Type</label>
              <select id="type" v-model="form.type" class="form-select" required>
                <option value="phone">Phone Number</option>
                <option value="email">Email Address</option>
                <option value="location">Physical Location</option>
                <option value="social">Social Media Link</option>
                <option value="other">Other</option>
              </select>
            </div>
            <div>
              <label for="icon" class="form-label">Icon Name</label>
              <input type="text" id="icon" v-model="form.icon" class="form-input" placeholder="e.g., phone, envelope, whatsapp">
            </div>
          </div>
          <div class="mt-4">
            <label for="description" class="form-label">Description <span class="font-normal text-gray-400">(shown on the contact page card)</span></label>
            <textarea id="description" v-model="form.description" rows="2" class="form-input" placeholder="e.g., Free, confidential hotline available 24/7"></textarea>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
            <div>
              <label for="order" class="form-label">Order</label>
              <input type="number" id="order" v-model="form.order" class="form-input" placeholder="0" required>
            </div>
            <div class="flex items-center pt-8">
              <input type="checkbox" id="is_visible" v-model="form.is_visible" class="h-4 w-4 rounded border-gray-300 text-[#009EDB] focus:ring-[#009EDB]">
              <label for="is_visible" class="ml-2 block text-sm font-medium text-gray-700">Visible on the public site</label>
            </div>
          </div>
          <div class="flex items-center gap-3 mt-6">
            <button type="submit" class="btn-primary">
              {{ editingContact ? 'Update Contact' : 'Create Contact' }}
            </button>
            <button type="button" @click="cancelEdit" v-if="editingContact" class="btn-outline">
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Contact List -->
    <div class="card">
      <div class="card-header">
        <h2 class="text-lg font-bold text-gray-900">Existing Contact Channels</h2>
      </div>
      <LoadingState v-if="loading" message="Loading contacts..." />
      <EmptyState
        v-else-if="contacts.length === 0"
        :icon="PhoneIcon"
        title="No contact channels yet"
        message="Add your first contact channel using the form above."
      />
      <div v-else class="overflow-x-auto">
        <table class="min-w-full">
          <thead class="table-header">
            <tr>
              <th class="table-cell text-left text-xs font-bold uppercase tracking-wider">Name</th>
              <th class="table-cell text-left text-xs font-bold uppercase tracking-wider">Value</th>
              <th class="table-cell text-left text-xs font-bold uppercase tracking-wider">Description</th>
              <th class="table-cell text-left text-xs font-bold uppercase tracking-wider">Type</th>
              <th class="table-cell text-left text-xs font-bold uppercase tracking-wider">Icon</th>
              <th class="table-cell text-left text-xs font-bold uppercase tracking-wider">Order</th>
              <th class="table-cell text-left text-xs font-bold uppercase tracking-wider">Visible</th>
              <th class="table-cell text-right text-xs font-bold uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white">
            <tr v-for="contact in contacts" :key="contact.id" class="table-row">
              <td class="table-cell font-semibold text-gray-900">{{ contact.name }}</td>
              <td class="table-cell text-gray-500">{{ contact.value }}</td>
              <td class="table-cell text-gray-500 max-w-xs truncate" :title="contact.description">{{ contact.description || '—' }}</td>
              <td class="table-cell text-gray-500 capitalize">{{ contact.type }}</td>
              <td class="table-cell text-gray-500">{{ contact.icon || '—' }}</td>
              <td class="table-cell text-gray-500">{{ contact.order }}</td>
              <td class="table-cell">
                <span class="inline-flex px-2.5 py-0.5 text-xs font-semibold rounded-full" :class="contact.is_visible ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'">
                  {{ contact.is_visible ? 'Visible' : 'Hidden' }}
                </span>
              </td>
              <td class="table-cell text-right">
                <div class="flex items-center justify-end gap-2">
                  <button @click="editContact(contact)" class="p-2 text-gray-400 hover:text-[#009EDB] hover:bg-blue-50 rounded-full transition-all" title="Edit">
                    <PencilIcon class="h-4 w-4" />
                  </button>
                  <button @click="deleteContact(contact.id)" class="p-2 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded-full transition-all" title="Delete">
                    <TrashIcon class="h-4 w-4" />
                  </button>
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
import { ref, onMounted } from 'vue';
import { useToast } from 'vue-toastification';
import { api } from '@/utils/api';
import { PageHeader, LoadingState, EmptyState } from '@/components/admin';
import { PlusIcon, PencilIcon, TrashIcon, PhoneIcon } from '@heroicons/vue/24/outline';

const toast = useToast();
const contacts = ref([]);
const loading = ref(true);
const form = ref({
  name: '',
  value: '',
  type: 'phone',
  icon: '',
  description: '',
  order: 0,
  is_visible: true,
});
const editingContact = ref(null); // Stores the contact being edited

const fetchContacts = async () => {
  loading.value = true;
  try {
    const response = await api.contacts.list();
    // Endpoint has pagination disabled, so the payload is a plain array.
    contacts.value = Array.isArray(response.data) ? response.data : (response.data?.results || []);
  } catch (error) {
    console.error('Error fetching contact items:', error);
    toast.error('Failed to load contact items');
  } finally {
    loading.value = false;
  }
};

const saveContact = async () => {
  try {
    if (editingContact.value) {
      await api.contacts.update(editingContact.value.id, form.value);
      toast.success('Contact updated successfully');
    } else {
      await api.contacts.create(form.value);
      toast.success('Contact created successfully');
    }
    cancelEdit();
    await fetchContacts(); // Refresh the list
  } catch (error) {
    console.error('Error saving contact item:', error);
    toast.error('Failed to save contact item');
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
      await api.contacts.delete(id);
      toast.success('Contact deleted successfully');
      await fetchContacts(); // Refresh the list
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
    description: '',
    order: 0,
    is_visible: true,
  };
};

onMounted(fetchContacts);
</script>

<style scoped>
/* Add Tailwind CSS or custom styles here */
</style>
