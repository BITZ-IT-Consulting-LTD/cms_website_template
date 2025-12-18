<template>
  <div id="app" class="flex flex-col min-h-screen">
    <AppHeader />
    
    <main class="flex-grow">
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
import '@/assets/giz-css/root.css'
import '@/assets/giz-css/giz-scoped.css'

onMounted(() => {
  // Add any global initialization logic here
  console.log('Sauti Frontend Loaded')
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
