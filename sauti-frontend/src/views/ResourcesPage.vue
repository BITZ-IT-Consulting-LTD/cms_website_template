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
    </div>
  </div>
</template>

<script setup>
  import { ref, watch, onMounted, computed } from 'vue'
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
    ExclamationTriangleIcon
  } from '@heroicons/vue/24/outline'
  import { Chart as ChartJS, ArcElement, Tooltip, Legend, BarElement, CategoryScale, LinearScale, Title } from 'chart.js'
  import { Doughnut, Bar } from 'vue-chartjs'

  ChartJS.register(ArcElement, Tooltip, Legend, BarElement, CategoryScale, LinearScale, Title)

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

  // Fetch statistics
  onMounted(async () => {
    await settingsStore.fetchGlobalSettings()
    try {
      const [cats] = await Promise.all([
        resourcesStore.fetchCategories(),
        fetchList(),
        fetchStats()
      ])
      categories.value = Array.isArray(cats) ? cats : []
    } catch (error) {
      console.error('Error initializing resources:', error)
      categories.value = []
    } finally {
      loading.value = false
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
