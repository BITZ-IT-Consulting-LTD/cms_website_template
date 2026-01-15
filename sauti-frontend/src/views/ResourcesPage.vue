<template>
  <div class="bg-neutral-white min-h-screen">
    <!-- 1. Page Header -->
    <div class="container-custom section-padding">
      <div class="container-custom section-rhythm">


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
                <Search
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
                <ChevronDown
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
                    <Speaker v-if="isAudio(resource)" class="w-8 h-8 text-primary" />
                    <FileText v-else class="w-8 h-8 text-primary" />
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
                  <button
                    v-if="resource.file"
                    type="button"
                    class="btn btn-primary !py-3 !px-6 text-[10px]"
                    :disabled="downloadingSlug === resource.slug"
                    @click="downloadResource(resource)"
                  >
                    {{ downloadingSlug === resource.slug ? 'Downloading...' : 'Download' }}
                  </button>
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
              <Search class="w-10 h-10 text-primary" />
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
    Search,
    ChevronDown,
    FileText,
    Speaker,
    AlertTriangle,
    Code,
    Globe,
    Phone,
    ShieldCheck,
    BarChart
  } from 'lucide-vue-next'
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
  const downloadingSlug = ref(null)

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
  const resourcesDownloadsTitle = computed(() => settingsStore.settings?.resources_downloads_title || 'Resources')
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
          font: { family: 'Inter', weight: 'bold' },
          color: brand_colors.value['secondary']
        }
      },
      tooltip: {
        mode: 'index',
        intersect: false,
        backgroundColor: brand_colors.value['secondary'],
        titleFont: { family: 'Inter', size: 14, weight: 'bold' },
        bodyFont: { family: 'Inter', size: 12 }
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        grid: { color: brand_colors.value['neutral-offwhite'] },
        ticks: {
          font: { family: 'Inter', weight: 'bold' },
          color: brand_colors.value['secondary'] + '80'
        }
      },
      x: {
        grid: { display: false },
        ticks: {
          font: { family: 'Inter', weight: 'bold' },
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
            family: 'Inter'
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
            family: 'Inter'
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
            family: 'Inter'
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

  async function downloadResource(resource) {
    if (!resource?.slug || !resource?.file) return
    downloadingSlug.value = resource.slug
    try {
      // Increment download_count on backend (ResourceDetailView.retrieve)
      await api.resources.get(resource.slug)
      // Open the actual file URL
      window.open(resource.file, '_blank', 'noopener,noreferrer')
      // Refresh list so counts update in UI
      await fetchList()
    } catch (error) {
      console.error('Failed to download resource:', error)
      // Fall back to opening file anyway
      window.open(resource.file, '_blank', 'noopener,noreferrer')
    } finally {
      downloadingSlug.value = null
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
