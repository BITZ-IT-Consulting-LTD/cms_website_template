<template>
  <div class="flex h-screen bg-white">
    <!-- Enhanced Sidebar -->
    <div class="fixed inset-y-0 left-0 z-50 w-72 bg-white shadow-2xl transform transition-transform duration-300 ease-in-out lg:translate-x-0 lg:static lg:inset-0 border-r border-gray-200" :class="{ '-translate-x-full': !sidebarOpen }">
      <div class="flex flex-col h-full">
        <!-- Enhanced Logo -->
        <div class="flex items-center justify-between h-20 px-6 border-b border-gray-200 bg-gradient-to-r from-[#8B4000] to-[#A0522D]">
          <div class="flex items-center space-x-3">
            <div class="h-10 w-10 rounded-2xl bg-white flex items-center justify-center">
              <span class="text-[#8B4000] font-bold text-lg">S</span>
            </div>
            <div>
              <h1 class="text-xl font-bold text-white" style="font-family: 'Roboto', sans-serif;">Sauti Admin</h1>
              <p class="text-xs text-white/80">Child Helpline CMS</p>
            </div>
          </div>
          <button
            @click="sidebarOpen = false"
            class="lg:hidden p-2 rounded-xl text-white/80 hover:text-white hover:bg-white/20 transition-all duration-300"
          >
            <XMarkIcon class="h-6 w-6" />
          </button>
        </div>

        <!-- Enhanced Quick Actions -->
        <div class="px-4 py-6 border-b border-gray-200 space-y-3">
          <router-link
            to="/posts/create"
            class="w-full px-4 py-3 bg-gradient-to-r from-[#8B4000] to-[#A0522D] text-white hover:from-[#A0522D] hover:to-[#8B4000] rounded-full transition-all duration-300 flex items-center justify-center font-semibold text-sm shadow-lg hover:shadow-xl transform hover:scale-105"
          >
            <PlusCircleIcon class="h-5 w-5 mr-2" />
            New Blog Post
          </router-link>
          
          <router-link
            to="/videos/create"
            class="w-full px-4 py-3 bg-gradient-to-r from-purple-100 to-indigo-100 text-purple-700 hover:from-purple-200 hover:to-indigo-200 rounded-full transition-all duration-300 flex items-center justify-center text-sm font-semibold border border-purple-200 hover:border-purple-300"
          >
            <VideoCameraIcon class="h-5 w-5 mr-2" />
            New Video
          </router-link>
        </div>

        <!-- Enhanced Navigation -->
        <nav class="flex-1 px-4 py-6 space-y-8 overflow-y-auto">

          <!-- Main Content Management Section -->
          <div>
            <h3 class="px-3 text-xs font-bold text-gray-600 uppercase tracking-wider mb-4 flex items-center">
              <div class="w-2 h-2 bg-[#8B4000] rounded-full mr-2"></div>
              Content Management
            </h3>
            <div class="space-y-2">
              <router-link
                to="/dashboard"
                class="sidebar-link group"
                :class="{ active: $route.path === '/dashboard' }"
              >
                <Squares2X2Icon class="h-5 w-5 mr-3 text-[#8B4000] group-hover:text-[#A0522D] transition-colors duration-300" />
                <span class="flex-1">Dashboard</span>
              </router-link>
              
              <router-link
                to="/posts"
                class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/posts') }"
              >
                <DocumentTextIcon class="h-5 w-5 mr-3 text-green-500 group-hover:text-green-600 transition-colors duration-300" />
                <span class="flex-1">Blog Posts</span>
                <span v-if="draftCount > 0" class="bg-yellow-100 text-yellow-700 text-xs font-bold px-2 py-1 rounded-full">
                  {{ draftCount }}
                </span>
              </router-link>
              
              <router-link
                to="/drafts"
                class="sidebar-link group"
                :class="{ active: $route.path === '/drafts' }"
              >
                <PencilSquareIcon class="h-5 w-5 mr-3 text-yellow-500 group-hover:text-yellow-600 transition-colors duration-300" />
                <span class="flex-1">Drafts</span>
                <span v-if="draftCount > 0" class="bg-yellow-100 text-yellow-700 text-xs font-bold px-2 py-1 rounded-full">
                  {{ draftCount }}
                </span>
              </router-link>
              
              <router-link
                to="/videos"
                class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/videos') }"
              >
                <VideoCameraIcon class="h-5 w-5 mr-3 text-purple-500 group-hover:text-purple-600 transition-colors duration-300" />
                <span class="flex-1">Videos</span>
              </router-link>
              
              <router-link
                to="/resources"
                class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/resources') }"
              >
                <FolderOpenIcon class="h-5 w-5 mr-3 text-indigo-500 group-hover:text-indigo-600 transition-colors duration-300" />
                <span class="flex-1">Resources</span>
              </router-link>
              
              <router-link
                to="/faqs"
                class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/faqs') }"
              >
                <QuestionMarkCircleIcon class="h-5 w-5 mr-3 text-teal-500 group-hover:text-teal-600 transition-colors duration-300" />
                <span class="flex-1">FAQs</span>
              </router-link>
            </div>
          </div>

          <!-- Content Organization Section -->
          <div>
            <h3 class="px-3 text-xs font-bold text-gray-600 uppercase tracking-wider mb-4 flex items-center">
              <div class="w-2 h-2 bg-green-500 rounded-full mr-2"></div>
              Content Organization
            </h3>
            <div class="space-y-2">
              <router-link
                to="/partners"
                class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/partners') }"
              >
                <UserGroupIcon class="h-5 w-5 mr-3 text-green-500 group-hover:text-green-600 transition-colors duration-300" />
                <span class="flex-1">Partners</span>
              </router-link>
              
              <router-link
                to="/success-stories"
                class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/success-stories') }"
              >
                <ChatBubbleLeftRightIcon class="h-5 w-5 mr-3 text-emerald-500 group-hover:text-emerald-600 transition-colors duration-300" />
                <span class="flex-1">Success Stories</span>
              </router-link>
            </div>
          </div>

          <!-- System & Settings Section -->
          <div>
            <h3 class="px-3 text-xs font-bold text-gray-600 uppercase tracking-wider mb-4 flex items-center">
              <div class="w-2 h-2 bg-gray-500 rounded-full mr-2"></div>
              System & Settings
            </h3>
            <div class="space-y-2">
              <router-link
                to="/users"
                class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/users') }"
              >
                <UsersIcon class="h-5 w-5 mr-3 text-gray-500 group-hover:text-gray-600 transition-colors duration-300" />
                <span class="flex-1">Team Members</span>
              </router-link>
              
              <router-link
                to="/settings"
                class="sidebar-link group"
                :class="{ active: $route.path === '/settings' }"
              >
                <CogIcon class="h-5 w-5 mr-3 text-gray-500 group-hover:text-gray-600 transition-colors duration-300" />
                <span class="flex-1">Settings</span>
              </router-link>
            </div>
          </div>
        </nav>

        <!-- Enhanced User Info & Logout -->
        <div class="border-t border-gray-200 p-6 bg-white">
          <div class="flex items-center mb-4">
            <div class="flex-shrink-0">
              <div class="h-12 w-12 rounded-2xl bg-gradient-to-br from-[#8B4000] to-[#A0522D] flex items-center justify-center shadow-lg">
                <span class="text-white text-lg font-bold">
                  {{ userInitials }}
                </span>
              </div>
            </div>
            <div class="ml-4">
              <p class="text-sm font-bold text-gray-900" style="font-family: 'Poppins', sans-serif;">{{ authStore.userFullName }}</p>
              <p class="text-xs text-gray-600 font-medium">{{ authStore.user?.role }}</p>
            </div>
          </div>
          
          <button
            @click="handleLogout"
            class="flex items-center w-full px-4 py-3 text-sm text-gray-700 hover:bg-red-50 hover:text-red-700 rounded-xl transition-all duration-300 font-semibold border border-gray-200 hover:border-red-200"
          >
            <ArrowRightOnRectangleIcon class="h-5 w-5 mr-3" />
            Logout
          </button>
        </div>
      </div>
    </div>

    <!-- Enhanced Main content -->
    <div class="flex-1 flex flex-col overflow-hidden lg:ml-0">
      <!-- Enhanced Mobile header -->
      <div class="lg:hidden bg-white shadow-lg border-b border-gray-200">
        <div class="flex items-center justify-between h-16 px-4">
          <button
            @click="sidebarOpen = true"
            class="p-3 rounded-xl text-gray-400 hover:text-gray-600 hover:bg-gray-100 transition-all duration-300"
          >
            <Bars3Icon class="h-6 w-6" />
          </button>
          <h1 class="text-lg font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">{{ pageTitle }}</h1>
          <div class="w-10"></div>
        </div>
      </div>

      <!-- Enhanced Page content -->
      <main class="flex-1 overflow-y-auto bg-white">
        <div class="p-6">
          <router-view />
        </div>
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
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { usePostsStore } from '@/stores/posts'
import { useToast } from 'vue-toastification'
import {
  Bars3Icon,
  XMarkIcon,
  Squares2X2Icon,
  DocumentTextIcon,
  VideoCameraIcon,
  CogIcon,
  ArrowRightOnRectangleIcon,
  PlusCircleIcon,
  PencilSquareIcon,
  FolderOpenIcon,
  QuestionMarkCircleIcon,
  UserGroupIcon,
  ChatBubbleLeftRightIcon,
  UsersIcon
} from '@heroicons/vue/24/outline'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()
const postsStore = usePostsStore()
const toast = useToast()

const sidebarOpen = ref(false)

// Real draft count from backend
const draftCount = ref(0)

const fetchDraftCount = async () => {
  try {
    const drafts = await postsStore.fetchPosts({ status: 'DRAFT' })
    draftCount.value = Array.isArray(drafts) ? drafts.length : 0
  } catch (err) {
    console.error('Failed to fetch draft count:', err)
    draftCount.value = 0
  }
}

onMounted(() => {
  fetchDraftCount()
})

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
