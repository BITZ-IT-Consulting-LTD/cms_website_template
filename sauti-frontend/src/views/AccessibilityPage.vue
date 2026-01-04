<template>
  <div class="bg-sauti-white min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <h1 class="page-header-title">Accessibility Statement</h1>
        <p class="page-header-subtitle">Ensuring every child and citizen can access help, without barriers.</p>
        <div class="mt-8 flex justify-center">
          <div class="pill bg-sauti-blue/10 text-sauti-blue">Last updated: {{ lastUpdated }}</div>
        </div>
      </div>
    </header>

    <div class="container-custom section-padding">
      <div class="max-w-4xl mx-auto section-rhythm">
        <!-- Content Card -->
        <div class="bg-sauti-white p-10 md:p-16 rounded-[4rem] border-2 border-sauti-neutral shadow-sm space-y-16">

          <!-- Section 1 -->
          <section aria-labelledby="commitment-heading">
            <h2 id="commitment-heading"
              class="campaign-header text-3xl text-sauti-darkGreen mb-8 flex items-center gap-4">
              <span class="w-1.5 h-8 bg-sauti-blue rounded-full"></span>
              Our Commitment
            </h2>
            <p class="text-sauti-darkGreen/70 font-bold text-xl leading-relaxed">
              Sauti 116 helpline is committed to ensuring digital accessibility for all users, including those
              with disabilities. We strive to provide an accessible and inclusive experience for everyone who
              needs our services, adhering to the highest standards of universal design.
            </p>
          </section>

          <!-- Section 2 -->
          <section aria-labelledby="features-heading">
            <h2 id="features-heading"
              class="campaign-header text-3xl text-sauti-darkGreen mb-8 flex items-center gap-4">
              <span class="w-1.5 h-8 bg-sauti-orange rounded-full"></span>
              Accessibility Features
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div v-for="feature in accessibilityFeatures" :key="feature"
                class="flex items-center gap-4 p-5 bg-sauti-neutral/30 rounded-2xl border-2 border-transparent hover:border-sauti-orange transition-all group">
                <div
                  class="w-10 h-10 bg-sauti-orange/10 rounded-xl flex items-center justify-center text-sauti-orange shadow-sm group-hover:scale-110 transition-transform">
                  <CheckIcon class="w-6 h-6" />
                </div>
                <span class="text-sauti-darkGreen font-bold text-sm uppercase tracking-wide">{{ feature }}</span>
              </div>
            </div>
          </section>

          <!-- Section 3 -->
          <section aria-labelledby="helpline-heading">
            <h2 id="helpline-heading"
              class="campaign-header text-3xl text-sauti-darkGreen mb-8 flex items-center gap-4">
              <span class="w-1.5 h-8 bg-sauti-lightGreen rounded-full"></span>
              Helpline Accessibility
            </h2>
            <div class="bg-sauti-neutral/30 p-10 rounded-[2.5rem] border-2 border-sauti-neutral space-y-6">
              <div v-for="method in helplineMethods" :key="method" class="flex items-start gap-5">
                <div
                  class="w-10 h-10 rounded-xl bg-sauti-lightGreen/10 flex-shrink-0 flex items-center justify-center text-sauti-lightGreen mt-1">
                  <CheckCircleIcon class="w-6 h-6" />
                </div>
                <span class="text-sauti-darkGreen font-bold leading-tight text-lg pt-1">{{ method }}</span>
              </div>
            </div>
          </section>

          <!-- Section 4 -->
          <section aria-labelledby="standards-heading">
            <h2 id="standards-heading"
              class="campaign-header text-3xl text-sauti-darkGreen mb-8 flex items-center gap-4">
              <span class="w-1.5 h-8 bg-sauti-blue rounded-full"></span>
              Standards Compliance
            </h2>
            <div class="bg-sauti-white border-2 border-sauti-blue p-10 rounded-[3rem] shadow-sm">
              <p class="text-sauti-darkGreen font-bold text-lg leading-relaxed mb-10">
                We strictly aim to conform to the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA standards.
              </p>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
                <div v-for="standard in standards" :key="standard.title" class="space-y-3">
                  <h4 class="campaign-header text-sauti-blue text-[10px]">{{ standard.title }}</h4>
                  <p class="text-sauti-darkGreen font-bold text-xl leading-snug">{{ standard.desc }}</p>
                </div>
              </div>
            </div>
          </section>

          <!-- Section 5 -->
          <section aria-labelledby="feedback-heading">
            <h2 id="feedback-heading" class="campaign-header text-3xl text-sauti-darkGreen mb-6">Feedback and Support
            </h2>
            <p class="text-sauti-darkGreen/70 font-bold text-lg mb-10 leading-relaxed max-w-3xl">
              We welcome feedback on the accessibility of our services. If you encounter any barriers, please contact
              our accessibility coordinator.
            </p>
            <div
              class="bg-sauti-blue/5 p-10 rounded-[3rem] border-2 border-sauti-blue/20 grid grid-cols-1 md:grid-cols-2 gap-10">
              <div class="space-y-8">
                <div class="flex items-center gap-6">
                  <div
                    class="w-14 h-14 bg-sauti-white rounded-2xl shadow-sm flex items-center justify-center text-sauti-blue">
                    <EnvelopeIcon class="w-7 h-7" />
                  </div>
                  <div>
                    <p class="campaign-header text-[10px] text-sauti-darkGreen/50 mb-1">Coordinator Email</p>
                    <p class="text-sauti-darkGreen font-bold break-all">accessibility@sauti.gov.ug</p>
                  </div>
                </div>
                <div class="flex items-center gap-6">
                  <div
                    class="w-14 h-14 bg-sauti-white rounded-2xl shadow-sm flex items-center justify-center text-sauti-red">
                    <PhoneIcon class="w-7 h-7" />
                  </div>
                  <div>
                    <p class="campaign-header text-[10px] text-sauti-darkGreen/50 mb-1">Helpline</p>
                    <p class="text-sauti-darkGreen font-bold text-2xl">116</p>
                  </div>
                </div>
              </div>
              <div class="flex items-center gap-6">
                <div
                  class="w-14 h-14 bg-sauti-white rounded-2xl shadow-sm flex items-center justify-center text-sauti-blue">
                  <MapPinIcon class="w-7 h-7" />
                </div>
                <div>
                  <p class="campaign-header text-[10px] text-sauti-darkGreen/50 mb-1">Location</p>
                  <p class="text-sauti-darkGreen font-bold leading-tight">MGLSD, Plot 2,<br />Simbamanyo House, Kampala
                  </p>
                </div>
              </div>
            </div>
          </section>
        </div>

        <!-- Back to Home -->
        <div class="text-center">
          <BaseCTA href="/" variant="outline" class="inline-flex items-center gap-3">
            <ArrowLeftIcon class="w-5 h-5" />
            Back to Sanctuary
          </BaseCTA>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { computed } from 'vue'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import {
    CheckIcon,
    CheckCircleIcon,
    EnvelopeIcon,
    PhoneIcon,
    MapPinIcon,
    ArrowLeftIcon
  } from '@heroicons/vue/24/outline'

  defineOptions({
    name: 'AccessibilityPage'
  })

  const accessibilityFeatures = [
    'Keyboard navigation support',
    'Screen reader compatibility',
    'High contrast color schemes',
    'Resizable text and images',
    'Alternative text for images',
    'Clear and simple language',
    'Consistent navigation structure'
  ]

  const helplineMethods = [
    'Toll-free calling (116) from any phone',
    'WhatsApp messaging for text-based communication',
    'SMS services through U-Report',
    'Mobile app with accessibility features',
    'Multiple language support (English, Luganda, Swahili)'
  ]

  const standards = [
    { title: 'Perceivable', desc: 'Content with alternative formats' },
    { title: 'Operable', desc: 'Interface with keyboard and voice navigation' },
    { title: 'Understandable', desc: 'Information and interface consistency' },
    { title: 'Robust', desc: 'Compatible with assistive technologies' }
  ]

  const lastUpdated = computed(() => {
    return new Date().toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    })
  })
</script>
