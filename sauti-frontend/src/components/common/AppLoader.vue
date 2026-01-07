<template>
  <div v-if="loading" class="flex items-center justify-center" :class="containerClass">
    <div class="text-center">
      <!-- Spinner -->
      <div class="spinner" :class="sizeClass" role="status" aria-label="Loading">
        <span class="sr-only">Loading...</span>
      </div>

      <!-- Optional message -->
      <p v-if="message" class="mt-4 text-secondary font-bold" :class="textSizeClass">
        {{ message }}
      </p>
    </div>
  </div>
</template>

<script setup>
  import { computed } from 'vue'

  defineOptions({
    name: 'AppLoader'
  })

  const props = defineProps({
    loading: {
      type: Boolean,
      default: true,
    },
    message: {
      type: String,
      default: '',
    },
    size: {
      type: String,
      default: 'medium', // small, medium, large
      validator: (value) => ['small', 'medium', 'large'].includes(value),
    },
    fullScreen: {
      type: Boolean,
      default: false,
    },
  })

  const containerClass = computed(() => {
    return props.fullScreen
      ? 'fixed inset-0 bg-neutral-white bg-opacity-90 z-50'
      : 'py-12'
  })

  const sizeClass = computed(() => {
    const sizes = {
      small: 'w-6 h-6 border-2',
      medium: 'w-8 h-8 border-4',
      large: 'w-12 h-12 border-4',
    }
    return sizes[props.size]
  })

  const textSizeClass = computed(() => {
    const sizes = {
      small: 'text-sm',
      medium: 'text-base',
      large: 'text-lg',
    }
    return sizes[props.size]
  })
</script>
