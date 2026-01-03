<template>
  <div>
    <!-- 1. Hero Section -->
    <section class="relative overflow-hidden bg-white">
      <div class="container-custom relative py-16 md:py-24 lg:py-32">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          <div class="lg:col-span-12 text-center space-y-8">
            <div class="space-y-6 max-w-4xl mx-auto">
              <h1
                class="text-5xl md:text-6xl lg:text-7xl font-extrabold tracking-tight leading-tight text-darkGreen">
                {{ settingsStore.settings.hero_title || 'Your Voice is Powerful. Report Violence and Find Safety.' }}
              </h1>
              <p class="text-xl md:text-2xl text-darkGreen leading-relaxed max-w-3xl mx-auto">
                {{ settingsStore.settings.hero_value_prop || `Sauti 116 is Uganda’s national helpline providing
                confidential, 24/7 support.` }}
              </p>
            </div>

            <div class="flex flex-col sm:flex-row gap-6 justify-center items-center">
              <BaseCTA variant="emergency" size="hero" :href="`tel:${settingsStore.settings.hotline_number || '116'}`"
                class="gap-4" external>
                <PhoneIcon class="w-8 h-8" />
                <span>Call {{ settingsStore.settings.hotline_number || '116' }}</span>
              </BaseCTA>

              <BaseCTA to="/report" variant="primary" size="hero" class="gap-4">
                <ShieldCheckIcon class="w-8 h-8" />
                <span>{{ settingsStore.settings.primary_cta_text || 'Report Violence' }}</span>
              </BaseCTA>
            </div>

            <div class="flex flex-wrap justify-center gap-4 pt-8">
              <p class="text-sm font-bold uppercase tracking-widest text-darkGreen">A Government of Uganda
                initiative for immediate response to violence and abuse.</p>
            </div>


          </div>
        </div>
      </div>
    </section>

    <!-- 2. Intro Section -->
    <section class="section-padding bg-sauti-white border-y border-white">
      <div class="container-custom">
        <div class="max-w-4xl mx-auto text-center">
          <h2
            class="text-3xl md:text-4xl font-bold mb-8 text-darkGreen border-b-4 border-blue inline-block pb-2">
            {{ settingsStore.settings.intro_title || 'Our Mandate' }}
          </h2>
          <p class="text-xl md:text-2xl text-darkGreen leading-relaxed font-medium">
            {{ settingsStore.settings.intro_description || `Sauti 116 is Uganda’s National Child Helpline, providing
            support and crisis intervention for those in need.` }}
          </p>
        </div>
      </div>
    </section>

    <!-- 3. Services Section -->
    <section id="services" class="section-padding bg-white">
      <div class="container-custom">
        <div class="text-center mb-16">
          <h2 class="text-4xl font-bold mb-4 text-darkGreen">{{ settingsStore.settings.services_title || `Our
            Services for Your Protection` }}</h2>
          <p class="text-xl text-darkGreen max-w-2xl mx-auto">{{ settingsStore.settings.services_description ||
            'Access immediate support across these key protection areas.' }}</p>
        </div>

        <div class="space-y-6 max-w-5xl mx-auto">
          <div v-if="helpServicesStore.loading" class="text-center py-12">
            <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue mx-auto"></div>
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
    <section v-if="latestVideos.length > 0" class="section-padding bg-sauti-white">
      <div class="container-custom">
        <div class="flex flex-col md:flex-row justify-between items-end mb-12 gap-6">
          <div class="text-left">
            <h2 class="text-4xl font-bold text-darkGreen mb-4">{{ settingsStore.settings.news_title || `Latest
              Updates`
            }}</h2>
            <p class="text-xl text-darkGreen max-w-2xl">{{ settingsStore.settings.news_description || `Stories of
              impact
              and important information from Sauti 116.` }}</p>
          </div>
          <router-link to="/blogs" class="btn-outline flex items-center gap-2 mb-2">
            {{ settingsStore.settings.news_link_text || 'View All News' }}
            <ArrowRightIcon class="w-5 h-5" />
          </router-link>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="post in latestVideos" :key="post.id" class="group cursor-pointer">
            <div
              class="relative rounded-3xl overflow-hidden aspect-[16/10] shadow-xl group-hover:shadow-2xl transition-all duration-500">
              <img :src="post.thumbnail" :alt="post.title"
                class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700" />
              <div class="absolute inset-0 bg-black/20 opacity-60 group-hover:opacity-80 transition-opacity">
              </div>

              <div class="absolute bottom-6 left-6 right-6">
                <span
                  class="inline-block px-3 py-1 bg-orange text-white text-xs font-bold rounded-full mb-3 shadow-lg">
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
    <section class="py-20 bg-sauti-white border-t border-white">
      <div class="container-custom">
        <div class="text-center mb-12">
          <h3 class="text-2xl font-bold text-darkGreen mb-4">{{ settingsStore.settings.partners_title || `Our
            Partners`
          }}</h3>
          <p class="text-darkGreen">{{ settingsStore.settings.partners_description || `Working together with
            organizations committed to protecting children.` }}</p>
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
    border-color: theme('colors.white');
    background-color: theme('colors.white');
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
    color: theme('colors.darkGreen');
  }

  .avm-text {
    line-height: 1.625;
    color: theme('colors.darkGreen');
  }
</style>
