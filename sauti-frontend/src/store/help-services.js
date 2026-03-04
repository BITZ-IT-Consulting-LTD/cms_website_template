import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/utils/axios'

export const useHelpServicesStore = defineStore('help-services', () => {
    const services = ref([])
    const loading = ref(false)
    const error = ref(null)

    async function fetchServices() {
        loading.value = true
        error.value = null
        try {
            const response = await api.get('/services/help-services/')
            services.value = response.data.results || response.data
        } catch (e) {
            console.error('Failed to fetch help services:', e)
            error.value = e
        } finally {
            loading.value = false
        }
    }

    return { services, loading, error, fetchServices }
})
