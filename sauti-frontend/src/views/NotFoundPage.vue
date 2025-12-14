<template>
  <div class="section-padding text-center">
    <div class="container-custom max-w-2xl">
      <h1 class="text-6xl font-bold text-gray-900 mb-4">404</h1>
      <h2 class="text-2xl font-semibold text-gray-700 mb-6">Page Not Found</h2>
      <p class="text-gray-600 mb-8">The page you're looking for doesn't exist or has been moved.</p>
      <router-link to="/" class="btn-primary">← Return Home</router-link>
    </div>
  </div>
</template>

<script setup>
defineOptions({
  name: 'NotFoundPage'
})
</script>
