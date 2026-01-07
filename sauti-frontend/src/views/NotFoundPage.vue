<template>
  <div class="min-h-screen bg-neutral-white flex flex-col justify-center items-center section-padding">
    <div class="container-custom max-w-4xl text-center">
      <!-- 404 Illustration placeholder or Icon -->
      <div class="relative inline-block mb-16">
        <div class="absolute inset-0 bg-primary/10 rounded-full blur-3xl transform -translate-y-1/2"></div>
        <h1 class="text-[12rem] md:text-[18rem] font-bold leading-none text-neutral-offwhite relative z-10 select-none">
          404</h1>
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-20">
          <div
            class="w-32 h-32 md:w-48 md:h-48 bg-neutral-white rounded-[3rem] shadow-2xl border-4 border-primary flex items-center justify-center animate-bounce-slow">
            <MagnifyingGlassIcon class="w-16 h-16 md:w-24 md:h-24 text-primary" />
          </div>
        </div>
      </div>

      <!-- Message -->
      <h2 class="campaign-header text-4xl md:text-6xl text-secondary mb-6">Lost in the Sanctuary?</h2>
      <p class="text-xl md:text-2xl font-bold text-secondary/50 max-w-2xl mx-auto leading-relaxed mb-16">
        The page you are looking for has been moved or does not exist in our current records. Let's get you back to
        safety.
      </p>

      <!-- Action -->
      <div class="flex flex-col sm:flex-row gap-6 justify-center items-center">
        <BaseCTA href="/" variant="primary" class="!px-12 !py-5 shadow-2xl">
          Return to Sanctuary
        </BaseCTA>
        <BaseCTA href="/contact" variant="outline" class="!px-12 !py-5">
          Report a Problem
        </BaseCTA>
      </div>

      <!-- Quick Links -->
      <div class="mt-24 pt-12 border-t-2 border-neutral-offwhite flex flex-wrap justify-center gap-8">
        <router-link v-for="link in [
          { name: 'Helpline', path: '/contact' },
          { name: 'Resources', path: '/resources' },
          { name: 'Reports', path: '/reports-insights' }
        ]" :key="link.name" :to="link.path"
          class="campaign-header text-[10px] text-primary hover:text-secondary transition-colors">
          {{ link.name }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import { MagnifyingGlassIcon } from '@heroicons/vue/24/outline'

  defineOptions({
    name: 'NotFoundPage'
  })
</script>

<style scoped>
  @keyframes bounce-slow {

    0%,
    100% {
      transform: translate(-50%, -55%);
    }

    50% {
      transform: translate(-50%, -45%);
    }
  }

  .animate-bounce-slow {
    animation: bounce-slow 4s ease-in-out infinite;
  }
</style>
