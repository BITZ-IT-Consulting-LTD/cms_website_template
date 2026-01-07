<template>
  <header
    class="sticky top-0 z-50 bg-neutral-white/95 backdrop-blur-md border-b border-primary/10 shadow-sm transition-all duration-300">
    <!-- Skip link handled in App.vue for better first-element accessibility -->
    <nav class="container-custom" aria-label="Main Navigation">
      <div class="flex items-center justify-between h-[100px]">
        <!-- Sauti Brand Logo Section (Re-aligned) -->
        <router-link to="/" class="flex items-center gap-4 group no-underline shrink-0 relative z-20">
          <div class="relative">
            <div
              class="absolute -inset-2 bg-primary/5 rounded-full scale-0 group-hover:scale-100 transition-transform duration-300">
            </div>
            <BaseLogo size="lg" variant="default" alt="Sauti 116" class="relative" />
          </div>
          <div class="hidden md:block border-l-2 border-primary/10 pl-4 py-1">
            <h1
              class="text-xl font-bold tracking-tight text-neutral-black group-hover:text-primary transition-colors duration-300 m-0 leading-none">
              {{ filteredOrgName }}
            </h1>
            <div class="flex items-center gap-2 mt-1">
              <p class="text-[10px] font-black uppercase tracking-[0.15em] text-primary">Operated by MGLSD</p>
            </div>
          </div>
        </router-link>

        <!-- Premium Desktop Navigation -->
        <div class="hidden lg:flex flex-1 items-center justify-center pl-8 pr-8">
          <div class="flex items-center gap-1 bg-neutral-offwhite/50 p-1.5 rounded-full border border-primary/5">
            <router-link v-for="link in [
              { to: '/', label: 'Home' },
              { to: '/about', label: 'Who We Are' },
              { to: '/resources', label: 'Get Help' },
              { to: '/faqs', label: 'FAQs' },
              { to: '/blogs', label: 'Updates' },
              { to: '/contact', label: 'Contact Us' }
            ]" :key="link.to" :to="link.to"
              class="px-5 py-2.5 rounded-full text-neutral-black text-sm font-bold transition-all duration-300 hover:text-primary relative overflow-hidden group"
              active-class="bg-white text-primary shadow-sm ring-1 ring-black/5">
              <span class="relative z-10">{{ link.label }}</span>
            </router-link>
          </div>
        </div>

        <!-- Refined Right Actions -->
        <div class="hidden lg:flex items-center gap-4 shrink-0">
          <!-- Helpline Number Display (The One Primary Action) -->
          <BaseCTA :href="`tel:${settings.hotline_number || '116'}`" variant="emergency" external
            class="!rounded-full !px-8 !py-3 shadow-xl hover:shadow-2xl gap-3 !border-0 flex items-center group overflow-hidden relative"
            aria-label="Call Emergency Helpline 116">
            <PhoneIcon class="w-5 h-5 text-white group-hover:rotate-12 transition-transform" stroke-width="2.5" />
            <span class="text-sm font-black tracking-widest uppercase">Call 116</span>
          </BaseCTA>

          <BaseCTA to="/report" variant="outline"
            class="!rounded-full !px-6 !py-2.5 !text-xs !font-black tracking-widest uppercase border-2 text-primary border-primary/20 hover:border-primary/40">
            {{ settings.primary_cta_text || 'Report Violence Online' }}
          </BaseCTA>
        </div>

        <!-- Mobile Actions Group -->
        <div class="lg:hidden flex items-center gap-2 relative z-20">
          <!-- Compact Mobile Call Prompt (Always Visible) -->
          <BaseCTA :href="`tel:${settings.hotline_number || '116'}`" variant="emergency" external
            class="!rounded-full !px-4 !py-2 !text-xs shadow-lg flex items-center gap-2 !border-0"
            aria-label="Call Emergency Helpline 116">
            <PhoneIcon class="w-4 h-4 text-white" stroke-width="3" />
            <span class="font-black">116</span>
          </BaseCTA>

          <button @click="mobileMenuOpen = !mobileMenuOpen"
            class="p-2.5 text-secondary hover:bg-primary/5 rounded-full transition-all duration-300"
            aria-label="Toggle menu" :aria-expanded="mobileMenuOpen">
            <Bars3Icon v-if="!mobileMenuOpen" class="w-8 h-8" stroke-width="2" />
            <XMarkIcon v-else class="w-8 h-8" stroke-width="2" />
          </button>
        </div>
      </div>
    </nav>

    <!-- Full Screen Mobile Menu -->
    <Transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 translate-y-4"
      enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-4">
      <div v-if="mobileMenuOpen"
        class="lg:hidden absolute inset-x-0 top-full h-[calc(100vh-88px)] bg-neutral-white/95 backdrop-blur-xl border-t border-neutral-offwhite/50 overflow-y-auto">
        <div class="container-custom py-8 space-y-8">
          <div class="grid gap-4 mb-8">
            <BaseCTA :href="`tel:${settings.hotline_number || '116'}`" variant="emergency" external
              class="flex items-center justify-center gap-4 w-full p-6 !rounded-3xl shadow-xl ring-4 ring-white/10 text-center group">
              <PhoneIcon class="w-10 h-10 group-hover:rotate-12 transition-transform" />
              <div class="text-left leading-none uppercase">
                <div class="text-xs font-black tracking-[0.2em] opacity-80 mb-1">Emergency 24/7</div>
                <div class="text-4xl font-black tracking-tighter">Call {{ settings.hotline_number || '116' }}</div>
              </div>
            </BaseCTA>
            <BaseCTA to="/report" variant="primary"
              class="w-full justify-center !py-6 !text-lg !rounded-3xl shadow-xl flex items-center gap-3"
              @click="mobileMenuOpen = false">
              <ShieldCheckIcon class="w-6 h-6" />
              <span>Report Violence Online</span>
            </BaseCTA>
          </div>

          <nav class="grid gap-0 border-t border-neutral-offwhite pt-4" aria-label="Mobile Navigation">
            <router-link v-for="link in [
              { to: '/', label: 'Home' },
              { to: '/about', label: 'Who We Are' },
              { to: '/resources', label: 'Get Help' },
              { to: '/faqs', label: 'FAQs' },
              { to: '/blogs', label: 'Updates' },
              { to: '/contact', label: 'Contact Us' }
            ]" :key="link.to" :to="link.to"
              class="text-xl font-normal text-secondary py-6 border-b border-neutral-offwhite/50 flex items-center justify-between group px-2"
              active-class="text-primary border-primary/30 !font-semibold" @click="mobileMenuOpen = false">
              {{ link.label }}
              <ArrowRightIcon class="w-5 h-5 opacity-40 group-hover:opacity-100 transition-all text-primary"
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
    PhoneIcon,
    Bars3Icon,
    XMarkIcon,
    ArrowRightIcon
  } from '@heroicons/vue/24/outline'

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
