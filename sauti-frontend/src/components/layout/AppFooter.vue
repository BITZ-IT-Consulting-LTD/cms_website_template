<template>
  <footer class="bg-secondary text-neutral-white no-print border-t-8 border-accent-orange" role="contentinfo">
    <!-- Main Footer Content -->
    <div class="container-custom py-16">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">

        <!-- Brand Section -->
        <section class="space-y-6" aria-labelledby="footer-about">
          <div class="flex items-center gap-4">
            <BaseLogo size="md" variant="white" :alt="settings.site_name" />
            <h3 id="footer-about" class="text-2xl font-bold tracking-tight leading-tight text-neutral-white">
              {{ orgProfile?.name || settings.site_name || 'Sauti 116' }}
            </h3>
          </div>

          <p class="text-neutral-white leading-relaxed text-lg font-bold">
            {{ settings.site_description || `Uganda’s Child Helpline providing confidential, 24/7 support and
            crisis intervention.` }}
          </p>

          <nav class="flex flex-wrap gap-4" aria-label="Social media links">
            <a v-for="(link, platform) in socialMedia" :key="platform" v-show="link.url" :href="link.url"
              target="_blank" rel="noopener noreferrer"
              class="w-11 h-11 rounded-xl bg-neutral-white text-secondary flex items-center justify-center hover:bg-primary hover:text-neutral-white focus:outline-none transition-all transform hover:-translate-y-1 active:scale-95 group shadow-lg"
              :aria-label="`Visit our ${platform} page`">
              <i :class="link.icon" class="text-xl transition-colors" aria-hidden="true"></i>
            </a>
          </nav>
        </section>

        <!-- Navigation Section -->
        <nav aria-labelledby="footer-links">
          <h3 id="footer-links"
            class="text-lg font-bold uppercase tracking-widest mb-8 border-l-4 border-primary pl-4 text-neutral-white">
            Navigation
          </h3>
          <ul class="space-y-4">
            <li v-for="link in navLinks" :key="link.to">
              <router-link :to="link.to"
                class="text-neutral-white hover:text-primary focus:text-primary focus:outline-none rounded px-1 transition-all flex items-center gap-2 group text-lg font-bold">
                <div class="w-1.5 h-1.5 rounded-full bg-primary opacity-0 group-hover:opacity-100 transition-opacity">
                </div>
                {{ link.label }}
              </router-link>
            </li>
          </ul>
        </nav>

        <!-- Emergency & Support Section -->
        <section aria-labelledby="footer-support">
          <h3 id="footer-support"
            class="text-lg font-bold uppercase tracking-widest mb-8 border-l-4 border-emergency pl-4 text-neutral-white">
            Get Help
          </h3>
          <div class="space-y-8">
            <a :href="`tel:${settings.hotline_number || '116'}`"
              class="block group focus:outline-none rounded-2xl p-2 -m-2 transition-all"
              aria-label="Call our toll free hotline: 116">
              <span class="text-accent-orange font-bold text-xs uppercase tracking-[0.2em] block mb-1">Toll Free
                Helpline</span>
              <span
                class="text-4xl font-bold group-hover:text-accent-orange transition-colors block text-neutral-white">
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
            class="text-lg font-bold uppercase tracking-widest mb-8 border-l-4 border-primary pl-4 text-neutral-white">
            Contact Us
          </h3>
          <div class="inline-flex items-center gap-3 mb-6 bg-white/10 px-4 py-2 rounded-full border border-white/10">
            <CheckBadgeIcon class="w-4 h-4 text-secondary-light" />
            <span class="text-[10px] font-black uppercase tracking-[0.2em] text-neutral-white">Official Government
              Service</span>
          </div>
          <address class="not-italic space-y-6">
            <div v-if="settings.contact_email" class="flex items-start gap-4 group">
              <div
                class="w-10 h-10 rounded-xl bg-neutral-white text-primary flex items-center justify-center shrink-0 shadow-lg">
                <EnvelopeIcon class="w-5 h-5" aria-hidden="true" />
              </div>
              <div class="space-y-1">
                <span class="text-xs font-bold text-primary uppercase tracking-widest">Email
                  Address</span>
                <a :href="`mailto:${settings.contact_email}`"
                  class="block text-neutral-white hover:text-primary transition-colors focus:outline-none rounded px-1 font-bold">
                  {{ settings.contact_email }}
                </a>
              </div>
            </div>

            <div class="flex items-start gap-4 group">
              <div
                class="w-10 h-10 rounded-xl bg-neutral-white text-primary flex items-center justify-center shrink-0 shadow-lg">
                <MapPinIcon class="w-5 h-5" aria-hidden="true" />
              </div>
              <div class="space-y-1">
                <span class="text-xs font-bold text-primary uppercase tracking-widest">Visit Us</span>
                <p class="text-neutral-white leading-tight font-bold">
                  Ministry of Gender, Labour and Social Development, Kampala
                </p>
              </div>
            </div>
            <div>
              <h4 class="font-black text-xs uppercase tracking-[0.2em] text-primary mb-2">Legal Mandate & Governance
              </h4>
              <p class="text-sm text-neutral-white/90 leading-relaxed font-bold">
                Operated under the exclusive mandate of the **Ministry of Gender, Labour and Social Development**. All
                interventions are regulated, strictly confidential, and provided at no cost to the public.
              </p>
            </div>
          </address>
        </section>
      </div>
    </div>

    <!-- Sub-footer Bar (Consolidated Digital Endorsement) -->
    <div class="bg-neutral-black py-12 border-t-4 border-primary/30 relative overflow-hidden">
      <!-- Background subtle crest texture/decoration -->
      <div class="absolute right-0 bottom-0 top-0 w-1/3 opacity-[0.03] pointer-events-none grayscale invert">
        <BaseLogo size="lg" variant="white" class="scale-150 rotate-12" />
      </div>

      <div class="container-custom flex flex-col lg:flex-row justify-between items-center gap-10 relative z-10">
        <div class="text-center lg:text-left space-y-4">
          <div class="flex items-center justify-center lg:justify-start gap-4 mb-2">
            <div class="h-12 w-12 bg-neutral-white/10 rounded-xl p-2.5 backdrop-blur-sm border border-neutral-white/10">
              <img src="@/assets/logo.png" alt="GoU Crest"
                class="w-full h-full object-contain grayscale brightness-200" />
            </div>
            <div>
              <p class="text-neutral-white text-sm font-black uppercase tracking-widest leading-none mb-1">
                Official Helpline
              </p>
              <p class="text-[10px] text-primary font-bold uppercase tracking-[0.2em] opacity-80">
                Ministry of Gender, Labour and Social Development
              </p>
            </div>
          </div>
          <p class="text-neutral-white/40 text-[10px] font-bold uppercase tracking-[0.1em]">
            {{ settings.footer_text || `&copy; ${new Date().getFullYear()} Sauti 116. All rights reserved.` }}
          </p>
        </div>

        <nav class="flex flex-wrap justify-center gap-x-8 gap-y-4 text-[10px] font-black uppercase tracking-[0.2em]"
          aria-label="Legal navigation">
          <router-link v-for="legal in legalLinks" :key="legal.to" :to="legal.to"
            class="text-neutral-white/60 hover:text-primary transition-colors focus:outline-none focus:ring-1 focus:ring-primary rounded px-2">
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
  const orgProfile = computed(() => settingsStore.orgProfile)

  const socialMedia = computed(() => ({
    Facebook: { url: settings.value.social_facebook || 'https://facebook.com/sauti116', icon: 'fab fa-facebook-f' },
    X: { url: settings.value.social_twitter || 'https://twitter.com/sauti116', icon: 'fab fa-x-twitter' },
    TikTok: { url: settings.value.social_tiktok, icon: 'fab fa-tiktok' },
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

</script>

<style scoped></style>
