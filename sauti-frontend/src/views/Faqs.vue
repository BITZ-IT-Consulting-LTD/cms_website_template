<template>
  <div class="bg-gradient-to-br from-[#FFF8DC] via-white to-[#F5F5DC] py-16">
    <div class="container-custom">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        <!-- Left visuals -->
        <div class="lg:col-span-5 order-2 lg:order-1 space-y-5">
          <!-- Hero image -->
          <div class="rounded-3xl bg-gradient-to-br from-[#8B4000] to-[#A0522D] h-72 flex items-center justify-center">
            <div class="text-center text-white">
              <svg class="w-16 h-16 mx-auto mb-4" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
              </svg>
              <h3 class="text-xl font-bold">{{ faqsSupportTitle }}</h3>
              <p class="text-sm opacity-90">{{ faqsSupportSubtitle }}</p>
            </div>
          </div>
          
          <!-- Info cards -->
          <div class="rounded-3xl bg-white shadow-lg p-6 border border-gray-100">
            <div class="flex items-center gap-4 mb-4">
              <div class="h-12 w-12 rounded-full bg-[#8B4000] text-white flex items-center justify-center">
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                </svg>
              </div>
              <div>
                <h4 class="font-semibold text-gray-900">{{ faqsQuickResponseTitle }}</h4>
                <p class="text-gray-600 text-sm">{{ faqsQuickResponseSubtitle }}</p>
              </div>
            </div>
            <p class="text-gray-600 text-sm">{{ faqsQuickResponseText }}</p>
          </div>

          <!-- Contact card -->
          <div class="rounded-3xl bg-gradient-to-r from-[#8B4000] to-[#A0522D] p-6 text-white">
            <h4 class="font-bold text-lg mb-2">{{ faqsImmediateHelpTitle }}</h4>
            <p class="text-sm opacity-90 mb-4">{{ faqsImmediateHelpSubtitle }}</p>
            <a href="tel:116" class="btn-emergency inline-flex items-center gap-2">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/>
              </svg>
              {{ faqsCallButton }}
            </a>
          </div>
        </div>

        <!-- Right content -->
        <div class="lg:col-span-7 order-1 lg:order-2">
          <p class="text-sm uppercase tracking-widest text-[#8B4000] font-semibold">{{ faqsPageTitle }}</p>
          <h1 class="text-4xl md:text-5xl font-extrabold leading-tight bg-gradient-to-r from-[#8B4000] to-[#A0522D] bg-clip-text text-transparent mt-2">{{ faqsPageSubtitle }}</h1>

          <!-- Search -->
          <div class="mt-8 mb-4">
            <div class="relative">
              <input v-model="query" type="text" :placeholder="faqsSearchPlaceholder" class="w-full px-5 py-4 rounded-2xl border border-gray-200 bg-white shadow-sm pl-12 focus:ring-2 focus:ring-primary-500 focus:border-primary-500" />
              <svg class="w-5 h-5 text-gray-400 absolute left-4 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35M10 18a8 8 0 100-16 8 8 0 000 16z"/></svg>
            </div>
          </div>

          <Loader v-if="loading" />

          <!-- FAQ Categories and Accordion -->
          <div v-else>
            <!-- Category Filter -->
            <div v-if="categories.length" class="mb-6">
              <div class="flex flex-wrap gap-2">
                <button 
                  @click="selectedCategory = ''"
                  :class="selectedCategory === '' ? 'bg-[#8B4000] text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'"
                  class="px-4 py-2 rounded-full text-sm font-medium transition-colors"
                >
                  {{ faqsAllCategoriesButton }}
                </button>
                <button 
                  v-for="category in categories" 
                  :key="category.id"
                  @click="selectedCategory = category.id"
                  :class="selectedCategory === category.id ? 'bg-[#8B4000] text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'"
                  class="px-4 py-2 rounded-full text-sm font-medium transition-colors"
                >
                  {{ category.name }}
                </button>
              </div>
            </div>

            <!-- FAQ List -->
            <div v-if="filteredFaqs.length" class="space-y-4">
              <div
                v-for="(faq, index) in filteredFaqs"
                :key="faq.id || index"
                class="rounded-2xl border border-gray-200 bg-white shadow-sm overflow-hidden hover:shadow-md transition-shadow"
              >
                <button @click="toggleFaq(index)" class="w-full text-left px-6 py-5 flex justify-between items-center hover:bg-gray-50 transition-colors">
                  <div class="flex-1">
                    <span class="font-semibold text-gray-900 block">{{ faq.question }}</span>
                    <span v-if="faq.category_name" class="text-xs text-[#8B4000] font-medium mt-1">{{ faq.category_name }}</span>
                  </div>
                  <span class="inline-flex h-9 w-9 items-center justify-center rounded-full bg-[#8B4000] bg-opacity-10 text-[#8B4000] ml-4 flex-shrink-0">
                    <svg class="w-5 h-5 transition-transform" :class="{ 'rotate-180': openFaq === index }" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                  </span>
                </button>
                <Transition name="fade">
                  <div v-if="openFaq === index" class="px-6 pb-6 text-gray-600 border-t border-gray-100">
                    <div class="pt-4">{{ faq.answer }}</div>
                  </div>
                </Transition>
              </div>
            </div>
            <div v-else class="text-center py-12">
              <svg class="w-16 h-16 mx-auto text-gray-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <p class="text-gray-600 text-lg">{{ faqsNoResults }}</p>
              <p class="text-gray-500 text-sm mt-2">{{ faqsNoResultsSubtitle }}</p>
            </div>
          </div>

          <!-- Footer links -->
          <div class="text-sm text-gray-500 mt-10">
            <router-link to="/privacy" class="hover:text-gray-700">{{ faqsPrivacyPolicy }}</router-link>
            <span class="mx-2">•</span>
            <router-link to="/terms" class="hover:text-gray-700">{{ faqsTermsOfService }}</router-link>
            <span class="mx-2">•</span>
            <router-link to="/contact" class="hover:text-gray-700">{{ faqsContactUs }}</router-link>
            <p class="mt-2">{{ faqsFooterText }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useFaqsStore } from '@/store/faqs'
import Loader from '@/components/common/Loader.vue'
import { useContentStore } from '@/store/content'

const faqsStore = useFaqsStore()
const contentStore = useContentStore()
const faqs = ref([])
const categories = ref([])
const loading = ref(true)
const openFaq = ref(null)
const query = ref('')
const selectedCategory = ref('')

// Computed properties for content
const faqsSupportTitle = computed(() => contentStore.getContent('faqs_support_title', '24/7 Support'))
const faqsSupportSubtitle = computed(() => contentStore.getContent('faqs_support_subtitle', 'Always here to help'))
const faqsQuickResponseTitle = computed(() => contentStore.getContent('faqs_quick_response_title', 'Quick Response'))
const faqsQuickResponseSubtitle = computed(() => contentStore.getContent('faqs_quick_response_subtitle', 'Get help immediately'))
const faqsQuickResponseText = computed(() => contentStore.getContent('faqs_quick_response_text', 'Our trained counselors are available 24/7 to provide immediate support and guidance.'))
const faqsImmediateHelpTitle = computed(() => contentStore.getContent('faqs_immediate_help_title', 'Need Immediate Help?'))
const faqsImmediateHelpSubtitle = computed(() => contentStore.getContent('faqs_immediate_help_subtitle', 'Call our toll-free helpline'))
const faqsCallButton = computed(() => contentStore.getContent('faqs_call_button', 'Call 116'))
const faqsPageTitle = computed(() => contentStore.getContent('faqs_page_title', 'Frequently Asked'))
const faqsPageSubtitle = computed(() => contentStore.getContent('faqs_page_subtitle', 'Questions & Answers'))
const faqsSearchPlaceholder = computed(() => contentStore.getContent('faqs_search_placeholder', 'Search questions'))
const faqsAllCategoriesButton = computed(() => contentStore.getContent('faqs_all_categories_button', 'All Categories'))
const faqsNoResults = computed(() => contentStore.getContent('faqs_no_results', 'No FAQs found'))
const faqsNoResultsSubtitle = computed(() => contentStore.getContent('faqs_no_results_subtitle', 'Try adjusting your search or category filter'))
const faqsPrivacyPolicy = computed(() => contentStore.getContent('faqs_privacy_policy', 'Privacy Policy'))
const faqsTermsOfService = computed(() => contentStore.getContent('faqs_terms_of_service', 'Terms of Service'))
const faqsContactUs = computed(() => contentStore.getContent('faqs_contact_us', 'Contact Us'))
const faqsFooterText = computed(() => contentStore.getContent('faqs_footer_text', '© 2024 Sauti Uganda. All rights reserved. A sanctuary for every child.'))

onMounted(async () => {
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
