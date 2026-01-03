<template>
  <div class="bg-sauti-neutral py-16 md:py-24 min-h-screen">
    <div class="container-custom">
      <div class="max-w-4xl mx-auto">
        <!-- Header -->
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-5xl lg:text-6xl font-black text-sauti-darkGreen mb-4 tracking-tight">
            Privacy Policy
          </h1>
          <p class="text-xl text-sauti-darkGreen/70 font-medium">How we protect your information and privacy</p>
          <div class="mt-6 inline-flex items-center px-4 py-2 bg-sauti-blue/10 rounded-full">
            <p class="text-xs text-sauti-blue font-black uppercase tracking-widest">Last updated: {{ lastUpdated }}</p>
          </div>
        </div>

        <!-- Content -->
        <div class="bg-sauti-white p-8 md:p-12 rounded-[3.5rem] border border-sauti-neutral shadow-sm space-y-12">
          <section>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-6 flex items-center gap-3">
              <span class="w-3 h-3 bg-sauti-blue rounded-full"></span>
              1. Information We Collect
            </h2>
            <p class="text-sauti-darkGreen/80 font-medium text-lg leading-relaxed mb-6">
              We collect information you provide directly to us, such as when you:
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
              <div v-for="item in collectionMethods" :key="item"
                class="flex items-center gap-3 p-4 bg-sauti-neutral/30 rounded-2xl border border-sauti-neutral">
                <div class="w-2 h-2 bg-sauti-blue rounded-full"></div>
                <span class="text-sauti-darkGreen font-bold">{{ item }}</span>
              </div>
            </div>
            <p class="text-sauti-darkGreen/60 font-medium italic">
              This may include your name, contact information, location, and details about the situation you're
              reporting.
            </p>
          </section>

          <section>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-6 flex items-center gap-3">
              <span class="w-3 h-3 bg-sauti-orange rounded-full"></span>
              2. How We Use Your Information
            </h2>
            <div class="space-y-4">
              <div v-for="use in infoUsage" :key="use" class="flex items-start gap-3">
                <div
                  class="w-6 h-6 rounded-full bg-sauti-neutral flex-shrink-0 flex items-center justify-center text-sauti-darkGreen mt-1">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <span class="text-sauti-darkGreen font-bold text-lg">{{ use }}</span>
              </div>
            </div>
          </section>

          <section>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-6 flex items-center gap-3">
              <span class="w-3 h-3 bg-sauti-lightGreen rounded-full"></span>
              3. Information Sharing
            </h2>
            <div class="bg-sauti-neutral/30 p-8 rounded-3xl border border-sauti-neutral">
              <p class="text-sauti-darkGreen/80 font-medium text-lg leading-relaxed mb-6">
                We do not share your personal information except in the following circumstances:
              </p>
              <ul class="space-y-3">
                <li v-for="sh in sharing" :key="sh" class="flex items-center gap-3 text-sauti-darkGreen font-bold">
                  <span class="w-1.5 h-1.5 bg-sauti-lightGreen rounded-full"></span>
                  {{ sh }}
                </li>
              </ul>
            </div>
          </section>

          <section>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-6 flex items-center gap-3">
              <span class="w-2 h-8 bg-sauti-blue rounded-full"></span>
              4. Data Security
            </h2>
            <p class="text-sauti-darkGreen/80 font-medium text-lg leading-relaxed mb-8">
              We implement appropriate security measures to protect your information against unauthorized access,
              alteration, disclosure, or destruction.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div v-for="sec in security" :key="sec.title"
                class="p-6 bg-sauti-white border-2 border-sauti-neutral rounded-3xl shadow-sm">
                <h4 class="text-sauti-blue font-black uppercase tracking-widest text-xs mb-2">{{ sec.title }}</h4>
                <p class="text-sauti-darkGreen font-bold">{{ sec.desc }}</p>
              </div>
            </div>
          </section>

          <section>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-8">5. Your Rights</h2>
            <div class="grid gap-4">
              <div v-for="right in rights" :key="right"
                class="group flex items-center justify-between p-6 bg-sauti-neutral/10 hover:bg-sauti-blue/5 rounded-3xl border border-sauti-neutral hover:border-sauti-blue transition-all duration-300">
                <span class="text-sauti-darkGreen font-black text-lg">{{ right }}</span>
                <svg class="w-6 h-6 text-sauti-darkGreen/20 group-hover:text-sauti-blue transition-colors" fill="none"
                  stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
            </div>
          </section>

          <section>
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-4">6. Contact Us</h2>
            <p class="text-sauti-darkGreen/80 font-medium mb-8 leading-relaxed">
              If you have questions about this Privacy Policy or our data practices, please contact us:
            </p>
            <div
              class="bg-sauti-neutral p-8 rounded-[2.5rem] border-2 border-sauti-neutral shadow-inner grid grid-cols-1 md:grid-cols-2 gap-8">
              <div class="space-y-4">
                <div class="flex items-center gap-4">
                  <div
                    class="w-12 h-12 bg-sauti-white rounded-xl shadow-sm flex items-center justify-center text-sauti-blue">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                    </svg>
                  </div>
                  <div>
                    <p class="text-xs uppercase tracking-widest text-sauti-darkGreen/50 font-black">Privacy Admin</p>
                    <p class="text-sauti-darkGreen font-bold break-all">privacy@sauti.gov.ug</p>
                  </div>
                </div>
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
            <h2 class="text-2xl md:text-3xl font-black text-sauti-darkGreen mb-4">7. Changes to This Policy</h2>
            <p class="text-sauti-darkGreen/60 font-bold leading-relaxed">
              We may update this Privacy Policy from time to time. We will notify you of any changes by posting
              the new Privacy Policy on this page and updating the "Last updated" date.
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
  defineOptions({
    name: 'PrivacyPage'
  })
  import { computed } from 'vue'

  const collectionMethods = [
    'Call our helpline (116)',
    'Submit reports through our website',
    'Contact us via email or WhatsApp',
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