<template>
  <div class="bg-sauti-neutral py-16 md:py-24 min-h-screen">
    <div class="container-custom">
      <div class="max-w-4xl mx-auto">
        <!-- Header -->
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-5xl lg:text-6xl font-black text-sauti-darkGreen mb-4 tracking-tight">
            Terms of Service
          </h1>
          <p class="text-xl text-sauti-darkGreen/70 font-medium">Terms and conditions for using our services</p>
          <div class="mt-6 inline-flex items-center px-4 py-2 bg-sauti-blue/10 rounded-full">
            <p class="text-xs text-sauti-blue font-black uppercase tracking-widest">Last updated: {{ lastUpdated }}</p>
          </div>
        </div>

        <!-- Content -->
        <div class="bg-sauti-white p-8 md:p-12 rounded-[3.5rem] border border-sauti-neutral shadow-sm space-y-12">
          <section>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-6 flex items-center gap-3">
              <span class="w-3 h-3 bg-sauti-blue rounded-full"></span>
              1. Acceptance of Terms
            </h2>
            <p class="text-sauti-darkGreen/80 font-medium text-lg leading-relaxed">
              By accessing and using the Sauti 116 helpline services, you accept and agree to be bound by the terms
              and provision of this agreement. If you do not agree to abide by the above, please do not use this
              service.
            </p>
          </section>

          <section>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-6 flex items-center gap-3">
              <span class="w-3 h-3 bg-sauti-orange rounded-full"></span>
              2. Description of Service
            </h2>
            <p class="text-sauti-darkGreen font-bold mb-4">Sauti 116 helpline provides:</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div v-for="service in services" :key="service"
                class="flex items-center gap-3 p-4 bg-sauti-neutral/30 rounded-2xl border border-sauti-neutral">
                <div class="w-2 h-2 bg-sauti-orange rounded-full"></div>
                <span class="text-sauti-darkGreen font-bold">{{ service }}</span>
              </div>
            </div>
          </section>

          <section>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-6">3. User Responsibilities</h2>
            <div class="space-y-4">
              <div v-for="resp in responsibilities" :key="resp" class="flex items-start gap-3">
                <div
                  class="w-6 h-6 rounded-full bg-sauti-neutral flex-shrink-0 flex items-center justify-center text-sauti-darkGreen mt-1">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <span class="text-sauti-darkGreen font-bold text-lg">{{ resp }}</span>
              </div>
            </div>
          </section>

          <section>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-6 flex items-center gap-3">
              <span class="w-3 h-3 bg-sauti-lightGreen rounded-full"></span>
              4. Confidentiality
            </h2>
            <div class="bg-sauti-neutral/30 p-8 rounded-3xl border border-sauti-neutral">
              <p class="text-sauti-darkGreen/80 font-medium text-lg leading-relaxed mb-6">
                We are committed to maintaining the confidentiality of all information shared with us. However, we may
                be required to share information in the following circumstances:
              </p>
              <ul class="space-y-3">
                <li v-for="conf in confidentiality" :key="conf"
                  class="flex items-center gap-3 text-sauti-darkGreen font-bold">
                  <span class="w-1.5 h-1.5 bg-sauti-lightGreen rounded-full"></span>
                  {{ conf }}
                </li>
              </ul>
            </div>
          </section>

          <section>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-6 flex items-center gap-3">
              <span class="w-2 h-8 bg-sauti-blue rounded-full"></span>
              5. Service Availability
            </h2>
            <p class="text-sauti-darkGreen/80 font-medium text-lg leading-relaxed mb-6">
              While we strive to provide continuous service availability, we cannot guarantee that our services
              will be available at all times.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div v-for="rights in availabilityRights" :key="rights"
                class="p-4 bg-sauti-white border-2 border-sauti-neutral rounded-2xl">
                <p class="text-sauti-darkGreen font-bold">{{ rights }}</p>
              </div>
            </div>
          </section>

          <section>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-6 flex items-center gap-3">
              <span class="w-3 h-3 bg-sauti-red rounded-full"></span>
              6. Limitation of Liability
            </h2>
            <p class="text-sauti-darkGreen/80 font-medium text-lg leading-relaxed">
              Sauti 116 helpline and its partners are not liable for any direct, indirect, incidental, special,
              or consequential damages resulting from the use or inability to use our services.
            </p>
          </section>

          <section>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-red mb-6">7. Emergency Situations</h2>
            <div class="bg-sauti-red/5 p-8 rounded-3xl border-2 border-sauti-red/20 space-y-4">
              <p class="text-sauti-darkGreen font-black text-xl mb-4">In case of immediate danger, please:</p>
              <div v-for="step in emergencySteps" :key="step"
                class="flex items-center gap-4 text-sauti-darkGreen font-bold">
                <div
                  class="w-8 h-8 rounded-full bg-sauti-red text-sauti-white flex items-center justify-center font-black flex-shrink-0">
                  !
                </div>
                {{ step }}
              </div>
            </div>
          </section>

          <section>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-4">8. Contact Information</h2>
            <div
              class="bg-sauti-neutral p-8 rounded-[2.5rem] border-2 border-sauti-neutral shadow-inner grid grid-cols-1 md:grid-cols-2 gap-8">
              <div class="space-y-4">
                <div class="flex items-center gap-4">
                  <div
                    class="w-12 h-12 bg-sauti-white rounded-xl shadow-sm flex items-center justify-center text-sauti-red">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                    </svg>
                  </div>
                  <div>
                    <p class="text-xs uppercase tracking-widest text-sauti-darkGreen/50 font-black">Helpline</p>
                    <p class="text-sauti-darkGreen font-black text-xl">116 (Toll Free)</p>
                  </div>
                </div>
                <div class="flex items-center gap-4">
                  <div
                    class="w-12 h-12 bg-sauti-white rounded-xl shadow-sm flex items-center justify-center text-sauti-blue">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                    </svg>
                  </div>
                  <div>
                    <p class="text-xs uppercase tracking-widest text-sauti-darkGreen/50 font-black">Support Admin</p>
                    <p class="text-sauti-darkGreen font-bold break-all">info@sauti.gov.ug</p>
                  </div>
                </div>
              </div>
              <div class="flex items-center gap-4">
                <div
                  class="w-12 h-12 bg-sauti-white rounded-xl shadow-sm flex items-center justify-center text-sauti-blue">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                </div>
                <div>
                  <p class="text-xs uppercase tracking-widest text-sauti-darkGreen/50 font-black">Location</p>
                  <p class="text-sauti-darkGreen font-bold leading-tight">MGLSD, Kampala, Uganda</p>
                </div>
              </div>
            </div>
          </section>

          <section>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-4">9. Changes to Terms</h2>
            <p class="text-sauti-darkGreen/60 font-bold leading-relaxed">
              We reserve the right to modify these terms at any time. Changes will be posted on this page with
              an updated revision date. Continued use of our services constitutes acceptance of the modified terms.
            </p>
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
    name: 'TermsPage'
  })

  const services = [
    '24/7 confidential helpline (116)',
    'Online reporting & support',
    'Child protection resources',
    'Referrals to specialist services',
    'Counseling & guidance services'
  ]

  const responsibilities = [
    'Provide accurate & truthful information',
    'Use the service for legitimate purposes only',
    'Respect the confidentiality of other users',
    'No misuse or abuse of our services',
    'Report technical issues promptly'
  ]

  const confidentiality = [
    'Immediate risk of harm to a child',
    'When required by law or court order',
    'With your explicit consent',
    'Emergency situations requiring action'
  ]

  const availabilityRights = [
    'Suspension for maintenance',
    'Service modification or discontinuation',
    'Critical security implementations',
    'Response to technical outages'
  ]

  const emergencySteps = [
    'Call emergency services (999)',
    'Contact local police authorities',
    'Seek immediate medical attention',
    'Call 116 for further assistance'
  ]

  const lastUpdated = computed(() => {
    return new Date().toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    })
  })
</script>