<template>
  <div class="section-padding">
    <div class="container-custom">
      <!-- Header -->
      <div class="text-center max-w-3xl mx-auto mb-12">
        <h1 class="mb-4">Report a Case</h1>
        <p class="text-xl text-gray-600">
          Your report will be handled confidentially by our trained professionals. 
          You can choose to remain anonymous.
        </p>
      </div>

      <!-- Confidentiality Notice -->
      <div class="max-w-3xl mx-auto mb-8">
        <div class="bg-primary-50 border-l-4 border-primary-500 p-6 rounded-lg">
          <div class="flex items-start">
            <svg class="w-6 h-6 text-primary-600 mt-1 mr-3 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/>
            </svg>
            <div>
              <h3 class="font-bold text-primary-900 mb-2">Your Privacy is Protected</h3>
              <ul class="text-primary-800 space-y-1 text-sm">
                <li>✓ All reports are encrypted and stored securely</li>
                <li>✓ You can submit anonymously</li>
                <li>✓ Your information will not be shared without your consent</li>
                <li>✓ You'll receive a reference number to track your report</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Report Form -->
      <ReportForm />

      <!-- Additional Help -->
      <div class="max-w-3xl mx-auto mt-12 text-center">
        <h3 class="text-xl font-bold text-gray-900 mb-4">Need Immediate Help?</h3>
        <p class="text-gray-600 mb-6">
          If you're in immediate danger, please call our emergency hotline:
        </p>
        <a href="tel:116" class="hotline-btn block mb-6">116</a>
        <div class="flex flex-wrap justify-center gap-4">
          <a href="https://wa.me/256123456789" target="_blank" class="btn-outline">
            WhatsApp Us
          </a>
          <router-link to="/contact" class="btn-outline">
            View All Contacts
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import ReportForm from '@/components/reports/ReportForm.vue'
</script>
