<template>
  <div class="p-6 space-y-6">
    <!-- Header -->
    <div class="flex justify-between items-start">
      <div>
        <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">Success Stories</h1>
        <p class="text-gray-600 mt-1">Share inspiring stories of impact and transformation</p>
      </div>
      <button
        @click="showCreateModal = true"
        class="px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 transition-colors duration-200 flex items-center font-medium shadow-sm"
      >
        <PlusIcon class="h-5 w-5 mr-2" />
        Add New Story
      </button>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total Stories</p>
            <p class="text-3xl font-bold text-gray-900 mt-2">{{ stats.total }}</p>
          </div>
          <div class="p-3 bg-blue-100 rounded-lg">
            <SparklesIcon class="h-8 w-8 text-blue-600" />
          </div>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Published</p>
            <p class="text-3xl font-bold text-green-600 mt-2">{{ stats.published }}</p>
          </div>
          <div class="p-3 bg-green-100 rounded-lg">
            <CheckCircleIcon class="h-8 w-8 text-green-600" />
          </div>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total Views</p>
            <p class="text-3xl font-bold text-purple-600 mt-2">{{ stats.views.toLocaleString() }}</p>
          </div>
          <div class="p-3 bg-purple-100 rounded-lg">
            <EyeIcon class="h-8 w-8 text-purple-600" />
          </div>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Lives Impacted</p>
            <p class="text-3xl font-bold text-orange-600 mt-2">{{ stats.impacted.toLocaleString() }}</p>
          </div>
          <div class="p-3 bg-orange-100 rounded-lg">
            <HeartIcon class="h-8 w-8 text-orange-600" />
          </div>
        </div>
      </div>
    </div>

    <!-- Filters and Search -->
    <div class="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
      <div class="flex flex-col md:flex-row gap-4">
        <div class="flex-1 relative">
          <MagnifyingGlassIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search stories..."
            class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        </div>
        
        <select
          v-model="filterCategory"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Categories</option>
          <option value="rescue">Rescue & Recovery</option>
          <option value="education">Education</option>
          <option value="rehabilitation">Rehabilitation</option>
          <option value="family">Family Reunification</option>
          <option value="empowerment">Youth Empowerment</option>
        </select>

        <select
          v-model="filterStatus"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Status</option>
          <option value="published">Published</option>
          <option value="draft">Draft</option>
          <option value="pending">Pending Review</option>
        </select>
      </div>
    </div>

    <!-- Stories Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <div
        v-for="story in filteredStories"
        :key="story.id"
        class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow duration-200"
      >
        <!-- Story Image -->
        <div class="relative h-56 bg-gradient-to-br from-orange-400 to-pink-500">
          <img
            v-if="story.image"
            :src="story.image"
            :alt="story.title"
            class="w-full h-full object-cover"
          />
          <div v-else class="w-full h-full flex items-center justify-center text-white">
            <PhotoIcon class="h-20 w-20 opacity-50" />
          </div>
          
          <!-- Status Badge -->
          <span
            class="absolute top-4 right-4 px-3 py-1 text-xs font-semibold rounded-full shadow-sm"
            :class="statusBadgeClass(story.status)"
          >
            {{ story.status }}
          </span>

          <!-- Category Badge -->
          <span class="absolute top-4 left-4 px-3 py-1 text-xs font-semibold rounded-full bg-white text-gray-700 shadow-sm">
            {{ story.category }}
          </span>
        </div>

        <!-- Story Content -->
        <div class="p-6">
          <div class="flex items-start justify-between mb-3">
            <h3 class="font-semibold text-xl text-gray-900 flex-1">
              {{ story.title }}
            </h3>
          </div>

          <p class="text-gray-600 mb-4 line-clamp-3">
            {{ story.excerpt }}
          </p>

          <!-- Impact Stats -->
          <div class="grid grid-cols-3 gap-4 mb-4 py-4 border-y border-gray-100">
            <div class="text-center">
              <p class="text-2xl font-bold text-primary-600">{{ story.beneficiaries }}</p>
              <p class="text-xs text-gray-500">Beneficiaries</p>
            </div>
            <div class="text-center">
              <p class="text-2xl font-bold text-green-600">{{ story.views }}</p>
              <p class="text-xs text-gray-500">Views</p>
            </div>
            <div class="text-center">
              <p class="text-2xl font-bold text-purple-600">{{ story.shares }}</p>
              <p class="text-xs text-gray-500">Shares</p>
            </div>
          </div>

          <!-- Meta Info -->
          <div class="flex items-center text-sm text-gray-500 mb-4">
            <CalendarIcon class="h-4 w-4 mr-1" />
            <span>{{ formatDate(story.date) }}</span>
            <span class="mx-2">•</span>
            <UserIcon class="h-4 w-4 mr-1" />
            <span>{{ story.author }}</span>
          </div>

          <!-- Location -->
          <div v-if="story.location" class="flex items-center text-sm text-gray-600 mb-4">
            <MapPinIcon class="h-4 w-4 mr-1 text-gray-400" />
            <span>{{ story.location }}</span>
          </div>

          <!-- Actions -->
          <div class="flex gap-2">
            <button
              @click="viewStory(story)"
              class="flex-1 px-3 py-2 bg-gray-100 text-gray-700 rounded-md hover:bg-gray-200 transition-colors duration-200 flex items-center justify-center text-sm font-medium"
            >
              <EyeIcon class="h-4 w-4 mr-1" />
              View
            </button>
            <button
              @click="editStory(story)"
              class="flex-1 px-3 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 transition-colors duration-200 flex items-center justify-center text-sm font-medium"
            >
              <PencilIcon class="h-4 w-4 mr-1" />
              Edit
            </button>
            <button
              v-if="story.status === 'published'"
              @click="shareStory(story)"
              class="px-3 py-2 bg-blue-100 text-blue-600 rounded-md hover:bg-blue-200 transition-colors duration-200"
            >
              <ShareIcon class="h-4 w-4" />
            </button>
            <button
              @click="deleteStory(story)"
              class="px-3 py-2 bg-red-100 text-red-600 rounded-md hover:bg-red-200 transition-colors duration-200"
            >
              <TrashIcon class="h-4 w-4" />
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-if="filteredStories.length === 0" class="bg-white rounded-lg shadow-sm border border-gray-200 p-12 text-center">
      <SparklesIcon class="mx-auto h-12 w-12 text-gray-400" />
      <h3 class="mt-2 text-sm font-medium text-gray-900">No stories found</h3>
      <p class="mt-1 text-sm text-gray-500">Start sharing inspiring success stories</p>
      <button
        @click="showCreateModal = true"
        class="mt-4 px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 transition-colors duration-200"
      >
        Add New Story
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import {
  PlusIcon,
  MagnifyingGlassIcon,
  SparklesIcon,
  CheckCircleIcon,
  EyeIcon,
  HeartIcon,
  PhotoIcon,
  PencilIcon,
  TrashIcon,
  ShareIcon,
  CalendarIcon,
  UserIcon,
  MapPinIcon
} from '@heroicons/vue/24/outline'

// Mock data
const stories = ref([
  {
    id: 1,
    title: 'Amina\'s Journey: From Street Child to University Graduate',
    excerpt: 'At just 12 years old, Amina was living on the streets of Kampala. Today, she holds a degree in Social Work and helps other children escape similar situations. Her story is a testament to resilience and the power of intervention.',
    category: 'Education',
    status: 'published',
    image: null,
    date: '2024-01-15',
    author: 'Sarah Nakato',
    location: 'Kampala, Uganda',
    beneficiaries: 1,
    views: 2847,
    shares: 156
  },
  {
    id: 2,
    title: 'Safe Haven: How a Village United to Protect Its Children',
    excerpt: 'When reports of child abuse increased in Mbale District, the community came together to create a child protection committee. Within 18 months, reported cases dropped by 60% and 45 children found safe homes.',
    category: 'Rescue & Recovery',
    status: 'published',
    image: null,
    date: '2024-01-10',
    author: 'John Okello',
    location: 'Mbale District, Uganda',
    beneficiaries: 45,
    views: 3921,
    shares: 284
  },
  {
    id: 3,
    title: 'Breaking Cycles: Joseph\'s Story of Healing and Hope',
    excerpt: 'After experiencing severe trauma, 15-year-old Joseph entered our rehabilitation program. Through counseling, education, and vocational training, he now runs a successful carpentry business and mentors other youth.',
    category: 'Rehabilitation',
    status: 'published',
    image: null,
    date: '2023-12-20',
    author: 'Grace Apio',
    location: 'Gulu, Uganda',
    beneficiaries: 1,
    views: 1834,
    shares: 92
  },
  {
    id: 4,
    title: 'Family Reunion: Reuniting 8 Siblings After 5 Years',
    excerpt: 'When their parents passed away, 8 siblings were separated across different households. Through dedicated case work and family tracing, all siblings were successfully reunited with their grandmother who received support to care for them.',
    category: 'Family Reunification',
    status: 'published',
    image: null,
    date: '2023-12-15',
    author: 'Patrick Musoke',
    location: 'Jinja, Uganda',
    beneficiaries: 8,
    views: 4562,
    shares: 387
  },
  {
    id: 5,
    title: 'Young Leaders: Teen Mothers Return to School',
    excerpt: 'Our adolescent mothers program has enabled 34 young mothers to return to school while receiving childcare support and life skills training. Meet Maria, who is now preparing for her nursing exams.',
    category: 'Youth Empowerment',
    status: 'draft',
    image: null,
    date: '2024-01-18',
    author: 'Betty Namuli',
    location: 'Kampala, Uganda',
    beneficiaries: 34,
    views: 0,
    shares: 0
  }
])

const stats = ref({
  total: 47,
  published: 42,
  views: 28456,
  impacted: 1247
})

const searchQuery = ref('')
const filterCategory = ref('')
const filterStatus = ref('')
const showCreateModal = ref(false)

const filteredStories = computed(() => {
  return stories.value.filter(story => {
    const matchesSearch = !searchQuery.value ||
      story.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      story.excerpt.toLowerCase().includes(searchQuery.value.toLowerCase())
    
    const matchesCategory = !filterCategory.value || story.category === filterCategory.value
    const matchesStatus = !filterStatus.value || story.status === filterStatus.value

    return matchesSearch && matchesCategory && matchesStatus
  })
})

const statusBadgeClass = (status) => {
  const classes = {
    published: 'bg-green-100 text-green-800',
    draft: 'bg-yellow-100 text-yellow-800',
    pending: 'bg-blue-100 text-blue-800'
  }
  return classes[status] || 'bg-gray-100 text-gray-800'
}

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}

const viewStory = (story) => {
  console.log('View story:', story)
}

const editStory = (story) => {
  console.log('Edit story:', story)
}

const shareStory = (story) => {
  console.log('Share story:', story)
}

const deleteStory = (story) => {
  if (confirm(`Delete "${story.title}"?`)) {
    console.log('Delete story:', story)
  }
}
</script>
