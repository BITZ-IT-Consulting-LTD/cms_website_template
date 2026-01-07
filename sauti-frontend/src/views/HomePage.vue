<template>
  <div>
    <!-- 1. Hero Section -->
    <section class="page-header !border-b-0">
      <div class="container-custom relative">
        <div class="max-w-5xl mx-auto text-center space-y-10">
          <div class="space-y-6">
            <h1 class="mb-8 font-black text-secondary leading-[1.1] tracking-tight">
              Someone is listening. <span
                class="text-primary border-b-8 border-accent-yellow/40 transition-all hover:border-accent-yellow">A safe
                space</span> for you, anytime.
            </h1>
            <p class="page-header-subtitle mx-auto max-w-2xl">
              Sauti 116 is Uganda’s 24/7 helpline for children and adults. Whatever you’re going through, we’re here
              to listen, support, and help you stay safe.
            </p>
          </div>

          <div class="flex flex-col items-center gap-8">
            <!-- The One Primary Action: Call 116 (Signal Red for life-saving focus) -->
            <BaseCTA variant="emergency" size="hero" :href="`tel:${settingsStore.settings.hotline_number || '116'}`"
              class="w-full max-w-md !py-8 shadow-2xl ring-8 ring-white/10 group" external>
              <div class="flex items-center justify-center gap-4">
                <div class="bg-white/20 p-4 rounded-2xl group-hover:scale-110 transition-transform">
                  <PhoneIcon class="w-12 h-12 text-white" stroke-width="2.5" />
                </div>
                <div class="text-left">
                  <span class="text-xs font-black tracking-[0.3em] opacity-80 block mb-1">Emergency 24/7</span>
                  <span class="text-4xl font-black tracking-tighter">CALL {{
                    settingsStore.settings.hotline_number || '116' }}</span>
                </div>
              </div>
            </BaseCTA>

            <!-- Secondary Path: Clearly differentiated by Color & Style -->
            <div class="flex flex-wrap justify-center gap-6 pt-6">
              <BaseCTA @click="toggleService('child-abuse')" variant="secondary" size="lg"
                class="!px-8 shadow-lg ring-1 ring-secondary/20">
                <InformationCircleIcon class="w-6 h-6 mr-2 opacity-80" />
                <span>How we help</span>
              </BaseCTA>

              <BaseCTA to="/report" variant="primary" size="lg" class="!px-8 shadow-lg ring-1 ring-primary/20">
                <ShieldCheckIcon class="w-6 h-6 mr-2 opacity-80" />
                <span>Report Violence Online</span>
              </BaseCTA>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- 2. Intro Section -->
    <section class="section-padding bg-primary/5 overflow-hidden">
      <div class="container-custom">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <div class="space-y-10">
            <div
              class="inline-flex items-center gap-2 px-4 py-2 bg-secondary-light/10 text-secondary-light rounded-full font-black text-[10px] uppercase tracking-[0.2em] border border-secondary-light/20">
              <HeartIcon class="w-4 h-4" />
              <span>Our Impact</span>
            </div>
            <h2 class="text-secondary">Uganda’s Institutional <span class="text-secondary-light">Action Center</span>.
            </h2>
            <p class="text-xl font-bold leading-relaxed text-secondary/60">
              Managed by the Ministry of Gender, Labour and Social Development, we coordinate a nationwide network of
              protection experts, legal advocates, and health providers to ensure immediate safety for every child and
              survivor.
            </p>
            <div class="pt-4">
              <BaseCTA to="/about" variant="secondary" class="shadow-md">
                Learn About Sauti 116
                <ArrowRightIcon class="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform" />
              </BaseCTA>
            </div>
          </div>
          <div class="relative group">
            <div
              class="absolute -inset-4 bg-primary/10 rounded-[4rem] group-hover:bg-primary/20 transition-all duration-700 -rotate-2">
            </div>
            <div class="relative rounded-[4rem] overflow-hidden shadow-2xl group">
              <img src="@/assets/diverse_helpline_operations.png"
                alt="Diverse Sauti 116 Helpline counselors serving the nation"
                class="w-full h-[600px] object-cover transition-transform duration-1000 group-hover:scale-110" />
              <div class="absolute inset-0 bg-gradient-to-t from-secondary/60 via-transparent to-transparent">
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
    <section id="services" class="section-padding bg-neutral-white">
      <div class="container-custom">
        <div class="text-center mb-16">
          <h2 class="campaign-header text-4xl mb-4 text-secondary">{{ settingsStore.settings.services_title ||
            `Ways We Protect You` }}</h2>
          <p class="text-xl text-secondary max-w-2xl mx-auto font-bold opacity-70">{{
            settingsStore.settings.services_description ||
            `We offer support for different types of safety needs. Select an option below to learn more.` }}</p>
        </div>

        <div class="space-y-6 max-w-5xl mx-auto">
          <div v-if="helpServicesStore.loading" class="text-center py-12">
            <div class="animate-spin rounded-full h-12 w-12 border-b-4 border-primary mx-auto"></div>
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
    <section v-if="latestVideos.length > 0" class="section-padding bg-neutral-offwhite">
      <div class="container-custom">
        <div class="flex flex-col md:flex-row justify-between items-end mb-12 gap-6">
          <div class="text-left">
            <h2 class="campaign-header text-4xl text-secondary mb-4">{{ settingsStore.settings.news_title ||
              `Impact Stories & News` }}</h2>
            <p class="text-xl text-secondary max-w-2xl font-bold opacity-70">{{ settingsStore.settings.news_description
              ||
              `Stories and news from our team on how we are making Uganda safer.` }}</p>
          </div>
          <BaseCTA to="/blogs" variant="outline" size="sm" class="!rounded-full border-primary/20 text-primary">
            {{ settingsStore.settings.news_link_text || `See Latest Stories` }}
            <ArrowRightIcon class="w-4 h-4 ml-2" />
          </BaseCTA>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
          <div v-for="post in latestVideos" :key="post.id" class="group cursor-pointer">
            <div
              class="relative rounded-3xl overflow-hidden aspect-[16/10] shadow-xl group-hover:shadow-2xl transition-all duration-500">
              <img :src="post.thumbnail" :alt="post.title"
                class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700" />
              <div class="absolute inset-0 bg-primary/40 group-hover:bg-secondary/60 transition-colors">
              </div>

              <div class="absolute bottom-6 left-6 right-6">
                <span
                  class="inline-block px-3 py-1 bg-accent-orange text-neutral-white text-xs font-bold rounded-lg mb-3 shadow-lg">
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
    <section class="section-padding bg-neutral-white">
      <div class="container-custom">
        <div class="text-center mb-16">
          <h2 class="campaign-header text-4xl text-secondary mb-4">
            {{ settingsStore.settings.partners_title || `Official Protection Partners` }}
          </h2>
          <p class="text-xl text-secondary font-bold opacity-70">
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
    ArrowRightIcon,
    InformationCircleIcon
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
    @apply py-20;
  }

  @media (min-width: 768px) {
    .section-padding {
      @apply py-32;
    }
  }

  /* Support for any legacy AVM classes if they surface from dynamic content */
  .avm-card {
    @apply p-8 rounded-[1.5rem] border border-neutral-offwhite bg-neutral-white transition-all duration-300 ease-in-out hover:shadow-xl;
  }

  .avm-icon {
    @apply w-16 h-16 rounded-2xl flex items-center justify-center mb-6;
  }

  .avm-title {
    @apply text-xl font-bold mb-4 text-secondary;
  }

  .avm-text {
    @apply leading-relaxed text-secondary;
  }
</style>
