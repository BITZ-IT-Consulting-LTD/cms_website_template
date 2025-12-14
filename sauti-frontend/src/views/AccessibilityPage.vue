<template>
  <div class="bg-white py-16">
    <div class="container-custom">
      <div class="max-w-4xl mx-auto">
        <!-- Header -->
        <div class="text-center mb-12">
          <h1 class="text-4xl md:text-5xl font-extrabold bg-gradient-to-r from-[#8B4000] to-[#A0522D] bg-clip-text text-transparent mb-4">
            Accessibility Statement
          </h1>
          <p class="text-gray-600 text-lg">Our commitment to making our services accessible to everyone</p>
          <p class="text-sm text-gray-500 mt-2">Last updated: {{ lastUpdated }}</p>
        </div>

        <!-- Content -->
        <div class="prose prose-lg max-w-none">
          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">Our Commitment</h2>
            <p class="text-gray-700 mb-4">
              Sauti 116 helpline is committed to ensuring digital accessibility for all users, including those 
              with disabilities. We strive to provide an accessible and inclusive experience for everyone who 
              needs our services.
            </p>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">Accessibility Features</h2>
            <p class="text-gray-700 mb-4">Our website and services include the following accessibility features:</p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>Keyboard navigation support</li>
              <li>Screen reader compatibility</li>
              <li>High contrast color schemes</li>
              <li>Resizable text and images</li>
              <li>Alternative text for images</li>
              <li>Clear and simple language</li>
              <li>Consistent navigation structure</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">Helpline Accessibility</h2>
            <p class="text-gray-700 mb-4">Our helpline services are designed to be accessible through:</p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>Toll-free calling (116) from any phone</li>
              <li>WhatsApp messaging for text-based communication</li>
              <li>SMS services through U-Report</li>
              <li>Mobile app with accessibility features</li>
              <li>Multiple language support (English, Luganda, Swahili)</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">Standards Compliance</h2>
            <p class="text-gray-700 mb-4">
              We aim to conform to the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA standards. 
              This includes:
            </p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>Perceivable content with alternative formats</li>
              <li>Operable interface with keyboard and voice navigation</li>
              <li>Understandable information and interface</li>
              <li>Robust content compatible with assistive technologies</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">Assistive Technologies</h2>
            <p class="text-gray-700 mb-4">Our services are compatible with:</p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>Screen readers (NVDA, JAWS, VoiceOver)</li>
              <li>Voice recognition software</li>
              <li>Switch navigation devices</li>
              <li>Magnification software</li>
              <li>Alternative input devices</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">Alternative Access Methods</h2>
            <p class="text-gray-700 mb-4">If you encounter accessibility barriers, you can:</p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>Call our helpline at 116 (toll-free)</li>
              <li>Use WhatsApp for text-based communication</li>
              <li>Send an SMS through U-Report</li>
              <li>Contact us via email</li>
              <li>Visit our physical office locations</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">Feedback and Support</h2>
            <p class="text-gray-700 mb-4">
              We welcome feedback on the accessibility of our services. If you encounter any barriers or 
              have suggestions for improvement, please contact us:
            </p>
            <div class="bg-gray-50 p-6 rounded-lg">
              <p class="text-gray-700 mb-2"><strong>Accessibility Coordinator:</strong> accessibility@sauti.mglsd.go.ug</p>
              <p class="text-gray-700 mb-2"><strong>Helpline:</strong> 116 (Toll Free)</p>
              <p class="text-gray-700 mb-2"><strong>Email:</strong> info@sauti.mglsd.go.ug</p>
              <p class="text-gray-700"><strong>Address:</strong> Ministry of Gender, Labour & Social Development, Kampala, Uganda</p>
            </div>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">Ongoing Improvements</h2>
            <p class="text-gray-700 mb-4">
              We are continuously working to improve the accessibility of our services. This includes:
            </p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>Regular accessibility audits</li>
              <li>User testing with people with disabilities</li>
              <li>Staff training on accessibility best practices</li>
              <li>Implementation of new accessibility technologies</li>
              <li>Regular updates to our digital platforms</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">Emergency Accessibility</h2>
            <p class="text-gray-700 mb-4">
              In emergency situations, we ensure that our services remain accessible through:
            </p>
            <ul class="list-disc list-inside text-gray-700 mb-4 space-y-2">
              <li>Multiple communication channels</li>
              <li>Backup systems and redundancy</li>
              <li>24/7 availability</li>
              <li>Alternative contact methods</li>
              <li>Emergency response protocols</li>
            </ul>
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

defineOptions({
  name: 'AccessibilityPage'
})

const lastUpdated = computed(() => {
  return new Date().toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  })
})
</script>
