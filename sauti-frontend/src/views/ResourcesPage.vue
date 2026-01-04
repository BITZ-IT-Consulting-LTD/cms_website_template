<template>
  <div class="bg-sauti-white min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <h1 class="page-header-title">RESOURCE CENTER</h1>
        <p class="page-header-subtitle">
          {{ settingsStore.settings.publications_description || `Access official guidance, research, and child
          protection materials provided by the National Helpline.` }}
        </p>
      </div>
    </header>

    <div class="container-custom section-padding section-rhythm">
      <!-- Statistics Dashboard -->
      <section aria-labelledby="stats-heading">
        <div class="flex items-center justify-between mb-12">
          <h2 id="stats-heading" class="campaign-header text-3xl text-sauti-darkGreen">
            {{ settingsStore.settings.resources_stats_title || `Impact Dashboard` }}
          </h2>
          <div class="pill bg-sauti-blue/10 text-sauti-blue">
            {{ settingsStore.settings.resources_stats_updated || `Real-time Statistics` }}
          </div>
        </div>

        <div v-if="statsLoading" class="py-20 text-center">
          <div class="spinner mx-auto mb-6"></div>
          <p class="text-sauti-darkGreen/50 font-bold">Fetching latest data...</p>
        </div>

        <div v-else-if="statsError" class="bg-sauti-red/5 rounded-[3rem] border-2 border-sauti-red/20 p-16 text-center">
          <ExclamationTriangleIcon class="w-16 h-16 text-sauti-red mx-auto mb-6" />
          <p class="text-sauti-red font-bold text-xl">{{ settingsStore.settings.resources_stats_error || `Resource
            statistics temporary unavailable` }}</p>
        </div>

        <div v-else class="space-y-12">
          <!-- Key Metrics -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div
              class="bg-sauti-darkGreen rounded-[2.5rem] p-10 text-sauti-white shadow-xl hover:scale-105 transition-transform duration-500">
              <h3 class="text-5xl font-bold mb-2 tabular-nums">{{ stats.total_reports || 0 }}</h3>
              <p class="campaign-header text-xs opacity-60">Total Reports Received</p>
            </div>

            <div
              class="bg-sauti-blue rounded-[2.5rem] p-10 text-sauti-white shadow-xl hover:scale-105 transition-transform duration-500">
              <h3 class="text-5xl font-bold mb-2 tabular-nums">{{ getCategoryCount('CHILD_PROTECTION') }}</h3>
              <p class="campaign-header text-xs opacity-60">Child Protection Cases</p>
            </div>

            <div
              class="bg-sauti-orange rounded-[2.5rem] p-10 text-sauti-white shadow-xl hover:scale-105 transition-transform duration-500">
              <h3 class="text-5xl font-bold mb-2 tabular-nums">{{ getCategoryCount('GBV') }}</h3>
              <p class="campaign-header text-xs opacity-60">GBV Reports Managed</p>
            </div>

            <div
              class="bg-sauti-lightGreen rounded-[2.5rem] p-10 text-sauti-white shadow-xl hover:scale-105 transition-transform duration-500">
              <h3 class="text-5xl font-bold mb-2 tabular-nums">{{ getCategoryCount('MIGRANT') }}</h3>
              <p class="campaign-header text-xs opacity-60">Migrant Worker Assistance</p>
            </div>
          </div>

          <!-- Charts Section -->
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-10">
            <!-- Doughnut Chart - Cases by Category -->
            <div
              class="bg-sauti-white rounded-[3rem] border-2 border-sauti-neutral p-10 shadow-sm transition-all duration-500 hover:shadow-2xl">
              <div class="flex items-center justify-between mb-10">
                <h3 class="text-2xl font-bold text-sauti-darkGreen">{{
                  settingsStore.settings.resources_cases_by_category || `Cases by Category` }}</h3>
                <div class="pill bg-sauti-blue/10 text-sauti-blue">Interactive</div>
              </div>
              <div class="h-80 flex items-center justify-center">
                <Doughnut :data="categoryChartData" :options="doughnutOptions" />
              </div>
            </div>

            <!-- Bar Chart - Reports Over Time -->
            <div
              class="bg-sauti-white rounded-[3rem] border-2 border-sauti-neutral p-10 shadow-sm transition-all duration-500 hover:shadow-2xl">
              <div class="flex items-center justify-between mb-10">
                <h3 class="text-2xl font-bold text-sauti-darkGreen">{{
                  settingsStore.settings.resources_reports_over_time || `Reports Over Time` }}</h3>
                <div class="pill bg-sauti-lightGreen/10 text-sauti-lightGreen">Last 6 Months</div>
              </div>
              <div class="h-80">
                <Bar :data="timeChartData" :options="barOptions" />
              </div>
            </div>
          </div>

          <!-- Status Distribution -->
          <div class="bg-sauti-white rounded-[3.5rem] border-4 border-sauti-blue p-10 shadow-sm transition-all">
            <h3 class="text-2xl font-bold text-sauti-darkGreen mb-10">Case Status Distribution</h3>
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
              <div class="text-center p-8 bg-sauti-white rounded-3xl border-2 border-sauti-orange group transition-all">
                <div class="text-5xl font-bold text-sauti-orange mb-3">{{ getStatusCount('PENDING') }}</div>
                <div class="campaign-header text-[10px] text-sauti-darkGreen">Pending</div>
              </div>
              <div class="text-center p-8 bg-sauti-white rounded-3xl border-2 border-sauti-blue group transition-all">
                <div class="text-5xl font-bold text-sauti-blue mb-3">{{ getStatusCount('IN_PROGRESS') }}</div>
                <div class="campaign-header text-[10px] text-sauti-darkGreen">In Progress</div>
              </div>
              <div
                class="text-center p-8 bg-sauti-white rounded-3xl border-2 border-sauti-lightGreen group transition-all">
                <div class="text-5xl font-bold text-sauti-lightGreen mb-3">{{ getStatusCount('RESOLVED') }}</div>
                <div class="campaign-header text-[10px] text-sauti-darkGreen">Resolved</div>
              </div>
              <div
                class="text-center p-8 bg-sauti-white rounded-3xl border-2 border-sauti-darkGreen group transition-all">
                <div class="text-5xl font-bold text-sauti-darkGreen mb-3">{{ getStatusCount('CLOSED') }}</div>
                <div class="campaign-header text-[10px] text-sauti-darkGreen">Closed</div>
              </div>
            </div>
          </div>

          <!-- New: Helpline Statistics Interactive Infographic -->
          <div v-if="callStats" class="bg-sauti-neutral/30 rounded-[4rem] p-12 lg:p-16 border-2 border-sauti-neutral">
            <div class="flex flex-col lg:flex-row gap-16">
              <!-- Info Cards Area -->
              <div class="lg:w-1/3 space-y-10">
                <div>
                  <h3 class="campaign-header text-sauti-blue text-sm mb-4">Live Helpline Data</h3>
                  <h2 class="text-4xl font-black text-sauti-darkGreen leading-tight">National Support Performance</h2>
                </div>

                <div class="grid grid-cols-1 gap-6">
                  <div
                    class="bg-white p-8 rounded-3xl shadow-sm border-l-8 border-sauti-blue flex items-center gap-6 group hover:translate-x-2 transition-transform duration-300">
                    <div class="w-14 h-14 bg-sauti-blue/10 rounded-2xl flex items-center justify-center shrink-0">
                      <PhoneIcon class="w-8 h-8 text-sauti-blue" />
                    </div>
                    <div>
                      <div class="text-3xl font-black text-sauti-darkGreen tabular-nums">{{ callStats.stats.calls_today
                        }}</div>
                      <div class="text-xs font-bold text-sauti-darkGreen/40 uppercase">Calls Answered Today</div>
                    </div>
                  </div>

                  <div
                    class="bg-white p-8 rounded-3xl shadow-sm border-l-8 border-sauti-orange flex items-center gap-6 group hover:translate-x-2 transition-transform duration-300">
                    <div class="w-14 h-14 bg-sauti-orange/10 rounded-2xl flex items-center justify-center shrink-0">
                      <ShieldCheckIcon class="w-8 h-8 text-sauti-orange" />
                    </div>
                    <div>
                      <div class="text-3xl font-black text-sauti-darkGreen tabular-nums">{{ callStats.stats.cases_today
                        }}</div>
                      <div class="text-xs font-bold text-sauti-darkGreen/40 uppercase">Cases Registered Today</div>
                    </div>
                  </div>

                  <div
                    class="bg-white p-8 rounded-3xl shadow-sm border-l-8 border-sauti-lightGreen flex items-center gap-6 group hover:translate-x-2 transition-transform duration-300">
                    <div class="w-14 h-14 bg-sauti-lightGreen/10 rounded-2xl flex items-center justify-center shrink-0">
                      <ChartBarIcon class="w-8 h-8 text-sauti-lightGreen" />
                    </div>
                    <div>
                      <div class="text-3xl font-black text-sauti-darkGreen tabular-nums">{{
                        callStats.stats.cases_ongoing }}</div>
                      <div class="text-xs font-bold text-sauti-darkGreen/40 uppercase">Active Case Load</div>
                    </div>
                  </div>

                  <!-- Total Stats (Historic) -->
                  <div class="pt-6 border-t border-sauti-neutral">
                    <div class="grid grid-cols-2 gap-4">
                      <div class="bg-sauti-darkGreen/5 p-6 rounded-[2rem] border border-sauti-darkGreen/10">
                        <div class="text-2xl font-black text-sauti-darkGreen tabular-nums">{{
                          Number(callStats.stats.calls_total).toLocaleString() }}</div>
                        <div class="text-[9px] font-bold text-sauti-darkGreen/50 uppercase tracking-tighter">Lifetime
                          Calls</div>
                      </div>
                      <div class="bg-sauti-blue/5 p-6 rounded-[2rem] border border-sauti-blue/10">
                        <div class="text-2xl font-black text-sauti-blue tabular-nums">{{
                          Number(callStats.stats.cases_total).toLocaleString() }}</div>
                        <div class="text-[9px] font-bold text-sauti-blue/50 uppercase tracking-tighter">Total Cases
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Call Trend Graph -->
              <div
                class="lg:w-2/3 bg-white rounded-[4rem] p-12 shadow-2xl border border-sauti-neutral relative overflow-hidden group">
                <div class="absolute top-0 right-0 p-10">
                  <div class="pill bg-sauti-blue/10 text-sauti-blue text-[10px] animate-pulse">Live Link Active</div>
                </div>
                <div class="mb-10">
                  <h3 class="text-2xl font-bold text-sauti-darkGreen flex items-center gap-3">
                    Call Frequency Trends
                  </h3>
                  <p class="text-sauti-darkGreen/50 font-bold text-sm">Hourly distribution of incoming calls by status
                  </p>
                </div>
                <div class="h-[420px]">
                  <Line :data="callTrendData" :options="lineOptions" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Downloadable Resources Section -->
      <section aria-labelledby="downloads-heading">
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
          <div>
            <h2 id="downloads-heading" class="campaign-header text-3xl text-sauti-darkGreen mb-4">
              {{ settingsStore.settings.resources_downloads_title || `Downloadable Resources` }}
            </h2>
            <p class="text-sauti-darkGreen/60 font-bold text-lg">Public awareness materials and official guidance.</p>
          </div>
          <div class="pill bg-sauti-blue/10 text-sauti-blue">
            {{ resources.length }} {{ settingsStore.settings.resources_available || `items available` }}
          </div>
        </div>

        <!-- Search & Filters -->
        <div class="bg-sauti-neutral rounded-[2.5rem] p-8 mb-16 shadow-none">
          <div class="flex flex-col md:flex-row gap-8">
            <div class="flex-1 relative group">
              <MagnifyingGlassIcon
                class="absolute left-6 top-1/2 transform -translate-y-1/2 w-6 h-6 text-sauti-blue group-focus-within:text-sauti-darkGreen transition-colors" />
              <input v-model="search" type="text"
                :placeholder="settingsStore.settings.resources_search_placeholder || `Search keywords...`"
                class="w-full pl-16 pr-6 py-4 bg-white shadow-sm border-none focus:ring-0 focus:shadow-md rounded-2xl font-bold text-sauti-darkGreen outline-none transition-all" />
            </div>
            <div class="relative min-w-[240px]">
              <select v-model="category"
                class="w-full appearance-none pl-6 pr-12 py-4 bg-white shadow-sm border-none focus:ring-0 focus:shadow-md rounded-2xl font-bold text-sauti-darkGreen uppercase tracking-widest text-[10px] outline-none transition-all cursor-pointer">
                <option value="">{{ settingsStore.settings.resources_all_categories || `All Categories` }}</option>
                <option v-for="cat in categories" :key="cat.slug || cat.id" :value="cat.slug || cat.id">
                  {{ cat.name }}
                </option>
              </select>
              <ChevronDownIcon
                class="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-sauti-blue pointer-events-none" />
            </div>
          </div>
        </div>

        <!-- Resources Loading -->
        <AppLoader v-if="loading" :message="settingsStore.settings.resources_loading" />

        <!-- Resources Grid -->
        <div v-else-if="resources.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
          <article v-for="resource in resources" :key="resource.id"
            class="group bg-sauti-white rounded-[3.5rem] border-2 border-sauti-neutral transition-all duration-500 hover:shadow-2xl hover:border-sauti-blue/30 transform hover:-translate-y-2 overflow-hidden flex flex-col">

            <div class="p-10 flex-1 flex flex-col">
              <div class="mb-8">
                <div class="w-16 h-16 rounded-2xl bg-sauti-blue/10 flex items-center justify-center mb-8">
                  <SpeakerWaveIcon v-if="isAudio(resource)" class="w-8 h-8 text-sauti-blue" />
                  <DocumentTextIcon v-else class="w-8 h-8 text-sauti-blue" />
                </div>
                <h3 class="text-2xl font-bold text-sauti-darkGreen mb-4 leading-tight line-clamp-2">{{ resource.title
                }}</h3>
                <p class="text-lg text-sauti-darkGreen/50 font-bold leading-relaxed line-clamp-3">{{
                  resource.description }}</p>
              </div>

              <div class="flex flex-wrap gap-3 mb-10 mt-auto">
                <span v-if="resource.category_name" class="pill bg-sauti-blue text-sauti-white">{{
                  resource.category_name }}</span>
                <span v-if="resource.language" class="pill bg-sauti-lightGreen text-sauti-white">{{
                  getLanguageName(resource.language) }}</span>
              </div>

              <div v-if="isAudio(resource) && resource.file" class="mb-8 p-4 bg-sauti-neutral rounded-2xl">
                <audio :src="resource.file" controls class="w-full"></audio>
              </div>

              <div class="flex items-center justify-between pt-8 border-t-2 border-sauti-neutral">
                <BaseCTA v-if="resource.file" :href="resource.file" variant="primary" class="!py-3 !px-6 text-[10px]"
                  external download>
                  Download
                </BaseCTA>
                <div class="text-[10px] font-bold text-sauti-darkGreen/40 uppercase tracking-widest">
                  <span class="text-sauti-darkGreen">{{ resource.download_count || 0 }}</span> Downloads
                </div>
              </div>
            </div>
          </article>
        </div>

        <!-- Empty State -->
        <div v-else
          class="text-center py-24 bg-sauti-neutral/30 rounded-[3rem] border-2 border-dashed border-sauti-blue max-w-2xl mx-auto">
          <div
            class="w-20 h-20 bg-sauti-white rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-sm border-2 border-sauti-blue">
            <MagnifyingGlassIcon class="w-10 h-10 text-sauti-blue" />
          </div>
          <h3 class="text-2xl font-bold text-sauti-darkGreen mb-2">{{ settingsStore.settings.resources_no_results ||
            'No Resources Found' }}</h3>
          <p class="text-sauti-darkGreen/50 font-bold mb-8">{{ settingsStore.settings.resources_no_results_subtitle ||
            'Try adjusting your search criteria.' }}</p>
          <button @click="search = ''; category = ''" class="btn btn-outline">Clear all filters</button>
        </div>

        <!-- Pagination -->
        <div v-if="pagination.next || pagination.previous" class="mt-20 flex justify-center gap-6">
          <button :disabled="!pagination.previous || loading" @click="prevPage"
            class="btn btn-outline px-10">Previous</button>
          <button :disabled="!pagination.next || loading" @click="nextPage" class="btn btn-outline px-10">Next</button>
        </div>
      </section>

      <!-- API & Developer Resources Section -->
      <section id="developer-resources" aria-labelledby="api-heading" class="section-padding pt-0">
        <div
          class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12 border-t-2 border-sauti-neutral pt-24">
          <div>
            <h2 id="api-heading" class="campaign-header text-3xl text-sauti-darkGreen mb-4">
              Developer & Data APIs
            </h2>
            <p class="text-sauti-darkGreen/60 font-bold text-lg">Programmatic access to normalized helpline statistics
              and reporting data.</p>
          </div>
          <div class="pill bg-sauti-orange/10 text-sauti-orange uppercase tracking-widest text-[10px] font-black">
            V1 API Stable
          </div>
        </div>

        <div class="bg-sauti-darkGreen rounded-[4rem] overflow-hidden shadow-2xl">
          <div class="grid grid-cols-1 lg:grid-cols-2">
            <!-- Documentation -->
            <div class="p-12 lg:p-16 space-y-8">
              <div class="w-16 h-16 rounded-2xl bg-sauti-white/10 flex items-center justify-center">
                <CodeBracketIcon class="w-8 h-8 text-sauti-lightGreen" />
              </div>
              <h3 class="text-3xl font-bold text-sauti-white">Normalized Call Statistics (Key-Pair Format)</h3>
              <p class="text-sauti-white/70 text-lg leading-relaxed font-bold">
                A semantic, chart-ready endpoint that transforms positional upstream call data into grouped key-pair
                objects. Ideal for direct frontend consumption.
              </p>

              <div class="space-y-4 pt-4">
                <div class="flex items-center gap-4 text-sauti-white/50 font-bold uppercase tracking-widest text-xs">
                  <GlobeAltIcon class="w-5 h-5 text-sauti-blue" />
                  Endpoint URL
                </div>
                <code
                  class="block p-4 bg-black/30 rounded-xl text-sauti-lightGreen font-mono text-sm break-all border border-white/5">
                  GET /api/v1/calls/stats/keypair/
                </code>
              </div>

              <div class="pt-8">
                <BaseCTA variant="outline" class="!border-sauti-white/20 !text-sauti-white hover:!bg-sauti-white/10"
                  href="/api/v1/calls/stats/keypair/" external>
                  Test Endpoint
                </BaseCTA>
              </div>
            </div>

            <!-- Sample Response -->
            <div class="bg-black/40 p-12 lg:p-16 border-l border-white/10">
              <div class="flex items-center justify-between mb-8">
                <span class="text-sauti-white/30 font-bold uppercase tracking-widest text-xs">Sample JSON
                  Response</span>
                <span class="text-sauti-lightGreen font-mono text-xs">application/json</span>
              </div>
              <pre class="text-sauti-white/80 font-mono text-sm overflow-x-auto leading-relaxed scrollbar-hide">
{
  "stats": {
    "calls_today": 342,
    "calls_total": 89230,
    "cases_today": 12,
    "cases_total": 4562,
    "cases_ongoing": 89
  },
  "calls": {
    "answered": {
      "36000": 27,
      "39600": 42
    },
    "abandoned": {
      "36000": 5,
      "39600": 8
    }
  }
}
              </pre>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
  import { ref, watch, onMounted, onUnmounted, computed } from 'vue'
  import { useResourcesStore } from '@/store/resources'
  import { useSettingsStore } from '@/store/settings'
  import { api } from '@/utils/axios'
  import AppLoader from '@/components/common/AppLoader.vue'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import {
    MagnifyingGlassIcon,
    ChevronDownIcon,
    DocumentTextIcon,
    SpeakerWaveIcon,
    ExclamationTriangleIcon,
    CodeBracketIcon,
    GlobeAltIcon,
    PhoneIcon,
    ShieldCheckIcon,
    ChartBarIcon
  } from '@heroicons/vue/24/outline'
  import {
    Chart as ChartJS,
    ArcElement,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale,
    Title,
    LineElement,
    PointElement
  } from 'chart.js'
  import { Doughnut, Bar, Line } from 'vue-chartjs'

  ChartJS.register(
    ArcElement,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale,
    Title,
    LineElement,
    PointElement
  )

  defineOptions({
    name: 'ResourcesPage'
  })

  const resourcesStore = useResourcesStore()
  const settingsStore = useSettingsStore()

  const resources = ref([])
  const loading = ref(true)
  const search = ref('')
  const category = ref('')
  const language = ref('')
  const categories = ref([])
  const pagination = ref({ count: 0, next: null, previous: null })

  // Statistics
  const statsLoading = ref(true)
  const statsError = ref(null)
  const stats = ref(null)

  // Call Statistics (v1 Normalized)
  const callStatsLoading = ref(true)
  const callStats = ref(null)

  // Polling reference
  let pollingInterval = null

  // Fetch statistics
  onMounted(async () => {
    await settingsStore.fetchGlobalSettings()
    try {
      const [cats] = await Promise.all([
        resourcesStore.fetchCategories(),
        fetchList(),
        fetchStats(),
        fetchCallStats()
      ])
      categories.value = Array.isArray(cats) ? cats : []

      // Setup polling every 3 minutes (180,000 ms)
      pollingInterval = setInterval(fetchCallStats, 180000)
    } catch (error) {
      console.error('Error initializing resources:', error)
      categories.value = []
    } finally {
      loading.value = false
    }
  })

  onUnmounted(() => {
    if (pollingInterval) {
      clearInterval(pollingInterval)
      pollingInterval = null
    }
  })

  async function fetchStats() {
    statsLoading.value = true
    statsError.value = null
    try {
      const response = await api.get('/reports/stats/public/')
      stats.value = response.data
    } catch (err) {
      console.error('Failed to fetch stats:', err)
      statsError.value = 'Failed to load statistics. Please try again later.'
    } finally {
      statsLoading.value = false
    }
  }

  async function fetchCallStats() {
    callStatsLoading.value = true
    try {
      const response = await api.get('/v1/calls/stats/keypair/')
      callStats.value = response.data
    } catch (err) {
      console.error('Failed to fetch call stats:', err)
    } finally {
      callStatsLoading.value = false
    }
  }

  // Helpline Call Trends Chart
  const callTrendData = computed(() => {
    if (!callStats.value?.calls) return { labels: [], datasets: [] }

    // Get all unique buckets (X-axis)
    const buckets = new Set()
    Object.values(callStats.value.calls).forEach(statusData => {
      Object.keys(statusData).forEach(bucket => buckets.add(bucket))
    })
    const sortedBuckets = Array.from(buckets).sort((a, b) => parseInt(a) - parseInt(b))

    // Format buckets as HH:MM
    const labels = sortedBuckets.map(b => {
      const totalSeconds = parseInt(b)
      const hours = Math.floor(totalSeconds / 3600) % 24
      const minutes = Math.floor((totalSeconds % 3600) / 60)
      return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`
    })

    const statusColors = {
      'answered': '#007BBF',   // Sauti Blue
      'abandoned': '#FF9933',  // Sauti Orange
      'busy': '#006633'        // Sauti Dark Green
    }

    const datasets = Object.keys(callStats.value.calls).map(status => {
      return {
        label: status.charAt(0).toUpperCase() + status.slice(1),
        borderColor: statusColors[status.toLowerCase()] || '#8CC63F',
        backgroundColor: (statusColors[status.toLowerCase()] || '#8CC63F') + '22',
        data: sortedBuckets.map(b => callStats.value.calls[status][b] || 0),
        tension: 0.4,
        fill: true,
        pointRadius: 4,
        pointHoverRadius: 6
      }
    })

    return { labels, datasets }
  })

  const lineOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top',
        labels: {
          usePointStyle: true,
          font: { family: 'Cronos Pro', weight: 'bold' }
        }
      },
      tooltip: {
        mode: 'index',
        intersect: false,
        backgroundColor: '#006633',
        titleFont: { family: 'Cronos Pro', size: 14, weight: 'bold' },
        bodyFont: { family: 'Cronos Pro', size: 12 }
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        grid: { color: '#E2E8F0' },
        ticks: { font: { family: 'Cronos Pro', weight: 'bold' } }
      },
      x: {
        grid: { display: false },
        ticks: { font: { family: 'Cronos Pro', weight: 'bold' } }
      }
    }
  }

  // Chart data
  const categoryChartData = computed(() => {
    if (!stats.value?.by_category) return { labels: [], datasets: [] }

    const labels = stats.value.by_category.map(item => formatCategory(item.category))
    const data = stats.value.by_category.map(item => item.count)

    return {
      labels,
      datasets: [{
        backgroundColor: [
          '#007BBF', // Sauti Blue
          '#FF9933', // Sauti Orange
          '#006633', // Sauti Dark Green
          '#8CC63F'  // Sauti Light Green
        ],
        borderWidth: 0,
        data
      }]
    }
  })

  const timeChartData = computed(() => {
    if (!stats.value?.over_time) return { labels: [], datasets: [] }

    const labels = stats.value.over_time.map(item => {
      const date = new Date(item.month)
      return date.toLocaleDateString('en-US', { month: 'short', year: 'numeric' })
    })
    const data = stats.value.over_time.map(item => item.count)

    return {
      labels,
      datasets: [{
        label: 'Reports',
        backgroundColor: '#007BBF', // Sauti Blue
        borderRadius: 16,
        barThickness: 24,
        data
      }]
    }
  })

  const doughnutOptions = {
    responsive: true,
    maintainAspectRatio: true,
    cutout: '75%',
    plugins: {
      legend: {
        position: 'bottom',
        labels: {
          padding: 32,
          font: {
            size: 11,
            weight: '900',
            family: 'Cronos Pro'
          },
          usePointStyle: true,
          pointStyle: 'rectRounded',
          color: '#006633'
        }
      },
      tooltip: {
        backgroundColor: '#006633',
        padding: 16,
        titleFont: {
          size: 14,
          weight: '900'
        },
        bodyFont: {
          size: 13,
          weight: '700'
        },
        cornerRadius: 16,
        displayColors: false
      }
    }
  }

  const barOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: false
      },
      tooltip: {
        backgroundColor: '#006633',
        padding: 16,
        titleFont: {
          size: 14,
          weight: '900'
        },
        bodyFont: {
          size: 13,
          weight: '700'
        },
        cornerRadius: 16,
        displayColors: false
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          stepSize: 1,
          font: {
            size: 11,
            weight: '900',
            family: 'Cronos Pro'
          },
          color: '#007BBF'
        },
        grid: {
          color: '#007BBF',
          drawBorder: false
        }
      },
      x: {
        ticks: {
          font: {
            size: 11,
            weight: '900',
            family: 'Cronos Pro'
          },
          color: '#007BBF'
        },
        grid: {
          display: false
        }
      }
    }
  }

  function formatCategory(code) {
    const map = {
      'CHILD_PROTECTION': 'Child Protection',
      'GBV': 'Gender-Based Violence',
      'MIGRANT': 'Migrant Worker',
      'PSEA': 'PSEA'
    }
    return map[code] || code
  }

  function getCategoryCount(category) {
    if (!stats.value?.by_category) return 0
    const found = stats.value.by_category.find(item => item.category === category)
    return found ? found.count : 0
  }

  function getStatusCount(status) {
    if (!stats.value?.by_status) return 0
    const found = stats.value.by_status.find(item => item.status === status)
    return found ? found.count : 0
  }

  watch([search, category, language], () => {
    fetchList()
  })

  async function fetchList() {
    loading.value = true
    try {
      const params = {
        status: 'PUBLISHED'
      }
      if (search.value) params.search = search.value
      if (category.value) params.category = category.value
      if (language.value) params.language = language.value
      await resourcesStore.fetchResources(params)
      resources.value = Array.isArray(resourcesStore.resources) ? resourcesStore.resources : []
      pagination.value = resourcesStore.pagination || { count: 0, next: null, previous: null }
    } catch (error) {
      console.error('Error fetching resources:', error)
      resources.value = []
    } finally {
      loading.value = false
    }
  }

  function nextPage() {
    if (!pagination.value.next) return
    fetchList()
  }

  function prevPage() {
    if (!pagination.value.previous) return
    fetchList()
  }

  function getLanguageName(code) {
    const languages = {
      'en': 'English',
      'lg': 'Luganda',
      'sw': 'Swahili'
    }
    return languages[code] || code.toUpperCase()
  }

  function isAudio(resource) {
    const type = (resource.file_type || '').toLowerCase()
    const url = (resource.file || '').toLowerCase()
    const exts = ['mp3', 'm4a', 'wav', 'ogg']
    return exts.some(ext => type.includes(ext) || url.endsWith(`.${ext}`))
  }
</script>
