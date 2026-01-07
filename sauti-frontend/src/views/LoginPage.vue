<template>
  <div class="min-h-screen bg-neutral-white flex flex-col justify-center section-padding">
    <div class="container-custom max-w-xl mx-auto">
      <!-- Logo / Identity Area -->
      <div class="text-center mb-12">
        <div
          class="inline-flex items-center justify-center w-20 h-20 bg-primary/10 rounded-[2rem] mb-6 shadow-sm border-2 border-primary/20">
          <LockClosedIcon class="w-10 h-10 text-primary" />
        </div>
        <h1 class="campaign-header text-4xl text-secondary mb-4">Authorized Access</h1>
        <p class="text-lg font-bold text-neutral-black/40 uppercase tracking-widest">Sauti 116 Helpline Portal</p>
      </div>

      <!-- Login Form Card -->
      <div
        class="bg-neutral-white rounded-[4rem] border-2 border-primary p-10 md:p-16 shadow-2xl relative overflow-hidden">
        <!-- Decoration -->
        <div class="absolute -right-10 -bottom-10 w-40 h-40 bg-primary/5 rounded-full blur-2xl"></div>

        <form @submit.prevent="handleLogin" class="space-y-8 relative z-10">
          <div class="space-y-3">
            <label class="form-label">Username</label>
            <div class="relative group">
              <input v-model="credentials.username" type="text" class="form-input !pl-14" required
                placeholder="Enter username" />
              <UserIcon
                class="w-6 h-6 text-primary absolute left-5 top-1/2 -translate-y-1/2 group-focus-within:text-secondary transition-colors" />
            </div>
          </div>

          <div class="space-y-3">
            <label class="form-label">Secure Password</label>
            <div class="relative group">
              <input v-model="credentials.password" type="password" class="form-input !pl-14" required
                placeholder="••••••••" />
              <KeyIcon
                class="w-6 h-6 text-primary absolute left-5 top-1/2 -translate-y-1/2 group-focus-within:text-secondary transition-colors" />
            </div>
          </div>

          <div v-if="error"
            class="bg-emergency/10 border-2 border-emergency/20 p-6 rounded-2xl flex items-center gap-4 text-emergency">
            <ExclamationCircleIcon class="w-6 h-6 shrink-0" />
            <span class="font-bold text-xs uppercase tracking-widest">{{ error }}</span>
          </div>

          <button type="submit" class="btn btn-primary w-full justify-center !py-6 shadow-xl shadow-primary/20"
            :disabled="loading">
            <span v-if="!loading" class="flex items-center gap-3">
              <ShieldCheckIcon class="w-6 h-6" />
              Verify & Enter
            </span>
            <span v-else class="flex items-center gap-3">
              <div class="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin"></div>
              Authenticating...
            </span>
          </button>
        </form>
      </div>

      <!-- Footer Help -->
      <div class="mt-12 text-center">
        <p class="text-sm font-bold text-black/40">
          Trouble logging in? Contact the <span class="text-primary font-bold underline underline-offset-4">Systems
            Administrator</span>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { reactive, ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { useAuthStore } from '@/store/auth'
  import {
    LockClosedIcon,
    UserIcon,
    KeyIcon,
    ExclamationCircleIcon,
    ShieldCheckIcon
  } from '@heroicons/vue/24/outline'

  defineOptions({
    name: 'LoginPage'
  })

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
      error.value = 'Invalid access credentials'
    } finally {
      loading.value = false
    }
  }
</script>

<style scoped></style>
