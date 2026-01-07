<template>
  <div class="bg-neutral-white min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <h1 class="page-header-title">Terms of Service</h1>
        <p class="page-header-subtitle">Terms and conditions for using our services</p>
        <div class="mt-8 flex justify-center">
          <div class="pill bg-primary/10 text-primary">Last updated: {{ lastUpdated }}</div>
        </div>
      </div>
    </header>

    <div class="container-custom section-padding">
      <div class="max-w-4xl mx-auto section-rhythm">
        <!-- Content Card -->
        <div class="bg-neutral-white p-6 md:p-16 rounded-[4rem] border-2 border-neutral-offwhite shadow-sm space-y-16">

          <!-- Terms in a Flash (Flash Pattern) -->
          <section class="bg-secondary/5 p-8 md:p-10 rounded-[2.5rem] border-2 border-secondary/10">
            <h2 class="campaign-header text-xl text-secondary mb-6 flex items-center gap-3">
              <ShieldCheckIcon class="w-6 h-6 text-secondary" />
              Terms in a Flash
            </h2>
            <ul class="space-y-4">
              <li class="flex items-start gap-4">
                <div class="w-2 h-2 bg-secondary rounded-full mt-2"></div>
                <p class="text-black font-bold"><strong>Zero Cost</strong>: All our services are 100% free to use.
                </p>
              </li>
              <li class="flex items-start gap-4">
                <div class="w-2 h-2 bg-secondary rounded-full mt-2"></div>
                <p class="text-black font-bold"><strong>Safety First</strong>: We only share info to stop immediate
                  harm.</p>
              </li>
              <li class="flex items-start gap-4">
                <div class="w-2 h-2 bg-secondary rounded-full mt-2"></div>
                <p class="text-black font-bold"><strong>Official Support</strong>: You are protected by Ugandan law
                  (MGLSD).</p>
              </li>
            </ul>
          </section>

          <!-- Section 1 -->
          <section aria-labelledby="acceptance-heading">
            <h2 id="acceptance-heading" class="campaign-header text-3xl text-secondary mb-8 flex items-center gap-4">
              <span class="w-1.5 h-8 bg-primary rounded-full"></span>
              1. Using Our Sanctuary
            </h2>
            <p class="text-black/80 font-bold text-lg leading-relaxed">
              By accessing and using the Sauti 116 helpline services, you accept and agree to be bound by the terms
              and provision of this agreement. If you do not agree to abide by the above, please do not use this
              service.
            </p>
          </section>

          <!-- Section 2 -->
          <section aria-labelledby="description-heading">
            <h2 id="description-heading" class="campaign-header text-3xl text-secondary mb-8 flex items-center gap-4">
              <span class="w-1.5 h-8 bg-hotline rounded-full"></span>
              2. What We Provide for You
            </h2>
            <p class="text-black font-bold mb-6 uppercase tracking-widest text-xs">Sauti 116 helpline
              provides:</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div v-for="service in services" :key="service"
                class="flex items-center gap-4 p-6 bg-neutral-offwhite/30 rounded-2xl border-2 border-transparent hover:border-hotline transition-all">
                <div class="w-2.5 h-2.5 bg-hotline rounded-full"></div>
                <span class="text-secondary font-bold text-sm uppercase tracking-wide">{{ service }}</span>
              </div>
            </div>
          </section>

          <!-- Section 3 -->
          <section aria-labelledby="responsibilities-heading">
            <h2 id="responsibilities-heading" class="campaign-header text-3xl text-secondary mb-8">3. Keeping Each Other
              Safe</h2>
            <div class="space-y-6">
              <div v-for="resp in responsibilities" :key="resp" class="flex items-start gap-6">
                <div
                  class="w-10 h-10 rounded-xl bg-primary/10 flex-shrink-0 flex items-center justify-center text-primary mt-1">
                  <CheckIcon class="w-6 h-6" />
                </div>
                <span class="text-secondary font-bold text-lg pt-1">{{ resp }}</span>
              </div>
            </div>
          </section>

          <!-- Section 4 -->
          <section aria-labelledby="confidentiality-heading">
            <h2 id="confidentiality-heading"
              class="campaign-header text-3xl text-secondary mb-8 flex items-center gap-4">
              <span class="w-1.5 h-8 bg-secondary-light rounded-full"></span>
              4. How We Protect Your Privacy
            </h2>
            <div class="bg-neutral-offwhite/30 p-10 rounded-[2.5rem] border-2 border-neutral-offwhite">
              <p class="text-black font-bold text-lg leading-relaxed mb-8">
                We are committed to maintaining the confidentiality of all information shared with us. However, we may
                be required to share information in the following circumstances:
              </p>
              <ul class="space-y-4">
                <li v-for="conf in confidentiality" :key="conf"
                  class="flex items-center gap-4 text-secondary font-bold text-sm uppercase tracking-wider">
                  <div class="w-2 h-2 bg-secondary-light rounded-full"></div>
                  {{ conf }}
                </li>
              </ul>
            </div>
          </section>

          <!-- Section 5 -->
          <section aria-labelledby="availability-heading">
            <h2 id="availability-heading" class="campaign-header text-3xl text-secondary mb-8 flex items-center gap-4">
              <span class="w-1.5 h-8 bg-primary rounded-full"></span>
              5. When You Can Reach Us
            </h2>
            <p class="text-black/80 font-bold text-lg leading-relaxed mb-10">
              While we strive to provide continuous service availability, we cannot guarantee that our services will be
              available at all times.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div v-for="rights in availabilityRights" :key="rights"
                class="p-8 bg-neutral-white border-2 border-neutral-offwhite rounded-3xl shadow-sm hover:border-primary transition-colors">
                <p class="text-black font-bold text-sm">{{ rights }}</p>
              </div>
            </div>
          </section>

          <!-- Section 6 -->
          <section aria-labelledby="emergency-heading">
            <h2 id="emergency-heading" class="campaign-header text-3xl text-emergency mb-8">6. Emergency Situations</h2>
            <div class="bg-emergency/5 p-10 rounded-[3rem] border-2 border-emergency/20 space-y-8">
              <p class="text-black font-bold text-xl">In case of immediate danger, please:</p>
              <div class="grid gap-4">
                <div v-for="step in emergencySteps" :key="step"
                  class="flex items-center gap-6 p-6 bg-neutral-white rounded-2xl border-2 border-emergency/10 shadow-sm">
                  <div
                    class="w-10 h-10 rounded-full bg-emergency text-neutral-white flex items-center justify-center font-bold flex-shrink-0">
                    !
                  </div>
                  <span class="text-secondary font-bold text-sm uppercase tracking-wide">{{ step }}</span>
                </div>
              </div>
            </div>
          </section>

          <!-- Section 7 -->
          <section aria-labelledby="contact-heading">
            <h2 id="contact-heading" class="campaign-header text-3xl text-secondary mb-8">7. Contact Information
            </h2>
            <div
              class="bg-primary/5 p-10 rounded-[3rem] border-2 border-primary/20 grid grid-cols-1 md:grid-cols-2 gap-10">
              <div class="space-y-8">
                <div class="flex items-center gap-6">
                  <div
                    class="w-14 h-14 bg-neutral-white rounded-2xl shadow-sm flex items-center justify-center text-emergency">
                    <PhoneIcon class="w-7 h-7" />
                  </div>
                  <div>
                    <p class="campaign-header text-[10px] text-black/50 mb-1">Helpline</p>
                    <p class="text-black font-bold text-2xl">116</p>
                  </div>
                </div>
                <div class="flex items-center gap-6">
                  <div
                    class="w-14 h-14 bg-neutral-white rounded-2xl shadow-sm flex items-center justify-center text-primary">
                    <EnvelopeIcon class="w-7 h-7" />
                  </div>
                  <div>
                    <p class="campaign-header text-[10px] text-black/50 mb-1">Support Admin</p>
                    <p class="text-black font-bold break-all">info@sauti.gov.ug</p>
                  </div>
                </div>
              </div>
              <div class="flex items-center gap-6">
                <div
                  class="w-14 h-14 bg-neutral-white rounded-2xl shadow-sm flex items-center justify-center text-primary">
                  <MapPinIcon class="w-7 h-7" />
                </div>
                <div>
                  <p class="campaign-header text-[10px] text-black/50 mb-1">Location</p>
                  <p class="text-black font-bold leading-tight">MGLSD Headquarters,<br />Kampala, Uganda</p>
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
    EnvelopeIcon,
    PhoneIcon,
    MapPinIcon,
    ArrowLeftIcon,
    ShieldCheckIcon
  } from '@heroicons/vue/24/outline'

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