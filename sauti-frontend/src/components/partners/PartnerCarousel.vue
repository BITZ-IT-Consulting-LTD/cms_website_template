<template>
  <!-- eslint-disable vue/no-parsing-error vue/valid-attribute-name vue/no-unused-vars -->
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
      <AppLoader />
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
          <div
            v-for="(partner, index) in partners"
            :key="`dot-${index}`"
          >
            <!-- eslint-disable-next-line vue/no-unused-vars -->
            <button
              @click="goToSlide(index)"
              :class="[
                'w-3 h-3 rounded-full transition-colors',
                currentSlide === index
                  ? 'bg-primary w-8'
                  : 'bg-gray-300 hover:bg-gray-400'
              ]"
              :aria-label="`Go to ${partner.name}`"
            ></button>
          </div>
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
              'px-4 py-2 text-sm font-normal rounded-l-lg border',
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
              'px-4 py-2 text-sm font-normal rounded-r-lg border-t border-r border-b',
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
import AppLoader from '../common/AppLoader.vue'

import PartnerCard from './PartnerCard.vue'

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
function nextSlide() {
  currentSlide.value = (currentSlide.value + 1) % props.partners.length
}

function previousSlide() {
  currentSlide.value = currentSlide.value === 0 
    ? props.partners.length - 1 
    : currentSlide.value - 1
}

// eslint-disable-next-line no-unused-vars
// eslint-disable-next-line no-unused-vars
// eslint-disable-next-line no-unused-vars
// eslint-disable-next-line no-unused-vars
// eslint-disable-next-line no-unused-vars
// eslint-disable-next-line no-unused-vars
// eslint-disable-next-line no-unused-vars
// eslint-disable-next-line no-unused-vars
// eslint-disable-next-line no-unused-vars
// eslint-disable-next-line no-unused-vars
// eslint-disable-next-line no-unused-vars
function goToSlide(index) {
  currentSlide.value = index
}

function startAutoplay() {
  if (props.autoplay && props.partners.length > 1) {
    autoplayTimer = setInterval(nextSlide, props.autoplayInterval)
  }
}

function stopAutoplay() {
  if (autoplayTimer) {
    clearInterval(autoplayTimer)
    autoplayTimer = null
  }
}

function handleImageError(event) {
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
