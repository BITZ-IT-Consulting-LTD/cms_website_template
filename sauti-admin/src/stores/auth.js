import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { api } from '@/utils/api'

export const useAuthStore = defineStore('auth', () => {
  // State
  const token = ref(localStorage.getItem('admin_token') || null)
  const refreshToken = ref(localStorage.getItem('admin_refresh_token') || null)
  const user = ref(JSON.parse(localStorage.getItem('admin_user') || 'null'))
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
      // For now, check against hardcoded admin credentials while backend is being set up
      if (credentials.username === 'admin' && credentials.password === 'admin123') {
        // Mock successful login response
        const mockUser = {
          username: 'admin',
          email: 'admin@sauti.org',
          first_name: 'Admin',
          last_name: 'User',
          role: 'ADMIN'
        }
        
        const mockTokens = {
          access: 'mock-access-token',
          refresh: 'mock-refresh-token'
        }
        
        // Store tokens
        token.value = mockTokens.access
        refreshToken.value = mockTokens.refresh
        user.value = mockUser
        
        // Persist to localStorage
        localStorage.setItem('admin_token', mockTokens.access)
        localStorage.setItem('admin_refresh_token', mockTokens.refresh)
        localStorage.setItem('admin_user', JSON.stringify(mockUser))
        
        return {
          access: mockTokens.access,
          refresh: mockTokens.refresh,
          user: mockUser
        }
      } else {
        throw new Error('Invalid credentials')
      }
      
      // TODO: Uncomment this when Django backend is running
      // const response = await api.auth.login(credentials)
      // const { access, refresh, user: userData } = response.data
      // 
      // // Store tokens
      // token.value = access
      // refreshToken.value = refresh
      // user.value = userData
      // 
      // // Persist to localStorage
      // localStorage.setItem('admin_token', access)
      // localStorage.setItem('admin_refresh_token', refresh)
      // localStorage.setItem('admin_user', JSON.stringify(userData))
      // 
      // return response.data
    } catch (err) {
      error.value = err.response?.data?.detail || err.message || 'Login failed'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function logout() {
    // Clear all auth data
    token.value = null
    refreshToken.value = null
    user.value = null
    
    // Clear localStorage
    localStorage.removeItem('admin_token')
    localStorage.removeItem('admin_refresh_token')
    localStorage.removeItem('admin_user')
  }
  
  async function refreshAccessToken() {
    if (!refreshToken.value) {
      throw new Error('No refresh token available')
    }
    
    try {
      const response = await api.auth.refreshToken(refreshToken.value)
      const { access } = response.data
      
      token.value = access
      localStorage.setItem('admin_token', access)
      
      return access
    } catch (err) {
      // If refresh fails, logout user
      logout()
      throw err
    }
  }
  
  async function fetchProfile() {
    try {
      const response = await api.auth.profile()
      user.value = response.data
      localStorage.setItem('admin_user', JSON.stringify(response.data))
      return response.data
    } catch (err) {
      console.error('Failed to fetch profile:', err)
      throw err
    }
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
    logout,
    refreshAccessToken,
    fetchProfile,
  }
})
