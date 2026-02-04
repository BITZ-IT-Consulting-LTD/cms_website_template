<template>
  <div class="min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <h1 class="page-header-title">
          Reports <span class="text-primary">&</span> Insights
        </h1>
        <p class="page-header-subtitle">
          Real-time data and statistics from the Sauti 116 Helpline.
        </p>
      </div>
    </header>

    <div class="section-padding !pt-0">
      <div class="container-custom section-rhythm">

        <!-- 2. Quick Stats Row -->
        <section aria-label="Quick Statistics" class="mb-16">
          <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-6">
            <!-- Total Calls -->
            <div class="bg-white rounded-3xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-shadow">
              <p class="text-secondary/60 text-xs font-bold uppercase tracking-widest mb-2">Total Calls</p>
              <div class="text-3xl font-black text-primary">
                 {{ formatNumber(stats.total_calls) }}
              </div>
            </div>

            <!-- Total Cases -->
            <div class="bg-white rounded-3xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-shadow">
              <p class="text-secondary/60 text-xs font-bold uppercase tracking-widest mb-2">Total Cases</p>
              <div class="text-3xl font-black text-secondary">
                 {{ formatNumber(stats.total_cases) }}
              </div>
            </div>

            <!-- Total GBV Cases -->
            <div class="bg-white rounded-3xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-shadow">
               <p class="text-secondary/60 text-xs font-bold uppercase tracking-widest mb-2">Total GBV Cases</p>
               <div class="text-3xl font-black text-hotline">
                  {{ formatNumber(stats.total_gbv_cases) }}
               </div>
            </div>

            <!-- Total SEA Cases -->
            <div class="bg-white rounded-3xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-shadow">
               <p class="text-secondary/60 text-xs font-bold uppercase tracking-widest mb-2">Total SEA Cases</p>
               <div class="text-3xl font-black text-emergency">
                  {{ formatNumber(stats.total_sea_cases) }}
               </div>
            </div>

             <!-- Migrant Workers -->
            <div class="bg-white rounded-3xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-shadow">
               <p class="text-secondary/60 text-xs font-bold uppercase tracking-widest mb-2">Migrant Workers</p>
               <div class="text-3xl font-black text-secondary-light">
                  {{ formatNumber(stats.total_migrant_workers) }}
               </div>
            </div>
          </div>
        </section>

        <!-- 3. Charts Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-10">
          
          <!-- Chart 1: Cases by Source -->
          <div class="card-base group">
            <h3 class="campaign-header text-xl text-secondary mb-8 flex items-center gap-4">
              <div class="w-1.5 h-6 bg-primary rounded-full"></div>
              Cases by Source
            </h3>
            <div class="h-[400px]">
              <BarChart :chartData="charts.subcategoryBySex" />
            </div>
          </div>

          <!-- Chart 2: Top 15 Abuse Subcategories Distribution -->
          <div class="card-base group">
            <h3 class="campaign-header text-xl text-secondary mb-8 flex items-center gap-4">
               <div class="w-1.5 h-6 bg-secondary rounded-full"></div>
               Top 15 Abuse Subcategories Distribution
            </h3>
            <div class="h-[400px]">
              <BarChart :chartData="charts.subcategoryByAge" :horizontal="true" />
            </div>
          </div>

          <!-- Chart 3: Cases by Region -->
           <div class="card-base group lg:col-span-2">
            <h3 class="campaign-header text-xl text-secondary mb-8 flex items-center gap-4">
               <div class="w-1.5 h-6 bg-hotline rounded-full"></div>
               Cases by Region
            </h3>
            <div class="h-[450px]">
              <BarChart :chartData="charts.subcategoryByRegion" />
            </div>
          </div>

          <!-- Chart 4: Top 15 Abuse Subcategories -->
          <div class="card-base group lg:col-span-2">
            <h3 class="campaign-header text-xl text-secondary mb-8 flex items-center gap-4">
               <div class="w-1.5 h-6 bg-secondary-light rounded-full"></div>
               Top 15 Abuse Subcategories (Detailed)
            </h3>
            <div class="h-[500px]">
               <BarChart :chartData="charts.subcategoryByDistrict" :horizontal="true" />
            </div>
          </div>

        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import { api } from '@/utils/axios' // Assuming an axios helper exists

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const loading = ref(true)
const error = ref(null)

// --- Data State ---
const stats = ref({
  total_calls: 0,
  total_cases: 0,
  total_gbv_cases: 0,
  total_sea_cases: 0,
  total_migrant_workers: 0
})

const charts = ref({
  subcategoryBySex: { labels: [], datasets: [] },
  subcategoryByAge: { labels: [], datasets: [] },
  subcategoryByRegion: { labels: [], datasets: [] },
  subcategoryByDistrict: { labels: [], datasets: [] }
})

// --- Helper Functions ---
const formatNumber = (num) => {
  return num !== null && num !== undefined ? num.toLocaleString() : '0'
}

// --- API Fetch Logic ---
const fetchDashboardData = async () => {
  loading.value = true
  try {
    // Fetch helpline statistics and charts from the correct endpoints
    const [statsResponse, chartsResponse] = await Promise.all([
      api.get('/dashboard/helpline-stats/'),
      api.get('/dashboard/helpline-charts/')
    ])

    // Populate Quick Stats (data is returned directly, not nested under .stats)
    if (statsResponse.data) {
      stats.value = {
        total_calls: statsResponse.data.total_calls || 0,
        total_cases: statsResponse.data.total_cases || 0,
        total_gbv_cases: statsResponse.data.total_gbv_cases || 0,
        total_sea_cases: statsResponse.data.total_sea_cases || 0,
        total_migrant_workers: statsResponse.data.total_migrant_workers || 0
      }
      console.log('📊 Stats updated:', stats.value)
    }

    // Populate Charts with Real Data (data is returned directly)
    if (chartsResponse.data) {
      charts.value = {
        subcategoryBySex: formatChartData(chartsResponse.data.subcategoryBySex),
        subcategoryByAge: formatChartData(chartsResponse.data.subcategoryByAge),
        subcategoryByRegion: formatChartData(chartsResponse.data.subcategoryByRegion),
        subcategoryByDistrict: formatChartData(chartsResponse.data.subcategoryByDistrict)
      }
      console.log('📈 Charts updated:', Object.keys(charts.value))
    }

  } catch (err) {
    console.error('❌ Failed to fetch dashboard data:', err)
    error.value = 'Could not load statistics at this time.'
  } finally {
    loading.value = false
  }
}

// Format chart data from API response to Chart.js format
const formatChartData = (apiData) => {
  if (!apiData || !apiData.labels || !apiData.datasets) {
    return { labels: [], datasets: [] }
  }

  return {
    labels: apiData.labels,
    datasets: apiData.datasets.map((ds, index) => ({
      label: ds.label || 'Data',
      data: ds.data || [],
      backgroundColor: getBrandColor(index),
      borderRadius: 4
    }))
  }
}

const getBrandColor = (index) => {
  const palette = ['#0087CF', '#006837', '#F7941E', '#9DC83E', '#ED1C24', '#0F172A']
  return palette[index % palette.length]
}

// Auto-refresh interval reference
let refreshInterval = null

onMounted(() => {
  // Initial fetch
  fetchDashboardData()

  // Set up auto-refresh every 60 seconds for real-time updates
  refreshInterval = setInterval(() => {
    console.log('🔄 Auto-refreshing helpline data...')
    fetchDashboardData()
  }, 60000) // 60 seconds = 60,000 milliseconds

  console.log('✅ Real-time updates enabled (refresh every 60 seconds)')
})

// Cleanup interval when component unmounts
onUnmounted(() => {
  if (refreshInterval) {
    clearInterval(refreshInterval)
    console.log('🛑 Auto-refresh stopped')
  }
})

// --- Chart Component ---
const BarChart = {
  name: 'BarChart',
  props: {
    chartData: { type: Object, default: () => ({ labels: [], datasets: [] }) },
    horizontal: { type: Boolean, default: false }
  },
  components: { Bar },
  setup(props) {
    const options = computed(() => ({
      indexAxis: props.horizontal ? 'y' : 'x',
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { position: 'bottom', labels: { usePointStyle: true, boxWidth: 8 } }
      },
      scales: {
        x: { stacked: true, grid: { display: false } },
        y: { stacked: true, beginAtZero: true }
      }
    }))

    return { options }
  },
  template: `<Bar :data="chartData" :options="options" />`
}
</script>
