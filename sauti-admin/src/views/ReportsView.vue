<template>
  <div class="p-6">
    <!-- Page Header -->
    <PageHeader :title="pageTitle" description="Manage and respond to child protection reports"
      action-label="Log New Report" :action-icon="PlusIcon" @action="$router.push('/reports/create')" />

    <div class="flex flex-col items-end gap-2 -mt-3 mb-4">
      <button @click="showExportPanel = !showExportPanel" :disabled="exportingCsv"
        class="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 flex items-center gap-2 shadow-sm disabled:opacity-50">
        <ArrowDownTrayIcon class="h-4 w-4" />
        {{ exportingCsv ? 'Preparing…' : 'Download All (CSV)' }}
      </button>

      <!-- CSV Export: optional date range, defaults to everything when left blank -->
      <div v-if="showExportPanel"
        class="bg-white border border-gray-200 rounded-md shadow-sm p-4 flex flex-wrap items-end gap-4">
        <div>
          <label class="block text-xs font-medium text-gray-600 mb-1">From</label>
          <input type="date" v-model="exportDateFrom"
            class="px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-red-500" />
        </div>
        <div>
          <label class="block text-xs font-medium text-gray-600 mb-1">To</label>
          <input type="date" v-model="exportDateTo"
            class="px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-red-500" />
        </div>
        <button @click="downloadAllCsv" :disabled="exportingCsv"
          class="px-4 py-2 bg-gray-800 text-white text-sm font-medium rounded-md hover:bg-gray-900 disabled:opacity-50">
          {{ exportingCsv ? 'Preparing…' : 'Download' }}
        </button>
        <button @click="showExportPanel = false; exportDateFrom = ''; exportDateTo = ''"
          class="px-4 py-2 text-sm font-medium text-gray-500 hover:text-gray-700">
          Cancel
        </button>
        <p class="w-full text-xs text-gray-400">Leave both blank to download everything.</p>
      </div>
    </div>

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
          <select v-model="filterType"
            class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-red-500 bg-white">
            <option value="">All Types</option>
            <option value="CHILD_PROTECTION">Child Protection</option>
            <option value="GBV">Gender-Based Violence</option>
            <option value="MIGRANT">Migrant Worker</option>
            <option value="PSEA">PSEA</option>
          </select>

          <select v-model="filterReportingFor"
            class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-red-500 bg-white">
            <option value="">Reporting For: Any</option>
            <option value="SELF">Self</option>
            <option value="ADULT_OTHER">Adult (Other)</option>
            <option value="CHILD">Child</option>
            <option value="MULTIPLE">Multiple People</option>
            <option value="UNSPECIFIED">Unspecified</option>
          </select>

          <select v-if="activeTab === 'all'" v-model="filterStatus"
            class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-red-500 bg-white">
            <option value="">Any Status</option>
            <option value="PENDING">Pending Review</option>
            <option value="IN_PROGRESS">In Progress</option>
            <option value="RESOLVED">Resolved</option>
            <option value="CLOSED">Closed</option>
          </select>

          <div class="flex items-center gap-2">
            <label class="text-sm text-gray-600">Age</label>
            <input v-model="filterAgeMin" type="number" min="0" placeholder="Min"
              class="w-20 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-red-500 bg-white" />
            <span class="text-gray-400">–</span>
            <input v-model="filterAgeMax" type="number" min="0" placeholder="Max"
              class="w-20 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-red-500 bg-white" />
          </div>

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
              <th @click="toggleSort('reference_number')"
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer select-none hover:text-gray-700">
                <span class="inline-flex items-center gap-1">
                  Case ID
                  <ChevronUpIcon v-if="sortField === 'reference_number' && sortDirection === 'asc'" class="h-3.5 w-3.5" />
                  <ChevronDownIcon v-else-if="sortField === 'reference_number' && sortDirection === 'desc'" class="h-3.5 w-3.5" />
                </span>
              </th>
              <th @click="toggleSort('category')"
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer select-none hover:text-gray-700">
                <span class="inline-flex items-center gap-1">
                  Type
                  <ChevronUpIcon v-if="sortField === 'category' && sortDirection === 'asc'" class="h-3.5 w-3.5" />
                  <ChevronDownIcon v-else-if="sortField === 'category' && sortDirection === 'desc'" class="h-3.5 w-3.5" />
                </span>
              </th>
              <th @click="toggleSort('status')"
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer select-none hover:text-gray-700">
                <span class="inline-flex items-center gap-1">
                  Status
                  <ChevronUpIcon v-if="sortField === 'status' && sortDirection === 'asc'" class="h-3.5 w-3.5" />
                  <ChevronDownIcon v-else-if="sortField === 'status' && sortDirection === 'desc'" class="h-3.5 w-3.5" />
                </span>
              </th>
              <th @click="toggleSort('location')"
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer select-none hover:text-gray-700">
                <span class="inline-flex items-center gap-1">
                  Location
                  <ChevronUpIcon v-if="sortField === 'location' && sortDirection === 'asc'" class="h-3.5 w-3.5" />
                  <ChevronDownIcon v-else-if="sortField === 'location' && sortDirection === 'desc'" class="h-3.5 w-3.5" />
                </span>
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Reporting For
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Incident Type
              </th>
              <th @click="toggleSort('reported_person_age')"
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer select-none hover:text-gray-700">
                <span class="inline-flex items-center gap-1">
                  Age
                  <ChevronUpIcon v-if="sortField === 'reported_person_age' && sortDirection === 'asc'" class="h-3.5 w-3.5" />
                  <ChevronDownIcon v-else-if="sortField === 'reported_person_age' && sortDirection === 'desc'" class="h-3.5 w-3.5" />
                </span>
              </th>
              <th @click="toggleSort('created_at')"
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer select-none hover:text-gray-700">
                <span class="inline-flex items-center gap-1">
                  Reported
                  <ChevronUpIcon v-if="sortField === 'created_at' && sortDirection === 'asc'" class="h-3.5 w-3.5" />
                  <ChevronDownIcon v-else-if="sortField === 'created_at' && sortDirection === 'desc'" class="h-3.5 w-3.5" />
                </span>
              </th>
              <th @click="toggleSort('assigned_to_name')"
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer select-none hover:text-gray-700">
                <span class="inline-flex items-center gap-1">
                  Assigned To
                  <ChevronUpIcon v-if="sortField === 'assigned_to_name' && sortDirection === 'asc'" class="h-3.5 w-3.5" />
                  <ChevronDownIcon v-else-if="sortField === 'assigned_to_name' && sortDirection === 'desc'" class="h-3.5 w-3.5" />
                </span>
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
                <div class="text-xs text-gray-400 mt-0.5">
                  <span v-if="!report.reporting_for || report.reporting_for === 'UNSPECIFIED'">
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
                  :class="statusClass(report.status)">
                  {{ formatStatus(report.status) }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-600">
                {{ report.location }}
                <div v-if="report.victim_location && report.victim_location !== report.location" class="text-xs text-gray-400">
                  Victim: {{ report.victim_location }}
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-600">
                {{ formatReportingFor(report.reporting_for) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-600">
                {{ report.incident_type ? formatType(report.incident_type) : '—' }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-600">
                {{ report.reported_person_age ?? '—' }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-600">
                {{ formatDate(report.created_at) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-600">
                {{ report.assigned_to_name || 'Unassigned' }}
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
                <div class="h-5 w-24 bg-gray-200 rounded-full animate-pulse"></div>
              </td>
              <td class="px-6 py-4">
                <div class="h-4 w-32 bg-gray-200 rounded animate-pulse"></div>
              </td>
              <td class="px-6 py-4">
                <div class="h-4 w-20 bg-gray-200 rounded animate-pulse"></div>
              </td>
              <td class="px-6 py-4">
                <div class="h-4 w-24 bg-gray-200 rounded animate-pulse"></div>
              </td>
              <td class="px-6 py-4">
                <div class="h-4 w-10 bg-gray-200 rounded animate-pulse"></div>
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
  import { useToast } from 'vue-toastification'
  import { api, downloadBlobResponse } from '@/utils/api'
  import { PageHeader, StatsGrid, StatCard } from '@/components/admin'
  import {
    PlusIcon,
    MagnifyingGlassIcon,
    ShieldExclamationIcon,
    ExclamationTriangleIcon,
    ClockIcon,
    CheckCircleIcon,
    EyeIcon,
    PencilIcon,
    ArrowDownTrayIcon,
    ChevronUpIcon,
    ChevronDownIcon
  } from '@heroicons/vue/24/outline'

  const router = useRouter()
  const route = useRoute()
  const toast = useToast()
  const exportingCsv = ref(false)
  const showExportPanel = ref(false)
  const exportDateFrom = ref('')
  const exportDateTo = ref('')

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
  const filterType = ref('')
  const filterStatus = ref('')
  const filterReportingFor = ref('')
  const filterAgeMin = ref('')
  const filterAgeMax = ref('')
  const currentPage = ref(1)
  const perPage = ref(10)
  const loading = ref(false)
  const error = ref(null)

  // Column sorting for the reports table. Defaults to the same order the
  // API already returns (newest created_at first), so the table doesn't
  // visibly re-order on first load.
  const sortField = ref('created_at')
  const sortDirection = ref('desc')

  // Watch search and filters to reset pagination
  watch([searchQuery, filterType, filterStatus, filterReportingFor, filterAgeMin, filterAgeMax, activeTab], () => {
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
      } else if (activeTab.value === 'archive') {
        if (report.status !== 'RESOLVED' && report.status !== 'CLOSED') return false
      }

      const searchLower = searchQuery.value.toLowerCase()
      const matchesSearch = !searchQuery.value ||
        report.reference_number?.toLowerCase().includes(searchLower) ||
        report.id.toLowerCase().includes(searchLower) ||
        report.location.toLowerCase().includes(searchLower) ||
        report.assigned_to_name?.toLowerCase().includes(searchLower) ||
        formatType(report.category).toLowerCase().includes(searchLower) ||
        (report.incident_type && formatType(report.incident_type).toLowerCase().includes(searchLower))

      const matchesType = !filterType.value || report.category === filterType.value
      const matchesStatus = !filterStatus.value || report.status === filterStatus.value
      const matchesReportingFor = !filterReportingFor.value || report.reporting_for === filterReportingFor.value

      const age = report.reported_person_age
      const matchesAgeMin = filterAgeMin.value === '' ||
        (age !== null && age !== undefined && age >= Number(filterAgeMin.value))
      const matchesAgeMax = filterAgeMax.value === '' ||
        (age !== null && age !== undefined && age <= Number(filterAgeMax.value))

      return matchesSearch && matchesType && matchesStatus && matchesReportingFor && matchesAgeMin && matchesAgeMax
    })
  })

  // Client-side sort: the table is fetched and filtered client-side already
  // (api.reports.list() has no server-side params in this view), so sorting
  // the already-filtered page in the browser is the simplest fit rather than
  // threading a sort param through the API.
  const sortedReports = computed(() => {
    const list = [...filteredReports.value]
    const field = sortField.value
    const direction = sortDirection.value === 'asc' ? 1 : -1

    list.sort((a, b) => {
      let av = a[field]
      let bv = b[field]

      if (field === 'created_at') {
        av = av ? new Date(av).getTime() : 0
        bv = bv ? new Date(bv).getTime() : 0
      } else if (field === 'reported_person_age') {
        av = av ?? -Infinity
        bv = bv ?? -Infinity
      } else {
        av = (av ?? '').toString().toLowerCase()
        bv = (bv ?? '').toString().toLowerCase()
      }

      if (av < bv) return -1 * direction
      if (av > bv) return 1 * direction
      return 0
    })

    return list
  })

  const totalPages = computed(() => Math.max(1, Math.ceil(sortedReports.value.length / perPage.value)))

  const startIndex = computed(() => (currentPage.value - 1) * perPage.value)
  const endIndex = computed(() => Math.min(currentPage.value * perPage.value, sortedReports.value.length))
  const pagedReports = computed(() => sortedReports.value.slice(startIndex.value, endIndex.value))

  function toggleSort(field) {
    if (sortField.value === field) {
      sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
    } else {
      sortField.value = field
      sortDirection.value = 'asc'
    }
  }

  const formatReportingFor = (value) => {
    const labels = {
      SELF: 'Self',
      ADULT_OTHER: 'Adult (Other)',
      CHILD: 'Child',
      MULTIPLE: 'Multiple People',
      UNSPECIFIED: 'Unspecified'
    }
    return labels[value] || value || '—'
  }

  const statusClass = (status) => {
    const classes = {
      PENDING: 'bg-yellow-100 text-yellow-800',
      IN_PROGRESS: 'bg-purple-100 text-purple-800',
      ESCALATED: 'bg-red-100 text-red-800',
      FORWARDED: 'bg-indigo-100 text-indigo-800',
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
      'ESCALATED': 'Escalated',
      'FORWARDED': 'Forwarded to OpenCHS',
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

  const downloadAllCsv = async () => {
    exportingCsv.value = true
    try {
      // Mirror the table's active filters into the export so "download what
      // I'm currently looking at" holds true, plus the optional date range.
      const params = {}
      if (filterStatus.value) params.status = filterStatus.value
      if (filterType.value) params.category = filterType.value
      if (filterReportingFor.value) params.reporting_for = filterReportingFor.value
      if (filterAgeMin.value !== '') params.age_min = filterAgeMin.value
      if (filterAgeMax.value !== '') params.age_max = filterAgeMax.value
      if (exportDateFrom.value) params.date_from = exportDateFrom.value
      if (exportDateTo.value) params.date_to = exportDateTo.value

      const response = await api.reports.exportCsv(params)

      let fallbackName
      if (exportDateFrom.value || exportDateTo.value) {
        const from = exportDateFrom.value || 'start'
        const to = exportDateTo.value || 'present'
        fallbackName = `case-reports-${from}_to_${to}.csv`
      } else {
        const today = new Date().toISOString().split('T')[0]
        fallbackName = `case-reports-${today}.csv`
      }
      downloadBlobResponse(response, fallbackName)
    } catch (err) {
      console.error('Error downloading reports CSV:', err)
      toast.error('Failed to download CSV')
    } finally {
      exportingCsv.value = false
    }
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
