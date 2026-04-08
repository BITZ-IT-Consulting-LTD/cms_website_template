<template>
  <div class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden">
    <button
      @click="isOpen = !isOpen"
      class="w-full px-6 py-4 flex items-center justify-between hover:bg-gray-50 transition-colors"
    >
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-gray-100 flex items-center justify-center">
          <component :is="icon" class="h-5 w-5 text-gray-600" />
        </div>
        <div class="text-left">
          <h3 class="font-bold text-gray-900">{{ title }}</h3>
          <p class="text-xs text-gray-500">{{ subtitle }}</p>
        </div>
      </div>
      <div class="flex items-center gap-3">
        <span
          v-if="badge"
          :class="[
            'px-2 py-1 text-xs font-bold rounded-full',
            badgeColorClass
          ]"
        >{{ badge.text }}</span>
        <ChevronDownIcon v-if="!isOpen" class="h-5 w-5 text-gray-400" />
        <ChevronUpIcon v-else class="h-5 w-5 text-gray-400" />
      </div>
    </button>
    <div v-show="isOpen" class="px-6 pb-6 border-t border-gray-100">
      <div class="pt-4">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { ChevronDownIcon, ChevronUpIcon } from '@heroicons/vue/24/outline'

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  subtitle: {
    type: String,
    default: ''
  },
  icon: {
    type: [Object, Function],
    required: true
  },
  badge: {
    type: Object,
    default: null
  },
  defaultOpen: {
    type: Boolean,
    default: false
  }
})

const isOpen = ref(props.defaultOpen)

const badgeColorClass = computed(() => {
  if (!props.badge) return ''
  const colorMap = {
    green: 'bg-green-100 text-green-700',
    amber: 'bg-amber-100 text-amber-700',
    blue: 'bg-blue-100 text-blue-700',
    purple: 'bg-purple-100 text-purple-700',
    indigo: 'bg-indigo-100 text-indigo-700',
    rose: 'bg-rose-100 text-rose-700',
    teal: 'bg-teal-100 text-teal-700'
  }
  return colorMap[props.badge.color] || 'bg-gray-100 text-gray-700'
})
</script>
