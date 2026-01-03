<template>
  <div class="flex h-screen bg-white">
    <!-- Enhanced Sidebar -->
    <div
      class="fixed inset-y-0 left-0 z-50 w-72 bg-white shadow-2xl transform transition-transform duration-300 ease-in-out lg:translate-x-0 lg:static lg:inset-0 border-r border-gray-200"
      :class="{ '-translate-x-full': !sidebarOpen }">
      <div class="flex flex-col h-full">
        <!-- Enhanced Logo -->
        <div class="flex items-center justify-between h-20 px-6 bg-transparent">
          <div class="flex items-center space-x-3">
            <div class="h-16 w-16 flex items-center justify-center">
              <img :src="sautiLogo" alt="Sauti Logo" class="h-full w-full object-contain" />
            </div>
            <div>
              <h1 class="text-xl font-bold" style="font-family: 'Roboto', sans-serif; color: #222222;">Sauti Admin</h1>
              <p class="text-xs" style="color: #555555;">116 helpline CMS</p>
            </div>
          </div>
          <button @click="sidebarOpen = false"
            class="lg:hidden p-2 rounded-xl text-gray-600 hover:text-gray-900 hover:bg-gray-100 transition-all duration-300">
            <XMarkIcon class="h-6 w-6" />
          </button>
        </div>

        <!-- Enhanced Quick Actions -->
        <div class="px-4 py-6 space-y-3">
          <router-link to="/posts/create"
            class="w-full btn-primary justify-center gap-2 text-sm shadow-lg hover:shadow-xl">
            <PlusCircleIcon class="h-5 w-5" />
            New Blog Post
          </router-link>

          <router-link to="/videos/create"
            class="w-full btn-secondary justify-center gap-2 text-sm border border-transparent hover:border-[#E68A00]">
            <VideoCameraIcon class="h-5 w-5" />
            New Video
          </router-link>
        </div>

        <!-- Enhanced Navigation -->
        <!-- Enhanced Navigation -->
        <nav class="flex-1 px-4 py-6 space-y-8 overflow-y-auto">

          <!-- Overview & Operations -->
          <div>
            <h3 class="px-3 text-xs font-bold uppercase tracking-wider mb-4 flex items-center" style="color: #64748b;">
              <div class="w-2 h-2 rounded-full mr-2 bg-slate-400"></div>
              Overview & Operations
            </h3>
            <div class="space-y-2">
              <router-link to="/dashboard" class="sidebar-link group" :class="{ active: $route.path === '/dashboard' }">
                <Squares2X2Icon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path === '/dashboard' ? 'text-white' : 'text-blue-500 group-hover:text-blue-600'
                ]" />
                <span class="flex-1">Dashboard</span>
              </router-link>

              <router-link to="/reports" class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/reports') }">
                <ShieldExclamationIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/reports') ? 'text-white' : 'text-red-500 group-hover:text-red-600'
                ]" />
                <span class="flex-1">Reports & Cases</span>
              </router-link>
            </div>
          </div>

          <!-- Central Content Management Hub -->
          <div>
            <div class="flex items-center justify-between mb-4 px-3">
              <h3 class="text-xs font-bold uppercase tracking-wider flex items-center" style="color: #0F172A;">
                <div class="w-2 h-2 rounded-full mr-2 bg-blue-600"></div>
                Content Management
              </h3>
            </div>

            <div class="space-y-2">
              <!-- THE HUB -->
              <router-link to="/content-hub"
                class="sidebar-link group bg-blue-50 border-blue-100 hover:bg-blue-100 mb-4"
                :class="{ active: $route.path === '/content-hub' }">
                <WrenchScrewdriverIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path === '/content-hub' ? 'text-white' : 'text-blue-700'
                ]" />
                <span class="flex-1 font-bold">CONTENT HUB</span>
              </router-link>

              <!-- Editorial Group -->
              <div class="pt-2 pb-1 px-3 text-[10px] font-bold text-gray-400 uppercase tracking-widest">Editorial &
                Media</div>

              <router-link to="/posts" class="sidebar-link group" :class="{ active: $route.path.startsWith('/posts') }">
                <DocumentTextIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/posts') ? 'text-white' : 'text-orange-500 group-hover:text-orange-600'
                ]" />
                <span class="flex-1">Blog Posts</span>
                <span v-if="draftCount > 0"
                  class="text-[10px] font-bold px-1.5 py-0.5 rounded bg-orange-100 text-orange-700">
                  {{ draftCount }} DRAFTS
                </span>
              </router-link>

              <router-link to="/videos" class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/videos') }">
                <VideoCameraIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/videos') ? 'text-white' : 'text-purple-500 group-hover:text-purple-600'
                ]" />
                <span class="flex-1">Videos</span>
              </router-link>

              <router-link to="/resources" class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/resources') }">
                <FolderOpenIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/resources') ? 'text-white' : 'text-teal-500 group-hover:text-teal-600'
                ]" />
                <span class="flex-1">Resources</span>
              </router-link>

              <router-link to="/uploads" class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/uploads') }">
                <PhotoIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/uploads') ? 'text-white' : 'text-indigo-500 group-hover:text-indigo-600'
                ]" />
                <span class="flex-1">Media Library</span>
              </router-link>

              <!-- Site Structure Group -->
              <div class="pt-4 pb-1 px-3 text-[10px] font-bold text-gray-400 uppercase tracking-widest">Site Structure
              </div>

              <router-link to="/content" class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/content') }">
                <HomeIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/content') ? 'text-white' : 'text-blue-500'
                ]" />
                <span class="flex-1">Page Content</span>
              </router-link>

              <router-link to="/services" class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/services') }">
                <CubeIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/services') ? 'text-white' : 'text-cyan-500'
                ]" />
                <span class="flex-1">Help Services</span>
              </router-link>

              <router-link to="/faqs" class="sidebar-link group" :class="{ active: $route.path.startsWith('/faqs') }">
                <QuestionMarkCircleIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/faqs') ? 'text-white' : 'text-green-500'
                ]" />
                <span class="flex-1">FAQs</span>
              </router-link>

              <router-link to="/feedback" class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/feedback') }">
                <ChatBubbleLeftRightIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/feedback') ? 'text-white' : 'text-indigo-500'
                ]" />
                <span class="flex-1">General Feedback</span>
              </router-link>



              <router-link to="/partners" class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/partners') }">
                <HandThumbUpIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/partners') ? 'text-white' : 'text-yellow-500'
                ]" />
                <span class="flex-1">Partners</span>
              </router-link>

              <!-- About Details Group -->
              <div class="pt-4 pb-1 px-3 text-[10px] font-bold text-gray-400 uppercase tracking-widest">About Page
                Details</div>

              <router-link to="/team" class="sidebar-link group" :class="{ active: $route.path.startsWith('/team') }">
                <UserGroupIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/team') ? 'text-white' : 'text-rose-500'
                ]" />
                <span class="flex-1">Organization Team</span>
              </router-link>

              <router-link to="/timeline" class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/timeline') }">
                <ClockIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/timeline') ? 'text-white' : 'text-amber-500'
                ]" />
                <span class="flex-1">Timeline Events</span>
              </router-link>

              <router-link to="/core-values" class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/core-values') }">
                <HeartIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/core-values') ? 'text-white' : 'text-pink-500'
                ]" />
                <span class="flex-1">Core Values</span>
              </router-link>

              <router-link to="/protection-approach" class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/protection-approach') }">
                <ShieldCheckIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/protection-approach') ? 'text-white' : 'text-emerald-500'
                ]" />
                <span class="flex-1">Protection Approach</span>
              </router-link>

              <!-- Connectivity Group -->
              <div class="pt-4 pb-1 px-3 text-[10px] font-bold text-gray-400 uppercase tracking-widest">Connectivity
              </div>

              <router-link to="/social-media" class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/social-media') }">
                <ShareIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/social-media') ? 'text-white' : 'text-sky-500'
                ]" />
                <span class="flex-1">Profiles & Social</span>
              </router-link>
            </div>
          </div>

          <!-- System Settings -->
          <div>
            <h3 class="px-3 text-xs font-bold uppercase tracking-wider mb-4 flex items-center" style="color: #64748b;">
              <div class="w-2 h-2 rounded-full mr-2 bg-slate-400"></div>
              System & Configuration
            </h3>
            <div class="space-y-2">
              <router-link to="/users" class="sidebar-link group" :class="{ active: $route.path.startsWith('/users') }">
                <UsersIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/users') ? 'text-white' : 'text-slate-500 group-hover:text-slate-700'
                ]" />
                <span class="flex-1">Admin Users</span>
              </router-link>

              <router-link to="/settings" class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/settings') }">
                <CogIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/settings') ? 'text-white' : 'text-slate-500 group-hover:text-slate-700'
                ]" />
                <span class="flex-1">System Settings</span>
              </router-link>

              <router-link to="/legal-footer" class="sidebar-link group"
                :class="{ active: $route.path.startsWith('/legal-footer') }">
                <ScaleIcon :class="[
                  'h-5 w-5 mr-3 transition-colors duration-300',
                  $route.path.startsWith('/legal-footer') ? 'text-white' : 'text-slate-500 group-hover:text-slate-700'
                ]" />
                <span class="flex-1">Legal & Footer</span>
              </router-link>
            </div>
          </div>
        </nav>

        <!-- Enhanced User Info & Logout -->
        <div class="p-6 bg-white">
          <div class="flex items-center mb-4">
            <div class="flex-shrink-0">
              <div class="h-12 w-12 rounded-2xl flex items-center justify-center shadow-lg"
                style="background-color: #009EDB;">
                <span class="text-white text-lg font-bold">
                  {{ userInitials }}
                </span>
              </div>
            </div>
            <div class="ml-4">
              <p class="text-sm font-bold" style="font-family: 'Poppins', sans-serif; color: #222222;">{{
                authStore.userFullName }}</p>
              <p class="text-xs font-medium" style="color: #555555;">{{ authStore.user?.role }}</p>
            </div>
          </div>

          <button @click="handleLogout"
            class="flex items-center w-full px-4 py-3 text-sm rounded-xl transition-all duration-300 font-semibold border"
            :style="{
              color: isHoveringLogout ? '#CC0000' : '#222222',
              borderColor: isHoveringLogout ? '#CC0000' : '#DDDDDD',
              backgroundColor: isHoveringLogout ? 'rgba(236, 0, 0, 0.08)' : '#FFFFFF'
            }" @mouseover="isHoveringLogout = true" @mouseleave="isHoveringLogout = false">
            <ArrowRightOnRectangleIcon class="h-5 w-5 mr-3 transition-colors duration-300"
              :class="isHoveringLogout ? 'text-[#CC0000]' : 'text-[#EC0000]'" />
            <span>Logout</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Enhanced Main content -->
    <div class="flex-1 flex flex-col overflow-hidden lg:ml-0">
      <!-- Enhanced Mobile header -->
      <div class="lg:hidden bg-white shadow-lg" style="border-bottom: 1px solid #E6E6E6;">
        <div class="flex items-center justify-between h-16 px-4">
          <button @click="sidebarOpen = true" class="p-3 rounded-xl transition-all duration-300"
            style="color: #009EDB;">
            <Bars3Icon class="h-6 w-6" />
          </button>
          <h1 class="text-lg font-bold" style="font-family: 'Roboto', sans-serif; color: #222222;">{{ pageTitle }}</h1>
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
    <div v-if="sidebarOpen" class="fixed inset-0 z-40 lg:hidden" @click="sidebarOpen = false">
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
  import sautiLogo from '@/assets/sauti-logo.jpeg'
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
    UsersIcon,
    ShieldExclamationIcon,
    ShieldCheckIcon,
    PhotoIcon,
    ShareIcon,
    BookOpenIcon,
    WrenchScrewdriverIcon,
    ClockIcon,
    CubeIcon,
    PhoneIcon,
    HandThumbUpIcon,
    HomeIcon,
    HeartIcon,
    ScaleIcon,
    ChatBubbleLeftRightIcon
  } from '@heroicons/vue/24/outline'

  const router = useRouter()
  const route = useRoute()
  const authStore = useAuthStore()
  const postsStore = usePostsStore()
  const toast = useToast()

  const sidebarOpen = ref(false)
  const isHoveringLogout = ref(false)

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
      '/content-hub': 'Content Management Hub',
      '/posts': 'Blog Posts',
      '/videos': 'Videos',
      '/settings': 'System Settings',
      '/reports': 'Reports & Case Management',
      '/social-media': 'Social Media',
      '/site-settings': 'Site Settings'
    }

    // Check for exact matches first
    if (routeNames[route.path]) {
      return routeNames[route.path]
    }

    // Check for partial matches
    if (route.path.startsWith('/reports')) return 'Reports'
    if (route.path.startsWith('/posts')) return 'Blogs'
    if (route.path.startsWith('/videos')) return 'Videos'
    if (route.path.startsWith('/social-media')) return 'Social Media'
    if (route.path.startsWith('/site-settings')) return 'Site Settings' // Added for Site Settings

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