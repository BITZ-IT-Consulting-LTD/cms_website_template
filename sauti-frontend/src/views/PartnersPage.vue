<template>
  <div class="bg-sauti-white min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <h1 class="page-header-title">
          Our <span class="text-sauti-blue">Partners</span>
        </h1>
        <p class="page-header-subtitle">
          Working together with organizations committed to protecting children and vulnerable communities across Uganda.
        </p>
      </div>
    </header>

    <div class="container-custom section-padding section-rhythm">
      <!-- 2. Content Area -->
      <section aria-label="Partner Directory">
        <AppLoader v-if="loading" message="Loading partner organizations..." />

        <div v-else-if="partners.length"
          class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-8 md:gap-10">
          <div v-for="partner in partners" :key="partner.id"
            class="group relative bg-sauti-white rounded-[2.5rem] border-2 border-sauti-neutral p-10 h-56 flex items-center justify-center transition-all duration-500 hover:shadow-2xl hover:border-sauti-blue card-base !p-0">
            <a v-if="partner.website_url" :href="partner.website_url" target="_blank"
              class="flex items-center justify-center h-full w-full p-10">
              <img :src="partner.logo" :alt="partner.name"
                class="max-h-full max-w-full object-contain mx-auto transition-transform duration-700 group-hover:scale-110" />
              <div
                class="absolute inset-x-0 bottom-6 opacity-0 group-hover:opacity-100 transition-all transform translate-y-2 group-hover:translate-y-0">
                <span class="block text-[10px] text-center font-bold uppercase tracking-widest text-sauti-blue">
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
          class="text-center py-24 bg-sauti-neutral/10 rounded-[4rem] border-2 border-dashed border-sauti-neutral">
          <div
            class="w-20 h-20 bg-sauti-white border-2 border-sauti-neutral rounded-2xl flex items-center justify-center mx-auto mb-6 text-sauti-neutral opacity-50">
            <UserGroupIcon class="w-10 h-10" />
          </div>
          <p class="campaign-header text-sauti-darkGreen/40 text-xl font-bold">No partners listed yet.</p>
        </div>
      </section>

      <!-- 3. Partnership CTA -->
      <section class="mt-20">
        <div
          class="bg-sauti-blue/5 p-12 md:p-16 rounded-[4rem] border-2 border-sauti-blue/20 text-center max-w-4xl mx-auto">
          <h3 class="campaign-header text-3xl text-sauti-darkGreen mb-6">Become a Partner</h3>
          <p class="text-xl font-bold text-sauti-darkGreen/60 mb-10 leading-relaxed">
            Interested in joining our mission to protect the children of Uganda? We are always looking for organizations
            that share our commitment.
          </p>
          <div class="cta-group justify-center">
            <BaseCTA href="/contact" variant="primary">Express Interest</BaseCTA>
            <BaseCTA href="/about" variant="outline">Learn About Our Impact</BaseCTA>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { usePartnersStore } from '@/store/partners'
  import AppLoader from '@/components/common/AppLoader.vue'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import { UserGroupIcon } from '@heroicons/vue/24/outline'

  defineOptions({
    name: 'PartnersPage'
  })

  const partnersStore = usePartnersStore()
  const partners = ref([])
  const loading = ref(true)

  onMounted(async () => {
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
