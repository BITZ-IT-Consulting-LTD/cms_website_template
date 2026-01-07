<template>
  <div class="bg-neutral-white rounded-lg shadow-lg overflow-hidden border border-neutral-offwhite">
    <!-- Logo -->
    <div class="h-48 bg-neutral-offwhite flex items-center justify-center p-8">
      <img
        v-if="partner.logo"
        :src="partner.logo"
        :alt="partner.name"
        class="max-h-full max-w-full object-contain"
        @error="handleImageError"
      />
      <div v-else class="text-center">
        <svg class="w-20 h-20 mx-auto text-secondary/30" fill="currentColor" viewBox="0 0 20 20">
          <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z" />
        </svg>
      </div>
    </div>

    <!-- Content -->
    <div class="p-6">
      <h3 class="text-xl font-bold text-secondary mb-2">
        {{ partner.name }}
      </h3>

      <p v-if="partner.description" class="text-secondary/70 text-sm mb-4 line-clamp-3">
        {{ partner.description }}
      </p>

      <!-- Partner Type Badge -->
      <span v-if="partner.partner_type" class="inline-block px-3 py-1 text-xs font-semibold bg-primary/10 text-primary rounded-full mb-4">
        {{ partner.partner_type }}
      </span>

      <!-- Contact Information -->
      <div class="space-y-4 text-sm">
        <a
          v-if="partner.website"
          :href="partner.website"
          target="_blank"
          rel="noopener noreferrer"
          class="flex items-center text-primary hover:text-primary/80 transition-colors"
        >
          <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z" clip-rule="evenodd" />
          </svg>
          Visit Website
        </a>

        <a
          v-if="partner.email"
          :href="'mailto:' + partner.email"
          class="flex items-center text-secondary/70 hover:text-secondary transition-colors"
        >
          <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
            <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
            <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
          </svg>
          {{ partner.email }}
        </a>

        <a
          v-if="partner.phone"
          :href="'tel:' + partner.phone"
          class="flex items-center text-secondary/70 hover:text-secondary transition-colors"
        >
          <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
            <path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z" />
          </svg>
          {{ partner.phone }}
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
defineOptions({
  name: 'PartnerCard'
})

defineProps({
  partner: {
    type: Object,
    required: true
  }
})

const handleImageError = (event) => {
  event.target.src = 'https://via.placeholder.com/150?text=Logo' // Placeholder image
}
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
