<template>
  <header class="bg-white backdrop-blur-md sticky top-0 z-50 shadow-sm">
    <nav class="container-custom py-4">
      <div class="flex items-center justify-between min-h-[72px]">
        <!-- Enhanced Logo -->
        <router-link to="/" class="flex items-center space-x-3 group no-underline">
          <template v-if="!useFallback">
            <img :src="settingsStore.settings.logo || logoUrl" alt="Sauti" class="h-16 w-16 object-contain group-hover:scale-110 transition-transform duration-300" @error="useFallback = true" />
          </template>
          <template v-else>
            <div class="h-16 w-16 rounded-2xl flex items-center justify-center text-white font-bold text-2xl group-hover:scale-110 transition-transform duration-300" style="background-color: #009EDB;">S</div>
          </template>
          <div>
            <h1 class="text-xl md:text-2xl font-bold group-hover:text-[#009EDB] transition-colors duration-300" style="font-family: 'Poppins', sans-serif; color: #222222;">
              {{ settings.site_name }}
            </h1>
            <p class="text-xs -mt-1" style="color: #555555;">116 helpline</p>
          </div>
        </router-link>

        <!-- Enhanced Desktop Navigation -->
        <div class="hidden lg:flex flex-1 items-center justify-center gap-2 xl:gap-4 whitespace-nowrap">
          <router-link to="/" class="nav-link" :class="{ 'nav-link-active': $route.path === '/' }">Home</router-link>
          <router-link to="/about" class="nav-link" :class="{ 'nav-link-active': $route.path === '/about' }">About</router-link>
          
          <router-link to="/operations" class="nav-link" :class="{ 'nav-link-active': $route.path === '/operations' }">Services</router-link>
          <router-link to="/resources" class="nav-link" :class="{ 'nav-link-active': $route.path === '/resources' }">Reports & Resources</router-link>
          <router-link to="/blogs" class="nav-link" :class="{ active: $route.path === '/blogs' }">Blogs</router-link>
          <router-link to="/videos" class="nav-link" :class="{ 'nav-link-active': $route.path === '/videos' }">Videos</router-link>
          <router-link to="/faqs" class="nav-link" :class="{ 'nav-link-active': $route.path === '/faqs' }">FAQs</router-link>
          <router-link to="/contact" class="nav-link" :class="{ 'nav-link-active': $route.path === '/contact' }">Contact</router-link>
        </div>

        <!-- Enhanced Right Actions -->
        <div class="hidden lg:flex items-center gap-4 whitespace-nowrap shrink-0">
          <a :href="`tel:${contactPhone}`" class="btn-emergency text-sm px-6 py-3 flex items-center gap-2">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
            </svg>
            <span>Call {{ contactPhone }}</span>
          </a>
        </div>

        <!-- Enhanced Mobile Menu Button -->
        <button
          @click="mobileMenuOpen = !mobileMenuOpen"
          class="lg:hidden p-3 text-gray-700 hover:text-blue-600 hover:bg-gray-100 rounded-xl transition-all duration-300"
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

      <!-- Enhanced Mobile Menu -->
      <Transition name="slide">
        <div v-if="mobileMenuOpen" class="lg:hidden mt-6 pb-6 bg-gray-50 rounded-2xl p-6 space-y-4">
          <!-- Primary pages in required order -->
          <router-link 
            to="/" 
            class="mobile-nav-link" 
            :class="{ 'mobile-nav-link-active': $route.path === '/' }"
            @click="mobileMenuOpen = false"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg>
            Home
          </router-link>
          
          <router-link 
            to="/about" 
            class="mobile-nav-link" 
            :class="{ 'mobile-nav-link-active': $route.path === '/about' }"
            @click="mobileMenuOpen = false"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            About
          </router-link>
          

          
          <router-link
            to="/operations"
            class="mobile-nav-link"
            :class="{ 'mobile-nav-link-active': $route.path === '/operations' }"
            @click="mobileMenuOpen = false"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
            </svg>
            Services
          </router-link>

          <router-link
            to="/resources"
            class="mobile-nav-link"
            :class="{ 'mobile-nav-link-active': $route.path === '/resources' }"
            @click="mobileMenuOpen = false"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
            </svg>
            Reports & Resources
          </router-link>

          <router-link
            to="/blogs"
            class="mobile-nav-link"
            :class="{ 'mobile-nav-link-active': $route.path === '/blogs' }"
            @click="mobileMenuOpen = false"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z" />
            </svg>
            Blogs
          </router-link>

          <router-link
            to="/videos"
            class="mobile-nav-link"
            :class="{ 'mobile-nav-link-active': $route.path === '/videos' }"
            @click="mobileMenuOpen = false"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
            </svg>
            Videos
          </router-link>
          
          <router-link 
            to="/faqs" 
            class="mobile-nav-link" 
            :class="{ 'mobile-nav-link-active': $route.path === '/faqs' }"
            @click="mobileMenuOpen = false"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            FAQs
          </router-link>
          
          <router-link 
            to="/contact" 
            class="mobile-nav-link" 
            :class="{ 'mobile-nav-link-active': $route.path === '/contact' }"
            @click="mobileMenuOpen = false"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
            Contact
          </router-link>

          <!-- Mobile CTA Buttons -->
          <div class="pt-6">
            <a :href="`tel:${contactPhone}`" class="w-full btn-emergency text-center justify-center flex items-center gap-2">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
              </svg>
              <span>Call {{ contactPhone }}</span>
            </a>
          </div>
        </div>
      </Transition>
    </nav>
  </header>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useContentStore } from '@/store/content'
import { useSettingsStore } from '@/store/settings'

const contentStore = useContentStore()
const settingsStore = useSettingsStore()
const mobileMenuOpen = ref(false)
const useFallback = ref(false)
const logoUrl = new URL('@/assets/sauti-logo.jpeg', import.meta.url).href

const contactPhone = computed(() => contentStore.getContent('contact_phone_main', '116'))
const settings = computed(() => settingsStore.settings)

onMounted(() => {
  contentStore.fetchContent()
  settingsStore.fetchSettings()
})
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
