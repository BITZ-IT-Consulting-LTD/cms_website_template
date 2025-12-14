<template>
  <div class="space-y-6">
    <!-- Category Filter -->
    <div v-if="categories && categories.length > 0" class="bg-white rounded-lg shadow-md p-6">
      <h2 class="text-lg font-bold text-gray-900 mb-4">Filter by Category</h2>
      <div class="flex flex-wrap gap-2">
        <button
          @click="selectCategory(null)"
          :class="[
            'px-4 py-2 rounded-full text-sm font-semibold transition-colors',
            selectedCategory === null
              ? 'bg-purple-500 text-white'
              : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
          ]"
        >
          All FAQs
        </button>
        <button
          v-for="cat in categories"
          :key="cat.slug"
          @click="selectCategory(cat.slug)"
          :class="[
            'px-4 py-2 rounded-full text-sm font-semibold transition-colors',
            selectedCategory === cat.slug
              ? 'bg-purple-500 text-white'
              : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
          ]"
        >
          {{ cat.name }}
        </button>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="text-center py-12">
      <AppLoader />
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="bg-red-50 border border-red-200 rounded-lg p-6 text-center">
      <p class="text-red-700">{{ error }}</p>
      <button @click="$emit('retry')" class="mt-4 btn-primary">
        Try Again
      </button>
    </div>

    <!-- Empty State -->
    <div v-else-if="filteredFaqs.length === 0" class="bg-gray-50 border border-gray-200 rounded-lg p-12 text-center">
      <svg class="w-16 h-16 mx-auto text-gray-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
      <h3 class="text-lg font-semibold text-gray-700 mb-2">No FAQs Found</h3>
      <p class="text-gray-500">
        {{ selectedCategory ? 'No FAQs in this category.' : 'Check back later for frequently asked questions.' }}
      </p>
    </div>

    <!-- FAQ Accordion -->
    <div v-else class="space-y-3">
      <div
        v-for="(faq, index) in filteredFaqs"
        :key="faq.id"
        class="bg-white rounded-lg shadow-md overflow-hidden transition-all duration-300"
        :class="{ 'ring-2 ring-purple-500': openIndex === index }"
      >
        <!-- Question (Toggle Button) -->
        <button
          @click="toggleFaq(index)"
          class="w-full px-6 py-4 text-left flex items-center justify-between hover:bg-gray-50 transition-colors focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-inset"
          :aria-expanded="openIndex === index"
          :aria-controls="`faq-answer-${faq.id}`"
        >
          <div class="flex-1 pr-4">
            <!-- Category Badge -->
            <span
              v-if="faq.category && !selectedCategory"
              class="inline-block px-2 py-1 text-xs font-semibold bg-purple-100 text-purple-700 rounded-full mb-2"
            >
              {{ faq.category.name }}
            </span>

            <!-- Question -->
            <h3 class="text-lg font-semibold text-gray-900">
              {{ faq.question }}
            </h3>

            <!-- Language Badge -->
            <span
              v-if="faq.language"
              class="inline-block mt-2 px-2 py-1 text-xs font-medium bg-gray-100 text-gray-600 rounded-full"
            >
              {{ getLanguageName(faq.language) }}
            </span>
          </div>

          <!-- Toggle Icon -->
          <div class="flex-shrink-0">
            <svg
              :class="[
                'w-6 h-6 text-purple-500 transition-transform duration-300',
                { 'transform rotate-180': openIndex === index }
              ]"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </div>
        </button>

        <!-- Answer (Collapsible) -->
        <transition
          name="accordion"
          @enter="enter"
          @leave="leave"
        >
          <div
            v-show="openIndex === index"
            :id="`faq-answer-${faq.id}`"
            class="px-6 pb-6"
          >
            <div class="pt-4 border-t border-gray-200">
              <p class="text-gray-700 leading-relaxed whitespace-pre-line">
                {{ faq.answer }}
              </p>

              <!-- Views Count -->
              <div v-if="faq.views_count" class="mt-4 flex items-center text-sm text-gray-500">
                <svg class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M10 12a2 2 0 100-4 2 2 0 000 4z" />
                  <path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd" />
                </svg>
                Viewed {{ faq.views_count }} times
              </div>
            </div>
          </div>
        </transition>
      </div>
    </div>

    <!-- Help Contact Section -->
    <div class="bg-purple-50 border-2 border-purple-200 rounded-lg p-6 mt-8">
      <div class="flex items-start space-x-4">
        <div class="flex-shrink-0">
          <svg class="w-8 h-8 text-purple-500" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" />
          </svg>
        </div>
        <div class="flex-1">
          <h3 class="text-lg font-bold text-gray-900 mb-2">Didn't find your answer?</h3>
          <p class="text-gray-600 mb-4">Our team is here to help you. Contact us through any of these channels:</p>
          <div class="flex flex-wrap gap-3">
            <a href="tel:116" class="btn-primary">
              Call 116
            </a>
            <router-link to="/contact" class="btn-secondary">
              Contact Us
            </router-link>
            <router-link to="/report" class="btn-secondary">
              Report a Case
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import AppLoader from '../common/AppLoader.vue'

const props = defineProps({
  faqs: {
    type: Array,
    default: () => []
  },
  categories: {
    type: Array,
    default: () => []
  },
  loading: {
    type: Boolean,
    default: false
  },
  error: {
    type: String,
    default: null
  }
})

const emit = defineEmits(['retry', 'view'])

// State
const openIndex = ref(null)
const selectedCategory = ref(null)

// Computed
const filteredFaqs = computed(() => {
  if (!selectedCategory.value) return props.faqs
  
  return props.faqs.filter(faq => 
    faq.category && faq.category.slug === selectedCategory.value
  )
})

// Methods
const toggleFaq = (index) => {
  if (openIndex.value === index) {
    openIndex.value = null
  } else {
    openIndex.value = index
    // Emit view event for tracking
    emit('view', filteredFaqs.value[index])
  }
}

const selectCategory = (categorySlug) => {
  selectedCategory.value = categorySlug
  openIndex.value = null // Close any open FAQ when changing category
}

const getLanguageName = (code) => {
  const languages = {
    en: 'English',
    lg: 'Luganda',
    sw: 'Swahili'
  }
  return languages[code] || code
}

// Accordion animation methods
const enter = (element) => {
  element.style.height = '0'
  element.style.overflow = 'hidden'
  
  requestAnimationFrame(() => {
    element.style.height = element.scrollHeight + 'px'
    element.style.transition = 'height 0.3s ease'
  })
}

const leave = (element) => {
  element.style.height = element.scrollHeight + 'px'
  element.style.overflow = 'hidden'
  
  requestAnimationFrame(() => {
    element.style.height = '0'
    element.style.transition = 'height 0.3s ease'
  })
}
</script>

<style scoped>
.accordion-enter-active,
.accordion-leave-active {
  overflow: hidden;
}

.whitespace-pre-line {
  white-space: pre-line;
}
</style>
