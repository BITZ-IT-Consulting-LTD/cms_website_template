<template>
  <div class="p-6 space-y-6">
    <!-- Header -->
    <div class="flex justify-between items-start">
      <div>
        <h1 class="text-2xl font-bold text-gray-900">{{ pageTitle }}</h1>
        <p class="text-gray-600 mt-1">Manage and respond to child protection reports</p>
      </div>
      <router-link
        to="/reports/create"
        class="px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700 transition-colors duration-200 flex items-center font-medium shadow-sm"
      >
        <PlusIcon class="h-5 w-5 mr-2" />
        Log New Report
      </router-link>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total Active</p>
            <p class="text-3xl font-bold text-gray-900 mt-2">{{ stats.total }}</p>
          </div>
          <div class="p-3 bg-blue-100 rounded-lg">
            <ShieldExclamationIcon class="h-8 w-8 text-blue-600" />
          </div>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Critical</p>
            <p class="text-3xl font-bold text-red-600 mt-2">{{ stats.critical }}</p>
          </div>
          <div class="p-3 bg-red-100 rounded-lg">
            <ExclamationTriangleIcon class="h-8 w-8 text-red-600" />
          </div>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">In Progress</p>
            <p class="text-3xl font-bold text-orange-600 mt-2">{{ stats.inProgress }}</p>
          </div>
          <div class="p-3 bg-orange-100 rounded-lg">
            <ClockIcon class="h-8 w-8 text-orange-600" />
          </div>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Resolved Today</p>
            <p class="text-3xl font-bold text-green-600 mt-2">{{ stats.resolvedToday }}</p>
          </div>
          <div class="p-3 bg-green-100 rounded-lg">
            <CheckCircleIcon class="h-8 w-8 text-green-600" />
          </div>
        </div>
      </div>
    </div>

    <!-- Filters and Search -->
    <div class="bg-white p-4 rounded-lg shadow-sm">
      <div class="flex flex-col md:flex-row gap-4">
        <div class="flex-1 relative">
          <MagnifyingGlassIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search by case ID, reporter name, or location..."
            class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        </div>
        
        <select
          v-model="filterPriority"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Priorities</option>
          <option value="critical">Critical</option>
          <option value="high">High</option>
          <option value="medium">Medium</option>
          <option value="low">Low</option>
        </select>

        <select
          v-model="filterType"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Types</option>
          <option value="CHILD_PROTECTION">Child Protection</option>
          <option value="GBV">Gender-Based Violence</option>
          <option value="MIGRANT">Migrant Worker</option>
          <option value="PSEA">PSEA</option>
        </select>

        <select
          v-model="filterStatus"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Statuses</option>
          <option value="PENDING">Pending Review</option>
          <option value="IN_PROGRESS">In Progress</option>
          <option value="RESOLVED">Resolved</option>
          <option value="CLOSED">Closed</option>
        </select>

        <div class="flex items-center gap-2 ml-auto">
          <label class="text-sm text-gray-600">Per page</label>
          <select
            v-model.number="perPage"
            class="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
          >
            <option :value="10">10</option>
            <option :value="20">20</option>
            <option :value="50">50</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Reports Table -->
    <div class="bg-white rounded-lg shadow-sm overflow-hidden">
      <div class="overflow-x-auto">
        <table class="min-w-full">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Case ID
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Type
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Priority
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Status
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Location
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Reported
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Assigned To
              </th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                Actions
              </th>
            </tr>
          </thead>
          <tbody v-if="!loading" class="bg-white">
            <tr v-for="report in pagedReports" :key="report.id" class="hover:bg-gray-50 cursor-pointer" @click="viewReport(report.id)">
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm font-medium text-gray-900">{{ report.reference_number || `#${report.id}` }}</div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm text-gray-900">{{ formatType(report.type) }}</div>
                <div v-if="report.incident_type" class="text-xs text-gray-500">{{ formatType(report.incident_type) }}</div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span
                  class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full"
                  :class="priorityClass(report.priority)"
                >
                  {{ report.priority }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span
                  class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full"
                  :class="statusClass(report.status)"
                >
                  {{ formatStatus(report.status) }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-600">
                {{ report.location }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-600">
                {{ formatDate(report.created_at) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-600">
                {{ report.assigned_to || 'Unassigned' }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <button
                  @click.stop="viewReport(report.id)"
                  class="text-primary-600 hover:text-primary-900 mr-3"
                >
                  <EyeIcon class="h-5 w-5" />
                </button>
                <button
                  @click.stop="editReport(report.id)"
                  class="text-blue-600 hover:text-blue-900"
                >
                  <PencilIcon class="h-5 w-5" />
                </button>
              </td>
            </tr>
          </tbody>
          <tbody v-else class="bg-white">
            <tr v-for="n in 5" :key="n">
              <td class="px-6 py-4">
                <div class="h-4 w-20 bg-gray-200 rounded animate-pulse"></div>
              </td>
              <td class="px-6 py-4">
                <div class="h-4 w-28 bg-gray-200 rounded animate-pulse"></div>
              </td>
              <td class="px-6 py-4">
                <div class="h-5 w-16 bg-gray-200 rounded-full animate-pulse"></div>
              </td>
              <td class="px-6 py-4">
                <div class="h-5 w-24 bg-gray-200 rounded-full animate-pulse"></div>
              </td>
              <td class="px-6 py-4">
                <div class="h-4 w-32 bg-gray-200 rounded animate-pulse"></div>
              </td>
              <td class="px-6 py-4">
                <div class="h-4 w-24 bg-gray-200 rounded animate-pulse"></div>
              </td>
              <td class="px-6 py-4">
                <div class="h-4 w-24 bg-gray-200 rounded animate-pulse"></div>
              </td>
              <td class="px-6 py-4 text-right">
                <div class="h-5 w-12 ml-auto bg-gray-200 rounded animate-pulse"></div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Empty State -->
      <div v-if="!loading && filteredReports.length === 0" class="text-center py-12">
        <ShieldExclamationIcon class="mx-auto h-12 w-12 text-gray-400" />
        <h3 class="mt-2 text-sm font-medium text-gray-900">No reports found</h3>
        <p class="mt-1 text-sm text-gray-500">Try adjusting your search or filters</p>
      </div>
    </div>

    <!-- Pagination -->
    <div v-if="filteredReports.length > 0" class="flex items-center justify-between bg-white px-4 py-3 rounded-lg shadow-sm border border-gray-200">
      <div class="flex-1 flex justify-between sm:hidden">
        <button
          @click="previousPage"
          :disabled="currentPage === 1"
          class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 disabled:opacity-50"
        >
          Previous
        </button>
        <button
          @click="nextPage"
          :disabled="currentPage === totalPages"
          class="ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 disabled:opacity-50"
        >
          Next
        </button>
      </div>
      <div class="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
        <div>
          <p class="text-sm text-gray-700">
            Showing
            <span class="font-medium">{{ startIndex + 1 }}</span>
            to
            <span class="font-medium">{{ endIndex }}</span>
            of
            <span class="font-medium">{{ filteredReports.length }}</span>
            results
          </p>
        </div>
        <div>
          <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px">
            <button
              @click="previousPage"
              :disabled="currentPage === 1"
              class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50 disabled:opacity-50"
            >
              Previous
            </button>
            <button
              @click="nextPage"
              :disabled="currentPage === totalPages"
              class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50 disabled:opacity-50"
            >
              Next
            </button>
          </nav>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import {
  PlusIcon,
  MagnifyingGlassIcon,
  ShieldExclamationIcon,
  ExclamationTriangleIcon,
  ClockIcon,
  CheckCircleIcon,
  EyeIcon,
  PencilIcon
} from '@heroicons/vue/24/outline'

const router = useRouter()
const route = useRoute()

const pageTitle = computed(() => {
  if (route.name === 'reports-urgent') return 'Urgent Cases'
  if (route.name === 'reports-archive') return 'Closed Cases'
  return 'Active Reports'
})

// Mock data - Replace with actual API calls
const reports = ref([
  {
    id: 'SAUTI-CH-20250124103015',
    type: 'CHILD_PROTECTION',
    incident_type: 'child_neglect',
    priority: 'critical',
    status: 'IN_PROGRESS',
    location: 'Kampala, Central',
    created_at: '2025-01-24T10:30:00Z',
    assigned_to: 'Jane Mukasa',
    reference_number: 'SAUTI-CH-20250124103015'
  },
  {
    id: 'SAUTI-CH-20250124091522',
    type: 'CHILD_PROTECTION',
    incident_type: 'physical_violence',
    priority: 'high',
    status: 'PENDING',
    location: 'Gulu, Northern',
    created_at: '2025-01-24T09:15:00Z',
    assigned_to: null,
    reference_number: 'SAUTI-CH-20250124091522'
  },
  {
    id: 'SAUTI-GB-20250123164530',
    type: 'GBV',
    incident_type: 'sexual_violence',
    priority: 'critical',
    status: 'IN_PROGRESS',
    location: 'Mbarara, Western',
    created_at: '2025-01-23T16:45:00Z',
    assigned_to: 'Peter Okello',
    reference_number: 'SAUTI-GB-20250123164530'
  },
  {
    id: 'SAUTI-CH-20250123142045',
    type: 'CHILD_PROTECTION',
    incident_type: 'emotional_abuse',
    priority: 'medium',
    status: 'PENDING',
    location: 'Jinja, Eastern',
    created_at: '2025-01-23T14:20:00Z',
    assigned_to: 'Sarah Nambi',
    reference_number: 'SAUTI-CH-20250123142045'
  },
  {
    id: 'SAUTI-CH-20250122110030',
    type: 'CHILD_PROTECTION',
    incident_type: 'child_neglect',
    priority: 'high',
    status: 'IN_PROGRESS',
    location: 'Kampala, Central',
    created_at: '2025-01-22T11:00:00Z',
    assigned_to: 'Jane Mukasa',
    reference_number: 'SAUTI-CH-20250122110030'
  },
  {
    id: 'SAUTI-MI-20250122104515',
    type: 'MIGRANT',
    incident_type: 'trafficking',
    priority: 'critical',
    status: 'IN_PROGRESS',
    location: 'Kampala, Central',
    created_at: '2025-01-22T10:45:00Z',
    assigned_to: 'Peter Okello',
    reference_number: 'SAUTI-MI-20250122104515'
  },
  {
    id: 'SAUTI-GB-20250121153020',
    type: 'GBV',
    incident_type: 'physical_violence',
    priority: 'high',
    status: 'RESOLVED',
    location: 'Kampala, Central',
    created_at: '2025-01-21T15:30:00Z',
    assigned_to: 'Sarah Nambi',
    reference_number: 'SAUTI-GB-20250121153020'
  },
  {
    id: 'SAUTI-CH-20250121090010',
    type: 'CHILD_PROTECTION',
    incident_type: 'child_neglect',
    priority: 'medium',
    status: 'PENDING',
    location: 'Mbale, Eastern',
    created_at: '2025-01-21T09:00:00Z',
    assigned_to: null,
    reference_number: 'SAUTI-CH-20250121090010'
  },
  {
    id: 'SAUTI-GB-20250120140025',
    type: 'GBV',
    incident_type: 'economic_violence',
    priority: 'medium',
    status: 'IN_PROGRESS',
    location: 'Kampala, Central',
    created_at: '2025-01-20T14:00:00Z',
    assigned_to: 'Jane Mukasa',
    reference_number: 'SAUTI-GB-20250120140025'
  },
  {
    id: 'SAUTI-CH-20250119120050',
    type: 'CHILD_PROTECTION',
    incident_type: 'sexual_violence',
    priority: 'critical',
    status: 'IN_PROGRESS',
    location: 'Gulu, Northern',
    created_at: '2025-01-19T12:00:00Z',
    assigned_to: 'Peter Okello',
    reference_number: 'SAUTI-CH-20250119120050'
  },
  {
    id: 'SAUTI-CH-20250118103040',
    type: 'CHILD_PROTECTION',
    incident_type: 'child_exploitation',
    priority: 'high',
    status: 'PENDING',
    location: 'Kampala, Central',
    created_at: '2025-01-18T10:30:00Z',
    assigned_to: null,
    reference_number: 'SAUTI-CH-20250118103040'
  },
  {
    id: 'SAUTI-GB-20250117150015',
    type: 'GBV',
    incident_type: 'harmful_traditional_practices',
    priority: 'medium',
    status: 'RESOLVED',
    location: 'Mbarara, Western',
    created_at: '2025-01-17T15:00:00Z',
    assigned_to: 'Sarah Nambi',
    reference_number: 'SAUTI-GB-20250117150015'
  },
  {
    id: 'SAUTI-CH-20250116110030',
    type: 'CHILD_PROTECTION',
    incident_type: 'child_neglect',
    priority: 'high',
    status: 'IN_PROGRESS',
    location: 'Kampala, Central',
    created_at: '2025-01-16T11:00:00Z',
    assigned_to: 'Jane Mukasa',
    reference_number: 'SAUTI-CH-20250116110030'
  },
  {
    id: 'SAUTI-MI-20250115143020',
    type: 'MIGRANT',
    incident_type: 'trafficking',
    priority: 'critical',
    status: 'IN_PROGRESS',
    location: 'Jinja, Eastern',
    created_at: '2025-01-15T14:30:00Z',
    assigned_to: 'Peter Okello',
    reference_number: 'SAUTI-MI-20250115143020'
  },
  {
    id: 'SAUTI-GB-20250114090045',
    type: 'GBV',
    incident_type: 'physical_violence',
    priority: 'high',
    status: 'PENDING',
    location: 'Kampala, Central',
    created_at: '2025-01-14T09:00:00Z',
    assigned_to: null,
    reference_number: 'SAUTI-GB-20250114090045'
  },
  {
    id: 'SAUTI-CH-20250113120010',
    type: 'CHILD_PROTECTION',
    incident_type: 'child_neglect',
    priority: 'medium',
    status: 'RESOLVED',
    location: 'Kampala, Central',
    created_at: '2025-01-13T12:00:00Z',
    assigned_to: 'Sarah Nambi',
    reference_number: 'SAUTI-CH-20250113120010'
  }
])

const stats = ref({
  total: 2761, // Total active cases (Child Neglect is highest category)
  critical: 312, // Critical priority cases
  inProgress: 1845, // Cases in progress
  resolvedToday: 23 // Cases resolved today
})

const searchQuery = ref('')
const filterPriority = ref('')
const filterType = ref('')
const filterStatus = ref('')
const currentPage = ref(1)
const perPage = ref(10)
const loading = ref(false)

const filteredReports = computed(() => {
  return reports.value.filter(report => {
    const searchLower = searchQuery.value.toLowerCase()
    const matchesSearch = !searchQuery.value ||
      report.reference_number?.toLowerCase().includes(searchLower) ||
      report.id.toLowerCase().includes(searchLower) ||
      report.location.toLowerCase().includes(searchLower) ||
      report.assigned_to?.toLowerCase().includes(searchLower) ||
      formatType(report.type).toLowerCase().includes(searchLower) ||
      (report.incident_type && formatType(report.incident_type).toLowerCase().includes(searchLower))
    
    const matchesPriority = !filterPriority.value || report.priority === filterPriority.value
    const matchesType = !filterType.value || report.type === filterType.value
    const matchesStatus = !filterStatus.value || report.status === filterStatus.value

    return matchesSearch && matchesPriority && matchesType && matchesStatus
  })
})

const totalPages = computed(() => Math.max(1, Math.ceil(filteredReports.value.length / perPage.value)))

const startIndex = computed(() => (currentPage.value - 1) * perPage.value)
const endIndex = computed(() => Math.min(currentPage.value * perPage.value, filteredReports.value.length))
const pagedReports = computed(() => filteredReports.value.slice(startIndex.value, endIndex.value))

const priorityClass = (priority) => {
  const classes = {
    critical: 'bg-red-100 text-red-800',
    high: 'bg-orange-100 text-orange-800',
    medium: 'bg-yellow-100 text-yellow-800',
    low: 'bg-green-100 text-green-800'
  }
  return classes[priority] || 'bg-gray-100 text-gray-800'
}

const statusClass = (status) => {
  const classes = {
    PENDING: 'bg-yellow-100 text-yellow-800',
    IN_PROGRESS: 'bg-purple-100 text-purple-800',
    RESOLVED: 'bg-green-100 text-green-800',
    CLOSED: 'bg-gray-100 text-gray-800',
    // Legacy support
    new: 'bg-blue-100 text-blue-800',
    in_progress: 'bg-purple-100 text-purple-800',
    pending: 'bg-yellow-100 text-yellow-800',
    resolved: 'bg-green-100 text-green-800'
  }
  return classes[status] || 'bg-gray-100 text-gray-800'
}

const formatType = (type) => {
  if (!type) return 'Unknown'
  const typeMap = {
    'CHILD_PROTECTION': 'Child Protection',
    'GBV': 'Gender-Based Violence',
    'MIGRANT': 'Migrant Worker',
    'PSEA': 'PSEA',
    'child_neglect': 'Child Neglect',
    'physical_violence': 'Physical Violence',
    'sexual_violence': 'Sexual Violence',
    'economic_violence': 'Economic Violence',
    'emotional_abuse': 'Emotional Abuse',
    'child_exploitation': 'Child Exploitation',
    'trafficking': 'Trafficking',
    'harmful_traditional_practices': 'Harmful Traditional Practices'
  }
  return typeMap[type] || type.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')
}

const formatStatus = (status) => {
  const statusMap = {
    'PENDING': 'Pending Review',
    'IN_PROGRESS': 'In Progress',
    'RESOLVED': 'Resolved',
    'CLOSED': 'Closed',
    // Legacy support
    'pending': 'Pending',
    'in_progress': 'In Progress',
    'resolved': 'Resolved',
    'new': 'New'
  }
  return statusMap[status] || status.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')
}

const formatDate = (date) => {
  const d = new Date(date)
  const now = new Date()
  const diffHours = Math.floor((now - d) / (1000 * 60 * 60))
  
  if (diffHours < 1) return 'Just now'
  if (diffHours < 24) return `${diffHours}h ago`
  if (diffHours < 48) return 'Yesterday'
  return d.toLocaleDateString()
}

const viewReport = (id) => {
  router.push(`/reports/${id}`)
}

const editReport = (id) => {
  router.push(`/reports/${id}/edit`)
}

const previousPage = () => {
  if (currentPage.value > 1) currentPage.value--
}

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++
}

onMounted(() => {
  // Placeholder for fetch; show skeleton very briefly to communicate loading state
  loading.value = true
  setTimeout(() => { loading.value = false }, 300)
})
</script>

<style scoped>
.sidebar-link {
  @apply flex items-center px-3 py-2 text-sm font-medium text-gray-700 rounded-md hover:bg-gray-100 hover:text-gray-900 transition-colors duration-200;
}

.sidebar-link.active {
  @apply bg-primary-50 text-primary-700;
}
</style>
