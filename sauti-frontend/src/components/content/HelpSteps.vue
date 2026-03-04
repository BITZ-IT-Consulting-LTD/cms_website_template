<template>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
    <div v-for="(step, index) in steps" :key="step.id || index" class="bg-primary/5 p-6 rounded-2xl border border-primary/10">
      <div class="w-8 h-8 rounded-full bg-[#009EDB] text-white flex items-center justify-center font-bold mb-4">
        {{ step.step_order || index + 1 }}
      </div>
      <h3 class="text-lg font-bold text-secondary mb-2">{{ step.title }}</h3>
      <p class="text-black/60">{{ step.description }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  steps: {
    type: Array,
    required: true,
    default: () => []
  }
})
</script>
