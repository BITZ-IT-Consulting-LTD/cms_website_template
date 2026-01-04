<template>
  <div class="p-6 space-y-6">
    <!-- Header -->
    <div class="mb-8">
      <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">Legal & Footer Content</h1>
      <p class="text-gray-600 mt-1">Manage privacy policy, terms of service, and footer text displayed across your website</p>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex items-center justify-center py-12">
      <div class="text-center">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
        <p class="text-gray-600">Loading legal content...</p>
      </div>
    </div>

    <!-- Content Sections -->
    <div v-else class="space-y-6">
      <!-- Privacy Policy -->
      <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div class="flex items-center mb-4">
          <ShieldCheckIcon class="h-6 w-6 text-blue-600 mr-3" />
          <h2 class="text-xl font-semibold text-gray-900">Privacy Policy</h2>
        </div>
        <p class="text-sm text-gray-600 mb-4">
          Define your organization's privacy policy and data protection practices.
        </p>
        
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Privacy Policy URL</label>
            <input
              v-model="form.privacy_policy_url"
              type="url"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              placeholder="https://example.com/privacy"
            />
            <p class="mt-1 text-xs text-gray-500">Link to your full privacy policy document (can be external or internal page)</p>
          </div>
        </div>
      </div>

      <!-- Terms of Service -->
      <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div class="flex items-center mb-4">
          <DocumentTextIcon class="h-6 w-6 text-green-600 mr-3" />
          <h2 class="text-xl font-semibold text-gray-900">Terms of Service</h2>
        </div>
        <p class="text-sm text-gray-600 mb-4">
          Specify the terms and conditions for using your services.
        </p>
        
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Terms of Service URL</label>
            <input
              v-model="form.terms_of_service_url"
              type="url"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              placeholder="https://example.com/terms"
            />
            <p class="mt-1 text-xs text-gray-500">Link to your terms of service document</p>
          </div>
        </div>
      </div>

      <!-- Accessibility Statement -->
      <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div class="flex items-center mb-4">
          <UserGroupIcon class="h-6 w-6 text-purple-600 mr-3" />
          <h2 class="text-xl font-semibold text-gray-900">Accessibility Statement</h2>
        </div>
        <p class="text-sm text-gray-600 mb-4">
          Communicate your commitment to web accessibility and inclusion.
        </p>
        
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Accessibility Statement URL</label>
            <input
              v-model="form.accessibility_url"
              type="url"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              placeholder="https://example.com/accessibility"
            />
            <p class="mt-1 text-xs text-gray-500">Link to your accessibility statement or WCAG compliance information</p>
          </div>
        </div>
      </div>

      <!-- Footer Text -->
      <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div class="flex items-center mb-4">
          <ChatBubbleBottomCenterTextIcon class="h-6 w-6 text-gray-600 mr-3" />
          <h2 class="text-xl font-semibold text-gray-900">Footer Text</h2>
        </div>
        <p class="text-sm text-gray-600 mb-4">
          Main footer description text that appears at the bottom of every page.
        </p>
        
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Footer Description</label>
            <textarea
              v-model="form.footer_text"
              rows="4"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-y"
              placeholder="Enter the main footer text that describes your organization..."
            ></textarea>
            <p class="mt-1 text-xs text-gray-500">Brief description of your organization shown in the website footer</p>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Ministry Attribution</label>
            <textarea
              v-model="form.ministry_attribution_text"
              rows="2"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-y"
              placeholder="e.g., A service of the Ministry of Gender, Labour and Social Development"
            ></textarea>
            <p class="mt-1 text-xs text-gray-500">Government or organizational attribution text</p>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Disclaimer Text</label>
            <textarea
              v-model="form.disclaimer_text"
              rows="3"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-y"
              placeholder="Enter any legal disclaimers or important notices..."
            ></textarea>
            <p class="mt-1 text-xs text-gray-500">Legal disclaimer or important notice displayed in the footer</p>
          </div>
        </div>
      </div>

      <!-- Footer Links Configuration -->
      <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-4">
          <div class="flex items-center">
            <LinkIcon class="h-6 w-6 text-indigo-600 mr-3" />
            <h2 class="text-xl font-semibold text-gray-900">Footer Navigation Links</h2>
          </div>
          <button
            @click="addFooterLink"
            class="btn-outline text-sm flex items-center"
          >
            <PlusIcon class="h-4 w-4 mr-1" />
            Add Link
          </button>
        </div>
        <p class="text-sm text-gray-600 mb-4">
          Manage the navigation links displayed in your website footer.
        </p>

        <div class="space-y-3">
          <div
            v-for="(link, index) in form.footer_links"
            :key="index"
            class="flex items-start gap-3 p-4 bg-gray-50 rounded-lg border border-gray-200"
          >
            <div class="flex-1 grid grid-cols-1 md:grid-cols-3 gap-3">
              <div>
                <label class="block text-xs font-medium text-gray-700 mb-1">Label</label>
                <input
                  v-model="link.label"
                  type="text"
                  class="w-full px-3 py-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="e.g., About Us"
                />
              </div>
              <div>
                <label class="block text-xs font-medium text-gray-700 mb-1">URL Path</label>
                <input
                  v-model="link.to"
                  type="text"
                  class="w-full px-3 py-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="/about"
                />
              </div>
              <div>
                <label class="block text-xs font-medium text-gray-700 mb-1">Type</label>
                <select
                  v-model="link.type"
                  class="w-full px-3 py-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                >
                  <option value="nav">Navigation</option>
                  <option value="legal">Legal</option>
                </select>
              </div>
            </div>
            <button
              @click="removeFooterLink(index)"
              class="mt-6 p-2 text-red-600 hover:text-red-800 hover:bg-red-50 rounded transition-colors"
              title="Remove link"
            >
              <TrashIcon class="h-4 w-4" />
            </button>
          </div>

          <div v-if="form.footer_links.length === 0" class="text-center py-8 text-gray-500 text-sm">
            No footer links configured. Click "Add Link" to create one.
          </div>
        </div>
      </div>

      <!-- Save Actions -->
      <div class="flex justify-end gap-4 pt-4">
        <button
          @click="loadSettings"
          class="px-6 py-3 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 font-medium"
          :disabled="saving"
        >
          Reset Changes
        </button>
        <button
          @click="saveSettings"
          class="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium disabled:opacity-50 disabled:cursor-not-allowed"
          :disabled="saving"
        >
          {{ saving ? 'Saving...' : 'Save All Changes' }}
        </button>
      </div>

      <!-- Last Updated -->
      <div v-if="lastUpdated" class="text-center pt-4 border-t border-gray-200">
        <p class="text-sm text-gray-500">
          Last updated: {{ formatDate(lastUpdated) }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useToast } from 'vue-toastification'
import {
  ShieldCheckIcon,
  DocumentTextIcon,
  UserGroupIcon,
  ChatBubbleBottomCenterTextIcon,
  LinkIcon,
  PlusIcon,
  TrashIcon
} from '@heroicons/vue/24/outline'
import { api } from '@/utils/api'

const toast = useToast()
const loading = ref(true)
const saving = ref(false)
const lastUpdated = ref(null)

const form = ref({
  privacy_policy_url: '',
  terms_of_service_url: '',
  accessibility_url: '',
  footer_text: '',
  ministry_attribution_text: '',
  disclaimer_text: '',
  footer_links: []
})

const loadSettings = async () => {
  loading.value = true
  try {
    const response = await api.siteSettings.get()
    const settings = response.data

    form.value = {
      privacy_policy_url: settings.privacy_policy_url || '',
      terms_of_service_url: settings.terms_of_service_url || '',
      accessibility_url: settings.accessibility_url || '',
      footer_text: settings.footer_text || '',
      ministry_attribution_text: settings.ministry_attribution_text || '',
      disclaimer_text: settings.disclaimer_text || '',
      footer_links: Array.isArray(settings.footer_links) ? settings.footer_links : []
    }

    lastUpdated.value = settings.updated_at
  } catch (error) {
    console.error('Failed to load legal settings:', error)
    toast.error('Failed to load legal and footer content')
  } finally {
    loading.value = false
  }
}

const saveSettings = async () => {
  saving.value = true
  try {
    await api.siteSettings.update(form.value)
    toast.success('Legal and footer content saved successfully')
    await loadSettings()
  } catch (error) {
    console.error('Failed to save legal settings:', error)
    toast.error('Failed to save changes')
  } finally {
    saving.value = false
  }
}

const addFooterLink = () => {
  form.value.footer_links.push({
    label: '',
    to: '',
    type: 'nav'
  })
}

const removeFooterLink = (index) => {
  if (confirm('Are you sure you want to remove this footer link?')) {
    form.value.footer_links.splice(index, 1)
  }
}

const formatDate = (dateString) => {
  if (!dateString) return 'Never'
  const date = new Date(dateString)
  return date.toLocaleString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

onMounted(() => {
  loadSettings()
})
</script>
