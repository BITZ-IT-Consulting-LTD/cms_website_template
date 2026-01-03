<template>
  <div v-if="partners && partners.length > 0" class="flex flex-wrap justify-center items-center gap-12 lg:gap-20">
    <div v-for="partner in partners" :key="partner.id"
      class="w-32 md:w-40 hover:opacity-100 transition-opacity duration-300">
      <template v-if="partner.logo">
        <a v-if="partner.website_url" :href="partner.website_url" target="_blank" rel="noopener" class="block">
          <img :src="partner.logo" :alt="partner.name"
            class="w-full h-20 object-contain grayscale hover:grayscale-0 transition-all duration-300" />
        </a>
        <img v-else :src="partner.logo" :alt="partner.name"
          class="w-full h-20 object-contain grayscale hover:grayscale-0 transition-all duration-300" />
      </template>
      <span v-else class="text-lg font-bold text-neutral block text-center">{{ partner.name }}</span>
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
