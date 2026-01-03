<template>
  <div class="bg-neutral py-16 md:py-24 min-h-screen">
    <div class="container-custom">
      <div class="max-w-5xl mx-auto">
        <!-- Header -->
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-5xl lg:text-7xl font-black text-darkGreen mb-6 tracking-tight">
            Accessibility <span class="text-blue">Statement</span>
          </h1>
          <p class="text-xl md:text-2xl text-darkGreen/70 font-bold max-w-3xl mx-auto leading-relaxed">
            Ensuring every child and citizen can access help, without barriers.
          </p>
          <div
            class="mt-10 inline-flex items-center px-6 py-2 bg-blue/10 rounded-2xl border-2 border-blue/20">
            <p class="text-[10px] text-blue font-black uppercase tracking-widest">Last updated: {{ lastUpdated }}
            </p>
          </div>
        </div>

        <!-- Content -->
        <div
          class="bg-white p-10 md:p-20 rounded-[4rem] border-2 border-neutral shadow-2xl shadow-darkGreen/5 space-y-20">
          <section>
            <h2 class="text-3xl md:text-4xl font-black text-darkGreen mb-8 flex items-center gap-4">
              <span class="w-2 h-10 bg-blue rounded-full"></span>
              Our Commitment
            </h2>
            <p class="text-darkGreen/70 font-bold text-xl leading-relaxed max-w-4xl">
              Sauti 116 helpline is committed to ensuring digital accessibility for all users, including those
              with disabilities. We strive to provide an accessible and inclusive experience for everyone who
              needs our services, adhering to the highest standards of universal design.
            </p>
          </section>

          <section>
            <h2 class="text-3xl md:text-4xl font-black text-darkGreen mb-8 flex items-center gap-4">
              <span class="w-2 h-10 bg-orange rounded-full"></span>
              Accessibility Features
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div v-for="feature in accessibilityFeatures" :key="feature"
                class="flex items-center gap-4 p-6 bg-neutral/30 rounded-3xl border-2 border-neutral transition-all hover:bg-white hover:border-orange group">
                <div
                  class="w-10 h-10 bg-white rounded-xl flex items-center justify-center text-orange shadow-sm group-hover:scale-110 transition-transform">
                  <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                      clip-rule="evenodd" />
                  </svg>
                </div>
                <span class="text-darkGreen font-black text-lg">{{ feature }}</span>
              </div>
            </div>
          </section>

          <section>
            <h2 class="text-3xl md:text-4xl font-black text-darkGreen mb-8 flex items-center gap-4">
              <span class="w-2 h-10 bg-lightGreen rounded-full"></span>
              Helpline Accessibility
            </h2>
            <div class="bg-neutral/10 p-10 rounded-[3rem] border-2 border-neutral space-y-6">
              <div v-for="method in helplineMethods" :key="method" class="flex items-start gap-5">
                <div
                  class="w-8 h-8 rounded-xl bg-lightGreen flex-shrink-0 flex items-center justify-center text-white mt-1 shadow-lg shadow-lightGreen/20">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <span class="text-darkGreen font-bold leading-tight text-xl">{{ method }}</span>
              </div>
            </div>
          </section>

          <section>
            <h2 class="text-3xl md:text-4xl font-black text-darkGreen mb-8 flex items-center gap-4">
              <span class="w-2 h-10 bg-blue rounded-full"></span>
              Standards Compliance
            </h2>
            <div class="bg-blue/5 p-10 rounded-[3rem] border-2 border-blue/10">
              <p class="text-darkGreen font-bold text-xl leading-relaxed mb-10">
                We strictly aim to conform to the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA standards.
              </p>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
                <div v-for="standard in standards" :key="standard.title" class="space-y-3">
                  <h4 class="text-blue font-black uppercase tracking-[0.2em] text-[10px]">{{ standard.title }}
                  </h4>
                  <p class="text-darkGreen font-black text-xl leading-snug">{{ standard.desc }}</p>
                </div>
              </div>
            </div>
          </section>

          <section>
            <h2 class="text-3xl font-black text-darkGreen mb-6">Feedback and Support</h2>
            <p class="text-darkGreen/70 font-bold text-lg mb-10 leading-relaxed max-w-3xl">
              We welcome feedback on the accessibility of our services. If you encounter any barriers, please contact
              our accessibility coordinator.
            </p>
            <div
              class="bg-neutral p-10 rounded-[3rem] border-2 border-neutral grid grid-cols-1 md:grid-cols-2 gap-10">
              <div class="space-y-8">
                <div class="flex items-center gap-5">
                  <div
                    class="w-14 h-14 bg-white rounded-2xl shadow-xl flex items-center justify-center text-blue">
                    <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                        d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                    </svg>
                  </div>
                  <div>
                    <p class="text-[10px] uppercase tracking-widest text-darkGreen/40 font-black mb-1">Coordinator
                      Email</p>
                    <p class="text-darkGreen font-black text-lg break-all">accessibility@sauti.gov.ug</p>
                  </div>
                </div>
                <div class="flex items-center gap-5">
                  <div
                    class="w-14 h-14 bg-white rounded-2xl shadow-xl flex items-center justify-center text-red">
                    <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                        d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                    </svg>
                  </div>
                  <div>
                    <p class="text-[10px] uppercase tracking-widest text-darkGreen/40 font-black mb-1">Helpline
                    </p>
                    <p class="text-red font-black text-3xl tracking-tighter">116</p>
                  </div>
                </div>
              </div>
              <div class="flex items-center gap-5">
                <div
                  class="w-14 h-14 bg-white rounded-2xl shadow-xl flex items-center justify-center text-blue">
                  <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                      d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                      d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                </div>
                <div>
                  <p class="text-[10px] uppercase tracking-widest text-darkGreen/40 font-black mb-1">Address</p>
                  <p class="text-darkGreen font-black text-xl leading-tight">MGLSD, Plot 2, Simbamanyo House,
                    Kampala</p>
                </div>
              </div>
            </div>
          </section>
        </div>

        <!-- Back to Home -->
        <div class="text-center mt-16">
          <router-link to="/" class="btn btn-outline inline-flex items-center gap-3">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M11 15l-3-3m0 0l3-3m-3 3h8M3 12a9 9 0 1118 0 9 9 0 01-18 0z" />
            </svg>
            Back to Sanctuary
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { computed } from 'vue'

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
