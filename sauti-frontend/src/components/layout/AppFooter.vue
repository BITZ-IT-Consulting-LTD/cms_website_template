<template>
  <footer class="bg-sauti-darkGreen text-sauti-white no-print border-t-8 border-sauti-orange" role="contentinfo">
    <!-- Main Footer Content -->
    <div class="container-custom py-16">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">

        <!-- Brand Section -->
        <section class="space-y-6" aria-labelledby="footer-about">
          <div class="flex items-center gap-4">
            <BaseLogo size="md" variant="white" :alt="settings.site_name" />
            <h3 id="footer-about" class="text-2xl font-bold tracking-tight leading-tight text-sauti-white">
              {{ settings.site_name || 'Sauti 116' }}
            </h3>
          </div>

          <p class="text-sauti-white leading-relaxed text-lg font-bold">
            {{ settings.site_description || `Uganda’s National Child Helpline providing confidential, 24/7 support and
            crisis intervention.` }}
          </p>

          <nav class="flex flex-wrap gap-4" aria-label="Social media links">
            <a v-for="(link, platform) in socialMedia" :key="platform" v-show="link.url" :href="link.url"
              target="_blank" rel="noopener noreferrer"
              class="w-11 h-11 rounded-xl bg-sauti-white text-sauti-darkGreen flex items-center justify-center hover:bg-sauti-blue hover:text-sauti-white focus:outline-none transition-all transform hover:-translate-y-1 active:scale-95 group shadow-lg"
              :aria-label="`Visit our ${platform} page`">
              <i :class="link.icon" class="text-xl transition-colors" aria-hidden="true"></i>
            </a>
          </nav>
        </section>

        <!-- Navigation Section -->
        <nav aria-labelledby="footer-links">
          <h3 id="footer-links"
            class="text-lg font-bold uppercase tracking-widest mb-8 border-l-4 border-sauti-blue pl-4 text-sauti-white">
            Navigation
          </h3>
          <ul class="space-y-4">
            <li v-for="link in navLinks" :key="link.to">
              <router-link :to="link.to"
                class="text-sauti-white hover:text-sauti-blue focus:text-sauti-blue focus:outline-none rounded px-1 transition-all flex items-center gap-2 group text-lg font-bold">
                <div
                  class="w-1.5 h-1.5 rounded-full bg-sauti-blue opacity-0 group-hover:opacity-100 transition-opacity">
                </div>
                {{ link.label }}
              </router-link>
            </li>
          </ul>
        </nav>

        <!-- Emergency & Support Section -->
        <section aria-labelledby="footer-support">
          <h3 id="footer-support"
            class="text-lg font-bold uppercase tracking-widest mb-8 border-l-4 border-sauti-red pl-4 text-sauti-white">
            Get Help
          </h3>
          <div class="space-y-8">
            <a :href="`tel:${settings.hotline_number || '116'}`"
              class="block group focus:outline-none rounded-2xl p-2 -m-2 transition-all"
              aria-label="Call our toll free hotline: 116">
              <span class="text-sauti-orange font-bold text-xs uppercase tracking-[0.2em] block mb-1">Toll Free
                Helpline</span>
              <span class="text-4xl font-bold group-hover:text-sauti-orange transition-colors block text-sauti-white">
                {{ settings.hotline_number || '116' }}
              </span>
            </a>

            <router-link to="/report" class="btn-emergency">
              <ShieldCheckIcon class="w-6 h-6" aria-hidden="true" />
              <span>{{ settings.primary_cta_text || 'Report a Case' }}</span>
            </router-link>
          </div>
        </section>

        <!-- Contact Section -->
        <section aria-labelledby="footer-contact">
          <h3 id="footer-contact"
            class="text-lg font-bold uppercase tracking-widest mb-8 border-l-4 border-sauti-blue pl-4 text-sauti-white">
            Contact Us
          </h3>
          <address class="not-italic space-y-6">
            <div v-if="settings.contact_email" class="flex items-start gap-4 group">
              <div
                class="w-10 h-10 rounded-xl bg-sauti-white text-sauti-blue flex items-center justify-center shrink-0 shadow-lg">
                <EnvelopeIcon class="w-5 h-5" aria-hidden="true" />
              </div>
              <div class="space-y-1">
                <span class="text-xs font-bold text-sauti-white uppercase tracking-widest opacity-60">Email
                  Address</span>
                <a :href="`mailto:${settings.contact_email}`"
                  class="block text-sauti-white hover:text-sauti-blue transition-colors focus:outline-none rounded px-1">
                  {{ settings.contact_email }}
                </a>
              </div>
            </div>

            <div v-if="settings.ministry_attribution_text"
              class="flex flex-col gap-2 pt-6 border-t-2 border-sauti-blue mt-6">
              <span class="text-xs font-bold text-sauti-orange uppercase tracking-widest">Official Governance</span>
              <p class="text-sauti-white text-base font-bold leading-tight uppercase">
                {{ settings.ministry_attribution_text || 'Ministry of Gender, Labour and Social Development (MGLSD)' }}
              </p>
              <div class="h-1 w-12 bg-sauti-blue rounded-full"></div>
            </div>
          </address>
        </section>
      </div>
    </div>

    <!-- Sub-footer Bar -->
    <div class="bg-sauti-black py-10 border-t-4 border-sauti-blue">
      <div class="container-custom flex flex-col lg:flex-row justify-between items-center gap-8">
        <div class="text-center lg:text-left space-y-2">
          <p class="text-sauti-white text-sm font-bold">
            {{ settings.footer_text || `&copy; ${new Date().getFullYear()} Sauti 116. All rights reserved.` }}
          </p>
          <p class="text-[10px] text-sauti-blue uppercase tracking-[0.3em] font-bold">
            Uganda National Child Helpline
          </p>
        </div>

        <nav class="flex flex-wrap justify-center gap-x-8 gap-y-4 text-xs font-bold uppercase tracking-widest"
          aria-label="Legal navigation">
          <router-link v-for="legal in legalLinks" :key="legal.to" :to="legal.to"
            class="text-sauti-white hover:text-sauti-blue focus:text-sauti-blue transition-colors focus:outline-none rounded px-2">
            {{ legal.label }}
          </router-link>
        </nav>
      </div>
    </div>
  </footer>
</template>

<script setup>
  import { computed, onMounted } from 'vue'
  import { useSettingsStore } from '@/store/settings'
  import BaseLogo from '@/components/common/BaseLogo.vue'
  import {
    ShieldCheckIcon,
    EnvelopeIcon,
    MapPinIcon
  } from '@heroicons/vue/24/outline'

  const settingsStore = useSettingsStore()
  const settings = computed(() => settingsStore.settings)

  const socialMedia = computed(() => ({
    Facebook: { url: settings.value.social_facebook || 'https://facebook.com/sauti116', icon: 'fab fa-facebook-f' },
    'Twitter (X)': { url: settings.value.social_twitter || 'https://twitter.com/sauti116', icon: 'fab fa-twitter' },
    Instagram: { url: settings.value.social_instagram, icon: 'fab fa-instagram' },
    WhatsApp: { url: settings.value.social_whatsapp || 'https://wa.me/256743889999', icon: 'fab fa-whatsapp' }
  }))

  const navLinks = computed(() => {
    const links = settings.value.footer_links || []
    const dynamicLinks = links.filter(l => l.type === 'nav')
    if (dynamicLinks.length > 0) return dynamicLinks

    // Fallback defaults
    return [
      { label: 'Home', to: '/' },
      { label: 'About Us', to: '/about' },
      { label: 'Latest News', to: '/blogs' },
      { label: 'Resources', to: '/resources' },
      { label: 'FAQs', to: '/faqs' }
    ]
  })

  const legalLinks = computed(() => {
    const links = settings.value.footer_links || []
    const dynamicLinks = links.filter(l => l.type === 'legal')
    if (dynamicLinks.length > 0) return dynamicLinks

    // Fallback defaults
    return [
      { label: 'Privacy Policy', to: '/privacy' },
      { label: 'Terms of Service', to: '/terms' },
      { label: 'Accessibility', to: '/accessibility' }
    ]
  })

  onMounted(async () => {
    await settingsStore.fetchGlobalSettings()
  })
</script>

<style scoped></style>
