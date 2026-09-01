<template>
  <footer class="bg-[#006633] text-neutral-white py-6 lg:py-12" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
    <div class="container-custom">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-6 lg:gap-6">
        <!-- Brand Column -->
        <div class="md:col-span-2 lg:col-span-4 space-y-3 lg:space-y-6">
          <div>
            <!-- Explicit text-white is required here, not just inherited from
                 <footer>: a global `h2 { color: text-secondary }` base style
                 targets this tag directly, and that brand green (#006837) is
                 nearly identical to this footer's own background (#006633) --
                 without an explicit color the heading was effectively
                 invisible on every page. -->
            <h2 class="font-black uppercase tracking-tight text-white mb-2" :style="{ fontSize: 'clamp(1.25rem, 5vw, 1.875rem)', fontFamily: 'var(--font-cronos), cronos-pro, Cronos Pro, Georgia, serif' }">{{ siteContent.getContent('footer_brand_name', 'Sauti 116') }}</h2>
            <p class="text-neutral-white/70 font-bold leading-relaxed max-w-sm text-sm lg:text-base" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
              {{ siteContent.getContent('footer_brand_description', 'Uganda\'s verified National Child Helpline. Providing 24/7 confidential support, guidance, and emergency intervention for all citizens.') }}
            </p>
          </div>
          <div class="flex gap-2 lg:gap-4">
             <!-- X (Twitter) -->
             <a :href="siteContent.getContent('footer_social_x_url', 'https://x.com/sauti116?s=21')" target="_blank" rel="noopener noreferrer" class="social-btn group relative rounded-full bg-white flex items-center justify-center transition-all hover:scale-110 w-9 h-9 lg:w-12 lg:h-12">
                <BrandIcon name="x" class="w-5 h-5 lg:w-6 lg:h-6" />
                <span class="social-tooltip" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ siteContent.getContent('footer_social_x_label', 'X') }}</span>
             </a>
             <!-- Instagram -->
             <a :href="siteContent.getContent('footer_social_instagram_url', 'https://www.instagram.com/sauti116helpline?igsh=MTdyNjgwOG42ZjB2dA%3D%3D&utm_source=qr')" target="_blank" rel="noopener noreferrer" class="social-btn group relative rounded-full bg-white flex items-center justify-center transition-all hover:scale-110 w-9 h-9 lg:w-12 lg:h-12">
                <BrandIcon name="instagram" class="w-5 h-5 lg:w-6 lg:h-6" />
                <span class="social-tooltip" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ siteContent.getContent('footer_social_instagram_label', 'Instagram') }}</span>
             </a>
             <!-- Facebook -->
             <a :href="siteContent.getContent('footer_social_facebook_url', 'https://www.facebook.com/share/14W6eurox1o/')" target="_blank" rel="noopener noreferrer" class="social-btn group relative rounded-full bg-white flex items-center justify-center transition-all hover:scale-110 w-9 h-9 lg:w-12 lg:h-12">
                <BrandIcon name="facebook" class="w-5 h-5 lg:w-6 lg:h-6" />
                <span class="social-tooltip" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ siteContent.getContent('footer_social_facebook_label', 'Facebook') }}</span>
             </a>
             <!-- TikTok -->
             <a :href="siteContent.getContent('footer_social_tiktok_url', 'https://www.tiktok.com/@sauti116helplineuganda?_r=1&_t=ZS-952NtlMMSIs')" target="_blank" rel="noopener noreferrer" class="social-btn group relative rounded-full bg-white flex items-center justify-center transition-all hover:scale-110 w-9 h-9 lg:w-12 lg:h-12">
                <BrandIcon name="tiktok" class="w-5 h-5 lg:w-6 lg:h-6" />
                <span class="social-tooltip" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ siteContent.getContent('footer_social_tiktok_label', 'TikTok') }}</span>
             </a>
             <!-- YouTube -->
             <a :href="siteContent.getContent('footer_social_youtube_url', 'https://www.youtube.com/@Sauti116HelplineUganda')" target="_blank" rel="noopener noreferrer" class="social-btn group relative rounded-full bg-white flex items-center justify-center transition-all hover:scale-110 w-9 h-9 lg:w-12 lg:h-12">
                <BrandIcon name="youtube" class="w-5 h-5 lg:w-6 lg:h-6" />
                <span class="social-tooltip" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ siteContent.getContent('footer_social_youtube_label', 'YouTube') }}</span>
             </a>
             <!-- WhatsApp -->
             <a :href="whatsappUrl" target="_blank" rel="noopener noreferrer" class="social-btn group relative rounded-full bg-white flex items-center justify-center transition-all hover:scale-110 w-9 h-9 lg:w-12 lg:h-12">
                <BrandIcon name="whatsapp" class="w-5 h-5 lg:w-6 lg:h-6" />
                <span class="social-tooltip" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ siteContent.getContent('footer_social_whatsapp_label', 'WhatsApp') }}</span>
             </a>
          </div>
        </div>

        <!-- Quick Links -->
        <div class="lg:col-span-2 lg:col-start-6 space-y-2 lg:space-y-5">
          <h3 class="text-[10px] lg:text-xs font-black uppercase tracking-widest text-neutral-white/50" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ siteContent.getContent('footer_menu_heading', 'Menu') }}</h3>
          <ul class="space-y-1.5 lg:space-y-3 font-bold text-sm lg:text-base" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
            <li><router-link to="/" class="hover:text-secondary-light transition-colors">{{ siteContent.getContent('footer_nav_home', 'Home') }}</router-link></li>
            <li><router-link to="/about" class="hover:text-secondary-light transition-colors">{{ siteContent.getContent('footer_nav_about', 'Who We Are') }}</router-link></li>
            <li><router-link to="/videos" class="hover:text-secondary-light transition-colors">{{ siteContent.getContent('footer_nav_videos', 'Videos') }}</router-link></li>
            <li><router-link to="/blogs" class="hover:text-secondary-light transition-colors">{{ siteContent.getContent('footer_nav_blogs', 'Blogs') }}</router-link></li>
            <li><router-link to="/news" class="hover:text-secondary-light transition-colors">{{ siteContent.getContent('footer_nav_news', 'Updates') }}</router-link></li>
            <li><router-link to="/resources" class="hover:text-secondary-light transition-colors">{{ siteContent.getContent('footer_nav_resources', 'Resources') }}</router-link></li>
          </ul>
        </div>

        <!-- Support -->
        <div class="lg:col-span-2 lg:col-start-8 space-y-2 lg:space-y-5">
          <h3 class="text-[10px] lg:text-xs font-black uppercase tracking-widest text-neutral-white/50" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ siteContent.getContent('footer_support_heading', 'Support') }}</h3>
          <ul class="space-y-1.5 lg:space-y-3 font-bold text-sm lg:text-base" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
            <li><router-link to="/report" class="hover:text-secondary-light transition-colors">{{ siteContent.getContent('footer_nav_report', 'Report a Case') }}</router-link></li>
            <li><router-link to="/faqs" class="hover:text-secondary-light transition-colors">{{ siteContent.getContent('footer_nav_faqs', 'FAQs') }}</router-link></li>
            <li><router-link to="/contact" class="hover:text-secondary-light transition-colors">{{ siteContent.getContent('footer_nav_contact', 'Contact Us') }}</router-link></li>
            <li>
              <router-link v-if="!isExternalUrl(privacyUrl)" :to="privacyUrl" class="hover:text-secondary-light transition-colors">{{ siteContent.getContent('footer_nav_privacy', 'Privacy Policy') }}</router-link>
              <a v-else :href="privacyUrl" target="_blank" rel="noopener noreferrer" class="hover:text-secondary-light transition-colors">{{ siteContent.getContent('footer_nav_privacy', 'Privacy Policy') }}</a>
            </li>
            <li>
              <router-link v-if="!isExternalUrl(termsUrl)" :to="termsUrl" class="hover:text-secondary-light transition-colors">{{ siteContent.getContent('footer_nav_terms', 'Terms of Service') }}</router-link>
              <a v-else :href="termsUrl" target="_blank" rel="noopener noreferrer" class="hover:text-secondary-light transition-colors">{{ siteContent.getContent('footer_nav_terms', 'Terms of Service') }}</a>
            </li>
            <li>
              <router-link v-if="!isExternalUrl(accessibilityUrl)" :to="accessibilityUrl" class="hover:text-secondary-light transition-colors">{{ siteContent.getContent('footer_nav_accessibility', 'Accessibility') }}</router-link>
              <a v-else :href="accessibilityUrl" target="_blank" rel="noopener noreferrer" class="hover:text-secondary-light transition-colors">{{ siteContent.getContent('footer_nav_accessibility', 'Accessibility') }}</a>
            </li>
          </ul>
        </div>

        <!-- Contact Column -->
        <div class="md:col-span-2 lg:col-span-3 lg:col-start-10 space-y-2 lg:space-y-5">
           <h3 class="text-[10px] lg:text-xs font-black uppercase tracking-widest text-neutral-white/50" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ siteContent.getContent('footer_contact_heading', 'Contact') }}</h3>
           <div class="space-y-3 lg:space-y-5">
              <a href="tel:116" class="flex items-center gap-3 lg:gap-4 group">
                 <div class="rounded-xl lg:rounded-2xl bg-white/10 flex items-center justify-center group-hover:bg-white group-hover:text-primary transition-all w-10 h-10 lg:w-12 lg:h-12">
                    <Phone class="w-5 h-5 lg:w-6 lg:h-6" />
                 </div>
                 <div>
                    <span class="block text-[10px] lg:text-xs font-bold opacity-60 uppercase tracking-wider" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ siteContent.getContent('footer_hotline_label', 'Toll Free') }}</span>
                    <span class="text-lg lg:text-2xl font-black" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ siteContent.getContent('footer_hotline_number', 'Call 116') }}</span>
                 </div>
              </a>

              <a :href="`mailto:${siteContent.getContent('footer_email_address', 'info@sauti116.ug')}`" class="flex items-center gap-3 lg:gap-4 group">
                 <div class="rounded-xl lg:rounded-2xl bg-white/10 flex items-center justify-center group-hover:bg-white group-hover:text-primary transition-all w-10 h-10 lg:w-12 lg:h-12">
                    <Mail class="w-5 h-5 lg:w-6 lg:h-6" />
                 </div>
                 <div>
                    <span class="block text-[10px] lg:text-xs font-bold opacity-60 uppercase tracking-wider" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ siteContent.getContent('footer_email_label', 'Email Us') }}</span>
                    <span class="text-sm lg:text-lg font-bold break-all" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ siteContent.getContent('footer_email_address', 'info@sauti116.ug') }}</span>
                 </div>
              </a>
           </div>
        </div>
      </div>

      <!-- Legal & Attribution -->
      <div v-if="footerText || ministryAttributionText || disclaimerText" class="mt-6 lg:mt-12 pt-4 lg:pt-8 border-t border-neutral-white/10 space-y-2 lg:space-y-3">
        <p v-if="footerText" class="text-xs lg:text-sm text-neutral-white/60 font-semibold leading-relaxed" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ footerText }}</p>
        <p v-if="ministryAttributionText" class="text-[10px] lg:text-xs font-bold text-neutral-white/50 uppercase tracking-widest" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ ministryAttributionText }}</p>
        <p v-if="disclaimerText" class="text-[10px] lg:text-xs text-neutral-white/40 leading-relaxed" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ disclaimerText }}</p>
      </div>

      <!-- Bottom Bar -->
      <div class="mt-6 lg:mt-12 pt-4 lg:pt-8 border-t border-neutral-white/10 flex flex-col md:flex-row items-center justify-between gap-3 lg:gap-6">
        <p class="text-[10px] lg:text-xs font-bold text-neutral-white/40 uppercase tracking-widest text-center md:text-left" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
           {{ siteContent.getContent('footer_copyright', '© 2026 Sauti 116. Ministry of Gender, Labour and Social Development.') }}
        </p>
        <div class="flex items-center gap-2 text-neutral-white/40">
           <Globe class="w-3 h-3 lg:w-4 lg:h-4" />
           <span class="text-[10px] lg:text-xs font-bold uppercase tracking-widest" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ siteContent.getContent('footer_country_label', 'Uganda') }}</span>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import {
  Phone,
  Mail,
  Globe
} from 'lucide-vue-next'
import { useSiteContent } from '@/composables/useSiteContent'
import { useSettingsStore } from '@/store/settings'
import BrandIcon from '@/components/common/BrandIcon.vue'
import { toWaMeNumber } from '@/utils/phone'

const siteContent = useSiteContent('footer')
const settingsStore = useSettingsStore()

const isExternalUrl = (url) => typeof url === 'string' && /^https?:\/\//i.test(url)

// Same normalisation ContactPage uses for its WhatsApp channel: the CMS value
// may be entered in Uganda local format (e.g. '0743889999'), which wa.me
// rejects — toWaMeNumber() converts it to the international digits-only form.
const whatsappUrl = computed(() => `https://wa.me/${toWaMeNumber(siteContent.getContent('footer_social_whatsapp_number', '0743889999'))}`)

const privacyUrl = computed(() => settingsStore.settings.privacy_policy_url || '/privacy')
const termsUrl = computed(() => settingsStore.settings.terms_of_service_url || '/terms')
const accessibilityUrl = computed(() => settingsStore.settings.accessibility_url || '/accessibility')

const footerText = computed(() => settingsStore.settings.footer_text || '')
const disclaimerText = computed(() => settingsStore.settings.disclaimer_text || '')
const ministryAttributionText = computed(() => settingsStore.settings.ministry_attribution_text || '')

onMounted(async () => {
  await siteContent.fetchContent()
  await settingsStore.fetchGlobalSettings()
})
</script>

<style scoped>
.social-tooltip {
  position: absolute;
  bottom: calc(100% + 0.5rem);
  left: 50%;
  transform: translateX(-50%);
  background-color: #FFFFFF;
  color: #000000;
  padding: clamp(0.25rem, 2vw, 0.375rem) clamp(0.5rem, 3vw, 0.75rem);
  border-radius: 0.375rem;
  font-size: clamp(0.625rem, 2vw, 0.75rem);
  font-weight: 700;
  white-space: nowrap;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
  pointer-events: none;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 10;
  max-width: 90vw; /* Prevent overflow on small screens */
  font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;
}

/* Tooltip Arrow */
.social-tooltip::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -6px;
  border-width: 6px;
  border-style: solid;
  border-color: #FFFFFF transparent transparent transparent;
}

/* Reveal Tooltip on Hover */
.group:hover .social-tooltip {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
}

/* Mobile-specific positioning to prevent tooltip overflow */
@media (max-width: 640px) {
  .social-tooltip {
    position: fixed;
    bottom: auto;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .group:hover .social-tooltip {
    transform: translate(-50%, -50%);
  }

  /* Hide arrow on mobile since we're using fixed positioning */
  .social-tooltip::after {
    display: none;
  }
}
</style>
