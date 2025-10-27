import axios from 'axios'
import { useAuthStore } from '@/stores/auth'
import router from '@/router'

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL || '/api',
  timeout: 15000,
  headers: {
    'Content-Type': 'application/json',
  },
})

const createFormData = (data) => {
  const formData = new FormData()
  Object.keys(data).forEach(key => {
    if (key === 'tags' && Array.isArray(data[key])) {
      data[key].forEach(tag => formData.append('tags', tag))
    } else if (data[key] !== null && data[key] !== undefined) {
      formData.append(key, data[key])
    }
  })
  return formData
}

apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('admin_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('admin_token')
      localStorage.removeItem('admin_refresh_token')
      localStorage.removeItem('admin_user')
      if (router.currentRoute.value.path !== '/login') {
        router.push('/login')
      }
    }
    return Promise.reject(error)
  }
)

export const api = {
  get: (url, config) => apiClient.get(url, config),
  post: (url, data, config) => apiClient.post(url, data, config),
  put: (url, data, config) => apiClient.put(url, data, config),
  patch: (url, data, config) => apiClient.patch(url, data, config),
  delete: (url, config) => apiClient.delete(url, config),
  
  auth: {
    login: (credentials) => apiClient.post('/auth/login/', credentials),
    profile: () => apiClient.get('/auth/profile/'),
    refreshToken: (refreshToken) => apiClient.post('/auth/token/refresh/', { refresh: refreshToken }),
  },
  
  dashboard: {
    stats: () => apiClient.get('/dashboard/stats/'),
    analytics: (params) => apiClient.get('/dashboard/analytics/', { params }),
    topContent: () => apiClient.get('/dashboard/top-content/'),
  },
  
  posts: {
    list: (params) => apiClient.get('/posts/', { params }),
    get: (slug) => apiClient.get(`/posts/${slug}/`),
    create: (data) => apiClient.post('/posts/', createFormData(data), {
      headers: { 'Content-Type': 'multipart/form-data' }
    }),
    update: (slug, data) => apiClient.put(`/posts/${slug}/`, createFormData(data), {
      headers: { 'Content-Type': 'multipart/form-data' }
    }),
    delete: (slug) => apiClient.delete(`/posts/${slug}/`),
    categories: () => apiClient.get('/posts/categories/'),
    tags: () => apiClient.get('/posts/tags/'),
  },
  
  videos: {
    list: (params) => apiClient.get('/videos/', { params }),
    get: (slug) => apiClient.get(`/videos/${slug}/`),
    create: (data) => apiClient.post('/videos/', createFormData(data), {
      headers: { 'Content-Type': 'multipart/form-data' }
    }),
    update: (slug, data) => apiClient.put(`/videos/${slug}/`, createFormData(data), {
      headers: { 'Content-Type': 'multipart/form-data' }
    }),
    delete: (slug) => apiClient.delete(`/videos/${slug}/`),
  },
  
  resources: {
    list: (params) => apiClient.get('/resources/', { params }),
    get: (slug) => apiClient.get(`/resources/${slug}/`),
    create: (data) => apiClient.post('/resources/', createFormData(data), {
      headers: { 'Content-Type': 'multipart/form-data' }
    }),
    update: (slug, data) => apiClient.put(`/resources/${slug}/`, createFormData(data), {
      headers: { 'Content-Type': 'multipart/form-data' }
    }),
    delete: (slug) => apiClient.delete(`/resources/${slug}/`),
    categories: () => apiClient.get('/resources/categories/'),
  },
  
  faqs: {
    list: (params) => apiClient.get('/faqs/', { params }),
    get: (id) => apiClient.get(`/faqs/${id}/`),
    create: (data) => apiClient.post('/faqs/', data),
    update: (id, data) => apiClient.put(`/faqs/${id}/`, data),
    delete: (id) => apiClient.delete(`/faqs/${id}/`),
    categories: () => apiClient.get('/faqs/categories/'),
  },
  
  partners: {
    list: (params) => apiClient.get('/partners/', { params }),
    get: (slug) => apiClient.get(`/partners/${slug}/`),
    create: (data) => apiClient.post('/partners/', createFormData(data), {
      headers: { 'Content-Type': 'multipart/form-data' }
    }),
    update: (slug, data) => apiClient.put(`/partners/${slug}/`, createFormData(data), {
      headers: { 'Content-Type': 'multipart/form-data' }
    }),
    delete: (slug) => apiClient.delete(`/partners/${slug}/`),
  },
  
  reports: {
    list: (params) => apiClient.get('/reports/list/', { params }),
    get: (id) => apiClient.get(`/reports/${id}/`),
    update: (id, data) => apiClient.put(`/reports/${id}/`, data),
    addFollowUp: (id, data) => apiClient.post(`/reports/${id}/followup/`, data),
  },
}

export default apiClient
