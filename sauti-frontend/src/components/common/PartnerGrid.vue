<template>
  <div v-if="partners && partners.length > 0"
    class="flex flex-wrap justify-center items-start gap-8 md:gap-12">

    <div v-for="(partner, index) in partners" :key="partner.id"
      class="partner-item group"
      :style="{ animationDelay: `${index * 100}ms` }">

      <!-- Partner with Link -->
      <a v-if="partner.website_url"
        :href="partner.website_url"
        target="_blank"
        rel="noopener noreferrer"
        :aria-label="`Visit ${partner.name} website`"
        class="partner-link">

        <!-- Logo -->
        <div class="logo-container">
          <img v-if="partner.logo_thumbnail_url || partner.logo_url || partner.logo"
            :src="partner.logo_thumbnail_url || partner.logo_url || partner.logo"
            :alt="`${partner.name} logo`"
            width="120"
            height="80"
            loading="lazy"
            decoding="async"
            class="partner-logo" />
          <div v-else class="logo-placeholder">
            <svg class="w-10 h-10 text-gray-300" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z" clip-rule="evenodd" />
            </svg>
          </div>
        </div>

        <!-- Partner Name & Type -->
        <p class="partner-name">{{ partner.name }}</p>
        <span v-if="partner.partner_type" class="partner-type">
          {{ formatPartnerType(partner.partner_type) }}
        </span>
      </a>

      <!-- Non-linked Partner -->
      <div v-else class="partner-link partner-link--static">
        <div class="logo-container">
          <img v-if="partner.logo_thumbnail_url || partner.logo_url || partner.logo"
            :src="partner.logo_thumbnail_url || partner.logo_url || partner.logo"
            :alt="`${partner.name} logo`"
            width="120"
            height="80"
            loading="lazy"
            decoding="async"
            class="partner-logo" />
          <div v-else class="logo-placeholder">
            <svg class="w-10 h-10 text-gray-300" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z" clip-rule="evenodd" />
            </svg>
          </div>
        </div>
        <p class="partner-name">{{ partner.name }}</p>
        <span v-if="partner.partner_type" class="partner-type">
          {{ formatPartnerType(partner.partner_type) }}
        </span>
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

  function formatPartnerType(type) {
    const types = {
      'GOVERNMENT': 'Government',
      'NGO': 'NGO',
      'INTERNATIONAL': 'International',
      'CORPORATE': 'Corporate',
      'ACADEMIC': 'Academic',
      'OTHER': 'Partner'
    }
    return types[type] || type
  }
</script>

<style scoped>
  /* Item Animation */
  .partner-item {
    animation: fadeInUp 0.5s ease-out forwards;
    opacity: 0;
    flex: 0 0 auto;
    width: 140px;
  }

  @media (min-width: 640px) {
    .partner-item {
      width: 160px;
    }
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

  /* Partner Link - Clean, no card */
  .partner-link {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 1rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    text-decoration: none;
  }

  .partner-link:hover {
    transform: translateY(-4px);
  }

  .partner-link--static {
    cursor: default;
  }

  .partner-link--static:hover {
    transform: none;
  }

  /* Logo Container */
  .logo-container {
    width: 120px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 0.75rem;
  }

  /* Logo - Full color, clean display */
  .partner-logo {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .partner-link:hover .partner-logo {
    transform: scale(1.08);
  }

  /* Logo Placeholder */
  .logo-placeholder {
    width: 80px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgb(var(--color-neutral-offwhite));
    border-radius: 0.5rem;
  }

  /* Partner Name */
  .partner-name {
    font-size: 0.875rem;
    font-weight: 600;
    color: rgb(var(--color-secondary));
    line-height: 1.3;
    margin-bottom: 0.375rem;
    transition: color 0.3s ease;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .partner-link:hover .partner-name {
    color: rgb(var(--color-primary));
  }

  /* Partner Type Badge */
  .partner-type {
    display: inline-block;
    font-size: 0.625rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: rgb(var(--color-primary));
    background: rgb(var(--color-primary) / 0.1);
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    transition: all 0.3s ease;
  }

  .partner-link:hover .partner-type {
    background: rgb(var(--color-primary) / 0.2);
  }

  /* Responsive Adjustments */
  @media (max-width: 640px) {
    .logo-container {
      width: 100px;
      height: 65px;
    }

    .partner-name {
      font-size: 0.75rem;
    }

    .partner-type {
      font-size: 0.5625rem;
      padding: 0.1875rem 0.5rem;
    }
  }
</style>
