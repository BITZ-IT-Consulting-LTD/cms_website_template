<template>
  <div class="section-padding">
    <div class="container-custom">
      <h1 class="text-center mb-4">Our Partners</h1>
      <p class="text-center text-gray-600 mb-12 max-w-2xl mx-auto">
        Working together with organizations committed to protecting children and vulnerable communities
      </p>
      
      <Loader v-if="loading" />
      
      <div v-else-if="partners.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div v-for="partner in partners" :key="partner.id" class="card card-body text-center">
          <img :src="partner.logo" :alt="partner.name" class="h-24 w-auto mx-auto mb-4 object-contain" />
          <h3 class="font-bold text-gray-900 mb-2">{{ partner.name }}</h3>
          <p class="text-sm text-gray-600 mb-4">{{ partner.description }}</p>
          <a v-if="partner.website_url" :href="partner.website_url" target="_blank" class="text-primary-600 hover:text-primary-700 text-sm font-medium">
            Visit Website →
          </a>
        </div>
      </div>

      <p v-else class="text-center text-gray-600">No partners listed yet.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { usePartnersStore } from '@/store/partners'
import Loader from '@/components/common/Loader.vue'

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
