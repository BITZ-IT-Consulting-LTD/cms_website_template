<template>
  <div>
    <!-- Hero Section (three-column composition with central Uganda map) -->
    <section class="bg-white">
      <div class="container-custom min-h-[calc(100vh-80px)] flex items-center">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center w-full">
          <!-- Left headline -->
          <div class="lg:col-span-3 order-2 lg:order-1">
            <h1 class="text-5xl md:text-6xl font-extrabold tracking-tight text-gray-900">Justice begins,</h1>
            <div class="mt-8">
              <router-link to="/about" class="inline-flex items-center rounded-full bg-gray-200 px-6 py-3 text-gray-900 font-semibold hover:bg-gray-300 transition-colors">Read More</router-link>
            </div>
          </div>

          <!-- Center: Uganda map -->
          <div class="lg:col-span-6 order-1 lg:order-2">
            <div class="bg-transparent rounded-none shadow-none border-0 h-[620px] md:h-[820px] lg:h-[900px] flex items-center justify-center overflow-visible">
              <template v-if="usePng">
                <img
                  :src="pngUrl"
                  alt="Uganda map"
                  class="w-full h-full object-contain scale-125 md:scale-[1.9] lg:scale-[2.2] xl:scale-[2.6]"
                  @error="usePng = false"
                />
              </template>
              <template v-else>
                <iframe
                  title="Map of Uganda"
                  class="w-full h-full"
                  style="border:0"
                  loading="lazy"
                  referrerpolicy="no-referrer-when-downgrade"
                  src="https://www.openstreetmap.org/export/embed.html?bbox=29.5%2C-1.7%2C35.2%2C4.5&layer=mapnik&marker=1.3733%2C32.2903">
                </iframe>
              </template>
            </div>
          </div>

          <!-- Right headline -->
          <div class="lg:col-span-3 order-3">
            <h2 class="text-5xl md:text-6xl font-extrabold tracking-tight text-gray-900 lg:text-right">where Inequality stops.</h2>
          </div>
        </div>
      </div>
    </section>

    

    <!-- About, Vision, Mission Cards -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom">
        <h2 id="about" class="text-center mb-3">About, Vision, Mission</h2>
        <p class="text-center text-gray-600 mb-10 max-w-2xl mx-auto">Our unwavering commitment to child protection.</p>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="avm-card">
            <div class="avm-icon bg-blue-50 text-blue-600">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11c0 1.657-1.343 3-3 3S6 12.657 6 11s1.343-3 3-3 3 1.343 3 3z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 17.804A11.955 11.955 0 0112 15c2.49 0 4.797.764 6.879 2.064"/>
              </svg>
            </div>
            <h3 class="avm-title">Our Commitment</h3>
            <p class="avm-text">We are dedicated to safeguarding children's rights and well-being, offering a secure and confidential platform for reporting abuse.</p>
          </div>
          <div class="avm-card" id="vision">
            <div class="avm-icon bg-cyan-50 text-cyan-600">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.522 5 12 5s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S3.732 16.057 2.458 12z"/>
              </svg>
            </div>
            <h3 class="avm-title">Our Vision</h3>
            <p class="avm-text">To create a society where every child is safe, protected, and empowered to reach their full potential.</p>
          </div>
          <div class="avm-card" id="mission">
            <div class="avm-icon bg-orange-50 text-orange-600">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v12"/>
              </svg>
            </div>
            <h3 class="avm-title">Our Mission</h3>
            <p class="avm-text">To provide immediate support, resources, and advocacy for children experiencing abuse, ensuring their voices are heard.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Journey Timeline -->
    <section class="section-padding">
      <div class="container-custom">
        <h2 class="text-center mb-3">Our Journey</h2>
        <p class="text-center text-gray-600 mb-12">Key milestones in our history of child advocacy.</p>
        <div class="relative max-w-4xl mx-auto">
          <div class="timeline-line"></div>
          <div class="timeline-item left">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm text-primary-600 font-bold">2010</h4>
              <h3 class="text-lg font-bold mb-1">Launch of Sauti Helpline</h3>
              <p class="text-gray-600">Established as a national child helpline, providing a critical first point of contact.</p>
            </div>
          </div>
          <div class="timeline-item right">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm text-primary-600 font-bold">2015</h4>
              <h3 class="text-lg font-bold mb-1">Expansion of Services</h3>
              <p class="text-gray-600">Introduced counseling and legal support to offer more comprehensive assistance.</p>
            </div>
          </div>
          <div class="timeline-item left">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm text-primary-600 font-bold">2020</h4>
              <h3 class="text-lg font-bold mb-1">Reaching 1 Million Children</h3>
              <p class="text-gray-600">A landmark achievement, having provided assistance to over a million children across Uganda.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Latest News (displaying videos) -->
    <section class="section-padding">
      <div class="container-custom">
        <div class="flex justify-between items-center mb-8">
          <h2>Latest News & Updates</h2>
          <router-link to="/videos" class="text-primary-600 hover:text-primary-700 font-medium">View all →</router-link>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <article v-for="video in latestVideos" :key="video.id" class="group">
            <div class="relative bg-gray-200 rounded-xl overflow-hidden aspect-video">
              <img :src="video.thumbnail" :alt="video.title" class="w-full h-full object-cover" loading="lazy" @error="useThumbPlaceholder($event)" />
              <span class="absolute bottom-2 right-2 text-xs font-bold bg-black/80 text-white px-1.5 py-0.5 rounded">{{ video.duration }}</span>
            </div>
            <div class="mt-3 flex gap-3">
              <img :src="video.channelAvatar" :alt="video.channel" class="h-9 w-9 rounded-full object-cover" loading="lazy" @error="useAvatarPlaceholder($event)" />
              <div class="min-w-0">
                <h3 class="text-sm font-semibold text-gray-900 leading-5 line-clamp-2 group-hover:text-primary-600">{{ video.title }}</h3>
                <p class="text-xs text-gray-600 mt-1">{{ video.channel }}</p>
                <p class="text-xs text-gray-500">{{ video.views }} • {{ video.published }}</p>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- Bottom CTA aligned with new style -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom text-center">
        <h2 class="mb-4">Need Help Right Now?</h2>
        <p class="text-lg text-gray-600 mb-6 max-w-2xl mx-auto">Don't wait. Reach out to us through any of our channels. All services are free and confidential.</p>
        <div class="flex flex-wrap justify-center gap-3">
          <a href="tel:116" class="pill pill-light">Call 116</a>
          <router-link to="/report" class="pill pill-primary">Report a Case</router-link>
          <router-link to="/contact" class="pill pill-outline">Contact Us</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { usePartnersStore } from '@/store/partners'
import GetHelpButton from '@/components/common/GetHelpButton.vue'
import Loader from '@/components/common/Loader.vue'

const partnersStore = usePartnersStore()

const latestVideos = ref([
  {
    id: 1,
    title: 'Understanding Child Rights',
    channel: 'Sauti Uganda',
    channelAvatar: 'https://i.pravatar.cc/48?img=12',
    views: '12K views',
    published: '2 weeks ago',
    duration: '12:45',
    category: 'Education',
    thumbnail: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=1200&auto=format&fit=crop'
  },
  {
    id: 2,
    title: 'Safety Tips for Children',
    channel: 'Sauti Uganda',
    channelAvatar: 'https://i.pravatar.cc/48?img=32',
    views: '15K views',
    published: '1 month ago',
    duration: '8:22',
    category: 'Safety',
    thumbnail: 'https://images.unsplash.com/photo-1512428559087-560fa5ceab42?q=80&w=1200&auto=format&fit=crop'
  },
  {
    id: 3,
    title: 'How to Report Abuse',
    channel: 'Sauti Uganda',
    channelAvatar: 'https://i.pravatar.cc/48?img=15',
    views: '8K views',
    published: '1 month ago',
    duration: '15:03',
    category: 'Support',
    thumbnail: 'https://images.unsplash.com/photo-1499355942262-97b58a6195b4?q=80&w=1200&auto=format&fit=crop'
  }
])

const partners = ref([])
const loadingPartners = ref(false)
const usePng = ref(true)
const pngUrl = new URL('@/assets/uganda maping .png', import.meta.url).href

onMounted(async () => {
  // Fetch partners
  loadingPartners.value = true
  try {
    await partnersStore.fetchPartners()
    partners.value = partnersStore.partners
  } catch (error) {
    console.error('Failed to load partners:', error)
  } finally {
    loadingPartners.value = false
  }
  // Probe if PNG exists; if not, fall back to OSM iframe
  try {
    const res = await fetch(pngUrl, { method: 'HEAD' })
    if (!res.ok) {
      usePng.value = false
    }
  } catch (e) {
    usePng.value = false
  }
})

function setPlaceholder(event) {
  const img = event.target
  const ph = img.getAttribute('data-ph') || 'https://picsum.photos/800/600'
  if (img.src !== ph) {
    img.src = ph
  }
}

function useThumbPlaceholder(e) {
  e.target.src = 'https://picsum.photos/640/360?blur=2'
}

function useAvatarPlaceholder(e) {
  e.target.src = 'https://i.pravatar.cc/48'
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.aspect-video {
  position: relative;
  width: 100%;
  padding-bottom: 56.25%; /* 16:9 */
}
.aspect-video > img,
.aspect-video > video,
.aspect-video > div {
  position: absolute;
  inset: 0;
}
</style>
