<template>
  <header
    class="absolute top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md shadow-sm transition-all duration-300">
    <!-- Skip link handled in App.vue for better first-element accessibility -->
    <nav class="w-full px-8 lg:px-12" aria-label="Main Navigation">
      <div class="flex items-center justify-between" style="height: clamp(60px, 5vw + 40px, 80px);">
        <!-- Text Brand Name - Hidden on Mobile -->
        <router-link to="/" class="hidden lg:flex items-center group no-underline shrink-0">
          <span class="text-xl lg:text-2xl font-black text-secondary tracking-tight">Sauti 116</span>
        </router-link>

        <!-- Desktop Navigation -->
        <div class="hidden lg:flex flex-1 items-center justify-center mx-4">
          <div class="flex items-center gap-4 xl:gap-6">
            <router-link v-for="link in [
              { to: '/', label: 'Home' },
              { to: '/about', label: 'Who We Are' },
              { to: '/operations', label: 'Operations' },
              { to: '/videos', label: 'Videos' },
              { to: '/blogs', label: 'Blogs' },
              { to: '/news', label: 'News' },
              { to: '/resources', label: 'Resources' },
              { to: '/faqs', label: 'FAQs' },
              { to: '/contact', label: 'Contact Us' }
            ]" :key="link.to" :to="link.to"
              class="text-neutral-black font-semibold transition-all duration-300 hover:text-primary relative py-2 after:absolute after:bottom-0 after:left-0 after:right-0 after:h-0.5 after:bg-primary after:scale-x-0 after:transition-transform after:duration-300 hover:after:scale-x-100 whitespace-nowrap text-sm"
              active-class="text-primary !after:scale-x-100">
              {{ link.label }}
            </router-link>
          </div>
        </div>

        <!-- Mobile Scrollable Navigation - Full Width -->
        <div class="flex lg:hidden flex-1 items-center overflow-x-auto hide-scrollbar -webkit-overflow-scrolling-touch" style="scrollbar-width: none;">
          <div class="flex items-center gap-3 py-2 px-1">
            <router-link v-for="link in [
              { to: '/', label: 'Home' },
              { to: '/about', label: 'Who We Are' },
              { to: '/operations', label: 'Operations' },
              { to: '/videos', label: 'Videos' },
              { to: '/blogs', label: 'Blogs' },
              { to: '/news', label: 'News' },
              { to: '/resources', label: 'Resources' },
              { to: '/faqs', label: 'FAQs' },
              { to: '/contact', label: 'Contact' }
            ]" :key="link.to" :to="link.to"
              class="text-neutral-black font-semibold transition-all duration-300 hover:text-primary px-3 py-2 rounded-lg whitespace-nowrap text-sm flex-shrink-0"
              active-class="text-primary bg-primary/10">
              {{ link.label }}
            </router-link>
          </div>
        </div>

        <!-- Right Actions -->
        <div class="hidden lg:flex items-center gap-2 xl:gap-3 shrink-0">
          <!-- Call Button -->
          <BaseCTA :href="`tel:${settings.hotline_number || '116'}`" variant="emergency" external
            class="!rounded-full !px-4 xl:!px-6 !py-2.5 shadow-lg hover:shadow-xl gap-2 !border-0 flex items-center group"
            aria-label="Call Emergency Helpline 116">
            <Phone class="w-4 h-4 text-white group-hover:rotate-12 transition-transform" stroke-width="2.5" />
            <span class="text-xs xl:text-sm font-bold whitespace-nowrap">Call 116</span>
          </BaseCTA>

          <!-- Report Button -->
          <BaseCTA to="/report" variant="primary"
            class="!rounded-full !px-4 xl:!px-6 !py-2.5 !text-xs xl:!text-sm !font-bold !bg-[#006837] hover:!bg-[#005529] !border-0 text-white shadow-lg hover:shadow-xl whitespace-nowrap">
            Report a case
          </BaseCTA>
        </div>

      </div>
    </nav>
  </header>
</template>

<script setup>
  import { ref, computed, onMounted, onUnmounted } from 'vue'
  import { useSettingsStore } from '@/store/settings'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import BaseLogo from '@/components/common/BaseLogo.vue'
  import {
    Phone,
    Menu,
    X,
    ArrowRight,
    ShieldCheck
  } from 'lucide-vue-next'

  const settingsStore = useSettingsStore()
  const mobileMenuOpen = ref(false)

  const settings = computed(() => settingsStore.settings)
  const orgProfile = computed(() => settingsStore.orgProfile)

  const filteredOrgName = computed(() => {
    const name = orgProfile.value?.name || settings.value.site_name || 'Sauti 116'
    // Remove "National" and "Child" to follow streamlined branding if preferred,
    // but definitely "National" as per user request
    return name.replace(/National/gi, '').trim()
  })

  // Calculate header height dynamically for mobile menu positioning
  const updateHeaderHeight = () => {
    const header = document.querySelector('header')
    if (header) {
      document.documentElement.style.setProperty('--header-height', `${header.offsetHeight}px`)
    }
  }

  onMounted(() => {
    updateHeaderHeight()
    window.addEventListener('resize', updateHeaderHeight)
  })

  onUnmounted(() => {
    window.removeEventListener('resize', updateHeaderHeight)
  })
</script>

<style scoped></style>
