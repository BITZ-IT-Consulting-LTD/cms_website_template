<template>
  <div class="p-6 bg-gray-50 min-h-screen">
    <h1 class="text-3xl font-bold text-gray-800 mb-6">Site Settings</h1>

    <div v-if="loading" class="text-center py-12">
      <p class="text-lg text-gray-600">Loading settings...</p>
    </div>

    <div v-if="error" class="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 mb-6 rounded-md shadow-md" role="alert">
      <p class="font-bold">Error</p>
      <p>{{ error }}</p>
    </div>

    <div v-if="success" class="bg-green-100 border-l-4 border-green-500 text-green-700 p-4 mb-6 rounded-md shadow-md" role="alert">
      <p class="font-bold">Success</p>
      <p>Site settings updated successfully.</p>
    </div>

    <form v-if="!loading && settings" @submit.prevent="saveSettings" class="space-y-8 bg-white p-8 rounded-lg shadow-md">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Text-based settings -->
        <div v-for="(value, key) in textSettings" :key="key" class="flex flex-col">
          <label :for="key" class="block text-sm font-medium text-gray-700 mb-1 capitalize">{{ key.replace(/_/g, ' ') }}</label>
          <input
            type="text"
            :id="key"
            v-model="settings[key]"
            class="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          />
        </div>
      </div>

      <div class="flex justify-end pt-4">
        <button
          type="submit"
          :disabled="isSaving"
          class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50"
        >
          <span v-if="isSaving">Saving...</span>
          <span v-else>Save Settings</span>
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { api } from '@/utils/api';

// Reactive state for the component
const settings = ref(null);
const loading = ref(true);
const error = ref(null);
const success = ref(false);
const isSaving = ref(false);

/**
 * Data flow: Fetches all site settings from the backend on component mount.
 * The data is stored in the `settings` reactive variable.
 */
onMounted(async () => {
  try {
    loading.value = true;
    error.value = null;
    // API Interaction: Fetch current settings from the backend.
    const response = await api.get('/api/sitesettings/settings/');
    settings.value = response.data;
  } catch (err) {
    // Error Handling: Catches and displays errors during the fetch operation.
    console.error('Failed to fetch site settings:', err);
    error.value = 'Could not load site settings. Please try again later.';
  } finally {
    loading.value = false;
  }
});

/**
 * Filters out non-text fields to be rendered in the form.
 * The backend might return fields like 'id' that are not meant to be edited.
 */
const textSettings = computed(() => {
  if (!settings.value) return {};
  const excludedKeys = ['id']; // Exclude non-editable fields
  const filtered = {};
  for (const key in settings.value) {
    if (!excludedKeys.includes(key)) {
      filtered[key] = settings.value[key];
    }
  }
  return filtered;
});

/**
 * Update Logic: Persists the entire settings object to the backend.
 * This function is called when the user submits the form.
 */
const saveSettings = async () => {
  try {
    isSaving.value = true;
    error.value = null;
    success.value = false;

    // API Interaction: Send the full settings object via a PUT request.
    // The backend expects the complete object, so no fields are omitted.
    await api.put('/api/sitesettings/settings/', settings.value);

    // Handle Success: Show a confirmation message.
    success.value = true;
    setTimeout(() => {
      success.value = false;
    }, 3000); // Hide message after 3 seconds
  } catch (err) {
    // Handle Failure: Show an error message.
    console.error('Failed to save site settings:', err);
    error.value = 'Failed to save settings. Please check your input and try again.';
  } finally {
    isSaving.value = false;
  }
};
</script>
