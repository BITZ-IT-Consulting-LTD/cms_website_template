<template>
  <div class="bg-gray-50 py-12">
    <div class="container-custom">
      <!-- Heading -->
      <div class="text-center mb-10">
        <h1 class="text-4xl md:text-5xl font-extrabold mb-3">Reports & Insights</h1>
        <p class="text-gray-600 max-w-3xl mx-auto">Explore the data collected by Sauti Uganda 116 helpline to understand the trends and patterns in child abuse and neglect across the country.</p>
      </div>

      <!-- Filters -->
      <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6 mb-8">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 items-end">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Search</label>
            <div class="relative">
              <input v-model="search" class="w-full form-input pl-10" placeholder="Search reports by keyword" />
              <svg class="w-5 h-5 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35M10 18a8 8 0 100-16 8 8 0 000 16z"/></svg>
            </div>
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Region</label>
            <select v-model="region" class="form-input">
              <option value="all">All Regions</option>
              <option>Central</option>
              <option>Eastern</option>
              <option>Northern</option>
              <option>Western</option>
            </select>
          </div>
          <div class="flex md:justify-end">
            <button class="pill pill-primary">Apply Filters</button>
          </div>
        </div>
        <!-- Date range placeholder strip -->
        <div class="mt-6 h-20 rounded-xl bg-gray-50 border border-gray-200 flex items-center justify-center text-gray-500 text-sm">Date Range Picker (placeholder)</div>
      </div>

      <!-- Cards grid -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Cases Per Category (Pie Chart) -->
        <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
          <h4 class="font-semibold mb-4">Cases Per Category</h4>
          <PieChart :labels="categoryLabels" :values="categoryValues" />
          <div class="mt-4 text-sm text-gray-600">
            <p class="font-medium mb-2">Key Insights:</p>
            <ul class="space-y-1 text-xs">
              <li>• Child Neglect: 48.1% (2,746 cases)</li>
              <li>• Physical Violence: 17.0% (817 cases)</li>
              <li>• Sexual Violence: 14.7% (595 cases)</li>
              <li>• Economic Violence: 5.0% (423 cases)</li>
            </ul>
          </div>
        </div>
        
        <!-- Summary -->
        <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
          <h4 class="font-semibold mb-4">Summary</h4>
          <div class="space-y-3 text-sm text-gray-600">
            <p><strong>Child Neglect</strong> remains the highest reported category, accounting for 48.1% of all cases (2,746 cases). This reflects the critical need for child protection services and support systems.</p>
            <p><strong>Physical Violence</strong> follows at 17.0% (817 cases), while <strong>Sexual Violence</strong> represents 14.7% (595 cases), highlighting the urgent need for comprehensive protection services.</p>
            <p>These trends indicate the importance of continued awareness campaigns and accessible reporting mechanisms across all regions of Uganda.</p>
          </div>
        </div>

        <!-- Cases Per Region Over Time -->
        <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
          <h4 class="font-semibold mb-4">Cases Per Region</h4>
          <p class="text-xs text-gray-500 mb-3">01/01/2025 12:00 AM - 31/12/2025 12:00 AM</p>
          <RegionChart :labels="timelineLabels" :regionData="regionTimeSeriesData" />
          <div class="mt-4 text-xs text-gray-600">
            <p class="font-medium mb-2">Regions:</p>
            <div class="grid grid-cols-3 gap-2">
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-purple-500"></div>
                <span>Central</span>
              </div>
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-green-500"></div>
                <span>Eastern</span>
              </div>
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-orange-500"></div>
                <span>Northern</span>
              </div>
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-blue-500"></div>
                <span>Western</span>
              </div>
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-dark-blue-500"></div>
                <span>International</span>
              </div>
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-light-green-500"></div>
                <span>Unknown</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Summary -->
        <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
          <h4 class="font-semibold mb-4">Regional Trends</h4>
          <div class="space-y-3 text-sm text-gray-600">
            <p><strong>Central region</strong> consistently reports the highest number of cases throughout the year, with peaks in May (470 cases) and April (330 cases).</p>
            <p><strong>Eastern region</strong> shows steady reporting with 1,320 total cases, while <strong>Northern region</strong> has 650 cases, with notable spikes in May (290 cases) and October (170 cases).</p>
            <p>This data helps guide resource allocation and targeted intervention programs across different regions.</p>
          </div>
        </div>

        <!-- Case Categories per Age Group -->
        <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
          <h4 class="font-semibold mb-4">Case Categories per Age Group</h4>
          <AgeGroupChart :labels="ageGroupLabels" :ageData="ageGroupData" />
          <div class="mt-4 text-xs text-gray-600">
            <p class="font-medium mb-2">Age Groups:</p>
            <div class="grid grid-cols-2 gap-2">
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-purple-500"></div>
                <span>0-04</span>
              </div>
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-green-500"></div>
                <span>05-09</span>
              </div>
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-blue-500"></div>
                <span>10-13</span>
              </div>
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-green-400"></div>
                <span>14-17</span>
              </div>
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-pink-500"></div>
                <span>18-24</span>
              </div>
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-orange-500"></div>
                <span>25-30</span>
              </div>
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-orange-400"></div>
                <span>31-45</span>
              </div>
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-dark-purple-500"></div>
                <span>Above 60</span>
              </div>
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-light-green-500"></div>
                <span>Unknown</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Case Categories per Gender -->
        <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
          <h4 class="font-semibold mb-4">Case Categories per Gender</h4>
          <GenderChart :labels="ageGroupLabels" :genderData="genderData" />
          <div class="mt-4 text-xs text-gray-600">
            <p class="font-medium mb-2">Gender Breakdown:</p>
            <div class="grid grid-cols-3 gap-2">
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-purple-500"></div>
                <span>Female</span>
              </div>
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-green-500"></div>
                <span>Male</span>
              </div>
              <div class="flex items-center">
                <div class="w-3 h-3 rounded mr-2 bg-light-green-500"></div>
                <span>Unknown</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Footer row like mock -->
      <div class="text-center text-sm text-gray-500 mt-10">
        <router-link to="/privacy" class="hover:text-gray-700">Privacy Policy</router-link>
        <span class="mx-2">•</span>
        <router-link to="/terms" class="hover:text-gray-700">Terms of Service</router-link>
        <span class="mx-2">•</span>
        <router-link to="/contact" class="hover:text-gray-700">Contact Us</router-link>
        <p class="mt-2">© 2024 Sauti Uganda 116 helpline. All rights reserved.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { Bar, Line, Pie, Doughnut } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  ArcElement
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, LineElement, CategoryScale, LinearScale, PointElement, ArcElement)

const search = ref('')
const region = ref('all')

// Mock datasets based on real data patterns
// Cases Per Category (Pie Chart Data)
const categoryLabels = [
  'Child Neglect',
  'Physical Violence',
  'Sexual Violence',
  'Economic Violence',
  'Emotional & Psychological Abuse',
  'Murder',
  'Trafficking in Persons',
  'Child Exploitation',
  'Harmful Traditional Practices',
  'Others',
  'Threatening Violence',
  'Online Sexual Abuse & Violence'
]
const categoryValues = [2746, 817, 595, 423, 134, 120, 118, 112, 102, 46, 75, 7]

// Cases Per Region Over Time (Monthly data for 2025 - stacked by region)
const timelineLabels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
const regionTimeSeriesData = computed(() => ({
  'CENTRAL': [310, 230, 260, 330, 470, 270, 330, 270, 260, 280, 20, 5],
  'EASTERN': [100, 110, 110, 120, 150, 120, 120, 120, 120, 150, 5, 0],
  'NORTHERN': [20, 70, 20, 20, 290, 20, 20, 20, 20, 170, 5, 0],
  'WESTERN': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0],
  'INTERNATIONAL': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0],
  'Unknown': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0]
}))

// Cases Per Region (Total for the year)
const regionLabels = ['Central', 'Eastern', 'Northern', 'Western', 'International', 'Unknown']
const regionValues = [2930, 1320, 650, 100, 60, 60]

// Cases Per Category by Age Group (for stacked bar chart)
const ageGroupLabels = [
  'Child Neglect',
  'Physical Violence',
  'Sexual Violence',
  'Economic Violence',
  'Child Exploitation',
  'Emotional & Psychological Abuse',
  'Harmful Traditional Practices',
  'Murder',
  'Trafficking in Persons',
  'Threatening Violence',
  'Others',
  'Online Sexual Abuse & Violence'
]
const ageGroupData = {
  '0-04': [895, 334, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  '05-09': [620, 95, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  '10-13': [489, 0, 95, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  '14-17': [0, 170, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  '18-24': [0, 163, 170, 145, 0, 0, 0, 0, 0, 0, 0, 0],
  '25-30': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  '31-45': [0, 161, 68, 89, 0, 0, 0, 0, 0, 0, 0, 0],
  '46-59': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  'Above 60': [0, 28, 130, 97, 0, 0, 0, 0, 0, 0, 0, 0],
  'Unknown': [646, 0, 0, 92, 0, 0, 0, 0, 0, 0, 0, 0]
}

// Cases Per Category by Gender (for stacked bar chart)
const genderData = {
  'Female': [1402, 482, 557, 260, 95, 88, 95, 79, 105, 13, 37, 5],
  'Male': [1297, 326, 32, 155, 12, 43, 7, 39, 10, 2, 9, 2],
  'Unknown': [62, 11, 3, 11, 4, 2, 0, 3, 2, 0, 0, 0]
}

// Chart components
const BarChart = {
  name: 'BarChart',
  props: { labels: Array, values: Array, color: { type: String, default: '#f97316' } },
  components: { Bar },
  setup(props) {
    const data = computed(() => ({
      labels: props.labels,
      datasets: [{ data: props.values, backgroundColor: props.color, borderRadius: 10 }]
    }))
    const options = { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } } }
    return { data, options }
  },
  template: `<div style="height:200px"><Bar :data="data" :options="options" /></div>`
}

const PieChart = {
  name: 'PieChart',
  props: { labels: Array, values: Array },
  components: { Pie },
  setup(props) {
    const data = computed(() => ({
      labels: props.labels,
      datasets: [{
        data: props.values,
        backgroundColor: [
          '#10b981', // Child Neglect - green
          '#3b82f6', // Physical Violence - blue
          '#8b5cf6', // Sexual Violence - purple
          '#f59e0b', // Economic Violence - orange
          '#ec4899', // Emotional Abuse - pink
          '#ef4444', // Murder - red
          '#06b6d4', // Trafficking - cyan
          '#84cc16', // Child Exploitation - lime
          '#f97316', // Harmful Practices - orange
          '#64748b', // Others - gray
          '#6366f1', // Threatening - indigo
          '#fbbf24' // Online Abuse - yellow
        ]
      }]
    }))
    const options = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: function(context) {
              const total = context.dataset.data.reduce((a, b) => a + b, 0)
              const percentage = ((context.parsed / total) * 100).toFixed(1)
              return `${context.label}: ${context.parsed} (${percentage}%)`
            }
          }
        }
      }
    }
    return { data, options }
  },
  template: `<div style="height:300px"><Pie :data="data" :options="options" /></div>`
}

const RegionChart = {
  name: 'RegionChart',
  props: { labels: Array, regionData: Object },
  components: { Bar },
  setup(props) {
    const data = computed(() => ({
      labels: props.labels,
      datasets: [
        {
          label: 'CENTRAL',
          data: props.regionData.CENTRAL,
          backgroundColor: '#a855f7' // purple
        },
        {
          label: 'EASTERN',
          data: props.regionData.EASTERN,
          backgroundColor: '#10b981' // green
        },
        {
          label: 'NORTHERN',
          data: props.regionData.NORTHERN,
          backgroundColor: '#f97316' // orange
        },
        {
          label: 'WESTERN',
          data: props.regionData.WESTERN,
          backgroundColor: '#3b82f6' // blue
        },
        {
          label: 'INTERNATIONAL',
          data: props.regionData.INTERNATIONAL,
          backgroundColor: '#1e40af' // dark blue
        },
        {
          label: 'Unknown',
          data: props.regionData.Unknown,
          backgroundColor: '#86efac' // light green
        }
      ]
    }))
    const options = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false }
      },
      scales: {
        x: { stacked: true },
        y: { stacked: true, beginAtZero: true, max: 500 }
      }
    }
    return { data, options }
  },
  template: `<div style="height:300px"><Bar :data="data" :options="options" /></div>`
}

const AgeGroupChart = {
  name: 'AgeGroupChart',
  props: { labels: Array, ageData: Object },
  components: { Bar },
  setup(props) {
    const ageGroups = ['0-04', '05-09', '10-13', '14-17', '18-24', '25-30', '31-45', '46-59', 'Above 60', 'Unknown']
    const colors = ['#a855f7', '#10b981', '#3b82f6', '#86efac', '#ec4899', '#f97316', '#f59e0b', '#f59e0b', '#7c3aed', '#86efac']
    
    const data = computed(() => ({
      labels: props.labels,
      datasets: ageGroups.map((age, idx) => ({
        label: age,
        data: props.ageData[age] || [],
        backgroundColor: colors[idx]
      }))
    }))
    const options = {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false }
      },
      scales: {
        x: { stacked: true, beginAtZero: true, max: 3000 },
        y: { stacked: true }
      }
    }
    return { data, options }
  },
  template: `<div style="height:400px"><Bar :data="data" :options="options" /></div>`
}

const GenderChart = {
  name: 'GenderChart',
  props: { labels: Array, genderData: Object },
  components: { Bar },
  setup(props) {
    const data = computed(() => ({
      labels: props.labels,
      datasets: [
        {
          label: 'Female',
          data: props.genderData.Female,
          backgroundColor: '#a855f7' // purple
        },
        {
          label: 'Male',
          data: props.genderData.Male,
          backgroundColor: '#10b981' // green
        },
        {
          label: 'Unknown',
          data: props.genderData.Unknown,
          backgroundColor: '#86efac' // light green
        }
      ]
    }))
    const options = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false }
      },
      scales: {
        x: { stacked: true },
        y: { stacked: true, beginAtZero: true, max: 3000 }
      }
    }
    return { data, options }
  },
  template: `<div style="height:400px"><Bar :data="data" :options="options" /></div>`
}

const LineChart = {
  name: 'LineChart',
  props: { labels: Array, values: Array },
  components: { Line },
  setup(props) {
    const data = computed(() => ({
      labels: props.labels,
      datasets: [{ data: props.values, borderColor: '#60a5fa', backgroundColor: 'rgba(96,165,250,0.2)', fill: true, tension: 0.35 }]
    }))
    const options = { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { y: { beginAtZero: true } } }
    return { data, options }
  },
  template: `<div style="height:200px"><Line :data="data" :options="options" /></div>`
}
</script>

