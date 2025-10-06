import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/store/auth'

// Lazy load views for better performance
const Home = () => import('@/views/Home.vue')
const About = () => import('@/views/About.vue')
const Blog = () => import('@/views/Blog.vue')
const BlogDetail = () => import('@/views/BlogDetail.vue')
const Resources = () => import('@/views/Resources.vue')
const Faqs = () => import('@/views/Faqs.vue')
const Partners = () => import('@/views/Partners.vue')
const Report = () => import('@/views/Report.vue')
const Contact = () => import('@/views/Contact.vue')
const Login = () => import('@/views/Login.vue')
const Operations = () => import('@/views/Operations.vue')
const ReportsInsights = () => import('@/views/ReportsInsights.vue')
const Articles = () => import('@/views/Videos.vue')
const Videos = () => import('@/views/Videos.vue')

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: {
      title: 'Sauti Child Helpline - Get Help Now',
      description: 'Support for children, GBV survivors, and migrant workers in Uganda',
    },
  },
  {
    path: '/operations',
    name: 'operations',
    component: Operations,
    meta: {
      title: 'Our Operations & Case Flow',
      description: 'How we handle every call with care and urgency',
    },
  },
  {
    path: '/reports',
    name: 'reports',
    component: ReportsInsights,
    meta: {
      title: 'Reports & Insights',
      description: 'Explore data and insights from Sauti Uganda',
    },
  },
  {
    path: '/videos',
    name: 'videos',
    component: Videos,
    meta: {
      title: 'Videos',
      description: 'Educational and awareness videos',
    },
  },
  {
    path: '/about',
    name: 'about',
    component: About,
    meta: {
      title: 'About Sauti',
      description: 'Learn about Sauti Child Helpline and our mission',
    },
  },
  {
    path: '/blog',
    name: 'blog',
    component: Blog,
    meta: {
      title: 'Blogs & Articles',
      description: 'Latest stories, updates, and insights from Sauti',
    },
  },
  {
    path: '/articles',
    name: 'articles',
    component: Articles,
    meta: {
      title: 'Articles',
      description: 'Featured articles and stories',
    },
  },
  {
    path: '/blog/:slug',
    name: 'blog-detail',
    component: BlogDetail,
    meta: {
      title: 'Blog Post',
    },
  },
  {
    path: '/resources',
    name: 'resources',
    component: Resources,
    meta: {
      title: 'Resources',
      description: 'Downloadable resources and guides',
    },
  },
  {
    path: '/faqs',
    name: 'faqs',
    component: Faqs,
    meta: {
      title: 'FAQs',
      description: 'Frequently asked questions',
    },
  },
  {
    path: '/partners',
    name: 'partners',
    component: Partners,
    meta: {
      title: 'Our Partners',
      description: 'Organizations supporting Sauti',
    },
  },
  {
    path: '/report',
    name: 'report',
    component: Report,
    meta: {
      title: 'Report a Case',
      description: 'Submit a confidential report anonymously',
    },
  },
  {
    path: '/contact',
    name: 'contact',
    component: Contact,
    meta: {
      title: 'Contact Us',
      description: 'Get in touch with Sauti',
    },
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {
      title: 'Staff Login',
      requiresGuest: true,
    },
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: () => import('@/views/NotFound.vue'),
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
  document.title = to.meta.title || 'Sauti Child Helpline'
  
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
