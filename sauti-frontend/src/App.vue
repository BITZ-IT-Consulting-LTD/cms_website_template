<template>
  <div id="app" class="flex flex-col min-h-screen" :style="themeStyles">
    <a href="#main-content" class="skip-link">Skip to main content</a>
    <AppHeader />

    <!-- Quick Exit (P0 Safety Action) -->
    <div class="fixed top-24 right-4 z-[60] lg:top-8 lg:right-8 transition-all duration-500">
      <button @click="quickExit"
        class="bg-emergency text-neutral-white px-4 py-2 lg:px-6 lg:py-3 rounded-full font-bold uppercase tracking-widest text-[10px] lg:text-xs shadow-2xl hover:brightness-110 active:scale-95 transition-all flex items-center gap-2 border-2 border-white/20"
        title="Immediately leave this site">
        <span class="hidden md:inline">Quick Exit</span>
        <XMarkIcon class="w-4 h-4" stroke-width="3" />
      </button>
    </div>

    <!-- Mobile Emergency FAB (P1 Reachability) -->
    <div class="fixed bottom-24 right-6 z-[60] lg:hidden">
      <a :href="`tel:${settingsStore.settings.hotline_number || '116'}`"
        class="flex flex-col items-center justify-center w-16 h-16 bg-emergency text-neutral-white rounded-full shadow-[0_0_30px_rgba(198,40,40,0.4)] animate-emergency-glow border-2 border-white/20 no-underline">
        <PhoneIcon class="w-7 h-7" stroke-width="2.5" />
        <span class="text-[8px] font-black uppercase mt-0.5 leading-none">116</span>
      </a>
    </div>

    <main id="main-content" class="flex-grow" role="main">
      <router-view v-slot="{ Component }">
        <Transition name="fade" mode="out-in">
          <component :is="Component" />
        </Transition>
      </router-view>
    </main>

    <AppFooter />

    <FloatingChatBot />
  </div>
</template>

<script setup>
  import { onMounted } from 'vue'
  import AppHeader from '@/components/layout/AppHeader.vue'
  import AppFooter from '@/components/layout/AppFooter.vue'
  import FloatingChatBot from '@/components/giz/FloatingChatBot.vue'
  import { XMarkIcon, PhoneIcon } from '@heroicons/vue/24/outline'

  // Import Giz styles
  import '@/assets/giz-css/giz-scoped.css'
  import { useSettingsStore } from '@/store/settings'
  import { computed } from 'vue'

  const settingsStore = useSettingsStore()
  const orgProfile = computed(() => settingsStore.orgProfile)

  function quickExit() {
    // Redirect to google and replace state to prune history
    window.location.replace('https://www.google.com')
  }

  function hexToRgb(hex) {
    if (!hex) return null
    hex = hex.replace('#', '')
    if (hex.length === 3) {
      hex = hex.split('').map(c => c + c).join('')
    }
    const r = parseInt(hex.substring(0, 2), 16)
    const g = parseInt(hex.substring(2, 4), 16)
    const b = parseInt(hex.substring(4, 6), 16)
    return isNaN(r) || isNaN(g) || isNaN(b) ? null : `${r} ${g} ${b}`
  }

  const themeStyles = computed(() => {
    if (!orgProfile.value) return {}

    const styles = {
      '--color-primary': hexToRgb(orgProfile.value.primary_color || '#0066A3'),
      '--color-secondary': hexToRgb(orgProfile.value.secondary_color || '#0F172A'),
      '--color-hotline': hexToRgb(orgProfile.value.hotline_color || '#EA580C'),
      '--color-emergency': hexToRgb(orgProfile.value.emergency_color || '#C62828'),
    }

    // Add all granular brand colors as dynamic variables mapping to --color-* channels
    if (orgProfile.value.brand_colors && Array.isArray(orgProfile.value.brand_colors)) {
      orgProfile.value.brand_colors.forEach(c => {
        const key = `--color-${c.id.replace(/_/g, '-')}`
        const rgb = hexToRgb(c.value)
        if (rgb) {
          styles[key] = rgb
        }
      })
    }

    return styles
  })

  onMounted(async () => {
    // Add any global initialization logic here
    console.log('Sauti Frontend Loaded')
    await settingsStore.fetchGlobalSettings()
  })
</script>

<style>

  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.3s ease;
  }

  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }
</style>
