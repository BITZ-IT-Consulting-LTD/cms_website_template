<template>
  <div class="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8" style="background-color: white !important;">
    <div class="max-w-md w-full space-y-8">
      <div>
        <div class="mx-auto h-24 w-24 flex items-center justify-center">
          <img :src="sautiLogo" alt="Sauti Logo" class="h-full w-full object-contain" />
        </div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900" style="font-family: 'Roboto', sans-serif !important;">
          Admin Dashboard
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600">
          Sign in to access the Sauti CMS
        </p>
      </div>
      
      <form class="mt-8 space-y-6" @submit.prevent="handleLogin">
        <div class="space-y-4">
          <div>
            <label for="username" class="form-label">Username</label>
            <input
              id="username"
              v-model="form.username"
              name="username"
              type="text"
              required
              class="form-input"
              placeholder="Enter your username"
              :disabled="loading"
              :value="form.username"
            />
          </div>
          <div>
            <label for="password" class="form-label">Password</label>
            <input
              id="password"
              v-model="form.password"
              name="password"
              type="password"
              required
              class="form-input"
              placeholder="Enter your password"
              :disabled="loading"
              :value="form.password"
            />
          </div>
        </div>

        <div v-if="error" class="rounded-md bg-red-50 p-4">
          <div class="flex">
            <ExclamationTriangleIcon class="h-5 w-5 text-red-400" />
            <div class="ml-3">
              <h3 class="text-sm font-medium text-red-800">
                Login Failed
              </h3>
              <div class="mt-2 text-sm text-red-700">
                {{ error }}
              </div>
            </div>
          </div>
        </div>

        <div>
          <button
            type="submit"
            :disabled="loading"
            class="btn-primary w-full"
          >
            <span v-if="loading" class="absolute left-0 inset-y-0 flex items-center pl-3">
              <div class="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
            </span>
            <span v-else class="absolute left-0 inset-y-0 flex items-center pl-3">
              <LockClosedIcon class="h-5 w-5 text-primary-300 group-hover:text-primary-400" />
            </span>
            {{ loading ? 'Signing in...' : 'Sign in' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useToast } from 'vue-toastification'
import { LockClosedIcon, ExclamationTriangleIcon } from '@heroicons/vue/24/solid'
import sautiLogo from '@/assets/sauti-logo.jpeg'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()
const toast = useToast()

const form = ref({
  username: '',
  password: ''
})

// Force clear form on mount
onMounted(() => {
  form.value.username = ''
  form.value.password = ''
})

const loading = computed(() => authStore.loading)
const error = computed(() => authStore.error)

const handleLogin = async () => {
  try {
    await authStore.login(form.value)
    
    toast.success('Welcome back!')
    
    // Redirect to intended page or dashboard
    const redirect = route.query.redirect || '/dashboard'
    router.push(redirect)
  } catch (err) {
    // Error is handled by the store and displayed in template
    console.error('Login error:', err)
  }
}
</script>
