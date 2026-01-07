<template>
  <div v-if="partners && partners.length > 0"
    class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-6 md:gap-8 lg:gap-12 items-center">

    <div v-for="partner in partners" :key="partner.id" class="group flex flex-col items-center text-center space-y-3">

      <!-- Partner Logo with Link (Professional Treatment) -->
      <a v-if="partner.logo && partner.website_url" :href="partner.website_url" target="_blank"
        rel="noopener noreferrer" :aria-label="`Visit ${partner.name} website`"
        class="block w-full h-20 md:h-24 p-3 bg-white rounded-xl border border-primary/10 hover:border-primary/30 hover:shadow-md transition-all duration-300">
        <img :src="partner.logo" :alt="`${partner.name} logo`"
          class="w-full h-full object-contain hover:scale-105 transition-transform duration-300" />
      </a>

      <!-- Partner Logo Only (No Link) -->
      <div v-else-if="partner.logo"
        class="w-full h-20 md:h-24 p-3 bg-white rounded-xl border border-primary/5 opacity-90">
        <img :src="partner.logo" :alt="`${partner.name} logo`" class="w-full h-full object-contain" />
      </div>

      <!-- Partner Name (Legible & Accessible) -->
      <div class="px-2">
        <p
          class="text-xs md:text-sm font-semibold text-black/70 group-hover:text-primary transition-colors leading-tight">
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
