<template>
  <div>
    <!-- 1. Hero Section -->
    <section class="page-header !border-b-0">
      <div class="container-custom relative">
        <div class="max-w-5xl mx-auto text-center space-y-10">
          <div class="space-y-6">
            <h1 class="page-header-title">
              {{ settingsStore.settings.hero_title || `Report Any Form of Violence. Call 116.` }}
            </h1>
            <p class="page-header-subtitle mx-auto">
              {{ settingsStore.settings.hero_value_prop || `Uganda’s National Helpline providing confidential, 24/7
              protection and immediate response.` }}
            </p>
          </div>

          <div class="cta-group justify-center">
            <BaseCTA variant="emergency" size="hero" :href="`tel:${settingsStore.settings.hotline_number || '116'}`"
              class="!px-12 !py-6 shadow-2xl" external>
              <PhoneIcon class="w-8 h-8" />
              <span class="text-3xl font-bold uppercase tracking-tight">CALL {{ settingsStore.settings.hotline_number
                || '116' }}</span>
            </BaseCTA>

            <BaseCTA to="/report" variant="emergency" size="hero"
              class="!px-12 !py-6 shadow-2xl opacity-90 transition-opacity hover:opacity-100">
              <ShieldCheckIcon class="w-8 h-8" />
              <span class="text-3xl font-bold uppercase tracking-tight">{{ settingsStore.settings.primary_cta_text ||
                `REPORT VIOLENCE`
                }}</span>
            </BaseCTA>
          </div>

          <div class="pt-8">
            <p class="text-sm font-bold uppercase tracking-[0.3em] text-sauti-darkGreen/40">
              <span class="border-t-2 border-sauti-orange pt-4 inline-block">A Government of Uganda Initiative</span>
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. Intro Section -->
    <section class="section-padding bg-sauti-blue/5 overflow-hidden">
      <div class="container-custom">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <div class="space-y-8">
            <h2
              class="campaign-header text-3xl md:text-4xl text-sauti-darkGreen border-b-4 border-sauti-blue inline-block pb-2">
              {{ settingsStore.settings.intro_title || `National Mandate` }}
            </h2>
            <p class="text-xl md:text-2xl text-sauti-darkGreen leading-relaxed font-bold">
              {{ settingsStore.settings.intro_description || `Under the Ministry of Gender, Labour and Social
              Development,
              Sauti 116 serves as Uganda’s primary response mechanism for child protection and social safety.` }}
            </p>
            <div class="pt-4">
              <BaseCTA to="/about" variant="outline" class="group">
                Discover Our Story
                <ArrowRightIcon class="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </BaseCTA>
            </div>
          </div>
          <div class="relative group">
            <div
              class="absolute -inset-4 bg-sauti-blue/10 rounded-[4rem] group-hover:bg-sauti-blue/20 transition-all duration-700 -rotate-2">
            </div>
            <div class="relative rounded-[3.5rem] overflow-hidden border-4 border-sauti-blue shadow-2xl">
              <img src="@/assets/helpline-center.png" alt="Sauti 116 Helpline Operations Center"
                class="w-full h-[500px] object-cover transition-transform duration-1000 group-hover:scale-110" />
              <div class="absolute inset-0 bg-gradient-to-t from-sauti-darkGreen/60 via-transparent to-transparent">
              </div>
              <div class="absolute bottom-8 left-8 right-8">
                <p class="campaign-header text-white text-xs tracking-widest opacity-80 uppercase">Real-time Response
                </p>
                <p class="text-white font-bold text-xl">Operational 24/7 Nationwide</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. Services Section -->
    <section id="services" class="section-padding bg-sauti-white">
      <div class="container-custom">
        <div class="text-center mb-16">
          <h2 class="campaign-header text-4xl mb-4 text-sauti-darkGreen">{{ settingsStore.settings.services_title ||
            `Core Protection Services` }}</h2>
          <p class="text-xl text-sauti-darkGreen max-w-2xl mx-auto">{{ settingsStore.settings.services_description ||
            `Immediate response and support across national priority protection areas.` }}</p>
        </div>

        <div class="space-y-6 max-w-5xl mx-auto">
          <div v-if="helpServicesStore.loading" class="text-center py-12">
            <div class="animate-spin rounded-full h-12 w-12 border-b-4 border-sauti-blue mx-auto"></div>
          </div>

          <template v-else>
            <ServiceExpandableCard v-for="service in helpServicesStore.services" :key="service.id" :id="service.key"
              :service="service" :is-open="expandedServiceKey === service.key" @toggle="toggleService(service.key)"
              :hotline-number="settingsStore.settings.hotline_number" />
          </template>
        </div>
      </div>
    </section>

    <!-- 4. Latest News / Blogs -->
    <section v-if="latestVideos.length > 0" class="section-padding bg-sauti-neutral">
      <div class="container-custom">
        <div class="flex flex-col md:flex-row justify-between items-end mb-12 gap-6">
          <div class="text-left">
            <h2 class="campaign-header text-4xl text-sauti-darkGreen mb-4">{{ settingsStore.settings.news_title ||
              `Helpline
              Updates` }}</h2>
            <p class="text-xl text-sauti-darkGreen max-w-2xl">{{ settingsStore.settings.news_description || `Official
              news
              and impact reports from the National Helpline.` }}</p>
          </div>
          <router-link to="/blogs" class="btn-outline flex items-center gap-2 mb-2">
            {{ settingsStore.settings.news_link_text || `View All News` }}
            <ArrowRightIcon class="w-5 h-5" />
          </router-link>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="post in latestVideos" :key="post.id" class="group cursor-pointer">
            <div
              class="relative rounded-3xl overflow-hidden aspect-[16/10] shadow-xl group-hover:shadow-2xl transition-all duration-500">
              <img :src="post.thumbnail" :alt="post.title"
                class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700" />
              <div class="absolute inset-0 bg-sauti-blue/40 group-hover:bg-sauti-darkGreen/60 transition-colors">
              </div>

              <div class="absolute bottom-6 left-6 right-6">
                <span
                  class="inline-block px-3 py-1 bg-sauti-orange text-sauti-white text-xs font-bold rounded-lg mb-3 shadow-lg">
                  {{ post.category }}
                </span>
                <h3 class="text-xl font-bold text-white leading-tight line-clamp-2">
                  {{ post.title }}
                </h3>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. Partner Logos -->
    <section class="section-padding bg-sauti-white">
      <div class="container-custom">
        <div class="text-center mb-16">
          <h2 class="campaign-header text-4xl text-sauti-darkGreen mb-4">
            {{ settingsStore.settings.partners_title || `Development Partners` }}
          </h2>
          <p class="text-xl text-sauti-darkGreen font-bold opacity-70">
            {{ settingsStore.settings.partners_description || `Partnering for a safer Uganda.` }}
          </p>
        </div>

        <PartnerGrid :partners="partners" class="opacity-60" />
      </div>
    </section>
  </div>
</template>

<script setup>
  import { ref, onMounted, computed } from 'vue'
  import { usePartnersStore } from '@/store/partners'
  import { useBlogStore } from '@/store/blog'
  import { useSettingsStore } from '@/store/settings'
  import { useHelpServicesStore } from '@/store/help-services'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import PartnerGrid from '@/components/common/PartnerGrid.vue'
  import ServiceExpandableCard from '@/components/home/ServiceExpandableCard.vue'
  import {
    PhoneIcon,
    ShieldCheckIcon,
    ArrowRightIcon
  } from '@heroicons/vue/24/outline'

  defineOptions({
    name: 'HomePage'
  })

  const partnersStore = usePartnersStore()
  const blogStore = useBlogStore()
  const settingsStore = useSettingsStore()
  const helpServicesStore = useHelpServicesStore()

  const latestVideos = ref([])
  const loadingVideos = ref(false)
  const partners = ref([])
  const expandedServiceKey = ref(null)

  const toggleService = (key) => {
    if (expandedServiceKey.value === key) {
      expandedServiceKey.value = null
    } else {
      expandedServiceKey.value = key
      // Smooth scroll to card after it has a chance to expand
      setTimeout(() => {
        const el = document.getElementById(key)
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'start' })
        }
      }, 100)
    }
  }

  const activeBadges = computed(() => {
    const badges = settingsStore.settings?.hero_badges
    if (Array.isArray(badges)) {
      return badges.filter(b => b && b.is_active)
    }
    return []
  })

  onMounted(async () => {
    // Load all data concurrently
    const results = await Promise.allSettled([
      settingsStore.fetchGlobalSettings(),
      partnersStore.fetchPartners(),
      blogStore.fetchPosts({
        status: 'PUBLISHED',
        ordering: '-published_at,-created_at',
        limit: 3
      }),
      helpServicesStore.fetchServices()
    ])

    // Handle partners result
    if (results[1].status === 'fulfilled') {
      const partnersData = partnersStore.partners
      console.log('Partners data loaded:', partnersData)
      // Ensure we are setting an array, regardless of potential proxy/reactivity nesting
      if (Array.isArray(partnersData)) {
        partners.value = [...partnersData]
      } else if (partnersData && partnersData.results && Array.isArray(partnersData.results)) {
        partners.value = [...partnersData.results]
      } else {
        partners.value = []
      }
    } else {
      console.error('Failed to load partners:', results[1].reason)
      partners.value = []
    }

    // Handle blog posts result
    if (results[2].status === 'fulfilled') {
      latestVideos.value = blogStore.posts
        .filter(post => post.featured_image)
        .map(post => ({
          id: post.id,
          title: post.title,
          category: post.category?.name || 'Story',
          thumbnail: post.featured_image
        }))
    } else {
      console.error('Failed to load recent publications:', results[2].reason)
    }

    // Help Services handled by store state directly

    // Auto-expand from hash if valid service key
    const hash = window.location.hash.replace('#', '')
    if (hash && helpServicesStore.services.some(s => s.key === hash)) {
      expandedServiceKey.value = hash
    }

    loadingVideos.value = false
  })
</script>

<style scoped>
  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .line-clamp-3 {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .section-padding {
    padding-top: 5rem;
    padding-bottom: 5rem;
  }

  @media (min-width: 768px) {
    .section-padding {
      padding-top: 8rem;
      padding-bottom: 8rem;
    }
  }

  .avm-card {
    padding: 2rem;
    border-radius: 1.5rem;
    border-width: 1px;
    border-style: solid;
    border-color: theme('colors.sauti.white');
    background-color: theme('colors.sauti.white');
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .avm-card:hover {
    box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
  }

  .avm-icon {
    width: 4rem;
    height: 4rem;
    border-radius: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.5rem;
  }

  .avm-title {
    font-size: 1.25rem;
    line-height: 1.75rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: theme('colors.sauti.darkGreen');
  }

  .avm-text {
    line-height: 1.625;
    color: theme('colors.sauti.darkGreen');
  }
</style>
