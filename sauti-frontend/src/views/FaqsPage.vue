<template>
  <div class="bg-neutral-white min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <p class="text-sm uppercase tracking-[0.4em] text-primary font-bold mb-4">{{ faqsPageTitle }}</p>
        <h1 class="page-header-title">
          {{ faqsPageSubtitle }}
        </h1>

        <!-- FAQ in a Flash (Flash Pattern) -->
        <div
          class="mt-16 bg-neutral-white p-8 md:p-12 rounded-[3rem] border-2 border-primary/10 shadow-sm max-w-5xl mx-auto">
          <h2 class="campaign-header text-xl text-primary mb-8 flex items-center gap-3">
            <ShieldCheckIcon class="w-6 h-6 text-primary" />
            Quick Answers for Immediate Help
          </h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-left">
            <div class="space-y-2">
              <p class="text-secondary font-bold">Is it free?</p>
              <p class="text-secondary/60 text-sm"><strong>Yes</strong>. Calls to 116 are 100% toll-free across all
                networks.</p>
            </div>
            <div class="space-y-2">
              <p class="text-secondary font-bold">Is it private?</p>
              <p class="text-secondary/60 text-sm"><strong>Yes</strong>. We protect your story and you can report
                anonymously.</p>
            </div>
            <div class="space-y-2">
              <p class="text-secondary font-bold">When can I call?</p>
              <p class="text-secondary/60 text-sm"><strong>Anytime</strong>. Our counselors are here 24 hours a day,
                every day.</p>
            </div>
          </div>
        </div>
      </div>
    </header>

    <div class="container-custom section-padding">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">

        <!-- Left Sidebar (Support Info) -->
        <div class="lg:col-span-4 order-2 lg:order-1 space-y-10 lg:sticky lg:top-32">
          <!-- Hero Card -->
          <div class="rounded-[3rem] bg-primary p-10 text-neutral-white shadow-xl relative overflow-hidden">
            <div class="relative z-10 text-center space-y-6">
              <div
                class="w-20 h-20 mx-auto bg-neutral-white/10 rounded-2xl flex items-center justify-center border border-neutral-white/20">
                <svg class="w-10 h-10 text-neutral-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                    d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z" />
                </svg>
              </div>
              <div>
                <h3 class="text-3xl font-bold mb-2 tracking-tight">{{ faqsSupportTitle }}</h3>
                <p class="text-neutral-white/80 font-bold leading-relaxed">{{ faqsSupportSubtitle }}</p>
              </div>
            </div>
          </div>

          <!-- Emergency Contact Card -->
          <div class="rounded-[3rem] bg-emergency/5 p-10 shadow-2xl space-y-6">
            <h4 class="campaign-header text-2xl text-emergency">{{ faqsImmediateHelpTitle }}</h4>
            <p class="text-secondary font-bold leading-relaxed">{{ faqsImmediateHelpSubtitle }}</p>
            <BaseCTA :href="`tel:116`" variant="emergency" class="w-full justify-center !py-4 font-bold" external>
              {{ faqsCallButton }}
            </BaseCTA>
          </div>
        </div>

        <!-- Right Content (FAQs) -->
        <div class="lg:col-span-8 order-1 lg:order-2 space-y-12">
          <!-- Search Bar -->
          <div class="relative mb-12 group">
            <div class="absolute inset-y-0 left-0 pl-8 flex items-center pointer-events-none">
              <svg class="h-8 w-8 text-primary group-focus-within:text-secondary transition-colors" fill="none"
                viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
            <input v-model="query" type="text" :placeholder="faqsSearchPlaceholder"
              class="w-full pl-20 pr-8 py-8 bg-neutral-white shadow-lg rounded-[2.5rem] text-secondary font-bold placeholder:text-primary/40 focus:outline-none focus:shadow-2xl transition-all text-xl" />
          </div>

          <AppLoader v-if="loading" />

          <div v-else>
            <!-- Category Filter -->
            <div v-if="categories.length" class="mb-12 overflow-x-auto pb-6 -mx-2 px-2 scrollbar-hide">
              <div class="flex flex-nowrap gap-4">
                <button @click="selectedCategory = ''"
                  :class="selectedCategory === '' ? 'bg-secondary text-neutral-white shadow-xl' : 'bg-neutral-white text-secondary shadow-md hover:shadow-lg'"
                  class="px-10 py-4 rounded-2xl text-[10px] font-bold uppercase tracking-widest whitespace-nowrap transition-all duration-300">
                  {{ faqsAllCategoriesButton }}
                </button>
                <button v-for="category in categories" :key="category.id" @click="selectedCategory = category.id"
                  :class="selectedCategory === category.id ? 'bg-secondary text-neutral-white shadow-xl' : 'bg-neutral-white text-secondary shadow-md hover:shadow-lg'"
                  class="px-10 py-4 rounded-2xl text-[10px] font-bold uppercase tracking-widest whitespace-nowrap transition-all duration-300">
                  {{ category.name }}
                </button>
              </div>
            </div>

            <!-- FAQ List -->
            <div v-if="filteredFaqs.length" class="space-y-8">
              <div v-for="(faq, index) in filteredFaqs" :key="faq.id || index"
                class="group bg-neutral-white rounded-[3rem] shadow-lg transition-all duration-500 overflow-hidden"
                :class="{ 'shadow-2xl': openFaq === index }">
                <button @click="toggleFaq(index)"
                  class="w-full text-left px-10 py-10 flex items-start gap-8 hover:bg-neutral-offwhite/30 transition-colors focus:outline-none"
                  :aria-expanded="openFaq === index">
                  <div class="mt-2 flex-shrink-0">
                    <div class="w-10 h-10 rounded-2xl flex items-center justify-center transition-all duration-500"
                      :class="openFaq === index ? 'bg-secondary text-neutral-white shadow-md' : 'bg-neutral-offwhite text-primary'">
                      <svg class="w-5 h-5 transition-transform duration-500 transform"
                        :class="{ 'rotate-180': openFaq === index }" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M19 9l-7 7-7-7" />
                      </svg>
                    </div>
                  </div>
                  <div class="flex-1">
                    <span
                      class="font-bold text-secondary text-2xl block mb-4 leading-tight group-hover:text-primary transition-colors">{{
                        faq.question
                      }}</span>
                    <span v-if="faq.category_name"
                      class="inline-block px-4 py-1.5 rounded-xl text-[10px] uppercase font-bold tracking-widest bg-primary text-neutral-white">{{
                        faq.category_name }}</span>
                  </div>
                </button>

                <div v-show="openFaq === index"
                  class="px-10 pb-12 pl-[6.5rem] text-secondary font-bold text-lg leading-relaxed pt-2 animate-fade-in bg-neutral-white">
                  <p class="max-w-3xl">{{ faq.answer }}</p>
                </div>
              </div>
            </div>

            <!-- Empty State -->
            <div v-else class="text-center py-24 bg-neutral-white rounded-[4rem] shadow-lg max-w-2xl mx-auto">
              <div
                class="w-24 h-24 mx-auto bg-neutral-offwhite/10 rounded-3xl flex items-center justify-center mb-8 shadow-sm">
                <svg class="w-12 h-12 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                    d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <h3 class="text-3xl font-bold text-secondary mb-4">{{ faqsNoResults }}</h3>
              <p class="text-xl text-secondary/50 font-bold mb-10">{{ faqsNoResultsSubtitle }}</p>
              <button @click="query = ''; selectedCategory = ''"
                class="px-12 py-4 bg-primary text-neutral-white rounded-2xl font-bold uppercase tracking-widest text-xs shadow-xl shadow-primary/20 hover:scale-105 transition-all">
                Clear all filters
              </button>
            </div>
          </div>

          <!-- Footer Links -->
          <div
            class="mt-32 py-10 border-t-2 border-primary flex flex-col md:flex-row items-center justify-between text-[10px] text-primary gap-8 text-center md:text-left font-bold uppercase tracking-widest">
            <p>{{ faqsFooterText }}</p>
            <div class="flex flex-wrap justify-center gap-8">
              <router-link to="/privacy" class="hover:text-primary transition-colors">{{ faqsPrivacyPolicy
              }}</router-link>
              <router-link to="/terms" class="hover:text-primary transition-colors">{{ faqsTermsOfService
              }}</router-link>
              <router-link to="/contact" class="hover:text-primary transition-colors">{{ faqsContactUs
              }}</router-link>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue'
  import { useFaqsStore } from '@/store/faqs'
  import { useSettingsStore } from '@/store/settings'
  import AppLoader from '@/components/common/AppLoader.vue'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import { ShieldCheckIcon } from '@heroicons/vue/24/outline'

  defineOptions({
    name: 'FaqsPage'
  })

  const faqsStore = useFaqsStore()
  const settingsStore = useSettingsStore()
  const faqs = ref([])
  const categories = ref([])
  const loading = ref(true)
  const openFaq = ref(null)
  const query = ref('')
  const selectedCategory = ref('')

  // Computed properties for content
  const faqsSupportTitle = computed(() => settingsStore.settings.faqs_support_title || '24/7 Support')
  const faqsSupportSubtitle = computed(() => settingsStore.settings.faqs_support_subtitle || 'Always here to help')
  const faqsQuickResponseTitle = computed(() => settingsStore.settings.faqs_quick_response_title || 'Quick Response')
  const faqsQuickResponseSubtitle = computed(() => settingsStore.settings.faqs_quick_response_subtitle || 'Get help immediately')
  const faqsQuickResponseText = computed(() => settingsStore.settings.faqs_quick_response_text || 'Our trained counselors are available 24/7 to provide immediate support and guidance.')
  const faqsImmediateHelpTitle = computed(() => settingsStore.settings.faqs_immediate_help_title || 'Need Immediate Help?')
  const faqsImmediateHelpSubtitle = computed(() => settingsStore.settings.faqs_immediate_help_subtitle || 'Call our toll-free helpline')
  const faqsCallButton = computed(() => settingsStore.settings.faqs_call_button || 'Call 116')
  const faqsPageTitle = computed(() => settingsStore.settings.faqs_page_title || 'Frequently Asked')
  const faqsPageSubtitle = computed(() => settingsStore.settings.faqs_page_subtitle || 'Questions & Answers')
  const faqsSearchPlaceholder = computed(() => settingsStore.settings.faqs_search_placeholder || 'Search questions')
  const faqsAllCategoriesButton = computed(() => settingsStore.settings.faqs_all_categories_button || 'All Categories')
  const faqsNoResults = computed(() => settingsStore.settings.faqs_no_results || 'No FAQs found')
  const faqsNoResultsSubtitle = computed(() => settingsStore.settings.faqs_no_results_subtitle || 'Try adjusting your search or category filter')
  const faqsPrivacyPolicy = computed(() => settingsStore.settings.faqs_privacy_policy || 'Privacy Policy')
  const faqsTermsOfService = computed(() => settingsStore.settings.faqs_terms_of_service || 'Terms of Service')
  const faqsContactUs = computed(() => settingsStore.settings.faqs_contact_us || 'Contact Us')
  const faqsFooterText = computed(() => settingsStore.settings.faqs_footer_text || '© 2024 Sauti Uganda. All rights reserved. A sanctuary for every child.')

  onMounted(async () => {
    await settingsStore.fetchGlobalSettings()
    try {
      await faqsStore.fetchFaqs({ status: 'PUBLISHED' })
      faqs.value = Array.isArray(faqsStore.faqs) ? faqsStore.faqs : []

      // Try to fetch categories from API first
      try {
        const fetchedCategories = await faqsStore.fetchCategories()
        if (Array.isArray(fetchedCategories) && fetchedCategories.length > 0) {
          categories.value = fetchedCategories
        } else {
          // Fallback: Extract unique categories from FAQs
          const categoryMap = new Map()
          faqs.value.forEach(faq => {
            if (faq.category_name && !categoryMap.has(faq.category)) {
              categoryMap.set(faq.category, {
                id: faq.category,
                name: faq.category_name
              })
            }
          })
          categories.value = Array.from(categoryMap.values())
        }
      } catch (catError) {
        console.log('Categories API not available, extracting from FAQs')
        // Extract unique categories from FAQs
        const categoryMap = new Map()
        faqs.value.forEach(faq => {
          if (faq.category_name && !categoryMap.has(faq.category)) {
            categoryMap.set(faq.category, {
              id: faq.category,
              name: faq.category_name
            })
          }
        })
        categories.value = Array.from(categoryMap.values())
      }
    } catch (error) {
      console.error('Error fetching FAQs:', error)
      faqs.value = []
    } finally {
      loading.value = false
    }
  })

  const filteredFaqs = computed(() => {
    // Ensure faqs is an array
    let filtered = Array.isArray(faqs.value) ? faqs.value : []

    // Filter by category
    if (selectedCategory.value) {
      filtered = filtered.filter(f => f.category == selectedCategory.value)
    }

    // Filter by search query
    const q = query.value.trim().toLowerCase()
    if (q) {
      filtered = filtered.filter(f =>
        String(f.question).toLowerCase().includes(q) ||
        String(f.answer).toLowerCase().includes(q)
      )
    }

    return filtered
  })

  function toggleFaq(index) {
    openFaq.value = openFaq.value === index ? null : index
  }
</script>
