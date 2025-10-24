<template>
  <div class="bg-gray-50 py-16">
    <div class="container-custom max-w-3xl">
      <h1 class="text-4xl md:text-5xl font-extrabold mb-6">Privacy Policy</h1>
      <p class="text-gray-600 mb-8">Last updated: {{ lastUpdated }}</p>

      <div class="space-y-8 bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
        <section>
          <h2 class="text-xl font-semibold mb-2">Your Privacy Matters</h2>
          <p class="text-gray-700">We are committed to protecting the privacy of children, families, and all users who contact Sauti. We collect only the information needed to provide help, and we handle it with strict confidentiality.</p>
        </section>

        <section>
          <h2 class="text-xl font-semibold mb-2">What We Collect</h2>
          <ul class="list-disc pl-5 text-gray-700 space-y-1">
            <li>Details you choose to share when asking for help</li>
            <li>Optional contact information for follow-up</li>
            <li>Technical data like IP address and user agent for security</li>
          </ul>
        </section>

        <section>
          <h2 class="text-xl font-semibold mb-2">How We Use Information</h2>
          <ul class="list-disc pl-5 text-gray-700 space-y-1">
            <li>Provide immediate assistance and referrals</li>
            <li>Improve our services and ensure safety</li>
            <li>Comply with legal and safeguarding obligations</li>
          </ul>
        </section>

        <section>
          <h2 class="text-xl font-semibold mb-2">Sharing and Confidentiality</h2>
          <p class="text-gray-700">We do not sell your data. We may share limited information with trusted partners solely to protect a child or provide services, and only when necessary.</p>
        </section>

        <section>
          <h2 class="text-xl font-semibold mb-2">Contact</h2>
          <p class="text-gray-700">Questions about this policy? <router-link to="/contact" class="text-primary-600 underline">Contact us</router-link> or call <a href="tel:116" class="text-primary-600 underline">116</a>.</p>
        </section>
      </div>
    </div>
  </div>
</template>

<script setup>
const lastUpdated = new Date().getFullYear()
</script>


