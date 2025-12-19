<template>
  <footer class="text-white no-print" style="background-color: #006633;">
    <!-- Main Footer Content -->
    <div class="container-custom py-12">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <!-- About Section -->
        <div>
          <h3 class="text-xl font-bold mb-4">{{ settings.site_name }}</h3>
          <p class="text-gray-400 mb-4">
            {{ settings.site_description }}
          </p>
          <div class="flex space-x-4">
            <!-- Facebook -->
            <a :href="socialFacebook" target="_blank" rel="noopener" class="text-gray-400 hover:text-white transition-colors" aria-label="Facebook - Sauti 116 Helpline">
              <svg class="w-6 h-6" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path d="M22.675 0H1.325C.593 0 0 .593 0 1.325v21.351C0 23.407.593 24 1.325 24H12.82v-9.294H9.692V11.09h3.129V8.413c0-3.1 1.893-4.788 4.659-4.788 1.325 0 2.463.099 2.795.143v3.24l-1.918.001c-1.503 0-1.794.715-1.794 1.763v2.316h3.587l-.467 3.616h-3.12V24h6.116C23.407 24 24 23.407 24 22.676V1.325C24 .593 23.407 0 22.675 0z"/>
              </svg>
            </a>
            <!-- X / Twitter -->
            <a :href="socialTwitter" target="_blank" rel="noopener" class="text-gray-400 hover:text-white transition-colors" aria-label="X (Twitter) - @sauti116">
              <svg class="w-6 h-6" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path d="M18.244 2H21l-6.52 7.455L22.5 22h-6.9l-4.5-6.22L5.7 22H3l7.03-8.036L1.5 2h7.02l4.08 5.64L18.244 2zm-2.41 18h1.6L8.28 4h-1.6l9.155 16z"/>
              </svg>
            </a>
            <!-- WhatsApp -->
            <a :href="socialWhatsapp" target="_blank" rel="noopener" class="text-gray-400 hover:text-white transition-colors" aria-label="WhatsApp">
              <svg class="w-6 h-6" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path d="M20.52 3.48A11.86 11.86 0 0012.07 0C5.43 0 .08 5.35.08 11.96c0 2.11.55 4.09 1.6 5.86L0 24l6.35-1.66a11.93 11.93 0 005.72 1.46h.01c6.63 0 12-5.36 12-11.98 0-3.2-1.25-6.2-3.56-8.34zM12.08 22a9.93 9.93 0 01-5.06-1.38l-.36-.21-3.77.99.99-3.65-.24-.37a9.9 9.9 0 01-1.66-5.41C2 6.46 6.55 1.98 12.07 1.98a10.06 10.06 0 017.14 2.95 9.95 9.95 0 012.94 7.12c0 5.53-4.51 10-10.07 10z"/>
              </svg>
            </a>
            <!-- Email -->
            <a :href="`mailto:${contactEmailSautichl}`" class="text-gray-400 hover:text-white transition-colors" aria-label="Email">
              <svg class="w-6 h-6" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path d="M4 4h16a2 2 0 012 2v12a2 2 0 01-2 2H4a2 2 0 01-2-2V6a2 2 0 012-2zm0 2v.01L12 13l8-6.99V6H4zm16 12V9l-8 7-8-7v9h16z"/>
              </svg>
            </a>
            <!-- Website -->
            <a :href="contactWebsite" target="_blank" rel="noopener" class="text-gray-400 hover:text-white transition-colors" aria-label="Website">
              <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" aria-hidden="true">
                <circle cx="12" cy="12" r="9" stroke-width="1.8"/>
                <path d="M3 12h18" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M12 3a15 15 0 010 18" stroke-width="1.8" stroke-linecap="round"/>
                <path d="M12 3a15 15 0 000 18" stroke-width="1.8" stroke-linecap="round"/>
              </svg>
            </a>
          </div>
        </div>

        <!-- Quick Links -->
        <div>
          <h3 class="text-lg font-semibold mb-4">Quick Links</h3>
          <ul class="space-y-2">
            <li><router-link to="/" class="text-gray-400 hover:text-white transition-colors">Home</router-link></li>
            <li><router-link to="/about" class="text-gray-400 hover:text-white transition-colors">About Us</router-link></li>
            <li><router-link to="/blogs" class="text-gray-400 hover:text-white transition-colors">Blogs</router-link></li>
            <li><router-link to="/resources" class="text-gray-400 hover:text-white transition-colors">Resources</router-link></li>
            <li><router-link to="/partners" class="text-gray-400 hover:text-white transition-colors">Partners</router-link></li>
            <li><router-link to="/donate" class="text-gray-400 hover:text-white transition-colors">Donate</router-link></li>
            <li><router-link to="/report" class="text-gray-400 hover:text-white transition-colors">Report a Case</router-link></li>
            <li><router-link to="/reports" class="text-gray-400 hover:text-white transition-colors">Reports</router-link></li>
            <li><router-link to="/faqs" class="text-gray-400 hover:text-white transition-colors">FAQs</router-link></li>
            <li><router-link to="/privacy" class="text-gray-400 hover:text-white transition-colors">Privacy Policy</router-link></li>
            <li><router-link to="/terms" class="text-gray-400 hover:text-white transition-colors">Terms of Service</router-link></li>
          </ul>
        </div>

        <!-- Services / Channels -->
        <div>
          <h3 class="text-lg font-semibold mb-4">Get Help</h3>
          <ul class="space-y-2">
            <li>
              <router-link to="/report" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3 3h18v4H3zM3 10h18v11H3z"/></svg>
                <span>Report a Case</span>
              </router-link>
            </li>
            <li>
              <router-link to="/contact" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
                <span>Contact Us</span>
              </router-link>
            </li>
            <li>
              <a :href="`tel:${contactPhone}`" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1 1 0 011.01-.24c1.12.37 2.33.57 3.58.57a1 1 0 011 1V21a1 1 0 01-1 1C10.85 22 2 13.15 2 2a1 1 0 011-1h3.5a1 1 0 011 1c0 1.25.2 2.46.57 3.58a1 1 0 01-.24 1.01l-2.21 2.2z"/></svg>
                <span>Call {{ contactPhone }}</span>
              </a>
            </li>
            <li>
              <a :href="socialWhatsapp" target="_blank" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.52 3.48A11.86 11.86 0 0012.07 0C5.43 0 .08 5.35.08 11.96c0 2.11.55 4.09 1.6 5.86L0 24l6.35-1.66a11.93 11.93 0 005.72 1.46h.01c6.63 0 12-5.36 12-11.98 0-3.2-1.25-6.2-3.56-8.34z"/></svg>
                <span>WhatsApp</span>
              </a>
            </li>
            <li>
              <a :href="socialUreport" target="_blank" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20 2H4a2 2 0 00-2 2v14l4-4h14a2 2 0 002-2V4a2 2 0 00-2-2z"/></svg>
                <span>U‑Report (SMS “Hello” to 116)</span>
              </a>
            </li>
            <li>
              <a :href="contactWebsite" target="_blank" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" aria-hidden="true">
                  <circle cx="12" cy="12" r="9" stroke-width="1.8"/>
                  <path d="M3 12h18" stroke-width="1.8" stroke-linecap="round"/>
                  <path d="M12 3a15 15 0 010 18" stroke-width="1.8" stroke-linecap="round"/>
                  <path d="M12 3a15 15 0 000 18" stroke-width="1.8" stroke-linecap="round"/>
                </svg>
                <span>Online Reporting</span>
              </a>
            </li>
            <li>
              <a :href="socialSafepal" target="_blank" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l10 6-10 6L2 8l10-6zm0 7l10 6-10 6-10-6 10-6z"/></svg>
                <span>SafePal App</span>
              </a>
            </li>
            <li>
              <a :href="`mailto:${contactEmailInfo}`" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4 4h16a2 2 0 012 2v12a2 2 0 01-2 2H4a2 2 0 01-2-2V6a2 2 0 012-2zm0 2v.01L12 13l8-6.99V6H4zm16 12V9l-8 7-8-7v9h16z"/></svg>
                <span>{{ contactEmailInfo }}</span>
              </a>
            </li>
            <li>
              <a :href="`mailto:${contactEmailSautichl}`" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4 4h16a2 2 0 012 2v12a2 2 0 01-2 2H4a2 2 0 01-2-2V6a2 2 0 012-2zm0 2v.01L12 13l8-6.99V6H4zm16 12V9l-8 7-8-7v9h16z"/></svg>
                <span>{{ contactEmailSautichl }}</span>
              </a>
            </li>
          </ul>
        </div>

        <!-- Contact Info -->
        <div>
          <h3 class="text-lg font-semibold mb-4">Contact Info</h3>
          <ul class="space-y-3 text-gray-400">
            <li class="flex items-start">
              <svg class="w-5 h-5 mr-2 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
              </svg>
              <span>{{ contactPhone }} (Toll Free)</span>
            </li>
            <li class="flex items-start">
              <svg class="w-5 h-5 mr-2 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
              </svg>
              <span>{{ contactEmailInfo }}</span>
            </li>
            <li class="flex items-start">
              <svg class="w-5 h-5 mr-2 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
              </svg>
              <span>{{ settings.ministry_attribution_text }}</span>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Trust badges -->
    <div>
      <div class="container-custom py-6">
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 text-center text-gray-400 text-sm">
          <div class="flex items-center justify-center gap-2"><span class="inline-block h-2 w-2 rounded-full bg-primary-500"></span> Supported by MGLSD</div>
          <div class="flex items-center justify-center gap-2"><span class="inline-block h-2 w-2 rounded-full bg-primary-500"></span> Endorsed by UNICEF</div>
          <div class="flex items-center justify-center gap-2"><span class="inline-block h-2 w-2 rounded-full bg-primary-500"></span> ITU 116 Standard</div>
        </div>
      </div>
    </div>

    <!-- Bottom Bar -->
    <div>
      <div class="container-custom py-6">
        <div class="flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
          <p class="text-gray-400 text-sm text-center md:text-left">
            {{ settings.footer_text }}
          </p>
          <div class="flex space-x-6 text-sm">
            <router-link to="/privacy" class="text-gray-400 hover:text-white transition-colors">Privacy Policy</router-link>
            <router-link to="/terms" class="text-gray-400 hover:text-white transition-colors">Terms of Service</router-link>
            <router-link to="/accessibility" class="text-gray-400 hover:text-white transition-colors">Accessibility</router-link>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useContentStore } from '@/store/content'
import { useSettingsStore } from '@/store/settings'

const contentStore = useContentStore()
const settingsStore = useSettingsStore()
const currentYear = computed(() => new Date().getFullYear())

// Dynamic content from Content Store (Socials, Contacts)
const socialFacebook = computed(() => contentStore.getContent('social_facebook', 'https://www.facebook.com/Sauti116Helpline'))
const socialTwitter = computed(() => contentStore.getContent('social_twitter', 'https://x.com/sauti116'))
const socialWhatsapp = computed(() => contentStore.getContent('social_whatsapp', 'https://wa.me/256743889999'))
const socialUreport = computed(() => contentStore.getContent('social_ureport', 'https://ureport.in'))
const socialSafepal = computed(() => contentStore.getContent('social_safepal', 'https://www.unicef.org/uganda/safepal-app'))
const contactEmailInfo = computed(() => contentStore.getContent('contact_email_info', 'info@sauti.mglsd.go.ug'))
const contactEmailSautichl = computed(() => contentStore.getContent('contact_email_sautichl', 'sautichl@mglsd.go.ug'))
const contactWebsite = computed(() => contentStore.getContent('contact_website', 'https://sauti.mglsd.go.ug'))
const contactPhone = computed(() => contentStore.getContent('contact_phone_main', '116'))

// Dynamic content from Settings Store (Global Text)
const settings = computed(() => settingsStore.settings)

onMounted(() => {
  contentStore.fetchContent()
  settingsStore.fetchSettings()
})
</script>
