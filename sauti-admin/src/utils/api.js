import axios from 'axios'
import { useAuthStore } from '@/stores/auth'
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
    const token = localStorage.getItem('admin_token')
    
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
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
          localStorage.removeItem('admin_token')
          localStorage.removeItem('admin_refresh_token')
          localStorage.removeItem('admin_user')
          
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
    profile: () => apiClient.get('/auth/profile/'),
    refreshToken: (refreshToken) => apiClient.post('/auth/token/refresh/', { refresh: refreshToken }),
  },
  
  // Dashboard endpoints
  dashboard: {
    stats: () => apiClient.get('/dashboard/stats/'),
    analytics: (params) => apiClient.get('/dashboard/analytics/', { params }),
    topContent: () => apiClient.get('/dashboard/top-content/'),
  },
  
  // Blog/Posts endpoints
  posts: {
    list: (params) => apiClient.get('/posts/', { params }),
    get: (slug) => apiClient.get(`/posts/${slug}/`),
    create: (data) => {
      const formData = new FormData()
      Object.keys(data).forEach(key => {
        if (key === 'tags' && Array.isArray(data[key])) {
          data[key].forEach(tag => formData.append('tags', tag))
        } else if (data[key] !== null && data[key] !== undefined) {
          formData.append(key, data[key])
        }
      })
      
      return apiClient.post('/posts/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
    },
    update: (slug, data) => {
      const formData = new FormData()
      Object.keys(data).forEach(key => {
        if (key === 'tags' && Array.isArray(data[key])) {
          data[key].forEach(tag => formData.append('tags', tag))
        } else if (data[key] !== null && data[key] !== undefined) {
          formData.append(key, data[key])
        }
      })
      
      return apiClient.put(`/posts/${slug}/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
    },
    delete: (slug) => apiClient.delete(`/posts/${slug}/`),
    categories: () => apiClient.get('/posts/categories/'),
    tags: () => apiClient.get('/posts/tags/'),
  },
  
  // Videos endpoints (assuming similar structure to posts)
  videos: {
    list: (params) => apiClient.get('/videos/', { params }),
    get: (id) => apiClient.get(`/videos/${id}/`),
    create: (data) => {
      const formData = new FormData()
      Object.keys(data).forEach(key => {
        if (data[key] !== null && data[key] !== undefined) {
          formData.append(key, data[key])
        }
      })
      
      return apiClient.post('/videos/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
    },
    update: (id, data) => {
      const formData = new FormData()
      Object.keys(data).forEach(key => {
        if (data[key] !== null && data[key] !== undefined) {
          formData.append(key, data[key])
        }
      })
      
      return apiClient.put(`/videos/${id}/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
    },
    delete: (id) => apiClient.delete(`/videos/${id}/`),
  },
  
  // Resources endpoints
  resources: {
    list: (params) => apiClient.get('/resources/', { params }),
    get: (slug) => apiClient.get(`/resources/${slug}/`),
    create: (data) => {
      const formData = new FormData()
      Object.keys(data).forEach(key => {
        if (data[key] !== null && data[key] !== undefined) {
          formData.append(key, data[key])
        }
      })
      
      return apiClient.post('/resources/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
    },
    update: (slug, data) => {
      const formData = new FormData()
      Object.keys(data).forEach(key => {
        if (data[key] !== null && data[key] !== undefined) {
          formData.append(key, data[key])
        }
      })
      
      return apiClient.put(`/resources/${slug}/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
    },
    delete: (slug) => apiClient.delete(`/resources/${slug}/`),
    categories: () => apiClient.get('/resources/categories/'),
  },
  
  // FAQs endpoints
  faqs: {
    list: (params) => apiClient.get('/faqs/', { params }),
    get: (id) => apiClient.get(`/faqs/${id}/`),
    create: (data) => apiClient.post('/faqs/', data),
    update: (id, data) => apiClient.put(`/faqs/${id}/`, data),
    delete: (id) => apiClient.delete(`/faqs/${id}/`),
    categories: () => apiClient.get('/faqs/categories/'),
  },
  
  // Partners endpoints
  partners: {
    list: (params) => apiClient.get('/partners/', { params }),
    get: (slug) => apiClient.get(`/partners/${slug}/`),
    create: (data) => {
      const formData = new FormData()
      Object.keys(data).forEach(key => {
        if (data[key] !== null && data[key] !== undefined) {
          formData.append(key, data[key])
        }
      })
      
      return apiClient.post('/partners/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
    },
    update: (slug, data) => {
      const formData = new FormData()
      Object.keys(data).forEach(key => {
        if (data[key] !== null && data[key] !== undefined) {
          formData.append(key, data[key])
        }
      })
      
      return apiClient.put(`/partners/${slug}/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
    },
    delete: (slug) => apiClient.delete(`/partners/${slug}/`),
  },
  
  // Reports endpoints (admin access)
  reports: {
    list: (params) => apiClient.get('/reports/list/', { params }),
    get: (id) => apiClient.get(`/reports/${id}/`),
    update: (id, data) => apiClient.put(`/reports/${id}/`, data),
    addFollowUp: (id, data) => apiClient.post(`/reports/${id}/followup/`, data),
  },
}

export default apiClient
