<template>
  <div class="section-padding">
    <div class="container-custom">
      <h1 class="text-center mb-4">Our Partners</h1>
      <p class="text-center text-gray-600 mb-12 max-w-2xl mx-auto">
        Working together with organizations committed to protecting children and vulnerable communities
      </p>
      
      <Loader v-if="loading" />
      
      <div v-else-if="partners.length" class="overflow-x-auto whitespace-nowrap py-4">
        <div class="inline-flex space-x-8">
          <div v-for="partner in partners" :key="partner.id" class="flex-shrink-0 w-48 h-24 flex items-center justify-center bg-white rounded-lg shadow-sm border border-gray-200 p-4">
            <a v-if="partner.website_url" :href="partner.website_url" target="_blank" class="block h-full w-full">
              <img :src="partner.logo" :alt="partner.name" class="max-h-full max-w-full object-contain mx-auto" />
            </a>
            <img v-else :src="partner.logo" :alt="partner.name" class="max-h-full max-w-full object-contain mx-auto" />
          </div>
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
