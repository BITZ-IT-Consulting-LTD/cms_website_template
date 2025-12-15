<template>
  <div class="group bg-white rounded-xl p-6 shadow-md hover:shadow-xl transition-all duration-300 border border-gray-100"
       :class="`hover:border-${color}-200`">
    <div class="flex items-start gap-4">
      <div class="flex-shrink-0 w-12 h-12 rounded-lg flex items-center justify-center group-hover:bg-blue-100 transition-colors"
           :class="`bg-${color}-50`">
        <component :is="getIconComponent(icon)" class="w-6 h-6" :class="`text-${color}-600`" />
      </div>
      <div>
        <h4 class="font-bold text-gray-900 mb-2">{{ service.title }}</h4>
        <p class="text-sm leading-relaxed text-gray-500">{{ service.description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';
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
    default: 'blue', // Default color if not provided
  },
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
