<template>
  <component :is="componentType" :to="to" :href="resolvedHref" :class="[
    'inline-flex items-center justify-center transition-all duration-300 transform font-semibold focus:outline-none',
    variantClasses,
    sizeClasses,
    disabled ? 'opacity-50 cursor-not-allowed pointer-events-none' : 'active:scale-95'
  ]" :aria-disabled="disabled" v-bind="$attrs">
    <slot>{{ label }}</slot>
  </component>
</template>

<script setup>
  import { computed } from 'vue'
  import { RouterLink } from 'vue-router'

  const props = defineProps({
    label: {
      type: String,
      default: ''
    },
    to: {
      type: [String, Object],
      default: null
    },
    href: {
      type: String,
      default: null
    },
    variant: {
      type: String,
      default: 'primary',
      validator: (value) => ['primary', 'secondary', 'emergency', 'outline', 'ghost'].includes(value)
    },
    size: {
      type: String,
      default: 'default', // 'default', 'large', 'small'
      validator: (value) => ['default', 'large', 'small', 'hero'].includes(value)
    },
    external: {
      type: Boolean,
      default: false
    },
    disabled: {
      type: Boolean,
      default: false
    }
  })

  const componentType = computed(() => {
    if (props.to && !props.external) {
      return 'router-link'
    }
    return 'a'
  })

  const resolvedHref = computed(() => {
    if (props.external && props.to) return props.to
    return props.href
  })

  const variantClasses = computed(() => {
    switch (props.variant) {
      case 'primary':
        return 'btn-primary'
      case 'secondary':
        return 'btn-secondary'
      case 'emergency':
        return 'btn-emergency'
      case 'outline':
        return 'btn-outline'
      default:
        return 'btn-primary'
    }
  })

  const sizeClasses = computed(() => {
    switch (props.size) {
      case 'small':
        return '!px-4 !py-2 !text-sm !rounded-lg'
      case 'large':
        return '!px-8 !py-4 !text-lg !rounded-xl'
      case 'hero':
        return '!px-10 !py-5 !text-2xl !rounded-2xl !font-bold !shadow-2xl'
      default:
        return '' // Default size handled by .btn class
    }
  })
</script>

<style scoped>
  /* Scoped overrides if necessary */
</style>
