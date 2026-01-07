import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/store/auth'
import { useSettingsStore } from '@/store/settings'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/HomePage.vue'),
    meta: {
      title: 'Sauti 116 helpline - Get Help Now',
      description: 'Support for children, GBV survivors, and migrant workers in Uganda',
    },
  },
  {
    path: '/privacy',
    name: 'privacy',
    component: () => import('@/views/PrivacyPage.vue'),
    meta: {
      title: 'Privacy Policy',
      description: 'How Sauti protects your data and confidentiality',
    },
  },
  {
    path: '/terms',
    name: 'terms',
    component: () => import('@/views/TermsPage.vue'),
    meta: {
      title: 'Terms of Service',
      description: 'Rules for using Sauti services and this website',
    },
  },
  {
    path: '/accessibility',
    name: 'accessibility',
    component: () => import('@/views/AccessibilityPage.vue'),
    meta: {
      title: 'Accessibility Statement',
      description: 'Our commitment to making our services accessible to everyone',
    },
  },
  {
    path: '/operations',
    name: 'operations',
    component: () => import('@/views/OperationsPage.vue'),
    meta: {
      title: 'Our Operations & Case Flow',
      description: 'How we handle every call with care and urgency',
    },
  },
  {
    path: '/reports',
    name: 'reports',
    component: () => import('@/views/ReportsInsightsPage.vue'),
    meta: {
      title: 'Reports & Insights',
      description: 'Explore data and insights from Sauti Uganda',
    },
  },
  {
    path: '/videos',
    name: 'videos',
    component: () => import('@/views/VideosPage.vue'),
    meta: {
      title: 'Videos',
      description: 'Educational and awareness videos',
    },
  },
  {
    path: '/about',
    name: 'AboutPage',
    component: () => import('@/views/AboutPage.vue')
  },

  {
    path: '/blogs',
    name: 'blog',
    component: () => import('@/views/BlogPage.vue'),
    meta: {
      title: 'Updates',
      description: 'Official updates, impact reports, and protection news from Sauti 116',
    },
  },
  {
    path: '/news',
    name: 'news',
    component: () => import('@/views/NewsPage.vue'),
    meta: {
      title: 'News',
      description: 'Official news and updates from Sauti',
    },
  },

  {
    path: '/blogs/:slug',
    name: 'blog-detail',
    component: () => import('@/views/BlogDetailPage.vue'),
    meta: {
      title: 'Success Story',
    },
  },
  {
    path: '/resources',
    name: 'resources',
    component: () => import('@/views/ResourcesPage.vue'),
    meta: {
      title: 'Resources',
      description: 'Downloadable resources and guides',
    },
  },
  {
    path: '/faqs',
    name: 'faqs',
    component: () => import('@/views/FaqsPage.vue'),
    meta: {
      title: 'FAQs',
      description: 'Frequently asked questions',
    },
  },
  {
    path: '/partners',
    name: 'partners',
    component: () => import('@/views/PartnersPage.vue'),
    meta: {
      title: 'Our Partners',
      description: 'Organizations supporting Sauti',
    },
  },
  {
    path: '/report',
    name: 'report',
    component: () => import('@/views/ReportPage.vue'),
    meta: {
      title: 'Report a Case',
      description: 'Submit a confidential report anonymously',
    },
  },
  {
    path: '/contact',
    name: 'contact',
    component: () => import('@/views/ContactPage.vue'),
    meta: {
      title: 'Contact Us',
      description: 'Get in touch with Sauti',
    },
  },
  {
    path: '/donate',
    name: 'donate',
    component: () => import('@/views/DonatePage.vue'),
    meta: {
      title: 'Donate',
      description: 'Support Sauti 116 helpline and make a difference',
    },
  },

  {
    path: '/get-help/:service',
    name: 'get-help-redirect',
    redirect: to => {
      return { path: '/', hash: `#${to.params.service}` }
    }
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/LoginPage.vue'),
    meta: {
      title: 'Staff Login',
      requiresGuest: true,
    },
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: () => import('@/views/NotFoundPage.vue'),
    meta: {
      title: '404 - Page Not Found',
    },
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    // Scroll to saved position if available (back/forward navigation)
    if (savedPosition) {
      return savedPosition
    }

    // Scroll to anchor if present
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
      }
    }

    // Scroll to top for new pages
    return { top: 0, behavior: 'smooth' }
  },
})

// Navigation guards
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  const settingsStore = useSettingsStore()

  // Update page title
  const suffix = settingsStore.settings?.default_meta_title_suffix || ' | Sauti'
  const baseTitle = to.meta.title || 'Sauti 116 helpline'

  // If the title doesn't already contain the suffix (or similar), append it
  // This is a simple check, might need refinement
  if (baseTitle.includes('| Sauti')) {
    document.title = baseTitle
  } else {
    document.title = `${baseTitle}${suffix}`
  }

  // Update meta description
  const descriptionTag = document.querySelector('meta[name="description"]')
  if (descriptionTag) {
    const desc = to.meta.description || settingsStore.settings?.default_meta_description || 'Sauti 116 helpline'
    descriptionTag.setAttribute('content', desc)
  }

  // Check authentication requirements
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next({ name: 'login', query: { redirect: to.fullPath } })
  } else if (to.meta.requiresGuest && authStore.isAuthenticated) {
    next({ name: 'home' })
  } else if (to.meta.requiresAdmin && !authStore.isAdmin) {
    next({ name: 'home' })
  } else {
    next()
  }
})

// Global error handler
router.onError((error) => {
  console.error('Router error:', error)
})

export default router
