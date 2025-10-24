<template>
  <footer class="bg-gray-900 text-white no-print">
    <!-- Main Footer Content -->
    <div class="container-custom py-12">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <!-- About Section -->
        <div>
          <h3 class="text-xl font-bold mb-4">Sauti</h3>
          <p class="text-gray-400 mb-4">
            Supporting children, GBV survivors, and migrant workers across Uganda with confidential helpline services.
          </p>
          <div class="flex space-x-4">
            <a href="https://facebook.com" target="_blank" rel="noopener" class="text-gray-400 hover:text-white transition-colors" aria-label="Facebook">
              <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
              </svg>
            </a>
            <a href="https://twitter.com" target="_blank" rel="noopener" class="text-gray-400 hover:text-white transition-colors" aria-label="Twitter">
              <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                <path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/>
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
            <li><router-link to="/blog" class="text-gray-400 hover:text-white transition-colors">News & Blog</router-link></li>
            <li><router-link to="/resources" class="text-gray-400 hover:text-white transition-colors">Resources</router-link></li>
            <li><router-link to="/partners" class="text-gray-400 hover:text-white transition-colors">Partners</router-link></li>
            <li><router-link to="/report" class="text-gray-400 hover:text-white transition-colors">Report a Case</router-link></li>
            <li><router-link to="/faqs" class="text-gray-400 hover:text-white transition-colors">FAQs</router-link></li>
            <li><router-link to="/privacy" class="text-gray-400 hover:text-white transition-colors">Privacy Policy</router-link></li>
            <li><router-link to="/terms" class="text-gray-400 hover:text-white transition-colors">Terms of Service</router-link></li>
          </ul>
        </div>

        <!-- Services / Channels -->
        <div>
          <h3 class="text-lg font-semibold mb-4">Get Help</h3>
          <ul class="space-y-2">
            <li><router-link to="/report" class="text-gray-400 hover:text-white transition-colors">Report a Case</router-link></li>
            <li><router-link to="/contact" class="text-gray-400 hover:text-white transition-colors">Contact Us</router-link></li>
            <li><a href="tel:116" class="text-gray-400 hover:text-white transition-colors">Call 116</a></li>
            <li><a href="https://wa.me/256123456789" target="_blank" class="text-gray-400 hover:text-white transition-colors">WhatsApp</a></li>
            <li><a href="https://ureport.in" target="_blank" class="text-gray-400 hover:text-white transition-colors">U-Report (SMS)</a></li>
            <li><a href="https://www.unicef.org/uganda/safepal-app" target="_blank" class="text-gray-400 hover:text-white transition-colors">SafePal App</a></li>
            <li><a href="mailto:info@sauti.mglsd.go.ug" class="text-gray-400 hover:text-white transition-colors">info@sauti.mglsd.go.ug</a></li>
            <li><a href="mailto:sautichildhelpline@gmail.com" class="text-gray-400 hover:text-white transition-colors">sautichildhelpline@gmail.com</a></li>
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
              <span>116 (Toll Free)</span>
            </li>
            <li class="flex items-start">
              <svg class="w-5 h-5 mr-2 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
              </svg>
              <span>info@sauti.mglsd.go.ug</span>
            </li>
            <li class="flex items-start">
              <svg class="w-5 h-5 mr-2 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
              </svg>
              <span>Ministry of Gender, Labour & Social Development, Kampala, Uganda</span>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Trust badges -->
    <div class="border-t border-gray-800">
      <div class="container-custom py-6">
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 text-center text-gray-400 text-sm">
          <div class="flex items-center justify-center gap-2"><span class="inline-block h-2 w-2 rounded-full bg-primary-500"></span> Supported by MGLSD</div>
          <div class="flex items-center justify-center gap-2"><span class="inline-block h-2 w-2 rounded-full bg-primary-500"></span> Endorsed by UNICEF</div>
          <div class="flex items-center justify-center gap-2"><span class="inline-block h-2 w-2 rounded-full bg-primary-500"></span> ITU 116 Standard</div>
        </div>
      </div>
    </div>

    <!-- Bottom Bar -->
    <div class="border-t border-gray-800">
      <div class="container-custom py-6">
        <div class="flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
          <p class="text-gray-400 text-sm text-center md:text-left">
            © {{ currentYear }} Sauti Child Helpline. All rights reserved. | Ministry of Gender, Labour & Social Development
          </p>
          <div class="flex space-x-6 text-sm">
            <a href="#" class="text-gray-400 hover:text-white transition-colors">Privacy Policy</a>
            <a href="#" class="text-gray-400 hover:text-white transition-colors">Terms of Service</a>
            <a href="#" class="text-gray-400 hover:text-white transition-colors">Accessibility</a>
          </div>
        </div>
        <p class="text-gray-500 text-xs text-center mt-4">
          Built with ❤️ by Sales Push Limited / Bitz ITC
        </p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { computed } from 'vue'

const currentYear = computed(() => new Date().getFullYear())
</script>
