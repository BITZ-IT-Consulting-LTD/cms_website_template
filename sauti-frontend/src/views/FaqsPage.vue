<template>
  <div class="min-h-screen bg-white">
    <!-- Hero Banner -->
    <header class="hero-banner" style="padding-top: clamp(70px, 15vw, 90px);">
      <div class="hero-overlay"></div>
      <div class="container-custom hero-content-wrapper">
        <div class="hero-text">
          <h1 class="hero-title">
            {{ siteContent.getContent('faqs_page_title', 'Frequently Asked') }} <span class="text-accent-yellow">{{ siteContent.getContent('faqs_page_title_highlight', 'Questions') }}</span>
          </h1>
          <p class="hero-subtitle">
            {{ siteContent.getContent('faqs_page_subtitle', 'Find answers to common questions about our services, child protection, and how we can support you.') }}
          </p>
        </div>
      </div>
    </header>

    <div class="container-custom section-padding !pt-12">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">

        <!-- Left Sidebar (Support Info) -->
        <div class="lg:col-span-4 order-2 lg:order-1 space-y-6 lg:space-y-8 lg:sticky lg:top-32">
          <!-- Hero Card -->
          <div class="rounded-xl lg:rounded-2xl bg-primary p-6 lg:p-8 text-neutral-white relative overflow-hidden">
            <div class="relative z-10 text-center space-y-4 lg:space-y-5">
              <div
                class="w-14 h-14 lg:w-16 lg:h-16 mx-auto bg-neutral-white/10 rounded-xl lg:rounded-2xl flex items-center justify-center border border-neutral-white/20">
                <Clock class="w-7 h-7 lg:w-9 lg:h-9 text-neutral-white" />
              </div>
              <div>
                <h3 class="text-xl lg:text-2xl font-bold mb-1.5 lg:mb-2 tracking-tight">{{ faqsSupportTitle }}</h3>
                <p class="text-sm lg:text-base text-neutral-white/80 font-semibold leading-relaxed">{{ faqsSupportSubtitle }}</p>
              </div>
            </div>
          </div>

          <!-- Emergency Contact Card -->
          <div class="rounded-xl lg:rounded-2xl bg-emergency/5 p-6 lg:p-8 space-y-4 lg:space-y-5">
            <h4 class="text-lg lg:text-xl font-bold text-emergency">{{ faqsImmediateHelpTitle }}</h4>
            <p class="text-sm lg:text-base text-black font-semibold leading-relaxed">{{ faqsImmediateHelpSubtitle }}</p>
            <BaseCTA :href="`tel:116`" variant="emergency" class="w-full justify-center !py-3 lg:!py-4 font-bold text-sm lg:text-base" external>
              {{ faqsCallButton }}
            </BaseCTA>
          </div>
        </div>

        <!-- Right Content (FAQs) -->
        <div class="lg:col-span-8 order-1 lg:order-2 space-y-8 lg:space-y-10">
          <!-- Search Bar -->
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-4 lg:pl-6 flex items-center pointer-events-none">
              <Search class="h-4 w-4 lg:h-5 lg:w-5 text-primary/50" />
            </div>
            <input v-model="query" type="text" :placeholder="faqsSearchPlaceholder"
              class="w-full pl-12 lg:pl-16 pr-4 lg:pr-6 py-3 lg:py-4 bg-neutral-offwhite rounded-full text-secondary font-semibold placeholder:text-black/30 focus:bg-white focus:ring-2 focus:ring-primary/20 transition-all text-sm lg:text-base border-none" />
          </div>

          <AppLoader v-if="loading" />

          <div v-else>
            <!-- Category Filter -->
            <div v-if="categories.length" class="overflow-x-auto pb-4 -mx-2 px-2 hide-scrollbar">
              <div class="flex flex-nowrap gap-2 lg:gap-3">
                <button @click="selectedCategory = ''"
                  :class="selectedCategory === '' ? 'bg-secondary text-neutral-white shadow-lg' : 'bg-neutral-white text-secondary shadow-sm hover:shadow-md'"
                  class="px-4 lg:px-6 py-2 lg:py-2.5 rounded-full text-xs font-bold uppercase tracking-wider whitespace-nowrap transition-all duration-300 flex-shrink-0">
                  {{ faqsAllCategoriesButton }}
                </button>
                <button v-for="category in categories" :key="category.id" @click="selectedCategory = category.id"
                  :class="selectedCategory === category.id ? 'bg-secondary text-neutral-white shadow-lg' : 'bg-neutral-white text-secondary shadow-sm hover:shadow-md'"
                  class="px-4 lg:px-6 py-2 lg:py-2.5 rounded-full text-xs font-bold uppercase tracking-wider whitespace-nowrap transition-all duration-300 flex-shrink-0">
                  {{ category.name }}
                </button>
              </div>
            </div>

            <!-- FAQ List -->
            <div v-if="filteredFaqs.length" class="space-y-4 lg:space-y-5">
              <div v-for="(faq, index) in filteredFaqs" :key="faq.id || index"
                class="group bg-neutral-white rounded-xl lg:rounded-2xl shadow-md transition-all duration-500 overflow-hidden"
                :class="{ 'shadow-xl': openFaq === index }">
                <button @click="toggleFaq(index)"
                  class="w-full text-left px-4 py-4 lg:px-6 lg:py-5 flex items-start gap-3 lg:gap-4 hover:bg-neutral-offwhite/30 transition-colors focus:outline-none"
                  :aria-expanded="openFaq === index">
                  <div class="mt-0.5 lg:mt-1 flex-shrink-0">
                    <div class="w-8 h-8 lg:w-9 lg:h-9 rounded-lg lg:rounded-xl flex items-center justify-center transition-all duration-500"
                      :class="openFaq === index ? 'bg-secondary text-neutral-white shadow-md' : 'bg-neutral-offwhite text-primary'">
                      <ChevronDown class="w-4 h-4 lg:w-5 lg:h-5 transition-transform duration-500 transform"
                        :class="{ 'rotate-180': openFaq === index }" />
                    </div>
                  </div>
                  <div class="flex-1 min-w-0">
                    <span
                      class="font-bold text-secondary text-base lg:text-lg block mb-2 lg:mb-3 leading-snug group-hover:text-primary transition-colors">{{
                        faq.question
                      }}</span>
                    <span v-if="faq.category_name"
                      class="inline-block px-3 py-1 rounded-lg text-[10px] lg:text-xs uppercase font-bold tracking-wider bg-primary/10 text-primary border border-primary/20">{{
                        faq.category_name }}</span>
                  </div>
                </button>

                <div v-show="openFaq === index"
                  class="px-4 pb-5 pl-14 lg:px-6 lg:pb-6 lg:pl-16 text-secondary font-medium text-sm lg:text-base leading-relaxed animate-fade-in bg-neutral-white">
                  <p class="max-w-3xl">{{ faq.answer }}</p>
                </div>
              </div>
            </div>

            <!-- Empty State -->
            <div v-else class="text-center py-16 lg:py-20 max-w-2xl mx-auto">
              <div
                class="w-16 h-16 lg:w-20 lg:h-20 mx-auto bg-neutral-offwhite rounded-2xl flex items-center justify-center mb-6 lg:mb-8 shadow-sm">
                <Search class="w-8 h-8 lg:w-10 lg:h-10 text-primary/60" />
              </div>
              <h3 class="text-xl lg:text-2xl font-bold text-secondary mb-3 lg:mb-4">{{ faqsNoResults }}</h3>
              <p class="text-sm lg:text-base text-black/60 font-semibold mb-6 lg:mb-8">{{ faqsNoResultsSubtitle }}</p>
              <button @click="query = ''; selectedCategory = ''"
                class="px-8 lg:px-10 py-3 lg:py-3.5 bg-primary text-neutral-white rounded-full font-bold uppercase tracking-wider text-xs lg:text-sm shadow-lg shadow-primary/20 hover:scale-105 transition-all">
                Clear all filters
              </button>
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
  import { useSiteContent } from '@/composables/useSiteContent'
  import AppLoader from '@/components/common/AppLoader.vue'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import {
    Clock,
    Search,
    ChevronDown,
    XCircle
  } from 'lucide-vue-next'


  defineOptions({
    name: 'FaqsPage'
  })

  const faqsStore = useFaqsStore()
  const settingsStore = useSettingsStore()
  const siteContent = useSiteContent('faqs')
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
    await siteContent.fetchContent()
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
      filtered = filtered.filter(f => {
        const categoryId = typeof f.category === 'object' ? f.category?.id : f.category
        return categoryId == selectedCategory.value
      })
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

<style scoped>
/* Hero Banner */
.hero-banner {
  position: relative;
  background: linear-gradient(135deg, rgb(var(--color-secondary)) 0%, rgb(var(--color-primary-dark)) 100%);
  min-height: clamp(200px, 25vh, 300px);
  display: flex;
  align-items: center;
  overflow: hidden;
  margin-top: 0;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800"><defs><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1"/></pattern></defs><rect width="1200" height="800" fill="url(%23grid)"/></svg>');
  opacity: 0.5;
}

.hero-content-wrapper {
  position: relative;
  z-index: 2;
  padding: clamp(1.25rem, 3vh, 2.5rem) 0;
}

.hero-text {
  text-align: center;
  margin-bottom: clamp(0.75rem, 2vw, 1rem);
}

.hero-title {
  font-size: clamp(1rem, 2vw, 1.75rem);
  font-weight: 900;
  color: white;
  margin-bottom: 0.375rem;
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.text-accent-yellow {
  color: rgb(var(--color-accent-yellow));
}

.hero-subtitle {
  font-size: clamp(0.75rem, 0.9vw, 0.875rem);
  color: rgba(255, 255, 255, 0.85);
  font-weight: 400;
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.4;
  padding: 0 1rem;
}

/* Hide scrollbar for category filter */
.hide-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.hide-scrollbar::-webkit-scrollbar {
  display: none;
}

/* Fade in animation */
.animate-fade-in {
  animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
