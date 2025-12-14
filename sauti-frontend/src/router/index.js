import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/store/auth'

// Lazy load views for better performance
import HomePage from '@/views/HomePage.vue'
import AboutPage from '@/views/AboutPage.vue'
import BlogPage from '@/views/BlogPage.vue'
import BlogDetailPage from '@/views/BlogDetailPage.vue'
import ResourcesPage from '@/views/ResourcesPage.vue'
import FaqsPage from '@/views/FaqsPage.vue'
import PartnersPage from '@/views/PartnersPage.vue'
import ReportPage from '@/views/ReportPage.vue'
import ContactPage from '@/views/ContactPage.vue'
import DonatePage from '@/views/DonatePage.vue'
import LoginPage from '@/views/LoginPage.vue'
import OperationsPage from '@/views/OperationsPage.vue'
import ReportsInsightsPage from '@/views/ReportsInsightsPage.vue'
import VideosPage from '@/views/VideosPage.vue'
import PrivacyPage from '@/views/PrivacyPage.vue'
import TermsPage from '@/views/TermsPage.vue'
import AccessibilityPage from '@/views/AccessibilityPage.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage,
    meta: {
      title: 'Sauti 116 helpline - Get Help Now',
      description: 'Support for children, GBV survivors, and migrant workers in Uganda',
    },
  },
  {
    path: '/privacy',
    name: 'privacy',
    component: PrivacyPage,
    meta: {
      title: 'Privacy Policy',
      description: 'How Sauti protects your data and confidentiality',
    },
  },
  {
    path: '/terms',
    name: 'terms',
    component: TermsPage,
    meta: {
      title: 'Terms of Service',
      description: 'Rules for using Sauti services and this website',
    },
  },
  {
    path: '/accessibility',
    name: 'accessibility',
    component: AccessibilityPage,
    meta: {
      title: 'Accessibility Statement',
      description: 'Our commitment to making our services accessible to everyone',
    },
  },
  {
    path: '/operations',
    name: 'operations',
    component: OperationsPage,
    meta: {
      title: 'Our Operations & Case Flow',
      description: 'How we handle every call with care and urgency',
    },
  },
  {
    path: '/reports',
    name: 'reports',
    component: ReportsInsightsPage,
    meta: {
      title: 'Reports & Insights',
      description: 'Explore data and insights from Sauti Uganda',
    },
  },
  {
    path: '/videos',
    name: 'videos',
    component: VideosPage,
    meta: {
      title: 'Videos',
      description: 'Educational and awareness videos',
    },
  },
  {
    path: '/about',
    name: 'AboutPage',
    component: AboutPage
  },

  {
    path: '/blogs',
    name: 'blog',
    component: BlogPage,
    meta: {
      title: 'Blogs',
      description: 'Latest stories, updates, and insights from Sauti',
    },
  },
  {
    path: '/articles',
    name: 'articles',
    component: VideosPage, // Assuming Articles also uses VideosPage
    meta: {
      title: 'Articles',
      description: 'Featured articles and stories',
    },
  },
  {
    path: '/blogs/:slug',
    name: 'blog-detail',
    component: BlogDetailPage,
    meta: {
      title: 'Success Story',
    },
  },
  {
    path: '/resources',
    name: 'resources',
    component: ResourcesPage,
    meta: {
      title: 'Resources',
      description: 'Downloadable resources and guides',
    },
  },
  {
    path: '/faqs',
    name: 'faqs',
    component: FaqsPage,
    meta: {
      title: 'FAQs',
      description: 'Frequently asked questions',
    },
  },
  {
    path: '/partners',
    name: 'partners',
    component: PartnersPage,
    meta: {
      title: 'Our Partners',
      description: 'Organizations supporting Sauti',
    },
  },
  {
    path: '/report',
    name: 'report',
    component: ReportPage,
    meta: {
      title: 'Report a Case',
      description: 'Submit a confidential report anonymously',
    },
  },
  {
    path: '/contact',
    name: 'contact',
    component: ContactPage,
    meta: {
      title: 'Contact Us',
      description: 'Get in touch with Sauti',
    },
  },
  {
    path: '/donate',
    name: 'donate',
    component: DonatePage,
    meta: {
      title: 'Donate',
      description: 'Support Sauti 116 helpline and make a difference',
    },
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage,
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

  // Update page title
  document.title = to.meta.title || 'Sauti 116 helpline'

  // Update meta description
  const descriptionTag = document.querySelector('meta[name="description"]')
  if (descriptionTag && to.meta.description) {
    descriptionTag.setAttribute('content', to.meta.description)
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
