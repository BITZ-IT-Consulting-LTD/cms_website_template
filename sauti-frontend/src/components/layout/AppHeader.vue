<template>
  <header
    class="absolute top-0 left-0 right-0 z-50 bg-transparent transition-all duration-300">
    <!-- Skip link handled in App.vue for better first-element accessibility -->
    <nav class="w-full px-8 lg:px-12" aria-label="Main Navigation">
      <div class="flex items-center justify-between h-[80px]">
        <!-- Logo - Text Only at Extreme Left -->
        <router-link to="/" class="flex items-center group no-underline shrink-0">
          <h1 class="text-2xl tracking-tight text-neutral-black group-hover:text-primary transition-colors duration-300 m-0 font-bold">
            SAUTI 116
          </h1>
        </router-link>

        <!-- Centered Desktop Navigation -->
        <div class="hidden lg:flex flex-1 items-center justify-center">
          <div class="flex items-center gap-8">
            <router-link v-for="link in [
              { to: '/', label: 'Home' },
              { to: '/about', label: 'Who We Are' },
              { to: '/videos', label: 'Videos' },
              { to: '/blogs', label: 'Updates' },
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
          <!-- Compact Mobile Call Prompt (Always Visible) -->
          <BaseCTA :href="`tel:${settings.hotline_number || '116'}`" variant="emergency" external
            class="!rounded-full !px-4 !py-2 !text-xs shadow-lg flex items-center gap-2 !border-0"
            aria-label="Call Emergency Helpline 116">
            <Phone class="w-4 h-4 text-white" stroke-width="3" />
            <span class="font-bold">116</span>
          </BaseCTA>

          <button @click="mobileMenuOpen = !mobileMenuOpen"
            class="p-2.5 text-secondary hover:bg-primary/5 rounded-full transition-all duration-300"
            aria-label="Toggle menu" :aria-expanded="mobileMenuOpen">
            <Menu v-if="!mobileMenuOpen" class="w-7 h-7" stroke-width="2" />
            <X v-else class="w-7 h-7" stroke-width="2" />
          </button>
        </div>
      </div>
    </nav>

    <!-- Full Screen Mobile Menu -->
    <Transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 translate-y-4"
      enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-4">
      <div v-if="mobileMenuOpen"
        class="lg:hidden absolute inset-x-0 top-full h-[calc(100vh-100px)] bg-neutral-white/95 backdrop-blur-xl border-t border-neutral-offwhite/50 overflow-y-auto">
        <div class="container-custom py-8 space-y-8">
          <div class="grid gap-4 mb-8">
            <BaseCTA :href="`tel:${settings.hotline_number || '116'}`" variant="emergency" external
              class="flex items-center justify-center gap-4 w-full p-6 !rounded-3xl shadow-xl ring-4 ring-white/10 text-center group">
              <Phone class="w-10 h-10 group-hover:rotate-12 transition-transform" />
              <div class="text-left leading-none uppercase">
                <div class="text-xs font-bold tracking-[0.2em] opacity-80 mb-1">Emergency 24/7</div>
                <div class="text-4xl font-bold tracking-tighter">Call {{ settings.hotline_number || '116' }}</div>
              </div>
            </BaseCTA>
            <BaseCTA to="/report" variant="primary"
              class="w-full justify-center !py-6 !text-lg !rounded-3xl shadow-xl flex items-center gap-3 !bg-[#006837] hover:!bg-[#005529]"
              @click="mobileMenuOpen = false">
              <ShieldCheck class="w-6 h-6" />
              <span>Report Here</span>
            </BaseCTA>
          </div>

          <nav class="grid gap-0 border-t border-neutral-offwhite pt-4" aria-label="Mobile Navigation">
            <router-link v-for="link in [
              { to: '/', label: 'Home' },
              { to: '/about', label: 'Who We Are' },
              { to: '/videos', label: 'Videos' },
              { to: '/blogs', label: 'Updates' },
              { to: '/resources', label: 'Resources' },
              { to: '/faqs', label: 'FAQs' },
              { to: '/contact', label: 'Contact Us' }
            ]" :key="link.to" :to="link.to"
              class="text-xl font-normal text-secondary py-6 border-b border-neutral-offwhite/50 flex items-center justify-between group px-2"
              active-class="text-primary border-primary/30 !font-semibold" @click="mobileMenuOpen = false">
              {{ link.label }}
              <ArrowRight class="w-5 h-5 opacity-40 group-hover:opacity-100 transition-all text-primary"
                aria-hidden="true" />
            </router-link>
          </nav>
        </div>
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
