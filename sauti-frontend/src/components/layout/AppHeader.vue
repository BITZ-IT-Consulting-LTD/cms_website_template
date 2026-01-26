<template>
  <header
    class="absolute top-0 left-0 right-0 z-50 bg-transparent transition-all duration-300">
    <!-- Skip link handled in App.vue for better first-element accessibility -->
    <nav class="w-full px-8 lg:px-12" aria-label="Main Navigation">
      <div class="flex items-center justify-between h-[80px]">
        <!-- Logo - Text Only at Extreme Left -->
        <router-link to="/" class="flex items-center group no-underline shrink-0">
          <h1 class="text-2xl tracking-tight text-neutral-black group-hover:text-primary transition-colors duration-300 m-0 font-bold" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
            SAUTI 116 HELPLINE
          </h1>
        </router-link>

        <!-- Centered Desktop Navigation -->
        <div class="hidden lg:flex flex-1 items-center justify-center">
          <div class="flex items-center gap-8">
            <router-link v-for="link in [
              { to: '/', label: 'Home' },
              { to: '/about', label: 'Who We Are' },
              { to: '/videos', label: 'Videos' },
              { to: '/blogs', label: 'Blogs' },
              { to: '/news', label: 'News' },
              { to: '/resources', label: 'Resources' },
              { to: '/faqs', label: 'FAQs' },
              { to: '/contact', label: 'Contact Us' }
            ]" :key="link.to" :to="link.to"
              class="text-neutral-black text-base font-semibold transition-all duration-300 hover:text-primary relative py-2"
              active-class="text-primary">
              {{ link.label }}
            </router-link>
          </div>
        </div>

        <!-- Right Actions -->
        <div class="hidden lg:flex items-center gap-3 shrink-0">
          <!-- Call Button -->
          <BaseCTA :href="`tel:${settings.hotline_number || '116'}`" variant="emergency" external
            class="!rounded-full !px-6 !py-2.5 shadow-lg hover:shadow-xl gap-2 !border-0 flex items-center group"
            aria-label="Call Emergency Helpline 116">
            <Phone class="w-4 h-4 text-white group-hover:rotate-12 transition-transform" stroke-width="2.5" />
            <span class="text-sm font-bold">Call 116</span>
          </BaseCTA>

          <!-- Report Button -->
          <BaseCTA to="/report" variant="primary"
            class="!rounded-full !px-6 !py-2.5 !text-sm !font-bold !bg-[#006837] hover:!bg-[#005529] !border-0 text-white shadow-lg hover:shadow-xl">
            Report a case here
          </BaseCTA>
        </div>

        <!-- Mobile Actions Group -->
        <div class="lg:hidden flex items-center gap-2 relative z-20">
          <!-- Compact Mobile Call Prompt (Removed per request) -->
          <!-- <div class="flex items-center gap-1.5 mr-2" aria-label="Call Emergency Helpline 116">
            <Phone class="w-5 h-5 text-[#ed1c24]" stroke-width="2.5" />
            <a :href="`tel:${settings.hotline_number || '116'}`" class="font-black text-lg text-[#ed1c24] tracking-tight no-underline">116</a>
          </div> -->

          <button @click="mobileMenuOpen = !mobileMenuOpen"
            class="p-2.5 text-secondary bg-white shadow-md border border-gray-100 rounded-full hover:bg-gray-50 active:scale-95 transition-all duration-300 ml-2"
            aria-label="Toggle menu" :aria-expanded="mobileMenuOpen">
            <Menu v-if="!mobileMenuOpen" class="w-6 h-6" stroke-width="2.5" />
            <X v-else class="w-6 h-6 text-red-500" stroke-width="2.5" />
          </button>
        </div>
      </div>
    </nav>

    <!-- Full Screen Mobile Menu -->
    <Transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 translate-y-4"
      enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-4">
      <div v-if="mobileMenuOpen"
        class="lg:hidden absolute inset-x-0 top-full h-[calc(100vh-80px)] bg-white/98 backdrop-blur-3xl border-t border-gray-100 shadow-2xl overflow-y-auto">
          <div class="grid gap-2 mb-2 border-b border-gray-100 pb-2">
            <!-- Call Link -->
            <a :href="`tel:${settings.hotline_number || '116'}`" 
               class="text-lg font-bold text-[#ed1c24] py-4 px-4 rounded-xl transition-all flex items-center justify-between group hover:bg-red-50 active:bg-red-100">
               <span class="flex items-center gap-3">
                 Emergency Call {{ settings.hotline_number || '116' }}
               </span>
               <ArrowRight class="w-5 h-5 opacity-30 group-hover:opacity-100 group-hover:translate-x-1 transition-all text-[#ed1c24]" stroke-width="2.5" />
            </a>
            
            <!-- Report Link -->
            <router-link to="/report" 
               class="text-lg font-bold text-[#006837] py-4 px-4 rounded-xl transition-all flex items-center justify-between group hover:bg-green-50 active:bg-green-100"
               @click="mobileMenuOpen = false">
               <span class="flex items-center gap-3">
                 Report a Case Here
               </span>
               <ArrowRight class="w-5 h-5 opacity-30 group-hover:opacity-100 group-hover:translate-x-1 transition-all text-[#006837]" stroke-width="2.5" />
            </router-link>
          </div>

          <nav class="grid gap-2 pt-2" aria-label="Mobile Navigation">
            <router-link v-for="link in [
              { to: '/', label: 'Home' },
              { to: '/about', label: 'Who We Are' },
              { to: '/videos', label: 'Videos' },
              { to: '/blogs', label: 'Blogs' },
              { to: '/news', label: 'News' },
              { to: '/resources', label: 'Resources' },
              { to: '/faqs', label: 'FAQs' },
              { to: '/contact', label: 'Contact Us' }
            ]" :key="link.to" :to="link.to"
              class="text-lg font-bold text-secondary-light py-4 px-4 rounded-xl transition-all flex items-center justify-center group hover:bg-gray-50 active:bg-gray-100 text-center"
              active-class="bg-blue-50 text-primary !font-black" @click="mobileMenuOpen = false">
              {{ link.label }}
              <!-- Arrow removed for centered clean look, or kept if preferred? User asked to center menus. Usually arrow implies left-right. I will remove arrow to perfectly center. -->
            </router-link>
          </nav>
        </div>
    </Transition>
  </header>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue'
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
</script>

<style scoped></style>
