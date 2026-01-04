<template>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
    <div v-for="(step, index) in steps" :key="step.id || index" class="bg-gray-50 p-6 rounded-2xl border border-gray-100">
      <div class="w-8 h-8 rounded-full bg-[#009EDB] text-white flex items-center justify-center font-bold mb-4">
        {{ step.step_order || index + 1 }}
      </div>
      <h3 class="text-lg font-bold text-gray-900 mb-2">{{ step.title }}</h3>
      <p class="text-gray-600">{{ step.description }}</p>
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
