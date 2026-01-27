<template>
  <div class="min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <h1 class="page-header-title">
          Our <span class="text-primary">Partners</span>
        </h1>
        <p class="page-header-subtitle">
          Working together with organizations committed to protecting children and vulnerable communities across Uganda.
        </p>
      </div>
    </header>

    <div class="section-padding !pt-0">
      <div class="container-custom">
        <!-- Partnership in a Flash (Flash Pattern) -->
        <section class="bg-secondary/5 p-8 md:p-12 rounded-[3.5rem] border-2 border-secondary/10 mb-16 shadow-sm">
          <h2 class="campaign-header text-xl text-secondary mb-8 flex items-center gap-3">
            <ShieldCheckIcon class="w-6 h-6 text-secondary" />
            Partnership at a Glance
          </h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
            <div class="space-y-4">
              <p class="text-black font-bold text-lg">Official Network</p>
              <p class="text-muted text-sm leading-relaxed">Backed by the **Ministry of Gender, Labour and Social
                Development**.</p>
            </div>
            <div class="space-y-4">
              <p class="text-black font-bold text-lg">National Reach</p>
              <p class="text-muted text-sm leading-relaxed">Connected to **over 50 NGOs** and international
                agencies.</p>
            </div>
            <div class="space-y-4">
              <p class="text-black font-bold text-lg">Expert Support</p>
              <p class="text-muted text-sm leading-relaxed">Collaborations with **UNICEF and local district
                leaders**.</p>
            </div>
          </div>
        </section>
      </div>

      <div class="container-custom section-rhythm">
        <!-- 2. Content Area -->
        <section aria-label="Partner Directory">
          <h2 class="campaign-header text-3xl text-secondary mb-12">Who We Work With</h2>
          <AppLoader v-if="loading" message="Loading partner organizations..." />

          <div v-else-if="partners.length"
            class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-8 md:gap-10">
            <div v-for="partner in partners" :key="partner.id"
              class="group relative bg-neutral-white rounded-[2.5rem] border-2 border-neutral-offwhite p-10 h-56 flex items-center justify-center transition-all duration-500 hover:shadow-2xl hover:border-primary card-base !p-0">
              <a v-if="partner.website_url" :href="partner.website_url" target="_blank"
                class="flex items-center justify-center h-full w-full p-10">
                <img :src="partner.logo" :alt="partner.name"
                  class="max-h-full max-w-full object-contain mx-auto transition-transform duration-700 group-hover:scale-110" />
                <div
                  class="absolute inset-x-0 bottom-6 opacity-0 group-hover:opacity-100 transition-all transform translate-y-2 group-hover:translate-y-0">
                  <span class="block text-[10px] text-center font-bold uppercase tracking-widest text-primary">
                    Visit official site →
                  </span>
                </div>
              </a>
              <div v-else class="flex items-center justify-center h-full w-full p-10">
                <img :src="partner.logo" :alt="partner.name"
                  class="max-h-full max-w-full object-contain mx-auto opacity-80" />
              </div>
            </div>
          </div>

          <div v-else
            class="text-center py-24 bg-neutral-offwhite/10 rounded-[4rem] border-2 border-dashed border-neutral-offwhite">
            <div
              class="w-20 h-20 bg-neutral-white border-2 border-neutral-offwhite rounded-2xl flex items-center justify-center mx-auto mb-6 text-neutral-offwhite opacity-50">
              <UserGroupIcon class="w-10 h-10" />
            </div>
            <p class="campaign-header text-black/40 text-xl font-bold">No partners listed yet.</p>
          </div>
        </section>

        <!-- 3. Partnership CTA -->
        <section class="mt-20">
          <div
            class="bg-primary/5 p-12 md:p-16 rounded-[4rem] border-2 border-primary/20 text-center max-w-4xl mx-auto">
            <h3 class="campaign-header text-3xl text-secondary mb-6">{{ siteContent.getContent('partners_cta_title', 'How We Work Together') }}</h3>
            <p class="text-xl font-bold text-muted mb-10 leading-relaxed">
              {{ siteContent.getContent('partners_cta_text', 'Interested in joining our mission to protect the children of Uganda? We are always looking for organizations that share our commitment.') }}
            </p>
            <div class="cta-group justify-center">
              <BaseCTA href="/contact" variant="primary">{{ siteContent.getContent('partners_cta_interest_button', 'Express Interest') }}</BaseCTA>
              <BaseCTA href="/about" variant="outline">{{ siteContent.getContent('partners_cta_learn_button', 'Learn About Our Impact') }}</BaseCTA>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { usePartnersStore } from '@/store/partners'
  import { useSiteContent } from '@/composables/useSiteContent'
  import AppLoader from '@/components/common/AppLoader.vue'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import { UserGroupIcon, ShieldCheckIcon } from '@heroicons/vue/24/outline'

  defineOptions({
    name: 'PartnersPage'
  })

  const partnersStore = usePartnersStore()
  const siteContent = useSiteContent('partners')
  const partners = ref([])
  const loading = ref(true)

  onMounted(async () => {
    // Fetch site content from CMS
    await siteContent.fetchContent()

    try {
      await partnersStore.fetchPartners()
      partners.value = partnersStore.partners
    } catch (error) {
      console.error('Failed to fetch partners:', error)
    } finally {
      loading.value = false
    }
  })
</script>
