<template>
  <div>
    <!-- Hero / reassurance banner -->
    <section class="relative overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-b from-white via-white to-gray-50"></div>
      <div class="container-custom relative py-12 md:py-16">
        <div class="max-w-3xl mx-auto text-center">
          <h1 class="mb-3">Report a Case</h1>
          <p class="text-lg md:text-xl text-gray-600">Free, confidential, and available 24/7. Your safety is our priority.</p>
          <div class="mt-4 flex flex-wrap justify-center gap-3 text-sm text-gray-600">
            <span class="badge-blue">Anonymous option</span>
            <span class="badge-orange">All telecoms</span>
            <span class="badge-teal">EN • LG • SW</span>
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
            <div class="card p-5 mb-6">
              <ol class="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm text-gray-600">
                <li class="flex items-start gap-3">
                  <span class="inline-flex h-8 w-8 items-center justify-center rounded-full bg-primary-100 text-gray-900 font-bold">1</span>
                  <div>
                    <p class="font-semibold text-gray-900">Fill in details</p>
                    <p>Provide as much as you can. Anonymous is okay.</p>
                  </div>
                </li>
                <li class="flex items-start gap-3">
                  <span class="inline-flex h-8 w-8 items-center justify-center rounded-full bg-primary-100 text-gray-900 font-bold">2</span>
                  <div>
                    <p class="font-semibold text-gray-900">Submit securely</p>
                    <p>Information is encrypted and confidential.</p>
                  </div>
                </li>
                <li class="flex items-start gap-3">
                  <span class="inline-flex h-8 w-8 items-center justify-center rounded-full bg-primary-100 text-gray-900 font-bold">3</span>
                  <div>
                    <p class="font-semibold text-gray-900">We follow up</p>
                    <p>Our team reviews and reaches out if needed.</p>
                  </div>
                </li>
              </ol>
            </div>

            <!-- Confidentiality Notice -->
            <div class="card p-5 mb-6">
              <div class="flex items-start">
                <svg class="w-6 h-6 text-green-600 mt-1 mr-3 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm-1-7a1 1 0 112 0v3a1 1 0 11-2 0v-3zm1-5a1 1 0 100 2 1 1 0 000-2z" clip-rule="evenodd" />
                </svg>
                <p class="text-green-700">All information is kept confidential and handled with care. You may choose to remain anonymous.</p>
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
          <aside class="lg:col-span-4">
            <div class="card p-5 mb-6">
              <h3 class="text-lg font-semibold mb-2">Need immediate help?</h3>
              <p class="text-gray-600">If you are in danger or need urgent assistance, call now.</p>
              <div class="mt-4 flex flex-wrap gap-2">
                <a href="tel:116" class="pill pill-primary" aria-label="Call the 116 helpline">Call 116</a>
                <a href="https://wa.me/256123456789" target="_blank" rel="noopener" class="pill pill-outline" aria-label="Chat on WhatsApp">WhatsApp</a>
              </div>
            </div>

            <div class="card p-5 mb-6">
              <h3 class="text-lg font-semibold mb-2">Other channels</h3>
              <ul class="space-y-2 text-gray-700 text-sm">
                <li>U-Report SMS: <strong>8500</strong></li>
                <li>SafePal App: <a href="https://www.unicef.org/uganda/safepal-app" target="_blank" rel="noopener" class="text-primary-600 hover:text-primary-700">Install</a></li>
                <li>Email: <a href="mailto:info@sauti.mglsd.go.ug" class="text-primary-600 hover:text-primary-700">info@sauti.mglsd.go.ug</a></li>
                <li>Email: <a href="mailto:sautichildhelpline@gmail.com" class="text-primary-600 hover:text-primary-700">sautichildhelpline@gmail.com</a></li>
              </ul>
            </div>

            <div class="card p-5">
              <h3 class="text-lg font-semibold mb-2">Privacy & Safety</h3>
              <p class="text-gray-600 text-sm">We never share your information without consent, unless required to prevent immediate harm. Read our <router-link to="/privacy" class="text-primary-600 hover:text-primary-700">Privacy Policy</router-link>.</p>
            </div>
          </aside>
        </div>
      </div>
    </section>

    <!-- Footer links -->
    <section class="pb-12">
      <div class="container-custom">
        <div class="max-w-5xl mx-auto text-center text-sm text-gray-500">
          <router-link to="/privacy" class="hover:text-gray-700">Privacy Policy</router-link>
          <span class="mx-2">•</span>
          <router-link to="/terms" class="hover:text-gray-700">Terms of Service</router-link>
          <span class="mx-2">•</span>
          <router-link to="/contact" class="hover:text-gray-700">Contact Us</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import ReportForm from '@/components/reports/ReportForm.vue'
</script>
