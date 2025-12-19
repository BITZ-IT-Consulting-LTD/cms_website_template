import axios from 'axios'
import { useAuthStore } from '@/stores/auth'
import router from '@/router'

console.log('Vite Environment Variables:', import.meta.env);

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 15000,
  headers: {
    'Content-Type': 'application/json',
  },
})

const createFormData = (data) => {
  const formData = new FormData()
  Object.keys(data).forEach(key => {
    const value = data[key]
    
    // Skip null, undefined, or empty strings for optional fields
    if (value === null || value === undefined) {
      return
    }
    
    // Handle tags array - only append if array has items
    if (key === 'tags') {
      if (Array.isArray(value) && value.length > 0) {
        value.forEach(tag => {
          // Only append if tag is a valid ID (number or string number)
          const tagId = typeof tag === 'number' ? tag : parseInt(tag, 10)
          if (!isNaN(tagId) && tagId > 0) {
            formData.append('tags', tagId)
          }
        })
      }
      // If tags is empty array or null/undefined, skip it completely
      return
    }
    
    // Handle file fields - only append if it's a File object
    const fileFields = ['featured_image', 'thumbnail', 'file', 'image', 'photo', 'video_file']
    if (fileFields.includes(key)) {
      if (value instanceof File) {
        formData.append(key, value)
      }
      // If it's a string (existing URL), skip it - backend will keep existing file
      return
    }
    
    // Handle category and category_id - ensure it's a number and skip if invalid
    if (key === 'category' || key === 'category_id') {
      if (value === null || value === '' || value === undefined) {
        return
      }
      // Ensure category is sent as a number (FormData will convert to string)
      const categoryId = typeof value === 'number' ? value : parseInt(value, 10)
      if (!isNaN(categoryId) && categoryId > 0) {
        formData.append(key, categoryId.toString())
      }
      return
    }
    
    // Handle empty strings for optional fields - convert to empty string or skip
    if (value === '' && ['excerpt', 'slug'].includes(key)) {
      // Allow empty strings for these optional fields
      formData.append(key, '')
      return
    }
    
    // Skip empty strings for other optional fields
    if (value === '') {
      return
    }
    
    // Handle boolean values - Django expects 'true'/'false' or '1'/'0'
    if (typeof value === 'boolean') {
      formData.append(key, value ? 'true' : 'false')
      return
    }
    
    // Handle number values
    if (typeof value === 'number') {
      formData.append(key, value.toString())
      return
    }
    
    // Handle empty strings for optional text fields
    if (value === '' && ['description', 'youtube_url'].includes(key)) {
      // Allow empty strings for these optional fields
      formData.append(key, '')
      return
    }
    
    // For all other fields, append the value as-is (FormData handles strings)
    formData.append(key, value)
  })
  return formData
}

apiClient.interceptors.request.use(
  (config) => {
    const authStore = useAuthStore() // Use the auth store
    const token = authStore.token // Get token from the store
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
    categories: {
      list: () => apiClient.get('/posts/categories/'),
      create: (data) => apiClient.post('/posts/categories/', data),
      update: (id, data) => apiClient.put(`/posts/categories/${id}/`, data).catch(() => {
        // Fallback to PATCH if PUT not supported
        return apiClient.patch(`/posts/categories/${id}/`, data)
      }),
      delete: (id) => apiClient.delete(`/posts/categories/${id}/`).catch(() => {
        // Handle gracefully if endpoint doesn't exist
        return Promise.reject(new Error('Delete endpoint not available'))
      }),
    },
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
    categories: {
      list: () => apiClient.get('/videos/categories/'),
      create: (data) => apiClient.post('/videos/categories/', data),
      update: (id, data) => apiClient.put(`/videos/categories/${id}/`, data).catch(() => {
        // Fallback to PATCH if PUT not supported
        return apiClient.patch(`/videos/categories/${id}/`, data)
      }),
      delete: (id) => apiClient.delete(`/videos/categories/${id}/`).catch(() => {
        // Handle gracefully if endpoint doesn't exist
        return Promise.reject(new Error('Delete endpoint not available'))
      }),
    },
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
    categories: {
      list: () => apiClient.get('/resources/categories/'),
      create: (data) => apiClient.post('/resources/categories/', data),
      update: (id, data) => apiClient.put(`/resources/categories/${id}/`, data).catch(() => {
        return apiClient.patch(`/resources/categories/${id}/`, data)
      }),
      delete: (id) => apiClient.delete(`/resources/categories/${id}/`).catch(() => {
        return Promise.reject(new Error('Delete endpoint not available'))
      }),
    },
  },
  
  faqs: {
    list: (params) => apiClient.get('/faqs/', { params }),
    get: (id) => apiClient.get(`/faqs/${id}/`),
    create: (data) => apiClient.post('/faqs/', data),
    update: (id, data) => apiClient.put(`/faqs/${id}/`, data),
    delete: (id) => apiClient.delete(`/faqs/${id}/`),
    categories: {
      list: () => apiClient.get('/faqs/categories/'),
      create: (data) => apiClient.post('/faqs/categories/', data),
      update: (id, data) => apiClient.put(`/faqs/categories/${id}/`, data).catch(() => {
        return apiClient.patch(`/faqs/categories/${id}/`, data)
      }),
      delete: (id) => apiClient.delete(`/faqs/categories/${id}/`).catch(() => {
        return Promise.reject(new Error('Delete endpoint not available'))
      }),
    },
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
  
  users: {
    list: (params) => apiClient.get('/auth/users/', { params }),
    get: (id) => apiClient.get(`/auth/users/${id}/`),
    create: (data) => apiClient.post('/auth/register/', data),
    update: (id, data) => apiClient.put(`/auth/users/${id}/`, data),
    delete: (id) => apiClient.delete(`/auth/users/${id}/`),
  },

  socialMedia: {
    list: (params) => apiClient.get('/social/posts/', { params }),
    get: (id) => apiClient.get(`/social/posts/${id}/`),
    create: (data) => apiClient.post('/social/posts/', createFormData(data), {
      headers: { 'Content-Type': 'multipart/form-data' }
    }),
    update: (id, data) => apiClient.put(`/social/posts/${id}/`, createFormData(data), {
      headers: { 'Content-Type': 'multipart/form-data' }
    }),
    delete: (id) => apiClient.delete(`/social/posts/${id}/`),
    fetchMetadata: (url) => apiClient.post('/social/posts/fetch-metadata/', { url }),
    channels: {
      get: () => apiClient.get('/social/channels/'),
      update: (data) => apiClient.put('/social/channels/', data),
    },
    contact: {
      get: () => apiClient.get('/social/contact/'),
      update: (data) => apiClient.put('/social/contact/', data),
    },
  },

  siteSettings: {
    get: () => apiClient.get('/api/sitesettings/settings/'),
    update: (data) => apiClient.put('/api/sitesettings/settings/', data),
  },
}

export default apiClient
