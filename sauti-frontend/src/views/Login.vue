<template>
  <div class="section-padding">
    <div class="container-custom max-w-md mx-auto">
      <div class="card card-body">
        <h1 class="text-2xl font-bold text-center mb-6">Staff Login</h1>
        <form @submit.prevent="handleLogin" class="space-y-4">
          <div>
            <label class="form-label">Username</label>
            <input v-model="credentials.username" type="text" class="form-input" required />
          </div>
          <div>
            <label class="form-label">Password</label>
            <input v-model="credentials.password" type="password" class="form-input" required />
          </div>
          <div v-if="error" class="text-danger-600 text-sm">{{ error }}</div>
          <button type="submit" class="btn-primary w-full" :disabled="loading">
            <span v-if="!loading">Login</span>
            <span v-else>Logging in...</span>
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/store/auth'

const router = useRouter()
const authStore = useAuthStore()
const credentials = reactive({ username: '', password: '' })
const loading = ref(false)
const error = ref('')

async function handleLogin() {
  loading.value = true
  error.value = ''
  try {
    await authStore.login(credentials)
    router.push('/')
  } catch (err) {
    error.value = 'Invalid credentials'
  } finally {
    loading.value = false
  }
}
</script>
