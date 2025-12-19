import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

// Lazy load components
const LoginView = () => import('@/views/LoginView.vue')
const DashboardLayout = () => import('@/components/DashboardLayout.vue')
const DashboardView = () => import('@/views/DashboardView.vue')
const PostsView = () => import('@/views/PostsView.vue')
const PostEditView = () => import('@/views/PostEditView.vue')
const VideosView = () => import('@/views/VideosView.vue')
const VideoEditView = () => import('@/views/VideoEditView.vue')
const SettingsView = () => import('@/views/SettingsView.vue')
const DraftsView = () => import('@/views/DraftsView.vue')
const ReportsView = () => import('@/views/ReportsView.vue')
const ReportDetailView = () => import('@/views/ReportDetailView.vue')
const ReportEditView = () => import('@/views/ReportEditView.vue')
const ResourcesView = () => import('@/views/ResourcesView.vue')
const FaqsView = () => import('@/views/FaqsView.vue')
const PartnersView = () => import('@/views/PartnersView.vue')
const UsersView = () => import('@/views/UsersView.vue')
const BlogsView = () => import('@/views/BlogsView.vue')
const UploadsView = () => import('@/views/UploadsView.vue')
const SocialMediaView = () => import('@/views/SocialMediaView.vue')
const ContentManagerView = () => import('@/views/ContentManager.vue')
const TimelineAdmin = () => import('@/views/TimelineAdmin.vue')
const ServiceAdmin = () => import('@/views/ServiceAdmin.vue')
const ContactAdmin = () => import('@/views/ContactAdmin.vue')
const CoreValuesAdmin = () => import('@/views/CoreValuesAdmin.vue')
const TeamAdmin = () => import('@/views/TeamAdmin.vue')
const ProtectionApproachAdmin = () => import('@/views/ProtectionApproachAdmin.vue')

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    meta: {
      requiresGuest: true,
      title: 'Login - Sauti Admin'
    }
  },
  {
    path: '/',
    component: DashboardLayout,
    meta: {
      requiresAuth: true
    },
    children: [
      {
        path: '',
        redirect: '/dashboard'
      },
      {
        path: 'dashboard',
        name: 'dashboard',
        component: DashboardView,
        meta: {
          title: 'Dashboard - Sauti Admin'
        }
      },
      {
        path: 'posts',
        name: 'posts',
        component: PostsView,
        meta: {
          title: 'Posts - Sauti Admin'
        }
      },
      {
        path: 'posts/create',
        name: 'post-create',
        component: PostEditView,
        meta: {
          title: 'Create Post - Sauti Admin'
        }
      },
      {
        path: 'posts/:slug/edit',
        name: 'post-edit',
        component: PostEditView,
        meta: {
          title: 'Edit Post - Sauti Admin'
        }
      },
      {
        path: 'drafts',
        name: 'drafts',
        component: DraftsView,
        meta: {
          title: 'Drafts - Sauti Admin'
        }
      },
      {
        path: 'videos',
        name: 'videos',
        component: VideosView,
        meta: {
          title: 'Videos - Sauti Admin'
        }
      },
      {
        path: 'videos/create',
        name: 'video-create',
        component: VideoEditView,
        meta: {
          title: 'Create Video - Sauti Admin'
        }
      },
      {
        path: 'videos/:id/edit',
        name: 'video-edit',
        component: VideoEditView,
        meta: {
          title: 'Edit Video - Sauti Admin'
        }
      },
      {
        path: 'settings',
        name: 'settings',
        component: SettingsView,
        meta: {
          title: 'Settings - Sauti Admin'
        }
      },
      {
        path: 'reports',
        name: 'reports',
        component: ReportsView,
        meta: {
          title: 'Active Reports - Sauti Admin'
        }
      },
      {
        path: 'reports/:id',
        name: 'report-detail',
        component: ReportDetailView,
        meta: {
          title: 'Report Details - Sauti Admin'
        }
      },
      {
        path: 'reports/:id/edit',
        name: 'report-edit',
        component: ReportEditView,
        meta: {
          title: 'Edit Report - Sauti Admin'
        }
      },
      {
        path: 'reports/urgent',
        name: 'reports-urgent',
        component: ReportsView,
        meta: {
          title: 'Urgent Cases - Sauti Admin'
        }
      },
      {
        path: 'reports/archive',
        name: 'reports-archive',
        component: ReportsView,
        meta: {
          title: 'Closed Cases - Sauti Admin'
        }
      },
      {
        path: 'resources',
        name: 'resources',
        component: ResourcesView,
        meta: {
          title: 'Resources - Sauti Admin'
        }
      },
      {
        path: 'faqs',
        name: 'faqs',
        component: FaqsView,
        meta: {
          title: 'FAQs - Sauti Admin'
        }
      },
      {
        path: 'partners',
        name: 'partners',
        component: PartnersView,
        meta: {
          title: 'Partners - Sauti Admin'
        }
      },
      {
        path: 'users',
        name: 'users',
        component: UsersView,
        meta: {
          title: 'Admin Users - Sauti Admin'
        }
      },
      {
        path: 'team',
        name: 'team-admin',
        component: TeamAdmin,
        meta: {
          title: 'Organization Team - Sauti Admin'
        }
      },
      {
        path: 'core-values',
        name: 'core-values-admin',
        component: CoreValuesAdmin,
        meta: {
          title: 'Core Values - Sauti Admin'
        }
      },
      {
        path: 'protection-approach',
        name: 'protection-approach-admin',
        component: ProtectionApproachAdmin,
        meta: {
          title: 'Protection Approach - Sauti Admin'
        }
      },
      {
        path: 'blogs',
        name: 'blogs',
        component: BlogsView,
        meta: {
          title: 'Blogs - Sauti Admin'
        }
      },
      {
        path: 'uploads',
        name: 'uploads',
        component: UploadsView,
        meta: {
          title: 'Frontend Content - Sauti Admin'
        }
      },
      {
        path: 'social-media',
        name: 'social-media',
        component: SocialMediaView,
        meta: {
          title: 'Social Media Posts - Sauti Admin'
        }
      },
      {
        path: '/content',
        name: 'ContentManager',
        component: ContentManagerView,
        meta: { requiresAuth: true }
      },
      {
        path: 'timeline',
        name: 'timeline-admin',
        component: TimelineAdmin,
        meta: {
          title: 'Timeline Events - Sauti Admin'
        }
      },
      {
        path: 'services',
        name: 'services-admin',
        component: ServiceAdmin,
        meta: {
          title: 'Services - Sauti Admin'
        }
      },
      {
        path: 'contacts',
        name: 'contacts-admin',
        component: ContactAdmin,
        meta: {
          title: 'Contact Info - Sauti Admin'
        }
      }
    ]
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/dashboard'
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }
    return { top: 0, behavior: 'smooth' }
  }
})

// Navigation guards
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()

  // Update page title
  document.title = to.meta.title || 'Sauti Admin Dashboard'

  // Check authentication requirements
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next({ name: 'login', query: { redirect: to.fullPath } })
  } else if (to.meta.requiresGuest && authStore.isAuthenticated) {
    next({ name: 'dashboard' })
  } else {
    next()
  }
})

export default router