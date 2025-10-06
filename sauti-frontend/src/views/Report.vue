<template>
  <div class="section-padding bg-gray-50">
    <div class="container-custom">
      <!-- Header -->
      <div class="text-center max-w-3xl mx-auto mb-12">
        <h1 class="mb-4">Report an Incident</h1>
        <p class="text-xl text-gray-600">
          Your voice is important. Let us help.
        </p>
      </div>

      <!-- Confidentiality Notice -->
      <div class="max-w-3xl mx-auto mb-8">
        <div class="bg-green-50 border border-green-100 p-6 rounded-2xl">
          <div class="flex items-start">
            <svg class="w-6 h-6 text-green-600 mt-1 mr-3 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/>
            </svg>
            <div>
              <p class="text-green-700">All information captured is confidential and will be handled with the utmost care.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Report Form -->
      <div class="max-w-3xl mx-auto">
        <ReportForm />
      </div>

      <!-- Footer links -->
      <div class="max-w-3xl mx-auto mt-12 text-center">
        <div class="text-sm text-gray-500">
          <router-link to="/privacy" class="hover:text-gray-700">Privacy Policy</router-link>
          <span class="mx-2">•</span>
          <router-link to="/terms" class="hover:text-gray-700">Terms of Service</router-link>
          <span class="mx-2">•</span>
          <router-link to="/contact" class="hover:text-gray-700">Contact Us</router-link>
          <p class="mt-2">© 2024 Sauti. All rights reserved. Your safety is our priority.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import ReportForm from '@/components/reports/ReportForm.vue'
</script>
