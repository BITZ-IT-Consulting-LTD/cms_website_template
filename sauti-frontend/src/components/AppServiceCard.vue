<template>
  <div
    class="group bg-neutral-white rounded-xl p-6 shadow-md hover:shadow-xl transition-all duration-300 border border-neutral-offwhite"
    :class="`hover:border-${colorToken}/30`">
    <div class="flex items-start gap-4">
      <div class="flex-shrink-0 w-12 h-12 rounded-lg flex items-center justify-center transition-colors"
        :class="[`bg-${colorToken}/10`, `group-hover:bg-${colorToken}/20`]">
        <component :is="getIconComponent(service.icon)" class="w-6 h-6" :class="`text-${colorToken}`" />
      </div>
      <div>
        <h4 class="font-bold text-secondary mb-2">{{ service.title }}</h4>
        <p class="text-sm leading-relaxed text-muted font-bold">{{ service.description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { defineProps, computed } from 'vue';
  import {
    PhoneIcon,
    UserGroupIcon,
    MegaphoneIcon,
    ArrowPathIcon,
    GlobeAltIcon,
    ShieldCheckIcon,
    HandRaisedIcon,
    BookOpenIcon,
    VideoCameraIcon,
    QuestionMarkCircleIcon,
    BuildingOfficeIcon,
    ShareIcon,
    WrenchScrewdriverIcon,
    ClockIcon,
    DocumentTextIcon,
    FolderOpenIcon,
    Squares2X2Icon,
    PencilSquareIcon,
    ShieldExclamationIcon,
    PhotoIcon,
    ArrowRightOnRectangleIcon,
    PlusCircleIcon,
    Bars3Icon,
    XMarkIcon,
  } from '@heroicons/vue/24/outline';

  defineOptions({
    name: 'AppServiceCard'
  })

  const { service, color } = defineProps({
    service: {
      type: Object,
      required: true,
    },
    color: {
      type: String,
      default: 'primary',
    },
  });

  const colorToken = computed(() => {
    const map = {
      'blue': 'primary',
      'orange': 'hotline',
      'green': 'secondary-light',
      'red': 'emergency'
    };
    return map[color] || color || 'primary';
  });

  // Map icon names to Heroicons components
  const getIconComponent = (iconName) => {
    const icons = {
      'phone': PhoneIcon,
      'walk': UserGroupIcon, // Using UserGroupIcon for 'walk-in'
      'media': MegaphoneIcon,
      'guidance': ArrowPathIcon,
      'community': GlobeAltIcon,
      'shield': ShieldCheckIcon,
      'hand': HandRaisedIcon,
      'book': BookOpenIcon,
      'video': VideoCameraIcon,
      'question': QuestionMarkCircleIcon,
      'building': BuildingOfficeIcon,
      'share': ShareIcon,
      'wrench': WrenchScrewdriverIcon,
      'clock': ClockIcon,
      'document': DocumentTextIcon,
      'folder': FolderOpenIcon,
      'squares': Squares2X2Icon,
      'pencil': PencilSquareIcon,
      'exclamation': ShieldExclamationIcon,
      'photo': PhotoIcon,
      'logout': ArrowRightOnRectangleIcon,
      'plus': PlusCircleIcon,
      'bars': Bars3Icon,
      'xmark': XMarkIcon,
    };
    return icons[iconName] || GlobeAltIcon; // Default to GlobeAltIcon if not found
  };
</script>

<style scoped>
  /* Add any specific styles for the ServiceCard here */
</style>
