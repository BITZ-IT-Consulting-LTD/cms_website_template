<template>
  <div class="bg-gray-50 py-16">
    <div class="container-custom max-w-4xl">
      <!-- Heading -->
      <div class="text-center mb-10">
        <h1 class="text-4xl md:text-5xl font-extrabold mb-3">Frequently Asked Questions</h1>
        <p class="text-gray-600 max-w-2xl mx-auto">Find answers to common questions about our services and how we help children in Uganda.</p>
      </div>

      <!-- Search -->
      <div class="mb-8">
        <div class="relative">
          <input v-model="query" type="text" placeholder="Search for a question..." class="w-full px-5 py-4 rounded-2xl border border-gray-200 bg-white shadow-sm pl-12 focus:ring-2 focus:ring-primary-500 focus:border-primary-500" />
          <svg class="w-5 h-5 text-gray-400 absolute left-4 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35M10 18a8 8 0 100-16 8 8 0 000 16z"/></svg>
        </div>
      </div>

      <Loader v-if="loading" />

      <!-- Accordion list -->
      <div v-else-if="filteredFaqs.length" class="space-y-4">
        <div v-for="(faq, index) in filteredFaqs" :key="faq.id || index" class="bg-white rounded-2xl border border-gray-200 shadow-sm">
          <button @click="toggleFaq(index)" class="w-full text-left p-6 flex justify-between items-center">
            <span class="font-semibold text-gray-900">{{ faq.question }}</span>
            <svg class="w-5 h-5 text-gray-500 transition-transform" :class="{ 'rotate-180': openFaq === index }" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
            </svg>
          </button>
          <Transition name="fade">
            <div v-if="openFaq === index" class="px-6 pb-6 text-gray-600">
              {{ faq.answer }}
            </div>
          </Transition>
        </div>
      </div>

      <p v-else class="text-center text-gray-600">No FAQs available yet.</p>

      <!-- Footer links -->
      <div class="text-center text-sm text-gray-500 mt-10">
        <router-link to="/privacy" class="hover:text-gray-700">Privacy Policy</router-link>
        <span class="mx-2">•</span>
        <router-link to="/terms" class="hover:text-gray-700">Terms of Service</router-link>
        <span class="mx-2">•</span>
        <router-link to="/contact" class="hover:text-gray-700">Contact Us</router-link>
        <p class="mt-2">© 2024 Sauti Uganda. All rights reserved. A sanctuary for every child.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useFaqsStore } from '@/store/faqs'
import Loader from '@/components/common/Loader.vue'

const faqsStore = useFaqsStore()
const faqs = ref([])
const loading = ref(true)
const openFaq = ref(null)
const query = ref('')

onMounted(async () => {
  try {
    await faqsStore.fetchFaqs()
    faqs.value = faqsStore.faqs
  } finally {
    loading.value = false
  }
})

const filteredFaqs = computed(() => {
  const q = query.value.trim().toLowerCase()
  if (!q) return faqs.value
  return faqs.value.filter(f =>
    String(f.question).toLowerCase().includes(q) || String(f.answer).toLowerCase().includes(q)
  )
})

function toggleFaq(index) {
  openFaq.value = openFaq.value === index ? null : index
}
</script>
