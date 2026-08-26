<template>
  <div class="min-h-screen bg-white overflow-x-hidden">
    <!-- Hero Banner -->
    <header class="hero-banner" style="padding-top: clamp(70px, 15vw, 90px);">
      <div class="hero-overlay"></div>
      <div class="container-custom hero-content-wrapper">
        <div class="hero-text">
          <h1 class="hero-title">
            {{ siteContent.getContent('operations_page_title', 'How We') }} <span class="text-accent-yellow">{{ siteContent.getContent('operations_page_title_highlight', 'Operate') }}</span>
          </h1>
          <p class="hero-subtitle">
            {{ siteContent.getContent('operations_page_subtitle', 'Sauti is a Swahili word that means voice. Discover how we serve every citizen across Uganda 24/7.') }}
          </p>
        </div>
      </div>
    </header>

    <div class="container-custom section-padding !pt-6 md:!pt-8">
      <!-- 2. Enhanced Journey Flow with Images -->
      <section class="mb-8 md:mb-16">
        <div class="text-center mb-6 md:mb-12 px-4">
          <h2 class="text-lg md:text-2xl lg:text-3xl font-bold text-secondary tracking-tight break-words">
            {{ siteContent.getContent('operations_journey_title', 'The Journey of a') }} <span class="text-primary">{{ siteContent.getContent('operations_journey_title_highlight', 'Voice') }}</span>
          </h2>
          <div class="w-16 h-1 bg-primary mx-auto mt-2 md:mt-4 rounded-full"></div>
          <p class="text-xs md:text-sm lg:text-base text-black/60 font-semibold mt-2 md:mt-4 max-w-2xl mx-auto break-words">
            {{ siteContent.getContent('operations_journey_subtitle', 'Every call goes through a carefully designed process to ensure the best possible outcome') }}
          </p>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-2 lg:grid-cols-4 gap-3 md:gap-6">
          <!-- Item 1: Access -->
          <div class="relative overflow-hidden rounded-2xl md:rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-500 group h-[240px] md:h-[400px]">
            <!-- Background Image -->
            <img
              :src="getJourneyImage(0)"
              :alt="siteContent.getContent('operations_journey_step1_title', 'Access')"
              width="400"
              height="500"
              loading="lazy"
              decoding="async"
              class="absolute inset-0 w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
            />
            <!-- Gradient Overlay - Stronger for text visibility -->
            <div class="absolute inset-0 bg-gradient-to-t from-primary via-primary/85 to-primary/30"></div>

            <!-- Content -->
            <div class="relative z-10 h-full flex flex-col justify-end p-4 md:p-6 text-white">
              <span class="text-xs md:text-sm font-bold tracking-widest uppercase mb-1 md:mb-2 text-white/90 break-words">{{ siteContent.getContent('operations_journey_step1_label', 'Step 1') }}</span>
              <h4 class="text-base md:text-xl lg:text-2xl font-bold mb-1 md:mb-3 break-words drop-shadow-sm">{{ siteContent.getContent('operations_journey_step1_title', 'Access') }}</h4>
              <p class="text-sm md:text-base lg:text-lg font-semibold text-white leading-relaxed break-words drop-shadow-sm">
                {{ siteContent.getContent('operations_journey_step1_description', 'Toll-free 116 available 24/7 from any network across Uganda.') }}
              </p>
            </div>
          </div>

          <!-- Item 2: Response -->
          <div class="relative overflow-hidden rounded-2xl md:rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-500 group h-[240px] md:h-[400px]">
            <img
              :src="getJourneyImage(1)"
              :alt="siteContent.getContent('operations_journey_step2_title', 'Response')"
              width="400"
              height="500"
              loading="lazy"
              decoding="async"
              class="absolute inset-0 w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-secondary-light via-secondary-light/85 to-secondary-light/30"></div>

            <div class="relative z-10 h-full flex flex-col justify-end p-4 md:p-6 text-white">
              <span class="text-xs md:text-sm font-bold tracking-widest uppercase mb-1 md:mb-2 text-white/90 break-words">{{ siteContent.getContent('operations_journey_step2_label', 'Step 2') }}</span>
              <h4 class="text-base md:text-xl lg:text-2xl font-bold mb-1 md:mb-3 break-words drop-shadow-sm">{{ siteContent.getContent('operations_journey_step2_title', 'Response') }}</h4>
              <p class="text-sm md:text-base lg:text-lg font-semibold text-white leading-relaxed break-words drop-shadow-sm">
                {{ siteContent.getContent('operations_journey_step2_description', 'Professional counselors responding in 26 local languages.') }}
              </p>
            </div>
          </div>

          <!-- Item 3: Management -->
          <div class="relative overflow-hidden rounded-2xl md:rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-500 group h-[240px] md:h-[400px]">
            <img
              :src="getJourneyImage(2)"
              :alt="siteContent.getContent('operations_journey_step3_title', 'Management')"
              width="400"
              height="500"
              loading="lazy"
              decoding="async"
              class="absolute inset-0 w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-hotline via-hotline/85 to-hotline/30"></div>

            <div class="relative z-10 h-full flex flex-col justify-end p-4 md:p-6 text-white">
              <span class="text-xs md:text-sm font-bold tracking-widest uppercase mb-1 md:mb-2 text-white/90 break-words">{{ siteContent.getContent('operations_journey_step3_label', 'Step 3') }}</span>
              <h4 class="text-base md:text-xl lg:text-2xl font-bold mb-1 md:mb-3 break-words drop-shadow-sm">{{ siteContent.getContent('operations_journey_step3_title', 'Management') }}</h4>
              <p class="text-sm md:text-base lg:text-lg font-semibold text-white leading-relaxed break-words drop-shadow-sm">
                {{ siteContent.getContent('operations_journey_step3_description', 'Case follow-up and specialized support coordination.') }}
              </p>
            </div>
          </div>

          <!-- Item 4: Protection -->
          <div class="relative overflow-hidden rounded-2xl md:rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-500 group h-[240px] md:h-[400px]">
            <img
              :src="getJourneyImage(3)"
              :alt="siteContent.getContent('operations_journey_step4_title', 'Protection')"
              width="400"
              height="500"
              loading="lazy"
              decoding="async"
              class="absolute inset-0 w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-secondary via-secondary/85 to-secondary/30"></div>

            <div class="relative z-10 h-full flex flex-col justify-end p-4 md:p-6 text-white">
              <span class="text-xs md:text-sm font-bold tracking-widest uppercase mb-1 md:mb-2 text-white/90 break-words">{{ siteContent.getContent('operations_journey_step4_label', 'Step 4') }}</span>
              <h4 class="text-base md:text-xl lg:text-2xl font-bold mb-1 md:mb-3 break-words drop-shadow-sm">{{ siteContent.getContent('operations_journey_step4_title', 'Protection') }}</h4>
              <p class="text-sm md:text-base lg:text-lg font-semibold text-white leading-relaxed break-words drop-shadow-sm">
                {{ siteContent.getContent('operations_journey_step4_description', 'Resolution and community reintegration support.') }}
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- 3. Enhanced Infrastructure Section with Split Layout -->
      <section class="mb-8 md:mb-16">
        <div class="bg-white rounded-2xl md:rounded-3xl overflow-hidden shadow-lg border border-gray-100">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-0">
            <!-- Left: Image Side -->
            <div class="relative min-h-[250px] md:min-h-[280px] lg:min-h-[320px]">
              <img
                :src="getInfrastructureImage()"
                alt="Infrastructure"
                width="800"
                height="800"
                loading="lazy"
                decoding="async"
                class="w-full h-full object-cover"
              />
              <div class="absolute inset-0 bg-gradient-to-br from-primary/40 to-secondary/40"></div>

              <!-- Floating Stats Card -->
              <div class="absolute bottom-4 left-4 right-4 md:bottom-6 md:left-6 md:right-6 bg-white/95 backdrop-blur-sm rounded-xl md:rounded-2xl p-3 md:p-4 shadow-xl">
                <div class="grid grid-cols-3 gap-2 md:gap-3">
                  <div class="text-center">
                    <div class="text-lg md:text-xl font-black text-primary">{{ siteContent.getContent('operations_infra_stat1_value', '26') }}</div>
                    <div class="text-[10px] md:text-xs text-black/60 font-bold">{{ siteContent.getContent('operations_infra_stat1_label', 'Languages') }}</div>
                  </div>
                  <div class="text-center border-x border-gray-200">
                    <div class="text-lg md:text-xl font-black text-secondary">{{ siteContent.getContent('operations_infra_stat2_value', '24/7') }}</div>
                    <div class="text-[10px] md:text-xs text-black/60 font-bold">{{ siteContent.getContent('operations_infra_stat2_label', 'Available') }}</div>
                  </div>
                  <div class="text-center">
                    <div class="text-lg md:text-xl font-black text-hotline">{{ siteContent.getContent('operations_infra_stat3_value', '100%') }}</div>
                    <div class="text-[10px] md:text-xs text-black/60 font-bold">{{ siteContent.getContent('operations_infra_stat3_label', 'Coverage') }}</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Right: Content Side -->
            <div class="p-5 md:p-6 lg:p-8 flex flex-col justify-center bg-neutral-offwhite">
              <div class="mb-2">
                <span class="inline-block px-2 md:px-3 py-0.5 md:py-1 rounded-full bg-primary/10 text-primary text-[10px] md:text-xs font-black tracking-widest border border-primary/20 uppercase">
                  {{ siteContent.getContent('operations_infra_badge', 'Our Foundation') }}
                </span>
              </div>

              <h2 class="text-base md:text-xl lg:text-2xl font-bold text-secondary mb-2 leading-tight break-words">
                {{ siteContent.getContent('operations_infra_title', 'A Robust Infrastructure for') }} <span class="text-primary">{{ siteContent.getContent('operations_infra_title_highlight', 'Nationwide Impact') }}</span>
              </h2>

              <p class="text-xs md:text-sm text-black/60 font-semibold mb-3 md:mb-4 leading-relaxed break-words">
                {{ siteContent.getContent('operations_infra_description', 'Our operations are built on sustainable pillars that ensure every caller receives expert attention, no matter where they are in Uganda.') }}
              </p>

              <!-- Pillars List -->
              <div class="space-y-2 md:space-y-3">
                <div v-for="(pillar, pi) in computedPillars" :key="pi"
                     class="flex gap-3 md:gap-4 items-start group">
                  <div class="flex-1 min-w-0">
                    <h5 class="text-sm md:text-base font-bold text-secondary mb-0.5 break-words">{{ pillar.title }}</h5>
                    <p class="text-xs md:text-sm text-black/60 font-medium leading-relaxed break-words">{{ pillar.desc }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 4. Key Facts -->
      <section class="mb-8 md:mb-16">
        <div class="text-center mb-6 md:mb-10 px-4">
          <h2 class="text-lg md:text-2xl lg:text-3xl font-bold text-secondary tracking-tight break-words">
            {{ siteContent.getContent('operations_key_facts_title', 'Operations at a') }} <span class="text-primary">{{ siteContent.getContent('operations_key_facts_title_highlight', 'Glance') }}</span>
          </h2>
          <div class="w-16 h-1 bg-primary mx-auto mt-2 md:mt-4 rounded-full"></div>
          <p class="text-xs md:text-sm lg:text-base text-black/60 font-semibold mt-2 md:mt-4 max-w-2xl mx-auto break-words">
            {{ siteContent.getContent('operations_page_description', 'Our comprehensive case management system ensures every report is handled with care and urgency.') }}
          </p>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-3 md:gap-6">
          <div v-for="(fact, fi) in computedKeyFacts" :key="fi"
               class="bg-neutral-offwhite rounded-2xl p-4 md:p-6 text-center shadow-sm hover:shadow-md transition-shadow">
            <h5 class="text-sm md:text-base font-bold text-secondary mb-1 md:mb-2 break-words">{{ fact.title }}</h5>
            <p class="text-xs md:text-sm text-black/60 font-medium leading-relaxed break-words">{{ fact.desc }}</p>
          </div>
        </div>
      </section>

      <!-- 5. Services Slideshow -->
      <section class="mb-6 md:mb-12">
        <div class="text-center mb-6 md:mb-10 px-4">
          <h2 class="text-xl md:text-3xl lg:text-4xl font-bold text-secondary mb-2 md:mb-3 lg:mb-4 break-words">
            {{ siteContent.getContent('services_section_title', 'Services We') }} <span class="text-primary">{{ siteContent.getContent('services_section_title_highlight', 'Offer') }}</span>
          </h2>
          <p class="text-sm md:text-base lg:text-lg text-black/60 font-semibold max-w-2xl mx-auto leading-relaxed break-words">
            {{ siteContent.getContent('services_section_subtitle', 'Comprehensive support systems protecting and empowering every voice in Uganda.') }}
          </p>
        </div>

        <!-- Large Slideshow Container -->
        <div
          class="services-slideshow relative overflow-hidden rounded-2xl md:rounded-3xl shadow-2xl mx-auto max-w-5xl h-[350px] md:h-[450px] lg:h-[550px]"
          @mouseenter="pauseServiceSlideshow"
          @mouseleave="resumeServiceSlideshow"
        >
          <!-- Slides -->
          <div v-for="(service, idx) in services" :key="idx"
               :class="[
                 'absolute inset-0 transition-all duration-700 ease-in-out',
                 currentServiceIndex === idx ? 'opacity-100 z-10' : 'opacity-0 z-0'
               ]">
            <img
              :src="getServiceImage(idx)"
              :alt="siteContent.getContent(service.cid_title, service.title)"
              width="800"
              height="600"
              :loading="idx === 0 ? 'eager' : 'lazy'"
              decoding="async"
              class="absolute inset-0 w-full h-full object-cover"
            />
            <!-- Stronger gradient for text visibility -->
            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/50 to-black/20"></div>

            <!-- Content - Larger text -->
            <div class="relative z-10 h-full flex flex-col justify-end p-6 md:p-10 lg:p-14 text-white">
              <span class="text-xs md:text-sm font-bold tracking-widest uppercase mb-2 md:mb-3 text-white/80">
                Service {{ idx + 1 }} of {{ services.length }}
              </span>
              <h3 class="text-2xl md:text-4xl lg:text-5xl font-bold mb-3 md:mb-4 drop-shadow-lg break-words">
                {{ siteContent.getContent(service.cid_title, service.title) }}
              </h3>
              <p class="text-base md:text-xl lg:text-2xl text-white font-medium leading-relaxed max-w-3xl drop-shadow-md break-words">
                {{ siteContent.getContent(service.cid_text, service.text) }}
              </p>
            </div>
          </div>

          <!-- Navigation Arrows -->
          <button
            @click="prevService"
            class="absolute left-4 top-1/2 -translate-y-1/2 z-20 w-12 h-12 md:w-14 md:h-14 bg-white/20 hover:bg-white/40 backdrop-blur-sm rounded-full flex items-center justify-center text-white transition-all shadow-lg"
            aria-label="Previous service"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="15 18 9 12 15 6"></polyline>
            </svg>
          </button>
          <button
            @click="nextService"
            class="absolute right-4 top-1/2 -translate-y-1/2 z-20 w-12 h-12 md:w-14 md:h-14 bg-white/20 hover:bg-white/40 backdrop-blur-sm rounded-full flex items-center justify-center text-white transition-all shadow-lg"
            aria-label="Next service"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </button>

          <!-- Dots Navigation -->
          <div class="absolute bottom-4 md:bottom-6 left-1/2 -translate-x-1/2 z-20 flex gap-2 md:gap-3">
            <button
              v-for="(service, idx) in services"
              :key="'dot-' + idx"
              @click="goToService(idx)"
              :class="[
                'w-3 h-3 md:w-4 md:h-4 rounded-full transition-all duration-300',
                currentServiceIndex === idx
                  ? 'bg-white scale-125'
                  : 'bg-white/40 hover:bg-white/70'
              ]"
              :aria-label="'Go to service ' + (idx + 1)"
            ></button>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { onMounted, onBeforeUnmount, ref, computed } from 'vue'
import { useSettingsStore } from '@/store/settings'
import { useSiteContent } from '@/composables/useSiteContent'

defineOptions({
  name: 'OperationsPage'
})

const services = [
  { title: 'Telephone Counseling', cid_title: 'service_counseling_title', cid_text: 'service_counseling_text', text: 'Professional counseling services available 24/7 through our toll-free helpline 116.' },
  { title: 'Walk-In Support', cid_title: 'service_walkin_title', cid_text: 'service_walkin_text', text: 'Handle walk-in clients at our offices for face-to-face consultation and support.' },
  { title: 'Media Response', cid_title: 'service_media_title', cid_text: 'service_media_text', text: 'Respond to cases of violence against children and gender-based violence reported through media and U-report.' },
  { title: 'Information & Guidance', cid_title: 'service_guidance_title', cid_text: 'service_guidance_text', text: 'Provision of information and guidance on child care and protection matters.' },
  { title: 'Essential Service Referrals', cid_title: 'service_referral_title', cid_text: 'service_referral_text', text: 'Referral to essential services including healthcare, legal aid, and social support.' },
  { title: 'Community Sensitization', cid_title: 'service_community_title', cid_text: 'service_community_text', text: 'Community sensitization activities to raise awareness about child protection and GBV prevention.' },
  { title: 'MHPSS Chatbot', cid_title: 'service_chatbot_title', cid_text: 'service_chatbot_text', text: 'Mental Health and Psychosocial Support chatbot for immediate automated assistance.' }
]

const settingsStore = useSettingsStore()
const siteContent = useSiteContent('operations')

// Services Slideshow
const currentServiceIndex = ref(0)
let serviceSlideshowInterval = null
const isSlideshowPaused = ref(false)

// Operations page images from API
const operationsImages = ref([])

// Computed pillars using CMS content
const computedPillars = computed(() => [
  {
    title: siteContent.getContent('operations_pillar1_title', '26 Local Languages'),
    desc: siteContent.getContent('operations_pillar1_description', 'Bridging the communication gap for every community in Uganda.')
  },
  {
    title: siteContent.getContent('operations_pillar2_title', '24/7 Availability'),
    desc: siteContent.getContent('operations_pillar2_description', 'Support is always just a phone call away, day or night.')
  },
  {
    title: siteContent.getContent('operations_pillar3_title', 'Sustainable Funding'),
    desc: siteContent.getContent('operations_pillar3_description', 'Partnering with MGLSD and UNICEF for long-term service stability.')
  }
])

// Computed key facts using CMS content
const computedKeyFacts = computed(() => [
  {
    title: siteContent.getContent('operations_availability_title', '24/7 Nationwide Coverage'),
    desc: siteContent.getContent('operations_availability_text', 'Operational 24/7 and accessible from every part of the country.')
  },
  {
    title: siteContent.getContent('operations_shortcode_title', 'Toll-Free Access'),
    desc: siteContent.getContent('operations_shortcode_text', 'Operates on the short code 116 (toll free) accessible from any telecom network.')
  },
  {
    title: siteContent.getContent('operations_languages_title', 'Multilingual Counselors'),
    desc: siteContent.getContent('operations_languages_text', 'Our counselors speak a total of 26 local languages to serve every community.')
  },
  {
    title: siteContent.getContent('operations_structure_title', 'Two-Division Structure'),
    desc: siteContent.getContent('operations_structure_text', 'Divided into 2 sections: call center for immediate response and case work for follow-up support.')
  },
  {
    title: siteContent.getContent('operations_funding_title', 'Funding & Support'),
    desc: siteContent.getContent('operations_funding_text', 'Government of Uganda covers utility bills and 14% of salaries, while donors (UNICEF) support case management funds and project staff salaries.')
  }
])

// Default fallback images for Journey section
const defaultJourneyImages = [
  'https://images.unsplash.com/photo-1423666639041-f56000c27a9a?w=400&h=500&fit=crop', // Step 1: Access
  'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&h=500&fit=crop', // Step 2: Response
  'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=400&h=500&fit=crop', // Step 3: Management
  'https://images.unsplash.com/photo-1469571486292-0ba58a3f068b?w=400&h=500&fit=crop'  // Step 4: Protection
]

// Default fallback images for Services section
const defaultServiceImages = [
  'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&h=600&fit=crop', // Service 1: Telephone Counseling
  'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=400&h=300&fit=crop', // Service 2: Walk-In Support
  'https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=400&h=600&fit=crop', // Service 3: Media Response
  'https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=400&h=300&fit=crop', // Service 4: Information & Guidance
  'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=400&h=300&fit=crop', // Service 5: Essential Service Referrals
  'https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=800&h=300&fit=crop', // Service 6: Community Sensitization
  'https://images.unsplash.com/photo-1531746790731-6c087fecd65a?w=800&h=300&fit=crop'  // Service 7: MHPSS Chatbot
]

// Default infrastructure image
const defaultInfraImage = 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&h=800&fit=crop'

// Helper function to get Journey images (from API or fallback)
const getJourneyImage = (index) => {
  // Look for uploaded journey images first
  const journeyImage = operationsImages.value.find(img => img.position === `journey_step_${index + 1}`)
  if (journeyImage?.image_url) {
    return journeyImage.image_url
  }
  return defaultJourneyImages[index] || defaultJourneyImages[0]
}

// Helper function to get Service images (from API or fallback)
const getServiceImage = (index) => {
  // Look for uploaded service images first
  const serviceKeys = ['counseling', 'walkin', 'media', 'guidance', 'referral', 'community', 'chatbot']
  const serviceImage = operationsImages.value.find(img => img.position === `service_${serviceKeys[index]}`)
  if (serviceImage?.image_url) {
    return serviceImage.image_url
  }
  return defaultServiceImages[index] || defaultServiceImages[0]
}

// Helper function to get Infrastructure image (from API or fallback)
const getInfrastructureImage = () => {
  const infraImage = operationsImages.value.find(img => img.position === 'infrastructure')
  if (infraImage?.image_url) {
    return infraImage.image_url
  }
  return defaultInfraImage
}

// Fetch operations images from API
const fetchOperationsImages = async () => {
  try {
    const response = await fetch(`${import.meta.env.VITE_API_URL || ''}/content/operations-images/`)
    if (response.ok) {
      operationsImages.value = await response.json()
    }
  } catch (error) {
    console.warn('Failed to fetch operations images, using defaults:', error)
  }
}

// Services Slideshow Functions
const startServiceSlideshow = () => {
  serviceSlideshowInterval = setInterval(() => {
    if (isSlideshowPaused.value) return
    currentServiceIndex.value = (currentServiceIndex.value + 1) % services.length
  }, 5000) // Change slide every 5 seconds
}

const pauseServiceSlideshow = () => {
  isSlideshowPaused.value = true
}

const resumeServiceSlideshow = () => {
  isSlideshowPaused.value = false
}

const nextService = () => {
  currentServiceIndex.value = (currentServiceIndex.value + 1) % services.length
}

const prevService = () => {
  currentServiceIndex.value = (currentServiceIndex.value - 1 + services.length) % services.length
}

const goToService = (index) => {
  currentServiceIndex.value = index
}

onMounted(async () => {
  await siteContent.fetchContent()
  await settingsStore.fetchGlobalSettings()
  await fetchOperationsImages()

  // Start services slideshow after a short delay
  setTimeout(() => {
    startServiceSlideshow()
  }, 500)
})

onBeforeUnmount(() => {
  if (serviceSlideshowInterval) {
    clearInterval(serviceSlideshowInterval)
  }
})
</script>

<style scoped>
/* Hero Banner */
/* Hero banner styles are global now — see .hero-banner et al. in main.css */

.animate-fade-in-up {
  animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Services Slideshow — brand gradient (deep green → sky blue) instead of
   an off-palette navy, so the section reads as intentional Sauti branding. */
.services-slideshow {
  background: linear-gradient(135deg, rgb(var(--color-secondary)) 0%, rgb(var(--color-primary-dark)) 100%);
}

</style>
