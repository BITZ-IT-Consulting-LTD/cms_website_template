<template>
  <div>
    <!-- Hero Section (clean landing like reference) -->
    <section class="bg-white">
      <div class="container-custom min-h-[calc(100vh-80px)] flex items-center">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 items-center w-full">
          <!-- Left copy -->
          <div>
            <h1 class="text-5xl md:text-7xl font-extrabold leading-tight text-gray-900 mb-6">
              Your Lifeline & Support
            </h1>
            <p class="text-lg text-gray-600 mb-8 max-w-xl">A safe and confidential space for every child in Uganda. We are here to listen and help.</p>
            <div class="flex items-center gap-4">
              <router-link to="/report" class="pill bg-secondary-500 text-white hover:bg-secondary-600">Report a Case</router-link>
              <router-link to="/faqs" class="pill pill-outline">Learn More</router-link>
            </div>
          </div>

          <!-- Right visual: Bento grid 3 photos -->
          <div class="grid grid-cols-2 lg:grid-rows-2 gap-4 lg:h-[460px]">
            <div class="col-span-2 lg:col-span-1 lg:row-span-2 bg-white rounded-[2rem] shadow-sm border border-gray-100 overflow-hidden">
              <img
                src="https://images.unsplash.com/photo-1519681393784-d120267933ba?q=80&w=1200&auto=format&fit=crop"
                alt="Community"
                class="w-full h-[220px] md:h-[300px] lg:h-full object-cover"
                @error="setPlaceholder"
                data-ph="https://picsum.photos/1200/800?blur=2"
              />
            </div>
            <div class="bg-white rounded-[1.75rem] shadow-sm border border-gray-100 overflow-hidden">
              <img
                src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=900&auto=format&fit=crop"
                alt="Supporter"
                class="w-full h-[200px] md:h-[220px] lg:h-full object-cover"
                @error="setPlaceholder"
                data-ph="https://picsum.photos/900/600?grayscale"
              />
            </div>
            <div class="bg-white rounded-[1.75rem] shadow-sm border border-gray-100 overflow-hidden">
              <img
                src="https://images.unsplash.com/photo-1520975922284-8b456906c813?q=80&w=900&auto=format&fit=crop"
                alt="Team"
                class="w-full h-[200px] md:h-[220px] lg:h-full object-cover"
                @error="setPlaceholder"
                data-ph="https://picsum.photos/900/600"
              />
            </div>
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
