<template>
  <router-link 
    :to="to" 
    class="group flex flex-col p-6 bg-white rounded-2xl shadow-sm border border-gray-100 hover:shadow-xl hover:border-blue-200 transition-all duration-300 relative overflow-hidden"
  >
    <!-- Background Accent -->
    <div 
      class="absolute top-0 right-0 -tr-y-4 tr-x-4 w-24 h-24 rounded-full opacity-0 group-hover:opacity-10 transition-opacity duration-300"
      :class="color.split(' ')[0]"
    ></div>

    <div class="flex items-center justify-between mb-4">
      <div :class="['p-3 rounded-xl', color]">
        <component :is="icons[icon]" class="h-6 w-6" />
      </div>
      <div class="text-gray-300 group-hover:text-blue-500 transition-colors">
        <ArrowRightIcon class="h-5 w-5" />
      </div>
    </div>
    
    <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-blue-600 transition-colors">
      {{ title }}
    </h3>
    <p class="text-sm text-gray-500 leading-relaxed">
      {{ description }}
    </p>
  </router-link>
</template>

<script setup>
import { 
  DocumentTextIcon, 
  VideoCameraIcon, 
  FolderOpenIcon, 
  QuestionMarkCircleIcon,
  HomeIcon,
  InformationCircleIcon,
  CubeIcon,
  UserGroupIcon,
  ClockIcon,
  HeartIcon,
  ShieldCheckIcon,
  PhotoIcon,
  ShareIcon,
  PhoneIcon,
  ScaleIcon,
  HandThumbUpIcon,
  ArrowRightIcon
} from '@heroicons/vue/24/outline'

const icons = {
  DocumentTextIcon, 
  VideoCameraIcon, 
  FolderOpenIcon, 
  QuestionMarkCircleIcon,
  HomeIcon,
  InformationCircleIcon,
  CubeIcon,
  UserGroupIcon,
  ClockIcon,
  HeartIcon,
  ShieldCheckIcon,
  PhotoIcon,
  ShareIcon,
  PhoneIcon,
  ScaleIcon,
  HandThumbUpIcon
}

defineProps({
  title: String,
  description: String,
  icon: String,
  to: String,
  color: {
    type: String,
    default: 'bg-gray-50 text-gray-600'
  }
})
</script>
