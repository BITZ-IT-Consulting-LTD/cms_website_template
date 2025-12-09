<template>
  <div class="min-h-screen bg-gradient-to-b from-gray-50 to-white">
    <div class="section-padding">
      <div class="container-custom">
        <!-- Header -->
        <div class="text-center mb-12">
          <h1 class="text-4xl md:text-5xl font-extrabold text-gray-900 mb-4">
            Resources & Statistics
          </h1>
          <p class="text-lg text-gray-600 max-w-3xl mx-auto">
            Real-time insights from case reports and downloadable resources to support communities
          </p>
        </div>

        <!-- Statistics Dashboard -->
        <div class="mb-16">
          <div class="flex items-center justify-between mb-6">
            <h2 class="text-2xl font-bold text-gray-900">Case Report Statistics</h2>
            <div class="text-sm text-gray-500">Updated in real-time</div>
          </div>

          <!-- Loading State for Stats -->
          <div v-if="statsLoading" class="bg-white rounded-3xl shadow-xl p-12 text-center">
            <div class="animate-spin rounded-full h-16 w-16 border-b-4 border-blue-600 mx-auto mb-4"></div>
            <p class="text-gray-600">Loading statistics...</p>
          </div>

          <!-- Error State for Stats -->
          <div v-else-if="statsError" class="bg-red-50 rounded-3xl border-2 border-red-200 p-8 text-center">
            <svg class="w-16 h-16 text-red-500 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            <p class="text-red-700 font-medium">{{ statsError }}</p>
          </div>

          <!-- Stats Content -->
          <div v-else>
            <!-- Key Metrics Cards -->
            <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
              <!-- Total Reports -->
              <div class="group relative bg-gradient-to-br from-blue-500 to-blue-600 rounded-2xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden">
                <div class="absolute top-0 right-0 w-24 h-24 bg-white/10 rounded-full -mr-12 -mt-12"></div>
                <div class="relative">
                  <div class="flex items-center justify-between mb-2">
                    <svg class="w-10 h-10 opacity-80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                    </svg>
                  </div>
                  <h3 class="text-4xl font-extrabold mb-1">{{ stats.total_reports || 0 }}</h3>
                  <p class="text-blue-100 text-sm font-medium">Total Reports</p>
                </div>
              </div>

              <!-- Child Protection -->
              <div class="group relative bg-gradient-to-br from-purple-500 to-purple-600 rounded-2xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden">
                <div class="absolute top-0 right-0 w-24 h-24 bg-white/10 rounded-full -mr-12 -mt-12"></div>
                <div class="relative">
                  <div class="flex items-center justify-between mb-2">
                    <svg class="w-10 h-10 opacity-80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/>
                    </svg>
                  </div>
                  <h3 class="text-4xl font-extrabold mb-1">{{ getCategoryCount('CHILD_PROTECTION') }}</h3>
                  <p class="text-purple-100 text-sm font-medium">Child Protection</p>
                </div>
              </div>

              <!-- GBV Cases -->
              <div class="group relative bg-gradient-to-br from-teal-500 to-teal-600 rounded-2xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden">
                <div class="absolute top-0 right-0 w-24 h-24 bg-white/10 rounded-full -mr-12 -mt-12"></div>
                <div class="relative">
                  <div class="flex items-center justify-between mb-2">
                    <svg class="w-10 h-10 opacity-80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
                    </svg>
                  </div>
                  <h3 class="text-4xl font-extrabold mb-1">{{ getCategoryCount('GBV') }}</h3>
                  <p class="text-teal-100 text-sm font-medium">GBV Cases</p>
                </div>
              </div>

              <!-- Migrant Worker -->
              <div class="group relative bg-gradient-to-br from-orange-500 to-orange-600 rounded-2xl p-6 text-white shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden">
                <div class="absolute top-0 right-0 w-24 h-24 bg-white/10 rounded-full -mr-12 -mt-12"></div>
                <div class="relative">
                  <div class="flex items-center justify-between mb-2">
                    <svg class="w-10 h-10 opacity-80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                  </div>
                  <h3 class="text-4xl font-extrabold mb-1">{{ getCategoryCount('MIGRANT') }}</h3>
                  <p class="text-orange-100 text-sm font-medium">Migrant Worker</p>
                </div>
              </div>
            </div>

            <!-- Charts Section -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
              <!-- Doughnut Chart - Cases by Category -->
              <div class="bg-white rounded-3xl shadow-xl p-8 border border-gray-100">
                <div class="flex items-center justify-between mb-6">
                  <h3 class="text-xl font-bold text-gray-900">Cases by Category</h3>
                  <div class="px-3 py-1 bg-blue-50 text-blue-700 text-xs font-semibold rounded-full">
                    Interactive
                  </div>
                </div>
                <div class="h-80 flex items-center justify-center">
                  <Doughnut :data="categoryChartData" :options="doughnutOptions" />
                </div>
              </div>

              <!-- Bar Chart - Reports Over Time -->
              <div class="bg-white rounded-3xl shadow-xl p-8 border border-gray-100">
                <div class="flex items-center justify-between mb-6">
                  <h3 class="text-xl font-bold text-gray-900">Reports Over Time</h3>
                  <div class="px-3 py-1 bg-teal-50 text-teal-700 text-xs font-semibold rounded-full">
                    Last 6 Months
                  </div>
                </div>
                <div class="h-80">
                  <Bar :data="timeChartData" :options="barOptions" />
                </div>
              </div>
            </div>

            <!-- Status Distribution -->
            <div class="bg-white rounded-3xl shadow-xl p-8 border border-gray-100">
              <h3 class="text-xl font-bold text-gray-900 mb-6">Report Status Distribution</h3>
              <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
                <div class="text-center p-6 bg-gradient-to-br from-yellow-50 to-yellow-100 rounded-2xl border-2 border-yellow-200">
                  <div class="text-4xl font-extrabold text-yellow-700 mb-2">{{ getStatusCount('PENDING') }}</div>
                  <div class="text-sm font-semibold text-yellow-800">Pending</div>
                </div>
                <div class="text-center p-6 bg-gradient-to-br from-blue-50 to-blue-100 rounded-2xl border-2 border-blue-200">
                  <div class="text-4xl font-extrabold text-blue-700 mb-2">{{ getStatusCount('IN_PROGRESS') }}</div>
                  <div class="text-sm font-semibold text-blue-800">In Progress</div>
                </div>
                <div class="text-center p-6 bg-gradient-to-br from-green-50 to-green-100 rounded-2xl border-2 border-green-200">
                  <div class="text-4xl font-extrabold text-green-700 mb-2">{{ getStatusCount('RESOLVED') }}</div>
                  <div class="text-sm font-semibold text-green-800">Resolved</div>
                </div>
                <div class="text-center p-6 bg-gradient-to-br from-gray-50 to-gray-100 rounded-2xl border-2 border-gray-200">
                  <div class="text-4xl font-extrabold text-gray-700 mb-2">{{ getStatusCount('CLOSED') }}</div>
                  <div class="text-sm font-semibold text-gray-800">Closed</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Downloadable Resources Section -->
        <div>
          <div class="flex items-center justify-between mb-8">
            <div>
              <h2 class="text-2xl font-bold text-gray-900 mb-2">Downloadable Resources</h2>
              <p class="text-gray-600">Guides, policies, and toolkits available in multiple languages</p>
            </div>
            <div class="text-sm text-gray-500">
              <span class="font-semibold text-gray-900">{{ resources.length }}</span> resources available
            </div>
          </div>

          <!-- Filters -->
          <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6 mb-8">
            <div class="flex flex-col md:flex-row gap-4">
              <div class="flex-1 relative">
                <svg class="absolute left-4 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
                </svg>
                <input
                  v-model="search"
                  type="text"
                  placeholder="Search resources by title or description..."
                  class="w-full pl-12 pr-4 py-3 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>
              <select
                v-model="category"
                class="px-4 py-3 border border-gray-200 rounded-xl min-w-[200px] focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="">All Categories</option>
                <option v-for="cat in categories" :key="cat.slug || cat.id" :value="cat.slug || cat.id">
                  {{ cat.name }}
                </option>
              </select>
              <select
                v-model="language"
                class="px-4 py-3 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="">All Languages</option>
                <option value="en">English</option>
                <option value="lg">Luganda</option>
                <option value="sw">Swahili</option>
              </select>
            </div>
          </div>

          <!-- Resources Loading -->
          <Loader v-if="loading" message="Loading resources..." />

          <!-- Resources Grid -->
          <div v-else-if="resources.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <article
              v-for="resource in resources"
              :key="resource.id"
              class="group relative bg-white rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-500 overflow-hidden border-2 border-transparent hover:border-blue-300 transform hover:-translate-y-2"
            >
              <!-- Featured Badge -->
              <div v-if="resource.is_featured" class="absolute top-0 right-0 z-10">
                <div class="bg-gradient-to-br from-orange-500 to-orange-600 text-white text-xs font-bold px-4 py-2 rounded-bl-3xl shadow-lg flex items-center gap-1">
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                  </svg>
                  Featured
                </div>
              </div>

              <!-- Decorative Background -->
              <div class="absolute inset-0 bg-gradient-to-br from-blue-50/50 via-transparent to-purple-50/50 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>

              <div class="relative p-8">
                <!-- Icon and Title -->
                <div class="flex items-start gap-4 mb-6">
                  <div class="flex-shrink-0 w-16 h-16 rounded-2xl bg-gradient-to-br from-blue-500 to-blue-600 flex items-center justify-center shadow-xl group-hover:scale-110 group-hover:rotate-3 transition-transform duration-300">
                    <svg v-if="isAudio(resource)" class="w-8 h-8 text-white" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M9 19V6l12-2v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-2"/>
                    </svg>
                    <svg v-else class="w-8 h-8 text-white" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z" clip-rule="evenodd" />
                    </svg>
                  </div>
                  <div class="flex-1 min-w-0">
                    <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-blue-600 transition-colors line-clamp-2">
                      {{ resource.title }}
                    </h3>
                    <p class="text-sm text-gray-600 line-clamp-2">
                      {{ resource.description }}
                    </p>
                  </div>
                </div>

                <!-- Tags -->
                <div class="flex flex-wrap gap-2 mb-6">
                  <span v-if="resource.category_name" class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-blue-100 text-blue-700">
                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd"/>
                    </svg>
                    {{ resource.category_name }}
                  </span>
                  <span v-if="resource.language" class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-purple-100 text-purple-700">
                    <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M7 2a1 1 0 011 1v1h3a1 1 0 110 2H9.578a18.87 18.87 0 01-1.724 4.78c.29.354.596.696.914 1.026a1 1 0 11-1.44 1.389c-.188-.196-.373-.396-.554-.6a19.098 19.098 0 01-3.107 3.567 1 1 0 01-1.334-1.49 17.087 17.087 0 003.13-3.733 18.992 18.992 0 01-1.487-2.494 1 1 0 111.79-.89c.234.47.489.928.764 1.372.417-.934.752-1.913.997-2.927H3a1 1 0 110-2h3V3a1 1 0 011-1zm6 6a1 1 0 01.894.553l2.991 5.982a.869.869 0 01.02.037l.99 1.98a1 1 0 11-1.79.895L15.383 16h-4.764l-.724 1.447a1 1 0 11-1.788-.894l.99-1.98.019-.038 2.99-5.982A1 1 0 0113 8zm-1.382 6h2.764L13 11.236 11.618 14z" clip-rule="evenodd"/>
                    </svg>
                    {{ getLanguageName(resource.language) }}
                  </span>
                  <span v-if="resource.file_type" class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-green-100 text-green-700">
                    {{ resource.file_type.toUpperCase() }}
                  </span>
                </div>

                <!-- Audio Player -->
                <div v-if="isAudio(resource) && resource.file" class="mb-6">
                  <audio :src="resource.file" controls class="w-full rounded-xl"></audio>
                </div>

                <!-- Actions -->
                <div class="flex items-center justify-between pt-6 border-t border-gray-100">
                  <a
                    v-if="resource.file"
                    :href="resource.file"
                    target="_blank"
                    rel="noopener"
                    class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white text-sm font-bold rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 transform hover:scale-105"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
                    </svg>
                    Download
                  </a>
                  <span v-else class="px-6 py-3 bg-gray-100 text-gray-500 text-sm font-semibold rounded-xl">
                    Coming Soon
                  </span>

                  <!-- Download Count -->
                  <div class="flex items-center gap-2 text-sm text-gray-500">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
                    </svg>
                    <span class="font-bold text-gray-700">{{ resource.download_count || 0 }}</span>
                  </div>
                </div>
              </div>
            </article>
          </div>

          <!-- Empty State -->
          <div v-else class="text-center py-20">
            <svg class="w-24 h-24 mx-auto text-gray-300 mb-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
            </svg>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">No resources found</h3>
            <p class="text-gray-600">Try adjusting your search or filters</p>
          </div>

          <!-- Pagination -->
          <div v-if="pagination.next || pagination.previous" class="mt-12 flex justify-center gap-4">
            <button
              :disabled="!pagination.previous || loading"
              @click="prevPage"
              class="px-6 py-3 rounded-xl border-2 border-gray-200 hover:border-blue-500 hover:bg-blue-50 disabled:opacity-50 disabled:cursor-not-allowed font-semibold transition-all"
            >
              Previous
            </button>
            <button
              :disabled="!pagination.next || loading"
              @click="nextPage"
              class="px-6 py-3 rounded-xl border-2 border-gray-200 hover:border-blue-500 hover:bg-blue-50 disabled:opacity-50 disabled:cursor-not-allowed font-semibold transition-all"
            >
              Next
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, computed } from 'vue'
import { useResourcesStore } from '@/store/resources'
import { api } from '@/utils/axios'
import Loader from '@/components/common/Loader.vue'
import { Chart as ChartJS, ArcElement, Tooltip, Legend, BarElement, CategoryScale, LinearScale, Title } from 'chart.js'
import { Doughnut, Bar } from 'vue-chartjs'

ChartJS.register(ArcElement, Tooltip, Legend, BarElement, CategoryScale, LinearScale, Title)

const resourcesStore = useResourcesStore()
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
        '#6366F1', // Indigo
        '#8B5CF6', // Purple
        '#14B8A6', // Teal
        '#F59E0B'  // Amber
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
      backgroundColor: '#3B82F6',
      borderRadius: 8,
      data
    }]
  }
})

const doughnutOptions = {
  responsive: true,
  maintainAspectRatio: true,
  plugins: {
    legend: {
      position: 'bottom',
      labels: {
        padding: 20,
        font: {
          size: 13,
          weight: '600'
        },
        usePointStyle: true,
        pointStyle: 'circle'
      }
    },
    tooltip: {
      backgroundColor: 'rgba(0, 0, 0, 0.8)',
      padding: 12,
      titleFont: {
        size: 14,
        weight: 'bold'
      },
      bodyFont: {
        size: 13
      },
      borderColor: 'rgba(255, 255, 255, 0.1)',
      borderWidth: 1
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
      backgroundColor: 'rgba(0, 0, 0, 0.8)',
      padding: 12,
      titleFont: {
        size: 14,
        weight: 'bold'
      },
      bodyFont: {
        size: 13
      }
    }
  },
  scales: {
    y: {
      beginAtZero: true,
      ticks: {
        stepSize: 1,
        font: {
          size: 12,
          weight: '600'
        }
      },
      grid: {
        color: 'rgba(0, 0, 0, 0.05)'
      }
    },
    x: {
      ticks: {
        font: {
          size: 12,
          weight: '600'
        }
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

async function fetchList(pageUrl = null) {
  loading.value = true
  try {
    const params = {
      status: 'PUBLISHED'
    }
    if (search.value) params.search = search.value
    if (category.value) params.category = category.value
    if (language.value) params.language = language.value
    const data = await resourcesStore.fetchResources(params)
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
  const url = new URL(pagination.value.next)
  const page = url.searchParams.get('page')
  fetchList({ page })
}

function prevPage() {
  if (!pagination.value.previous) return
  const url = new URL(pagination.value.previous)
  const page = url.searchParams.get('page')
  fetchList({ page })
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

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
