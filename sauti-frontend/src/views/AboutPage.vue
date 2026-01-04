<template>
  <div class="bg-sauti-white min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <h1 class="page-header-title">
          About Sauti 116
        </h1>
        <p class="page-header-subtitle">
          Uganda’s National Helpline championed by the Ministry of Gender, Labour and Social Development.
        </p>
      </div>
    </header>

    <div>
      <!-- 2. Mission & Vision -->
      <section id="mission-vision" aria-labelledby="mission-heading" class="section-padding bg-sauti-white">
        <div class="container-custom">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center">
            <div class="lg:col-span-7 space-y-12">
              <!-- Mission -->
              <div class="card-base group">
                <div
                  class="w-20 h-20 bg-sauti-blue/10 rounded-2xl flex items-center justify-center mb-10 group-hover:scale-110 transition-transform duration-500">
                  <BoltIcon class="w-10 h-10 text-sauti-blue" />
                </div>
                <h2 id="mission-heading" class="campaign-header text-3xl text-sauti-darkGreen mb-6">Our Mission</h2>
                <p v-if="settings" class="text-xl text-sauti-darkGreen leading-relaxed font-bold">
                  {{ settings.mission || `To provide a confidential, accessible, and effective platform for reporting
                  and
                  responding to cases of child abuse, ensuring the safety and well-being of every child.` }}
                </p>
              </div>

              <!-- Vision -->
              <div class="card-base group border-sauti-lightGreen hover:border-sauti-lightGreen">
                <div
                  class="w-20 h-20 bg-sauti-lightGreen/10 rounded-2xl flex items-center justify-center mb-10 group-hover:scale-110 transition-transform duration-500">
                  <EyeIcon class="w-10 h-10 text-sauti-lightGreen" />
                </div>
                <h2 class="campaign-header text-3xl text-sauti-darkGreen mb-6">Our Vision</h2>
                <p v-if="settings" class="text-xl text-sauti-darkGreen leading-relaxed font-bold">
                  {{ settings.vision || `A Uganda where every child is safe, protected, and empowered to reach their
                  full
                  potential, free from all forms of violence and exploitation.` }}
                </p>
              </div>
            </div>

            <div class="lg:col-span-5">
              <div class="relative group">
                <div
                  class="absolute -inset-4 bg-sauti-orange/10 rounded-[4rem] rotate-3 group-hover:rotate-0 transition-transform duration-700">
                </div>
                <div class="relative rounded-[4rem] overflow-hidden border-4 border-sauti-orange shadow-2xl">
                  <img src="@/assets/community-protection.png" alt="Community protection in action"
                    class="w-full h-[600px] object-cover transition-transform duration-1000 group-hover:scale-110" />
                  <div class="absolute inset-0 bg-gradient-to-t from-sauti-darkGreen/40 to-transparent"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 3. Impact Statistics (Break Section) -->
    </div>

    <!-- Impact Stats - Full Width Break -->
    <section id="impact-stats" class="py-24 bg-sauti-darkGreen relative overflow-hidden">
      <div class="container-custom relative z-10 text-center">
        <div class="mb-20">
          <h2 class="campaign-header text-4xl md:text-5xl text-sauti-white mb-6">Our National Impact</h2>
          <p class="text-xl text-sauti-white/80 max-w-2xl mx-auto font-bold">
            Verifiable data showcasing our commitment to Ugandan citizens.
          </p>
        </div>

        <div v-if="settings" class="grid grid-cols-2 lg:grid-cols-4 gap-8 md:gap-12">
          <div v-for="stat in impactStats" :key="stat.title" class="text-center group">
            <div
              class="inline-flex items-center justify-center p-8 rounded-[3rem] bg-sauti-white/10 mb-6 backdrop-blur-sm group-hover:bg-sauti-white/20 transition-all duration-500 border border-sauti-white/10">
              <p class="text-5xl md:text-6xl font-bold text-sauti-white tracking-tighter">
                {{ stat.title }}
              </p>
            </div>
            <p class="campaign-header text-xs text-sauti-white/60 tracking-[0.2em]">{{ stat.text }}</p>
          </div>
        </div>
      </div>
    </section>

    <div>
      <!-- 4. Core Values -->
      <section id="core-values" aria-labelledby="values-heading" class="section-padding bg-sauti-white">
        <div class="container-custom">
          <div class="text-center mb-20">
            <h2 id="values-heading" class="campaign-header text-4xl text-sauti-darkGreen mb-6">Our Core Values</h2>
            <p class="text-xl text-sauti-darkGreen max-w-3xl mx-auto font-bold opacity-70">
              The principles that guide every interaction, decision, and action we take.
            </p>
          </div>

          <div v-if="loading.coreValues" class="py-20 text-center">
            <div class="spinner mx-auto"></div>
          </div>

          <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
            <div v-for="value in coreValues" :key="value.id" class="card-base group">
              <div
                class="w-16 h-16 rounded-2xl flex items-center justify-center mb-8 bg-sauti-blue/10 group-hover:scale-110 transition-transform duration-500">
                <component :is="getIconComponent(value.icon)" class="w-8 h-8 text-sauti-blue" />
              </div>
              <h3 class="campaign-header text-2xl text-sauti-darkGreen mb-4">{{ value.title }}</h3>
              <p class="text-lg text-sauti-darkGreen/70 leading-relaxed font-bold">{{ value.description }}</p>
            </div>
          </div>
        </div>
      </section>

      <!-- 5. History / Journey -->
      <section id="history" aria-labelledby="history-heading" class="section-padding bg-sauti-blue/5">
        <div class="container-custom">
          <div class="text-center mb-20">
            <h2 id="history-heading" class="campaign-header text-4xl text-sauti-darkGreen mb-6">Our Journey</h2>
            <p class="text-xl text-sauti-darkGreen max-w-2xl mx-auto font-bold opacity-70">
              Milestones that define our commitment to child protection.
            </p>
          </div>

          <div v-if="loading.timeline" class="py-20 text-center">
            <div class="spinner mx-auto"></div>
          </div>

          <AppTimeline v-else :timeline-events="timelineEvents" />
        </div>
      </section>

      <!-- 6. Partners -->
      <section id="partners" aria-labelledby="partners-heading" class="section-padding bg-sauti-white">
        <div class="container-custom">
          <div class="text-center mb-20">
            <h2 id="partners-heading" class="campaign-header text-4xl text-sauti-darkGreen mb-4">Trusted Partners</h2>
            <p class="text-xl text-sauti-darkGreen max-w-3xl mx-auto font-bold opacity-70">
              We work alongside leading organizations to deliver comprehensive support.
            </p>
          </div>

          <div v-if="loading.partners" class="py-20 text-center">
            <div class="spinner mx-auto"></div>
          </div>

          <div v-else class="bg-sauti-white rounded-[4rem] p-12 border-2 border-sauti-neutral">
            <PartnerGrid :partners="partners"
              class="opacity-80 grayscale hover:grayscale-0 transition-all duration-700" />
          </div>
        </div>
      </section>
    </div>
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
    ShieldCheckIcon,
    UserGroupIcon,
    LockClosedIcon,
    GlobeAltIcon,
    HeartIcon,
    BoltIcon,
    EyeIcon
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
    return iconMap[iconName] || ShieldCheckIcon
  }

  const impactStats = computed(() => {
    if (!settings.value) return []

    // Prefer new JSON list structure
    if (settings.value.impact_stats && Array.isArray(settings.value.impact_stats)) {
      return settings.value.impact_stats
        .filter(stat => stat.is_active !== false)
        .sort((a, b) => (a.order || 0) - (b.order || 0))
        .map(stat => ({
          title: stat.value,
          text: stat.label
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
    if (!settings.value) {
      await settingsStore.fetchGlobalSettings()
    }
    fetchCoreValues()
    fetchTimelineEvents()
    fetchPartners()
  })
</script>

<style scoped></style>