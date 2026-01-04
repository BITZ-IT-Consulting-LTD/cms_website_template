<template>
  <div class="space-y-12">
    <!-- 1. Category Filter -->
    <div v-if="categories && categories.length > 0"
      class="bg-sauti-white rounded-[2.5rem] border-2 border-sauti-neutral p-8 shadow-sm">
      <h2 class="campaign-header text-sm text-sauti-darkGreen mb-6 opacity-40">Knowledge Base Categories</h2>
      <div class="flex flex-wrap gap-3">
        <button @click="selectCategory(null)" :class="[
          'px-6 py-2.5 rounded-full text-[10px] font-bold uppercase tracking-widest transition-all duration-300 border-2',
          selectedCategory === null
            ? 'bg-sauti-blue border-sauti-blue text-sauti-white shadow-lg scale-105'
            : 'bg-sauti-white border-sauti-neutral text-sauti-darkGreen/50 hover:border-sauti-blue hover:text-sauti-blue'
        ]">
          All Topics
        </button>
        <button v-for="cat in categories" :key="cat.slug" @click="selectCategory(cat.slug)" :class="[
          'px-6 py-2.5 rounded-full text-[10px] font-bold uppercase tracking-widest transition-all duration-300 border-2',
          selectedCategory === cat.slug
            ? 'bg-sauti-blue border-sauti-blue text-sauti-white shadow-xl scale-105'
            : 'bg-sauti-white border-sauti-neutral text-sauti-darkGreen/50 hover:border-sauti-blue hover:text-sauti-blue'
        ]">
          {{ cat.name }}
        </button>
      </div>
    </div>

    <!-- 2. Loading State -->
    <div v-if="loading" class="flex justify-center py-20">
      <div class="spinner"></div>
    </div>

    <!-- 3. Error State -->
    <div v-else-if="error" class="bg-sauti-red/5 border-2 border-sauti-red/20 rounded-[2.5rem] p-12 text-center">
      <ExclamationTriangleIcon class="w-12 h-12 text-sauti-red mx-auto mb-6" />
      <p class="text-sauti-darkGreen/70 font-bold mb-8">{{ error }}</p>
      <BaseCTA @click="$emit('retry')" variant="primary">
        Try Reconnecting
      </BaseCTA>
    </div>

    <!-- 4. Empty State -->
    <div v-else-if="filteredFaqs.length === 0"
      class="bg-sauti-neutral/10 border-2 border-dashed border-sauti-neutral rounded-[3rem] p-16 text-center">
      <QuestionMarkCircleIcon class="w-16 h-16 mx-auto text-sauti-darkGreen/20 mb-6" />
      <h3 class="campaign-header text-xl text-sauti-darkGreen mb-4">No insights found</h3>
      <p class="text-lg font-bold text-sauti-darkGreen/40">
        {{ selectedCategory ? 'There are currently no listed questions in this category.' : 'Check back later as we
        update our knowledge base.' }}
      </p>
    </div>

    <!-- 5. FAQ Accordion Grid -->
    <div v-else class="space-y-4">
      <div v-for="(faq, index) in filteredFaqs" :key="faq.id"
        class="rounded-[2rem] transition-all duration-500 overflow-hidden"
        :class="openIndex === index ? 'bg-white shadow-xl' : 'bg-white shadow-sm hover:shadow-md'">
        <!-- Question Toggle -->
        <button @click="toggleFaq(index)"
          class="w-full px-8 py-6 text-left flex items-start justify-between gap-6 group"
          :aria-expanded="openIndex === index">
          <div class="flex-1">
            <!-- Badges -->
            <div class="flex items-center gap-3 mb-4">
              <span v-if="faq.category" class="pill bg-sauti-blue/10 text-sauti-blue text-[8px]">
                {{ faq.category.name }}
              </span>
              <span v-if="faq.language" class="pill bg-sauti-neutral/50 text-sauti-darkGreen/60 text-[8px]">
                {{ getLanguageName(faq.language) }}
              </span>
            </div>

            <!-- Question Text -->
            <h3
              class="text-xl md:text-2xl font-bold text-sauti-darkGreen leading-tight group-hover:text-sauti-blue transition-colors">
              {{ faq.question }}
            </h3>
          </div>

          <!-- Icon -->
          <div
            :class="['w-10 h-10 rounded-xl flex items-center justify-center transition-all duration-500 shrink-0', openIndex === index ? 'bg-sauti-blue text-white rotate-180' : 'bg-sauti-neutral text-sauti-blue group-hover:bg-sauti-blue/10']">
            <ChevronDownIcon class="w-6 h-6" stroke-width="3" />
          </div>
        </button>

        <!-- Answer Content -->
        <transition name="accordion" @enter="enter" @leave="leave">
          <div v-show="openIndex === index" class="px-8 pb-8">
            <div class="pt-8 border-t-2 border-sauti-neutral/30">
              <div
                class="text-lg md:text-xl font-bold text-sauti-darkGreen/70 leading-relaxed whitespace-pre-line prose-faq"
                v-html="faq.answer"></div>

              <!-- Metadata footer -->
              <div v-if="faq.views_count" class="mt-8 flex items-center gap-3">
                <div class="w-8 h-8 rounded-lg bg-sauti-neutral/50 flex items-center justify-center text-sauti-blue">
                  <EyeIcon class="w-4 h-4" />
                </div>
                <span class="campaign-header text-[10px] text-sauti-darkGreen/30">Verified and viewed {{ faq.views_count
                  }} times</span>
              </div>
            </div>
          </div>
        </transition>
      </div>
    </div>

    <!-- 6. Help Banner Overlay -->
    <div class="bg-sauti-darkGreen p-10 md:p-16 rounded-[4rem] text-sauti-white shadow-2xl relative overflow-hidden">
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-sauti-blue/10 rounded-full blur-3xl"></div>
      <div class="relative z-10 flex flex-col md:flex-row items-center md:items-start gap-12 text-center md:text-left">
        <div
          class="w-16 h-16 bg-white/10 rounded-[1.5rem] flex items-center justify-center shrink-0 border border-white/20">
          <InformationCircleIcon class="w-8 h-8 text-sauti-blue" />
        </div>
        <div class="flex-1">
          <h3 class="campaign-header text-2xl text-white mb-4">Didn't find your answer?</h3>
          <p class="text-lg font-bold text-white/50 mb-10 leading-relaxed">
            Our professional support team is available 24/7 to provide personalized assistance for your specific
            situation.
          </p>
          <div class="cta-group justify-center md:justify-start">
            <BaseCTA href="tel:116" variant="primary"
              class="!bg-sauti-white !text-sauti-darkGreen hover:!bg-sauti-blue hover:!text-white">Call 116</BaseCTA>
            <BaseCTA href="/contact" variant="outline" class="text-white border-white/20">Message Support</BaseCTA>
            <BaseCTA href="/report" variant="outline" class="text-white border-white/20">Log Statement</BaseCTA>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import BaseCTA from '../common/BaseCTA.vue'
  import {
    ChevronDownIcon,
    QuestionMarkCircleIcon,
    EyeIcon,
    InformationCircleIcon,
    ExclamationTriangleIcon
  } from '@heroicons/vue/24/outline'

  const props = defineProps({
    faqs: { type: Array, default: () => [] },
    categories: { type: Array, default: () => [] },
    loading: { type: Boolean, default: false },
    error: { type: String, default: null }
  })

  const emit = defineEmits(['retry', 'view'])

  const openIndex = ref(null)
  const selectedCategory = ref(null)

  const filteredFaqs = computed(() => {
    if (!selectedCategory.value) return props.faqs
    return props.faqs.filter(faq => faq.category?.slug === selectedCategory.value)
  })

  const toggleFaq = (index) => {
    if (openIndex.value === index) {
      openIndex.value = null
    } else {
      openIndex.value = index
      emit('view', filteredFaqs.value[index])
    }
  }

  const selectCategory = (categorySlug) => {
    selectedCategory.value = categorySlug
    openIndex.value = null
  }

  const getLanguageName = (code) => {
    const languages = { en: 'English', lg: 'Luganda', sw: 'Swahili' }
    return languages[code] || code.toUpperCase()
  }

  // Animation helpers
  const enter = (el) => {
    el.style.height = '0'
    el.style.overflow = 'hidden'
    requestAnimationFrame(() => {
      el.style.height = el.scrollHeight + 'px'
      el.style.transition = 'height 0.3s cubic-bezier(0.4, 0, 0.2, 1)'
    })
  }

  const leave = (el) => {
    el.style.height = el.scrollHeight + 'px'
    el.style.overflow = 'hidden'
    requestAnimationFrame(() => {
      el.style.height = '0'
      el.style.transition = 'height 0.3s cubic-bezier(0.4, 0, 0.2, 1)'
    })
  }
</script>

<style scoped>

  .accordion-enter-active,
  .accordion-leave-active {
    overflow: hidden;
  }

  :deep(.prose-faq p) {
    margin-bottom: 1.5rem;
  }

  :deep(.prose-faq p:last-child) {
    margin-bottom: 0;
  }
</style>
