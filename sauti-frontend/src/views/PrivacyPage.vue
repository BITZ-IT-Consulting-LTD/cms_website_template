<template>
  <div class="min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <h1 class="page-header-title">Privacy Policy</h1>
        <p class="page-header-subtitle">How we protect your information and privacy</p>
        <div class="mt-8 flex justify-center">
          <div class="pill bg-primary/10 text-primary">Last updated: {{ lastUpdated }}</div>
        </div>
      </div>
    </header>

    <div class="container-custom section-padding">
      <div class="max-w-4xl mx-auto section-rhythm">
        <!-- Content Card -->
        <div class="bg-neutral-white p-6 md:p-16 rounded-[4rem] border-2 border-neutral-offwhite shadow-sm space-y-16">

          <!-- Quick Summary Block (The Flash Pattern) -->
          <section class="bg-primary/5 p-8 md:p-10 rounded-[2.5rem] border-2 border-primary/10">
            <h2 class="campaign-header text-xl text-primary mb-6 flex items-center gap-3">
              <ShieldCheckIcon class="w-6 h-6" />
              Privacy in a Flash
            </h2>
            <ul class="space-y-4">
              <li class="flex items-start gap-4">
                <div class="w-2 h-2 bg-primary rounded-full mt-2"></div>
                <p class="text-black font-bold"><strong>Your number is hidden</strong>: Calls to 116 will not show
                  on your phone bill.</p>
              </li>
              <li class="flex items-start gap-4">
                <div class="w-2 h-2 bg-primary rounded-full mt-2"></div>
                <p class="text-black font-bold"><strong>You can stay anonymous</strong>: We respect your right to
                  share only what you want.</p>
              </li>
              <li class="flex items-start gap-4">
                <div class="w-2 h-2 bg-primary rounded-full mt-2"></div>
                <p class="text-black font-bold"><strong>We are government experts</strong>: Your story is locked and
                  read only by protection teams.</p>
              </li>
            </ul>
          </section>

          <!-- Section 1 -->
          <section aria-labelledby="collect-heading">
            <h2 id="collect-heading" class="campaign-header text-3xl text-secondary mb-8 flex items-center gap-4">
              <span class="w-1.5 h-8 bg-primary rounded-full"></span>
              1. Information We Use to Help You
            </h2>
            <p class="text-black/80 font-bold text-lg leading-relaxed mb-8">
              We collect information you provide directly to us, such as when you:
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
              <div v-for="item in collectionMethods" :key="item"
                class="flex items-center gap-4 p-6 bg-neutral-offwhite/30 rounded-2xl border-2 border-transparent hover:border-primary transition-all">
                <div class="w-2.5 h-2.5 bg-primary rounded-full"></div>
                <span class="text-secondary font-bold text-sm uppercase tracking-wide">{{ item }}</span>
              </div>
            </div>
            <p class="text-black/60 font-bold italic text-base">
              This may include your name, contact information, location, and details about the situation you're
              reporting.
            </p>
          </section>

          <!-- Section 2 -->
          <section aria-labelledby="usage-heading">
            <h2 id="usage-heading" class="campaign-header text-3xl text-secondary mb-8 flex items-center gap-4">
              <span class="w-1.5 h-8 bg-hotline rounded-full"></span>
              2. How We Protect Your Story
            </h2>
            <div class="space-y-6">
              <div v-for="use in infoUsage" :key="use" class="flex items-start gap-6">
                <div
                  class="w-10 h-10 rounded-xl bg-primary/10 flex-shrink-0 flex items-center justify-center text-primary mt-1">
                  <CheckIcon class="w-6 h-6" />
                </div>
                <span class="text-secondary font-bold text-lg pt-1">{{ use }}</span>
              </div>
            </div>
          </section>

          <!-- Section 3 -->
          <section aria-labelledby="sharing-heading">
            <h2 id="sharing-heading" class="campaign-header text-3xl text-secondary mb-8 flex items-center gap-4">
              <span class="w-1.5 h-8 bg-secondary-light rounded-full"></span>
              3. When We Share Your Information
            </h2>
            <div class="bg-neutral-offwhite/30 p-10 rounded-[2.5rem] border-2 border-neutral-offwhite">
              <p class="text-black font-bold text-lg leading-relaxed mb-8">
                We do not share your personal information except in the following circumstances:
              </p>
              <ul class="space-y-4">
                <li v-for="sh in sharing" :key="sh"
                  class="flex items-center gap-4 text-secondary font-bold text-sm uppercase tracking-wider">
                  <div class="w-2 h-2 bg-secondary-light rounded-full"></div>
                  {{ sh }}
                </li>
              </ul>
            </div>
          </section>

          <!-- Section 4 -->
          <section aria-labelledby="security-heading">
            <h2 id="security-heading" class="campaign-header text-3xl text-secondary mb-8 flex items-center gap-4">
              <span class="w-1.5 h-8 bg-primary rounded-full"></span>
              4. Our Security Commitment
            </h2>
            <p class="text-black/80 font-bold text-lg leading-relaxed mb-10">
              We implement appropriate security measures to protect your information against unauthorized access,
              alteration, disclosure, or destruction.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div v-for="sec in security" :key="sec.title"
                class="p-8 bg-neutral-white border-2 border-neutral-offwhite rounded-3xl shadow-sm hover:border-primary transition-colors">
                <h4 class="campaign-header text-primary text-xs mb-3">{{ sec.title }}</h4>
                <p class="text-black font-bold">{{ sec.desc }}</p>
              </div>
            </div>
          </section>

          <!-- Section 5 -->
          <section aria-labelledby="rights-heading">
            <h2 id="rights-heading" class="campaign-header text-3xl text-secondary mb-10">5. Your Rights</h2>
            <div class="grid gap-4">
              <div v-for="right in rights" :key="right"
                class="flex items-center justify-between p-6 bg-neutral-offwhite/30 rounded-2xl border-2 border-transparent hover:border-primary transition-all group">
                <span class="text-secondary font-bold text-lg">{{ right }}</span>
                <CheckCircleIcon class="w-8 h-8 text-primary opacity-20 group-hover:opacity-100 transition-opacity" />
              </div>
            </div>
          </section>

          <!-- Section 6 -->
          <section aria-labelledby="contact-heading">
            <h2 id="contact-heading" class="campaign-header text-3xl text-secondary mb-8">6. Contact Us</h2>
            <p class="text-black/80 font-bold mb-10 text-lg leading-relaxed">
              If you have questions about this Privacy Policy or our data practices, please contact us:
            </p>
            <div
              class="bg-primary/5 p-10 rounded-[3rem] border-2 border-primary/20 grid grid-cols-1 md:grid-cols-2 gap-10">
              <div class="space-y-8">
                <div class="flex items-center gap-6">
                  <div
                    class="w-14 h-14 bg-neutral-white rounded-2xl shadow-sm flex items-center justify-center text-primary">
                    <EnvelopeIcon class="w-7 h-7" />
                  </div>
                  <div>
                    <p class="campaign-header text-[10px] text-black/50 mb-1">Privacy Admin</p>
                    <p class="text-black font-bold break-all">privacy@sauti.gov.ug</p>
                  </div>
                </div>
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

          <!-- Section 7 -->
          <section>
            <h2 class="campaign-header text-2xl text-secondary mb-6">7. Changes to This Policy</h2>
            <p class="text-black/60 font-bold leading-relaxed">
              We may update this Privacy Policy from time to time. We will notify you of any changes by posting
              the new Privacy Policy on this page and updating the "Last updated" date.
            </p>
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
    name: 'PrivacyPage'
  })

  const collectionMethods = [
    'Call our helpline (116)',
    'Submit reports through our website',
    'Contact us via official channels',
    'Use our mobile applications'
  ]

  const infoUsage = [
    'Provide immediate support and counseling',
    'Connect you with appropriate services',
    'Follow up on cases when necessary',
    'Improve our services and training',
    'Comply with legal requirements'
  ]

  const sharing = [
    'With your explicit consent',
    'When required by law to protect a child',
    'With authorized service providers who assist us',
    'In emergency situations where action is needed'
  ]

  const security = [
    { title: 'Encryption', desc: 'Secure data transmission and storage' },
    { title: 'Access Control', desc: 'Limited access to authorized personnel only' },
    { title: 'Audit', desc: 'Regular security and practice audits' },
    { title: 'Infrastructure', desc: 'Secure enterprise grade infrastructure' }
  ]

  const rights = [
    'Access your information',
    'Correct inaccuracies',
    'Request data deletion',
    'Withdraw consent',
    'File a complaint'
  ]

  const lastUpdated = computed(() => {
    return new Date().toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    })
  })
</script>