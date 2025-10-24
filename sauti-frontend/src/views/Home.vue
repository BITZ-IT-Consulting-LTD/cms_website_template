<template>
  <div>
    <!-- Hero (Airbnb-inspired: big headline, soft background, quick actions) -->
    <section class="relative overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-b from-white via-white to-gray-50"></div>
      <div class="container-custom relative py-14 md:py-20">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          <div class="lg:col-span-7">
            <h1 class="text-5xl md:text-6xl font-extrabold tracking-tight text-gray-900">Every child deserves a safe voice.</h1>
            <p class="mt-4 text-lg md:text-xl text-gray-600 max-w-2xl">Sauti 116 is free, confidential and available 24/7 across all telecoms. Report abuse, seek guidance, or get urgent help in your language.</p>
            <!-- Quick Action Bar -->
            <div class="mt-6 bg-white border border-gray-100 rounded-full shadow-sm p-2 flex flex-wrap items-center gap-2 md:gap-3">
              <a href="tel:116" class="pill pill-primary" aria-label="Call 116 now">Call 116</a>
              <router-link to="/report" class="pill pill-light" aria-label="Report a case">Report a Case</router-link>
              <a href="https://wa.me/256123456789" target="_blank" rel="noopener" class="pill pill-outline" aria-label="Contact via WhatsApp">WhatsApp</a>
              <a href="https://ureport.in" target="_blank" rel="noopener" class="pill pill-outline" aria-label="U-Report 8500">U-Report 8500</a>
            </div>
            <div class="mt-4 flex flex-wrap gap-3 text-sm text-gray-600">
              <span class="badge-blue">24/7</span>
              <span class="badge-orange">All Telecoms</span>
              <span class="badge-teal">EN • LG • SW</span>
              <span class="badge-purple">Confidential</span>
            </div>
          </div>
          <div class="lg:col-span-5">
            <div class="card p-0 overflow-hidden">
              <img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=1600&auto=format&fit=crop" alt="Protecting children" class="w-full h-72 md:h-96 object-cover" />
            </div>
          </div>
        </div>
      </div>
    </section>

    

    <!-- Quick tiles (Airbnb-style categories) -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
          <router-link to="/report" class="avm-card hover:shadow-md transition-shadow">
            <h3 class="avm-title">Report a case</h3>
            <p class="avm-text">Confidential, fast, and supportive.</p>
          </router-link>
          <router-link to="/resources" class="avm-card hover:shadow-md transition-shadow">
            <h3 class="avm-title">Resources</h3>
            <p class="avm-text">Guides, policies and toolkits.</p>
          </router-link>
          <router-link to="/faqs" class="avm-card hover:shadow-md transition-shadow">
            <h3 class="avm-title">FAQs</h3>
            <p class="avm-text">Answers to common questions.</p>
          </router-link>
          <router-link to="/partners" class="avm-card hover:shadow-md transition-shadow">
            <h3 class="avm-title">Partners</h3>
            <p class="avm-text">MGLSD, UNICEF, UCRNN, ITU.</p>
          </router-link>
        </div>
      </div>
    </section>

    <!-- Journey Timeline -->
    <section class="section-padding">
      <div class="container-custom">
        <h2 class="text-center mb-3">Our Journey</h2>
        <p class="text-center text-gray-600 mb-12">Key milestones in our history of child advocacy, including international recommendations and national designation of 116.</p>
        <div class="relative max-w-4xl mx-auto">
          <div class="timeline-line"></div>
          <div class="timeline-item left">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm text-primary-600 font-bold">2005</h4>
              <h3 class="text-lg font-bold mb-1">Launch of Child Helpline Initiative</h3>
              <p class="text-gray-600">Inception of the national child protection helpline in partnership with NGOs and international agencies.</p>
            </div>
          </div>
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
          <div class="timeline-item right">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm text-primary-600 font-bold">2016</h4>
              <h3 class="text-lg font-bold mb-1">Legal & Regulatory Backing</h3>
              <p class="text-gray-600">116 designated by UCC; strengthened by national child protection policies and frameworks.</p>
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
        <p class="text-center text-gray-500 text-sm mt-6">Aligned with ITU recommendation for 116 child helplines; operated under MGLSD in collaboration with NGOs and UN partners.</p>
      </div>
    </section>

    <!-- Featured Content (videos) -->
    <section class="section-padding">
      <div class="container-custom">
        <div class="flex justify-between items-center mb-8">
          <h2>Featured Content</h2>
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

    <!-- Trust strip -->
    <section class="py-8 bg-white border-y border-gray-100">
      <div class="container-custom">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-center text-gray-600">
          <div class="card p-4">MGLSD</div>
          <div class="card p-4">UNICEF</div>
          <div class="card p-4">UCRNN</div>
          <div class="card p-4">ITU 116</div>
        </div>
      </div>
    </section>

    <!-- Bottom CTA aligned with new style -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom text-center">
        <h2 class="mb-4">Need Help Right Now?</h2>
        <p class="text-lg text-gray-600 mb-6 max-w-2xl mx-auto">Accessible 24/7 across all telecom networks. Support in multiple local languages. All services are free and confidential.</p>
        <div class="flex flex-wrap justify-center gap-3">
          <a href="tel:116" class="pill pill-light">Call 116</a>
          <router-link to="/report" class="pill pill-primary">Report a Case</router-link>
          <router-link to="/contact" class="pill pill-outline">Contact Us</router-link>
        </div>
        <div class="mt-6 grid grid-cols-1 sm:grid-cols-3 gap-3 text-sm text-gray-600">
          <div class="avm-card"><strong>Channels:</strong> 116 • WhatsApp • U-Report SMS • SafePal App • Email</div>
          <div class="avm-card"><strong>Languages:</strong> English • Luganda • Swahili • Local languages</div>
          <div class="avm-card"><strong>Availability:</strong> 24/7 • Nationwide • All telecoms</div>
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
const pngUrl = ref('')

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
  // Try multiple filename variants to match the asset you placed
  const candidates = [
    new URL('@/assets/uganda mapping.png', import.meta.url).href,
    new URL('@/assets/uganda mapping .png', import.meta.url).href,
    new URL('@/assets/uganda maping.png', import.meta.url).href,
    new URL('@/assets/uganda maping .png', import.meta.url).href,
  ]
  usePng.value = false
  for (const candidate of candidates) {
    try {
      const res = await fetch(candidate, { method: 'HEAD' })
      if (res.ok) {
        pngUrl.value = candidate
        usePng.value = true
        break
      }
    } catch (_) { /* ignore and try next */ }
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
