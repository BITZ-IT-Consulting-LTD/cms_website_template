import { defineStore } from 'pinia'
import { ref, reactive } from 'vue'

export const useSettingsStore = defineStore('settings', () => {
    const settings = ref({
        security: {
            requireTwoFactor: false,
            sessionTimeout: 30,
            maxLoginAttempts: 5,
            minPasswordLength: 8,
            requireSpecialChars: true
        },
        api: {
            baseUrl: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api',
            rateLimit: 60,
            enableCors: true
        }
    })

    const loading = ref(false)
    const error = ref(null)

    async function fetchSettings() {
        loading.value = true
        error.value = null
        try {
            // In a real app, this would be an API call
            // For now we keep the defaults or load from local storage
            const saved = localStorage.getItem('admin_settings')
            if (saved) {
                settings.value = JSON.parse(saved)
            }
        } catch (err) {
            error.value = 'Failed to load settings'
            console.error(err)
        } finally {
            loading.value = false
        }
    }

    async function updateSettings(newSettings) {
        loading.value = true
        try {
            settings.value = { ...settings.value, ...newSettings }
            localStorage.setItem('admin_settings', JSON.stringify(settings.value))
            return true
        } catch (err) {
            error.value = 'Failed to update settings'
            return false
        } finally {
            loading.value = false
        }
    }

    return {
        settings,
        loading,
        error,
        fetchSettings,
        updateSettings
    }
})
