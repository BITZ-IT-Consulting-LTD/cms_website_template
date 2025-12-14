<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-b from-white via-white to-gray-50"></div>
      <div class="container-custom relative py-16 md:py-24">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
          <div class="lg:col-span-7">
            <h1 class="mb-4">{{ aboutHeroTitle }}</h1>
            <p class="text-xl max-w-2xl" style="color: #555555;">
              {{ aboutHeroSubtitle }}
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
              <h3 class="text-4xl font-extrabold mb-2">{{ aboutStat1Title }}</h3>
              <p class="text-white/90 text-sm font-medium">{{ aboutStat1Text }}</p>
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
              <h3 class="text-4xl font-extrabold mb-2">{{ aboutStat2Title }}</h3>
              <p class="text-white/90 text-sm font-medium">{{ aboutStat2Text }}</p>
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
              <h3 class="text-4xl font-extrabold mb-2">{{ aboutStat3Title }}</h3>
              <p class="text-white/90 text-sm font-medium">{{ aboutStat3Text }}</p>
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
              <h3 class="text-4xl font-extrabold mb-2">{{ aboutStat4Title }}</h3>
              <p class="text-white/90 text-sm font-medium">{{ aboutStat4Text }}</p>
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
            <h2 class="mb-3">{{ aboutMissionTitle }}</h2>
            <p class="leading-relaxed" style="color: #222222;">
              {{ aboutMissionText }}
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
                    <h4 class="font-bold text-gray-900 mb-2">{{ aboutService1Title }}</h4>
                    <p class="text-sm leading-relaxed" style="color: #555555;">{{ aboutService1Text }}</p>
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
                    <h4 class="font-bold text-gray-900 mb-2">{{ aboutService2Title }}</h4>
                    <p class="text-sm leading-relaxed" style="color: #555555;">{{ aboutService2Text }}</p>
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
                    <h4 class="font-bold text-gray-900 mb-2">{{ aboutService3Title }}</h4>
                    <p class="text-sm leading-relaxed" style="color: #555555;">{{ aboutService3Text }}</p>
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
                    <h4 class="font-bold text-gray-900 mb-2">{{ aboutService4Title }}</h4>
                    <p class="text-sm leading-relaxed" style="color: #555555;">{{ aboutService4Text }}</p>
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
                    <h4 class="font-bold text-gray-900 mb-2">{{ aboutService5Title }}</h4>
                    <p class="text-sm leading-relaxed" style="color: #555555;">{{ aboutService5Text }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div>
            <h2 class="mb-3">{{ aboutValuesTitle }}</h2>

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
        <h2 class="text-center mb-4">{{ aboutBackgroundTitle }}</h2>
        <div class="max-w-5xl mx-auto">
          <ul class="space-y-4 text-lg" style="color: #222222;">
            <li>{{ aboutBackgroundItem1 }}</li>
            <li>{{ aboutBackgroundItem2 }}</li>
            <li>{{ aboutBackgroundItem3 }}</li>
            <li>{{ aboutBackgroundItem4 }}</li>
            <li>{{ aboutBackgroundItem5 }}</li>
            <li>{{ aboutBackgroundItem6 }}</li>
          </ul>
          <p class="text-sm mt-6" style="color: #555555;">{{ aboutBackgroundNote }}</p>
        </div>
      </div>
    </section>

    <!-- Our Journey (Milestones) -->
    <section class="section-padding">
      <div class="container-custom">
        <Timeline />
      </div>
    </section>

    <!-- Operations -->
    <section class="section-padding">
      <div class="container-custom">
        <h2 class="mb-4">{{ aboutOperationsTitle }}</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-lg" style="color: #222222;">
          <div>
            <ul class="space-y-3">
              <li>{{ aboutOperationsItem1 }}</li>
              <li>{{ aboutOperationsItem2 }}</li>
              <li>{{ aboutOperationsItem3 }}</li>
              <li>{{ aboutOperationsItem4 }}</li>
            </ul>
          </div>
          <div class="hidden md:block"></div>
        </div>
      </div>
    </section>

    <!-- Path to Resolution (Case Flow) -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom">
        <h2 class="text-center mb-10">{{ aboutResolutionTitle }}</h2>
        <div class="max-w-3xl mx-auto">
          <div class="space-y-6">
            <div class="card p-5 text-center">
              <h3 class="text-xl font-bold" style="color: #222222;">{{ aboutResolutionCard1Title }}</h3>
              <p class="text-sm" style="color: #555555;">{{ aboutResolutionCard1Text }}</p>
            </div>
            <div class="text-center">⬇️</div>
            <div class="card p-5 text-center">
              <h3 class="text-xl font-bold" style="color: #222222;">{{ aboutResolutionCard2Title }}</h3>
            </div>
            <div class="text-center">⬇️</div>
            <div class="card p-5 text-center">
              <h3 class="text-xl font-bold" style="color: #222222;">{{ aboutResolutionCard3Title }}</h3>
            </div>
            <div class="text-center">⬇️</div>
            <div class="card p-5 text-center">
              <h3 class="text-xl font-bold" style="color: #226B5E;">{{ aboutResolutionCard4Title }}</h3>
              <p class="text-sm" style="color: #555555;">{{ aboutResolutionCard4Text }}</p>
            </div>
            <div class="text-center">⬇️</div>
            <div class="card p-5 text-center">
              <h3 class="text-xl font-bold" style="color: #222222;">{{ aboutResolutionCard5Title }}</h3>
              <p class="text-sm" style="color: #555555;">{{ aboutResolutionCard5Text }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Partners / Legitimacy -->
    <section class="section-padding">
      <div class="container-custom">
        <h2 class="text-center mb-8">{{ aboutPartnersTitle }}</h2>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 items-center">
          <div class="card p-6 text-center">{{ aboutPartner1 }}</div>
          <div class="card p-6 text-center">{{ aboutPartner2 }}</div>
          <div class="card p-6 text-center">{{ aboutPartner3 }}</div>
          <div class="card p-6 text-center">{{ aboutPartner4 }}</div>
        </div>
        <p class="text-center text-sm mt-6" style="color: #555555;">{{ aboutPartnersText }}</p>
      </div>
    </section>

    <!-- CTA -->
    <section class="section-padding">
      <div class="container-custom text-center">
        <h2 class="mb-3">{{ aboutCtaTitle }}</h2>
        <p class="max-w-2xl mx-auto" style="color: #555555;">{{ aboutCtaText }}</p>
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
import Timeline from '@/components/Timeline.vue' // Import the Timeline component

const contentStore = useContentStore()

// Get dynamic content
const aboutImage = computed(() => contentStore.getContent('about_image', sautiAboutpage))
const aboutHeroTitle = computed(() => contentStore.getContent('about_hero_title', 'About Sauti 116 helpline'))
const aboutHeroSubtitle = computed(() => contentStore.getContent('about_hero_subtitle', 'Free, confidential and accessible 24/7 across all telecoms. We protect and empower children, GBV survivors and migrant workers with rapid, compassionate support.'))
const aboutStat1Title = computed(() => contentStore.getContent('about_stat_1_title', '116'))
const aboutStat1Text = computed(() => contentStore.getContent('about_stat_1_text', 'Toll-free Hotline'))
const aboutStat2Title = computed(() => contentStore.getContent('about_stat_2_title', '24/7'))
const aboutStat2Text = computed(() => contentStore.getContent('about_stat_2_text', 'Always Available'))
const aboutStat3Title = computed(() => contentStore.getContent('about_stat_3_title', '26+'))
const aboutStat3Text = computed(() => contentStore.getContent('about_stat_3_text', 'Local Languages'))
const aboutStat4Title = computed(() => contentStore.getContent('about_stat_4_title', '100%'))
const aboutStat4Text = computed(() => contentStore.getContent('about_stat_4_text', 'National Coverage'))
const aboutMissionTitle = computed(() => contentStore.getContent('about_mission_title', 'Our Mission'))
const aboutMissionText = computed(() => contentStore.getContent('about_mission_text', 'To protect and empower vulnerable populations through accessible, confidential, and professional support services available 24/7.'))
const aboutService1Title = computed(() => contentStore.getContent('about_service_1_title', 'Telephone Counseling'))
const aboutService1Text = computed(() => contentStore.getContent('about_service_1_text', 'Immediate, confidential support via 116.'))
const aboutService2Title = computed(() => contentStore.getContent('about_service_2_title', 'Walk-in Support'))
const aboutService2Text = computed(() => contentStore.getContent('about_service_2_text', 'On-site help and rapid referrals.'))
const aboutService3Title = computed(() => contentStore.getContent('about_service_3_title', 'Media & U-Report'))
const aboutService3Text = computed(() => contentStore.getContent('about_service_3_text', 'Engagement via broadcast and U-Report 8500.'))
const aboutService4Title = computed(() => contentStore.getContent('about_service_4_title', 'Guidance & Referral'))
const aboutService4Text = computed(() => contentStore.getContent('about_service_4_text', 'Connections to specialized services.'))
const aboutService5Title = computed(() => contentStore.getContent('about_service_5_title', 'Community Sensitization'))
const aboutService5Text = computed(() => contentStore.getContent('about_service_5_text', 'Awareness and advocacy in communities nationwide.'))
const aboutValuesTitle = computed(() => contentStore.getContent('about_values_title', 'Core Values'))
const aboutBackgroundTitle = computed(() => contentStore.getContent('about_background_title', 'Background'))
const aboutBackgroundItem1 = computed(() => contentStore.getContent('about_background_item_1', 'In early 2013, MGLSD in partnership with UCRNN and UNICEF lobbied for 116 to be designated as a child helpline number.'))
const aboutBackgroundItem2 = computed(() => contentStore.getContent('about_background_item_2', 'August 2013, 116 was officially designated as an emergency and toll-free number by UCC.'))
const aboutBackgroundItem3 = computed(() => contentStore.getContent('about_background_item_3', 'On 4th November 2013, the first call was received by UCHL on the code 116.'))
const aboutBackgroundItem4 = computed(() => contentStore.getContent('about_background_item_4', 'In December 2014, government (MGLSD) took over the management of UCHL from UCRNN.'))
const aboutBackgroundItem5 = computed(() => contentStore.getContent('about_background_item_5', 'UCHL was instituted by law (Children’s Act cap 59 2016, as amended) section 42 C.'))
const aboutBackgroundItem6 = computed(() => contentStore.getContent('about_background_item_6', 'In 2021, GBV response was integrated into Sauti’s work.'))
const aboutBackgroundNote = computed(() => contentStore.getContent('about_background_note', 'Note: In October 2007, ITU asked all countries around the world to allocate 116 to Child Helplines.'))
const aboutJourneyTitle = computed(() => contentStore.getContent('about_journey_title', 'Our Journey'))
const aboutJourneySubtitle = computed(() => contentStore.getContent('about_journey_subtitle', 'Key milestones in our history of child advocacy and the national designation of 116.'))
const aboutJourneyItem1Year = computed(() => contentStore.getContent('about_journey_item_1_year', '2013'))
const aboutJourneyItem1Title = computed(() => contentStore.getContent('about_journey_item_1_title', 'Lobbying & Designation Effort'))
const aboutJourneyItem1Text = computed(() => contentStore.getContent('about_journey_item_1_text', 'MGLSD, with UCRNN and UNICEF, lobbied for 116 to be designated as Uganda’s child helpline number.'))
const aboutJourneyItem2Year = computed(() => contentStore.getContent('about_journey_item_2_year', 'Aug 2013'))
const aboutJourneyItem2Title = computed(() => contentStore.getContent('about_journey_item_2_title', 'Official Toll-Free Number'))
const aboutJourneyItem2Text = computed(() => contentStore.getContent('about_journey_item_2_text', 'UCC officially designated 116 as an emergency and toll-free number.'))
const aboutJourneyItem3Year = computed(() => contentStore.getContent('about_journey_item_3_year', 'Nov 2013'))
const aboutJourneyItem3Title = computed(() => contentStore.getContent('about_journey_item_3_title', 'First Call Received'))
const aboutJourneyItem3Text = computed(() => contentStore.getContent('about_journey_item_3_text', 'UCHL received the first call on code 116 on 4th November 2013.'))
const aboutJourneyItem4Year = computed(() => contentStore.getContent('about_journey_item_4_year', 'Dec 2014'))
const aboutJourneyItem4Title = computed(() => contentStore.getContent('about_journey_item_4_title', 'Government Takes Over'))
const aboutJourneyItem4Text = computed(() => contentStore.getContent('about_journey_item_4_text', 'MGLSD took over the management of UCHL from UCRNN.'))
const aboutJourneyItem5Year = computed(() => contentStore.getContent('about_journey_item_5_year', '2016'))
const aboutJourneyItem5Title = computed(() => contentStore.getContent('about_journey_item_5_title', 'Legal & Regulatory Framework'))
const aboutJourneyItem5Text = computed(() => contentStore.getContent('about_journey_item_5_text', 'UCHL instituted by law (Children’s Act cap 59 2016, as amended) section 42 C.'))
const aboutJourneyItem6Year = computed(() => contentStore.getContent('about_journey_item_6_year', '2021'))
const aboutJourneyItem6Title = computed(() => contentStore.getContent('about_journey_item_6_title', 'GBV Response Integrated'))
const aboutJourneyItem6Text = computed(() => contentStore.getContent('about_journey_item_6_text', 'Gender-based violence response integrated into Sauti’s work nationwide.'))
const aboutOperationsTitle = computed(() => contentStore.getContent('about_operations_title', 'Operations'))
const aboutOperationsItem1 = computed(() => contentStore.getContent('about_operations_item_1', 'Sauti is a Swahili word that means “voice”.'))
const aboutOperationsItem2 = computed(() => contentStore.getContent('about_operations_item_2', 'Operates on short code 116 (toll-free), accessible from any telecom network.'))
const aboutOperationsItem3 = computed(() => contentStore.getContent('about_operations_item_3', 'Operational 24/7 and accessible from every part of the country.'))
const aboutOperationsItem4 = computed(() => contentStore.getContent('about_operations_item_4', 'The counselors speak a total of 26 local languages.'))
const aboutResolutionTitle = computed(() => contentStore.getContent('about_resolution_title', 'Path to Resolution'))
const aboutResolutionCard1Title = computed(() => contentStore.getContent('about_resolution_card_1_title', 'Caller'))
const aboutResolutionCard1Text = computed(() => contentStore.getContent('about_resolution_card_1_text', 'Case reported'))
const aboutResolutionCard2Title = computed(() => contentStore.getContent('about_resolution_card_2_title', 'Call Center'))
const aboutResolutionCard3Title = computed(() => contentStore.getContent('about_resolution_card_3_title', 'Case Management Department'))
const aboutResolutionCard4Title = computed(() => contentStore.getContent('about_resolution_card_4_title', 'Probation Offices (DACs)'))
const aboutResolutionCard4Text = computed(() => contentStore.getContent('about_resolution_card_4_text', 'Supported by partners & CSOs, police, court, etc.'))
const aboutResolutionCard5Title = computed(() => contentStore.getContent('about_resolution_card_5_title', 'Local Leaders, CDOs, Para-Social Workers, VHTs, etc.'))
const aboutResolutionCard5Text = computed(() => contentStore.getContent('about_resolution_card_5_text', 'Feedback shared back through the chain.'))
const aboutPartnersTitle = computed(() => contentStore.getContent('about_partners_title', 'Partners & Affiliations'))
const aboutPartner1 = computed(() => contentStore.getContent('about_partner_1', 'MGLSD'))
const aboutPartner2 = computed(() => contentStore.getContent('about_partner_2', 'UNICEF'))
const aboutPartner3 = computed(() => contentStore.getContent('about_partner_3', 'UCRNN'))
const aboutPartner4 = computed(() => contentStore.getContent('about_partner_4', 'ITU 116'))
const aboutPartnersText = computed(() => contentStore.getContent('about_partners_text', 'Legally designated 116 child helpline; compliant with national and international standards.'))
const aboutCtaTitle = computed(() => contentStore.getContent('about_cta_title', 'Need help or ready to partner?'))
const aboutCtaText = computed(() => contentStore.getContent('about_cta_text', 'Reach out any time. Your call or message could change a life.'))


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
