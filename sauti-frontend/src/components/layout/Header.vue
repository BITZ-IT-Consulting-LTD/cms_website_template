<template>
  <header class="bg-white/90 backdrop-blur sticky top-0 z-50 border-b border-gray-100">
    <nav class="container-custom py-3">
      <div class="flex items-center justify-between min-h-[64px]">
        <!-- Logo -->
        <router-link to="/" class="flex items-center space-x-2">
          <template v-if="!useFallback">
            <img :src="logoUrl" alt="Sauti" class="h-8 w-8 object-contain" @error="useFallback = true" />
          </template>
          <template v-else>
            <div class="h-8 w-8 rounded-full bg-secondary-500 flex items-center justify-center text-white font-bold">S</div>
          </template>
          <div>
            <h1 class="text-lg md:text-xl font-bold text-gray-900">Sauti.</h1>
          </div>
        </router-link>

        <!-- Desktop Navigation (aligned with provided design) -->
        <div class="hidden lg:flex flex-1 items-center justify-center gap-8 xl:gap-10 whitespace-nowrap">
          <router-link to="/" class="text-gray-700 hover:text-gray-900 px-2 py-1 rounded-full hover:bg-gray-100">Home</router-link>
          <router-link to="/about" class="text-gray-700 hover:text-gray-900 px-2 py-1 rounded-full hover:bg-gray-100">About</router-link>
          <router-link to="/operations" class="text-gray-700 hover:text-gray-900 px-2 py-1 rounded-full hover:bg-gray-100">Services</router-link>
          <router-link to="/blog" class="text-gray-700 hover:text-gray-900 px-2 py-1 rounded-full hover:bg-gray-100">Blogs</router-link>
          <router-link to="/videos" class="text-gray-700 hover:text-gray-900 px-2 py-1 rounded-full hover:bg-gray-100">Videos</router-link>
          <router-link to="/resources" class="text-gray-700 hover:text-gray-900 px-2 py-1 rounded-full hover:bg-gray-100">Resources</router-link>
          <router-link to="/contact" class="text-gray-700 hover:text-gray-900 px-2 py-1 rounded-full hover:bg-gray-100">Contact</router-link>
        </div>

        <!-- Right Actions -->
        <div class="hidden lg:flex items-center gap-3 whitespace-nowrap shrink-0">
          <a href="#" class="inline-flex items-center rounded-full bg-orange-500 px-4 py-2 text-white font-semibold hover:bg-orange-600 transition-colors">Donate</a>
          <a href="tel:116" class="inline-flex items-center rounded-full border border-gray-300 px-4 py-2 text-gray-800 font-semibold hover:bg-gray-100 transition-colors">Call Helpline</a>
        </div>

        <!-- Mobile Menu Button -->
        <button
          @click="mobileMenuOpen = !mobileMenuOpen"
          class="lg:hidden p-2 text-gray-700 hover:text-primary-600"
          aria-label="Toggle menu"
        >
          <svg v-if="!mobileMenuOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
          <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- Mobile Menu -->
      <Transition name="slide">
        <div v-if="mobileMenuOpen" class="lg:hidden mt-4 pb-4 space-y-3">
          <!-- Primary pages in required order -->
          <router-link to="/" class="block py-2 text-gray-700 hover:text-gray-900" @click="mobileMenuOpen = false">Home</router-link>
          <router-link to="/about" class="block py-2 text-gray-700 hover:text-gray-900" @click="mobileMenuOpen = false">About</router-link>
          <router-link to="/operations" class="block py-2 text-gray-700 hover:text-gray-900" @click="mobileMenuOpen = false">Services</router-link>
          <router-link to="/blog" class="block py-2 text-gray-700 hover:text-gray-900" @click="mobileMenuOpen = false">Blogs</router-link>
          <router-link to="/videos" class="block py-2 text-gray-700 hover:text-gray-900" @click="mobileMenuOpen = false">Videos</router-link>
          <router-link to="/resources" class="block py-2 text-gray-700 hover:text-gray-900" @click="mobileMenuOpen = false">Resources</router-link>
          <router-link to="/contact" class="block py-2 text-gray-700 hover:text-gray-900" @click="mobileMenuOpen = false">Contact</router-link>

          <div class="pt-3 border-t border-gray-200 grid grid-cols-2 gap-3">
            <a href="#" class="inline-flex items-center justify-center rounded-full bg-orange-500 px-4 py-2 text-white font-semibold hover:bg-orange-600 transition-colors">Donate</a>
            <a href="tel:116" class="inline-flex items-center justify-center rounded-full border border-gray-300 px-4 py-2 text-gray-800 font-semibold hover:bg-gray-100 transition-colors">Call Helpline</a>
          </div>
        </div>
      </Transition>
    </nav>
  </header>
</template>

<script setup>
import { ref } from 'vue'

const mobileMenuOpen = ref(false)
const useFallback = ref(false)
const logoUrl = new URL('@/assets/ug.svg', import.meta.url).href
</script>

<style scoped>
.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s ease;
}

.slide-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}

.slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
