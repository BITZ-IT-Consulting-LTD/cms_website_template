<!-- ResourcesPage.vue - Updated 2026-03-06 with chart improvements -->
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
              {{ siteContent.getContent('resources_live_data_badge', 'Live Data') }}
            </div>
          </div>

          <!-- Enhanced Quick Stats Cards -->
          <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 mb-16">
            <!-- Total Calls -->
            <div class="relative overflow-hidden rounded-2xl p-4 sm:p-6 shadow-lg hover:shadow-xl transition-all duration-300 group bg-gradient-to-br from-primary to-primary/80">
              <div class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
              <div class="relative z-10">
                <div class="text-2xl sm:text-3xl md:text-4xl font-black text-white mb-1">
                   {{ formatNumber(dashboardStats.total_calls) }}
                </div>
                <p class="text-white/80 text-xs font-bold tracking-wider uppercase">
                  {{ siteContent.getContent('stats_kpi_calls', 'Total Calls') }}
                </p>
              </div>
            </div>

            <!-- Total Cases -->
            <div class="relative overflow-hidden rounded-2xl p-4 sm:p-6 shadow-lg hover:shadow-xl transition-all duration-300 group bg-gradient-to-br from-secondary to-secondary/80">
              <div class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
              <div class="relative z-10">
                <div class="text-2xl sm:text-3xl md:text-4xl font-black text-white mb-1">
                   {{ formatNumber(dashboardStats.total_cases) }}
                </div>
                <p class="text-white/80 text-xs font-bold tracking-wider uppercase">
                  {{ siteContent.getContent('stats_kpi_cases', 'Total Cases') }}
                </p>
              </div>
            </div>

            <!-- Total GBV Cases -->
            <div class="relative overflow-hidden rounded-2xl p-4 sm:p-6 shadow-lg hover:shadow-xl transition-all duration-300 group bg-gradient-to-br from-hotline to-hotline/80">
              <div class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
              <div class="relative z-10">
                <div class="text-2xl sm:text-3xl md:text-4xl font-black text-white mb-1">
                   {{ formatNumber(dashboardStats.total_gbv_cases) }}
                </div>
                <p class="text-white/80 text-xs font-bold tracking-wider uppercase">
                  {{ siteContent.getContent('stats_kpi_gbv', 'Total GBV Cases') }}
                </p>
              </div>
            </div>

            <!-- Total SEA Cases -->
            <div class="relative overflow-hidden rounded-2xl p-4 sm:p-6 shadow-lg hover:shadow-xl transition-all duration-300 group bg-gradient-to-br from-emergency to-emergency/80">
              <div class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
              <div class="relative z-10">
                <div class="text-2xl sm:text-3xl md:text-4xl font-black text-white mb-1">
                   {{ formatNumber(dashboardStats.total_sea_cases) }}
                </div>
                <p class="text-white/80 text-xs font-bold tracking-wider uppercase">
                  {{ siteContent.getContent('stats_kpi_sea', 'Total SEA Cases') }}
                </p>
              </div>
            </div>

            <!-- Total Migrant Workers -->
            <div class="relative overflow-hidden rounded-2xl p-4 sm:p-6 shadow-lg hover:shadow-xl transition-all duration-300 group bg-gradient-to-br from-secondary-light to-secondary-light/80">
              <div class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
              <div class="relative z-10">
                <div class="text-2xl sm:text-3xl md:text-4xl font-black text-white mb-1">
                   {{ formatNumber(dashboardStats.total_migrant_workers) }}
                </div>
                <p class="text-white/80 text-xs font-bold tracking-wider uppercase">
                  {{ siteContent.getContent('stats_kpi_migrant', 'Migrant Workers') }}
                </p>
              </div>
            </div>
          </div>

          <!-- Filter Bar -->
          <div class="bg-neutral-offwhite rounded-2xl p-4 mb-8">
            <div class="flex flex-wrap items-center gap-4">
              <!-- Period Filter -->
              <div class="flex items-center gap-2">
                <label class="text-xs font-bold text-secondary/60 uppercase tracking-wider whitespace-nowrap">
                  {{ siteContent.getContent('resources_filter_time_period', 'Time Period') }}
                </label>
                <div class="flex bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
                  <button
                    v-for="option in periodOptions"
                    :key="option.value"
                    @click="selectedPeriod = option.value; fetchDashboardData(true)"
                    :class="[
                      'px-4 py-2 text-xs font-bold transition-all',
                      selectedPeriod === option.value
                        ? 'bg-primary text-white'
                        : 'text-secondary/70 hover:bg-gray-50'
                    ]"
                  >
                    {{ option.label }}
                  </button>
                </div>
              </div>

              <!-- Case Type Filter (only for All Time view) -->
              <div v-if="selectedPeriod === 'all'" class="flex items-center gap-2">
                <label for="caseTypeFilter" class="text-xs font-bold text-secondary/60 uppercase tracking-wider whitespace-nowrap">
                  {{ siteContent.getContent('resources_filter_case_type', 'Case Type') }}
                </label>
                <select
                  id="caseTypeFilter"
                  v-model="caseTypeFilter"
                  class="rounded-xl border border-gray-100 bg-white px-4 py-2 text-xs font-bold text-secondary shadow-sm focus:border-primary focus:ring-1 focus:ring-primary outline-none"
                >
                  <option value="All">All Types</option>
                  <option value="Abuse">Abuse</option>
                  <option value="Counseling">Counseling</option>
                  <option value="Information Inquiry">Information</option>
                </select>
              </div>

              <!-- Loading indicator -->
              <div v-if="chartsLoading" class="flex items-center gap-2 text-primary">
                <svg class="animate-spin h-4 w-4" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <span class="text-xs font-semibold">{{ siteContent.getContent('resources_loading_charts', 'Loading...') }}</span>
              </div>
            </div>
          </div>

          <!-- Enhanced Charts Grid (2x2) -->
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <!-- Chart 1: Cases by Gender -->
            <div class="chart-card group">
              <div class="chart-card-bg bg-primary/5"></div>
              <div class="relative z-10">
                <div class="chart-header">
                  <div class="chart-indicator bg-primary"></div>
                  <h3 class="chart-title">{{ siteContent.getContent('resources_chart_gender_title', 'Cases by Gender') }}</h3>
                </div>
                <p class="chart-subtitle">{{ siteContent.getContent('resources_chart_gender_subtitle', 'Distribution of case types across genders') }}</p>
                <div class="h-[350px]">
                  <Bar :data="filteredCategoryBySex" :options="getChartOptions('Gender')" />
                </div>
              </div>
            </div>

            <!-- Chart 2: Cases by Region -->
            <div class="chart-card group">
              <div class="chart-card-bg bg-secondary/5"></div>
              <div class="relative z-10">
                <div class="chart-header">
                  <div class="chart-indicator bg-secondary"></div>
                  <h3 class="chart-title">{{ siteContent.getContent('resources_chart_region_title', 'Cases by Region') }}</h3>
                </div>
                <p class="chart-subtitle">{{ siteContent.getContent('resources_chart_region_subtitle', 'Geographic distribution of reported cases') }}</p>
                <div class="h-[350px]">
                  <Bar :data="filteredCategoryByRegion" :options="getChartOptions('Region')" />
                </div>
              </div>
            </div>

            <!-- Chart 3: Cases by Age Group -->
            <div class="chart-card group">
              <div class="chart-card-bg bg-hotline/5"></div>
              <div class="relative z-10">
                <div class="chart-header">
                  <div class="chart-indicator bg-hotline"></div>
                  <h3 class="chart-title">{{ siteContent.getContent('resources_chart_age_title', 'Cases by Age Group') }}</h3>
                </div>
                <p class="chart-subtitle">{{ siteContent.getContent('resources_chart_age_subtitle', 'Age demographics of reported cases') }}</p>
                <div class="h-[350px]">
                  <Bar :data="filteredCategoryByAgeGroup" :options="getChartOptions('Age Group')" />
                </div>
              </div>
            </div>

            <!-- Chart 4: Top Districts -->
            <div class="chart-card group">
              <div class="chart-card-bg bg-emergency/5"></div>
              <div class="relative z-10">
                <div class="chart-header">
                  <div class="chart-indicator bg-emergency"></div>
                  <h3 class="chart-title">{{ siteContent.getContent('resources_chart_district_title', 'Top Districts') }}</h3>
                </div>
                <p class="chart-subtitle">{{ siteContent.getContent('resources_chart_district_subtitle', 'Districts with highest case volumes') }}</p>
                <div class="h-[350px]">
                  <Bar :data="filteredCategoryByDistrict" :options="getChartOptions('District')" />
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
            <span class="text-xs font-black tracking-widest text-secondary/60 uppercase">{{ siteContent.getContent('resources_downloads_divider', 'Downloads') }}</span>
          </div>
          <div class="flex-1 h-px bg-gray-200"></div>
        </div>

        <!-- ============================================ -->
        <!-- DOWNLOADABLE RESOURCES SECTION               -->
        <!-- ============================================ -->
        <section aria-labelledby="downloads-heading">
          <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
            <div>
              <h2 id="downloads-heading" class="campaign-header text-2xl lg:text-3xl text-secondary mb-4">
                {{ siteContent.getContent('resources_downloads_title', 'Downloadable Resources') }}
              </h2>
              <p class="text-black/60 font-bold text-lg">
                {{ siteContent.getContent('resources_downloads_subtitle', 'Public awareness materials and official guidance.') }}
              </p>
            </div>
            <div class="pill bg-primary/10 text-primary flex items-center gap-2">
              <svg v-if="loading && filteredResources.length" class="animate-spin h-3 w-3" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              {{ filteredResources.length }} {{ siteContent.getContent('resources_available', 'resources available') }}
            </div>
          </div>

          <!-- Search & Filters -->
          <div class="bg-neutral-offwhite rounded-[2.5rem] p-8 mb-16 shadow-none">
            <div class="flex flex-col gap-4">
              <!-- Search Bar -->
              <div class="flex-1 relative group">
                <Search
                  class="absolute left-6 top-1/2 transform -translate-y-1/2 w-6 h-6 text-primary group-focus-within:text-secondary transition-colors" />
                <input v-model="search" type="text" :placeholder="siteContent.getContent('resources_search_placeholder', 'Search resources by title or description...')"
                  class="w-full pl-16 pr-6 py-4 bg-white shadow-sm border-none focus:ring-0 focus:shadow-md rounded-2xl font-bold text-secondary outline-none transition-all" />
              </div>

              <!-- Filter Dropdowns -->
              <div class="flex flex-col md:flex-row gap-4">
                <!-- Category Filter -->
                <div class="relative flex-1">
                  <select v-model="category"
                    class="w-full appearance-none pl-6 pr-12 py-4 bg-white shadow-sm border-none focus:ring-0 focus:shadow-md rounded-2xl font-bold text-secondary tracking-widest text-[10px] outline-none transition-all cursor-pointer">
                    <option value="">{{ siteContent.getContent('resources_all_categories', 'All Categories') }}</option>
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
                    <option value="">{{ siteContent.getContent('resources_all_formats', 'All Formats') }}</option>
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
                    <option value="">{{ siteContent.getContent('resources_all_languages', 'All Languages') }}</option>
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

          <!-- Resources Loading - Only show full loader on initial load with no data -->
          <AppLoader v-if="loading && !filteredResources.length" :message="siteContent.getContent('resources_loading', 'Loading resources...')" />

          <!-- Enhanced Resources Grid (No Images - CMS Driven) -->
          <div v-else-if="filteredResources.length" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8" :class="{ 'opacity-60': loading }">
            <article v-for="resource in filteredResources" :key="resource.id" :id="`resource-${resource.slug}`"
              class="group bg-white rounded-3xl shadow-lg border border-gray-100 transition-all duration-500 hover:shadow-2xl hover:border-primary/30 transform hover:-translate-y-2 overflow-hidden flex flex-col"
              :class="{ 'ring-4 ring-primary/40': route.query.resource === resource.slug }">

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
                    {{ expandedDescriptions[resource.id] ? siteContent.getContent('resources_show_less', '− Show less') : siteContent.getContent('resources_read_more', '+ Read more') }}
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
                    {{ downloadingSlug === resource.slug ? siteContent.getContent('resources_downloading', 'Downloading...') : siteContent.getContent('resources_download', 'Download') }}
                  </button>
                  <span v-if="resource.download_count" class="text-sm text-black/40 font-semibold">
                    {{ resource.download_count }} {{ siteContent.getContent('resources_downloads_count', 'downloads') }}
                  </span>
                </div>

                <!-- Share Row: same platform set as the article share row, sharing
                     a stable per-resource URL (?resource=<slug>) rather than a
                     Download-only affordance. -->
                <div class="flex items-center flex-wrap gap-1.5 pt-4 mt-4 border-t border-gray-100">
                  <span class="text-[9px] font-black uppercase tracking-widest text-black/30 mr-1">
                    {{ siteContent.getContent('resources_share_label', 'Share') }}
                  </span>
                  <button v-for="social in socialShareButtons" :key="social.name" type="button"
                    @click="social.action(resource)"
                    class="w-7 h-7 rounded-lg bg-neutral-offwhite flex items-center justify-center hover:scale-110 hover:bg-primary/10 transition-all"
                    :aria-label="`Share ${resource.title} on ${social.label}`">
                    <BrandIcon :name="social.name" class="w-3.5 h-3.5" />
                  </button>
                  <button type="button" @click="copyResourceLink(resource)"
                    class="w-7 h-7 rounded-lg bg-neutral-offwhite flex items-center justify-center hover:scale-110 hover:bg-primary/10 transition-all"
                    :aria-label="`Copy link to ${resource.title}`">
                    <Check v-if="copiedSlug === resource.slug" class="w-3.5 h-3.5 text-primary" />
                    <Link2 v-else class="w-3.5 h-3.5 text-black/50" />
                  </button>
                </div>
                <p v-if="shareToastSlug === resource.slug" role="status"
                  class="text-[11px] font-bold text-primary mt-2">
                  {{ shareToastMessage }}
                </p>
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
            <h3 class="text-2xl font-bold text-secondary mb-2">{{ siteContent.getContent('resources_no_results', 'No Resources Found') }}</h3>
            <p class="text-black/50 font-bold mb-8">{{ siteContent.getContent('resources_no_results_subtitle', 'Try adjusting your search criteria.') }}</p>
            <button @click="search = ''; category = ''; language = ''; format = ''" class="btn btn-outline">{{ siteContent.getContent('resources_clear_filters', 'Clear all filters') }}</button>
          </div>

          <!-- Pagination -->
          <div v-if="pagination.next || pagination.previous" class="mt-20 flex justify-center gap-6">
            <button :disabled="!pagination.previous || loading" @click="prevPage"
              class="btn btn-outline px-8">{{ siteContent.getContent('resources_previous', 'Previous') }}</button>
            <button :disabled="!pagination.next || loading" @click="nextPage" class="btn btn-outline px-8">{{ siteContent.getContent('resources_next', 'Next') }}</button>
          </div>
        </section>

      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, watch, onMounted, onUnmounted, computed, nextTick } from 'vue'
  import { useRoute } from 'vue-router'
  import { useResourcesStore } from '@/store/resources'
  import { useSettingsStore } from '@/store/settings'
  import { useSiteContent } from '@/composables/useSiteContent'
  import { api } from '@/utils/axios'
  import AppLoader from '@/components/common/AppLoader.vue'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import BrandIcon from '@/components/common/BrandIcon.vue'
  import {
    Search,
    ChevronDown,
    FileText,
    BarChart,
    Link2,
    Check
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
  const route = useRoute()
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

  // --- Share row -----------------------------------------------------------
  // Resources have no dedicated detail route, so the "stable per-resource URL"
  // is this same listing page with a `?resource=<slug>` query param (query
  // params — unlike hash fragments — are visible to the server/crawlers and
  // to this page's own onMounted/watch below, which scrolls to + highlights
  // the named card). Built from the canonical public base URL so a link
  // shared from a dev host/IP still resolves for the recipient.
  function getPublicOrigin() {
    const configuredBase = (import.meta.env.VITE_PUBLIC_BASE_URL || '').replace(/\/+$/, '')
    return configuredBase || (window.location.origin + (import.meta.env.BASE_URL || '/').replace(/\/+$/, ''))
  }

  function resourceShareUrl(resource) {
    return `${getPublicOrigin()}/resources?resource=${encodeURIComponent(resource.slug)}`
  }

  const copiedSlug = ref(null)
  const shareToastSlug = ref(null)
  const shareToastMessage = ref('')

  async function copyResourceLink(resource, message = 'Link copied') {
    const url = resourceShareUrl(resource)
    try {
      if (navigator.clipboard?.writeText) {
        await navigator.clipboard.writeText(url)
      } else {
        window.prompt('Copy this link:', url)
      }
    } catch (err) {
      window.prompt('Copy this link:', url)
    }
    copiedSlug.value = resource.slug
    shareToastSlug.value = resource.slug
    shareToastMessage.value = message
    setTimeout(() => {
      copiedSlug.value = null
      shareToastSlug.value = null
    }, 2500)
  }

  function shareResourceOnFacebook(resource) {
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(resourceShareUrl(resource))}`, '_blank', 'width=600,height=400')
  }

  function shareResourceOnTwitter(resource) {
    window.open(`https://twitter.com/intent/tweet?url=${encodeURIComponent(resourceShareUrl(resource))}&text=${encodeURIComponent(resource.title || '')}`, '_blank', 'width=600,height=400')
  }

  function shareResourceOnWhatsApp(resource) {
    window.open(`https://wa.me/?text=${encodeURIComponent((resource.title ? resource.title + ' - ' : '') + resourceShareUrl(resource))}`, '_blank')
  }

  function shareResourceOnLinkedIn(resource) {
    window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(resourceShareUrl(resource))}`, '_blank', 'width=600,height=500')
  }

  function shareResourceOnTelegram(resource) {
    window.open(`https://t.me/share/url?url=${encodeURIComponent(resourceShareUrl(resource))}&text=${encodeURIComponent(resource.title || '')}`, '_blank')
  }

  function shareResourceByEmail(resource) {
    window.location.href = `mailto:?subject=${encodeURIComponent(resource.title || 'Sauti 116 resource')}&body=${encodeURIComponent(resourceShareUrl(resource))}`
  }

  // Instagram and TikTok have no web share-intent URL. Prefer the native
  // share sheet (surfaces the visitor's installed apps, Instagram/TikTok
  // included); fall back to copy-link with an explicit toast so the button
  // never silently does nothing.
  async function shareResourceViaNativeOrCopy(resource, platformLabel) {
    const url = resourceShareUrl(resource)
    if (navigator.share) {
      try {
        await navigator.share({ title: resource.title || 'Sauti 116 resource', url })
        return
      } catch (err) {
        if (err?.name === 'AbortError') return
      }
    }
    await copyResourceLink(resource, `Link copied — paste it in ${platformLabel}`)
  }

  const shareResourceOnInstagram = (resource) => shareResourceViaNativeOrCopy(resource, 'Instagram')
  const shareResourceOnTikTok = (resource) => shareResourceViaNativeOrCopy(resource, 'TikTok')

  const socialShareButtons = [
    { name: 'facebook', label: 'Facebook', action: shareResourceOnFacebook },
    { name: 'x', label: 'X', action: shareResourceOnTwitter },
    { name: 'whatsapp', label: 'WhatsApp', action: shareResourceOnWhatsApp },
    { name: 'linkedin', label: 'LinkedIn', action: shareResourceOnLinkedIn },
    { name: 'telegram', label: 'Telegram', action: shareResourceOnTelegram },
    { name: 'instagram', label: 'Instagram', action: shareResourceOnInstagram },
    { name: 'tiktok', label: 'TikTok', action: shareResourceOnTikTok },
    { name: 'email', label: 'Email', action: shareResourceByEmail },
  ]

  // Scroll to + highlight the resource named by ?resource=<slug> (from a
  // shared card link) once the list has loaded.
  watch(filteredResources, async (list) => {
    if (!route.query.resource || !list.length) return
    await nextTick()
    const el = document.getElementById(`resource-${route.query.resource}`)
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' })
  }, { once: true })

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
  // --- Dashboard Statistics Logic with Caching ---
  const DASHBOARD_CACHE_KEY = 'sauti-dashboard-cache'
  const DASHBOARD_TTL = 10 * 60 * 1000 // 10 minutes

  // Load cached data immediately on initialization
  const loadCachedDashboard = () => {
    try {
      const cached = localStorage.getItem(DASHBOARD_CACHE_KEY)
      if (cached) {
        const { stats, charts, timestamp } = JSON.parse(cached)
        if (stats && charts) {
          return { stats, charts, isFresh: Date.now() - timestamp < DASHBOARD_TTL }
        }
      }
    } catch (e) {
      console.warn('Failed to load dashboard cache:', e)
    }
    return null
  }

  const saveDashboardCache = (stats, charts) => {
    try {
      localStorage.setItem(DASHBOARD_CACHE_KEY, JSON.stringify({
        stats,
        charts,
        timestamp: Date.now()
      }))
    } catch (e) {
      console.warn('Failed to save dashboard cache:', e)
    }
  }

  // Initialize with cached data if available
  const cachedData = loadCachedDashboard()

  const dashboardStats = ref(cachedData?.stats || {
    total_calls: 0,
    total_cases: 0,
    total_gbv_cases: 0,
    total_sea_cases: 0,
    total_migrant_workers: 0
  })

  const dashboardCharts = ref(cachedData?.charts || {
    categoryBySex: { labels: [], datasets: [] },
    categoryByRegion: { labels: [], datasets: [] },
    categoryByAgeGroup: { labels: [], datasets: [] },
    categoryByDistrict: { labels: [], datasets: [] }
  })

  const caseTypeFilter = ref('All')
  const chartsLoading = ref(!cachedData) // Only show loading if no cache
  const dashboardInitialized = ref(!!cachedData)

  // Time period filter for dashboard charts
  const selectedPeriod = ref('year')
  const periodOptions = [
    { value: 'year', label: 'This Year' },
    // { value: 'all', label: 'All Time' },
    // { value: 'month', label: 'This Month' },
    // { value: 'week', label: 'This Week' }
  ]

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

  // API Fetch Logic for Dashboard - Now with caching
  const fetchDashboardData = async (forceRefresh = false) => {
    // If we have fresh cached data and not forcing refresh, skip API call
    const cached = loadCachedDashboard()
    if (!forceRefresh && cached?.isFresh && dashboardInitialized.value) {
      console.log('[Dashboard] Using fresh cache, skipping API call')
      return
    }

    // Only show loading spinner if we don't have any data yet
    if (!dashboardInitialized.value) {
      chartsLoading.value = true
    }

    try {
      // Fetch real statistics from the external Sauti helpline system
      const statsResponse = await api.get('/dashboard/helpline-stats/')

      const newStats = statsResponse.data ? {
        total_calls: statsResponse.data.total_calls || 0,
        total_cases: statsResponse.data.total_cases || 0,
        total_gbv_cases: statsResponse.data.total_gbv_cases || 0,
        total_sea_cases: statsResponse.data.total_sea_cases || 0,
        total_migrant_workers: statsResponse.data.total_migrant_workers || 0
      } : dashboardStats.value

      dashboardStats.value = newStats

      const mapChartData = (apiData) => {
          if (!apiData) return { labels: [], datasets: [] }
          return {
              labels: apiData.labels || [],
              datasets: (apiData.datasets || []).map((ds, index) => ({
                  label: ds.label,
                  data: ds.data,
                  backgroundColor: getBrandColor(index),
                  borderRadius: 6,
                  borderSkipped: false
              }))
          }
      }

      // Fetch chart data from the helpline system with period filter
      const chartsResponse = await api.get(`/dashboard/helpline-charts/?period=${selectedPeriod.value}`)
      if (chartsResponse.data) {
        const newCharts = {
          categoryBySex: mapChartData(chartsResponse.data.categoryBySex),
          categoryByRegion: mapChartData(chartsResponse.data.categoryByRegion),
          categoryByAgeGroup: mapChartData(chartsResponse.data.categoryByAgeGroup),
          categoryByDistrict: mapChartData(chartsResponse.data.categoryByDistrict)
        }
        dashboardCharts.value = newCharts

        // Save to cache
        saveDashboardCache(newStats, newCharts)
      }

      dashboardInitialized.value = true
    } catch (err) {
      console.warn('Statistics dashboard data unavailable:', err)
    } finally {
      chartsLoading.value = false
    }
  }

  // Load dashboard data on mount - fetch in background if cache exists
  onMounted(() => {
    if (cachedData?.isFresh) {
      // Have fresh cache - fetch in background without loading state
      console.log('[Dashboard] Using cached data, refreshing in background')
      fetchDashboardData()
    } else {
      // No cache or stale - fetch with loading state
      fetchDashboardData()
    }
  })

  // Improved Chart Options with cleaner design
  const getChartOptions = (xAxisLabel = '') => {
    return {
      responsive: true,
      maintainAspectRatio: false,
      interaction: {
        mode: 'index',
        intersect: false,
      },
      plugins: {
        legend: {
          display: true,
          position: 'bottom',
          labels: {
            usePointStyle: true,
            pointStyle: 'circle',
            boxWidth: 8,
            padding: 16,
            font: { family: 'cronos-pro', weight: '600', size: 10 },
            color: '#023047'
          }
        },
        tooltip: {
          backgroundColor: 'rgba(2, 48, 71, 0.95)',
          titleFont: { family: 'cronos-pro', size: 13, weight: '700' },
          bodyFont: { family: 'cronos-pro', size: 11 },
          padding: 12,
          cornerRadius: 8,
          displayColors: true,
          boxPadding: 4,
          callbacks: {
            label: (context) => {
              const value = context.parsed.y || context.parsed.x || 0
              return ` ${context.dataset.label}: ${value.toLocaleString()}`
            }
          }
        }
      },
      scales: {
        x: {
          stacked: true,
          grid: { display: false },
          border: { display: false },
          ticks: {
            font: { family: 'cronos-pro', weight: '700', size: 10 },
            color: '#023047',
            maxRotation: 45,
            minRotation: 0
          },
          title: {
            display: !!xAxisLabel,
            text: xAxisLabel,
            font: { family: 'cronos-pro', weight: '700', size: 11 },
            color: '#023047',
            padding: { top: 8 }
          }
        },
        y: {
          stacked: true,
          beginAtZero: true,
          grid: {
            color: 'rgba(0, 0, 0, 0.04)',
            drawBorder: false
          },
          border: { display: false },
          ticks: {
            font: { family: 'cronos-pro', weight: '600', size: 10 },
            color: 'rgba(2, 48, 71, 0.6)',
            padding: 8,
            callback: (value) => {
              if (value >= 1000) {
                return (value / 1000).toFixed(0) + 'k'
              }
              return value
            }
          },
          title: {
            display: true,
            text: 'Number of Cases',
            font: { family: 'cronos-pro', weight: '700', size: 11 },
            color: '#023047',
            padding: { bottom: 8 }
          }
        }
      }
    }
  }

  // Keep old function for backward compatibility
  const getDashboardOptions = (horizontal) => getChartOptions('')

</script>

<style scoped>
/* Hero Banner */
/* Hero banner styles are global now — see .hero-banner et al. in main.css */

/* Chart Card Styles */
.chart-card {
  position: relative;
  background: white;
  border-radius: 1.5rem;
  padding: 1.5rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
  border: 1px solid rgba(0, 0, 0, 0.04);
  transition: all 0.3s ease;
  overflow: hidden;
}

.chart-card:hover {
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
  transform: translateY(-2px);
}

.chart-card-bg {
  position: absolute;
  top: 0;
  right: 0;
  width: 16rem;
  height: 16rem;
  border-radius: 50%;
  transform: translate(50%, -50%);
  transition: transform 0.7s ease;
}

.chart-card:hover .chart-card-bg {
  transform: translate(50%, -50%) scale(1.1);
}

.chart-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.25rem;
}

.chart-indicator {
  width: 0.625rem;
  height: 0.625rem;
  border-radius: 50%;
  flex-shrink: 0;
}

.chart-title {
  font-size: 1.125rem;
  font-weight: 900;
  color: rgb(var(--color-secondary));
  letter-spacing: -0.01em;
}

.chart-subtitle {
  font-size: 0.75rem;
  color: rgba(0, 0, 0, 0.5);
  font-weight: 500;
  margin-bottom: 1rem;
  padding-left: 1.375rem;
}

@media (max-width: 640px) {
  .chart-card {
    padding: 1rem;
  }

  .chart-title {
    font-size: 1rem;
  }
}
</style>
