<template>
  <div class="bg-neutral-white min-h-screen">
    <!-- 1. Page Header (Verdict Messaging) -->
    <header class="page-header !py-24 md:!py-32">
      <div class="container-custom">
        <h1 class="mb-4">
          <span class="text-primary">10+ Years</span> of Dedicated Protection.
        </h1>
        <p class="page-header-subtitle">
          Sauti 116 is Uganda’s official safety mechanism managed by the Ministry of Gender, Labour and Social
          Development.
        </p>
      </div>
    </header>

    <div class="section-padding !pt-0">
      <div class="container-custom">
        <!-- Quick Summary (Flash Pattern) - Brand Enforced -->
        <section
          class="bg-accent-yellow/5 p-8 md:p-12 rounded-[3.5rem] border-2 border-accent-yellow/20 mb-16 shadow-sm overflow-hidden relative">
          <div class="absolute top-0 right-0 w-32 h-32 bg-accent-yellow/10 rounded-full -mr-16 -mt-16 blur-3xl"></div>
          <h2 class="campaign-header text-xl text-secondary mb-8 flex items-center gap-3">
            <ShieldCheckIcon class="w-6 h-6 text-primary" />
            Sauti 116 at a Glance
          </h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-10 relative z-10">
            <div class="space-y-4">
              <p class="text-primary font-black text-xs uppercase tracking-widest">Always Listening</p>
              <p class="text-black font-bold text-lg leading-snug">Open 24/7, every day of the year, nationwide
                across Uganda.</p>
            </div>
            <div class="space-y-4">
              <p class="text-primary font-black text-xs uppercase tracking-widest">Always Private</p>
              <p class="text-black font-bold text-lg leading-snug">Your calls and reports are strictly confidential
                by law.</p>
            </div>
            <div class="space-y-4">
              <p class="text-primary font-black text-xs uppercase tracking-widest">Always Official</p>
              <p class="text-black font-bold text-lg leading-snug">Managed by government protection experts (MGLSD).
              </p>
            </div>
          </div>
        </section>
      </div>

      <!-- 2. Mission & Vision (Sanctuary Layout) -->
      <section id="mission-vision" aria-labelledby="mission-heading"
        class="section-padding bg-neutral-white !py-24 md:!py-32">
        <div class="container-custom">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">
            <div class="lg:col-span-12 xl:col-span-7 space-y-12">
              <!-- Mission -->
              <div class="card-base group border-l-4 border-primary">
                <div class="flex items-start gap-8">
                  <div class="w-16 h-16 bg-primary/10 rounded-2xl flex items-center justify-center shrink-0">
                    <BoltIcon class="w-8 h-8 text-primary" />
                  </div>
                  <div>
                    <h2 id="mission-heading" class="mb-4">Our <span class="text-primary">Promise</span> to You</h2>
                    <p v-if="settings" class="text-xl font-bold leading-relaxed">
                      {{ settings.mission || `We are here to listen. We help you report harm and make sure you get the
                      support you need to stay safe.` }}
                    </p>
                  </div>
                </div>
              </div>

              <!-- Vision -->
              <div class="card-base group border-l-4 border-secondary-light">
                <div class="flex items-start gap-8">
                  <div class="w-16 h-16 bg-secondary-light/10 rounded-2xl flex items-center justify-center shrink-0">
                    <EyeIcon class="w-8 h-8 text-secondary-light" />
                  </div>
                  <div>
                    <h2 class="mb-4">A Safer <span class="text-secondary-light">Uganda</span> for Everyone</h2>
                    <p v-if="settings" class="text-xl font-bold leading-relaxed">
                      {{ settings.vision || `A Uganda where everyone can live without fear of violence and reach their
                      full potential.` }}
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <div class="lg:col-span-12 xl:col-span-5">
              <div class="relative group">
                <div
                  class="absolute -inset-4 bg-primary/5 rounded-[4rem] group-hover:bg-primary/10 transition-all duration-700">
                </div>
                <div class="relative rounded-[4rem] overflow-hidden shadow-xl group">
                  <img src="@/assets/inclusive_community_protection.png"
                    alt="Inclusive community protection dialogue involving elders, youth, and caregivers"
                    class="w-full h-[600px] object-cover transition-transform duration-1000 group-hover:scale-105" />
                  <div class="absolute inset-0 bg-gradient-to-t from-secondary/40 via-transparent to-transparent"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 3. Impact Statistics (Break Section) -->
    </div>

    <!-- Impact Stats - Full Width Break -->
    <section id="impact-stats" class="py-24 bg-secondary relative overflow-hidden">
      <div class="container-custom relative z-10 text-center">
        <div class="mb-20">
          <h2 class="campaign-header text-4xl md:text-5xl text-neutral-white mb-6">Reach Across the Nation</h2>
          <p class="text-xl text-neutral-white/80 max-w-2xl mx-auto font-bold">
            How we are helping people across Uganda every day.
          </p>
        </div>

        <div v-if="settings" class="grid grid-cols-2 lg:grid-cols-4 gap-8 md:gap-12">
          <div v-for="stat in impactStats" :key="stat.title" class="text-center group">
            <div
              class="inline-flex items-center justify-center p-8 rounded-[3rem] bg-neutral-white/10 mb-6 backdrop-blur-sm group-hover:bg-neutral-white/20 transition-all duration-500 border border-neutral-white/10">
              <p class="text-5xl md:text-6xl font-bold text-neutral-white tracking-tighter">
                {{ stat.title }}
              </p>
            </div>
            <p class="campaign-header text-xs text-neutral-white/60 tracking-[0.2em]">{{ stat.text }}</p>
          </div>
        </div>
      </div>
    </section>

    <div>
      <!-- 4. Core Values (Sanctuary Layout) -->
      <section id="core-values" aria-labelledby="values-heading"
        class="section-padding bg-neutral-white !py-32 md:!py-48">
        <div class="container-custom">
          <div class="text-center mb-24 max-w-3xl mx-auto">
            <h2 id="values-heading" class="mb-6">The Principles That <span class="text-primary">Guide Us</span></h2>
            <p class="text-xl font-bold text-black/60">
              Clear legibility and trust are our priority. We operate under these six non-negotiable pillars of
              protection.
            </p>
          </div>

          <div v-if="loading.coreValues" class="py-20 text-center">
            <div class="spinner mx-auto"></div>
          </div>

          <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
            <div v-for="value in coreValues" :key="value.id" class="card-base group">
              <div
                class="w-16 h-16 rounded-2xl flex items-center justify-center mb-8 bg-primary/10 group-hover:scale-110 transition-transform duration-500">
                <component :is="getIconComponent(value.icon)" class="w-8 h-8 text-primary" />
              </div>
              <h3 class="campaign-header text-2xl text-secondary mb-4">{{ value.title }}</h3>
              <p class="text-lg text-black/70 leading-relaxed font-bold">{{ value.description }}</p>
            </div>
          </div>
        </div>
      </section>

      <!-- 5. History / Journey -->
      <section id="history" aria-labelledby="history-heading" class="section-padding bg-primary/5">
        <div class="container-custom">
          <div class="text-center mb-20">
            <h2 id="history-heading" class="campaign-header text-4xl text-secondary mb-6">Years of Dedicated Protection
            </h2>
            <p class="text-xl text-black max-w-2xl mx-auto font-bold opacity-70">
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
      <section id="partners" aria-labelledby="partners-heading" class="section-padding bg-neutral-white">
        <div class="container-custom">
          <div class="text-center mb-20">
            <h2 id="partners-heading" class="campaign-header text-4xl text-secondary mb-4">Trusted Partners</h2>
            <p class="text-xl text-black max-w-3xl mx-auto font-bold opacity-70">
              We work alongside leading organizations to deliver comprehensive support.
            </p>
          </div>

          <div v-if="loading.partners" class="py-20 text-center">
            <div class="spinner mx-auto"></div>
          </div>

          <div v-else class="bg-neutral-white rounded-[4rem] p-12 border-2 border-neutral-offwhite">
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