<template>
  <div class="p-6">
    <!-- Page Header -->
    <PageHeader :title="pageTitle" description="Manage and respond to child protection reports"
      action-label="Log New Report" :action-icon="PlusIcon" @action="$router.push('/reports/create')" />

    <!-- Mini Dashboard -->
    <StatsGrid>
      <StatCard label="Total Active" :value="stats.total" :icon="ShieldExclamationIcon" color="blue" />
      <StatCard label="Critical" :value="stats.critical" :icon="ExclamationTriangleIcon" color="red" />
      <StatCard label="In Progress" :value="stats.inProgress" :icon="ClockIcon" color="orange" />
      <StatCard label="Resolved Today" :value="stats.resolvedToday" :icon="CheckCircleIcon" color="green" />
    </StatsGrid>

    <!-- Error Message -->
    <div v-if="error" class="bg-red-50 border-l-4 border-red-500 p-4 rounded-md">
      <div class="flex">
        <ExclamationTriangleIcon class="h-5 w-5 text-red-400 mr-3" />
        <p class="text-sm text-red-700">{{ error }}</p>
      </div>
    </div>

    <!-- Tabs and Filters -->
    <div class="bg-white rounded-lg shadow-sm border border-gray-200">
      <div class="border-b border-gray-200">
        <nav class="flex -mb-px px-6" aria-label="Tabs">
          <button v-for="tab in tabs" :key="tab.id" @click="activeTab = tab.id"
            class="whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm mr-8 transition-colors duration-200"
            :class="[
              activeTab === tab.id
                ? 'border-red-500 text-red-600'
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
            ]">
            <div class="flex items-center">
              <component :is="tab.icon" class="h-5 w-5 mr-2" />
              {{ tab.name }}
              <span v-if="tab.count !== undefined" class="ml-2 py-0.5 px-2 rounded-full text-xs"
                :class="activeTab === tab.id ? 'bg-red-100 text-red-600' : 'bg-gray-100 text-gray-600'">
                {{ tab.count }}
              </span>
            </div>
          </button>
        </nav>
      </div>

      <div class="p-4 bg-gray-50 flex flex-col md:flex-row gap-4">
        <div class="flex-1 relative">
          <MagnifyingGlassIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
          <input v-model="searchQuery" type="text" placeholder="Search by case ID, reporter name, or location..."
            class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-red-500 bg-white shadow-sm" />
        </div>

        <div class="flex flex-wrap gap-2">
          <select v-model="filterPriority"
            class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-red-500 bg-white">
            <option value="">All Priorities</option>
            <option value="critical">Critical</option>
            <option value="high">High</option>
            <option value="medium">Medium</option>
            <option value="low">Low</option>
          </select>

          <select v-model="filterType"
            class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-red-500 bg-white">
            <option value="">All Types</option>
            <option value="CHILD_PROTECTION">Child Protection</option>
            <option value="GBV">Gender-Based Violence</option>
            <option value="MIGRANT">Migrant Worker</option>
            <option value="PSEA">PSEA</option>
          </select>

          <select v-if="activeTab === 'all'" v-model="filterStatus"
            class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-red-500 bg-white">
            <option value="">Any Status</option>
            <option value="PENDING">Pending Review</option>
            <option value="IN_PROGRESS">In Progress</option>
            <option value="RESOLVED">Resolved</option>
            <option value="CLOSED">Closed</option>
          </select>

          <div class="flex items-center gap-2 ml-auto">
            <label class="text-sm text-gray-600">Per page</label>
            <select v-model.number="perPage"
              class="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-red-500 bg-white shadow-sm">
              <option :value="10">10</option>
              <option :value="20">20</option>
              <option :value="50">50</option>
            </select>
          </div>
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
            <tr v-for="report in pagedReports" :key="report.id" class="hover:bg-gray-50 cursor-pointer"
              @click="viewReport(report.id)">
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm font-medium text-gray-900">{{ report.reference_number || `#${report.id}` }}</div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm text-gray-900">{{ formatType(report.category) }}</div>
                <div v-if="report.incident_type" class="text-xs text-gray-500">{{ formatType(report.incident_type) }}
                </div>
                <div class="text-xs text-gray-400 mt-0.5">
                  <span v-if="report.reporting_for" class="font-medium">{{ report.reporting_for }}</span>
                  <span v-else>
                    {{ report.reported_person_age ? report.reported_person_age + 'y' : '?' }} •
                    {{ report.reported_person_gender || '?' }}
                  </span>
                  <span v-if="report.affected_persons && report.affected_persons.length > 0">
                    • {{ report.affected_persons.length }} Person(s)
                  </span>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full"
                  :class="priorityClass(report.priority)">
                  {{ report.priority }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span class="px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full"
                  :class="statusClass(report.status)">
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
                <button @click.stop="viewReport(report.id)" class="text-primary-600 hover:text-primary-900 mr-3">
                  <EyeIcon class="h-5 w-5" />
                </button>
                <button @click.stop="editReport(report.id)" class="text-blue-600 hover:text-blue-900">
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
    <div v-if="filteredReports.length > 0"
      class="flex items-center justify-between bg-white px-4 py-3 rounded-lg shadow-sm border border-gray-200">
      <div class="flex-1 flex justify-between sm:hidden">
        <button @click="previousPage" :disabled="currentPage === 1"
          class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 disabled:opacity-50">
          Previous
        </button>
        <button @click="nextPage" :disabled="currentPage === totalPages"
          class="ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 disabled:opacity-50">
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
            <button @click="previousPage" :disabled="currentPage === 1"
              class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50 disabled:opacity-50">
              Previous
            </button>
            <button @click="nextPage" :disabled="currentPage === totalPages"
              class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50 disabled:opacity-50">
              Next
            </button>
          </nav>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed, onMounted, watch } from 'vue'
  import { useRouter, useRoute } from 'vue-router'
  import { api } from '@/utils/api'
  import { PageHeader, StatsGrid, StatCard } from '@/components/admin'
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
    const currentTab = tabs.value.find(t => t.id === activeTab.value)
    return currentTab ? currentTab.name : 'Reports & Case Management'
  })

  // State
  const reports = ref([])
  const activeTab = ref(route.query.tab || 'active')
  const stats = ref({
    total: 0,
    critical: 0,
    inProgress: 0,
    resolvedToday: 0
  })

  const tabs = computed(() => [
    { id: 'active', name: 'Active Reports', icon: ShieldExclamationIcon, count: stats.value.total },
    { id: 'urgent', name: 'Urgent Cases', icon: ExclamationTriangleIcon, count: stats.value.critical },
    { id: 'archive', name: 'Case Archive', icon: CheckCircleIcon },
    { id: 'all', name: 'All Reports', icon: MagnifyingGlassIcon }
  ])

  const searchQuery = ref('')
  const filterPriority = ref('')
  const filterType = ref('')
  const filterStatus = ref('')
  const currentPage = ref(1)
  const perPage = ref(10)
  const loading = ref(false)
  const error = ref(null)

  // Watch search and filters to reset pagination
  watch([searchQuery, filterPriority, filterType, filterStatus, activeTab], () => {
    currentPage.value = 1
  })

  // Update query param when tab changes
  watch(activeTab, (newTab) => {
    router.replace({
      query: { ...route.query, tab: newTab }
    })
  })

  // Fetch reports from API
  async function fetchReports() {
    loading.value = true
    error.value = null

    try {
      const response = await api.reports.list()
      reports.value = response.data.results || response.data || []

      // Calculate stats from fetched data
      calculateStats()
    } catch (err) {
      console.error('❌ Error fetching reports:', err)
      error.value = 'Failed to load reports. Please try again.'
    } finally {
      loading.value = false
    }
  }

  // Calculate statistics from reports
  function calculateStats() {
    const now = new Date()
    const today = now.toISOString().split('T')[0]

    stats.value = {
      total: reports.value.filter(r => r.status !== 'CLOSED' && r.status !== 'RESOLVED').length,
      critical: reports.value.filter(r => (r.priority === 'critical' || r.priority === 'CRITICAL') && (r.status !== 'CLOSED' && r.status !== 'RESOLVED')).length,
      inProgress: reports.value.filter(r => r.status === 'IN_PROGRESS').length,
      resolvedToday: reports.value.filter(r => {
        const resolvedDate = r.resolved_at || r.updated_at
        return resolvedDate && resolvedDate.startsWith(today) && (r.status === 'RESOLVED' || r.status === 'CLOSED')
      }).length
    }
  }

  const filteredReports = computed(() => {
    return reports.value.filter(report => {
      // Tab Filtering
      if (activeTab.value === 'active') {
        if (report.status === 'RESOLVED' || report.status === 'CLOSED') return false
      } else if (activeTab.value === 'urgent') {
        if (report.status === 'RESOLVED' || report.status === 'CLOSED') return false
        if (report.priority !== 'critical' && report.priority !== 'CRITICAL') return false
      } else if (activeTab.value === 'archive') {
        if (report.status !== 'RESOLVED' && report.status !== 'CLOSED') return false
      }

      const searchLower = searchQuery.value.toLowerCase()
      const matchesSearch = !searchQuery.value ||
        report.reference_number?.toLowerCase().includes(searchLower) ||
        report.id.toLowerCase().includes(searchLower) ||
        report.location.toLowerCase().includes(searchLower) ||
        report.assigned_to?.toLowerCase().includes(searchLower) ||
        formatType(report.category).toLowerCase().includes(searchLower) ||
        (report.incident_type && formatType(report.incident_type).toLowerCase().includes(searchLower))

      const matchesPriority = !filterPriority.value || report.priority === filterPriority.value
      const matchesType = !filterType.value || report.category === filterType.value
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
    fetchReports()
  })
</script>

<style scoped>
  .sidebar-link {
    @apply flex items-center px-3 py-2 text-sm font-medium text-gray-700 rounded-md hover:bg-gray-100 hover:text-gray-900 transition-colors duration-200;
  }

  .sidebar-link.active {
    @apply bg-primary-50 text-primary-600;
  }
</style>
