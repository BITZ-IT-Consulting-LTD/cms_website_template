<template>
  <div class="space-y-6">
    <!-- Section Header -->
    <div class="text-center mb-8">
      <h2 class="text-3xl font-bold text-gray-900 mb-3">Our Partners</h2>
      <p class="text-gray-600 max-w-2xl mx-auto">
        Working together with these amazing organizations to protect and support vulnerable communities.
      </p>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="text-center py-12">
      <Loader />
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="bg-red-50 border border-red-200 rounded-lg p-6 text-center">
      <p class="text-red-700">{{ error }}</p>
    </div>

    <!-- Empty State -->
    <div v-else-if="partners.length === 0" class="bg-gray-50 border border-gray-200 rounded-lg p-12 text-center">
      <svg class="w-16 h-16 mx-auto text-gray-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
      </svg>
      <h3 class="text-lg font-semibold text-gray-700 mb-2">No Partners Yet</h3>
      <p class="text-gray-500">Check back soon for partner organizations.</p>
    </div>

    <!-- Partners Carousel -->
    <div v-else class="relative">
      <!-- Manual Carousel (No external library) -->
      <div v-if="displayMode === 'carousel'" class="relative overflow-hidden">
        <!-- Carousel Track -->
        <div class="flex transition-transform duration-500 ease-in-out"
             :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
          <div
            v-for="(partner, index) in partners"
            :key="partner.slug"
            class="flex-shrink-0 w-full px-4"
          >
            <PartnerCard :partner="partner" />
          </div>
        </div>

        <!-- Navigation Buttons -->
        <button
          v-if="partners.length > 1"
          @click="previousSlide"
          class="absolute left-0 top-1/2 -translate-y-1/2 -translate-x-4 w-12 h-12 bg-white rounded-full shadow-lg flex items-center justify-center hover:bg-gray-50 transition-colors z-10"
          aria-label="Previous partner"
        >
          <svg class="w-6 h-6 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
        </button>

        <button
          v-if="partners.length > 1"
          @click="nextSlide"
          class="absolute right-0 top-1/2 -translate-y-1/2 translate-x-4 w-12 h-12 bg-white rounded-full shadow-lg flex items-center justify-center hover:bg-gray-50 transition-colors z-10"
          aria-label="Next partner"
        >
          <svg class="w-6 h-6 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </button>

        <!-- Dots Indicator -->
        <div v-if="partners.length > 1" class="flex justify-center mt-6 space-x-2">
          <button
            v-for="(partner, index) in partners"
            :key="`dot-${index}`"
            @click="goToSlide(index)"
            :class="[
              'w-3 h-3 rounded-full transition-all',
              currentSlide === index
                ? 'bg-primary w-8'
                : 'bg-gray-300 hover:bg-gray-400'
            ]"
            :aria-label="`Go to ${partner.name}`"
          />
        </div>
      </div>

      <!-- Grid Display -->
      <div v-else class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        <div
          v-for="partner in partners"
          :key="partner.slug"
          class="bg-white rounded-lg shadow-md p-6 flex items-center justify-center hover:shadow-lg transition-shadow group"
        >
          <a
            v-if="partner.website"
            :href="partner.website"
            target="_blank"
            rel="noopener noreferrer"
            class="block"
            :aria-label="`Visit ${partner.name} website`"
          >
            <img
              v-if="partner.logo"
              :src="partner.logo"
              :alt="partner.name"
              class="max-h-20 w-auto mx-auto grayscale group-hover:grayscale-0 transition-all"
              @error="handleImageError"
            />
            <p v-else class="text-sm font-semibold text-gray-700 text-center">
              {{ partner.name }}
            </p>
          </a>
          <div v-else>
            <img
              v-if="partner.logo"
              :src="partner.logo"
              :alt="partner.name"
              class="max-h-20 w-auto mx-auto"
              @error="handleImageError"
            />
            <p v-else class="text-sm font-semibold text-gray-700 text-center">
              {{ partner.name }}
            </p>
          </div>
        </div>
      </div>

      <!-- Display Mode Toggle -->
      <div class="flex justify-center mt-8">
        <div class="inline-flex rounded-lg shadow-sm" role="group">
          <button
            @click="displayMode = 'carousel'"
            :class="[
              'px-4 py-2 text-sm font-medium rounded-l-lg border',
              displayMode === 'carousel'
                ? 'bg-primary text-white border-primary'
                : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
            ]"
          >
            <svg class="w-5 h-5 inline mr-1" fill="currentColor" viewBox="0 0 20 20">
              <path d="M2 6a2 2 0 012-2h12a2 2 0 012 2v2a2 2 0 01-2 2H4a2 2 0 01-2-2V6zM14 16a2 2 0 002-2v-2a2 2 0 00-2-2h-2v6h2zM6 16a2 2 0 01-2-2v-2a2 2 0 012-2h2v6H6z" />
            </svg>
            Carousel
          </button>
          <button
            @click="displayMode = 'grid'"
            :class="[
              'px-4 py-2 text-sm font-medium rounded-r-lg border-t border-r border-b',
              displayMode === 'grid'
                ? 'bg-primary text-white border-primary'
                : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
            ]"
          >
            <svg class="w-5 h-5 inline mr-1" fill="currentColor" viewBox="0 0 20 20">
              <path d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
            </svg>
            Grid
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import Loader from '../common/Loader.vue'

// We'll create a simple PartnerCard component inline since it's straightforward
const PartnerCard = {
  name: 'PartnerCard',
  props: {
    partner: {
      type: Object,
      required: true
    }
  },
  template: `
    <div class="bg-white rounded-lg shadow-lg overflow-hidden">
      <!-- Logo -->
      <div class="h-48 bg-gray-100 flex items-center justify-center p-8">
        <img
          v-if="partner.logo"
          :src="partner.logo"
          :alt="partner.name"
          class="max-h-full max-w-full object-contain"
          @error="handleImageError"
        />
        <div v-else class="text-center">
          <svg class="w-20 h-20 mx-auto text-gray-400" fill="currentColor" viewBox="0 0 20 20">
            <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z" />
          </svg>
        </div>
      </div>

      <!-- Content -->
      <div class="p-6">
        <h3 class="text-xl font-bold text-gray-900 mb-2">
          {{ partner.name }}
        </h3>

        <p v-if="partner.description" class="text-gray-600 text-sm mb-4 line-clamp-3">
          {{ partner.description }}
        </p>

        <!-- Partner Type Badge -->
        <span v-if="partner.partner_type" class="inline-block px-3 py-1 text-xs font-semibold bg-blue-100 text-blue-700 rounded-full mb-4">
          {{ partner.partner_type }}
        </span>

        <!-- Contact Information -->
        <div class="space-y-2 text-sm">
          <a
            v-if="partner.website"
            :href="partner.website"
            target="_blank"
            rel="noopener noreferrer"
            class="flex items-center text-primary hover:text-blue-600 transition-colors"
          >
            <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z" clip-rule="evenodd" />
            </svg>
            Visit Website
          </a>

          <a
            v-if="partner.email"
            :href="'mailto:' + partner.email"
            class="flex items-center text-gray-600 hover:text-gray-900 transition-colors"
          >
            <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
              <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
              <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
            </svg>
            {{ partner.email }}
          </a>

          <a
            v-if="partner.phone"
            :href="'tel:' + partner.phone"
            class="flex items-center text-gray-600 hover:text-gray-900 transition-colors"
          >
            <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
              <path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z" />
            </svg>
            {{ partner.phone }}
          </a>
        </div>
      </div>
    </div>
  `,
  methods: {
    handleImageError(event) {
      event.target.style.display = 'none'
    }
  }
}

const props = defineProps({
  partners: {
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
  },
  autoplay: {
    type: Boolean,
    default: true
  },
  autoplayInterval: {
    type: Number,
    default: 5000
  }
})

// State
const currentSlide = ref(0)
const displayMode = ref('carousel')
let autoplayTimer = null

// Methods
const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % props.partners.length
}

const previousSlide = () => {
  currentSlide.value = currentSlide.value === 0 
    ? props.partners.length - 1 
    : currentSlide.value - 1
}

const goToSlide = (index) => {
  currentSlide.value = index
}

const startAutoplay = () => {
  if (props.autoplay && props.partners.length > 1) {
    autoplayTimer = setInterval(nextSlide, props.autoplayInterval)
  }
}

const stopAutoplay = () => {
  if (autoplayTimer) {
    clearInterval(autoplayTimer)
    autoplayTimer = null
  }
}

const handleImageError = (event) => {
  event.target.style.display = 'none'
}

// Lifecycle
onMounted(() => {
  startAutoplay()
})

onUnmounted(() => {
  stopAutoplay()
})
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.grayscale {
  filter: grayscale(100%);
}

.grayscale-0 {
  filter: grayscale(0%);
}
</style>
