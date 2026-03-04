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
            The Journey of a <span class="text-primary">Voice</span>
          </h2>
          <div class="w-16 h-1 bg-primary mx-auto mt-2 md:mt-4 rounded-full"></div>
          <p class="text-xs md:text-sm lg:text-base text-black/60 font-semibold mt-2 md:mt-4 max-w-2xl mx-auto break-words">
            Every call goes through a carefully designed process to ensure the best possible outcome
          </p>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-2 lg:grid-cols-4 gap-3 md:gap-6">
          <!-- Item 1: Access -->
          <div class="relative overflow-hidden rounded-2xl md:rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-500 group h-[240px] md:h-[400px]">
            <!-- Background Image -->
            <img
              src="https://images.unsplash.com/photo-1423666639041-f56000c27a9a?w=400&h=500&fit=crop"
              alt="Access"
              class="absolute inset-0 w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
            />
            <!-- Gradient Overlay -->
            <div class="absolute inset-0 bg-gradient-to-t from-primary via-primary/80 to-transparent opacity-90"></div>

            <!-- Content -->
            <div class="relative z-10 h-full flex flex-col justify-end p-3 md:p-6 text-white">
              <span class="text-[10px] md:text-xs font-bold tracking-widest uppercase mb-1 md:mb-2 text-white/80 break-words">Step 1</span>
              <h4 class="text-sm md:text-lg lg:text-xl font-bold mb-1 md:mb-2 break-words">Access</h4>
              <p class="text-[10px] md:text-xs lg:text-sm font-medium text-white/90 leading-relaxed break-words">
                Toll-free 116 available 24/7 from any network across Uganda.
              </p>
            </div>
          </div>

          <!-- Item 2: Response -->
          <div class="relative overflow-hidden rounded-2xl md:rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-500 group h-[240px] md:h-[400px]">
            <img
              src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&h=500&fit=crop"
              alt="Response"
              class="absolute inset-0 w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-secondary-light via-secondary-light/80 to-transparent opacity-90"></div>

            <div class="relative z-10 h-full flex flex-col justify-end p-3 md:p-6 text-white">
              <span class="text-[10px] md:text-xs font-bold tracking-widest uppercase mb-1 md:mb-2 text-white/80 break-words">Step 2</span>
              <h4 class="text-sm md:text-lg lg:text-xl font-bold mb-1 md:mb-2 break-words">Response</h4>
              <p class="text-[10px] md:text-xs lg:text-sm font-medium text-white/90 leading-relaxed break-words">
                Professional counselors responding in 26 local languages.
              </p>
            </div>
          </div>

          <!-- Item 3: Management -->
          <div class="relative overflow-hidden rounded-2xl md:rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-500 group h-[240px] md:h-[400px]">
            <img
              src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=400&h=500&fit=crop"
              alt="Management"
              class="absolute inset-0 w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-hotline via-hotline/80 to-transparent opacity-90"></div>

            <div class="relative z-10 h-full flex flex-col justify-end p-3 md:p-6 text-white">
              <span class="text-[10px] md:text-xs font-bold tracking-widest uppercase mb-1 md:mb-2 text-white/80 break-words">Step 3</span>
              <h4 class="text-sm md:text-lg lg:text-xl font-bold mb-1 md:mb-2 break-words">Management</h4>
              <p class="text-[10px] md:text-xs lg:text-sm font-medium text-white/90 leading-relaxed break-words">
                Case follow-up and specialized support coordination.
              </p>
            </div>
          </div>

          <!-- Item 4: Protection -->
          <div class="relative overflow-hidden rounded-2xl md:rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-500 group h-[240px] md:h-[400px]">
            <img
              src="https://images.unsplash.com/photo-1469571486292-0ba58a3f068b?w=400&h=500&fit=crop"
              alt="Protection"
              class="absolute inset-0 w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-secondary via-secondary/80 to-transparent opacity-90"></div>

            <div class="relative z-10 h-full flex flex-col justify-end p-3 md:p-6 text-white">
              <span class="text-[10px] md:text-xs font-bold tracking-widest uppercase mb-1 md:mb-2 text-white/80 break-words">Step 4</span>
              <h4 class="text-sm md:text-lg lg:text-xl font-bold mb-1 md:mb-2 break-words">Protection</h4>
              <p class="text-[10px] md:text-xs lg:text-sm font-medium text-white/90 leading-relaxed break-words">
                Resolution and community reintegration support.
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
                src="https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&h=800&fit=crop"
                alt="Infrastructure"
                class="w-full h-full object-cover"
              />
              <div class="absolute inset-0 bg-gradient-to-br from-primary/40 to-secondary/40"></div>

              <!-- Floating Stats Card -->
              <div class="absolute bottom-4 left-4 right-4 md:bottom-6 md:left-6 md:right-6 bg-white/95 backdrop-blur-sm rounded-xl md:rounded-2xl p-3 md:p-4 shadow-xl">
                <div class="grid grid-cols-3 gap-2 md:gap-3">
                  <div class="text-center">
                    <div class="text-lg md:text-xl font-black text-primary">26</div>
                    <div class="text-[10px] md:text-xs text-black/60 font-bold">Languages</div>
                  </div>
                  <div class="text-center border-x border-gray-200">
                    <div class="text-lg md:text-xl font-black text-secondary">24/7</div>
                    <div class="text-[10px] md:text-xs text-black/60 font-bold">Available</div>
                  </div>
                  <div class="text-center">
                    <div class="text-lg md:text-xl font-black text-hotline">100%</div>
                    <div class="text-[10px] md:text-xs text-black/60 font-bold">Coverage</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Right: Content Side -->
            <div class="p-5 md:p-6 lg:p-8 flex flex-col justify-center bg-neutral-offwhite">
              <div class="mb-2">
                <span class="inline-block px-2 md:px-3 py-0.5 md:py-1 rounded-full bg-primary/10 text-primary text-[10px] md:text-xs font-black tracking-widest border border-primary/20 uppercase">
                  Our Foundation
                </span>
              </div>

              <h2 class="text-base md:text-xl lg:text-2xl font-bold text-secondary mb-2 leading-tight break-words">
                A Robust Infrastructure for <span class="text-primary">Nationwide Impact</span>
              </h2>

              <p class="text-xs md:text-sm text-black/60 font-semibold mb-3 md:mb-4 leading-relaxed break-words">
                Our operations are built on sustainable pillars that ensure every caller receives expert attention, no matter where they are in Uganda.
              </p>

              <!-- Pillars List -->
              <div class="space-y-2 md:space-y-3">
                <div v-for="(pillar, pi) in pillars" :key="pi"
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

      <!-- 4. Services Auto-Scroll Carousel -->
      <section class="mb-6 md:mb-12">
        <div class="text-center mb-6 md:mb-10 px-4">
          <h2 class="text-lg md:text-2xl lg:text-3xl font-bold text-secondary mb-2 md:mb-3 lg:mb-4 break-words">
            {{ siteContent.getContent('services_section_title', 'Services We Offer') }}
          </h2>
          <p class="text-xs md:text-sm lg:text-base text-black/60 font-semibold max-w-2xl mx-auto leading-relaxed break-words">
            Comprehensive support systems protecting and empowering every voice in Uganda.
          </p>
        </div>

        <!-- Auto-Scrolling Container -->
        <div class="services-carousel-container overflow-hidden relative">
          <!-- Back Navigation Button -->
          <button
            @click="scrollPrevious"
            class="carousel-nav-btn carousel-nav-prev"
            aria-label="Go back to previous service"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="15 18 9 12 15 6"></polyline>
            </svg>
          </button>

          <div
            ref="servicesCarousel"
            class="services-carousel flex gap-4 md:gap-6"
            @mouseenter="pauseAutoScroll"
            @mouseleave="resumeAutoScroll"
          >
            <!-- Service Cards (duplicated for infinite loop) -->
            <div v-for="(service, idx) in [...services, ...services]" :key="idx"
                 class="flex-shrink-0 w-[280px] md:w-[320px] lg:w-[380px] relative overflow-hidden rounded-2xl md:rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-500 group h-[240px] md:h-[280px]">
              <img
                :src="getServiceImage(idx % services.length)"
                :alt="siteContent.getContent(service.cid_title, service.title)"
                class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/50 to-transparent"></div>

              <div class="relative z-10 h-full flex flex-col justify-end p-4 md:p-6 text-white overflow-hidden">
                <h3 class="text-sm md:text-lg lg:text-xl font-bold mb-1 md:mb-2 break-words">
                  {{ siteContent.getContent(service.cid_title, service.title) }}
                </h3>
                <p class="text-xs md:text-sm text-white/90 font-medium leading-relaxed line-clamp-3 break-words">
                  {{ siteContent.getContent(service.cid_text, service.text) }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { onMounted, onBeforeUnmount, ref } from 'vue'
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
  { title: 'Community Sensitization', cid_title: 'service_community_title', cid_text: 'service_community_text', text: 'Community sensitization activities to raise awareness about child protection and GBV prevention.' }
]

const pillars = [
  { title: '26 Local Languages', desc: 'Bridging the communication gap for every community in Uganda.' },
  { title: '24/7 Availability', desc: 'Support is always just a phone call away, day or night.' },
  { title: 'Sustainable Funding', desc: 'Partnering with MGLSD and UNICEF for long-term service stability.' }
]

const settingsStore = useSettingsStore()
const siteContent = useSiteContent('operations')
const servicesCarousel = ref(null)
let autoScrollInterval = null
const isPaused = ref(false)

const getServiceImage = (index) => {
  const images = [
    'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&h=600&fit=crop', // Service 1: Telephone Counseling
    'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=400&h=300&fit=crop', // Service 2: Walk-In Support
    'https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=400&h=600&fit=crop', // Service 3: Media Response
    'https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=400&h=300&fit=crop', // Service 4: Information & Guidance
    'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=400&h=300&fit=crop', // Service 5: Essential Service Referrals
    'https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=800&h=300&fit=crop'  // Service 6: Community Sensitization
  ]
  return images[index]
}

const startAutoScroll = () => {
  if (!servicesCarousel.value) return

  autoScrollInterval = setInterval(() => {
    if (isPaused.value) return // Don't scroll if paused

    const carousel = servicesCarousel.value
    const scrollAmount = 1 // Scroll 1px at a time for smooth movement
    carousel.scrollLeft += scrollAmount

    // Reset scroll when reaching halfway (where duplicates start)
    const maxScroll = carousel.scrollWidth / 2
    if (carousel.scrollLeft >= maxScroll) {
      carousel.scrollLeft = 0
    }
  }, 20) // Update every 20ms for smooth animation
}

const pauseAutoScroll = () => {
  isPaused.value = true
}

const resumeAutoScroll = () => {
  isPaused.value = false
}

const scrollPrevious = () => {
  if (!servicesCarousel.value) return
  const carousel = servicesCarousel.value
  const cardWidth = 280 + 16 // card width + gap (adjust for md/lg if needed)
  carousel.scrollLeft -= cardWidth
}

onMounted(async () => {
  await siteContent.fetchContent()
  await settingsStore.fetchGlobalSettings()

  // Start auto-scroll after a short delay
  setTimeout(() => {
    startAutoScroll()
  }, 500)
})

onBeforeUnmount(() => {
  if (autoScrollInterval) {
    clearInterval(autoScrollInterval)
  }
})
</script>

<style scoped>
/* Hero Banner */
.hero-banner {
  position: relative;
  background: linear-gradient(135deg, rgb(var(--color-secondary)) 0%, rgb(var(--color-primary-dark)) 100%);
  min-height: clamp(200px, 25vh, 300px);
  display: flex;
  align-items: center;
  overflow: hidden;
  margin-top: 0;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800"><defs><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1"/></pattern></defs><rect width="1200" height="800" fill="url(%23grid)"/></svg>');
  opacity: 0.5;
}

.hero-content-wrapper {
  position: relative;
  z-index: 2;
  padding: clamp(1.25rem, 3vh, 2.5rem) 0;
}

.hero-text {
  text-align: center;
  margin-bottom: clamp(0.75rem, 2vw, 1rem);
}

.hero-title {
  font-size: clamp(1rem, 2vw, 1.75rem);
  font-weight: 900;
  color: white;
  margin-bottom: 0.375rem;
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.text-accent-yellow {
  color: rgb(var(--color-accent-yellow));
}

.hero-subtitle {
  font-size: clamp(0.75rem, 0.9vw, 0.875rem);
  color: rgba(255, 255, 255, 0.85);
  font-weight: 400;
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.4;
  padding: 0 1rem;
}

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

/* Auto-Scrolling Services Carousel */
.services-carousel-container {
  width: 100%;
  position: relative;
}

.services-carousel {
  scroll-behavior: smooth;
  overflow-x: hidden;
  overflow-y: hidden;
  padding: 0.5rem 0;
}

/* Back Navigation Button */
.carousel-nav-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
  background: rgba(0, 104, 55, 0.9);
  color: white;
  border: none;
  border-radius: 50%;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.carousel-nav-btn:hover {
  background: rgba(0, 104, 55, 1);
  transform: translateY(-50%) scale(1.1);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
}

.carousel-nav-btn:active {
  transform: translateY(-50%) scale(0.95);
}

.carousel-nav-prev {
  left: 1rem;
}

/* Responsive sizing on mobile */
@media (max-width: 768px) {
  .carousel-nav-btn {
    width: 40px;
    height: 40px;
  }

  .carousel-nav-prev {
    left: 0.5rem;
  }
}

</style>
