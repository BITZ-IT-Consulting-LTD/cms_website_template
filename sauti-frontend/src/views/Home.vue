<template>
  <div>
    <!-- Hero Section -->
    <section class="bg-gradient-to-br from-primary-600 to-primary-800 text-white section-padding">
      <div class="container-custom">
        <div class="text-center max-w-4xl mx-auto">
          <h1 class="text-4xl md:text-6xl font-bold mb-6 fade-in">
            We're Here to Help You
          </h1>
          <p class="text-xl md:text-2xl mb-8 text-primary-100">
            Support for children, GBV survivors, and migrant workers across Uganda
          </p>
          
          <!-- Hotline -->
          <div class="bg-white bg-opacity-10 backdrop-blur rounded-2xl p-8 mb-8">
            <p class="text-lg mb-4">Emergency Hotline</p>
            <a href="tel:116" class="text-6xl md:text-7xl font-bold hover:text-secondary-300 transition-colors">
              116
            </a>
            <p class="text-primary-200 mt-4">Toll-free · Available 24/7</p>
          </div>
          
          <GetHelpButton class="inline-block" />
        </div>
      </div>
    </section>

    <!-- Quick Access Services -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom">
        <h2 class="text-center mb-12">How Can We Help You?</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <router-link
            v-for="service in services"
            :key="service.title"
            :to="service.link"
            class="service-card"
          >
            <div :class="service.iconBg" class="p-4 rounded-lg mb-4">
              <svg class="w-8 h-8" :class="service.iconColor" fill="currentColor" viewBox="0 0 20 20">
                <path :d="service.icon" />
              </svg>
            </div>
            <h3 class="text-xl font-bold text-gray-900 mb-2">{{ service.title }}</h3>
            <p class="text-gray-600 mb-4">{{ service.description }}</p>
            <span :class="`text-${service.color}-600 font-medium`">
              Learn more →
            </span>
          </router-link>
        </div>
      </div>
    </section>

    <!-- Latest News -->
    <section class="section-padding">
      <div class="container-custom">
        <div class="flex justify-between items-center mb-8">
          <h2>Latest News & Updates</h2>
          <router-link to="/blog" class="text-primary-600 hover:text-primary-700 font-medium">
            View all →
          </router-link>
        </div>
        
        <Loader v-if="loadingPosts" message="Loading news..." />
        
        <div v-else-if="latestPosts.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <BlogCard v-for="post in latestPosts" :key="post.id" :post="post" />
        </div>
        
        <p v-else class="text-center text-gray-500 py-8">No news available at the moment.</p>
      </div>
    </section>

    <!-- Partners -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom text-center">
        <h2 class="mb-8">Our Partners</h2>
        <p class="text-gray-600 mb-12 max-w-2xl mx-auto">
          Working together with organizations committed to protecting children and vulnerable communities
        </p>
        
        <Loader v-if="loadingPartners" />
        
        <div v-else-if="partners.length" class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-8 items-center">
          <div v-for="partner in partners" :key="partner.id" class="grayscale hover:grayscale-0 transition-all">
            <img
              :src="partner.logo"
              :alt="partner.name"
              class="h-16 w-auto mx-auto object-contain"
              loading="lazy"
            />
          </div>
        </div>
      </div>
    </section>

    <!-- Call to Action -->
    <section class="section-padding bg-primary-600 text-white">
      <div class="container-custom text-center">
        <h2 class="mb-6">Need Help Right Now?</h2>
        <p class="text-xl mb-8 text-primary-100 max-w-2xl mx-auto">
          Don't wait. Reach out to us through any of our channels. All services are free and confidential.
        </p>
        <div class="flex flex-wrap justify-center gap-4">
          <a href="tel:116" class="btn bg-white text-primary-600 hover:bg-gray-100">
            Call 116
          </a>
          <router-link to="/report" class="btn bg-secondary-500 text-white hover:bg-secondary-600">
            Report a Case
          </router-link>
          <router-link to="/contact" class="btn-outline border-white text-white hover:bg-white hover:text-primary-600">
            Contact Us
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useBlogStore } from '@/store/blog'
import { usePartnersStore } from '@/store/partners'
import BlogCard from '@/components/blog/BlogCard.vue'
import GetHelpButton from '@/components/common/GetHelpButton.vue'
import Loader from '@/components/common/Loader.vue'

const blogStore = useBlogStore()
const partnersStore = usePartnersStore()

const latestPosts = ref([])
const partners = ref([])
const loadingPosts = ref(false)
const loadingPartners = ref(false)

const services = [
  {
    title: 'Child Protection',
    description: 'Help for children facing abuse, neglect, or exploitation',
    link: '/faqs?category=child-protection',
    icon: 'M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z',
    iconBg: 'bg-blue-100',
    iconColor: 'text-blue-600',
    color: 'blue',
  },
  {
    title: 'GBV Support',
    description: 'Confidential support for survivors of gender-based violence',
    link: '/faqs?category=gbv',
    icon: 'M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z',
    iconBg: 'bg-purple-100',
    iconColor: 'text-purple-600',
    color: 'purple',
  },
  {
    title: 'Migrant Workers',
    description: 'Protection and support for migrant workers',
    link: '/faqs?category=migrants',
    icon: 'M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z',
    iconBg: 'bg-teal-100',
    iconColor: 'text-teal-600',
    color: 'teal',
  },
  {
    title: 'PSEA',
    description: 'Report sexual exploitation by aid workers',
    link: '/faqs?category=psea',
    icon: 'M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z',
    iconBg: 'bg-orange-100',
    iconColor: 'text-orange-600',
    color: 'orange',
  },
]

onMounted(async () => {
  // Fetch latest posts
  loadingPosts.value = true
  try {
    await blogStore.fetchPosts({ page_size: 3 })
    latestPosts.value = blogStore.posts.slice(0, 3)
  } catch (error) {
    console.error('Failed to load posts:', error)
  } finally {
    loadingPosts.value = false
  }

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
</script>
