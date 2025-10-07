<template>
  <div class="bg-green-50/60 py-16">
    <div class="container-custom">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        <!-- Left visuals -->
        <div class="lg:col-span-5 order-2 lg:order-1 space-y-5">
          <div class="rounded-3xl bg-gray-200 h-72"></div>
          <div class="rounded-3xl bg-gray-200 h-40"></div>
          <div class="rounded-3xl bg-gray-200 h-80 ring-4 ring-blue-400"></div>

          <!-- Ready to Serve card -->
          <div class="mt-4 flex items-center gap-4 rounded-2xl border border-green-300 bg-white p-4 shadow-sm">
            <div class="h-12 w-12 rounded-full bg-green-500 text-white flex items-center justify-center">
              <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M12 2a10 10 0 100 20 10 10 0 000-20zm2.5 14.5l-3-3V7"/></svg>
            </div>
            <div>
              <p class="font-semibold text-gray-900">Ready to Serve</p>
              <p class="text-gray-500 text-sm">Our team is here to help.</p>
            </div>
          </div>
        </div>

        <!-- Right content -->
        <div class="lg:col-span-7 order-1 lg:order-2">
          <p class="text-sm uppercase tracking-widest text-green-700 font-semibold">Ask Question</p>
          <h1 class="text-4xl md:text-5xl font-extrabold leading-tight text-green-900 mt-2">Ask Us Your Migration Questions</h1>

          <!-- Search -->
          <div class="mt-8 mb-4">
            <div class="relative">
              <input v-model="query" type="text" placeholder="Search questions" class="w-full px-5 py-4 rounded-2xl border border-gray-200 bg-white shadow-sm pl-12 focus:ring-2 focus:ring-primary-500 focus:border-primary-500" />
              <svg class="w-5 h-5 text-gray-400 absolute left-4 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35M10 18a8 8 0 100-16 8 8 0 000 16z"/></svg>
            </div>
          </div>

          <Loader v-if="loading" />

          <!-- Accordion list styled like design -->
          <div v-else>
            <div v-if="filteredFaqs.length" class="space-y-4">
              <div
                v-for="(faq, index) in filteredFaqs"
                :key="faq.id || index"
                class="rounded-2xl border border-gray-200 bg-white shadow-sm overflow-hidden"
              >
                <button @click="toggleFaq(index)" class="w-full text-left px-6 py-5 flex justify-between items-center">
                  <span class="font-semibold text-gray-900">{{ faq.question }}</span>
                  <span class="inline-flex h-9 w-9 items-center justify-center rounded-full bg-green-100 text-green-700">
                    <svg class="w-5 h-5 transition-transform" :class="{ 'rotate-180': openFaq === index }" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                  </span>
                </button>
                <Transition name="fade">
                  <div v-if="openFaq === index" class="px-6 pb-6 text-gray-600">
                    {{ faq.answer }}
                  </div>
                </Transition>
              </div>
            </div>
            <p v-else class="text-gray-600">No FAQs available yet.</p>
          </div>

          <!-- Footer links -->
          <div class="text-sm text-gray-500 mt-10">
            <router-link to="/privacy" class="hover:text-gray-700">Privacy Policy</router-link>
            <span class="mx-2">•</span>
            <router-link to="/terms" class="hover:text-gray-700">Terms of Service</router-link>
            <span class="mx-2">•</span>
            <router-link to="/contact" class="hover:text-gray-700">Contact Us</router-link>
            <p class="mt-2">© 2024 Sauti Uganda. All rights reserved. A sanctuary for every child.</p>
          </div>
        </div>
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

// Default FAQs to include in addition to API-provided FAQs
const defaultFaqs = [
  {
    id: 'local-1',
    question: 'How much does it cost to call the helpline?\u200b',
    answer:
      'Our services are completely free of charge. The call to our helpline is toll-free from all major networks in Uganda. No airtime is required to reach us on 116.',
  },
  {
    id: 'local-2',
    question: 'What services do you offer?',
    answer:
      'We offer counseling, guidance, referrals to partner services, and follow-up support for children and families in need of protection and welfare.',
  },
  {
    id: 'local-3',
    question: 'How can I report abuse?',
    answer:
      'Dial 116 or submit an anonymous report on this website via the Report page. Share as much detail as you can so we can help quickly and safely.',
  },
  {
    id: 'local-4',
    question: 'Is my information kept confidential?',
    answer:
      'Yes. We protect your privacy and only share information with authorized partners when necessary to keep a child safe.',
  },
  {
    id: 'local-5',
    question: 'What age group do you serve?',
    answer:
      'We primarily serve children and young people, but we also support parents, guardians, and community members seeking help for a child.',
  },
]

onMounted(async () => {
  try {
    await faqsStore.fetchFaqs()
    // Merge API FAQs with default FAQs, avoiding duplicates by question text
    const apiFaqs = Array.isArray(faqsStore.faqs) ? faqsStore.faqs : []
    const existingQuestions = new Set(apiFaqs.map(f => String(f.question).trim().toLowerCase()))
    const extras = defaultFaqs.filter(d => !existingQuestions.has(String(d.question).trim().toLowerCase()))
    faqs.value = [...apiFaqs, ...extras]
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
