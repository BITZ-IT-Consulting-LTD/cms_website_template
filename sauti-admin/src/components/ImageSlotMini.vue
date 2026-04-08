<template>
  <div
    @click="$emit('click')"
    class="aspect-[4/3] bg-white rounded-lg overflow-hidden border border-gray-200 cursor-pointer hover:border-emerald-400 hover:shadow-md transition-all relative group"
  >
    <img
      v-if="image?.image_url"
      :src="image.image_url"
      :alt="image.title"
      class="w-full h-full object-cover"
    />
    <div
      v-else
      class="w-full h-full flex items-center justify-center text-gray-300 bg-gray-50"
    >
      <PhotoIcon class="w-6 h-6" />
    </div>
    <div class="absolute top-0.5 left-0.5 bg-black/60 text-white text-[8px] font-bold px-1 rounded">
      {{ position }}
    </div>
    <div class="absolute inset-0 bg-emerald-600/20 opacity-0 group-hover:opacity-100 transition-opacity"></div>
  </div>
</template>

<script setup>
import { PhotoIcon } from '@heroicons/vue/24/outline'

defineProps({
  position: {
    type: [Number, String],
    required: true
  },
  image: {
    type: Object,
    default: null
  },
  label: {
    type: String,
    default: ''
  }
})

defineEmits(['click'])
</script>
