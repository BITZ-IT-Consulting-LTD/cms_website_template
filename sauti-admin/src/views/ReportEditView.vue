<template>
  <div class="p-6 space-y-6">
    <!-- Header -->
    <div class="flex justify-between items-start">
      <div class="flex items-center gap-4">
        <button
          @click="goBack"
          class="p-2 hover:bg-gray-100 rounded-md transition-colors"
        >
          <ArrowLeftIcon class="h-6 w-6 text-gray-600" />
        </button>
        <div>
          <h1 class="text-2xl font-bold text-gray-900">Edit Report</h1>
          <p class="text-gray-600 mt-1">{{ report.reference_number }}</p>
        </div>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex justify-center items-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500"></div>
    </div>

    <!-- Error Message -->
    <div v-if="error" class="bg-red-50 border-l-4 border-red-500 p-4 rounded-md">
      <div class="flex">
        <ExclamationTriangleIcon class="h-5 w-5 text-red-400 mr-3" />
        <p class="text-sm text-red-700">{{ error }}</p>
      </div>
    </div>

    <!-- Edit Form -->
    <div v-else class="space-y-6">
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <h2 class="text-lg font-semibold text-gray-900 mb-4">Report Management</h2>
        
        <form @submit.prevent="saveReport" class="space-y-4">
          <!-- Status -->
          <div>
            <label for="status" class="block text-sm font-medium text-gray-700 mb-2">
              Status
            </label>
            <select
              id="status"
              v-model="form.status"
              class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
              required
            >
              <option value="PENDING">Pending Review</option>
              <option value="IN_PROGRESS">In Progress</option>
              <option value="RESOLVED">Resolved</option>
              <option value="CLOSED">Closed</option>
            </select>
          </div>

          <!-- Assigned To -->
          <div>
            <label for="assigned_to" class="block text-sm font-medium text-gray-700 mb-2">
              Assign To
            </label>
            <input
              id="assigned_to"
              v-model="form.assigned_to"
              type="text"
              placeholder="Enter staff member ID"
              class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
            />
            <p class="mt-1 text-sm text-gray-500">Enter the user ID of the staff member to assign this report</p>
          </div>

          <!-- Internal Notes -->
          <div>
            <label for="notes" class="block text-sm font-medium text-gray-700 mb-2">
              Internal Notes
            </label>
            <textarea
              id="notes"
              v-model="form.notes"
              rows="6"
              placeholder="Add internal notes about this case (not visible to reporter)"
              class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 resize-none"
            ></textarea>
          </div>

          <!-- Action Buttons -->
          <div class="flex justify-end gap-3 pt-4">
            <button
              type="button"
              @click="goBack"
              class="px-6 py-2 border border-gray-300 text-gray-700 rounded-md hover:bg-gray-50 transition-colors duration-200"
            >
              Cancel
            </button>
            <button
              type="submit"
              :disabled="saving"
              class="px-6 py-2 bg-primary-500 text-white rounded-md hover:bg-primary-600 transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span v-if="!saving">Save Changes</span>
              <span v-else class="flex items-center">
                <span class="animate-spin w-5 h-5 mr-2 border-2 border-white border-t-transparent rounded-full"></span>
                Saving...
              </span>
            </button>
          </div>
        </form>
      </div>

      <!-- Read-Only Report Information -->
      <div class="bg-gray-50 p-6 rounded-lg border border-gray-200">
        <h2 class="text-lg font-semibold text-gray-900 mb-4">Report Information (Read-Only)</h2>
        <dl class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <dt class="text-sm font-medium text-gray-600">Category</dt>
            <dd class="mt-1 text-sm text-gray-900">{{ formatCategory(report.category) }}</dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Submitted</dt>
            <dd class="mt-1 text-sm text-gray-900">{{ formatDateTime(report.created_at) }}</dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Anonymous</dt>
            <dd class="mt-1 text-sm text-gray-900">{{ report.is_anonymous ? 'Yes' : 'No' }}</dd>
          </div>
          <div v-if="report.location">
            <dt class="text-sm font-medium text-gray-600">Location</dt>
            <dd class="mt-1 text-sm text-gray-900">{{ report.location }}</dd>
          </div>
        </dl>
        
        <div class="mt-4">
          <dt class="text-sm font-medium text-gray-600">Description</dt>
          <dd class="mt-2 text-sm text-gray-900 whitespace-pre-wrap bg-white p-4 rounded border border-gray-200">
            {{ report.description }}
          </dd>
        </div>
      </div>
    </div>

    <!-- Success Modal -->
    <div v-if="showSuccess" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black bg-opacity-50">
      <div class="bg-white rounded-lg shadow-xl max-w-md w-full p-6 text-center">
        <div class="bg-green-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
          <CheckCircleIcon class="w-10 h-10 text-green-600" />
        </div>
        <h2 class="text-2xl font-bold text-gray-900 mb-2">Report Updated</h2>
        <p class="text-gray-600 mb-6">The report has been successfully updated.</p>
        <button
          @click="goBack"
          class="px-6 py-2 bg-primary-500 text-white rounded-md hover:bg-primary-600 transition-colors duration-200"
        >
          Back to Reports
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { api } from '@/utils/api'
import {
  ArrowLeftIcon,
  ExclamationTriangleIcon,
  CheckCircleIcon
} from '@heroicons/vue/24/outline'

const router = useRouter()
const route = useRoute()

const report = ref({})
const loading = ref(false)
const saving = ref(false)
const error = ref(null)
const showSuccess = ref(false)

const form = reactive({
  status: '',
  assigned_to: null,
  notes: ''
})

async function fetchReport() {
  loading.value = true
  error.value = null
  
  try {
    const response = await api.reports.get(route.params.id)
    report.value = response.data
    
    // Populate form with current values
    form.status = report.value.status
    form.assigned_to = report.value.assigned_to
    form.notes = report.value.notes || ''
    
    console.log('✅ Fetched report:', report.value)
  } catch (err) {
    console.error('❌ Error fetching report:', err)
    error.value = 'Failed to load report details.'
    
    if (err.response?.status === 404) {
      error.value = 'Report not found.'
    }
  } finally {
    loading.value = false
  }
}

async function saveReport() {
  saving.value = true
  error.value = null
  
  try {
    await api.reports.update(route.params.id, {
      status: form.status,
      assigned_to: form.assigned_to || null,
      notes: form.notes
    })
    
    showSuccess.value = true
    console.log('✅ Report updated successfully')
    
    // Redirect after 2 seconds
    setTimeout(() => {
      goBack()
    }, 2000)
  } catch (err) {
    console.error('❌ Error updating report:', err)
    error.value = err.response?.data?.detail || 'Failed to update report. Please try again.'
  } finally {
    saving.value = false
  }
}

function formatCategory(category) {
  const map = {
    'CHILD_PROTECTION': 'Child Protection',
    'GBV': 'Gender-Based Violence',
    'MIGRANT': 'Migrant Worker',
    'PSEA': 'PSEA'
  }
  return map[category] || category
}

function formatDateTime(dateStr) {
  if (!dateStr) return 'N/A'
  const date = new Date(dateStr)
  return date.toLocaleString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

function goBack() {
  router.push('/reports')
}

onMounted(() => {
  fetchReport()
})
</script>

<style scoped>
.animate-spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>
