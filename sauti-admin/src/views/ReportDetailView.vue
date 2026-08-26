<template>
  <div class="p-6 space-y-6">
    <!-- Header -->
    <div class="flex justify-between items-start">
      <div class="flex items-center gap-4">
        <button @click="goBack" class="p-2 hover:bg-gray-100 rounded-md transition-colors">
          <ArrowLeftIcon class="h-6 w-6 text-gray-600" />
        </button>
        <div>
          <h1 class="text-2xl font-bold text-gray-900">Report Details</h1>
          <p class="text-gray-600 mt-1">{{ report.reference_number }}</p>
        </div>
      </div>
      <div class="flex gap-3">
        <button @click="downloadPdf" :disabled="exportingPdf"
          class="px-4 py-2 border border-gray-300 text-gray-700 bg-white rounded-md hover:bg-gray-50 transition-colors duration-200 flex items-center font-medium shadow-sm disabled:opacity-50">
          <ArrowDownTrayIcon class="h-5 w-5 mr-2" />
          {{ exportingPdf ? 'Preparing…' : 'Download PDF' }}
        </button>
        <button v-if="report.status !== 'ESCALATED' && report.status !== 'CLOSED'" @click="updateStatus('ESCALATED')"
          class="px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700 transition-colors duration-200 flex items-center font-medium shadow-sm">
          <ExclamationTriangleIcon class="h-5 w-5 mr-2" />
          Escalate
        </button>
        <button v-if="report.status !== 'FORWARDED' && report.status !== 'CLOSED'" @click="updateStatus('FORWARDED')"
          class="px-4 py-2 bg-purple-600 text-white rounded-md hover:bg-purple-700 transition-colors duration-200 flex items-center font-medium shadow-sm">
          <ShareIcon class="h-5 w-5 mr-2" />
          Forward of OpenCHS
        </button>
        <button @click="editReport"
          class="px-4 py-2 bg-primary-500 text-white rounded-md hover:bg-primary-600 transition-colors duration-200 flex items-center font-medium shadow-sm">
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
          <span :class="getCategoryClass(report.category)"
            class="mt-2 px-3 py-1 inline-flex text-sm font-semibold rounded-full">
            {{ formatCategory(report.category) }}
          </span>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <p class="text-sm font-medium text-gray-600">Status</p>
          <span :class="getStatusClass(report.status)"
            class="mt-2 px-3 py-1 inline-flex text-sm font-semibold rounded-full">
            {{ formatStatus(report.status) }}
          </span>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <p class="text-sm font-medium text-gray-600">Anonymous</p>
          <p class="mt-2 text-lg font-bold text-gray-900">{{ report.is_anonymous ? 'Yes' : 'No' }}</p>
        </div>
      </div>
      <!-- Case Information. Every field the intake form can capture is rendered
           whether or not it was answered, so an agent can tell "the reporter
           skipped this" apart from "the system never asked". -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <p class="text-sm font-medium text-gray-600">Reporting For</p>
          <p class="mt-2 text-lg font-bold" :class="valueClass(report.reporting_for)">
            {{ report.reporting_for || 'Not provided' }}
          </p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <p class="text-sm font-medium text-gray-600">Incident Type</p>
          <p class="mt-2 text-lg font-bold" :class="valueClass(report.incident_type)">
            {{ report.incident_type || 'Not provided' }}
          </p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <p class="text-sm font-medium text-gray-600">Reporting About Self</p>
          <p class="mt-2 text-lg font-bold" :class="valueClass(report.is_self_report)">
            {{ formatBoolean(report.is_self_report) }}
          </p>
        </div>
      </div>

      <!-- Affected Persons: always rendered. Every captured person is listed
           (not just the first), and each field shows "Not provided" rather than
           being hidden, so nothing the reporter said is invisible here. -->
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <h2 class="text-lg font-semibold text-gray-900 mb-4">Affected Persons</h2>

        <div v-if="affectedPersons.length" class="space-y-4">
          <div v-for="(person, index) in affectedPersons" :key="index"
            class="bg-gray-50 p-4 rounded border border-gray-100">
            <h3 class="font-bold text-sm text-gray-700 mb-2">Person {{ index + 1 }}</h3>
            <dl class="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
              <div v-for="field in personFields" :key="field.key">
                <dt class="text-gray-500">{{ field.label }}</dt>
                <dd class="font-medium" :class="valueClass(person[field.key])">
                  {{ person[field.key] || 'Not provided' }}
                </dd>
              </div>
            </dl>
          </div>
        </div>

        <p v-else class="text-sm text-gray-400 italic">
          No per-person details were captured for this report.
        </p>

        <!-- Flat person fields kept on the report itself (older submissions, and
             the summary copy the intake serializer writes for the first person). -->
        <dl class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6 pt-6 border-t border-gray-100">
          <div>
            <dt class="text-sm font-medium text-gray-600">Age (report summary)</dt>
            <dd class="mt-1 text-sm" :class="valueClass(report.reported_person_age)">
              {{ report.reported_person_age || 'Not provided' }}
            </dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Gender (report summary)</dt>
            <dd class="mt-1 text-sm" :class="valueClass(report.reported_person_gender)">
              {{ report.reported_person_gender || 'Not provided' }}
            </dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Victim / Affected-Person Location</dt>
            <dd class="mt-1 text-sm" :class="valueClass(report.victim_location)">
              {{ report.victim_location || 'Not provided' }}
            </dd>
          </div>
        </dl>
      </div>

      <!-- Main Content -->
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <h2 class="text-lg font-semibold text-gray-900 mb-4">Report Description</h2>
        <p class="text-gray-700 whitespace-pre-wrap">{{ report.description || 'No description provided' }}</p>
      </div>

      <!-- Contact Information (always shown; unfilled fields are marked so
           agents can see what the reporter did and did not provide) -->
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-lg font-semibold text-gray-900">Contact Information</h2>
          <span v-if="report.is_anonymous"
            class="px-3 py-1 text-xs font-semibold rounded-full bg-gray-100 text-gray-600">
            Submitted anonymously
          </span>
        </div>
        <dl class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <dt class="text-sm font-medium text-gray-600">Name</dt>
            <dd class="mt-1 text-sm" :class="report.contact_name ? 'text-gray-900' : 'text-gray-400 italic'">
              {{ report.contact_name || 'Not provided' }}
            </dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Phone</dt>
            <dd class="mt-1 text-sm" :class="report.contact_phone ? 'text-gray-900' : 'text-gray-400 italic'">
              {{ report.contact_phone || 'Not provided' }}
            </dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Alternative Contact</dt>
            <dd class="mt-1 text-sm" :class="valueClass(report.alternative_contact)">
              {{ report.alternative_contact || 'Not provided' }}
            </dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Email</dt>
            <dd class="mt-1 text-sm" :class="report.contact_email ? 'text-gray-900' : 'text-gray-400 italic'">
              {{ report.contact_email || 'Not provided' }}
            </dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Location</dt>
            <dd class="mt-1 text-sm" :class="report.location ? 'text-gray-900' : 'text-gray-400 italic'">
              {{ report.location || 'Not provided' }}
            </dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Safe to Contact</dt>
            <dd class="mt-1 text-sm">
              <span :class="report.safe_to_contact ? 'text-green-600' : 'text-red-600'" class="font-bold">
                {{ report.safe_to_contact ? 'Yes' : 'No' }}
              </span>
            </dd>
          </div>
        </dl>
      </div>

      <!-- Assignment and Tracking -->
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <h2 class="text-lg font-semibold text-gray-900 mb-4">Tracking Information</h2>
        <dl class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <dt class="text-sm font-medium text-gray-600">Assigned To</dt>
            <dd class="mt-1 text-sm" :class="valueClass(report.assigned_to)">
              {{ report.assigned_to || 'Unassigned' }}
            </dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">OpenCHS Case ID</dt>
            <dd class="mt-1 text-sm font-mono" :class="valueClass(report.openchs_case_id)">
              {{ report.openchs_case_id || 'Not provided' }}
            </dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Attachment</dt>
            <dd class="mt-1 text-sm">
              <a v-if="report.attachment" :href="report.attachment" target="_blank" rel="noopener noreferrer"
                class="text-primary-600 hover:underline font-medium">Download attachment</a>
              <span v-else class="text-gray-400 italic">Not provided</span>
            </dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Created At</dt>
            <dd class="mt-1 text-sm" :class="valueClass(report.created_at)">
              {{ report.created_at ? formatDateTime(report.created_at) : 'Not provided' }}
            </dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Last Updated</dt>
            <dd class="mt-1 text-sm" :class="valueClass(report.updated_at)">
              {{ report.updated_at ? formatDateTime(report.updated_at) : 'Not provided' }}
            </dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-red-600">Escalated At</dt>
            <dd class="mt-1 text-sm" :class="valueClass(report.escalated_at)">
              {{ report.escalated_at ? formatDateTime(report.escalated_at) : 'Not escalated' }}
            </dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Forwarded to OpenCHS At</dt>
            <dd class="mt-1 text-sm" :class="valueClass(report.forwarded_to_openchs_at)">
              {{ report.forwarded_to_openchs_at ? formatDateTime(report.forwarded_to_openchs_at) : 'Not forwarded' }}
            </dd>
          </div>
          <div>
            <dt class="text-sm font-medium text-gray-600">Resolved At</dt>
            <dd class="mt-1 text-sm" :class="valueClass(report.resolved_at)">
              {{ report.resolved_at ? formatDateTime(report.resolved_at) : 'Not resolved' }}
            </dd>
          </div>
        </dl>
      </div>

      <!-- Internal Notes -->
      <div class="bg-yellow-50 p-6 rounded-lg border border-yellow-200">
        <h2 class="text-lg font-semibold text-gray-900 mb-4">Internal Notes</h2>
        <p v-if="report.notes" class="text-gray-700 whitespace-pre-wrap">{{ report.notes }}</p>
        <p v-else class="text-gray-400 italic text-sm">No internal notes have been added.</p>
      </div>

      <!-- Audit History -->
      <AuditHistory :history="history" :loading="loadingHistory" />
    </div>
  </div>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue'
  import { useRouter, useRoute } from 'vue-router'
  import { useToast } from 'vue-toastification'
  import { api, downloadBlobResponse } from '@/utils/api'
  import {
    ArrowLeftIcon,
    PencilIcon,
    ExclamationTriangleIcon,
    ShareIcon,
    ArrowDownTrayIcon
  } from '@heroicons/vue/24/outline'
  import AuditHistory from '@/components/common/AuditHistory.vue'

  const router = useRouter()
  const route = useRoute()
  const toast = useToast()

  const report = ref({})
  const history = ref([])
  const loading = ref(false)
  const loadingHistory = ref(false)
  const error = ref(null)
  const exportingPdf = ref(false)

  // The detail page deliberately renders every field the intake form can
  // capture, marking unanswered ones "Not provided" instead of hiding them, so
  // an agent can see what was asked as well as what was answered.
  const personFields = [
    { key: 'name', label: 'Name' },
    { key: 'age', label: 'Age' },
    { key: 'gender', label: 'Gender' },
    { key: 'relationship', label: 'Relationship' },
    { key: 'location', label: 'Location' },
  ]

  const affectedPersons = computed(() => {
    const persons = report.value?.affected_persons
    return Array.isArray(persons) ? persons : []
  })

  // Greyed italics for an absent value, normal weight for a real one.
  const valueClass = (value) => {
    const missing = value === null || value === undefined || value === ''
    return missing ? 'text-gray-400 italic' : 'text-gray-900'
  }

  const formatBoolean = (value) => {
    if (value === null || value === undefined) return 'Not provided'
    return value ? 'Yes' : 'No'
  }

  async function fetchReport() {
    loading.value = true
    error.value = null

    try {
      const response = await api.reports.get(route.params.id)
      report.value = response.data
      console.log('✅ Fetched report:', report.value)
      fetchHistory()
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

  async function fetchHistory() {
    loadingHistory.value = true
    try {
      const response = await api.reports.history(route.params.id)
      history.value = response.data
    } catch (err) {
      console.error('❌ Error fetching history:', err)
    } finally {
      loadingHistory.value = false
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
      'ESCALATED': 'Escalated',
      'FORWARDED': 'Forwarded to OpenCHS',
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
      'ESCALATED': 'bg-red-100 text-red-800',
      'FORWARDED': 'bg-purple-100 text-purple-800',
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

  async function downloadPdf() {
    exportingPdf.value = true
    try {
      const response = await api.reports.exportPdf(route.params.id)
      const refNumber = report.value.reference_number || route.params.id
      downloadBlobResponse(response, `report-${refNumber}.pdf`)
    } catch (err) {
      console.error('Failed to download report PDF:', err)
      toast.error('Failed to download PDF')
    } finally {
      exportingPdf.value = false
    }
  }

  async function updateStatus(newStatus) {
    if (!confirm(`Are you sure you want to change status to ${newStatus}?`)) return

    loading.value = true
    try {
      await api.reports.update(report.value.id, { status: newStatus })
      await fetchReport()
    } catch (err) {
      console.error('Failed to update status:', err)
      error.value = 'Failed to update status.'
    } finally {
      loading.value = false
    }
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
