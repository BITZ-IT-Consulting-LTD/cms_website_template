<template>
  <div class="bg-sauti-white">
    <!-- Hero / Header -->
    <header class="relative bg-sauti-blue text-sauti-white py-24 overflow-hidden">
      <!-- Decorative background circles -->
      <div
        class="absolute top-0 right-0 -transtale-y-1/2 translate-x-1/2 w-96 h-96 bg-sauti-white rounded-full opacity-10 blur-3xl">
      </div>
      <div
        class="absolute bottom-0 left-0 translate-y-1/2 -translate-x-1/4 w-64 h-64 bg-sauti-white rounded-full opacity-10 blur-2xl">
      </div>

      <div class="container-custom relative z-10 text-center">
        <h1 class="text-4xl md:text-6xl font-black mb-6 tracking-tight text-sauti-white">
          About Sauti 116
        </h1>
        <p class="mt-6 max-w-3xl mx-auto text-xl md:text-2xl text-sauti-white font-medium leading-relaxed">
          Championing the safety, protection, and rights of every child in Uganda through accessible reporting and
          support.
        </p>
      </div>
    </header>

    <!-- Section: Mission & Vision -->
    <section id="mission-vision" class="py-20 bg-sauti-white">
      <div class="container-custom">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-16">
          <!-- Mission -->
          <div
            class="bg-sauti-neutral/50 rounded-[2.5rem] p-10 md:p-12 border border-sauti-neutral hover:shadow-xl transition-all duration-300 group">
            <div
              class="w-16 h-16 bg-sauti-blue rounded-2xl flex items-center justify-center mb-8 group-hover:scale-110 transition-transform duration-300 shadow-lg">
              <svg class="w-8 h-8 text-sauti-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h2 class="text-3xl font-bold text-sauti-darkGreen mb-6">Our Mission</h2>
            <p v-if="settings" class="text-lg text-sauti-darkGreen leading-relaxed font-medium">
              {{ settings.mission || 'To provide a confidential, accessible, and effective platform for reporting and
              responding to cases of child abuse, ensuring the safety and well - being of every child.' }}
            </p>
          </div>

          <!-- Vision -->
          <div
            class="bg-sauti-neutral/50 rounded-[2.5rem] p-10 md:p-12 border border-sauti-neutral hover:shadow-xl transition-all duration-300 group">
            <div
              class="w-16 h-16 bg-sauti-lightGreen rounded-2xl flex items-center justify-center mb-8 group-hover:scale-110 transition-transform duration-300 shadow-lg">
              <svg class="w-8 h-8 text-sauti-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
              </svg>
            </div>
            <h2 class="text-3xl font-bold text-sauti-darkGreen mb-6">Our Vision</h2>
            <p v-if="settings" class="text-lg text-sauti-darkGreen leading-relaxed font-medium">
              {{ settings.vision || 'A Uganda where every child is safe, protected, and empowered to reach their full
              potential, free from all forms of violence and exploitation.' }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section: Impact Statistics -->
    <section id="impact-stats" class="py-20 relative overflow-hidden bg-sauti-darkGreen">
      <div class="container-custom relative z-10">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-5xl font-black text-sauti-white mb-6">
            Our Impact
          </h2>
          <p class="text-xl text-sauti-neutral max-w-2xl mx-auto">
            Real numbers representing real lives changed through our intervention and support.
          </p>
        </div>

        <div v-if="settings" class="grid grid-cols-2 lg:grid-cols-4 gap-8 md:gap-12">
          <div v-for="stat in impactStats" :key="stat.title" class="text-center group">
            <div
              class="inline-flex items-center justify-center p-4 rounded-full bg-sauti-white/10 mb-6 backdrop-blur-sm group-hover:bg-sauti-white/20 transition-colors">
              <!-- Dynamic large text -->
              <p class="text-4xl md:text-5xl lg:text-6xl font-black text-sauti-white tracking-tight">
                {{ stat.title }}
              </p>
            </div>
            <p class="text-base md:text-lg font-bold text-sauti-neutral uppercase tracking-widest">{{ stat.text }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section: Core Values -->
    <section id="core-values" class="py-24 bg-sauti-neutral">
      <div class="container-custom">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-5xl font-extrabold text-sauti-darkGreen mb-6">
            Our Core Values
          </h2>
          <p class="text-xl text-sauti-darkGreen max-w-3xl mx-auto">
            The principles that guide every interaction, decision, and action we take.
          </p>
        </div>

        <div v-if="loading.coreValues" class="text-center py-12">
          <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-sauti-blue mx-auto"></div>
        </div>

        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="value in coreValues" :key="value.id"
            class="bg-sauti-white p-8 md:p-10 rounded-[2rem] shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 border border-sauti-neutral">
            <div class="w-14 h-14 rounded-2xl flex items-center justify-center mb-6 bg-sauti-neutral">
              <component :is="getIconComponent(value.icon)" class="w-8 h-8 text-sauti-blue" />
            </div>
            <h3 class="text-2xl font-bold text-sauti-darkGreen mb-4">{{ value.title }}</h3>
            <p class="text-sauti-darkGreen leading-relaxed">{{ value.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section: History / Journey -->
    <section id="history" class="py-24 bg-sauti-white">
      <div class="container-custom">
        <div class="text-center mb-20">
          <h2 class="text-3xl md:text-5xl font-extrabold text-sauti-darkGreen mb-6">
            Our Journey
          </h2>
          <p class="text-xl text-sauti-darkGreen max-w-2xl mx-auto">
            Milestones that define our commitment to child protection.
          </p>
        </div>

        <div v-if="loading.timeline" class="text-center py-12">
          <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-sauti-blue mx-auto"></div>
        </div>

        <AppTimeline v-else :timeline-events="timelineEvents" />
      </div>
    </section>

    <!-- Section: Partners -->
    <section id="partners" class="py-24 bg-sauti-neutral/30">
      <div class="container-custom">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-sauti-darkGreen mb-6">
            Trusted Partners
          </h2>
          <p class="text-lg text-sauti-darkGreen max-w-3xl mx-auto">
            We work alongside leading organizations to deliver comprehensive support.
          </p>
        </div>

        <div v-if="loading.partners" class="text-center py-12">
          <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-sauti-blue mx-auto"></div>
        </div>

        <div v-else>
          <PartnerGrid :partners="partners"
            class="opacity-90 grayscale hover:grayscale-0 transition-all duration-500" />
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
  import { ref, onMounted, computed } from 'vue'
  import { useSettingsStore } from '@/store/settings'
  import { usePartnersStore } from '@/store/partners'
  import { api } from '@/utils/axios'
  import AppTimeline from '@/components/AppTimeline.vue'
  import PartnerGrid from '@/components/common/PartnerGrid.vue'
  import {
    ShieldCheckIcon, UserGroupIcon, LockClosedIcon, GlobeAltIcon, HeartIcon
  } from '@heroicons/vue/24/outline'

  defineOptions({
    name: 'AboutPage'
  })

  const settingsStore = useSettingsStore()
  const partnersStore = usePartnersStore()
  const settings = computed(() => settingsStore.settings)
  const partners = computed(() => partnersStore.partners)

  const coreValues = ref([])
  const timelineEvents = ref([])

  const loading = ref({
    coreValues: false,
    timeline: false,
    partners: false
  })

  const iconMap = {
    ShieldCheckIcon,
    UserGroupIcon,
    LockClosedIcon,
    GlobeAltIcon,
    HeartIcon
  }

  const getIconComponent = (iconName) => {
    // A simple map to return an icon component. Add more as needed.
    return iconMap[iconName] || ShieldCheckIcon
  }

  const impactStats = computed(() => {
    if (!settings.value) return []

    // Prefer new JSON list structure
    if (settings.value.impact_stats && Array.isArray(settings.value.impact_stats)) {
      return settings.value.impact_stats
        .filter(stat => stat.is_active !== false) // default true if undefined
        .sort((a, b) => (a.order || 0) - (b.order || 0))
        .map(stat => ({
          title: stat.value, // Map value to title for template compatibility
          text: stat.label   // Map label to text for template compatibility
        }))
    }

    // Fallback to legacy fields
    const stats = []
    for (let i = 1; i <= 4; i++) {
      const title = settings.value[`about_stat${i}_title`]
      const text = settings.value[`about_stat${i}_text`]
      if (title && text) {
        stats.push({ title, text })
      }
    }
    return stats
  })

  const fetchCoreValues = async () => {
    loading.value.coreValues = true
    try {
      const response = await api.get('/content/core-values/')
      coreValues.value = response.data.results || response.data || []
    } catch (error) {
      console.error('Failed to fetch core values:', error)
    } finally {
      loading.value.coreValues = false
    }
  }

  const fetchTimelineEvents = async () => {
    loading.value.timeline = true
    try {
      const response = await api.get('/content/timeline-events/')
      timelineEvents.value = response.data.results || response.data || []
    } catch (error) {
      console.error('Failed to fetch timeline events:', error)
    } finally {
      loading.value.timeline = false
    }
  }

  const fetchPartners = async () => {
    loading.value.partners = true
    try {
      await partnersStore.fetchPartners()
    } catch (error) {
      console.error('Failed to fetch partners:', error)
    } finally {
      loading.value.partners = false
    }
  }

  onMounted(async () => {
    // Settings are fetched globally in the app layout, but we ensure they are loaded.
    if (!settings.value) {
      await settingsStore.fetchGlobalSettings()
    }
    fetchCoreValues()
    fetchTimelineEvents()
    fetchPartners()
  })
</script>

<style scoped>
  .container-custom {
    max-width: 80rem;
    margin-left: auto;
    margin-right: auto;
    padding-left: 1rem;
    padding-right: 1rem;
  }

  @media (min-width: 640px) {
    .container-custom {
      padding-left: 1.5rem;
      padding-right: 1.5rem;
    }
  }

  @media (min-width: 1024px) {
    .container-custom {
      padding-left: 2rem;
      padding-right: 2rem;
    }
  }
</style>