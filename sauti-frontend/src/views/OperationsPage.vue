<template>
  <div class="min-h-screen">
    <!-- 1. Page Header (Standard Alignment) -->
    <header class="page-header !pb-0">
      <div class="container-custom">
        <div class="mb-4">
          <span class="inline-block px-3 py-1 rounded-full bg-primary/10 text-primary text-xs font-black tracking-widest border border-primary/20 uppercase">
            {{ siteContent.getContent('operations_hero_badge', 'Operations') }}
          </span>
        </div>
        <h1 class="page-header-title">
          {{ siteContent.getContent('operations_page_title', 'How We') }}
          <span class="text-primary">{{ siteContent.getContent('operations_page_title_highlight', 'Operate') }}</span>
        </h1>
        <p class="page-header-subtitle max-w-2xl">
          {{ siteContent.getContent('operations_page_subtitle', 'Sauti is a Swahili word that means voice. Discover how we serve every citizen across Uganda 24/7.') }}
        </p>
      </div>
    </header>

    <div class="container-custom section-padding !pt-12">
      <!-- 2. The Process Flow (Beautified & Aligned) -->
      <section class="mb-24">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-black text-secondary tracking-tight">
            The Journey of a <span class="text-primary">Voice</span>
          </h2>
          <div class="w-20 h-1 bg-primary mx-auto mt-4 rounded-full"></div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
          <!-- Item 1 -->
          <div class="card-base bg-white border border-gray-100 hover:border-primary/20 transition-all text-center group">
            <div class="w-14 h-14 bg-transparent rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform">
              <Phone class="w-7 h-7 text-primary" />
            </div>
            <h4 class="text-lg font-black text-secondary mb-2">1. Access</h4>
            <p class="text-sm font-bold text-black/40">Toll-free 116 available 24/7 from any network.</p>
          </div>

          <!-- Item 2 -->
          <div class="card-base bg-white border border-gray-100 hover:border-secondary-light/20 transition-all text-center group">
            <div class="w-14 h-14 bg-transparent rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform">
              <Headphones class="w-7 h-7 text-secondary-light" />
            </div>
            <h4 class="text-lg font-black text-secondary mb-2">2. Response</h4>
            <p class="text-sm font-bold text-black/40">Counselors responding in 26 local languages.</p>
          </div>

          <!-- Item 3 -->
          <div class="card-base bg-white border border-gray-100 hover:border-hotline/20 transition-all text-center group">
            <div class="w-14 h-14 bg-transparent rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform">
              <Building2 class="w-7 h-7 text-hotline" />
            </div>
            <h4 class="text-lg font-black text-secondary mb-2">3. Management</h4>
            <p class="text-sm font-bold text-black/40">Case follow-up and specialized support.</p>
          </div>

          <!-- Item 4 -->
          <div class="card-base bg-white border border-gray-100 hover:border-secondary/20 transition-all text-center group">
            <div class="w-14 h-14 bg-transparent rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform">
              <ShieldCheck class="w-7 h-7 text-secondary" />
            </div>
            <h4 class="text-lg font-black text-secondary mb-2">4. Protection</h4>
            <p class="text-sm font-bold text-black/40">Resolution and community reintegration.</p>
          </div>
        </div>
      </section>

      <!-- 3. Infrastructure Section -->
      <section class="mb-24">
        <div class="bg-neutral-offwhite rounded-[3.5rem] p-10 md:p-16 border border-gray-100">
          <div class="max-w-5xl mx-auto text-center">
            <h2 class="text-4xl font-black text-secondary mb-6 leading-tight">
              A Robust Infrastructure for <br/><span class="text-primary">Nationwide Impact</span>
            </h2>
            <p class="text-lg font-bold text-black/50 mb-12 max-w-2xl mx-auto">
              Our operations are built on sustainable pillars that ensure every caller receives expert attention.
            </p>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
              <div v-for="(pillar, pi) in pillars" :key="pi" 
                   class="flex flex-col items-center p-8 bg-white rounded-[2.5rem] shadow-sm border border-gray-50 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                <div class="w-16 h-16 rounded-2xl flex items-center justify-center shrink-0 bg-transparent mb-6 group-hover:scale-110 transition-transform">
                  <component :is="pillar.icon" class="w-10 h-10" :style="{ color: pillar.bgColor }" />
                </div>
                <h5 class="text-xl font-black text-secondary leading-tight mb-3">{{ pillar.title }}</h5>
                <p class="text-sm font-bold text-black/40 leading-relaxed">{{ pillar.desc }}</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 4. Services Grid (Styled as Modern Cards) -->
      <section class="mb-16">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-black text-secondary mb-4">
            {{ siteContent.getContent('services_section_title', 'Services We Offer') }}
          </h2>
          <p class="text-black/50 font-bold max-w-2xl mx-auto">
            Comprehensive support systems protecting and empowering every voice in Uganda.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
           <!-- Featured Service: Takes more space for its longer content -->
           <div v-for="(service, idx) in services" :key="idx" 
                class="card-base bg-white border border-gray-100 p-8 hover:shadow-2xl transition-all group flex flex-col h-full"
                :class="{
                  'md:col-span-2 md:row-span-2': idx === 0,
                  'md:col-span-1 md:row-span-1': idx === 1 || idx === 3 || idx === 4,
                  'md:col-span-1 md:row-span-2': idx === 2,
                  'md:col-span-2 md:row-span-1': idx === 5
                }">
              <div class="w-12 h-12 rounded-xl flex items-center justify-center mb-6 bg-transparent group-hover:scale-110 transition-transform">
                <component :is="service.icon" class="w-8 h-8" :style="{ color: service.color }" />
              </div>
              <h3 class="font-black text-secondary mb-3 group-hover:text-primary transition-colors"
                  :class="idx === 0 || idx === 2 ? 'text-2xl' : 'text-lg'">
                {{ siteContent.getContent(service.cid_title, service.title) }}
              </h3>
              <p class="font-bold text-black/40 leading-relaxed"
                 :class="idx === 0 || idx === 2 ? 'text-base' : 'text-sm'">
                {{ siteContent.getContent(service.cid_text, service.text) }}
              </p>
           </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useSettingsStore } from '@/store/settings'
import { useSiteContent } from '@/composables/useSiteContent'
import { 
  Phone, 
  Clock, 
  Globe, 
  Building2, 
  Wallet, 
  Headphones, 
  UserCircle, 
  Radio, 
  BookOpen, 
  ArrowRightCircle, 
  Users,
  ShieldCheck,
  MessageCircle
} from 'lucide-vue-next'

defineOptions({
  name: 'OperationsPage'
})

const services = [
  { title: 'Telephone Counseling', icon: Headphones, color: '#2B4C7E', cid_title: 'service_counseling_title', cid_text: 'service_counseling_text', text: 'Professional counseling services available 24/7 through our toll-free helpline 116.' },
  { title: 'Walk-In Support', icon: UserCircle, color: '#8ECAE6', cid_title: 'service_walkin_title', cid_text: 'service_walkin_text', text: 'Handle walk-in clients at our offices for face-to-face consultation and support.' },
  { title: 'Media Response', icon: Radio, color: '#FB8500', cid_title: 'service_media_title', cid_text: 'service_media_text', text: 'Respond to cases of violence against children and gender-based violence reported through media and U-report.' },
  { title: 'Information & Guidance', icon: BookOpen, color: '#023047', cid_title: 'service_guidance_title', cid_text: 'service_guidance_text', text: 'Provision of information and guidance on child care and protection matters.' },
  { title: 'Essential Service Referrals', icon: ArrowRightCircle, color: '#2B4C7E', cid_title: 'service_referral_title', cid_text: 'service_referral_text', text: 'Referral to essential services including healthcare, legal aid, and social support.' },
  { title: 'Community Sensitization', icon: Users, color: '#8ECAE6', cid_title: 'service_community_title', cid_text: 'service_community_text', text: 'Community sensitization activities to raise awareness about child protection and GBV prevention.' }
]

const pillars = [
  { title: '26 Local Languages', desc: 'Bridging the communication gap for every community in Uganda.', icon: Globe, bgColor: '#2B4C7E' },
  { title: '24/7 Availability', desc: 'Support is always just a phone call away, day or night.', icon: Clock, bgColor: '#8ECAE6' },
  { title: 'Sustainable Funding', desc: 'Partnering with MGLSD and UNICEF for long-term service stability.', icon: Wallet, bgColor: '#FB8500' }
]

const settingsStore = useSettingsStore()
const siteContent = useSiteContent('operations')

onMounted(async () => {
  await siteContent.fetchContent()
  await settingsStore.fetchGlobalSettings()
})
</script>

<style scoped>
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
</style>
