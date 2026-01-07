<template>
  <div class="bg-neutral-white min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <h1 class="page-header-title">GET HELP</h1>
        <p class="page-header-subtitle">
          Find life-saving advice, helpful guides, and information on how we are making Uganda safer.
        </p>
      </div>
    </header>

    <div class="section-padding !pt-0">
      <div class="container-custom">
        <!-- Support in a Flash (Flash Pattern) -->
        <section class="bg-primary/5 p-8 md:p-12 rounded-[3.5rem] border-2 border-primary/10 mb-16 shadow-sm">
          <h2 class="campaign-header text-xl text-primary mb-8 flex items-center gap-3">
            <ShieldCheckIcon class="w-6 h-6 text-primary" />
            Support in a Flash
          </h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
            <div class="space-y-4">
              <p class="text-black font-bold text-lg">Help is Free</p>
              <p class="text-black/60 text-sm leading-relaxed">All materials and helpline calls are **100%
                toll-free**.</p>
            </div>
            <div class="space-y-4">
              <p class="text-black font-bold text-lg">Help is Ready</p>
              <p class="text-black/60 text-sm leading-relaxed">Download guides for **Child Protection and Safety**
                instantly.</p>
            </div>
            <div class="space-y-4">
              <p class="text-black font-bold text-lg">Help is Human</p>
              <p class="text-black/60 text-sm leading-relaxed">Speak to a certified counselor by **calling 116
                anytime**.</p>
            </div>
          </div>
        </section>
      </div>

      <div class="container-custom section-rhythm">
        <!-- Statistics Dashboard -->
        <section aria-labelledby="stats-heading">
          <div class="flex items-center justify-between mb-12">
            <h2 id="stats-heading" class="campaign-header text-3xl text-secondary">
              {{ resourcesStatsTitle }}
            </h2>
            <div class="pill bg-primary/10 text-primary">
              {{ resourcesStatsUpdated }}
            </div>
          </div>

          <div v-if="statsLoading" class="py-20 text-center">
            <div class="spinner mx-auto mb-6"></div>
            <p class="text-black/50 font-bold">Fetching latest data...</p>
          </div>

          <div v-else-if="statsError"
            class="bg-emergency/5 rounded-[3rem] border-2 border-emergency/20 p-16 text-center">
            <ExclamationTriangleIcon class="w-16 h-16 text-emergency mx-auto mb-6" />
            <p class="text-emergency font-bold text-xl">{{ resourcesStatsError }}</p>
          </div>

          <div v-else class="space-y-12">
            <!-- Key Metrics -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
              <div
                class="bg-secondary rounded-[2.5rem] p-10 text-neutral-white shadow-xl hover:scale-105 transition-transform duration-500">
                <h3 class="text-5xl font-bold mb-2 tabular-nums">{{ stats.total_reports || 0 }}</h3>
                <p class="campaign-header text-xs opacity-60">Total Reports Received</p>
              </div>

              <div
                class="bg-primary rounded-[2.5rem] p-10 text-neutral-white shadow-xl hover:scale-105 transition-transform duration-500">
                <h3 class="text-5xl font-bold mb-2 tabular-nums">{{ getCategoryCount('CHILD_PROTECTION') }}</h3>
                <p class="campaign-header text-xs opacity-60">Child Protection Cases</p>
              </div>

              <div
                class="bg-hotline rounded-[2.5rem] p-10 text-neutral-white shadow-xl hover:scale-105 transition-transform duration-500">
                <h3 class="text-5xl font-bold mb-2 tabular-nums">{{ getCategoryCount('GBV') }}</h3>
                <p class="campaign-header text-xs opacity-60">GBV Reports Managed</p>
              </div>

              <div
                class="bg-secondary-light rounded-[2.5rem] p-10 text-neutral-white shadow-xl hover:scale-105 transition-transform duration-500">
                <h3 class="text-5xl font-bold mb-2 tabular-nums">{{ getCategoryCount('MIGRANT') }}</h3>
                <p class="campaign-header text-xs opacity-60">Migrant Worker Assistance</p>
              </div>
            </div>

            <!-- Charts Section -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-10">
              <!-- Doughnut Chart - Cases by Category -->
              <div
                class="bg-neutral-white rounded-[3rem] border-2 border-neutral-offwhite p-10 shadow-sm transition-all duration-500 hover:shadow-2xl">
                <div class="flex items-center justify-between mb-10">
                  <h3 class="text-2xl font-bold text-secondary">{{ resourcesCasesByCategory }}</h3>
                  <div class="pill bg-primary/10 text-primary">Interactive</div>
                </div>
                <div class="h-80 flex items-center justify-center">
                  <Doughnut :data="categoryChartData" :options="doughnutOptions" />
                </div>
              </div>

              <!-- Bar Chart - Reports Over Time -->
              <div
                class="bg-neutral-white rounded-[3rem] border-2 border-neutral-offwhite p-10 shadow-sm transition-all duration-500 hover:shadow-2xl">
                <div class="flex items-center justify-between mb-10">
                  <h3 class="text-2xl font-bold text-secondary">{{ resourcesReportsOverTime }}</h3>
                  <div class="pill bg-secondary-light/10 text-secondary-light">Last 6 Months</div>
                </div>
                <div class="h-80">
                  <Bar :data="timeChartData" :options="barOptions" />
                </div>
              </div>
            </div>

            <!-- Status Distribution -->
            <div class="bg-neutral-white rounded-[3.5rem] border-4 border-primary p-10 shadow-sm transition-all">
              <h3 class="text-2xl font-bold text-secondary mb-10">Case Status Distribution</h3>
              <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
                <div class="text-center p-8 bg-neutral-white rounded-3xl border-2 border-hotline group transition-all">
                  <div class="text-5xl font-bold text-hotline mb-3">{{ getStatusCount('PENDING') }}</div>
                  <div class="campaign-header text-[10px] text-secondary">Pending</div>
                </div>
                <div class="text-center p-8 bg-neutral-white rounded-3xl border-2 border-primary group transition-all">
                  <div class="text-5xl font-bold text-primary mb-3">{{ getStatusCount('IN_PROGRESS') }}</div>
                  <div class="campaign-header text-[10px] text-secondary">In Progress</div>
                </div>
                <div
                  class="text-center p-8 bg-neutral-white rounded-3xl border-2 border-secondary-light group transition-all">
                  <div class="text-5xl font-bold text-secondary-light mb-3">{{ getStatusCount('RESOLVED') }}</div>
                  <div class="campaign-header text-[10px] text-secondary">Resolved</div>
                </div>
                <div
                  class="text-center p-8 bg-neutral-white rounded-3xl border-2 border-secondary group transition-all">
                  <div class="text-5xl font-bold text-secondary mb-3">{{ getStatusCount('CLOSED') }}</div>
                  <div class="campaign-header text-[10px] text-secondary">Closed</div>
                </div>
              </div>
            </div>

            <!-- New: Helpline Statistics Interactive Infographic -->
            <div v-if="callStats"
              class="bg-neutral-offwhite/30 rounded-[4rem] p-12 lg:p-16 border-2 border-neutral-offwhite">
              <div class="flex flex-col lg:flex-row gap-16">
                <!-- Info Cards Area -->
                <div class="lg:w-1/3 space-y-10">
                  <div>
                    <h3 class="campaign-header text-primary text-sm mb-4">Live Helpline Data</h3>
                    <h2 class="text-4xl font-black text-secondary leading-tight">National Support Performance</h2>
                  </div>

                  <div class="grid grid-cols-1 gap-6">
                    <div
                      class="bg-white p-8 rounded-3xl shadow-sm border-l-8 border-primary flex items-center gap-6 group hover:translate-x-2 transition-transform duration-300">
                      <div class="w-14 h-14 bg-primary/10 rounded-2xl flex items-center justify-center shrink-0">
                        <PhoneIcon class="w-8 h-8 text-primary" />
                      </div>
                      <div>
                        <div class="text-3xl font-black text-secondary tabular-nums">{{ callStats.stats.calls_today
                        }}</div>
                        <div class="text-xs font-bold text-black/40 uppercase">Calls Answered Today</div>
                      </div>
                    </div>

                    <div
                      class="bg-white p-8 rounded-3xl shadow-sm border-l-8 border-hotline flex items-center gap-6 group hover:translate-x-2 transition-transform duration-300">
                      <div class="w-14 h-14 bg-hotline/10 rounded-2xl flex items-center justify-center shrink-0">
                        <ShieldCheckIcon class="w-8 h-8 text-hotline" />
                      </div>
                      <div>
                        <div class="text-3xl font-black text-secondary tabular-nums">{{ callStats.stats.cases_today
                        }}</div>
                        <div class="text-xs font-bold text-black/40 uppercase">Cases Registered Today</div>
                      </div>
                    </div>

                    <div
                      class="bg-white p-8 rounded-3xl shadow-sm border-l-8 border-secondary-light flex items-center gap-6 group hover:translate-x-2 transition-transform duration-300">
                      <div
                        class="w-14 h-14 bg-secondary-light/10 rounded-2xl flex items-center justify-center shrink-0">
                        <ChartBarIcon class="w-8 h-8 text-secondary-light" />
                      </div>
                      <div>
                        <div class="text-3xl font-black text-secondary tabular-nums">{{
                          callStats.stats.cases_ongoing }}</div>
                        <div class="text-xs font-bold text-black/40 uppercase">Active Case Load</div>
                      </div>
                    </div>

                    <!-- Total Stats (Historic) -->
                    <div class="pt-6 border-t border-neutral-offwhite">
                      <div class="grid grid-cols-2 gap-4">
                        <div class="bg-secondary/5 p-6 rounded-[2rem] border border-secondary/10">
                          <div class="text-2xl font-black text-secondary tabular-nums">{{
                            Number(callStats.stats.calls_total).toLocaleString() }}</div>
                          <div class="text-[9px] font-bold text-black/50 uppercase tracking-tighter">Lifetime
                            Calls</div>
                        </div>
                        <div class="bg-primary/5 p-6 rounded-[2rem] border border-primary/10">
                          <div class="text-2xl font-black text-primary tabular-nums">{{
                            Number(callStats.stats.cases_total).toLocaleString() }}</div>
                          <div class="text-[9px] font-bold text-primary/50 uppercase tracking-tighter">Total Cases
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Call Trend Graph -->
                <div
                  class="lg:w-2/3 bg-white rounded-[4rem] p-12 shadow-2xl border border-neutral-offwhite relative overflow-hidden group">
                  <div class="absolute top-0 right-0 p-10">
                    <div class="pill bg-primary/10 text-primary text-[10px] animate-pulse">Live Link Active</div>
                  </div>
                  <div class="mb-10">
                    <h3 class="text-2xl font-bold text-secondary flex items-center gap-3">
                      Call Frequency Trends
                    </h3>
                    <p class="text-black/50 font-bold text-sm">Hourly distribution of incoming calls by status
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
              <h2 id="downloads-heading" class="campaign-header text-3xl text-secondary mb-4">
                {{ resourcesDownloadsTitle }}
              </h2>
              <p class="text-black/60 font-bold text-lg">Public awareness materials and official guidance.</p>
            </div>
            <div class="pill bg-primary/10 text-primary">
              {{ resources.length }} {{ resourcesAvailable }}
            </div>
          </div>

          <!-- Search & Filters -->
          <div class="bg-neutral-offwhite rounded-[2.5rem] p-8 mb-16 shadow-none">
            <div class="flex flex-col md:flex-row gap-8">
              <div class="flex-1 relative group">
                <MagnifyingGlassIcon
                  class="absolute left-6 top-1/2 transform -translate-y-1/2 w-6 h-6 text-primary group-focus-within:text-secondary transition-colors" />
                <input v-model="search" type="text" :placeholder="resourcesSearchPlaceholder"
                  class="w-full pl-16 pr-6 py-4 bg-white shadow-sm border-none focus:ring-0 focus:shadow-md rounded-2xl font-bold text-secondary outline-none transition-all" />
              </div>
              <div class="relative min-w-[240px]">
                <select v-model="category"
                  class="w-full appearance-none pl-6 pr-12 py-4 bg-white shadow-sm border-none focus:ring-0 focus:shadow-md rounded-2xl font-bold text-secondary uppercase tracking-widest text-[10px] outline-none transition-all cursor-pointer">
                  <option value="">{{ resourcesAllCategories }}</option>
                  <option v-for="cat in categories" :key="cat.slug || cat.id" :value="cat.slug || cat.id">
                    {{ cat.name }}
                  </option>
                </select>
                <ChevronDownIcon
                  class="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-primary pointer-events-none" />
              </div>
            </div>
          </div>

          <!-- Resources Loading -->
          <AppLoader v-if="loading" :message="settingsStore.settings.resources_loading" />

          <!-- Resources Grid -->
          <div v-else-if="resources.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
            <article v-for="resource in resources" :key="resource.id"
              class="group bg-neutral-white rounded-[3.5rem] border-2 border-neutral-offwhite transition-all duration-500 hover:shadow-2xl hover:border-primary/30 transform hover:-translate-y-2 overflow-hidden flex flex-col">

              <div class="p-10 flex-1 flex flex-col">
                <div class="mb-8">
                  <div class="w-16 h-16 rounded-2xl bg-primary/10 flex items-center justify-center mb-8">
                    <SpeakerWaveIcon v-if="isAudio(resource)" class="w-8 h-8 text-primary" />
                    <DocumentTextIcon v-else class="w-8 h-8 text-primary" />
                  </div>
                  <h3 class="text-2xl font-bold text-secondary mb-4 leading-tight line-clamp-2">{{ resource.title
                  }}</h3>
                  <p class="text-lg text-black/50 font-bold leading-relaxed line-clamp-3">{{
                    resource.description }}</p>
                </div>

                <div class="flex flex-wrap gap-3 mb-10 mt-auto">
                  <span v-if="resource.category_name" class="pill bg-primary text-neutral-white">{{
                    resource.category_name }}</span>
                  <span v-if="resource.language" class="pill bg-secondary-light text-neutral-white">{{
                    getLanguageName(resource.language) }}</span>
                </div>

                <div v-if="isAudio(resource) && resource.file" class="mb-8 p-4 bg-neutral-offwhite rounded-2xl">
                  <audio :src="resource.file" controls class="w-full"></audio>
                </div>

                <div class="flex items-center justify-between pt-8 border-t-2 border-neutral-offwhite">
                  <BaseCTA v-if="resource.file" :href="resource.file" variant="primary" class="!py-3 !px-6 text-[10px]"
                    external download>
                    Download
                  </BaseCTA>
                  <div class="text-[10px] font-bold text-black/40 uppercase tracking-widest">
                    <span class="text-secondary">{{ resource.download_count || 0 }}</span> Downloads
                  </div>
                </div>
              </div>
            </article>
          </div>

          <!-- Empty State -->
          <div v-else
            class="text-center py-24 bg-neutral-offwhite/30 rounded-[3rem] border-2 border-dashed border-primary max-w-2xl mx-auto">
            <div
              class="w-20 h-20 bg-neutral-white rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-sm border-2 border-primary">
              <MagnifyingGlassIcon class="w-10 h-10 text-primary" />
            </div>
            <h3 class="text-2xl font-bold text-secondary mb-2">{{ settingsStore.settings.resources_no_results ||
              'No Resources Found' }}</h3>
            <p class="text-black/50 font-bold mb-8">{{ settingsStore.settings.resources_no_results_subtitle ||
              'Try adjusting your search criteria.' }}</p>
            <button @click="search = ''; category = ''" class="btn btn-outline">Clear all filters</button>
          </div>

          <!-- Pagination -->
          <div v-if="pagination.next || pagination.previous" class="mt-20 flex justify-center gap-6">
            <button :disabled="!pagination.previous || loading" @click="prevPage"
              class="btn btn-outline px-8">Previous</button>
            <button :disabled="!pagination.next || loading" @click="nextPage" class="btn btn-outline px-8">Next</button>
          </div>
        </section>

        <!-- Common Questions Bridge -->
        <section class="section-padding pt-0">
          <div
            class="bg-primary rounded-[4rem] p-12 lg:p-20 text-center text-neutral-white shadow-2xl relative overflow-hidden group">
            <div
              class="absolute inset-0 bg-gradient-to-r from-secondary/50 to-primary/50 opacity-0 group-hover:opacity-100 transition-opacity duration-700">
            </div>
            <div class="relative z-10 space-y-8">
              <h2 class="text-4xl md:text-5xl font-black">Find Immediate Answers</h2>
              <p class="text-xl opacity-80 max-w-2xl mx-auto font-bold">
                We have answers to the most common questions about safety, reporting, and our services.
              </p>
              <div class="pt-4">
                <BaseCTA to="/faqs" variant="outline"
                  class="!border-white !text-white hover:!bg-white hover:!text-primary !px-12 !py-6 !text-xl !rounded-2xl">
                  View Common Questions
                </BaseCTA>
              </div>
            </div>
          </div>
        </section>
      </div>
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

  const brand_colors = computed(() => ({
    primary: settingsStore.settings.primary_color || '#2B4C7E',
    secondary: settingsStore.settings.secondary_color || '#023047',
    'secondary-light': settingsStore.settings.secondary_light_color || '#8ECAE6',
    'hotline': settingsStore.settings.accent_orange_color || '#FB8500',
    'accent-yellow': settingsStore.settings.accent_yellow_color || '#FFB703',
    'emergency': settingsStore.settings.emergency_color || '#D00000',
    'neutral-white': '#FFFFFF',
    'neutral-offwhite': '#F8F9FA'
  }))

  const resources = ref([])
  const loading = ref(true)
  const search = ref('')
  const category = ref('')
  const language = ref('')
  const categories = ref([])
  const pagination = ref({ count: 0, next: null, previous: null })

  const resourcesStatsTitle = computed(() => settingsStore.settings?.resources_stats_title || 'Live Help Performance')
  const resourcesStatsUpdated = computed(() => settingsStore.settings?.resources_stats_updated || 'Real-time Statistics')
  const resourcesStatsError = computed(() => settingsStore.settings?.resources_stats_error || 'Resource statistics temporary unavailable')
  const resourcesCasesByCategory = computed(() => settingsStore.settings?.resources_cases_by_category || 'Cases by Category')
  const resourcesReportsOverTime = computed(() => settingsStore.settings?.resources_reports_over_time || 'Reports Over Time')
  const resourcesDownloadsTitle = computed(() => settingsStore.settings?.resources_downloads_title || 'Life-Saving Guides')
  const resourcesAvailable = computed(() => settingsStore.settings?.resources_available || 'items available')
  const resourcesSearchPlaceholder = computed(() => settingsStore.settings?.resources_search_placeholder || 'Search keywords...')
  const resourcesAllCategories = computed(() => settingsStore.settings?.resources_all_categories || 'All Categories')

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
      'answered': brand_colors.value['primary'],
      'abandoned': brand_colors.value['hotline'],
      'busy': brand_colors.value['secondary']
    }

    const datasets = Object.keys(callStats.value.calls).map(status => {
      const color = statusColors[status.toLowerCase()] || brand_colors.value['secondary-light']
      return {
        label: status.charAt(0).toUpperCase() + status.slice(1),
        borderColor: color,
        backgroundColor: color + '22',
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
          font: { family: 'Cronos Pro', weight: 'bold' },
          color: brand_colors.value['secondary']
        }
      },
      tooltip: {
        mode: 'index',
        intersect: false,
        backgroundColor: brand_colors.value['secondary'],
        titleFont: { family: 'Cronos Pro', size: 14, weight: 'bold' },
        bodyFont: { family: 'Cronos Pro', size: 12 }
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        grid: { color: brand_colors.value['neutral-offwhite'] },
        ticks: {
          font: { family: 'Cronos Pro', weight: 'bold' },
          color: brand_colors.value['secondary'] + '80'
        }
      },
      x: {
        grid: { display: false },
        ticks: {
          font: { family: 'Cronos Pro', weight: 'bold' },
          color: brand_colors.value['secondary'] + '80'
        }
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
          brand_colors.value['primary'],
          brand_colors.value['hotline'],
          brand_colors.value['secondary'],
          brand_colors.value['secondary-light']
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
        backgroundColor: brand_colors.value['primary'],
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
          color: brand_colors.value['secondary']
        }
      },
      tooltip: {
        backgroundColor: brand_colors.value['secondary'],
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
        backgroundColor: brand_colors.value['secondary'],
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
          color: brand_colors.value['primary'] + '80'
        },
        grid: {
          color: brand_colors.value['primary'] + '20',
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
          color: brand_colors.value['primary'] + '80'
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

<style scoped></style>
