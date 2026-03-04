<template>
  <div class="min-h-screen bg-white">
    <!-- Hero Banner -->
    <header class="hero-banner" style="padding-top: clamp(70px, 15vw, 90px);">
      <div class="hero-overlay"></div>
      <div class="container-custom hero-content-wrapper">
        <div class="hero-text">
          <h1 class="hero-title">
            {{ siteContent.getContent('resources_page_title', 'Resources') }} <span class="text-accent-yellow">{{ siteContent.getContent('resources_page_title_highlight', 'and Statistics') }}</span>
          </h1>
          <p class="hero-subtitle">
            {{ siteContent.getContent('resources_page_subtitle', 'Access our library of official reports, awareness materials, and real-time helpline statistics.') }}
          </p>
        </div>
      </div>
    </header>

    <div class="container-custom section-padding !pt-12">
      <div class="container-custom section-rhythm">

        <!-- ============================================ -->
        <!-- STATISTICS DASHBOARD SECTION                 -->
        <!-- ============================================ -->
        <section aria-label="Statistics Dashboard" class="mb-20">
          <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
            <div>
              <h2 class="text-2xl lg:text-3xl font-bold text-secondary mb-3 lg:mb-4">
                {{ siteContent.getContent('statistics_dashboard_title', 'Live Statistics') }}
              </h2>
              <p class="text-sm lg:text-base text-black/60 font-semibold">
                {{ siteContent.getContent('statistics_dashboard_subtitle', 'Real-time data from the Sauti 116 Helpline') }}
              </p>
            </div>
            <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-secondary/10 text-secondary text-xs font-black tracking-widest border border-secondary/20">
              <BarChart class="w-4 h-4" />
              Live Data
            </div>
          </div>

          <!-- Enhanced Quick Stats Cards -->
          <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 mb-16">
            <!-- Total Calls -->
            <div class="relative overflow-hidden rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 group bg-gradient-to-br from-primary to-primary/80">
              <div class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
              <div class="relative z-10">
                <div class="text-3xl md:text-4xl font-black text-white mb-1">
                   {{ formatNumber(dashboardStats.total_calls) }}
                </div>
                <p class="text-white/80 text-xs font-bold tracking-wider uppercase">
                  {{ siteContent.getContent('stats_kpi_calls', 'Total Calls') }}
                </p>
              </div>
            </div>

            <!-- Total Cases -->
            <div class="relative overflow-hidden rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 group bg-gradient-to-br from-secondary to-secondary/80">
              <div class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
              <div class="relative z-10">
                <div class="text-3xl md:text-4xl font-black text-white mb-1">
                   {{ formatNumber(dashboardStats.total_cases) }}
                </div>
                <p class="text-white/80 text-xs font-bold tracking-wider uppercase">
                  {{ siteContent.getContent('stats_kpi_cases', 'Total Cases') }}
                </p>
              </div>
            </div>

            <!-- Total GBV Cases -->
            <div class="relative overflow-hidden rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 group bg-gradient-to-br from-hotline to-hotline/80">
              <div class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
              <div class="relative z-10">
                <div class="text-3xl md:text-4xl font-black text-white mb-1">
                   {{ formatNumber(dashboardStats.total_gbv_cases) }}
                </div>
                <p class="text-white/80 text-xs font-bold tracking-wider uppercase">
                  {{ siteContent.getContent('stats_kpi_gbv', 'Total GBV Cases') }}
                </p>
              </div>
            </div>

            <!-- Total SEA Cases -->
            <div class="relative overflow-hidden rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 group bg-gradient-to-br from-emergency to-emergency/80">
              <div class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
              <div class="relative z-10">
                <div class="text-3xl md:text-4xl font-black text-white mb-1">
                   {{ formatNumber(dashboardStats.total_sea_cases) }}
                </div>
                <p class="text-white/80 text-xs font-bold tracking-wider uppercase">
                  {{ siteContent.getContent('stats_kpi_sea', 'Total SEA Cases') }}
                </p>
              </div>
            </div>

            <!-- Total Migrant Workers -->
            <div class="relative overflow-hidden rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 group bg-gradient-to-br from-secondary-light to-secondary-light/80">
              <div class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
              <div class="relative z-10">
                <div class="text-3xl md:text-4xl font-black text-white mb-1">
                   {{ formatNumber(dashboardStats.total_migrant_workers) }}
                </div>
                <p class="text-white/80 text-xs font-bold tracking-wider uppercase">
                  {{ siteContent.getContent('stats_kpi_migrant', 'Migrant Workers') }}
                </p>
              </div>
            </div>
          </div>

          <!-- Filter Bar -->
          <div class="flex items-center gap-4 mb-8">
            <label for="caseTypeFilter" class="text-sm font-semibold text-secondary/70 uppercase tracking-wider">
              Filter by Case Type
            </label>
            <select
              id="caseTypeFilter"
              v-model="caseTypeFilter"
              class="rounded-xl border border-gray-200 bg-white px-4 py-2 text-sm font-medium text-secondary shadow-sm focus:border-primary focus:ring-1 focus:ring-primary outline-none"
            >
              <option value="All">All Case Types</option>
              <option value="Abuse">Abuse</option>
              <option value="Counseling">Counseling</option>
              <option value="Information Inquiry">Information Inquiry</option>
            </select>
          </div>

          <!-- Enhanced Charts Grid (2x2) -->
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <!-- Chart 1: Category vs Client Sex -->
            <div class="relative bg-white rounded-3xl p-8 shadow-xl border border-gray-100 hover:shadow-2xl transition-all duration-300 group overflow-hidden">
              <!-- Decorative Background Pattern -->
              <div class="absolute top-0 right-0 w-64 h-64 bg-primary/5 rounded-full -translate-y-1/2 translate-x-1/2 group-hover:scale-110 transition-transform duration-700"></div>

              <div class="relative z-10">
                <div class="flex items-center gap-3 mb-6">
                  <div class="w-3 h-3 bg-primary rounded-full"></div>
                  <h3 class="text-xl font-black text-secondary">
                    Case Distribution by Gender
                  </h3>
                </div>
                <div class="h-[400px]">
                   <Bar :data="filteredCategoryBySex" :options="getDashboardOptions(false)" />
                 </div>
              </div>
            </div>

            <!-- Chart 2: Category vs Client Region -->
            <div class="relative bg-white rounded-3xl p-8 shadow-xl border border-gray-100 hover:shadow-2xl transition-all duration-300 group overflow-hidden">
              <div class="absolute top-0 right-0 w-64 h-64 bg-secondary/5 rounded-full -translate-y-1/2 translate-x-1/2 group-hover:scale-110 transition-transform duration-700"></div>

              <div class="relative z-10">
                <div class="flex items-center gap-3 mb-6">
                  <div class="w-3 h-3 bg-secondary rounded-full"></div>
                  <h3 class="text-xl font-black text-secondary">
                     Case Distribution by Region
                  </h3>
                </div>
                 <div class="h-[400px]">
                   <Bar :data="filteredCategoryByRegion" :options="getDashboardOptions(false)" />
                 </div>
              </div>
            </div>

            <!-- Chart 3: Category vs Client Age Group -->
            <div class="relative bg-white rounded-3xl p-8 shadow-xl border border-gray-100 hover:shadow-2xl transition-all duration-300 group overflow-hidden">
              <div class="absolute top-0 right-0 w-64 h-64 bg-hotline/5 rounded-full -translate-y-1/2 translate-x-1/2 group-hover:scale-110 transition-transform duration-700"></div>

              <div class="relative z-10">
                <div class="flex items-center gap-3 mb-6">
                  <div class="w-3 h-3 bg-hotline rounded-full"></div>
                  <h3 class="text-xl font-black text-secondary">
                     Case Distribution by Age Group
                  </h3>
                </div>
                 <div class="h-[400px]">
                   <Bar :data="filteredCategoryByAgeGroup" :options="getDashboardOptions(false)" />
                 </div>
              </div>
            </div>

            <!-- Chart 4: Category vs Client District -->
            <div class="relative bg-white rounded-3xl p-8 shadow-xl border border-gray-100 hover:shadow-2xl transition-all duration-300 group overflow-hidden">
              <div class="absolute top-0 right-0 w-64 h-64 bg-emergency/5 rounded-full -translate-y-1/2 translate-x-1/2 group-hover:scale-110 transition-transform duration-700"></div>

              <div class="relative z-10">
                <div class="flex items-center gap-3 mb-6">
                  <div class="w-3 h-3 bg-emergency rounded-full"></div>
                  <h3 class="text-xl font-black text-secondary">
                     Case Distribution by District
                  </h3>
                </div>
                 <div class="h-[400px]">
                   <Bar :data="filteredCategoryByDistrict" :options="getDashboardOptions(false)" />
                 </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ============================================ -->
        <!-- SECTION DIVIDER                              -->
        <!-- ============================================ -->
        <div class="my-20 flex items-center gap-6">
          <div class="flex-1 h-px bg-gray-200"></div>
          <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-neutral-offwhite border border-gray-200">
            <FileText class="w-4 h-4 text-primary" />
            <span class="text-xs font-black tracking-widest text-secondary/60 uppercase">Downloads</span>
          </div>
          <div class="flex-1 h-px bg-gray-200"></div>
        </div>

        <!-- ============================================ -->
        <!-- DOWNLOADABLE RESOURCES SECTION               -->
        <!-- ============================================ -->
        <section aria-labelledby="downloads-heading">
          <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
            <div>
              <h2 id="downloads-heading" class="campaign-header text-3xl text-secondary mb-4">
                {{ siteContent.getContent('resources_section_title', resourcesDownloadsTitle) }}
              </h2>
              <p class="text-black/60 font-bold text-lg">
                {{ siteContent.getContent('resources_section_subtitle', 'Public awareness materials and official guidance.') }}
              </p>
            </div>
            <div class="pill bg-primary/10 text-primary">
              {{ filteredResources.length }} {{ resourcesAvailable }}
            </div>
          </div>

          <!-- Search & Filters -->
          <div class="bg-neutral-offwhite rounded-[2.5rem] p-8 mb-16 shadow-none">
            <div class="flex flex-col gap-4">
              <!-- Search Bar -->
              <div class="flex-1 relative group">
                <Search
                  class="absolute left-6 top-1/2 transform -translate-y-1/2 w-6 h-6 text-primary group-focus-within:text-secondary transition-colors" />
                <input v-model="search" type="text" :placeholder="siteContent.getContent('resources_search_placeholder', resourcesSearchPlaceholder)"
                  class="w-full pl-16 pr-6 py-4 bg-white shadow-sm border-none focus:ring-0 focus:shadow-md rounded-2xl font-bold text-secondary outline-none transition-all" />
              </div>

              <!-- Filter Dropdowns -->
              <div class="flex flex-col md:flex-row gap-4">
                <!-- Category Filter -->
                <div class="relative flex-1">
                  <select v-model="category"
                    class="w-full appearance-none pl-6 pr-12 py-4 bg-white shadow-sm border-none focus:ring-0 focus:shadow-md rounded-2xl font-bold text-secondary tracking-widest text-[10px] outline-none transition-all cursor-pointer">
                    <option value="">{{ siteContent.getContent('resources_filter_all_categories', resourcesAllCategories) }}</option>
                    <option v-for="cat in categories" :key="cat.slug || cat.id" :value="cat.slug || cat.id">
                      {{ cat.name }}
                    </option>
                  </select>
                  <ChevronDown
                    class="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-primary pointer-events-none" />
                </div>

                <!-- Format Filter -->
                <div class="relative flex-1">
                  <select v-model="format"
                    class="w-full appearance-none pl-6 pr-12 py-4 bg-white shadow-sm border-none focus:ring-0 focus:shadow-md rounded-2xl font-bold text-secondary tracking-widest text-[10px] outline-none transition-all cursor-pointer">
                    <option value="">{{ siteContent.getContent('resources_filter_all_formats', 'All Formats') }}</option>
                    <option value="audio">Audio</option>
                    <option value="document">Document</option>
                  </select>
                  <ChevronDown
                    class="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-primary pointer-events-none" />
                </div>

                <!-- Language Filter -->
                <div class="relative flex-1">
                  <select v-model="language"
                    class="w-full appearance-none pl-6 pr-12 py-4 bg-white shadow-sm border-none focus:ring-0 focus:shadow-md rounded-2xl font-bold text-secondary tracking-widest text-[10px] outline-none transition-all cursor-pointer">
                    <option value="">{{ siteContent.getContent('resources_filter_all_languages', 'All Languages') }}</option>
                    <option value="en">English</option>
                    <option value="lg">Luganda</option>
                    <option value="sw">Swahili</option>
                  </select>
                  <ChevronDown
                    class="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-primary pointer-events-none" />
                </div>
              </div>
            </div>
          </div>

          <!-- Resources Loading -->
          <AppLoader v-if="loading" :message="settingsStore.settings.resources_loading" />

          <!-- Enhanced Resources Grid (No Images - CMS Driven) -->
          <div v-else-if="filteredResources.length" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            <article v-for="resource in filteredResources" :key="resource.id"
              class="group bg-white rounded-3xl shadow-lg border border-gray-100 transition-all duration-500 hover:shadow-2xl hover:border-primary/30 transform hover:-translate-y-2 overflow-hidden flex flex-col">

              <!-- Content -->
              <div class="p-8 flex-1 flex flex-col">
                <!-- Type Badge Only -->
                <div class="flex items-start justify-end mb-6">
                  <div class="px-3 py-1 rounded-full flex items-center gap-2"
                       :class="isAudio(resource) ? 'bg-hotline/10 text-hotline' : 'bg-primary/10 text-primary'">
                    <span class="text-xs font-bold uppercase tracking-wider">
                      {{ isAudio(resource) ? 'Audio' : 'Document' }}
                    </span>
                  </div>
                </div>

                <h3 class="text-2xl font-bold text-secondary mb-4 leading-tight line-clamp-2 group-hover:text-primary transition-colors">
                  {{ resource.title }}
                </h3>

                <!-- Expandable Description -->
                <div class="text-base text-black/60 leading-relaxed mb-6 flex-1">
                  <p :class="expandedDescriptions[resource.id] ? '' : 'line-clamp-3'">
                    {{ resource.description }}
                  </p>
                  <button
                    v-if="resource.description && resource.description.length > 150"
                    @click="toggleDescription(resource.id)"
                    class="text-primary hover:text-secondary text-sm font-bold mt-2 transition-colors"
                  >
                    {{ expandedDescriptions[resource.id] ? '− Show less' : '+ Read more' }}
                  </button>
                </div>

                <!-- Audio Player (if audio) -->
                <div v-if="isAudio(resource) && resource.file" class="mb-6 p-4 bg-neutral-offwhite rounded-2xl">
                  <audio :src="resource.file" controls class="w-full"></audio>
                </div>

                <!-- Download Button & Stats -->
                <div class="flex items-center justify-between pt-6 border-t border-gray-100 mt-auto">
                  <button
                    v-if="resource.file"
                    type="button"
                    class="btn btn-primary !py-3 !px-6 !text-sm"
                    :disabled="downloadingSlug === resource.slug"
                    @click="downloadResource(resource)"
                  >
                    {{ downloadingSlug === resource.slug ? 'Downloading...' : 'Download' }}
                  </button>
                  <span v-if="resource.download_count" class="text-sm text-black/40 font-semibold">
                    {{ resource.download_count }} downloads
                  </span>
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
            <button @click="search = ''; category = ''; language = ''; format = ''" class="btn btn-outline">Clear all filters</button>
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
  import { useSiteContent } from '@/composables/useSiteContent'
  import { api } from '@/utils/axios'
  import AppLoader from '@/components/common/AppLoader.vue'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import {
    Search,
    ChevronDown,
    FileText,
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
  const siteContent = useSiteContent('resources')
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
  const format = ref('')
  const categories = ref([])
  const pagination = ref({ count: 0, next: null, previous: null })
  const expandedDescriptions = ref({})

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
        fetchCallStats(),
        siteContent.fetchContent()
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
          font: { family: 'cronos-pro', weight: 'bold' },
          color: brand_colors.value['secondary']
        }
      },
      tooltip: {
        mode: 'index',
        intersect: false,
        backgroundColor: brand_colors.value['secondary'],
        titleFont: { family: 'cronos-pro', size: 14, weight: 'bold' },
        bodyFont: { family: 'cronos-pro', size: 12 }
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        grid: { color: brand_colors.value['neutral-offwhite'] },
        ticks: {
          font: { family: 'cronos-pro', weight: 'bold' },
          color: brand_colors.value['secondary'] + '80'
        }
      },
      x: {
        grid: { display: false },
        ticks: {
          font: { family: 'cronos-pro', weight: 'bold' },
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
            family: 'cronos-pro'
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
            family: 'cronos-pro'
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
            family: 'cronos-pro'
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

  // Filtered resources based on format (client-side filtering)
  const filteredResources = computed(() => {
    if (!format.value) return resources.value

    return resources.value.filter(resource => {
      if (format.value === 'audio') {
        return isAudio(resource)
      } else if (format.value === 'document') {
        return !isAudio(resource)
      }
      return true
    })
  })

  // Toggle description expansion
  function toggleDescription(resourceId) {
    expandedDescriptions.value[resourceId] = !expandedDescriptions.value[resourceId]
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
  // --- Dashboard Statistics Logic ---
  const dashboardStats = ref({
    total_calls: 0,
    total_cases: 0,
    total_gbv_cases: 0,
    total_sea_cases: 0,
    total_migrant_workers: 0
  })

  const dashboardCharts = ref({
    categoryBySex: { labels: [], datasets: [] },
    categoryByRegion: { labels: [], datasets: [] },
    categoryByAgeGroup: { labels: [], datasets: [] },
    categoryByDistrict: { labels: [], datasets: [] }
  })

  const caseTypeFilter = ref('All')

  // --- Category-to-CaseType Mapping ---
  const ABUSE_CATEGORIES = [
    'Child Neglect', 'Sexual Violence', 'Physical Violence', 'Child Exploitation',
    'Economic Violence', 'Emotional & Psychological Abuse', 'Harmful Tranditional Practices',
    'Murder', 'Online Sexual Abuse & Violence', 'Others', 'Threatening Violence',
    'Trafficking in Persons'
  ]

  const COUNSELING_CATEGORIES = [
    'Addiction', 'Boy/Girl Relationship', 'Career Guidance', 'Child Custody',
    'Child In Conflict with the Law', 'Child to Child Sex', 'Denial of conjugal rights',
    'Differently Abled Persons', 'Discrimination', 'Family Issues', 'HIV Counselling',
    'Juvenile Deliquence', 'Legal Issues', 'Life Skills', 'Loss and Grief', 'Lost Child',
    'Medical_Care', 'Mental Issues', 'Orphans', 'Parent or Child Relationship',
    'Parental Guidance', 'Peer Influence', 'Property_Rights', 'Reproductive Health Issues',
    'Run Away Child', 'Self Esteem', 'Street Child', 'Stress/Depression',
    'Student or Teacher Relationship', 'Bestiality'
  ]

  const INFO_CATEGORIES = [
    'Appreciation', 'Birth Registration', 'Case Update', 'Employment/Job',
    'Financial Aid', 'In Need of School Fees', 'Information on Helpline Services',
    'Inquiry on Other Services', 'Medical Aid', 'Outbreaks', 'Pre-trial Briefing',
    'Topical Issues (Child rights, Biology etc)'
  ]

  // --- Filter Logic ---
  const getAllowedCategories = () => {
    switch (caseTypeFilter.value) {
      case 'Abuse': return ABUSE_CATEGORIES
      case 'Counseling': return COUNSELING_CATEGORIES
      case 'Information Inquiry': return INFO_CATEGORIES
      default: return null
    }
  }

  const filterChartData = (chartData) => {
    const allowed = getAllowedCategories()
    if (!allowed) return chartData
    if (!chartData || !chartData.labels || !chartData.labels.length) return chartData

    const indices = []
    chartData.labels.forEach((label, i) => {
      if (allowed.includes(label)) indices.push(i)
    })

    return {
      labels: indices.map(i => chartData.labels[i]),
      datasets: chartData.datasets.map(ds => ({
        ...ds,
        data: indices.map(i => ds.data[i])
      }))
    }
  }

  const filteredCategoryBySex = computed(() => filterChartData(dashboardCharts.value.categoryBySex))
  const filteredCategoryByRegion = computed(() => filterChartData(dashboardCharts.value.categoryByRegion))
  const filteredCategoryByAgeGroup = computed(() => filterChartData(dashboardCharts.value.categoryByAgeGroup))
  const filteredCategoryByDistrict = computed(() => filterChartData(dashboardCharts.value.categoryByDistrict))

  // Helper Functions
  const formatNumber = (num) => {
    return num !== null && num !== undefined ? num.toLocaleString() : '0'
  }

  const getBrandColor = (index) => {
    // Enhanced color palette with high contrast for white backgrounds
    // Using vibrant, saturated colors that maintain accessibility
    const palette = [
      '#007BBF', // Sauti Blue (Primary)
      '#006837', // Dark Green
      '#FB8500', // Orange
      '#2B4C7E', // Navy Blue
      '#ED1C24', // Red
      '#10B981', // Emerald
      '#8B5CF6', // Purple
      '#F59E0B', // Amber
      '#EC4899', // Pink
      '#14B8A6', // Teal
      '#6366F1', // Indigo
      '#EF4444'  // Bright Red
    ]
    return palette[index % palette.length]
  }

  // API Fetch Logic for Dashboard - Now connected to real Sauti helpline data
  const fetchDashboardData = async () => {
    try {
      // Fetch real statistics from the external Sauti helpline system
      const statsResponse = await api.get('/dashboard/helpline-stats/')

      if (statsResponse.data) {
        dashboardStats.value = {
          total_calls: statsResponse.data.total_calls || 0,
          total_cases: statsResponse.data.total_cases || 0,
          total_gbv_cases: statsResponse.data.total_gbv_cases || 0,
          total_sea_cases: statsResponse.data.total_sea_cases || 0,
          total_migrant_workers: statsResponse.data.total_migrant_workers || 0
        }
      }

      const mapChartData = (apiData) => {
          if (!apiData) return { labels: [], datasets: [] }
          return {
              labels: apiData.labels || [],
              datasets: (apiData.datasets || []).map((ds, index) => ({
                  label: ds.label,
                  data: ds.data,
                  backgroundColor: getBrandColor(index),
                  borderRadius: 4
              }))
          }
      }

      // Fetch chart data from the helpline system
      const chartsResponse = await api.get('/dashboard/helpline-charts/')
      if (chartsResponse.data) {
        dashboardCharts.value = {
          categoryBySex: mapChartData(chartsResponse.data.categoryBySex),
          categoryByRegion: mapChartData(chartsResponse.data.categoryByRegion),
          categoryByAgeGroup: mapChartData(chartsResponse.data.categoryByAgeGroup),
          categoryByDistrict: mapChartData(chartsResponse.data.categoryByDistrict)
        }
      }
    } catch (err) {
      console.warn('Statistics dashboard data unavailable:', err)
    }
  }

  // Load dashboard data on mount
  onMounted(() => {
    fetchDashboardData()
  })

  // Dashboard Chart Options Helper
  const getDashboardOptions = (horizontal) => {
    return {
      indexAxis: horizontal ? 'y' : 'x',
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: true,
          position: 'bottom',
          labels: {
            usePointStyle: true,
            boxWidth: 8,
            font: { family: 'cronos-pro', weight: 'bold', size: 10 },
            color: '#023047'
          }
        },
        tooltip: {
          backgroundColor: '#023047',
          titleFont: { family: 'cronos-pro', size: 14 },
          bodyFont: { family: 'cronos-pro', size: 12 }
        }
      },
      scales: {
        x: {
          stacked: true,
          grid: { display: false },
          ticks: { font: { family: 'cronos-pro', weight: 'bold' } }
        },
        y: {
          stacked: true,
          beginAtZero: true,
          grid: { color: '#F8F9FA' },
          ticks: { font: { family: 'cronos-pro', weight: 'bold' } }
        }
      }
    }
  }

</script>

<style scoped>
/* Hero Banner */
.hero-banner {
  position: relative;
  background: linear-gradient(135deg, rgb(var(--color-secondary)) 0%, rgb(var(--color-primary-dark)) 100%);
  min-height: clamp(200px, 25vh, 300px);
  display: flex;
  align-items: center;
  overflow: hidden;
  margin-top: 0;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800"><defs><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1"/></pattern></defs><rect width="1200" height="800" fill="url(%23grid)"/></svg>');
  opacity: 0.5;
}

.hero-content-wrapper {
  position: relative;
  z-index: 2;
  padding: clamp(1.25rem, 3vh, 2.5rem) 0;
}

.hero-text {
  text-align: center;
  margin-bottom: clamp(0.75rem, 2vw, 1rem);
}

.hero-title {
  font-size: clamp(1rem, 2vw, 1.75rem);
  font-weight: 900;
  color: white;
  margin-bottom: 0.375rem;
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.text-accent-yellow {
  color: rgb(var(--color-accent-yellow));
}

.hero-subtitle {
  font-size: clamp(0.75rem, 0.9vw, 0.875rem);
  color: rgba(255, 255, 255, 0.85);
  font-weight: 400;
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.4;
  padding: 0 1rem;
}
</style>
