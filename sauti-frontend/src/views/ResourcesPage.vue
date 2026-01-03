<template>
  <div class="min-h-screen bg-sauti-neutral py-16 md:py-24">
    <div class="container-custom">
      <!-- Header -->
      <div class="text-center mb-20 max-w-4xl mx-auto">
        <h1 class="text-4xl md:text-5xl lg:text-7xl font-black text-sauti-darkGreen mb-6 tracking-tight">
          Resources <span class="text-sauti-blue">&</span> Publications
        </h1>
        <p class="text-xl md:text-2xl text-sauti-darkGreen/70 font-bold leading-relaxed">
          {{ settingsStore.settings.publications_description || 'Explore our library of guidance materials and research
          updates.' }}
        </p>
      </div>

      <!-- Statistics Dashboard -->
      <div class="mb-24">
        <div class="flex items-center justify-between mb-10">
          <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen">{{
            settingsStore.settings.resources_stats_title || 'Statistics Dashboard' }}</h2>
          <div class="text-[10px] font-black uppercase tracking-widest text-sauti-darkGreen/40">{{
            settingsStore.settings.resources_stats_updated || 'Real-time Data' }}</div>
        </div>

        <!-- Loading State for Stats -->
        <div v-if="statsLoading"
          class="bg-sauti-white rounded-[3rem] border-2 border-sauti-neutral p-20 text-center shadow-sm">
          <div class="animate-spin rounded-full h-16 w-16 border-b-4 border-sauti-blue mx-auto mb-6"></div>
          <p class="text-sauti-darkGreen/50 font-bold">{{ settingsStore.settings.resources_stats_loading || 'Loading
            dynamic statistics...' }}</p>
        </div>

        <!-- Error State for Stats -->
        <div v-else-if="statsError" class="bg-sauti-red/5 rounded-[3rem] border-2 border-sauti-red/20 p-12 text-center">
          <svg class="w-16 h-16 text-sauti-red mx-auto mb-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
              d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <p class="text-sauti-red font-black text-xl">{{ settingsStore.settings.resources_stats_error || 'Failed to
            load statistics' }}</p>
        </div>

        <!-- Stats Content -->
        <div v-else>
          <!-- Key Metrics Cards -->
          <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-12">
            <!-- Total Reports -->
            <div
              class="group relative bg-sauti-darkGreen rounded-[2rem] p-8 text-sauti-white shadow-2xl shadow-sauti-darkGreen/10 hover:scale-[1.02] transition-all duration-500 overflow-hidden">
              <div class="absolute -right-6 -top-6 w-32 h-32 bg-sauti-white/5 rounded-full"></div>
              <div class="relative">
                <div class="w-12 h-12 bg-sauti-white/10 rounded-xl flex items-center justify-center mb-6">
                  <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                      d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                </div>
                <h3 class="text-5xl font-black mb-1 tabular-nums tracking-tighter">{{ stats.total_reports || 0 }}</h3>
                <p class="text-[10px] font-black uppercase tracking-widest text-sauti-white/40">{{
                  settingsStore.settings.resources_total_reports || 'Total Reports' }}</p>
              </div>
            </div>

            <!-- Child Protection -->
            <div
              class="group relative bg-sauti-blue rounded-[2rem] p-8 text-sauti-white shadow-2xl shadow-sauti-blue/10 hover:scale-[1.02] transition-all duration-500 overflow-hidden">
              <div class="absolute -right-6 -top-6 w-32 h-32 bg-sauti-white/5 rounded-full"></div>
              <div class="relative">
                <div class="w-12 h-12 bg-sauti-white/10 rounded-xl flex items-center justify-center mb-6">
                  <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                      d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
                  </svg>
                </div>
                <h3 class="text-5xl font-black mb-1 tabular-nums tracking-tighter">{{
                  getCategoryCount('CHILD_PROTECTION') }}</h3>
                <p class="text-[10px] font-black uppercase tracking-widest text-sauti-white/40">{{
                  settingsStore.settings.resources_child_protection || 'Child Protection' }}</p>
              </div>
            </div>

            <!-- GBV Cases -->
            <div
              class="group relative bg-sauti-orange rounded-[2rem] p-8 text-sauti-white shadow-2xl shadow-sauti-orange/10 hover:scale-[1.02] transition-all duration-500 overflow-hidden">
              <div class="absolute -right-6 -top-6 w-32 h-32 bg-sauti-white/5 rounded-full"></div>
              <div class="relative">
                <div class="w-12 h-12 bg-sauti-white/10 rounded-xl flex items-center justify-center mb-6">
                  <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                      d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                  </svg>
                </div>
                <h3 class="text-5xl font-black mb-1 tabular-nums tracking-tighter">{{ getCategoryCount('GBV') }}</h3>
                <p class="text-[10px] font-black uppercase tracking-widest text-sauti-white/40">{{
                  settingsStore.settings.resources_gbv_cases || 'GBV Cases' }}</p>
              </div>
            </div>

            <!-- Migrant Worker -->
            <div
              class="group relative bg-sauti-lightGreen rounded-[2rem] p-8 text-sauti-white shadow-2xl shadow-sauti-lightGreen/10 hover:scale-[1.02] transition-all duration-500 overflow-hidden">
              <div class="absolute -right-6 -top-6 w-32 h-32 bg-sauti-white/5 rounded-full"></div>
              <div class="relative">
                <div class="w-12 h-12 bg-sauti-white/10 rounded-xl flex items-center justify-center mb-6">
                  <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                      d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <h3 class="text-5xl font-black mb-1 tabular-nums tracking-tighter">{{ getCategoryCount('MIGRANT') }}
                </h3>
                <p class="text-[10px] font-black uppercase tracking-widest text-sauti-white/40">{{
                  settingsStore.settings.resources_migrant_worker || 'Migrant Worker' }}</p>
              </div>
            </div>
          </div>

          <!-- Charts Section -->
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 mb-12">
            <!-- Doughnut Chart - Cases by Category -->
            <div
              class="bg-sauti-white rounded-[3rem] border-2 border-sauti-neutral p-10 shadow-sm transition-all duration-500 hover:shadow-2xl hover:shadow-sauti-darkGreen/5">
              <div class="flex items-center justify-between mb-10">
                <h3 class="text-2xl font-black text-sauti-darkGreen">{{
                  settingsStore.settings.resources_cases_by_category || 'Cases by Category' }}</h3>
                <div
                  class="px-5 py-2 bg-sauti-blue/10 text-sauti-blue text-[10px] font-black uppercase tracking-widest rounded-full">
                  {{ settingsStore.settings.resources_interactive || 'Interactive' }}
                </div>
              </div>
              <div class="h-80 flex items-center justify-center">
                <Doughnut :data="categoryChartData" :options="doughnutOptions" />
              </div>
            </div>

            <!-- Bar Chart - Reports Over Time -->
            <div
              class="bg-sauti-white rounded-[3rem] border-2 border-sauti-neutral p-10 shadow-sm transition-all duration-500 hover:shadow-2xl hover:shadow-sauti-darkGreen/5">
              <div class="flex items-center justify-between mb-10">
                <h3 class="text-2xl font-black text-sauti-darkGreen">{{
                  settingsStore.settings.resources_reports_over_time || 'Reports Over Time' }}</h3>
                <div
                  class="px-5 py-2 bg-sauti-lightGreen/10 text-sauti-lightGreen text-[10px] font-black uppercase tracking-widest rounded-full">
                  {{ settingsStore.settings.resources_last_6_months || 'Last 6 Months' }}
                </div>
              </div>
              <div class="h-80">
                <Bar :data="timeChartData" :options="barOptions" />
              </div>
            </div>
          </div>

          <!-- Status Distribution -->
          <div class="bg-sauti-white rounded-[3.5rem] border-2 border-sauti-neutral p-10 shadow-sm">
            <h3 class="text-2xl font-black text-sauti-darkGreen mb-10">{{
              settingsStore.settings.resources_status_distribution || 'Case Status Distribution' }}</h3>
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
              <div
                class="text-center p-10 bg-sauti-neutral/30 rounded-3xl border-2 border-transparent hover:border-sauti-orange hover:bg-sauti-white transition-all group">
                <div class="text-5xl font-black text-sauti-orange mb-3 transition-transform group-hover:scale-110">{{
                  getStatusCount('PENDING') }}</div>
                <div class="text-[10px] font-black uppercase tracking-widest text-sauti-darkGreen/40">{{
                  settingsStore.settings.resources_pending || 'Pending' }}</div>
              </div>
              <div
                class="text-center p-10 bg-sauti-neutral/30 rounded-3xl border-2 border-transparent hover:border-sauti-blue hover:bg-sauti-white transition-all group">
                <div class="text-5xl font-black text-sauti-blue mb-3 transition-transform group-hover:scale-110">{{
                  getStatusCount('IN_PROGRESS') }}</div>
                <div class="text-[10px] font-black uppercase tracking-widest text-sauti-darkGreen/40">{{
                  settingsStore.settings.resources_in_progress || 'In Progress' }}</div>
              </div>
              <div
                class="text-center p-10 bg-sauti-neutral/30 rounded-3xl border-2 border-transparent hover:border-sauti-lightGreen hover:bg-sauti-white transition-all group">
                <div class="text-5xl font-black text-sauti-lightGreen mb-3 transition-transform group-hover:scale-110">
                  {{ getStatusCount('RESOLVED') }}</div>
                <div class="text-[10px] font-black uppercase tracking-widest text-sauti-darkGreen/40">{{
                  settingsStore.settings.resources_resolved || 'Resolved' }}</div>
              </div>
              <div
                class="text-center p-10 bg-sauti-neutral/30 rounded-3xl border-2 border-transparent hover:border-sauti-darkGreen hover:bg-sauti-white transition-all group">
                <div class="text-5xl font-black text-sauti-darkGreen mb-3 transition-transform group-hover:scale-110">{{
                  getStatusCount('CLOSED') }}</div>
                <div class="text-[10px] font-black uppercase tracking-widest text-sauti-darkGreen/40">{{
                  settingsStore.settings.resources_closed || 'Closed' }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Downloadable Resources Section -->
      <div>
        <div class="flex items-center justify-between mb-10">
          <div>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-2">{{
              settingsStore.settings.resources_downloads_title || 'Downloadable Resources' }}</h2>
            <p class="text-sauti-darkGreen/60 font-bold text-lg">{{ settingsStore.settings.resources_downloads_subtitle
              || 'Public awareness materials and guidance.' }}</p>
          </div>
          <div class="text-[10px] font-black uppercase tracking-widest text-sauti-darkGreen/40">
            <span class="text-sauti-darkGreen">{{ resources.length }}</span> {{
              settingsStore.settings.resources_available || 'items available' }}
          </div>
        </div>

        <!-- Search & Filters -->
        <div class="bg-sauti-white rounded-[2.5rem] border-2 border-sauti-neutral p-6 mb-12 shadow-sm">
          <div class="flex flex-col md:flex-row gap-6">
            <div class="flex-1 relative group">
              <svg
                class="absolute left-6 top-1/2 transform -translate-y-1/2 w-6 h-6 text-sauti-darkGreen/30 group-focus-within:text-sauti-blue transition-colors"
                fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
              <input v-model="search" type="text"
                :placeholder="settingsStore.settings.resources_search_placeholder || 'Search resources...'"
                class="w-full pl-16 pr-6 py-4 bg-sauti-neutral border-2 border-transparent focus:border-sauti-blue focus:bg-sauti-white rounded-2xl font-bold text-sauti-darkGreen outline-none transition-all" />
            </div>
            <div class="flex flex-col md:flex-row gap-4">
              <div class="relative">
                <select v-model="category"
                  class="appearance-none pl-6 pr-12 py-4 bg-sauti-neutral border-2 border-transparent focus:border-sauti-blue focus:bg-sauti-white rounded-2xl font-black text-sauti-darkGreen uppercase tracking-widest text-[10px] outline-none transition-all cursor-pointer min-w-[200px]">
                  <option value="">{{ settingsStore.settings.resources_all_categories || 'All Categories' }}</option>
                  <option v-for="cat in categories" :key="cat.slug || cat.id" :value="cat.slug || cat.id">
                    {{ cat.name }}
                  </option>
                </select>
                <svg
                  class="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-sauti-darkGreen/40 pointer-events-none"
                  fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M19 9l-7 7-7-7" />
                </svg>
              </div>
              <div class="relative">
                <select v-model="language"
                  class="appearance-none pl-6 pr-12 py-4 bg-sauti-neutral border-2 border-transparent focus:border-sauti-blue focus:bg-sauti-white rounded-2xl font-black text-sauti-darkGreen uppercase tracking-widest text-[10px] outline-none transition-all cursor-pointer min-w-[150px]">
                  <option value="">{{ settingsStore.settings.resources_all_languages || 'All Languages' }}</option>
                  <option value="en">English</option>
                  <option value="lg">Luganda</option>
                  <option value="sw">Swahili</option>
                </select>
                <svg
                  class="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-sauti-darkGreen/40 pointer-events-none"
                  fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M19 9l-7 7-7-7" />
                </svg>
              </div>
            </div>
          </div>
        </div>

        <!-- Resources Loading -->
        <AppLoader v-if="loading" :message="settingsStore.settings.resources_loading" />

        <!-- Resources Grid -->
        <div v-else-if="resources.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
          <article v-for="resource in resources" :key="resource.id"
            class="group relative bg-sauti-white rounded-[3.5rem] border-2 border-sauti-neutral transition-all duration-500 hover:shadow-2xl hover:shadow-sauti-blue/10 hover:border-sauti-blue/30 transform hover:-translate-y-2 overflow-hidden">
            <!-- Featured Badge -->
            <div v-if="resource.is_featured" class="absolute top-6 right-6 z-10">
              <div
                class="bg-sauti-orange text-sauti-white text-[10px] font-black uppercase tracking-widest px-4 py-2 rounded-xl shadow-lg shadow-sauti-orange/20 flex items-center gap-2">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                  <path
                    d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                </svg>
                Featured
              </div>
            </div>

            <div class="p-8 md:p-10">
              <!-- Icon and Title -->
              <div class="mb-8">
                <div
                  class="w-20 h-20 rounded-[2rem] bg-sauti-blue/10 flex items-center justify-center mb-8 transition-transform duration-500 group-hover:scale-110 group-hover:rotate-6">
                  <svg v-if="isAudio(resource)" class="w-10 h-10 text-sauti-blue" viewBox="0 0 24 24"
                    fill="currentColor">
                    <path
                      d="M9 19V6l12-2v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-2" />
                  </svg>
                  <svg v-else class="w-10 h-10 text-sauti-blue" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd"
                      d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z"
                      clip-rule="evenodd" />
                  </svg>
                </div>
                <h3
                  class="text-2xl font-black text-sauti-darkGreen mb-4 leading-tight group-hover:text-sauti-blue transition-colors line-clamp-2">
                  {{ resource.title }}
                </h3>
                <p class="text-lg text-sauti-darkGreen/50 font-bold leading-relaxed line-clamp-3">
                  {{ resource.description }}
                </p>
              </div>

              <!-- Tags -->
              <div class="flex flex-wrap gap-3 mb-10">
                <span v-if="resource.category_name"
                  class="inline-flex items-center px-4 py-1.5 rounded-xl text-[10px] font-black uppercase tracking-widest bg-sauti-neutral text-sauti-darkGreen/40">
                  {{ resource.category_name }}
                </span>
                <span v-if="resource.language"
                  class="inline-flex items-center px-4 py-1.5 rounded-xl text-[10px] font-black uppercase tracking-widest bg-sauti-neutral text-sauti-darkGreen/40">
                  {{ getLanguageName(resource.language) }}
                </span>
              </div>

              <!-- Audio Player -->
              <div v-if="isAudio(resource) && resource.file" class="mb-10 p-4 bg-sauti-neutral rounded-2xl">
                <audio :src="resource.file" controls class="w-full"></audio>
              </div>

              <!-- Actions -->
              <div class="flex items-center justify-between pt-8 border-t-2 border-sauti-neutral">
                <a v-if="resource.file" :href="resource.file" target="_blank" rel="noopener"
                  class="inline-flex items-center gap-3 px-8 py-3.5 bg-sauti-blue text-sauti-white text-[10px] font-black uppercase tracking-widest rounded-xl shadow-xl shadow-sauti-blue/20 hover:scale-105 transition-all">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3"
                      d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                  </svg>
                  Download
                </a>
                <span v-else
                  class="px-8 py-3.5 bg-sauti-neutral text-sauti-darkGreen/30 text-[10px] font-black uppercase tracking-widest rounded-xl">
                  {{ settingsStore.settings.resources_coming_soon || 'Coming Soon' }}
                </span>

                <!-- Download Count -->
                <div
                  class="flex items-center gap-2 text-[10px] font-black text-sauti-darkGreen/40 uppercase tracking-widest">
                  <span class="text-sauti-darkGreen">{{ resource.download_count || 0 }}</span>
                  Downloads
                </div>
              </div>
            </div>
          </article>
        </div>

        <!-- Empty State -->
        <div v-else class="text-center py-20">
          <svg class="w-24 h-24 mx-auto text-gray-300 mb-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ settingsStore.settings.resources_no_results }}</h3>
          <p class="text-gray-600">{{ settingsStore.settings.resources_no_results_subtitle }}</p>
        </div>

        <!-- Pagination -->
        <div v-if="pagination.next || pagination.previous" class="mt-20 flex justify-center gap-6">
          <button :disabled="!pagination.previous || loading" @click="prevPage"
            class="px-10 py-4 rounded-2xl border-2 border-sauti-neutral text-sauti-darkGreen hover:border-sauti-blue hover:text-sauti-blue disabled:opacity-30 disabled:cursor-not-allowed font-black uppercase tracking-widest text-xs transition-all">
            {{ settingsStore.settings.resources_previous || 'Previous' }}
          </button>
          <button :disabled="!pagination.next || loading" @click="nextPage"
            class="px-10 py-4 rounded-2xl border-2 border-sauti-neutral text-sauti-darkGreen hover:border-sauti-blue hover:text-sauti-blue disabled:opacity-30 disabled:cursor-not-allowed font-black uppercase tracking-widest text-xs transition-all">
            {{ settingsStore.settings.resources_next || 'Next' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, watch, onMounted, computed } from 'vue'
  import { useResourcesStore } from '@/store/resources'
  import { useSettingsStore } from '@/store/settings'
  import { api } from '@/utils/axios'
  import AppLoader from '@/components/common/AppLoader.vue'
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
        backgroundColor: '#0077A6', // sauti-blue
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
          color: '#002B52'
        }
      },
      tooltip: {
        backgroundColor: '#002B52',
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
        backgroundColor: '#002B52',
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
          color: '#002B5250'
        },
        grid: {
          color: '#002B5208',
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
          color: '#002B5250'
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

<style scoped>
  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    line-clamp: 2;
    overflow: hidden;
  }
</style>
