<template>
  <header
    class="sticky top-0 z-50 bg-sauti-white/95 backdrop-blur-md border-b border-sauti-blue/10 shadow-sm transition-all duration-300">
    <a href="#main-content"
      class="absolute top-0 left-0 -translate-y-full focus:translate-y-0 z-[100] bg-sauti-blue text-sauti-white px-6 py-3 font-bold transition-transform duration-300 rounded-br-xl shadow-lg">
      Skip to main content
    </a>
    <nav class="container-custom">
      <div class="flex items-center justify-between h-[88px]">
        <!-- Enhanced Logo Section -->
        <router-link to="/" class="flex items-center gap-3 group no-underline shrink-0 relative z-20">
          <div class="relative">
            <div
              class="absolute -inset-2 bg-sauti-blue/5 rounded-full scale-0 group-hover:scale-100 transition-transform duration-300">
            </div>
            <BaseLogo size="md" variant="default" alt="Sauti 116" class="relative" />
          </div>
          <div class="hidden md:block">
            <h1
              class="text-xl font-semibold tracking-tight text-sauti-darkGreen group-hover:text-sauti-blue transition-colors duration-300 m-0 leading-none">
              {{ settings.site_name || 'Sauti 116' }}
            </h1>
            <p class="text-[11px] font-normal uppercase tracking-[0.1em] text-sauti-blue/80 mt-1">National Helpline</p>
          </div>
        </router-link>

        <!-- Premium Desktop Navigation -->
        <div class="hidden lg:flex flex-1 items-center justify-center pl-8 pr-8">
          <div class="flex items-center gap-1 bg-sauti-neutral/50 p-1.5 rounded-full border border-sauti-blue/5">
            <router-link v-for="link in [
              { to: '/', label: 'Home' },
              { to: '/about', label: 'About' },
              { to: '/blogs', label: 'News/Blog' },
              { to: '/videos', label: 'Videos' },
              { to: '/resources', label: 'Resources' },
              { to: '/faqs', label: 'FAQs' },
              { to: '/contact', label: 'Contact' }
            ]" :key="link.to" :to="link.to"
              class="px-5 py-2.5 rounded-full text-sauti-darkGreen text-sm font-normal transition-all duration-300 hover:text-sauti-blue relative overflow-hidden group"
              active-class="bg-white text-sauti-blue shadow-sm ring-1 ring-black/5 !font-semibold">
              <span class="relative z-10">{{ link.label }}</span>
            </router-link>
          </div>
        </div>

        <!-- Refined Right Actions -->
        <div class="hidden lg:flex items-center gap-4 shrink-0">
          <!-- Helpline Number Display -->
          <!-- Helpline Number Display -->
          <BaseCTA :href="`tel:${settings.hotline_number || '116'}`" variant="emergency" external
            class="!rounded-full !px-6 !py-2.5 animate-emergency-glow shadow-sauti-red/30 gap-2.5 !border-0 flex items-center">
            <PhoneIcon class="w-5 h-5" stroke-width="2.5" />
            <div class="flex flex-col items-start leading-none ml-0.5">
              <span class="text-[10px] uppercase font-bold tracking-[0.25em] opacity-90">Emergency</span>
              <span class="text-xl font-bold tracking-[0.1em] uppercase">Call 116</span>
            </div>
          </BaseCTA>

          <!-- Primary CTA -->
          <BaseCTA to="/report" variant="primary"
            class="!rounded-full !px-8 !py-3 !text-sm shadow-lg shadow-sauti-blue/20 hover:shadow-sauti-blue/30 !font-bold tracking-[0.1em] border-2 border-transparent uppercase">
            {{ settings.primary_cta_text || 'Report Case' }}
          </BaseCTA>
        </div>

        <!-- Mobile Menu Button -->
        <button @click="mobileMenuOpen = !mobileMenuOpen"
          class="lg:hidden relative z-20 p-2.5 text-sauti-darkGreen hover:bg-sauti-neutral rounded-full transition-all duration-300"
          aria-label="Toggle menu" :aria-expanded="mobileMenuOpen">
          <Bars3Icon v-if="!mobileMenuOpen" class="w-8 h-8" stroke-width="2" />
          <XMarkIcon v-else class="w-8 h-8" stroke-width="2" />
        </button>
      </div>
    </nav>

    <!-- Full Screen Mobile Menu -->
    <Transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 translate-y-4"
      enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-4">
      <div v-if="mobileMenuOpen"
        class="lg:hidden absolute inset-x-0 top-full h-[calc(100vh-88px)] bg-sauti-white/95 backdrop-blur-xl border-t border-sauti-neutral/50 overflow-y-auto">
        <div class="container-custom py-8 space-y-8">
          <nav class="grid gap-2">
            <router-link v-for="link in [
              { to: '/', label: 'Home' },
              { to: '/about', label: 'About Us' },
              { to: '/blogs', label: 'News/Blog' },
              { to: '/videos', label: 'Videos' },
              { to: '/resources', label: 'Resources' },
              { to: '/faqs', label: 'FAQs' },
              { to: '/contact', label: 'Contact' }
            ]" :key="link.to" :to="link.to"
              class="text-2xl font-normal text-sauti-darkGreen py-4 border-b border-sauti-neutral/50 flex items-center justify-between group"
              active-class="text-sauti-blue border-sauti-blue/30 !font-semibold" @click="mobileMenuOpen = false">
              {{ link.label }}
              <ArrowRightIcon
                class="w-6 h-6 opacity-0 group-hover:opacity-100 -translate-x-4 group-hover:translate-x-0 transition-all text-sauti-blue" />
            </router-link>
          </nav>

          <div class="grid gap-4 pt-4">
            <BaseCTA :href="`tel:${settings.hotline_number || '116'}`" variant="emergency" external
              class="flex items-center justify-center gap-4 w-full p-6 !rounded-3xl animate-emergency-glow text-center">
              <PhoneIcon class="w-8 h-8" />
              <div class="text-left">
                <div class="text-xs font-bold uppercase tracking-[0.2em] opacity-80">Emergency Hotline</div>
                <div class="text-3xl font-bold uppercase tracking-[0.1em]">Call {{ settings.hotline_number || '116' }}</div>
              </div>
            </BaseCTA>
            <BaseCTA to="/report" variant="primary" class="w-full justify-center !py-6 !text-lg !rounded-3xl shadow-xl"
              @click="mobileMenuOpen = false">
              {{ settings.primary_cta_text || 'Report a Case' }}
            </BaseCTA>
          </div>
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

  onMounted(async () => {
    await settingsStore.fetchGlobalSettings()
  })
</script>

<style scoped></style>
