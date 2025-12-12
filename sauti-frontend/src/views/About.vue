<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-b from-white via-white to-gray-50"></div>
      <div class="container-custom relative py-16 md:py-24">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
          <div class="lg:col-span-7">
            <h1 class="mb-4">About Sauti 116 helpline</h1>
            <p class="text-xl max-w-2xl" style="color: #555555;">
              Uganda's national child helpline—free, confidential and accessible 24/7 across all telecoms.
              We protect and empower children, GBV survivors and migrant workers with rapid, compassionate support.
            </p>
            <div class="mt-6 flex flex-wrap gap-3">
              <a href="tel:116" class="pill pill-primary" aria-label="Call the 116 helpline">Call 116</a>
              <router-link to="/report" class="pill pill-outline">Report a Case</router-link>
            </div>
            <div class="mt-6 flex flex-wrap gap-3 text-sm" style="color: #555555;">
              <span class="badge-blue">24/7</span>
              <span class="badge-orange">All Telecoms</span>
              <span class="badge-teal">EN • LG • SW</span>
            </div>
          </div>
          <div class="lg:col-span-5">
            <div class="card p-0 overflow-hidden">
              <img :src="aboutImage" alt="About Sauti" class="w-full h-72 md:h-96 object-cover" />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Stats / At-a-glance -->
    <section class="section-padding">
      <div class="container-custom">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
          <!-- Stat Card 1 -->
          <div class="relative group">
            <div class="absolute inset-0 bg-gradient-to-br from-blue-500 to-blue-600 rounded-2xl opacity-90 group-hover:opacity-100 transition-opacity"></div>
            <div class="relative p-8 text-center text-white">
              <div class="mb-3">
                <svg class="w-12 h-12 mx-auto opacity-80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                </svg>
              </div>
              <h3 class="text-4xl font-extrabold mb-2">116</h3>
              <p class="text-white/90 text-sm font-medium">Toll-free Hotline</p>
            </div>
          </div>

          <!-- Stat Card 2 -->
          <div class="relative group">
            <div class="absolute inset-0 bg-gradient-to-br from-teal-500 to-teal-600 rounded-2xl opacity-90 group-hover:opacity-100 transition-opacity"></div>
            <div class="relative p-8 text-center text-white">
              <div class="mb-3">
                <svg class="w-12 h-12 mx-auto opacity-80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <h3 class="text-4xl font-extrabold mb-2">24/7</h3>
              <p class="text-white/90 text-sm font-medium">Always Available</p>
            </div>
          </div>

          <!-- Stat Card 3 -->
          <div class="relative group">
            <div class="absolute inset-0 bg-gradient-to-br from-orange-500 to-orange-600 rounded-2xl opacity-90 group-hover:opacity-100 transition-opacity"></div>
            <div class="relative p-8 text-center text-white">
              <div class="mb-3">
                <svg class="w-12 h-12 mx-auto opacity-80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129"/>
                </svg>
              </div>
              <h3 class="text-4xl font-extrabold mb-2">26+</h3>
              <p class="text-white/90 text-sm font-medium">Local Languages</p>
            </div>
          </div>

          <!-- Stat Card 4 -->
          <div class="relative group">
            <div class="absolute inset-0 bg-gradient-to-br from-purple-500 to-purple-600 rounded-2xl opacity-90 group-hover:opacity-100 transition-opacity"></div>
            <div class="relative p-8 text-center text-white">
              <div class="mb-3">
                <svg class="w-12 h-12 mx-auto opacity-80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <h3 class="text-4xl font-extrabold mb-2">100%</h3>
              <p class="text-white/90 text-sm font-medium">National Coverage</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Mission & Services -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 items-start">
          <div>
            <h2 class="mb-3">Our Mission</h2>
            <p class="leading-relaxed" style="color: #222222;">
              To protect and empower vulnerable populations through accessible, confidential, and
              professional support services available 24/7.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-6">
              <!-- Service 1 -->
              <div class="group bg-white rounded-xl p-6 shadow-md hover:shadow-xl transition-all duration-300 border border-gray-100 hover:border-blue-200">
                <div class="flex items-start gap-4">
                  <div class="flex-shrink-0 w-12 h-12 rounded-lg bg-blue-50 flex items-center justify-center group-hover:bg-blue-100 transition-colors">
                    <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                    </svg>
                  </div>
                  <div>
                    <h4 class="font-bold text-gray-900 mb-2">Telephone Counseling</h4>
                    <p class="text-sm leading-relaxed" style="color: #555555;">Immediate, confidential support via 116.</p>
                  </div>
                </div>
              </div>

              <!-- Service 2 -->
              <div class="group bg-white rounded-xl p-6 shadow-md hover:shadow-xl transition-all duration-300 border border-gray-100 hover:border-teal-200">
                <div class="flex items-start gap-4">
                  <div class="flex-shrink-0 w-12 h-12 rounded-lg bg-teal-50 flex items-center justify-center group-hover:bg-teal-100 transition-colors">
                    <svg class="w-6 h-6 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
                    </svg>
                  </div>
                  <div>
                    <h4 class="font-bold text-gray-900 mb-2">Walk-in Support</h4>
                    <p class="text-sm leading-relaxed" style="color: #555555;">On-site help and rapid referrals.</p>
                  </div>
                </div>
              </div>

              <!-- Service 3 -->
              <div class="group bg-white rounded-xl p-6 shadow-md hover:shadow-xl transition-all duration-300 border border-gray-100 hover:border-orange-200">
                <div class="flex items-start gap-4">
                  <div class="flex-shrink-0 w-12 h-12 rounded-lg bg-orange-50 flex items-center justify-center group-hover:bg-orange-100 transition-colors">
                    <svg class="w-6 h-6 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"/>
                    </svg>
                  </div>
                  <div>
                    <h4 class="font-bold text-gray-900 mb-2">Media & U-Report</h4>
                    <p class="text-sm leading-relaxed" style="color: #555555;">Engagement via broadcast and U-Report 8500.</p>
                  </div>
                </div>
              </div>

              <!-- Service 4 -->
              <div class="group bg-white rounded-xl p-6 shadow-md hover:shadow-xl transition-all duration-300 border border-gray-100 hover:border-purple-200">
                <div class="flex items-start gap-4">
                  <div class="flex-shrink-0 w-12 h-12 rounded-lg bg-purple-50 flex items-center justify-center group-hover:bg-purple-100 transition-colors">
                    <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/>
                    </svg>
                  </div>
                  <div>
                    <h4 class="font-bold text-gray-900 mb-2">Guidance & Referral</h4>
                    <p class="text-sm leading-relaxed" style="color: #555555;">Connections to specialized services.</p>
                  </div>
                </div>
              </div>

              <!-- Service 5 -->
              <div class="group bg-white rounded-xl p-6 shadow-md hover:shadow-xl transition-all duration-300 border border-gray-100 hover:border-green-200 sm:col-span-2">
                <div class="flex items-start gap-4">
                  <div class="flex-shrink-0 w-12 h-12 rounded-lg bg-green-50 flex items-center justify-center group-hover:bg-green-100 transition-colors">
                    <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
                    </svg>
                  </div>
                  <div>
                    <h4 class="font-bold text-gray-900 mb-2">Community Sensitization</h4>
                    <p class="text-sm leading-relaxed" style="color: #555555;">Awareness and advocacy in communities nationwide.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div>
            <h2 class="mb-3">Core Values</h2>

            <!-- Loading State -->
            <div v-if="loadingCoreValues" class="text-center py-8">
              <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
            </div>

            <!-- Core Values Grid -->
            <div v-else class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div
                v-for="value in coreValues"
                :key="value.id"
                class="group relative bg-gradient-to-br from-white rounded-2xl p-6 shadow-lg hover:shadow-2xl transition-all duration-300 border overflow-hidden"
                :class="`to-${value.color_from.split('-')[0]}-50/30 border-${value.border_color}/50`"
              >
                <div
                  class="absolute top-0 right-0 w-32 h-32 rounded-full -mr-16 -mt-16 group-hover:scale-150 transition-transform duration-500"
                  :class="`bg-${value.border_color}/20`"
                ></div>
                <div class="relative">
                  <div
                    class="inline-flex items-center justify-center h-14 w-14 rounded-xl bg-gradient-to-br text-white mb-4 shadow-lg"
                    :class="`from-${value.color_from} to-${value.color_to}`"
                  >
                    <component :is="getIconComponent(value.icon)" class="w-7 h-7" />
                  </div>
                  <h3 class="text-xl font-bold mb-3 text-gray-900">{{ value.title }}</h3>
                  <p class="text-sm leading-relaxed" style="color: #555555;">{{ value.description }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section removed: "How We Work Together" as per user request -->

    <!-- Background / Our Journey -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom">
        <h2 class="text-center mb-4">Background</h2>
        <div class="max-w-5xl mx-auto">
          <ul class="space-y-4 text-lg" style="color: #222222;">
            <li>In early 2013, MGLSD in partnership with UCRNN and UNICEF lobbied for 116 to be designated as a child helpline number.</li>
            <li>August 2013, 116 was officially designated as an emergency and toll‑free number by UCC.</li>
            <li>On 4th November 2013, the first call was received by UCHL on the code 116.</li>
            <li>In December 2014, government (MGLSD) took over the management of UCHL from UCRNN.</li>
            <li>UCHL was instituted by law (Children’s Act cap 59 2016, as amended) section 42 C.</li>
            <li>In 2021, GBV response was integrated into Sauti’s work.</li>
          </ul>
          <p class="text-sm mt-6" style="color: #555555;">Note: In October 2007, ITU asked all countries around the world to allocate 116 to Child Helplines.</p>
        </div>
      </div>
    </section>

    <!-- Our Journey (Milestones) -->
    <section class="section-padding">
      <div class="container-custom">
        <h2 class="text-center mb-4">Our Journey</h2>
        <p class="text-center mb-10" style="color: #555555;">Key milestones in our history of child advocacy and the national designation of 116.</p>
        <div class="relative max-w-5xl mx-auto py-8">
          <div class="timeline-line"></div>
          <!-- 2013 (Lobbying) -->
          <div class="timeline-item left">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm font-bold mb-2" style="color: #009EDB;">2013</h4>
              <h3 class="text-2xl font-bold mb-3" style="color: #222222;">Lobbying & Designation Effort</h3>
              <p class="leading-relaxed" style="color: #555555;">MGLSD, with UCRNN and UNICEF, lobbied for 116 to be designated as Uganda’s child helpline number.</p>
            </div>
          </div>
          <!-- Aug 2013 (UCC Designation) -->
          <div class="timeline-item right">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm font-bold mb-2" style="color: #009EDB;">Aug 2013</h4>
              <h3 class="text-2xl font-bold mb-3" style="color: #222222;">Official Toll‑Free Number</h3>
              <p class="leading-relaxed" style="color: #555555;">UCC officially designated 116 as an emergency and toll‑free number.</p>
            </div>
          </div>
          <!-- Nov 2013 (First Call) -->
          <div class="timeline-item left">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm font-bold mb-2" style="color: #009EDB;">Nov 2013</h4>
              <h3 class="text-2xl font-bold mb-3" style="color: #222222;">First Call Received</h3>
              <p class="leading-relaxed" style="color: #555555;">UCHL received the first call on code 116 on 4th November 2013.</p>
            </div>
          </div>
          <!-- Dec 2014 (Govt takeover) -->
          <div class="timeline-item right">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm font-bold mb-2" style="color: #009EDB;">Dec 2014</h4>
              <h3 class="text-2xl font-bold mb-3" style="color: #222222;">Government Takes Over</h3>
              <p class="leading-relaxed" style="color: #555555;">MGLSD took over the management of UCHL from UCRNN.</p>
            </div>
          </div>
          <!-- 2016 (Legal framework) -->
          <div class="timeline-item left">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm font-bold mb-2" style="color: #009EDB;">2016</h4>
              <h3 class="text-2xl font-bold mb-3" style="color: #222222;">Legal & Regulatory Framework</h3>
              <p class="leading-relaxed" style="color: #555555;">UCHL instituted by law (Children’s Act cap 59 2016, as amended) section 42 C.</p>
            </div>
          </div>
          <!-- 2021 (GBV Integration) -->
          <div class="timeline-item right">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm font-bold mb-2" style="color: #009EDB;">2021</h4>
              <h3 class="text-2xl font-bold mb-3" style="color: #222222;">GBV Response Integrated</h3>
              <p class="leading-relaxed" style="color: #555555;">Gender‑based violence response integrated into Sauti’s work nationwide.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Operations -->
    <section class="section-padding">
      <div class="container-custom">
        <h2 class="mb-4">Operations</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-lg" style="color: #222222;">
          <div>
            <ul class="space-y-3">
              <li>Sauti is a Swahili word that means “voice”.</li>
              <li>Operates on short code 116 (toll‑free), accessible from any telecom network.</li>
              <li>Operational 24/7 and accessible from every part of the country.</li>
              <li>The counselors speak a total of 26 local languages.</li>
            </ul>
          </div>
          <div class="hidden md:block"></div>
        </div>
      </div>
    </section>

    <!-- Path to Resolution (Case Flow) -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom">
        <h2 class="text-center mb-10">Path to Resolution</h2>
        <div class="max-w-3xl mx-auto">
          <div class="space-y-6">
            <div class="card p-5 text-center">
              <h3 class="text-xl font-bold" style="color: #222222;">Caller</h3>
              <p class="text-sm" style="color: #555555;">Case reported</p>
            </div>
            <div class="text-center">⬇️</div>
            <div class="card p-5 text-center">
              <h3 class="text-xl font-bold" style="color: #222222;">Call Center</h3>
            </div>
            <div class="text-center">⬇️</div>
            <div class="card p-5 text-center">
              <h3 class="text-xl font-bold" style="color: #222222;">Case Management Department</h3>
            </div>
            <div class="text-center">⬇️</div>
            <div class="card p-5 text-center">
              <h3 class="text-xl font-bold" style="color: #226B5E;">Probation Offices (DACs)</h3>
              <p class="text-sm" style="color: #555555;">Supported by partners & CSOs, police, court, etc.</p>
            </div>
            <div class="text-center">⬇️</div>
            <div class="card p-5 text-center">
              <h3 class="text-xl font-bold" style="color: #222222;">Local Leaders, CDOs, Para‑Social Workers, VHTs, etc.</h3>
              <p class="text-sm" style="color: #555555;">Feedback shared back through the chain.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Partners / Legitimacy -->
    <section class="section-padding">
      <div class="container-custom">
        <h2 class="text-center mb-8">Partners & Affiliations</h2>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 items-center">
          <div class="card p-6 text-center">MGLSD</div>
          <div class="card p-6 text-center">UNICEF</div>
          <div class="card p-6 text-center">UCRNN</div>
          <div class="card p-6 text-center">ITU 116</div>
        </div>
        <p class="text-center text-sm mt-6" style="color: #555555;">Legally designated 116 child helpline; compliant with national and international standards.</p>
      </div>
    </section>

    <!-- CTA -->
    <section class="section-padding">
      <div class="container-custom text-center">
        <h2 class="mb-3">Need help or ready to partner?</h2>
        <p class="max-w-2xl mx-auto" style="color: #555555;">Reach out any time. Your call or message could change a life.</p>
        <div class="mt-6 flex flex-wrap justify-center gap-3">
          <a href="tel:116" class="pill pill-primary">Call 116</a>
          <router-link to="/report" class="pill pill-outline">Report a Case</router-link>
          <router-link to="/contact" class="pill pill-light">Contact Us</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed, onMounted, ref, h } from 'vue'
import { useContentStore } from '@/store/content'
import { api } from '@/utils/axios'
import sautiAboutpage from '@/assets/sauti-aboutpage.webp'

const contentStore = useContentStore()

// Get dynamic content
const aboutImage = computed(() => contentStore.getContent('about_image', sautiAboutpage))

// Core Values
const coreValues = ref([])
const loadingCoreValues = ref(false)

// Icon components map
const getIconComponent = (iconName) => {
  const icons = {
    'lock': () => h('svg', { class: 'w-7 h-7', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z' })
    ]),
    'lightning': () => h('svg', { class: 'w-7 h-7', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M13 10V3L4 14h7v7l9-11h-7z' })
    ]),
    'heart': () => h('svg', { class: 'w-7 h-7', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z' })
    ]),
    'shield': () => h('svg', { class: 'w-7 h-7', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z' })
    ]),
    'users': () => h('svg', { class: 'w-7 h-7', fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z' })
    ])
  }

  return icons[iconName] || icons['shield']
}

// Fetch core values
const fetchCoreValues = async () => {
  loadingCoreValues.value = true
  try {
    const response = await api.get('/content/core-values/')
    coreValues.value = response.data
  } catch (error) {
    console.error('Failed to fetch core values:', error)
    coreValues.value = []
  } finally {
    loadingCoreValues.value = false
  }
}

onMounted(async () => {
  await contentStore.fetchContent()
  await fetchCoreValues()
})
</script>
