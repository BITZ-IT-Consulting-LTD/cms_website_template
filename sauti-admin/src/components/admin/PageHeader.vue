<template>
  <div class="mb-8">
    <div class="flex justify-between items-start">
      <div>
        <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">
          {{ title }}
        </h1>
        <p class="text-gray-600 mt-1">{{ description }}</p>
      </div>
      <button
        v-if="actionLabel"
        @click="handleAction"
        class="btn-primary flex items-center shadow-lg hover:shadow-xl"
      >
        <component v-if="actionIcon" :is="actionIcon" class="h-5 w-5 mr-2" />
        <span>{{ actionLabel }}</span>
      </button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  actionLabel: {
    type: String,
    default: null
  },
  actionIcon: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['action'])

const handleAction = () => {
  emit('action')
}
</script>
