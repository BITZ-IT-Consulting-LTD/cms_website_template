<template>
  <div class="p-6 space-y-6">
    <!-- Header -->
    <div class="flex justify-between items-start">
      <div>
        <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">FAQs</h1>
        <p class="text-gray-600 mt-1">Manage frequently asked questions</p>
      </div>
      <button
        @click="showCreateModal = true"
        class="px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 transition-colors duration-200 flex items-center font-medium shadow-sm"
      >
        <PlusIcon class="h-5 w-5 mr-2" />
        Add New FAQ
      </button>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total FAQs</p>
            <p class="text-3xl font-bold text-gray-900 mt-2">{{ stats.total }}</p>
          </div>
          <div class="p-3 bg-blue-100 rounded-lg">
            <QuestionMarkCircleIcon class="h-8 w-8 text-blue-600" />
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
            <p class="text-3xl font-bold text-purple-600 mt-2">{{ stats.views }}</p>
          </div>
          <div class="p-3 bg-purple-100 rounded-lg">
            <EyeIcon class="h-8 w-8 text-purple-600" />
          </div>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Helpful Votes</p>
            <p class="text-3xl font-bold text-teal-600 mt-2">{{ stats.helpful }}</p>
          </div>
          <div class="p-3 bg-teal-100 rounded-lg">
            <HandThumbUpIcon class="h-8 w-8 text-teal-600" />
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
            placeholder="Search FAQs..."
            class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        </div>
        
        <select
          v-model="filterCategory"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Categories</option>
          <option value="general">General Information</option>
          <option value="helpline">Using the Helpline</option>
          <option value="child_safety">Child Safety</option>
          <option value="reporting">Reporting Abuse</option>
          <option value="support">Support Services</option>
          <option value="legal">Legal Information</option>
        </select>

        <select
          v-model="filterStatus"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Status</option>
          <option value="published">Published</option>
          <option value="draft">Draft</option>
        </select>
      </div>
    </div>

    <!-- FAQs by Category -->
    <div class="space-y-6">
      <div
        v-for="(categoryFaqs, category) in groupedFaqs"
        :key="category"
        class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden"
      >
        <!-- Category Header -->
        <div class="bg-gray-50 px-6 py-4 border-b border-gray-200">
          <div class="flex items-center justify-between">
            <h2 class="text-lg font-semibold text-gray-900">{{ category }}</h2>
            <span class="text-sm text-gray-500">{{ categoryFaqs.length }} questions</span>
          </div>
        </div>

        <!-- FAQ Items -->
        <div class="divide-y divide-gray-200">
          <div
            v-for="(faq, index) in categoryFaqs"
            :key="faq.id"
            class="p-6 hover:bg-gray-50 transition-colors duration-200"
          >
            <div class="flex items-start justify-between gap-4">
              <div class="flex-1">
                <!-- Question -->
                <div class="flex items-start gap-3 mb-3">
                  <div class="flex-shrink-0 w-6 h-6 bg-primary-100 text-primary-600 rounded-full flex items-center justify-center text-sm font-semibold">
                    Q
                  </div>
                  <h3 class="font-semibold text-gray-900 text-lg">{{ faq.question }}</h3>
                </div>

                <!-- Answer -->
                <div class="flex items-start gap-3 mb-4 ml-9">
                  <p class="text-gray-700">{{ faq.answer }}</p>
                </div>

                <!-- Meta Info -->
                <div class="flex items-center gap-4 text-sm text-gray-500 ml-9">
                  <div class="flex items-center">
                    <EyeIcon class="h-4 w-4 mr-1" />
                    {{ faq.views }} views
                  </div>
                  <div class="flex items-center">
                    <HandThumbUpIcon class="h-4 w-4 mr-1" />
                    {{ faq.helpful }} helpful
                  </div>
                  <div>Updated {{ formatDate(faq.updated_at) }}</div>
                  <span
                    v-if="faq.status === 'draft'"
                    class="px-2 py-1 bg-yellow-100 text-yellow-800 text-xs font-semibold rounded-full"
                  >
                    Draft
                  </span>
                </div>
              </div>

              <!-- Actions -->
              <div class="flex-shrink-0 flex gap-2">
                <button
                  @click="editFaq(faq)"
                  class="p-2 text-blue-600 hover:bg-blue-50 rounded-md transition-colors duration-200"
                  title="Edit"
                >
                  <PencilIcon class="h-5 w-5" />
                </button>
                <button
                  @click="duplicateFaq(faq)"
                  class="p-2 text-gray-600 hover:bg-gray-100 rounded-md transition-colors duration-200"
                  title="Duplicate"
                >
                  <DocumentDuplicateIcon class="h-5 w-5" />
                </button>
                <button
                  @click="deleteFaq(faq)"
                  class="p-2 text-red-600 hover:bg-red-50 rounded-md transition-colors duration-200"
                  title="Delete"
                >
                  <TrashIcon class="h-5 w-5" />
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-if="filteredFaqs.length === 0" class="bg-white rounded-lg shadow-sm border border-gray-200 p-12 text-center">
      <QuestionMarkCircleIcon class="mx-auto h-12 w-12 text-gray-400" />
      <h3 class="mt-2 text-sm font-medium text-gray-900">No FAQs found</h3>
      <p class="mt-1 text-sm text-gray-500">Get started by adding a new FAQ</p>
      <button
        @click="showCreateModal = true"
        class="mt-4 px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 transition-colors duration-200"
      >
        Add New FAQ
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import {
  PlusIcon,
  MagnifyingGlassIcon,
  QuestionMarkCircleIcon,
  CheckCircleIcon,
  EyeIcon,
  HandThumbUpIcon,
  PencilIcon,
  DocumentDuplicateIcon,
  TrashIcon
} from '@heroicons/vue/24/outline'

// Mock data
const faqs = ref([
  {
    id: 1,
    question: 'What is the Sauti Child Helpline?',
    answer: 'Sauti Child Helpline (116) is a free, toll-free helpline service available 24/7 for children, parents, and caregivers in Uganda. We provide support, counseling, and referrals for issues related to child protection, safety, and well-being.',
    category: 'General Information',
    status: 'published',
    views: 2847,
    helpful: 234,
    updated_at: '2024-10-15T10:00:00Z'
  },
  {
    id: 2,
    question: 'How do I call the helpline?',
    answer: 'Simply dial 116 from any phone in Uganda. The call is completely free and will not appear on your phone bill. Our trained counselors are available 24 hours a day, 7 days a week.',
    category: 'Using the Helpline',
    status: 'published',
    views: 1923,
    helpful: 189,
    updated_at: '2024-10-12T14:30:00Z'
  },
  {
    id: 3,
    question: 'Is the helpline really confidential?',
    answer: 'Yes, absolutely. All calls to the Sauti helpline are completely confidential. We do not record your personal information unless you choose to provide it for follow-up services. Your privacy and safety are our top priorities.',
    category: 'Using the Helpline',
    status: 'published',
    views: 1654,
    helpful: 156,
    updated_at: '2024-10-10T09:15:00Z'
  },
  {
    id: 4,
    question: 'What types of issues can I report?',
    answer: 'You can report any concern related to child safety including physical abuse, sexual abuse, emotional abuse, neglect, trafficking, child labor, online safety issues, bullying, and more. No issue is too small - if you\'re worried about a child\'s safety, please call.',
    category: 'Reporting Abuse',
    status: 'published',
    views: 1432,
    helpful: 128,
    updated_at: '2024-10-08T11:20:00Z'
  },
  {
    id: 5,
    question: 'What happens after I make a report?',
    answer: 'After you report, our team will assess the situation and take appropriate action. This may include providing immediate counseling, contacting emergency services, or referring the case to relevant authorities. We will keep you updated on the progress if you provide contact information.',
    category: 'Reporting Abuse',
    status: 'published',
    views: 1289,
    helpful: 112,
    updated_at: '2024-10-05T16:45:00Z'
  },
  {
    id: 6,
    question: 'How can I keep my child safe online?',
    answer: 'Monitor your child\'s internet use, teach them not to share personal information online, use parental controls, keep devices in common areas, and maintain open communication about their online activities. If you suspect online abuse or exploitation, report it immediately.',
    category: 'Child Safety',
    status: 'published',
    views: 1156,
    helpful: 98,
    updated_at: '2024-10-03T13:30:00Z'
  },
  {
    id: 7,
    question: 'What support services do you provide?',
    answer: 'We provide crisis counseling, emotional support, safety planning, referrals to medical care, legal assistance, police intervention when needed, shelter referrals, and follow-up services. Our goal is to ensure every child gets the help they need.',
    category: 'Support Services',
    status: 'published',
    views: 987,
    helpful: 84,
    updated_at: '2024-10-01T10:00:00Z'
  },
  {
    id: 8,
    question: 'Can I remain anonymous when reporting?',
    answer: 'Yes, you can make an anonymous report. However, providing your contact information helps us follow up with you and provide better support. All information you share is kept strictly confidential.',
    category: 'Reporting Abuse',
    status: 'published',
    views: 876,
    helpful: 72,
    updated_at: '2024-09-28T14:15:00Z'
  }
])

const stats = ref({
  total: 45,
  published: 38,
  views: 18724,
  helpful: 1543
})

const searchQuery = ref('')
const filterCategory = ref('')
const filterStatus = ref('')
const showCreateModal = ref(false)

const filteredFaqs = computed(() => {
  return faqs.value.filter(faq => {
    const matchesSearch = !searchQuery.value ||
      faq.question.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      faq.answer.toLowerCase().includes(searchQuery.value.toLowerCase())
    
    const matchesCategory = !filterCategory.value || faq.category === filterCategory.value
    const matchesStatus = !filterStatus.value || faq.status === filterStatus.value

    return matchesSearch && matchesCategory && matchesStatus
  })
})

const groupedFaqs = computed(() => {
  const groups = {}
  filteredFaqs.value.forEach(faq => {
    if (!groups[faq.category]) {
      groups[faq.category] = []
    }
    groups[faq.category].push(faq)
  })
  return groups
})

const formatDate = (date) => {
  return new Date(date).toLocaleDateString()
}

const editFaq = (faq) => {
  console.log('Edit FAQ:', faq)
}

const duplicateFaq = (faq) => {
  console.log('Duplicate FAQ:', faq)
}

const deleteFaq = (faq) => {
  if (confirm(`Delete this FAQ?`)) {
    console.log('Delete FAQ:', faq)
  }
}
</script>
