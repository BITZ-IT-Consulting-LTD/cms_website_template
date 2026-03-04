import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { api } from '@/utils/axios'

export const useAuthStore = defineStore('auth', () => {
  // State
  const token = ref(localStorage.getItem('token') || null)
  const refreshToken = ref(localStorage.getItem('refreshToken') || null)
  const user = ref((() => {
    try {
      const userData = localStorage.getItem('user')
      return userData ? JSON.parse(userData) : null
    } catch (error) {
      console.error('Error parsing user data from localStorage:', error)
      return null
    }
  })())
  const loading = ref(false)
  const error = ref(null)
  
  // Getters
  const isAuthenticated = computed(() => !!token.value)
  const isAdmin = computed(() => user.value?.role === 'ADMIN')
  const isEditor = computed(() => ['ADMIN', 'EDITOR'].includes(user.value?.role))
  const userFullName = computed(() => {
    if (!user.value) return ''
    return `${user.value.first_name || ''} ${user.value.last_name || ''}`.trim() || user.value.username
  })
  
  // Actions
  async function login(credentials) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.auth.login(credentials)
      const { access, refresh, user: userData } = response.data
      
      // Store tokens
      token.value = access
      refreshToken.value = refresh
      user.value = userData
      
      // Persist to localStorage
      localStorage.setItem('token', access)
      localStorage.setItem('refreshToken', refresh)
      localStorage.setItem('user', JSON.stringify(userData))
      
      return response.data
    } catch (err) {
      error.value = err.response?.data?.detail || 'Login failed'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function register(userData) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.auth.register(userData)
      return response.data
    } catch (err) {
      error.value = err.response?.data || 'Registration failed'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function fetchProfile() {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.auth.profile()
      user.value = response.data
      localStorage.setItem('user', JSON.stringify(response.data))
      return response.data
    } catch (err) {
      error.value = err.response?.data || 'Failed to fetch profile'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function updateProfile(data) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.auth.updateProfile(data)
      user.value = response.data
      localStorage.setItem('user', JSON.stringify(response.data))
      return response.data
    } catch (err) {
      error.value = err.response?.data || 'Failed to update profile'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function refresh() {
    if (!refreshToken.value) {
      logout()
      return
    }
    
    try {
      const response = await api.auth.refreshToken(refreshToken.value)
      const { access, refresh: newRefresh } = response.data
      
      token.value = access
      refreshToken.value = newRefresh
      
      localStorage.setItem('token', access)
      localStorage.setItem('refreshToken', newRefresh)
      
      return response.data
    } catch (err) {
      console.error('Token refresh failed:', err)
      logout()
      throw err
    }
  }
  
  function logout() {
    // Clear state
    token.value = null
    refreshToken.value = null
    user.value = null
    error.value = null
    
    // Clear localStorage
    localStorage.removeItem('token')
    localStorage.removeItem('refreshToken')
    localStorage.removeItem('user')
  }
  
  function clearError() {
    error.value = null
  }
  
  return {
    // State
    token,
    refreshToken,
    user,
    loading,
    error,
    
    // Getters
    isAuthenticated,
    isAdmin,
    isEditor,
    userFullName,
    
    // Actions
    login,
    register,
    fetchProfile,
    updateProfile,
    refresh,
    logout,
    clearError,
  }
})
