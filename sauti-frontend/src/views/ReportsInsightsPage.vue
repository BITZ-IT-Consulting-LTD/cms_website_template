<template>
  <div class="bg-sauti-white min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <h1 class="page-header-title">
          Reports <span class="text-sauti-blue">&</span> Insights
        </h1>
        <p class="page-header-subtitle">
          {{ reportsInsightsSubtitle || 'Explore the data collected by Sauti Uganda 116 helpline to understand the trends and patterns in child abuse and neglect across the country.' }}
        </p>
      </div>
    </header>

    <div class="container-custom section-padding section-rhythm">
      <!-- 2. Filters Wrapper -->
      <section aria-labelledby="filters-heading">
        <div class="bg-sauti-white rounded-[3rem] border-2 border-sauti-blue p-8 md:p-12 shadow-sm max-w-6xl mx-auto">
          <h2 id="filters-heading" class="campaign-header text-sm text-sauti-darkGreen mb-10 opacity-50">Filter
            Statistical Data</h2>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-end">
            <div>
              <label class="form-label">{{ reportsInsightsSearchLabel }}</label>
              <div class="relative group">
                <input v-model="search" class="form-input !pl-14" :placeholder="reportsInsightsSearchPlaceholder" />
                <MagnifyingGlassIcon
                  class="w-6 h-6 text-sauti-blue absolute left-5 top-1/2 -translate-y-1/2 group-focus-within:text-sauti-darkGreen transition-colors" />
              </div>
            </div>

            <div>
              <label class="form-label">{{ reportsInsightsRegionLabel }}</label>
              <div class="relative">
                <select v-model="region"
                  class="w-full appearance-none bg-sauti-white border-2 border-sauti-blue focus:border-sauti-darkGreen py-4 px-6 rounded-2xl outline-none transition-all font-bold text-sauti-darkGreen uppercase tracking-widest text-xs cursor-pointer">
                  <option value="all">{{ reportsInsightsAllRegions }}</option>
                  <option>Central</option>
                  <option>Eastern</option>
                  <option>Northern</option>
                  <option>Western</option>
                </select>
                <ChevronDownIcon
                  class="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-sauti-blue pointer-events-none" />
              </div>
            </div>

            <div class="flex md:justify-end">
              <button class="btn btn-info w-full md:w-auto px-12 py-4">
                {{ reportsInsightsApplyFilters }}
              </button>
            </div>
          </div>

          <!-- Date range placeholder -->
          <div
            class="mt-12 p-8 bg-sauti-neutral/30 rounded-[2.5rem] border-2 border-dashed border-sauti-blue flex flex-col items-center justify-center text-sauti-darkGreen/50 text-xs font-bold uppercase tracking-[0.2em] gap-3">
            <CalendarDaysIcon class="w-6 h-6 text-sauti-blue" />
            {{ reportsInsightsDateRangePlaceholder }}
          </div>
        </div>
      </section>

      <!-- 3. Cards Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-10">
        <!-- Cases Per Category -->
        <div class="card-base group">
          <h3 class="campaign-header text-2xl text-sauti-darkGreen mb-10 flex items-center gap-4">
            <div class="w-2 h-8 bg-sauti-lightGreen rounded-full"></div>
            {{ reportsInsightsCasesPerCategory }}
          </h3>
          <div class="h-[350px]">
            <PieChart :labels="categoryLabels" :values="categoryValues" />
          </div>
          <div class="mt-12 p-8 bg-sauti-neutral/30 rounded-3xl border-2 border-sauti-neutral">
            <p class="campaign-header text-[10px] text-sauti-darkGreen/40 mb-6 font-bold uppercase tracking-widest">{{
              reportsInsightsKeyInsights }}</p>
            <ul class="space-y-4 font-bold text-lg text-sauti-darkGreen">
              <li class="flex items-center gap-4">
                <div class="w-3 h-3 rounded-full bg-sauti-lightGreen"></div> {{ reportsInsightsChildNeglectStat }}
              </li>
              <li class="flex items-center gap-4">
                <div class="w-3 h-3 rounded-full bg-sauti-blue"></div> {{ reportsInsightsPhysicalViolenceStat }}
              </li>
              <li class="flex items-center gap-4">
                <div class="w-3 h-3 rounded-full bg-sauti-orange"></div> {{ reportsInsightsSexualViolenceStat }}
              </li>
              <li class="flex items-center gap-4">
                <div class="w-3 h-3 rounded-full bg-sauti-darkGreen"></div> {{ reportsInsightsEconomicViolenceStat }}
              </li>
            </ul>
          </div>
        </div>

        <!-- Summary -->
        <div class="card-base bg-sauti-blue/5 border-sauti-blue/20 flex flex-col justify-center">
          <h3 class="campaign-header text-2xl text-sauti-darkGreen mb-10 flex items-center gap-4">
            <div class="w-2 h-8 bg-sauti-blue rounded-full"></div>
            {{ reportsInsightsSummaryTitle }}
          </h3>
          <div class="space-y-8 text-sauti-darkGreen/70 leading-relaxed font-bold text-lg">
            <p>{{ reportsInsightsSummaryParagraph1 }}</p>
            <p>{{ reportsInsightsSummaryParagraph2 }}</p>
            <p>{{ reportsInsightsSummaryParagraph3 }}</p>
          </div>
        </div>

        <!-- Cases Per Region Over Time -->
        <div class="card-base group">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-10">
            <h3 class="campaign-header text-2xl text-sauti-darkGreen flex items-center gap-4">
              <div class="w-2 h-8 bg-sauti-orange rounded-full"></div>
              {{ reportsInsightsCasesPerRegion }}
            </h3>
            <div class="pill bg-sauti-blue/10 text-sauti-blue text-[10px]">
              {{ reportsInsightsDateRange }}
            </div>
          </div>
          <div class="h-[400px]">
            <RegionChart :labels="timelineLabels" :regionData="regionTimeSeriesData" />
          </div>
        </div>

        <!-- Summary -->
        <div class="card-base bg-sauti-lightGreen/5 border-sauti-lightGreen/20 flex flex-col justify-center">
          <h3 class="campaign-header text-2xl text-sauti-darkGreen mb-10 flex items-center gap-4">
            <div class="w-2 h-8 bg-sauti-lightGreen rounded-full"></div>
            {{ reportsInsightsRegionalTrends }}
          </h3>
          <div class="space-y-8 text-sauti-darkGreen/70 leading-relaxed font-bold text-lg">
            <p>{{ reportsInsightsRegionalTrendsParagraph1 }}</p>
            <p>{{ reportsInsightsRegionalTrendsParagraph2 }}</p>
            <p>{{ reportsInsightsRegionalTrendsParagraph3 }}</p>
          </div>
        </div>

        <!-- Age Group Distribution -->
        <div class="card-base lg:col-span-2 group">
          <h3 class="campaign-header text-2xl text-sauti-darkGreen mb-10 flex items-center gap-4">
            <div class="w-2 h-8 bg-sauti-blue rounded-full"></div>
            {{ reportsInsightsCaseCategoriesPerAgeGroup }}
          </h3>
          <div class="h-[500px]">
            <AgeGroupChart :labels="ageGroupLabels" :ageData="ageGroupData" />
          </div>
        </div>

        <!-- Gender Breakdown -->
        <div class="card-base lg:col-span-2 group border-sauti-orange/30">
          <h3 class="campaign-header text-2xl text-sauti-darkGreen mb-10 flex items-center gap-4">
            <div class="w-2 h-8 bg-sauti-orange rounded-full"></div>
            {{ reportsInsightsCaseCategoriesPerGender }}
          </h3>
          <div class="h-[500px]">
            <GenderChart :labels="ageGroupLabels" :genderData="genderData" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue'
  import { Bar, Pie } from 'vue-chartjs'
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
  import { useSettingsStore } from '@/store/settings'
  import {
    MagnifyingGlassIcon,
    ChevronDownIcon,
    CalendarDaysIcon
  } from '@heroicons/vue/24/outline'

  ChartJS.register(Title, Tooltip, Legend, BarElement, LineElement, CategoryScale, LinearScale, PointElement, ArcElement)

  defineOptions({
    name: 'ReportsInsightsPage'
  })

  const search = ref('')
  const region = ref('all')
  const settingsStore = useSettingsStore()

  onMounted(() => {
    settingsStore.fetchGlobalSettings()
  })

  // Computed properties for content
  const reportsInsightsSubtitle = computed(() => settingsStore.settings.reports_insights_subtitle || 'Explore the data collected by Sauti Uganda 116 helpline to understand the trends and patterns in child abuse and neglect across the country.')
  const reportsInsightsSearchLabel = computed(() => settingsStore.settings.reports_insights_search_label || 'Search Database')
  const reportsInsightsSearchPlaceholder = computed(() => settingsStore.settings.reports_insights_search_placeholder || 'Keywords e.g. "neglect", "central"')
  const reportsInsightsRegionLabel = computed(() => settingsStore.settings.reports_insights_region_label || 'Region Selection')
  const reportsInsightsAllRegions = computed(() => settingsStore.settings.reports_insights_all_regions || 'All Administrative Regions')
  const reportsInsightsApplyFilters = computed(() => settingsStore.settings.reports_insights_apply_filters || 'Generate Report')
  const reportsInsightsDateRangePlaceholder = computed(() => settingsStore.settings.reports_insights_date_range_placeholder || 'Period: 01 Jan 2025 - 31 Dec 2025')
  const reportsInsightsCasesPerCategory = computed(() => settingsStore.settings.reports_insights_cases_per_category || 'Cases Per Category')
  const reportsInsightsKeyInsights = computed(() => settingsStore.settings.reports_insights_key_insights || 'Primary Statistics')
  const reportsInsightsChildNeglectStat = computed(() => settingsStore.settings.reports_insights_child_neglect_stat || 'Child Neglect: 48.1% (2,746 cases)')
  const reportsInsightsPhysicalViolenceStat = computed(() => settingsStore.settings.reports_insights_physical_violence_stat || 'Physical Violence: 17.0% (817 cases)')
  const reportsInsightsSexualViolenceStat = computed(() => settingsStore.settings.reports_insights_sexual_violence_stat || 'Sexual Violence: 14.7% (595 cases)')
  const reportsInsightsEconomicViolenceStat = computed(() => settingsStore.settings.reports_insights_economic_violence_stat || 'Economic Violence: 5.0% (423 cases)')
  const reportsInsightsSummaryTitle = computed(() => settingsStore.settings.reports_insights_summary_title || 'Executive Summary')
  const reportsInsightsSummaryParagraph1 = computed(() => settingsStore.settings.reports_insights_summary_paragraph_1 || 'Child Neglect remains the highest reported category, accounting for 48.1% of all cases (2,746 cases). This reflects the critical need for child protection services and support systems.')
  const reportsInsightsSummaryParagraph2 = computed(() => settingsStore.settings.reports_insights_summary_paragraph_2 || 'Physical Violence follows at 17.0% (817 cases), while Sexual Violence represents 14.7% (595 cases), highlighting the urgent need for comprehensive protection services.')
  const reportsInsightsSummaryParagraph3 = computed(() => settingsStore.settings.reports_insights_summary_paragraph_3 || 'These trends indicate the importance of continued awareness campaigns and accessible reporting mechanisms across all regions of Uganda.')
  const reportsInsightsCasesPerRegion = computed(() => settingsStore.settings.reports_insights_cases_per_region || 'Regional Distribution')
  const reportsInsightsDateRange = computed(() => settingsStore.settings.reports_insights_date_range || 'FY 2025 Statistical Overview')
  const reportsInsightsRegionalTrends = computed(() => settingsStore.settings.reports_insights_regional_trends || 'Regional Trends')
  const reportsInsightsRegionalTrendsParagraph1 = computed(() => settingsStore.settings.reports_insights_regional_trends_paragraph_1 || 'Central region consistently reports the highest number of cases throughout the year, with peaks in May (470 cases) and April (330 cases).')
  const reportsInsightsRegionalTrendsParagraph2 = computed(() => settingsStore.settings.reports_insights_regional_trends_paragraph_2 || 'Eastern region shows steady reporting with 1,320 total cases, while Northern region has 650 cases, with notable spikes in May (290 cases) and October (170 cases).')
  const reportsInsightsRegionalTrendsParagraph3 = computed(() => settingsStore.settings.reports_insights_regional_trends_paragraph_3 || 'This data helps guide resource allocation and targeted intervention programs across different regions.')
  const reportsInsightsCaseCategoriesPerAgeGroup = computed(() => settingsStore.settings.reports_insights_case_categories_per_age_group || 'Age Group Analysis')
  const reportsInsightsCaseCategoriesPerGender = computed(() => settingsStore.settings.reports_insights_case_categories_per_gender || 'Gender Sensitivity Data')

  // Mock datasets
  const categoryLabels = [
    'Child Neglect',
    'Physical Violence',
    'Sexual Violence',
    'Economic Violence',
    'Emotional Abuse',
    'Others'
  ]
  const categoryValues = [2746, 817, 595, 423, 134, 400]

  const timelineLabels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  const regionTimeSeriesData = computed(() => ({
    'CENTRAL': [310, 230, 260, 330, 470, 270, 330, 270, 260, 280, 20, 5],
    'EASTERN': [100, 110, 110, 120, 150, 120, 120, 120, 120, 150, 5, 0],
    'NORTHERN': [20, 70, 20, 20, 290, 20, 20, 20, 20, 170, 5, 0],
    'WESTERN': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0]
  }))

  const ageGroupLabels = ['Child Neglect', 'Physical Violence', 'Sexual Violence', 'Economic Violence', 'Others']
  const ageGroupData = {
    '0-4': [895, 334, 120, 50, 30],
    '5-9': [620, 95, 90, 40, 20],
    '10-13': [489, 100, 95, 60, 40],
    '14-17': [400, 170, 150, 100, 80],
    '18+': [200, 163, 170, 145, 120]
  }

  const genderData = {
    'Female': [1402, 482, 557, 260, 200],
    'Male': [1297, 326, 32, 155, 150],
    'Unknown': [62, 11, 3, 11, 10]
  }

  // Chart components
  const PieChart = {
    name: 'PieChart',
    props: { labels: Array, values: Array },
    components: { Pie },
    setup(props) {
      const data = computed(() => ({
        labels: props.labels,
        datasets: [{
          data: props.values,
          backgroundColor: ['#007BBF', '#8CC63F', '#FF9933', '#006633', '#ED1C24', '#F4F4F4']
        }]
      }))
      const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: {
              boxWidth: 12,
              font: { size: 10, family: 'Cronos Pro', weight: '900' },
              padding: 20
            }
          }
        }
      }
      return { data, options }
    },
    template: `<Pie :data="data" :options="options" />`
  }

  const RegionChart = {
    name: 'RegionChart',
    props: { labels: Array, regionData: Object },
    components: { Bar },
    setup(props) {
      const data = computed(() => ({
        labels: props.labels,
        datasets: Object.entries(props.regionData).map(([label, values], idx) => ({
          label,
          data: values,
          backgroundColor: ['#007BBF', '#8CC63F', '#FF9933', '#006633'][idx % 4],
          borderRadius: 4
        }))
      }))
      const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          x: { stacked: true, grid: { display: false } },
          y: { stacked: true, beginAtZero: true, grid: { color: '#F0F0F0' } }
        }
      }
      return { data, options }
    },
    template: `<Bar :data="data" :options="options" />`
  }

  const AgeGroupChart = {
    name: 'AgeGroupChart',
    props: { labels: Array, ageData: Object },
    components: { Bar },
    setup(props) {
      const data = computed(() => ({
        labels: props.labels,
        datasets: Object.entries(props.ageData).map(([label, values], idx) => ({
          label,
          data: values,
          backgroundColor: ['#007BBF', '#8CC63F', '#FF9933', '#006633', '#001A33'][idx % 5],
          borderRadius: 6
        }))
      }))
      const options = {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { position: 'bottom', labels: { boxWidth: 10, font: { size: 10 } } } },
        scales: {
          x: { stacked: true, beginAtZero: true },
          y: { stacked: true }
        }
      }
      return { data, options }
    },
    template: `<Bar :data="data" :options="options" />`
  }

  const GenderChart = {
    name: 'GenderChart',
    props: { labels: Array, genderData: Object },
    components: { Bar },
    setup(props) {
      const data = computed(() => ({
        labels: props.labels,
        datasets: Object.entries(props.genderData).map(([label, values], idx) => ({
          label,
          data: values,
          backgroundColor: ['#007BBF', '#8CC63F', '#F4F4F4'][idx % 3],
          borderRadius: 8
        }))
      }))
      const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { position: 'bottom' } },
        scales: {
          x: { stacked: true },
          y: { stacked: true, beginAtZero: true }
        }
      }
      return { data, options }
    },
    template: `<Bar :data="data" :options="options" />`
  }
</script>
