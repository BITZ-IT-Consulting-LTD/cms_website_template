<template>
  <div class="space-y-12">
    <!-- 1. Category Filter -->
    <div v-if="categories && categories.length > 0"
      class="bg-neutral-white rounded-[2.5rem] border-2 border-neutral-offwhite p-8 shadow-sm">
      <h2 class="campaign-header text-sm text-secondary mb-6 opacity-40">Knowledge Base Categories</h2>
      <div class="flex flex-wrap gap-3">
        <button @click="selectCategory(null)" :class="[
          'px-6 py-2.5 rounded-full text-[10px] font-bold uppercase tracking-widest transition-all duration-300 border-2',
          selectedCategory === null
            ? 'bg-primary border-primary text-neutral-white shadow-lg scale-105'
            : 'bg-neutral-white border-neutral-offwhite text-black/50 hover:border-primary hover:text-primary'
        ]">
          All Topics
        </button>
        <button v-for="cat in categories" :key="cat.slug" @click="selectCategory(cat.slug)" :class="[
          'px-6 py-2.5 rounded-full text-[10px] font-bold uppercase tracking-widest transition-all duration-300 border-2',
          selectedCategory === cat.slug
            ? 'bg-primary border-primary text-neutral-white shadow-xl scale-105'
            : 'bg-neutral-white border-neutral-offwhite text-black/50 hover:border-primary hover:text-primary'
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
    <div v-else-if="error" class="bg-emergency/5 border-2 border-emergency/20 rounded-[2.5rem] p-12 text-center">
      <ExclamationTriangleIcon class="w-12 h-12 text-emergency mx-auto mb-6" />
      <p class="text-black/70 font-bold mb-8">{{ error }}</p>
      <BaseCTA @click="$emit('retry')" variant="primary">
        Try Reconnecting
      </BaseCTA>
    </div>

    <!-- 4. Empty State -->
    <div v-else-if="filteredFaqs.length === 0"
      class="bg-neutral-offwhite border-2 border-dashed border-neutral-offwhite rounded-[3rem] p-16 text-center">
      <QuestionMarkCircleIcon class="w-16 h-16 mx-auto text-secondary/20 mb-6" />
      <h3 class="campaign-header text-xl text-secondary mb-4">No insights found</h3>
      <p class="text-lg font-bold text-black/40">
        {{ selectedCategory ? 'There are currently no listed questions in this category.' : 'Check back later as we update our knowledge base.' }}
      </p>
    </div>

    <!-- 5. FAQ Accordion Grid -->
    <div v-else class="space-y-4">
      <div v-for="(faq, index) in filteredFaqs" :key="faq.id"
        class="rounded-[2rem] transition-all duration-500 overflow-hidden"
        :class="openIndex === index ? 'bg-neutral-white shadow-xl' : 'bg-neutral-white shadow-sm hover:shadow-md'">
        <!-- Question Toggle -->
        <button @click="toggleFaq(index)"
          class="w-full px-8 py-6 text-left flex items-start justify-between gap-6 group"
          :aria-expanded="openIndex === index">
          <div class="flex-1">
            <!-- Badges -->
            <div class="flex items-center gap-3 mb-4">
              <span v-if="faq.category" class="pill bg-primary/10 text-primary text-[8px]">
                {{ faq.category.name }}
              </span>
              <span v-if="faq.language" class="pill bg-neutral-offwhite text-muted text-[8px]">
                {{ getLanguageName(faq.language) }}
              </span>
            </div>

            <!-- Question Text -->
            <h3
              class="text-xl md:text-2xl font-bold text-secondary leading-tight group-hover:text-primary transition-colors">
              {{ faq.question }}
            </h3>
          </div>

          <!-- Icon -->
          <div
            :class="['w-10 h-10 rounded-xl flex items-center justify-center transition-all duration-500 shrink-0', openIndex === index ? 'bg-primary text-neutral-white rotate-180' : 'bg-neutral-offwhite text-primary group-hover:bg-primary/10']">
            <ChevronDownIcon class="w-6 h-6" stroke-width="3" />
          </div>
        </button>

        <!-- Answer Content -->
        <transition name="accordion" @enter="enter" @leave="leave">
          <div v-show="openIndex === index" class="px-8 pb-8">
            <div class="pt-8 border-t-2 border-neutral-offwhite">
              <div
                class="text-lg md:text-xl font-bold text-black/70 leading-relaxed whitespace-pre-line prose-faq"
                v-html="faq.answer"></div>

              <!-- Metadata footer -->
              <div v-if="faq.views_count" class="mt-8 flex items-center gap-3">
                <div class="w-8 h-8 rounded-lg bg-neutral-offwhite flex items-center justify-center text-primary">
                  <EyeIcon class="w-4 h-4" />
                </div>
                <span class="campaign-header text-[10px] text-secondary/30">Verified and viewed {{ faq.views_count
                  }} times</span>
              </div>
            </div>
          </div>
        </transition>
      </div>
    </div>

    <!-- 6. Help Banner Overlay -->
    <div class="bg-secondary p-10 md:p-16 rounded-[4rem] text-neutral-white shadow-2xl relative overflow-hidden">
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-primary/10 rounded-full blur-3xl"></div>
      <div class="relative z-10 flex flex-col md:flex-row items-center md:items-start gap-12 text-center md:text-left">
        <div
          class="w-16 h-16 bg-neutral-white/10 rounded-[1.5rem] flex items-center justify-center shrink-0 border border-neutral-white/20">
          <InformationCircleIcon class="w-8 h-8 text-primary" />
        </div>
        <div class="flex-1">
          <h3 class="campaign-header text-2xl text-neutral-white mb-4">Didn't find your answer?</h3>
          <p class="text-lg font-bold text-neutral-white/50 mb-10 leading-relaxed">
            Our professional support team is available 24/7 to provide personalized assistance for your specific
            situation.
          </p>
          <div class="cta-group justify-center md:justify-start">
            <BaseCTA href="tel:116" variant="primary"
              class="!bg-neutral-white !text-secondary hover:!bg-primary hover:!text-neutral-white">Call 116</BaseCTA>
            <BaseCTA href="/contact" variant="outline" class="text-neutral-white border-neutral-white/20">Message Support</BaseCTA>
            <BaseCTA href="/report" variant="outline" class="text-neutral-white border-neutral-white/20">Log Statement</BaseCTA>
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
