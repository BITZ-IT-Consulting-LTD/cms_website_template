<template>
  <header class="bg-sauti-white/90 backdrop-blur-xl sticky top-0 z-50 border-b border-sauti-neutral">
    <a href="#main-content"
      class="absolute top-0 left-0 -translate-y-full focus:translate-y-0 z-[100] bg-sauti-blue text-sauti-white px-4 py-2 font-bold transition-transform duration-300">
      Skip to main content
    </a>
    <nav class="container-custom py-4">
      <div class="flex items-center justify-between min-h-[72px]">
        <!-- Enhanced Logo -->
        <router-link to="/" class="flex items-center space-x-3 group no-underline shrink-0">
          <div
            class="h-14 w-14 rounded-2xl flex items-center justify-center overflow-hidden transition-all duration-500 hover:rotate-6 bg-sauti-white shadow-sm border border-sauti-neutral">
            <template v-if="settings.logo">
              <img :src="settings.logo" alt="Sauti Logo" class="h-full w-full object-contain" />
            </template>
          </div>
          <div>
            <h1
              class="text-xl md:text-2xl font-black tracking-tight group-hover:text-sauti-blue transition-colors duration-300 m-0 leading-tight text-sauti-darkGreen">
              {{ settings.site_name || 'Sauti 116' }}
            </h1>
            <p class="text-[10px] font-bold uppercase tracking-[0.2em] -mt-0.5 text-sauti-blue">National Helpline</p>
          </div>
        </router-link>

        <!-- Desktop Navigation -->
        <div class="hidden lg:flex flex-1 items-center justify-center gap-1 xl:gap-2">
          <router-link to="/" class="nav-link" :class="{ 'nav-link-active': $route.path === '/' }">Home</router-link>
          <router-link to="/about" class="nav-link" :class="{ 'nav-link-active': $route.path === '/about' }">About
            Us</router-link>

          <router-link to="/blogs" class="nav-link"
            :class="{ 'nav-link-active': $route.path === '/blogs' }">News</router-link>
          <router-link to="/videos" class="nav-link"
            :class="{ 'nav-link-active': $route.path === '/videos' }">Videos</router-link>
          <router-link to="/resources" class="nav-link"
            :class="{ 'nav-link-active': $route.path === '/resources' }">Resources</router-link>
          <router-link to="/faqs" class="nav-link"
            :class="{ 'nav-link-active': $route.path === '/faqs' }">FAQs</router-link>
          <router-link to="/contact" class="nav-link"
            :class="{ 'nav-link-active': $route.path === '/contact' }">Contact</router-link>
        </div>

        <!-- Right Actions -->
        <div class="hidden lg:flex items-center gap-4 shrink-0">
          <BaseCTA variant="emergency" :href="`tel:${settings.hotline_number || '116'}`" external class="group gap-2">
            <PhoneIcon class="w-5 h-5 group-hover:rotate-12 transition-transform" />
            <span class="font-bold">Call {{ settings.hotline_number || '116' }}</span>
          </BaseCTA>
          <BaseCTA to="/report">
            {{ settings.primary_cta_text || 'Report Case' }}
          </BaseCTA>
        </div>

        <!-- Mobile Menu Button -->
        <button @click="mobileMenuOpen = !mobileMenuOpen"
          class="lg:hidden p-3 text-sauti-darkGreen hover:bg-sauti-neutral rounded-2xl transition-all duration-300"
          aria-label="Toggle menu" :aria-expanded="mobileMenuOpen" aria-controls="mobile-menu">
          <Bars3Icon v-if="!mobileMenuOpen" class="w-7 h-7" />
          <XMarkIcon v-else class="w-7 h-7" />
        </button>
      </div>

      <!-- Mobile Menu -->
      <Transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 -translate-y-4"
        enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-200 ease-in"
        leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 -translate-y-4">
        <div v-if="mobileMenuOpen" id="mobile-menu"
          class="lg:hidden absolute left-0 right-0 top-[100%] bg-sauti-white border-b border-sauti-neutral shadow-2xl p-6 space-y-4 overflow-y-auto max-h-[calc(100vh-80px)]">
          <router-link to="/" class="mobile-nav-link" :class="{ 'mobile-nav-link-active': $route.path === '/' }"
            @click="mobileMenuOpen = false">Home</router-link>
          <router-link to="/about" class="mobile-nav-link"
            :class="{ 'mobile-nav-link-active': $route.path === '/about' }" @click="mobileMenuOpen = false">About
            Us</router-link>

          <router-link to="/blogs" class="mobile-nav-link"
            :class="{ 'mobile-nav-link-active': $route.path === '/blogs' }"
            @click="mobileMenuOpen = false">News</router-link>
          <router-link to="/videos" class="mobile-nav-link"
            :class="{ 'mobile-nav-link-active': $route.path === '/videos' }"
            @click="mobileMenuOpen = false">Videos</router-link>
          <router-link to="/resources" class="mobile-nav-link"
            :class="{ 'mobile-nav-link-active': $route.path === '/resources' }"
            @click="mobileMenuOpen = false">Resources</router-link>
          <router-link to="/faqs" class="mobile-nav-link" :class="{ 'mobile-nav-link-active': $route.path === '/faqs' }"
            @click="mobileMenuOpen = false">FAQs</router-link>
          <router-link to="/contact" class="mobile-nav-link"
            :class="{ 'mobile-nav-link-active': $route.path === '/contact' }"
            @click="mobileMenuOpen = false">Contact</router-link>

          <div class="pt-6 grid grid-cols-1 gap-4 border-t border-sauti-neutral">
            <BaseCTA variant="emergency" :href="`tel:${settings.hotline_number || '116'}`" external size="large"
              class="w-full justify-center gap-2">
              <PhoneIcon class="w-6 h-6" />
              <span class="text-lg">Call {{ settings.hotline_number || '116' }}</span>
            </BaseCTA>
            <BaseCTA to="/report" size="large" class="w-full justify-center text-lg" @click="mobileMenuOpen = false">
              {{ settings.primary_cta_text || 'Report Case' }}
            </BaseCTA>
          </div>
        </div>
      </Transition>
    </nav>
  </header>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue'
  import { useSettingsStore } from '@/store/settings'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import {
    PhoneIcon,
    Bars3Icon,
    XMarkIcon
  } from '@heroicons/vue/24/outline'

  const settingsStore = useSettingsStore()
  const mobileMenuOpen = ref(false)

  const settings = computed(() => settingsStore.settings)

  onMounted(async () => {
    await settingsStore.fetchGlobalSettings()
  })
</script>
