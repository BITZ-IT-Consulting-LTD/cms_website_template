<template>
  <div class="bg-gray-50 py-12">
    <div class="container-custom">
      <!-- Heading -->
      <div class="text-center mb-10">
        <h1 class="text-4xl md:text-5xl font-extrabold mb-3">Reports & Insights</h1>
        <p class="text-gray-600 max-w-3xl mx-auto">Explore the data collected by Sauti Uganda Child Helpline to understand the trends and patterns in child abuse and neglect across the country.</p>
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
        <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
          <h4 class="font-semibold mb-2">Reported Cases by Category</h4>
          <BarChart :labels="categoryLabels" :values="categoryValues" />
        </div>
        <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
          <h4 class="font-semibold mb-2">Summary</h4>
          <p class="text-gray-600 text-sm">Child Neglect remains the highest reported category, accounting for 35% of all cases. Physical abuse follows closely at 28%, while emotional abuse represents 20%. Sexual abuse and exploitation make up the remainder.</p>
        </div>
        <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
          <h4 class="font-semibold mb-2">Reported Cases Over Time</h4>
          <LineChart :labels="timelineLabels" :values="timelineValues" />
        </div>
        <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
          <h4 class="font-semibold mb-2">Summary</h4>
          <p class="text-gray-600 text-sm">Reports have steadily increased over the last five years, with a notable rise during 2020–2021, likely due to increased awareness and access to support systems.</p>
        </div>
        <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
          <h4 class="font-semibold mb-2">Reported Cases by Region</h4>
          <BarChart :labels="regionLabels" :values="regionValues" :color="'#60a5fa'" />
        </div>
        <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
          <h4 class="font-semibold mb-2">Summary</h4>
          <p class="text-gray-600 text-sm">Central region consistently reports the highest number of cases, followed by Eastern. Northern and Western regions remain priorities for targeted outreach.</p>
        </div>
      </div>

      <!-- Footer row like mock -->
      <div class="text-center text-sm text-gray-500 mt-10">
        <router-link to="/privacy" class="hover:text-gray-700">Privacy Policy</router-link>
        <span class="mx-2">•</span>
        <router-link to="/terms" class="hover:text-gray-700">Terms of Service</router-link>
        <span class="mx-2">•</span>
        <router-link to="/contact" class="hover:text-gray-700">Contact Us</router-link>
        <p class="mt-2">© 2024 Sauti Uganda Child Helpline. All rights reserved.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { Bar, Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, LineElement, CategoryScale, LinearScale, PointElement)

const search = ref('')
const region = ref('all')

// Mock datasets
const categoryLabels = ['Neglect', 'Physical', 'Emotional', 'Sexual', 'Exploitation', 'Other']
const categoryValues = [380, 260, 210, 160, 110, 70]

const timelineLabels = ['2019', '2020', '2021', '2022', '2023']
const timelineValues = [900, 1200, 1500, 1300, 1700]

const regionLabels = ['Central', 'Eastern', 'Northern', 'Western']
const regionValues = [40, 25, 19, 16]

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

