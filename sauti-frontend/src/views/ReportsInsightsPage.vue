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

             <!-- Total Migrant Cases -->
            <div class="bg-white rounded-3xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-shadow">
               <p class="text-secondary/60 text-xs font-bold uppercase tracking-widest mb-2">Total Migrant Cases</p>
               <div class="text-3xl font-black text-secondary-light">
                  {{ formatNumber(stats.total_migrant_workers) }}
               </div>
            </div>
          </div>
        </section>

        <!-- 3. Filter Bar -->
        <section class="mb-8">
          <div class="flex items-center gap-4">
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
        </section>

        <!-- 4. Charts Grid (2x2) -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-10">

          <!-- Chart 1: Category vs Client Sex -->
          <div class="card-base group">
            <h3 class="campaign-header text-xl text-secondary mb-8 flex items-center gap-4">
              <div class="w-1.5 h-6 bg-primary rounded-full"></div>
              Abuse Category vs Client Sex
            </h3>
            <div class="h-[400px]">
              <BarChart :chartData="filteredCategoryBySex" />
            </div>
          </div>

          <!-- Chart 2: Category vs Client Region -->
          <div class="card-base group">
            <h3 class="campaign-header text-xl text-secondary mb-8 flex items-center gap-4">
               <div class="w-1.5 h-6 bg-secondary rounded-full"></div>
               Abuse Category vs Client Region
            </h3>
            <div class="h-[400px]">
              <BarChart :chartData="filteredCategoryByRegion" />
            </div>
          </div>

          <!-- Chart 3: Category vs Client Age Group -->
          <div class="card-base group">
            <h3 class="campaign-header text-xl text-secondary mb-8 flex items-center gap-4">
               <div class="w-1.5 h-6 bg-hotline rounded-full"></div>
               Abuse Category vs Client Age Group
            </h3>
            <div class="h-[400px]">
              <BarChart :chartData="filteredCategoryByAgeGroup" />
            </div>
          </div>

          <!-- Chart 4: Category vs Client District -->
          <div class="card-base group">
            <h3 class="campaign-header text-xl text-secondary mb-8 flex items-center gap-4">
               <div class="w-1.5 h-6 bg-emergency rounded-full"></div>
               Abuse Category vs Client District
            </h3>
            <div class="h-[400px]">
              <BarChart :chartData="filteredCategoryByDistrict" />
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
import { api } from '@/utils/axios'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const loading = ref(true)
const error = ref(null)

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

// --- Data State ---
const stats = ref({
  total_calls: 0,
  total_cases: 0,
  total_gbv_cases: 0,
  total_sea_cases: 0,
  total_migrant_workers: 0
})

const charts = ref({
  categoryBySex: { labels: [], datasets: [] },
  categoryByRegion: { labels: [], datasets: [] },
  categoryByAgeGroup: { labels: [], datasets: [] },
  categoryByDistrict: { labels: [], datasets: [] }
})

const caseTypeFilter = ref('All')

// --- Filter Logic ---
const getAllowedCategories = () => {
  switch (caseTypeFilter.value) {
    case 'Abuse': return ABUSE_CATEGORIES
    case 'Counseling': return COUNSELING_CATEGORIES
    case 'Information Inquiry': return INFO_CATEGORIES
    default: return null // null = show all
  }
}

const filterChartData = (chartData) => {
  const allowed = getAllowedCategories()
  if (!allowed) return chartData
  if (!chartData || !chartData.labels || !chartData.labels.length) return chartData

  // Find indices of labels that match the allowed categories
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

const filteredCategoryBySex = computed(() => formatChartData(filterChartData(charts.value.categoryBySex)))
const filteredCategoryByRegion = computed(() => formatChartData(filterChartData(charts.value.categoryByRegion)))
const filteredCategoryByAgeGroup = computed(() => formatChartData(filterChartData(charts.value.categoryByAgeGroup)))
const filteredCategoryByDistrict = computed(() => formatChartData(filterChartData(charts.value.categoryByDistrict)))

// --- Helper Functions ---
const formatNumber = (num) => {
  return num !== null && num !== undefined ? num.toLocaleString() : '0'
}

// --- API Fetch Logic ---
const fetchDashboardData = async () => {
  loading.value = true
  try {
    const [statsResponse, chartsResponse] = await Promise.all([
      api.get('/dashboard/helpline-stats/'),
      api.get('/dashboard/helpline-charts/')
    ])

    if (statsResponse.data) {
      stats.value = {
        total_calls: statsResponse.data.total_calls || 0,
        total_cases: statsResponse.data.total_cases || 0,
        total_gbv_cases: statsResponse.data.total_gbv_cases || 0,
        total_sea_cases: statsResponse.data.total_sea_cases || 0,
        total_migrant_workers: statsResponse.data.total_migrant_workers || 0
      }
    }

    if (chartsResponse.data) {
      charts.value = {
        categoryBySex: chartsResponse.data.categoryBySex || { labels: [], datasets: [] },
        categoryByRegion: chartsResponse.data.categoryByRegion || { labels: [], datasets: [] },
        categoryByAgeGroup: chartsResponse.data.categoryByAgeGroup || { labels: [], datasets: [] },
        categoryByDistrict: chartsResponse.data.categoryByDistrict || { labels: [], datasets: [] }
      }
    }

  } catch (err) {
    console.error('Failed to fetch dashboard data:', err)
    error.value = 'Could not load statistics at this time.'
  } finally {
    loading.value = false
  }
}

// Format chart data from API response to Chart.js format (adds colors)
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
  const palette = ['#0087CF', '#006837', '#F7941E', '#9DC83E', '#ED1C24', '#0F172A',
                    '#6366F1', '#EC4899', '#14B8A6', '#F59E0B', '#8B5CF6', '#EF4444']
  return palette[index % palette.length]
}

// Auto-refresh interval reference
let refreshInterval = null

onMounted(() => {
  fetchDashboardData()

  refreshInterval = setInterval(() => {
    fetchDashboardData()
  }, 60000)
})

onUnmounted(() => {
  if (refreshInterval) {
    clearInterval(refreshInterval)
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
