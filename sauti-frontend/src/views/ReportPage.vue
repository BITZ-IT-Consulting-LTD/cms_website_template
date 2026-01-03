<template>
  <div class="bg-sauti-neutral min-h-screen">
    <!-- Hero / reassurance banner -->
    <section class="relative overflow-hidden pt-16 md:pt-24 pb-8">
      <div class="container-custom relative">
        <div class="max-w-4xl mx-auto text-center">
          <h1 class="text-4xl md:text-5xl lg:text-7xl font-black text-sauti-darkGreen mb-6 tracking-tight">Report a
            <span class="text-sauti-blue">Case</span></h1>
          <p class="text-xl md:text-2xl text-sauti-darkGreen/70 font-bold max-w-2xl mx-auto leading-relaxed">
            Protecting our future, together. Your report is free, confidential, and handled with absolute urgency.
          </p>
          <div class="mt-10 flex flex-wrap justify-center gap-4">
            <div
              class="px-6 py-2 bg-sauti-blue/10 text-sauti-blue rounded-2xl border-2 border-sauti-blue/20 font-black uppercase tracking-widest text-xs">
              Anonymous option</div>
            <div
              class="px-6 py-2 bg-sauti-orange/10 text-sauti-orange rounded-2xl border-2 border-sauti-orange/20 font-black uppercase tracking-widest text-xs">
              All Uganda Networks</div>
            <div
              class="px-6 py-2 bg-sauti-lightGreen/10 text-sauti-lightGreen rounded-2xl border-2 border-sauti-lightGreen/20 font-black uppercase tracking-widest text-xs">
              EN • LG • SW • LS</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Two-column layout: form + help panel -->
    <section class="section-padding">
      <div class="container-custom">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <!-- Left: Form card -->
          <div class="lg:col-span-8">
            <!-- Stepper / how it works -->
            <div class="bg-sauti-white rounded-[2.5rem] border-2 border-sauti-neutral p-8 mb-8 shadow-sm">
              <ol class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <li class="flex flex-col md:items-center md:text-center gap-4">
                  <span
                    class="inline-flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-sauti-blue text-sauti-white font-black text-xl shadow-lg shadow-sauti-blue/20">1</span>
                  <div>
                    <p class="font-black text-sauti-darkGreen text-lg">Fill in details</p>
                    <p class="font-bold text-sauti-darkGreen/50 text-sm mt-2">Provide as much as you can. Anonymous
                      reports are welcome.</p>
                  </div>
                </li>
                <li class="flex flex-col md:items-center md:text-center gap-4">
                  <span
                    class="inline-flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-sauti-orange text-sauti-white font-black text-xl shadow-lg shadow-sauti-orange/20">2</span>
                  <div>
                    <p class="font-black text-sauti-darkGreen text-lg">Submit securely</p>
                    <p class="font-bold text-sauti-darkGreen/50 text-sm mt-2">Information is encrypted and strictly
                      confidential.</p>
                  </div>
                </li>
                <li class="flex flex-col md:items-center md:text-center gap-4">
                  <span
                    class="inline-flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-sauti-lightGreen text-sauti-white font-black text-xl shadow-lg shadow-sauti-lightGreen/20">3</span>
                  <div>
                    <p class="font-black text-sauti-darkGreen text-lg">We follow up</p>
                    <p class="font-bold text-sauti-darkGreen/50 text-sm mt-2">Our team of experts reviews and initiates
                      action immediately.</p>
                  </div>
                </li>
              </ol>
            </div>

            <!-- Confidentiality Notice -->
            <div class="bg-sauti-lightGreen/10 border border-sauti-lightGreen/20 rounded-3xl p-6 mb-6">
              <div class="flex items-start">
                <svg class="w-6 h-6 text-sauti-lightGreen mt-0.5 mr-3 flex-shrink-0" fill="currentColor"
                  viewBox="0 0 20 20" aria-hidden="true">
                  <path fill-rule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zm-1-7a1 1 0 112 0v3a1 1 0 11-2 0v-3zm1-5a1 1 0 100 2 1 1 0 000-2z"
                    clip-rule="evenodd" />
                </svg>
                <p class="text-sauti-darkGreen font-bold">All information is kept confidential and handled with care.
                  You may choose to remain anonymous.</p>
              </div>
            </div>

            <!-- Report Form -->
            <div class="card p-0">
              <div class="card-body">
                <ReportForm />
              </div>
            </div>
          </div>

          <!-- Right: Help / alternative channels -->
          <aside class="lg:col-span-4 space-y-6">
            <div class="bg-sauti-white rounded-3xl border border-sauti-neutral p-6 shadow-sm">
              <h3 class="text-xl font-bold text-sauti-darkGreen mb-3">Need immediate help?</h3>
              <p class="text-sauti-darkGreen/80 font-medium">If you are in danger or need urgent assistance, call now.
              </p>
              <div class="mt-6 flex flex-col gap-3">
                <a href="tel:116" class="btn btn-emergency w-full text-center" aria-label="Call the 116 helpline">Call
                  116</a>
                <a href="https://wa.me/256743889999" target="_blank" rel="noopener"
                  class="btn btn-outline w-full text-center" aria-label="Chat on WhatsApp">WhatsApp</a>
              </div>
            </div>

            <div class="bg-sauti-white rounded-3xl border border-sauti-neutral p-6 shadow-sm">
              <h3 class="text-xl font-bold text-sauti-darkGreen mb-3">Other channels</h3>
              <ul class="space-y-3 text-sauti-darkGreen font-medium text-sm">
                <li class="flex justify-between items-center bg-sauti-neutral p-3 rounded-xl">
                  <span>U-Report SMS:</span>
                  <strong class="text-sauti-blue">8500</strong>
                </li>
                <li>SafePal App: <a href="https://www.unicef.org/uganda/safepal-app" target="_blank" rel="noopener"
                    class="text-sauti-blue hover:underline">Install</a></li>
                <li>Email: <a href="mailto:info@sauti.mglsd.go.ug"
                    class="text-sauti-blue hover:underline">info@sauti.mglsd.go.ug</a></li>
                <li>Email: <a href="mailto:sautichildhelpline@gmail.com"
                    class="text-sauti-blue hover:underline">sautichildhelpline@gmail.com</a></li>
              </ul>
            </div>

            <div class="bg-sauti-darkGreen rounded-3xl p-6 shadow-xl text-sauti-white">
              <h3 class="text-xl font-bold mb-3">Privacy & Safety</h3>
              <p class="text-sm opacity-90 leading-relaxed font-medium">We never share your information without consent,
                unless required to prevent immediate harm. Read our <router-link to="/privacy"
                  class="text-sauti-blue hover:text-sauti-orange font-bold">Privacy Policy</router-link>.</p>
            </div>
          </aside>
        </div>
      </div>
    </section>

    <!-- Footer links -->
    <section class="pb-16">
      <div class="container-custom">
        <div
          class="max-w-5xl mx-auto py-8 border-t-2 border-sauti-neutral flex flex-wrap justify-center items-center gap-6 text-sm font-black text-sauti-darkGreen/40 uppercase tracking-widest">
          <router-link to="/privacy" class="hover:text-sauti-blue transition-colors">Privacy Policy</router-link>
          <span class="w-1.5 h-1.5 bg-sauti-neutral rounded-full"></span>
          <router-link to="/terms" class="hover:text-sauti-blue transition-colors">Terms of Service</router-link>
          <span class="w-1.5 h-1.5 bg-sauti-neutral rounded-full"></span>
          <router-link to="/contact" class="hover:text-sauti-blue transition-colors">Contact Us</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
  defineOptions({
    name: 'ReportPage'
  })
  import ReportForm from '@/components/reports/ReportForm.vue'
</script>
