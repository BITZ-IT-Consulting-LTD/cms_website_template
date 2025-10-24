<template>
  <div class="bg-white py-16">
    <div class="container-custom">
      <div class="max-w-4xl mx-auto">
        <!-- Header -->
        <div class="text-center mb-12">
          <h1 class="text-4xl md:text-5xl font-extrabold bg-gradient-to-r from-[#8B4000] to-[#A0522D] bg-clip-text text-transparent mb-4">
            Privacy Policy
          </h1>
          <p class="text-gray-600 text-lg">How we protect your information and privacy</p>
          <p class="text-sm text-gray-500 mt-2">Last updated: {{ lastUpdated }}</p>
        </div>

        <!-- Content -->
        <div class="prose prose-lg max-w-none">
          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">1. Information We Collect</h2>
            <p class="text-gray-700 mb-4">
              We collect information you provide directly to us, such as when you:
            </p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>Call our helpline (116)</li>
              <li>Submit reports through our website</li>
              <li>Contact us via email or WhatsApp</li>
              <li>Use our mobile applications</li>
            </ul>
            <p class="text-gray-700">
              This may include your name, contact information, location, and details about the situation you're reporting.
            </p>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">2. How We Use Your Information</h2>
            <p class="text-gray-700 mb-4">We use the information we collect to:</p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>Provide immediate support and counseling</li>
              <li>Connect you with appropriate services</li>
              <li>Follow up on cases when necessary</li>
              <li>Improve our services and training</li>
              <li>Comply with legal requirements</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">3. Information Sharing</h2>
            <p class="text-gray-700 mb-4">
              We do not share your personal information except in the following circumstances:
            </p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>With your explicit consent</li>
              <li>When required by law to protect a child</li>
              <li>With authorized service providers who assist us</li>
              <li>In emergency situations where immediate action is needed</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">4. Data Security</h2>
            <p class="text-gray-700 mb-4">
              We implement appropriate security measures to protect your information against unauthorized access, 
              alteration, disclosure, or destruction. This includes:
            </p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>Encrypted data transmission</li>
              <li>Secure data storage</li>
              <li>Regular security audits</li>
              <li>Limited access to authorized personnel only</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">5. Your Rights</h2>
            <p class="text-gray-700 mb-4">You have the right to:</p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>Access your personal information</li>
              <li>Correct inaccurate information</li>
              <li>Request deletion of your information</li>
              <li>Withdraw consent at any time</li>
              <li>File a complaint if you believe your rights have been violated</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">6. Contact Us</h2>
            <p class="text-gray-700 mb-4">
              If you have questions about this Privacy Policy or our data practices, please contact us:
            </p>
            <div class="bg-gray-50 p-6 rounded-lg">
              <p class="text-gray-700 mb-2"><strong>Email:</strong> privacy@sauti.mglsd.go.ug</p>
              <p class="text-gray-700 mb-2"><strong>Phone:</strong> 116 (Toll Free)</p>
              <p class="text-gray-700"><strong>Address:</strong> Ministry of Gender, Labour & Social Development, Kampala, Uganda</p>
            </div>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">7. Changes to This Policy</h2>
            <p class="text-gray-700">
              We may update this Privacy Policy from time to time. We will notify you of any changes by posting 
              the new Privacy Policy on this page and updating the "Last updated" date.
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