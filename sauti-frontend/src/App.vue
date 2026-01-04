<template>
  <div id="app" class="flex flex-col min-h-screen" :style="themeStyles">
    <a href="#main-content" class="skip-link">Skip to main content</a>
    <AppHeader />

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

  // Import Giz styles
  import '@/assets/giz-css/giz-scoped.css'
  import { useSettingsStore } from '@/store/settings'
  import { computed } from 'vue'

  const settingsStore = useSettingsStore()
  const orgProfile = computed(() => settingsStore.orgProfile)

  function hexToRgb(hex) {
    if (!hex) return null
    hex = hex.replace('#', '')
    if (hex.length === 3) {
      hex = hex.split('').map(c => c + c).join('')
    }
    const r = parseInt(hex.substring(0, 2), 16)
    const g = parseInt(hex.substring(2, 4), 16)
    const b = parseInt(hex.substring(4, 6), 16)
    return isNaN(r) || isNaN(g) || isNaN(b) ? null : `${r}, ${g}, ${b}`
  }

  const themeStyles = computed(() => {
    if (!orgProfile.value) return {}
    const primary = orgProfile.value.primary_color || '#007BBF'
    const secondary = orgProfile.value.secondary_color || '#006633'
    const accent = orgProfile.value.accent_color || '#FFF200'

    return {
      '--sauti-primary': primary,
      '--sauti-primary-rgb': hexToRgb(primary),
      '--sauti-secondary': secondary,
      '--sauti-secondary-rgb': hexToRgb(secondary),
      '--sauti-accent': accent,
      '--sauti-accent-rgb': hexToRgb(accent),
    }
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
