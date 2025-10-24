<template>
  <div class="flex h-screen bg-gray-50">
    <!-- Sidebar -->
    <div class="fixed inset-y-0 left-0 z-50 w-64 bg-white shadow-lg transform transition-transform duration-300 ease-in-out lg:translate-x-0 lg:static lg:inset-0" :class="{ '-translate-x-full': !sidebarOpen }">
      <div class="flex flex-col h-full">
        <!-- Logo -->
        <div class="flex items-center justify-between h-16 px-6 border-b border-gray-200">
          <h1 class="text-xl font-bold text-gray-900">Sauti.</h1>
          <button
            @click="sidebarOpen = false"
            class="lg:hidden p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100"
          >
            <XMarkIcon class="h-6 w-6" />
          </button>
        </div>

        <!-- Navigation -->
        <nav class="flex-1 px-4 py-6 space-y-2">
          <router-link
            to="/dashboard"
            class="sidebar-link"
            :class="{ active: $route.path === '/dashboard' }"
          >
            <Squares2X2Icon class="h-5 w-5 mr-3" />
            Dashboard
          </router-link>
          
          <router-link
            to="/posts"
            class="sidebar-link"
            :class="{ active: $route.path.startsWith('/posts') }"
          >
            <DocumentTextIcon class="h-5 w-5 mr-3" />
            Content
          </router-link>
          
          <router-link
            to="/drafts"
            class="sidebar-link"
            :class="{ active: $route.path === '/drafts' }"
          >
            <DocumentTextIcon class="h-5 w-5 mr-3" />
            Drafts
          </router-link>
          
          <router-link
            to="/videos"
            class="sidebar-link"
            :class="{ active: $route.path.startsWith('/videos') }"
          >
            <VideoCameraIcon class="h-5 w-5 mr-3" />
            Videos
          </router-link>
          
          <router-link
            to="/settings"
            class="sidebar-link"
            :class="{ active: $route.path === '/settings' }"
          >
            <CogIcon class="h-5 w-5 mr-3" />
            Settings
          </router-link>
        </nav>

        <!-- User Info & Logout -->
        <div class="border-t border-gray-200 p-4">
          <div class="flex items-center mb-4">
            <div class="flex-shrink-0">
              <div class="h-8 w-8 rounded-full bg-primary-500 flex items-center justify-center">
                <span class="text-white text-sm font-medium">
                  {{ userInitials }}
                </span>
              </div>
            </div>
            <div class="ml-3">
              <p class="text-sm font-medium text-gray-900">{{ authStore.userFullName }}</p>
              <p class="text-xs text-gray-500">{{ authStore.user?.role }}</p>
            </div>
          </div>
          
          <button
            @click="handleLogout"
            class="flex items-center w-full px-3 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900 rounded-md transition-colors duration-200"
          >
            <ArrowRightOnRectangleIcon class="h-5 w-5 mr-3" />
            Logout
          </button>
        </div>
      </div>
    </div>

    <!-- Main content -->
    <div class="flex-1 flex flex-col overflow-hidden lg:ml-0">
      <!-- Mobile header -->
      <div class="lg:hidden bg-white shadow-sm border-b border-gray-200">
        <div class="flex items-center justify-between h-16 px-4">
          <button
            @click="sidebarOpen = true"
            class="p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100"
          >
            <Bars3Icon class="h-6 w-6" />
          </button>
          <h1 class="text-lg font-semibold text-gray-900">{{ pageTitle }}</h1>
          <div class="w-10"></div>
        </div>
      </div>

      <!-- Page content -->
      <main class="flex-1 overflow-y-auto">
        <router-view />
      </main>
    </div>

    <!-- Mobile sidebar overlay -->
    <div
      v-if="sidebarOpen"
      class="fixed inset-0 z-40 lg:hidden"
      @click="sidebarOpen = false"
    >
      <div class="absolute inset-0 bg-gray-600 opacity-75"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useToast } from 'vue-toastification'
import {
  Bars3Icon,
  XMarkIcon,
  Squares2X2Icon,
  DocumentTextIcon,
  VideoCameraIcon,
  CogIcon,
  ArrowRightOnRectangleIcon
} from '@heroicons/vue/24/outline'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()
const toast = useToast()

const sidebarOpen = ref(false)

const userInitials = computed(() => {
  if (!authStore.user) return 'U'
  const firstName = authStore.user.first_name || ''
  const lastName = authStore.user.last_name || ''
  if (firstName && lastName) {
    return `${firstName[0]}${lastName[0]}`.toUpperCase()
  }
  return authStore.user.username ? authStore.user.username[0].toUpperCase() : 'U'
})

const pageTitle = computed(() => {
  const routeNames = {
    '/dashboard': 'Dashboard',
    '/posts': 'Content',
    '/drafts': 'Drafts',
    '/videos': 'Videos',
    '/settings': 'Settings'
  }
  
  // Check for exact matches first
  if (routeNames[route.path]) {
    return routeNames[route.path]
  }
  
  // Check for partial matches
  if (route.path.startsWith('/posts')) return 'Content'
  if (route.path.startsWith('/videos')) return 'Videos'
  
  return 'Dashboard'
})

const handleLogout = async () => {
  try {
    await authStore.logout()
    toast.success('Successfully logged out')
    router.push('/login')
  } catch (err) {
    console.error('Logout error:', err)
    toast.error('Error during logout')
  }
}
</script>
