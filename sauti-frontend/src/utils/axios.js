import axios from 'axios'
import { useAuthStore } from '@/store/auth'
import router from '@/router'

// Create axios instance
const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api',
  timeout: 15000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor - Add JWT token if available
apiClient.interceptors.request.use(
  (config) => {
    const authStore = useAuthStore()
    
    if (authStore.token) {
      config.headers.Authorization = `Bearer ${authStore.token}`
    }
    
    // Log request in development
    if (import.meta.env.DEV) {
      console.log(`🚀 API Request: ${config.method?.toUpperCase()} ${config.url}`)
    }
    
    return config
  },
  (error) => {
    console.error('❌ Request Error:', error)
    return Promise.reject(error)
  }
)

// Response interceptor - Handle errors globally
apiClient.interceptors.response.use(
  (response) => {
    // Log response in development
    if (import.meta.env.DEV) {
      console.log(`✅ API Response: ${response.config.url}`, response.data)
    }
    return response
  },
  (error) => {
    // Handle different error status codes
    if (error.response) {
      const status = error.response.status
      
      switch (status) {
        case 401:
          // Unauthorized - clear auth and redirect to login
          console.error('❌ 401 Unauthorized')
          const authStore = useAuthStore()
          authStore.logout()
          
          // Only redirect if not already on login page
          if (router.currentRoute.value.path !== '/login') {
            router.push('/login')
          }
          break
          
        case 403:
          console.error('❌ 403 Forbidden')
          break
          
        case 404:
          console.error('❌ 404 Not Found')
          break
          
        case 500:
          console.error('❌ 500 Server Error')
          break
          
        default:
          console.error(`❌ ${status} Error:`, error.response.data)
      }
    } else if (error.request) {
      // Request made but no response
      console.error('❌ Network Error: No response received')
    } else {
      // Error in request setup
      console.error('❌ Request Setup Error:', error.message)
    }
    
    return Promise.reject(error)
  }
)

// API methods
export const api = {
  // Generic methods
  get: (url, config) => apiClient.get(url, config),
  post: (url, data, config) => apiClient.post(url, data, config),
  put: (url, data, config) => apiClient.put(url, data, config),
  patch: (url, data, config) => apiClient.patch(url, data, config),
  delete: (url, config) => apiClient.delete(url, config),
  
  // Auth endpoints
  auth: {
    login: (credentials) => apiClient.post('/auth/login/', credentials),
    register: (userData) => apiClient.post('/auth/register/', userData),
    profile: () => apiClient.get('/auth/profile/'),
    updateProfile: (data) => apiClient.put('/auth/profile/', data),
    refreshToken: (refreshToken) => apiClient.post('/auth/token/refresh/', { refresh: refreshToken }),
  },
  
  // Blog/Posts endpoints
  posts: {
    list: (params) => apiClient.get('/posts/', { params }),
    get: (slug) => apiClient.get(`/posts/${slug}/`),
    create: (data) => apiClient.post('/posts/', data),
    update: (slug, data) => apiClient.put(`/posts/${slug}/`, data),
    delete: (slug) => apiClient.delete(`/posts/${slug}/`),
    categories: () => apiClient.get('/posts/categories/'),
    tags: () => apiClient.get('/posts/tags/'),
  },
  
  // Videos endpoints
  videos: {
    list: (params) => apiClient.get('/videos/', { params }),
    get: (slug) => apiClient.get(`/videos/${slug}/`),
    categories: () => apiClient.get('/videos/categories/'),
  },
  
  // Resources endpoints
  resources: {
    list: (params) => apiClient.get('/resources/', { params }),
    get: (slug) => apiClient.get(`/resources/${slug}/`),
    categories: () => apiClient.get('/resources/categories/'),
  },
  
  // FAQs endpoints
  faqs: {
    list: (params) => apiClient.get('/faqs/', { params }),
    get: (id) => apiClient.get(`/faqs/${id}/`),
    categories: () => apiClient.get('/faqs/categories/'),
  },
  
  // Partners endpoints
  partners: {
    list: () => apiClient.get('/partners/'),
    get: (slug) => apiClient.get(`/partners/${slug}/`),
  },
  
  // Reports endpoints (anonymous submission)
  reports: {
    submit: (data) => {
      // Use FormData for file upload
      const formData = new FormData()
      Object.keys(data).forEach(key => {
        if (data[key] !== null && data[key] !== undefined) {
          formData.append(key, data[key])
        }
      })
      
      return apiClient.post('/reports/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
    },
    list: (params) => apiClient.get('/reports/list/', { params }),
    get: (id) => apiClient.get(`/reports/${id}/`),
    update: (id, data) => apiClient.put(`/reports/${id}/`, data),
    addFollowUp: (id, data) => apiClient.post(`/reports/${id}/followup/`, data),
  },
}

export default apiClient
