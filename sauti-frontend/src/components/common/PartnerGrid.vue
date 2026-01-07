<template>
  <div v-if="partners && partners.length > 0"
    class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-8 lg:gap-12 items-start">

    <div v-for="partner in partners" :key="partner.id" class="group flex flex-col items-center text-center space-y-4">

      <!-- Partner Logo with Link (Subdued Hierarchy) -->
      <a v-if="partner.logo && partner.website_url" :href="partner.website_url" target="_blank"
        rel="noopener noreferrer"
        class="block w-full h-16 p-2 bg-transparent opacity-40 hover:opacity-100 grayscale hover:grayscale-0 transition-all duration-500">
        <img :src="partner.logo" :alt="partner.name" class="w-full h-full object-contain" />
      </a>

      <!-- Partner Logo Only (No Link) -->
      <div v-else-if="partner.logo" class="w-full h-16 p-2 bg-transparent opacity-30 grayscale">
        <img :src="partner.logo" :alt="partner.name" class="w-full h-full object-contain" />
      </div>

      <!-- Partner Name (Small & Light) -->
      <div class="px-2">
        <p
          class="text-[10px] font-bold uppercase tracking-widest text-secondary/40 group-hover:text-primary/60 transition-colors leading-tight">
          {{ partner.name }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
  defineProps({
    partners: {
      type: Array,
      default: () => []
    }
  })
</script>

<style scoped>
  /* Specific partner grid spacing if needed */
</style>
