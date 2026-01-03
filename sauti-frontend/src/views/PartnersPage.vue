<template>
  <div class="bg-sauti-neutral py-16 md:py-24 min-h-screen">
    <div class="container-custom">
      <div class="text-center mb-16">
        <h1 class="text-4xl md:text-5xl lg:text-7xl font-black text-sauti-darkGreen mb-4 tracking-tight">Our <span
            class="text-sauti-blue">Partners</span></h1>
        <p class="text-xl text-sauti-darkGreen/70 font-medium max-w-2xl mx-auto">
          Working together with organizations committed to protecting children and vulnerable communities across Uganda.
        </p>
      </div>

      <AppLoader v-if="loading" />

      <div v-else-if="partners.length"
        class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6 md:gap-8">
        <div v-for="partner in partners" :key="partner.id"
          class="group relative bg-sauti-white rounded-[2rem] border-2 border-sauti-neutral p-8 h-48 flex items-center justify-center transition-all duration-300 hover:shadow-xl hover:shadow-sauti-blue/10 hover:border-sauti-blue/30">
          <a v-if="partner.website_url" :href="partner.website_url" target="_blank" class="block h-full w-full">
            <img :src="partner.logo" :alt="partner.name"
              class="max-h-full max-w-full object-contain mx-auto transition-transform duration-500 group-hover:scale-110" />
            <div class="absolute inset-x-0 -bottom-2 opacity-0 group-hover:opacity-100 transition-opacity">
              <span class="block text-[10px] text-center font-black uppercase tracking-widest text-sauti-blue">Visit
                Website</span>
            </div>
          </a>
          <img v-else :src="partner.logo" :alt="partner.name" class="max-h-full max-w-full object-contain mx-auto" />
        </div>
      </div>

      <div v-else class="text-center py-24 bg-sauti-white rounded-[3.5rem] border-2 border-dashed border-sauti-neutral">
        <p class="text-sauti-darkGreen/40 font-black text-xl">No partners listed yet.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { usePartnersStore } from '@/store/partners'
  import AppLoader from '@/components/common/AppLoader.vue'

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
    } finally {
      loading.value = false
    }
  })
</script>
