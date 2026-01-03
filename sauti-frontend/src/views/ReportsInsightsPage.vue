<template>
  <div class="bg-neutral py-12">
    <div class="container-custom">
      <!-- Heading -->
      <div class="text-center mb-16 max-w-4xl mx-auto">
        <h1 class="text-4xl md:text-5xl lg:text-7xl font-black text-darkGreen mb-6 tracking-tight">
          Reports <span class="text-blue">&</span> Insights
        </h1>
        <p class="text-xl md:text-2xl text-darkGreen/70 font-bold leading-relaxed">{{ reportsInsightsSubtitle }}
        </p>
      </div>

      <!-- Filters -->
      <div class="bg-white rounded-[3rem] shadow-sm border-2 border-neutral p-10 mb-12">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-end">
          <div>
            <label class="block text-[10px] font-black uppercase tracking-widest text-darkGreen/50 mb-3">{{
              reportsInsightsSearchLabel }}</label>
            <div class="relative group">
              <input v-model="search"
                class="w-full bg-neutral border-2 border-transparent focus:border-blue focus:bg-white py-4 pl-14 pr-6 rounded-2xl outline-none transition-all font-bold text-darkGreen"
                :placeholder="reportsInsightsSearchPlaceholder" />
              <svg
                class="w-6 h-6 text-darkGreen/30 absolute left-5 top-1/2 -translate-y-1/2 group-focus-within:text-blue transition-colors"
                fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                  d="M21 21l-4.35-4.35M10 18a8 8 0 100-16 8 8 0 000 16z" />
              </svg>
            </div>
          </div>
          <div>
            <label class="block text-[10px] font-black uppercase tracking-widest text-darkGreen/50 mb-3">{{
              reportsInsightsRegionLabel }}</label>
            <div class="relative">
              <select v-model="region"
                class="w-full appearance-none bg-neutral border-2 border-transparent focus:border-blue focus:bg-white py-4 px-6 rounded-2xl outline-none transition-all font-black text-darkGreen uppercase tracking-widest text-xs cursor-pointer">
                <option value="all">{{ reportsInsightsAllRegions }}</option>
                <option>Central</option>
                <option>Eastern</option>
                <option>Northern</option>
                <option>Western</option>
              </select>
              <svg class="absolute right-4 top-1/2 -translate-y-1/2 w-5 h-5 text-darkGreen/40 pointer-events-none"
                fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M19 9l-7 7-7-7" />
              </svg>
            </div>
          </div>
          <div class="flex md:justify-end">
            <button
              class="px-10 py-4 bg-blue text-white rounded-2xl font-black uppercase tracking-widest text-xs shadow-xl shadow-blue/20 hover:scale-105 transition-all w-full md:w-auto">
              {{ reportsInsightsApplyFilters }}
            </button>
          </div>
        </div>
        <!-- Date range placeholder strip -->
        <div
          class="mt-10 h-28 rounded-[2rem] bg-neutral/30 border-2 border-dashed border-neutral flex flex-col items-center justify-center text-darkGreen/40 text-sm font-black uppercase tracking-[0.2em] gap-2">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
          </svg>
          {{ reportsInsightsDateRangePlaceholder }}
        </div>
      </div>

      <!-- Cards grid -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-10">
        <!-- Cases Per Category (Pie Chart) -->
        <div
          class="bg-white rounded-[3.5rem] border-2 border-neutral shadow-sm p-10 md:p-12 transition-all duration-500 hover:shadow-2xl hover:shadow-darkGreen/5">
          <h4 class="text-2xl font-black text-darkGreen mb-8 flex items-center gap-4">
            <span class="w-2 h-8 bg-lightGreen rounded-full"></span>
            {{ reportsInsightsCasesPerCategory }}
          </h4>
          <PieChart :labels="categoryLabels" :values="categoryValues" />
          <div class="mt-12 p-8 bg-neutral/30 rounded-3xl border-2 border-neutral">
            <p class="text-[10px] font-black uppercase tracking-widest text-darkGreen/40 mb-6">{{
              reportsInsightsKeyInsights }}</p>
            <ul class="space-y-4 font-black text-lg text-darkGreen">
              <li class="flex items-center gap-4">
                <div class="w-3 h-3 rounded-full bg-lightGreen shadow-lg shadow-lightGreen/20"></div> {{
                reportsInsightsChildNeglectStat }}
              </li>
              <li class="flex items-center gap-4">
                <div class="w-3 h-3 rounded-full bg-blue shadow-lg shadow-blue/20"></div> {{
                reportsInsightsPhysicalViolenceStat }}
              </li>
              <li class="flex items-center gap-4">
                <div class="w-3 h-3 rounded-full bg-orange shadow-lg shadow-orange/20"></div> {{
                reportsInsightsSexualViolenceStat }}
              </li>
              <li class="flex items-center gap-4">
                <div class="w-3 h-3 rounded-full bg-darkGreen shadow-lg shadow-darkGreen/20"></div> {{
                reportsInsightsEconomicViolenceStat }}
              </li>
            </ul>
          </div>
        </div>

        <!-- Summary -->
        <div
          class="bg-white rounded-[3.5rem] border-2 border-neutral shadow-sm p-10 md:p-12 transition-all duration-500 hover:shadow-2xl hover:shadow-darkGreen/5 flex flex-col justify-center">
          <h4 class="text-2xl font-black text-darkGreen mb-8 flex items-center gap-4">
            <span class="w-2 h-8 bg-blue rounded-full"></span>
            {{ reportsInsightsSummaryTitle }}
          </h4>
          <div class="space-y-6 text-darkGreen/70 leading-relaxed font-bold text-lg">
            <p>{{ reportsInsightsSummaryParagraph1 }}</p>
            <p>{{ reportsInsightsSummaryParagraph2 }}</p>
            <p>{{ reportsInsightsSummaryParagraph3 }}</p>
          </div>
        </div>

        <!-- Cases Per Region Over Time -->
        <div
          class="bg-white rounded-[3.5rem] border-2 border-neutral shadow-sm p-10 md:p-12 transition-all duration-500 hover:shadow-2xl hover:shadow-darkGreen/5">
          <h4 class="text-2xl font-black text-darkGreen mb-3 flex items-center gap-4">
            <span class="w-2 h-8 bg-orange rounded-full"></span>
            {{ reportsInsightsCasesPerRegion }}
          </h4>
          <p class="text-[10px] text-darkGreen/40 mb-10 font-black uppercase tracking-widest">{{
            reportsInsightsDateRange
            }}</p>
          <RegionChart :labels="timelineLabels" :regionData="regionTimeSeriesData" />
          <div class="mt-12 p-8 bg-neutral/30 rounded-3xl border-2 border-neutral">
            <p class="text-[10px] font-black uppercase tracking-widest text-darkGreen/40 mb-6">{{
              reportsInsightsRegionsLabel }}</p>
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-6">
              <div class="flex items-center gap-3">
                <div class="w-4 h-4 rounded-lg shadow-sm" style="background-color: #0077A6"></div>
                <span class="text-sm font-black text-darkGreen/60">{{ reportsInsightsRegionCentral }}</span>
              </div>
              <div class="flex items-center gap-3">
                <div class="w-4 h-4 rounded-lg shadow-sm" style="background-color: #00BD70"></div>
                <span class="text-sm font-black text-darkGreen/60">{{ reportsInsightsRegionEastern }}</span>
              </div>
              <div class="flex items-center gap-3">
                <div class="w-4 h-4 rounded-lg shadow-sm" style="background-color: #FF9900"></div>
                <span class="text-sm font-black text-darkGreen/60">{{ reportsInsightsRegionNorthern }}</span>
              </div>
              <div class="flex items-center gap-3">
                <div class="w-4 h-4 rounded-lg shadow-sm" style="background-color: #009EDB"></div>
                <span class="text-sm font-black text-darkGreen/60">{{ reportsInsightsRegionWestern }}</span>
              </div>
              <div class="flex items-center gap-3">
                <div class="w-4 h-4 rounded-lg shadow-sm" style="background-color: #002B52"></div>
                <span class="text-sm font-black text-darkGreen/60">{{ reportsInsightsRegionInternational }}</span>
              </div>
              <div class="flex items-center gap-3">
                <div class="w-4 h-4 rounded-lg shadow-sm bg-white border-2 border-neutral"></div>
                <span class="text-sm font-black text-darkGreen/60">{{ reportsInsightsRegionUnknown }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Summary -->
        <div
          class="bg-white rounded-[3.5rem] border-2 border-neutral shadow-sm p-10 md:p-12 transition-all duration-500 hover:shadow-2xl hover:shadow-darkGreen/5 flex flex-col justify-center">
          <h4 class="text-2xl font-black text-darkGreen mb-8 flex items-center gap-4">
            <span class="w-2 h-8 bg-lightGreen rounded-full"></span>
            {{ reportsInsightsRegionalTrends }}
          </h4>
          <div class="space-y-6 text-darkGreen/70 leading-relaxed font-bold text-lg">
            <p>{{ reportsInsightsRegionalTrendsParagraph1 }}</p>
            <p>{{ reportsInsightsRegionalTrendsParagraph2 }}</p>
            <p>{{ reportsInsightsRegionalTrendsParagraph3 }}</p>
          </div>
        </div>

        <!-- Case Categories per Age Group -->
        <div
          class="bg-white rounded-[3.5rem] border-2 border-neutral shadow-sm p-10 md:p-12 transition-all duration-500 hover:shadow-2xl hover:shadow-darkGreen/5 lg:col-span-2">
          <h4 class="text-2xl font-black text-darkGreen mb-10 flex items-center gap-4">
            <span class="w-2 h-8 bg-blue rounded-full"></span>
            {{ reportsInsightsCaseCategoriesPerAgeGroup }}
          </h4>
          <AgeGroupChart :labels="ageGroupLabels" :ageData="ageGroupData" />
          <div class="mt-12 p-8 bg-neutral/30 rounded-3xl border-2 border-neutral">
            <p class="text-[10px] font-black uppercase tracking-widest text-darkGreen/40 mb-6">{{
              reportsInsightsAgeGroupsLabel }}</p>
            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-6">
              <div v-for="(color, age, idx) in {
                [reportsInsightsAgeGroup04]: '#0077A6',
                [reportsInsightsAgeGroup0509]: '#00BD70',
                [reportsInsightsAgeGroup1013]: '#009EDB',
                [reportsInsightsAgeGroup1417]: '#86efac',
                [reportsInsightsAgeGroup1824]: '#FF9900',
                [reportsInsightsAgeGroup2530]: '#002B52',
                [reportsInsightsAgeGroup3145]: '#0077A6',
                [reportsInsightsAgeGroupAbove60]: '#002B52',
                [reportsInsightsAgeGroupUnknown]: '#F8F9FA'
              }" :key="age" class="flex items-center gap-3">
                <div class="w-4 h-4 rounded-lg shadow-sm" :style="{ backgroundColor: color }"></div>
                <span class="text-sm font-black text-darkGreen/60">{{ age }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Case Categories per Gender -->
        <div
          class="bg-white rounded-[3.5rem] border-2 border-neutral shadow-sm p-10 md:p-12 transition-all duration-500 hover:shadow-2xl hover:shadow-darkGreen/5 lg:col-span-2">
          <h4 class="text-2xl font-black text-darkGreen mb-10 flex items-center gap-4">
            <span class="w-2 h-8 bg-orange rounded-full"></span>
            {{ reportsInsightsCaseCategoriesPerGender }}
          </h4>
          <GenderChart :labels="ageGroupLabels" :genderData="genderData" />
          <div class="mt-12 p-8 bg-neutral/30 rounded-3xl border-2 border-neutral">
            <p class="text-[10px] font-black uppercase tracking-widest text-darkGreen/40 mb-6">{{
              reportsInsightsGenderBreakdownLabel }}</p>
            <div class="flex flex-wrap gap-10">
              <div class="flex items-center gap-3">
                <div class="w-4 h-4 rounded-lg shadow-sm" style="background-color: #0077A6"></div>
                <span class="text-sm font-black text-darkGreen/60">{{ reportsInsightsGenderFemale }}</span>
              </div>
              <div class="flex items-center gap-3">
                <div class="w-4 h-4 rounded-lg shadow-sm" style="background-color: #00BD70"></div>
                <span class="text-sm font-black text-darkGreen/60">{{ reportsInsightsGenderMale }}</span>
              </div>
              <div class="flex items-center gap-3">
                <div class="w-4 h-4 rounded-lg shadow-sm bg-white border-2 border-neutral"></div>
                <span class="text-sm font-black text-darkGreen/60">{{ reportsInsightsGenderUnknown }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Footer row like mock -->
      <div class="mt-32 py-12 border-t-2 border-neutral flex flex-col items-center text-center">
        <div class="flex gap-8 text-[10px] font-black uppercase tracking-[0.2em] text-darkGreen/30 mb-8">
          <router-link to="/privacy" class="hover:text-blue transition-colors">{{ reportsInsightsPrivacyPolicy
            }}</router-link>
          <router-link to="/terms" class="hover:text-blue transition-colors">{{ reportsInsightsTermsOfService
            }}</router-link>
          <router-link to="/contact" class="hover:text-blue transition-colors">{{ reportsInsightsContactUs
            }}</router-link>
        </div>
        <p class="text-[10px] font-black uppercase tracking-[0.2em] text-darkGreen/20">{{
          reportsInsightsFooterText }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed } from 'vue'
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

  ChartJS.register(Title, Tooltip, Legend, BarElement, LineElement, CategoryScale, LinearScale, PointElement, ArcElement)

  defineOptions({
    name: 'ReportsInsightsPage'
  })

  const search = ref('')
  const region = ref('all')
  const settingsStore = useSettingsStore()

  import { onMounted } from 'vue'
  onMounted(() => {
    settingsStore.fetchGlobalSettings()
  })

  // Computed properties for content
  const reportsInsightsTitle = computed(() => settingsStore.settings.reports_insights_title || 'Reports & Insights')
  const reportsInsightsSubtitle = computed(() => settingsStore.settings.reports_insights_subtitle || 'Explore the data collected by Sauti Uganda 116 helpline to understand the trends and patterns in child abuse and neglect across the country.')
  const reportsInsightsSearchLabel = computed(() => settingsStore.settings.reports_insights_search_label || 'Search')
  const reportsInsightsSearchPlaceholder = computed(() => settingsStore.settings.reports_insights_search_placeholder || 'Search reports by keyword')
  const reportsInsightsRegionLabel = computed(() => settingsStore.settings.reports_insights_region_label || 'Region')
  const reportsInsightsAllRegions = computed(() => settingsStore.settings.reports_insights_all_regions || 'All Regions')
  const reportsInsightsApplyFilters = computed(() => settingsStore.settings.reports_insights_apply_filters || 'Apply Filters')
  const reportsInsightsDateRangePlaceholder = computed(() => settingsStore.settings.reports_insights_date_range_placeholder || 'Date Range Picker (placeholder)')
  const reportsInsightsCasesPerCategory = computed(() => settingsStore.settings.reports_insights_cases_per_category || 'Cases Per Category')
  const reportsInsightsKeyInsights = computed(() => settingsStore.settings.reports_insights_key_insights || 'Key Insights:')
  const reportsInsightsChildNeglectStat = computed(() => settingsStore.settings.reports_insights_child_neglect_stat || 'Child Neglect: 48.1% (2,746 cases)')
  const reportsInsightsPhysicalViolenceStat = computed(() => settingsStore.settings.reports_insights_physical_violence_stat || 'Physical Violence: 17.0% (817 cases)')
  const reportsInsightsSexualViolenceStat = computed(() => settingsStore.settings.reports_insights_sexual_violence_stat || 'Sexual Violence: 14.7% (595 cases)')
  const reportsInsightsEconomicViolenceStat = computed(() => settingsStore.settings.reports_insights_economic_violence_stat || 'Economic Violence: 5.0% (423 cases)')
  const reportsInsightsSummaryTitle = computed(() => settingsStore.settings.reports_insights_summary_title || 'Summary')
  const reportsInsightsSummaryParagraph1 = computed(() => settingsStore.settings.reports_insights_summary_paragraph_1 || 'Child Neglect remains the highest reported category, accounting for 48.1% of all cases (2,746 cases). This reflects the critical need for child protection services and support systems.')
  const reportsInsightsSummaryParagraph2 = computed(() => settingsStore.settings.reports_insights_summary_paragraph_2 || 'Physical Violence follows at 17.0% (817 cases), while Sexual Violence represents 14.7% (595 cases), highlighting the urgent need for comprehensive protection services.')
  const reportsInsightsSummaryParagraph3 = computed(() => settingsStore.settings.reports_insights_summary_paragraph_3 || 'These trends indicate the importance of continued awareness campaigns and accessible reporting mechanisms across all regions of Uganda.')
  const reportsInsightsCasesPerRegion = computed(() => settingsStore.settings.reports_insights_cases_per_region || 'Cases Per Region')
  const reportsInsightsDateRange = computed(() => settingsStore.settings.reports_insights_date_range || '01/01/2025 12:00 AM - 31/12/2025 12:00 AM')
  const reportsInsightsRegionsLabel = computed(() => settingsStore.settings.reports_insights_regions_label || 'Regions:')
  const reportsInsightsRegionCentral = computed(() => settingsStore.settings.reports_insights_region_central || 'Central')
  const reportsInsightsRegionEastern = computed(() => settingsStore.settings.reports_insights_region_eastern || 'Eastern')
  const reportsInsightsRegionNorthern = computed(() => settingsStore.settings.reports_insights_region_northern || 'Northern')
  const reportsInsightsRegionWestern = computed(() => settingsStore.settings.reports_insights_region_western || 'Western')
  const reportsInsightsRegionInternational = computed(() => settingsStore.settings.reports_insights_region_international || 'International')
  const reportsInsightsRegionUnknown = computed(() => settingsStore.settings.reports_insights_region_unknown || 'Unknown')
  const reportsInsightsRegionalTrends = computed(() => settingsStore.settings.reports_insights_regional_trends || 'Regional Trends')
  const reportsInsightsRegionalTrendsParagraph1 = computed(() => settingsStore.settings.reports_insights_regional_trends_paragraph_1 || 'Central region consistently reports the highest number of cases throughout the year, with peaks in May (470 cases) and April (330 cases).')
  const reportsInsightsRegionalTrendsParagraph2 = computed(() => settingsStore.settings.reports_insights_regional_trends_paragraph_2 || 'Eastern region shows steady reporting with 1,320 total cases, while Northern region has 650 cases, with notable spikes in May (290 cases) and October (170 cases).')
  const reportsInsightsRegionalTrendsParagraph3 = computed(() => settingsStore.settings.reports_insights_regional_trends_paragraph_3 || 'This data helps guide resource allocation and targeted intervention programs across different regions.')
  const reportsInsightsCaseCategoriesPerAgeGroup = computed(() => settingsStore.settings.reports_insights_case_categories_per_age_group || 'Case Categories per Age Group')
  const reportsInsightsAgeGroupsLabel = computed(() => settingsStore.settings.reports_insights_age_groups_label || 'Age Groups:')
  const reportsInsightsAgeGroup04 = computed(() => settingsStore.settings.reports_insights_age_group_04 || '0-04')
  const reportsInsightsAgeGroup0509 = computed(() => settingsStore.settings.reports_insights_age_group_0509 || '05-09')
  const reportsInsightsAgeGroup1013 = computed(() => settingsStore.settings.reports_insights_age_group_1013 || '10-13')
  const reportsInsightsAgeGroup1417 = computed(() => settingsStore.settings.reports_insights_age_group_1417 || '14-17')
  const reportsInsightsAgeGroup1824 = computed(() => settingsStore.settings.reports_insights_age_group_1824 || '18-24')
  const reportsInsightsAgeGroup2530 = computed(() => settingsStore.settings.reports_insights_age_group_2530 || '25-30')
  const reportsInsightsAgeGroup3145 = computed(() => settingsStore.settings.reports_insights_age_group_3145 || '31-45')
  const reportsInsightsAgeGroupAbove60 = computed(() => settingsStore.settings.reports_insights_age_group_above_60 || 'Above 60')
  const reportsInsightsAgeGroupUnknown = computed(() => settingsStore.settings.reports_insights_age_group_unknown || 'Unknown')
  const reportsInsightsCaseCategoriesPerGender = computed(() => settingsStore.settings.reports_insights_case_categories_per_gender || 'Case Categories per Gender')
  const reportsInsightsGenderBreakdownLabel = computed(() => settingsStore.settings.reports_insights_gender_breakdown_label || 'Gender Breakdown:')
  const reportsInsightsGenderFemale = computed(() => settingsStore.settings.reports_insights_gender_female || 'Female')
  const reportsInsightsGenderMale = computed(() => settingsStore.settings.reports_insights_gender_male || 'Male')
  const reportsInsightsGenderUnknown = computed(() => settingsStore.settings.reports_insights_gender_unknown || 'Unknown')
  const reportsInsightsPrivacyPolicy = computed(() => settingsStore.settings.reports_insights_privacy_policy || 'Privacy Policy')
  const reportsInsightsTermsOfService = computed(() => settingsStore.settings.reports_insights_terms_of_service || 'Terms of Service')
  const reportsInsightsContactUs = computed(() => settingsStore.settings.reports_insights_contact_us || 'Contact Us')
  const reportsInsightsFooterText = computed(() => settingsStore.settings.reports_insights_footer_text || '© 2024 Sauti Uganda 116 helpline. All rights reserved.')

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
            '#00BD70', // Child Neglect - lightGreen
            '#0077A6', // Physical Violence - blue
            '#FF9900', // Sexual Violence - orange
            '#002B52', // Economic Violence - darkGreen
            '#FF0000', // Emotional Abuse - red
            '#C00000', // Murder - dark red
            '#009EDB', // Trafficking - info blue
            '#10b981', // Child Exploitation - green
            '#f59e0b', // Harmful Practices - amber
            '#F8F9FA', // Others - neutral
            '#0077A6', // Threatening - primary blue
            '#FF9900'  // Online Abuse - orange
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
              label: function (context) {
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
            backgroundColor: '#0077A6' // blue
          },
          {
            label: 'EASTERN',
            data: props.regionData.EASTERN,
            backgroundColor: '#00BD70' // lightGreen
          },
          {
            label: 'NORTHERN',
            data: props.regionData.NORTHERN,
            backgroundColor: '#FF9900' // orange
          },
          {
            label: 'WESTERN',
            data: props.regionData.WESTERN,
            backgroundColor: '#009EDB' // info blue
          },
          {
            label: 'INTERNATIONAL',
            data: props.regionData.INTERNATIONAL,
            backgroundColor: '#002B52' // darkGreen
          },
          {
            label: 'Unknown',
            data: props.regionData.Unknown,
            backgroundColor: '#F8F9FA' // neutral
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
      const colors = ['#0077A6', '#00BD70', '#009EDB', '#86efac', '#FF9900', '#002B52', '#0077A6', '#002B52', '#0077A6', '#F8F9FA']

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
            backgroundColor: '#0077A6' // blue
          },
          {
            label: 'Male',
            data: props.genderData.Male,
            backgroundColor: '#00BD70' // lightGreen
          },
          {
            label: 'Unknown',
            data: props.genderData.Unknown,
            backgroundColor: '#F8F9FA' // neutral
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
</script>
