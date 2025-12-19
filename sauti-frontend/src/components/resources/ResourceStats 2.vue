<template>
  <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6 mb-8">
    <h2 class="text-xl font-bold text-gray-900 mb-6">Key Statistics</h2>
    
    <div v-if="loading" class="flex justify-center py-12">
      <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-500"></div>
    </div>
    
    <div v-else-if="error" class="text-center py-8 text-red-500">
      {{ error }}
    </div>
    
    <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-8">
      <!-- Cases by Category -->
      <div>
        <h3 class="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-4 text-center">Cases by Category</h3>
        <div class="h-64 relative">
          <Doughnut :data="categoryData" :options="chartOptions" />
        </div>
      </div>
      
      <!-- Reports Over Time -->
      <div>
        <h3 class="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-4 text-center">Reports Over Time (Last 6 Months)</h3>
        <div class="h-64 relative">
          <Bar :data="timeData" :options="barOptions" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { Chart as ChartJS, ArcElement, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import { Doughnut, Bar } from 'vue-chartjs'
import { api } from '@/utils/axios'

ChartJS.register(ArcElement, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const loading = ref(true)
const error = ref(null)
const stats = ref(null)

const categoryData = computed(() => {
  if (!stats.value?.by_category) return { labels: [], datasets: [] }
  
  const labels = stats.value.by_category.map(item => formatCategory(item.category))
  const data = stats.value.by_category.map(item => item.count)
  
  return {
    labels,
    datasets: [{
      backgroundColor: ['#009EDB', '#7C3AED', '#0D9488', '#F59E0B'],
      data
    }]
  }
})

const timeData = computed(() => {
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
      backgroundColor: '#8B4000',
      data
    }]
  }
})

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: 'bottom'
    }
  }
}

const barOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false
    }
  },
  scales: {
    y: {
      beginAtZero: true,
      ticks: {
        stepSize: 1
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

onMounted(async () => {
  try {
    // We need to fetch from the public endpoint
    // Assuming api.get handles the base URL
    const response = await api.get('/reports/stats/public/')
    stats.value = response.data
  } catch (err) {
    console.error('Failed to fetch stats:', err)
    error.value = 'Failed to load statistics'
  } finally {
    loading.value = false
  }
})
</script>
