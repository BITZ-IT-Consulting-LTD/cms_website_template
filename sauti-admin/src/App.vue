<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

onMounted(() => {
  // Check if user is logged in and fetch profile if needed
  if (authStore.isAuthenticated && !authStore.user) {
    authStore.fetchProfile().catch(() => {
      // If profile fetch fails, logout user
      authStore.logout()
    })
  }
})
</script>

<style>
/* Global styles are handled in main.css */
</style>
