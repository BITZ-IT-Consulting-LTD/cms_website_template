<template>
  <header class="bg-white shadow-md sticky top-0 z-50">
    <!-- Emergency Banner -->
    <div class="emergency-banner no-print">
      <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
      </svg>
      <span>Emergency? Call <a href="tel:116" class="underline font-bold">116</a> now!</span>
    </div>

    <nav class="container-custom py-4">
      <div class="flex items-center justify-between">
        <!-- Logo -->
        <router-link to="/" class="flex items-center space-x-3">
          <img src="/logo.png" alt="Sauti Logo" class="h-12 w-auto" @error="handleLogoError" />
          <div>
            <h1 class="text-xl md:text-2xl font-bold text-primary-600">Sauti</h1>
            <p class="text-xs text-gray-600 hidden sm:block">Child Helpline</p>
          </div>
        </router-link>

        <!-- Desktop Navigation -->
        <div class="hidden lg:flex items-center space-x-6">
          <router-link
            v-for="link in navigationLinks"
            :key="link.to"
            :to="link.to"
            class="text-gray-700 hover:text-primary-600 font-medium transition-colors"
            active-class="text-primary-600"
          >
            {{ link.label }}
          </router-link>
          
          <!-- Language Switcher -->
          <LanguageSwitcher />
          
          <!-- Get Help Button -->
          <GetHelpButton />
          
          <!-- Auth Links -->
          <div v-if="isAuthenticated">
            <button
              @click="handleLogout"
              class="text-gray-700 hover:text-primary-600 font-medium"
            >
              Logout
            </button>
          </div>
          <router-link
            v-else
            to="/login"
            class="text-gray-700 hover:text-primary-600 font-medium"
          >
            Staff Login
          </router-link>
        </div>

        <!-- Mobile Menu Button -->
        <button
          @click="mobileMenuOpen = !mobileMenuOpen"
          class="lg:hidden p-2 text-gray-700 hover:text-primary-600"
          aria-label="Toggle menu"
        >
          <svg v-if="!mobileMenuOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
          <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- Mobile Menu -->
      <Transition name="slide">
        <div v-if="mobileMenuOpen" class="lg:hidden mt-4 pb-4 space-y-3">
          <router-link
            v-for="link in navigationLinks"
            :key="link.to"
            :to="link.to"
            class="block py-2 text-gray-700 hover:text-primary-600 font-medium"
            active-class="text-primary-600"
            @click="mobileMenuOpen = false"
          >
            {{ link.label }}
          </router-link>
          
          <div class="pt-3 border-t border-gray-200">
            <LanguageSwitcher class="mb-3" />
            <GetHelpButton class="w-full" />
          </div>
          
          <div v-if="isAuthenticated" class="pt-3 border-t border-gray-200">
            <button
              @click="handleLogout"
              class="block py-2 text-gray-700 hover:text-primary-600 font-medium"
            >
              Logout
            </button>
          </div>
          <router-link
            v-else
            to="/login"
            class="block py-2 text-gray-700 hover:text-primary-600 font-medium"
            @click="mobileMenuOpen = false"
          >
            Staff Login
          </router-link>
        </div>
      </Transition>
    </nav>
  </header>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/store/auth'
import LanguageSwitcher from '@/components/common/LanguageSwitcher.vue'
import GetHelpButton from '@/components/common/GetHelpButton.vue'

const router = useRouter()
const authStore = useAuthStore()

const mobileMenuOpen = ref(false)

const navigationLinks = [
  { to: '/', label: 'Home' },
  { to: '/about', label: 'About' },
  { to: '/blog', label: 'News' },
  { to: '/resources', label: 'Resources' },
  { to: '/faqs', label: 'FAQs' },
  { to: '/partners', label: 'Partners' },
  { to: '/report', label: 'Report Case' },
  { to: '/contact', label: 'Contact' },
]

const isAuthenticated = computed(() => authStore.isAuthenticated)

function handleLogout() {
  authStore.logout()
  router.push('/')
  mobileMenuOpen.value = false
}

function handleLogoError(event) {
  // Fallback if logo image fails to load
  event.target.src = 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text y="50" font-size="50">🛡️</text></svg>'
}
</script>

<style scoped>
.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s ease;
}

.slide-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}

.slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
