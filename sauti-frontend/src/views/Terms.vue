<template>
  <div class="bg-white py-16">
    <div class="container-custom">
      <div class="max-w-4xl mx-auto">
        <!-- Header -->
        <div class="text-center mb-12">
          <h1 class="text-4xl md:text-5xl font-extrabold bg-gradient-to-r from-[#8B4000] to-[#A0522D] bg-clip-text text-transparent mb-4">
            Terms of Service
          </h1>
          <p class="text-gray-600 text-lg">Terms and conditions for using our services</p>
          <p class="text-sm text-gray-500 mt-2">Last updated: {{ lastUpdated }}</p>
        </div>

        <!-- Content -->
        <div class="prose prose-lg max-w-none">
          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">1. Acceptance of Terms</h2>
            <p class="text-gray-700 mb-4">
              By accessing and using the Sauti Child Helpline services, you accept and agree to be bound by the terms 
              and provision of this agreement. If you do not agree to abide by the above, please do not use this service.
            </p>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">2. Description of Service</h2>
            <p class="text-gray-700 mb-4">
              Sauti Child Helpline provides:
            </p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>24/7 confidential helpline services (116)</li>
              <li>Online reporting and support services</li>
              <li>Information and resources for child protection</li>
              <li>Referrals to appropriate services</li>
              <li>Counseling and guidance services</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">3. User Responsibilities</h2>
            <p class="text-gray-700 mb-4">When using our services, you agree to:</p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>Provide accurate and truthful information</li>
              <li>Use the service for legitimate purposes only</li>
              <li>Respect the confidentiality of other users</li>
              <li>Not misuse or abuse our services</li>
              <li>Report any technical issues or concerns</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">4. Confidentiality</h2>
            <p class="text-gray-700 mb-4">
              We are committed to maintaining the confidentiality of all information shared with us. However, we may 
              be required to share information in the following circumstances:
            </p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>When there is immediate risk of harm to a child</li>
              <li>When required by law or court order</li>
              <li>With your explicit consent</li>
              <li>In emergency situations requiring immediate action</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">5. Service Availability</h2>
            <p class="text-gray-700 mb-4">
              While we strive to provide continuous service availability, we cannot guarantee that our services 
              will be available at all times. We reserve the right to:
            </p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>Suspend services for maintenance</li>
              <li>Modify or discontinue services</li>
              <li>Implement security measures</li>
              <li>Respond to technical issues</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">6. Limitation of Liability</h2>
            <p class="text-gray-700 mb-4">
              Sauti Child Helpline and its partners are not liable for any direct, indirect, incidental, special, 
              or consequential damages resulting from the use or inability to use our services.
            </p>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">7. Emergency Situations</h2>
            <p class="text-gray-700 mb-4">
              In case of emergency or immediate danger, please:
            </p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>Call emergency services (999) immediately</li>
              <li>Contact local police authorities</li>
              <li>Seek immediate medical attention if needed</li>
              <li>Contact us at 116 for additional support</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">8. Contact Information</h2>
            <p class="text-gray-700 mb-4">
              For questions about these terms or our services, please contact us:
            </p>
            <div class="bg-gray-50 p-6 rounded-lg">
              <p class="text-gray-700 mb-2"><strong>Helpline:</strong> 116 (Toll Free)</p>
              <p class="text-gray-700 mb-2"><strong>Email:</strong> info@sauti.mglsd.go.ug</p>
              <p class="text-gray-700"><strong>Address:</strong> Ministry of Gender, Labour & Social Development, Kampala, Uganda</p>
            </div>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">9. Changes to Terms</h2>
            <p class="text-gray-700">
              We reserve the right to modify these terms at any time. Changes will be posted on this page with 
              an updated revision date. Continued use of our services constitutes acceptance of the modified terms.
            </p>
          </section>
        </div>

        <!-- Back to Home -->
        <div class="text-center mt-12">
          <router-link to="/" class="btn-primary inline-flex items-center gap-2">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
            </svg>
            Back to Home
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const lastUpdated = computed(() => {
  return new Date().toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  })
})
</script>