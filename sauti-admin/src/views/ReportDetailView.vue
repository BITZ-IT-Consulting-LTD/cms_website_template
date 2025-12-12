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
          <h1 class="text-2xl font-bold text-gray-900">Report Details</h1>
          <p class="text-gray-600 mt-1">{{ report.reference_number }}</p>
        </div>
      </div>
      <div class="flex gap-3">
        <button
          @click="editReport"
          class="px-4 py-2 bg-primary-500 text-white rounded-md hover:bg-primary-600 transition-colors duration-200 flex items-center font-medium shadow-sm"
        >
          <PencilIcon class="h-5 w-5 mr-2" />
          Edit Report
        </button>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex justify-center items-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500"></div>
    </div>

    <!-- Error Message -->
    <div v-else-if="error" class="bg-red-50 border-l-4 border-red-500 p-4 rounded-md">
      <div class="flex">
        <ExclamationTriangleIcon class="h-5 w-5 text-red-400 mr-3" />
        <p class="text-sm text-red-700">{{ error }}</p>
      </div>
    </div>

    <!-- Report Content -->
    <div v-else class="space-y-6">
      <!-- Status and Category -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <p class="text-sm font-medium text-gray-600">Category</p>
          <span :class="getCategoryClass(report.category)" class="mt-2 px-3 py-1 inline-flex text-sm font-semibold rounded-full">
            {{ formatCategory(report.category) }}
          </span>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <p class="text-sm font-medium text-gray-600">Status</p>
          <span :class="getStatusClass(report.status)" class="mt-2 px-3 py-1 inline-flex text-sm font-semibold rounded-full">
            {{ formatStatus(report.status) }}
          </span>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <p class="text-sm font-medium text-gray-600">Anonymous</p>
          <p class="mt-2 text-lg font-bold text-gray-900">{{ report.is_anonymous ? 'Yes' : 'No' }}</p>
        </div>
      </div>

      <!-- Main Content -->
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <h2 class="text-lg font-semibold text-gray-900 mb-4">Report Description</h2>
        <p class="text-gray-700 whitespace-pre-wrap">{{ report.description || 'No description provided' }}</p>
      </div>

      <!-- Contact Information -->
      <div v-if="!report.is_anonymous" class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <h2 class="text-lg font-semibold text-gray-900 mb-4">Contact Information</h2>
        <dl class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-if="report.contact_name">
            <dt class="text-sm font-medium text-gray-600">Name</dt>
            <dd class="mt-1 text-sm text-gray-900">{{ report.contact_name }}</dd>
          </div>
          <div v-if="report.contact_phone">
            <dt class="text-sm font-medium text-gray-600">Phone</dt>
            <dd class="mt-1 text-sm text-gray-900">{{ report.contact_phone }}</dd>
          </div>
          <div v-if="report.contact_email">
            <dt class="text-sm font-medium text-gray-600">Email</dt>
            <dd class="mt-1 text-sm text-gray-900">{{ report.contact_email }}</dd>
          </div>
          <div v-if="report.location">
            <dt class="text-sm font-medium text-gray-600">Location</dt>
            <dd class="mt-1 text-sm text-gray-900">{{ report.location }}</dd>
          </div>
        </dl>
      </div>

      <!-- Assignment and Tracking -->
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <h2 class="text-lg font-semibold text-gray-900 mb-4">Tracking Information</h2>
        <dl class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <dt class="text-sm font-medium text-gray-600">Assigned To</dt>
            <dd class="mt-1 text-sm text-gray-900">{{ report.assigned_to || 'Unassigned' }}</dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Created At</dt>
            <dd class="mt-1 text-sm text-gray-900">{{ formatDateTime(report.created_at) }}</dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Last Updated</dt>
            <dd class="mt-1 text-sm text-gray-900">{{ formatDateTime(report.updated_at) }}</dd>
          </div>
          <div v-if="report.resolved_at">
            <dt class="text-sm font-medium text-gray-600">Resolved At</dt>
            <dd class="mt-1 text-sm text-gray-900">{{ formatDateTime(report.resolved_at) }}</dd>
          </div>
        </dl>
      </div>

      <!-- Internal Notes -->
      <div v-if="report.notes" class="bg-yellow-50 p-6 rounded-lg border border-yellow-200">
        <h2 class="text-lg font-semibold text-gray-900 mb-4">Internal Notes</h2>
        <p class="text-gray-700 whitespace-pre-wrap">{{ report.notes }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { api } from '@/utils/api'
import {
  ArrowLeftIcon,
  PencilIcon,
  ExclamationTriangleIcon
} from '@heroicons/vue/24/outline'

const router = useRouter()
const route = useRoute()

const report = ref({})
const loading = ref(false)
const error = ref(null)

async function fetchReport() {
  loading.value = true
  error.value = null
  
  try {
    const response = await api.reports.get(route.params.id)
    report.value = response.data
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

function formatCategory(category) {
  const map = {
    'CHILD_PROTECTION': 'Child Protection',
    'GBV': 'Gender-Based Violence',
    'MIGRANT': 'Migrant Worker',
    'PSEA': 'PSEA'
  }
  return map[category] || category
}

function formatStatus(status) {
  const map = {
    'PENDING': 'Pending Review',
    'IN_PROGRESS': 'In Progress',
    'RESOLVED': 'Resolved',
    'CLOSED': 'Closed'
  }
  return map[status] || status
}

function getCategoryClass(category) {
  const map = {
    'CHILD_PROTECTION': 'bg-blue-100 text-blue-800',
    'GBV': 'bg-purple-100 text-purple-800',
    'MIGRANT': 'bg-teal-100 text-teal-800',
    'PSEA': 'bg-orange-100 text-orange-800'
  }
  return map[category] || 'bg-gray-100 text-gray-800'
}

function getStatusClass(status) {
  const map = {
    'PENDING': 'bg-yellow-100 text-yellow-800',
    'IN_PROGRESS': 'bg-orange-100 text-orange-800',
    'RESOLVED': 'bg-green-100 text-green-800',
    'CLOSED': 'bg-gray-100 text-gray-800'
  }
  return map[status] || 'bg-gray-100 text-gray-800'
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

function editReport() {
  router.push(`/reports/${route.params.id}/edit`)
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
