<template>
  <div class="section-padding">
    <div class="container-custom max-w-4xl">
      <h1 class="text-center mb-12">Frequently Asked Questions</h1>
      
      <Loader v-if="loading" />
      
      <div v-else-if="faqs.length" class="space-y-4">
        <div v-for="(faq, index) in faqs" :key="faq.id" class="card">
          <button
            @click="toggleFaq(index)"
            class="w-full text-left p-6 flex justify-between items-center hover:bg-gray-50 transition-colors"
          >
            <span class="font-semibold text-gray-900">{{ faq.question }}</span>
            <svg
              class="w-5 h-5 text-gray-500 transition-transform"
              :class="{ 'rotate-180': openFaq === index }"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
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
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useFaqsStore } from '@/store/faqs'
import Loader from '@/components/common/Loader.vue'

const faqsStore = useFaqsStore()
const faqs = ref([])
const loading = ref(true)
const openFaq = ref(null)

onMounted(async () => {
  try {
    await faqsStore.fetchFaqs()
    faqs.value = faqsStore.faqs
  } finally {
    loading.value = false
  }
})

function toggleFaq(index) {
  openFaq.value = openFaq.value === index ? null : index
}
</script>
