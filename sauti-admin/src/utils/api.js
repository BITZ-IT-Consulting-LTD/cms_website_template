import axios from 'axios'
import { useAuthStore } from '@/stores/auth'
import router from '@/router'



const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 15000,
  headers: {
    'Content-Type': 'application/json',
  },
})

const createFormData = (data) => {
  if (data instanceof FormData) return data
  const formData = new FormData()
  Object.keys(data).forEach(key => {
    const value = data[key]

    // Handle file fields first
    const fileFields = ['featured_image', 'thumbnail', 'file', 'image', 'photo', 'video_file', 'logo', 'favicon']
    if (fileFields.includes(key)) {
      if (value instanceof File) {
        formData.append(key, value)
      } else if (value === null) {
        // To delete a file, send an empty string for the field
        formData.append(key, '')
      }
      // If it's a string (existing URL), or any other case for a file field, do nothing.
      // The backend will keep the existing file if the key is not present or not a file.
      return
    }

    // Skip null/undefined for non-file fields
    if (value === null || value === undefined) {
      return
    }

    // Handle tags array
    if (key === 'tags') {
      if (Array.isArray(value) && value.length > 0) {
        value.forEach(tag => {
          const tagId = typeof tag === 'number' ? tag : parseInt(tag, 10)
          if (!isNaN(tagId) && tagId > 0) {
            formData.append('tags', tagId)
          }
        })
      }
      return
    }

    // Handle category and category_id
    if (key === 'category' || key === 'category_id') {
      if (value === '') return // Don't append if it's an empty string
      const categoryId = typeof value === 'number' ? value : parseInt(value, 10)
      if (!isNaN(categoryId) && categoryId > 0) {
        formData.append(key, categoryId.toString())
      }
      return
    }

    // Handle boolean values
    if (typeof value === 'boolean') {
      formData.append(key, value ? 'true' : 'false')
      return
    }

    // Handle number values
    if (typeof value === 'number') {
      formData.append(key, value.toString())
      return
    }
    
    // Handle objects (e.g., for JSON fields)
    if (typeof value === 'object' && value !== null) {
      formData.append(key, JSON.stringify(value))
      return
    }

    // For all other fields (strings), append them.
    // This will also handle empty strings for fields that allow them.
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
  // Site content endpoints (full URL to avoid /api prefix)
  siteContent: {
    update: (key, data) => axios.put(`${import.meta.env.VITE_API_URL}/content/site-content/${key}/`, data),
    create: (data) => axios.post(`${import.meta.env.VITE_API_URL}/content/site-content/`, data),
  },

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
    history: (id) => apiClient.get(`/posts/${id}/history/`),
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
    history: (id) => apiClient.get(`/reports/${id}/history/`),
  },

  users: {
    list: (params) => apiClient.get('/auth/users/', { params }),
    get: (id) => apiClient.get(`/auth/users/${id}/`),
    create: (data) => apiClient.post('/auth/register/', data),
    update: (id, data) => apiClient.put(`/auth/users/${id}/`, data),
    delete: (id) => apiClient.delete(`/auth/users/${id}/`),
  },

  coreValues: {
    list: (params) => apiClient.get('/content/core-values/', { params }),
    get: (id) => apiClient.get(`/content/core-values/${id}/`),
    create: (data) => apiClient.post('/content/core-values/', data),
    update: (id, data) => apiClient.put(`/content/core-values/${id}/`, data),
    delete: (id) => apiClient.delete(`/content/core-values/${id}/`),
  },

  teamMembers: {
    list: (params) => apiClient.get('/content/team-members/', { params }),
    get: (id) => apiClient.get(`/content/team-members/${id}/`),
    create: (data) => apiClient.post('/content/team-members/', createFormData(data), {
      headers: { 'Content-Type': 'multipart/form-data' }
    }),
    update: (id, data) => apiClient.put(`/content/team-members/${id}/`, createFormData(data), {
      headers: { 'Content-Type': 'multipart/form-data' }
    }),
    delete: (id) => apiClient.delete(`/content/team-members/${id}/`),
  },

  protectionApproaches: {
    list: (params) => apiClient.get('/content/protection-approach/', { params }),
    get: (id) => apiClient.get(`/content/protection-approach/${id}/`),
    create: (data) => apiClient.post('/content/protection-approach/', data),
    update: (id, data) => apiClient.put(`/content/protection-approach/${id}/`, data),
    delete: (id) => apiClient.delete(`/content/protection-approach/${id}/`),
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
    get: () => apiClient.get('/sitesettings/'),
    update: (data) => apiClient.put('/sitesettings/', data),
    history: () => apiClient.get('/sitesettings/history/'),
  },

  organizationProfile: {
    get: () => apiClient.get('/sitesettings/organization/'),
    update: (data) => apiClient.put('/sitesettings/organization/', createFormData(data), {
      headers: { 'Content-Type': 'multipart/form-data' }
    }),
    history: () => apiClient.get('/sitesettings/organization/history/'),
  },

  services: {
    list: (params) => apiClient.get('/services/', { params }),
    get: (id) => apiClient.get(`/services/${id}/`),
    create: (data) => apiClient.post('/services/', data),
    update: (id, data) => apiClient.put(`/services/${id}/`, data),
    delete: (id) => apiClient.delete(`/services/${id}/`),
  },

  helpServices: {
    list: (params) => apiClient.get('/services/help-services/', { params }),
    get: (id) => apiClient.get(`/services/help-services/${id}/`),
    create: (data) => apiClient.post('/services/help-services/', data),
    update: (id, data) => apiClient.put(`/services/help-services/${id}/`, data),
    delete: (id) => apiClient.delete(`/services/help-services/${id}/`),
    steps: {
      create: (data) => apiClient.post('/services/help-steps/', data),
      update: (id, data) => apiClient.put(`/services/help-steps/${id}/`, data),
      delete: (id) => apiClient.delete(`/services/help-steps/${id}/`),
    }
  },

  feedback: {
    list: (params) => apiClient.get('/contact/feedback/list/', { params }),
    update: (id, data) => apiClient.patch(`/contact/feedback/${id}/`, data),
    delete: (id) => apiClient.delete(`/contact/feedback/${id}/`),
  },

  timeline: {
    list: (params) => apiClient.get('/timeline/', { params }),
    get: (id) => apiClient.get(`/timeline/${id}/`),
    create: (data) => apiClient.post('/timeline/', data),
    update: (id, data) => apiClient.put(`/timeline/${id}/`, data),
    delete: (id) => apiClient.delete(`/timeline/${id}/`),
  },
}

export default apiClient
