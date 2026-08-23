<template>
  <div class="min-h-screen bg-white">
    <header class="hero-banner" style="padding-top: clamp(70px, 15vw, 90px);">
      <div class="hero-overlay"></div>
      <div class="container-custom hero-content-wrapper">
        <div class="hero-text">
          <h1 class="hero-title">
            {{ siteContent.getContent('faqs_page_title', 'Frequently Asked') }}
            <span class="text-accent-yellow">{{ siteContent.getContent('faqs_page_title_highlight', 'Questions') }}</span>
          </h1>
          <p class="hero-subtitle">
            {{ siteContent.getContent('faqs_page_subtitle', 'Find answers to common questions about our services, child protection, and how we can support you.') }}
          </p>
        </div>
      </div>
    </header>

    <section class="bg-warm">
      <div class="container-custom section-padding !pt-10 md:!pt-14">
        <div class="faq-layout">

          <!-- Sidebar: support + category nav -->
          <aside class="faq-sidebar order-2 lg:order-1 space-y-5 lg:sticky lg:top-28 lg:self-start">
            <div class="support-card relative overflow-hidden rounded-2xl bg-secondary p-5 lg:p-6 text-neutral-white">
              <div class="support-card__glow" aria-hidden="true"></div>
              <div class="relative z-10 flex items-start gap-3">
                <div class="w-10 h-10 rounded-xl bg-neutral-white/10 border border-neutral-white/15 flex items-center justify-center shrink-0">
                  <Headphones class="w-5 h-5 text-accent-yellow" />
                </div>
                <div class="min-w-0">
                  <h3 class="text-base lg:text-lg font-bold tracking-tight">{{ faqsSupportTitle }}</h3>
                  <p class="text-xs lg:text-sm text-neutral-white/70 font-semibold mt-0.5">{{ faqsSupportSubtitle }}</p>
                </div>
              </div>
            </div>

            <div class="rounded-2xl bg-neutral-white border border-emergency/10 p-5 space-y-4 shadow-sm">
              <div class="flex items-start gap-3">
                <div class="w-9 h-9 rounded-lg bg-emergency/10 text-emergency flex items-center justify-center shrink-0">
                  <Phone class="w-4 h-4" />
                </div>
                <div class="min-w-0">
                  <h4 class="text-sm lg:text-base font-bold text-emergency">{{ faqsImmediateHelpTitle }}</h4>
                  <p class="text-xs text-black/55 font-semibold mt-0.5">{{ faqsImmediateHelpSubtitle }}</p>
                </div>
              </div>
              <BaseCTA :href="`tel:116`" variant="emergency" class="w-full justify-center !py-2.5 font-bold text-sm" external>
                {{ faqsCallButton }}
              </BaseCTA>
            </div>

            <!-- Desktop category nav -->
            <nav
              v-if="categories.length"
              class="hidden lg:block rounded-2xl bg-neutral-white border border-black/[0.05] p-3 shadow-sm"
              aria-label="Browse by topic"
            >
              <p class="px-3 pt-1 pb-2 text-[10px] font-bold uppercase tracking-wider text-secondary/40">
                Browse by topic
              </p>
              <ul class="space-y-0.5">
                <li>
                  <button
                    type="button"
                    class="cat-link"
                    :class="{ 'cat-link--active': selectedCategory === '' }"
                    @click="selectCategory('')"
                  >
                    <span>{{ faqsAllCategoriesButton }}</span>
                    <span class="cat-count">{{ faqs.length }}</span>
                  </button>
                </li>
                <li v-for="category in categories" :key="category.id">
                  <button
                    type="button"
                    class="cat-link"
                    :class="{ 'cat-link--active': selectedCategory === category.id }"
                    @click="selectCategory(category.id)"
                  >
                    <span class="truncate">{{ category.name }}</span>
                    <span class="cat-count">{{ categoryCount(category.id) }}</span>
                  </button>
                </li>
              </ul>
            </nav>
          </aside>

          <!-- Main -->
          <div class="faq-main order-1 lg:order-2 min-w-0">
            <!-- Sticky toolbar -->
            <div class="faq-toolbar sticky top-[70px] z-20 -mx-1 px-1 pb-4 pt-1 mb-2 bg-warm/95 backdrop-blur-md space-y-3">
              <div class="relative">
                <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                  <Search class="h-4 w-4 text-primary/40" />
                </div>
                <input
                  v-model="query"
                  type="search"
                  :placeholder="faqsSearchPlaceholder"
                  class="w-full pl-11 pr-10 py-3 bg-neutral-white rounded-xl text-secondary font-semibold placeholder:text-black/30 focus:outline-none focus:ring-2 focus:ring-primary/25 text-sm border border-black/5 shadow-sm"
                />
                <button
                  v-if="query"
                  type="button"
                  class="absolute inset-y-0 right-0 pr-4 flex items-center text-black/30 hover:text-secondary"
                  aria-label="Clear search"
                  @click="query = ''"
                >
                  <X class="w-4 h-4" />
                </button>
              </div>

              <!-- Mobile category chips -->
              <div v-if="categories.length" class="lg:hidden overflow-x-auto hide-scrollbar -mx-1 px-1">
                <div class="flex gap-2 pb-0.5">
                  <button
                    type="button"
                    :class="selectedCategory === '' ? 'chip-active' : 'chip-idle'"
                    class="chip"
                    @click="selectCategory('')"
                  >
                    {{ faqsAllCategoriesButton }}
                  </button>
                  <button
                    v-for="category in categories"
                    :key="category.id"
                    type="button"
                    :class="selectedCategory === category.id ? 'chip-active' : 'chip-idle'"
                    class="chip"
                    @click="selectCategory(category.id)"
                  >
                    {{ category.name }}
                  </button>
                </div>
              </div>

              <div v-if="!loading && filteredFaqs.length" class="flex flex-wrap items-center justify-between gap-2 text-xs font-semibold text-secondary/50">
                <span>{{ resultsSummary }}</span>
                <span v-if="totalPages > 1">Page {{ currentPage }} of {{ totalPages }}</span>
              </div>
            </div>

            <AppLoader v-if="loading" />

            <div v-else>
              <!-- Compact accordion list -->
              <div v-if="paginatedFaqs.length" class="faq-list rounded-2xl bg-neutral-white border border-black/[0.05] shadow-sm overflow-hidden divide-y divide-neutral-offwhite">
                <article
                  v-for="faq in paginatedFaqs"
                  :key="faq.id"
                  class="faq-row"
                  :class="{ 'faq-row--open': openFaqId === faq.id }"
                >
                  <button
                    type="button"
                    class="faq-row__trigger"
                    :aria-expanded="openFaqId === faq.id"
                    :aria-controls="`faq-answer-${faq.id}`"
                    :id="`faq-question-${faq.id}`"
                    @click="toggleFaq(faq.id)"
                  >
                    <span class="faq-row__question">{{ faq.question }}</span>
                    <span class="faq-row__meta">
                      <span v-if="!selectedCategory && faq.category_name" class="faq-row__badge">{{ faq.category_name }}</span>
                      <span
                        class="faq-row__chevron"
                        :class="{ 'faq-row__chevron--open': openFaqId === faq.id }"
                      >
                        <ChevronDown class="w-4 h-4" stroke-width="2.5" />
                      </span>
                    </span>
                  </button>

                  <transition name="accordion" @enter="enter" @leave="leave">
                    <div
                      v-show="openFaqId === faq.id"
                      :id="`faq-answer-${faq.id}`"
                      role="region"
                      :aria-labelledby="`faq-question-${faq.id}`"
                      class="faq-row__answer"
                    >
                      <p>{{ faq.answer }}</p>
                    </div>
                  </transition>
                </article>
              </div>

              <!-- Pagination -->
              <div v-if="totalPages > 1" class="flex items-center justify-center gap-2 mt-6">
                <button
                  type="button"
                  class="page-nav"
                  :disabled="currentPage <= 1"
                  aria-label="Previous page"
                  @click="goToPage(currentPage - 1)"
                >
                  <ChevronLeft class="w-4 h-4" />
                </button>

                <div class="flex items-center gap-1">
                  <button
                    v-for="n in pageNumbers"
                    :key="'pg-' + n"
                    type="button"
                    :class="['page-btn', currentPage === n ? 'page-btn--active' : 'page-btn--idle']"
                    @click="goToPage(n)"
                  >
                    {{ n }}
                  </button>
                </div>

                <button
                  type="button"
                  class="page-nav"
                  :disabled="currentPage >= totalPages"
                  aria-label="Next page"
                  @click="goToPage(currentPage + 1)"
                >
                  <ChevronRight class="w-4 h-4" />
                </button>
              </div>

              <!-- Empty -->
              <div v-if="!filteredFaqs.length" class="empty-state text-center py-14 px-6 rounded-2xl bg-neutral-white border border-dashed border-black/10">
                <div class="w-14 h-14 mx-auto bg-primary/10 rounded-xl flex items-center justify-center mb-5">
                  <Search class="w-7 h-7 text-primary/70" />
                </div>
                <h3 class="text-lg font-bold text-secondary mb-2">{{ faqsNoResults }}</h3>
                <p class="text-sm text-black/50 font-semibold mb-6 max-w-sm mx-auto">{{ faqsNoResultsSubtitle }}</p>
                <button
                  type="button"
                  class="px-6 py-2.5 bg-secondary text-neutral-white rounded-full font-bold uppercase tracking-wider text-xs hover:brightness-110 transition-all"
                  @click="clearFilters"
                >
                  Clear all filters
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="help-banner mt-10 lg:mt-14 relative overflow-hidden rounded-2xl lg:rounded-3xl bg-secondary text-neutral-white">
          <div class="help-banner__orb help-banner__orb--a" aria-hidden="true"></div>
          <div class="relative z-10 flex flex-col sm:flex-row items-center gap-6 p-6 md:p-10 text-center sm:text-left">
            <div class="w-12 h-12 rounded-xl bg-neutral-white/10 border border-neutral-white/15 flex items-center justify-center shrink-0">
              <MessageCircle class="w-6 h-6 text-accent-yellow" />
            </div>
            <div class="flex-1 min-w-0">
              <h3 class="text-lg lg:text-xl font-bold">Didn't find your answer?</h3>
              <p class="text-sm text-neutral-white/65 font-semibold mt-1">Call 116 or send us a message — we're here 24/7.</p>
            </div>
            <div class="flex gap-2 shrink-0">
              <BaseCTA href="tel:116" variant="primary" external class="!bg-neutral-white !text-secondary hover:!bg-accent-yellow !text-sm !px-5">
                Call 116
              </BaseCTA>
              <BaseCTA to="/contact" variant="outline" class="!border-neutral-white/30 !text-neutral-white hover:!bg-neutral-white/10 !text-sm !px-5">
                Contact
              </BaseCTA>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
  import { ref, computed, onMounted, watch } from 'vue'
  import { useFaqsStore } from '@/store/faqs'
  import { useSettingsStore } from '@/store/settings'
  import { useSiteContent } from '@/composables/useSiteContent'
  import AppLoader from '@/components/common/AppLoader.vue'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import {
    Search,
    ChevronDown,
    ChevronLeft,
    ChevronRight,
    Phone,
    Headphones,
    MessageCircle,
    X
  } from 'lucide-vue-next'

  defineOptions({ name: 'FaqsPage' })

  const PAGE_SIZE = 10

  const faqsStore = useFaqsStore()
  const settingsStore = useSettingsStore()
  const siteContent = useSiteContent('faqs')
  const faqs = ref([])
  const categories = ref([])
  const loading = ref(true)
  const openFaqId = ref(null)
  const query = ref('')
  const selectedCategory = ref('')
  const currentPage = ref(1)

  const faqsSupportTitle = computed(() => siteContent.getContent('faqs_support_title', '24/7 Support'))
  const faqsSupportSubtitle = computed(() => siteContent.getContent('faqs_support_subtitle', 'Always here to help'))
  const faqsImmediateHelpTitle = computed(() => siteContent.getContent('faqs_immediate_help_title', 'Need Immediate Help?'))
  const faqsImmediateHelpSubtitle = computed(() => siteContent.getContent('faqs_immediate_help_subtitle', 'Call our toll-free helpline'))
  const faqsCallButton = computed(() => siteContent.getContent('faqs_call_button', 'Call 116'))
  const faqsSearchPlaceholder = computed(() => siteContent.getContent('faqs_search_placeholder', 'Search questions'))
  const faqsAllCategoriesButton = computed(() => siteContent.getContent('faqs_all_categories_button', 'All Categories'))
  const faqsNoResults = computed(() => siteContent.getContent('faqs_no_results', 'No FAQs found'))
  const faqsNoResultsSubtitle = computed(() => siteContent.getContent('faqs_no_results_subtitle', 'Try adjusting your search or category filter'))

  onMounted(async () => {
    await siteContent.fetchContent()
    await settingsStore.fetchGlobalSettings()
    try {
      await faqsStore.fetchFaqs({ status: 'PUBLISHED' })
      faqs.value = Array.isArray(faqsStore.faqs) ? faqsStore.faqs : []

      try {
        const fetchedCategories = await faqsStore.fetchCategories()
        categories.value = Array.isArray(fetchedCategories) && fetchedCategories.length
          ? fetchedCategories
          : extractCategoriesFromFaqs()
      } catch {
        categories.value = extractCategoriesFromFaqs()
      }
    } catch (error) {
      console.error('Error fetching FAQs:', error)
      faqs.value = []
    } finally {
      loading.value = false
    }
  })

  watch([query, selectedCategory], () => {
    currentPage.value = 1
    openFaqId.value = null
  })

  function extractCategoriesFromFaqs() {
    const categoryMap = new Map()
    faqs.value.forEach(faq => {
      if (faq.category_name && !categoryMap.has(faq.category)) {
        categoryMap.set(faq.category, { id: faq.category, name: faq.category_name })
      }
    })
    return Array.from(categoryMap.values())
  }

  function categoryCount(categoryId) {
    return faqs.value.filter(f => {
      const id = typeof f.category === 'object' ? f.category?.id : f.category
      return id == categoryId
    }).length
  }

  const filteredFaqs = computed(() => {
    let filtered = Array.isArray(faqs.value) ? faqs.value : []

    if (selectedCategory.value) {
      filtered = filtered.filter(f => {
        const categoryId = typeof f.category === 'object' ? f.category?.id : f.category
        return categoryId == selectedCategory.value
      })
    }

    const q = query.value.trim().toLowerCase()
    if (q) {
      filtered = filtered.filter(f =>
        String(f.question).toLowerCase().includes(q) ||
        String(f.answer).toLowerCase().includes(q)
      )
    }

    return filtered
  })

  const totalPages = computed(() => Math.max(1, Math.ceil(filteredFaqs.value.length / PAGE_SIZE)))

  const paginatedFaqs = computed(() => {
    const start = (currentPage.value - 1) * PAGE_SIZE
    return filteredFaqs.value.slice(start, start + PAGE_SIZE)
  })

  const resultsSummary = computed(() => {
    const total = filteredFaqs.value.length
    if (!total) return ''
    const start = (currentPage.value - 1) * PAGE_SIZE + 1
    const end = Math.min(currentPage.value * PAGE_SIZE, total)
    return `Showing ${start}–${end} of ${total} ${total === 1 ? 'question' : 'questions'}`
  })

  const pageNumbers = computed(() => {
    const total = totalPages.value
    if (total <= 5) return Array.from({ length: total }, (_, i) => i + 1)
    const p = currentPage.value
    if (p <= 3) return [1, 2, 3, 4, '...', total]
    if (p >= total - 2) return [1, '...', total - 3, total - 2, total - 1, total]
    return [1, '...', p - 1, p, p + 1, '...', total]
  })

  function toggleFaq(id) {
    openFaqId.value = openFaqId.value === id ? null : id
  }

  function selectCategory(id) {
    selectedCategory.value = id
    openFaqId.value = null
  }

  function clearFilters() {
    query.value = ''
    selectedCategory.value = ''
    currentPage.value = 1
    openFaqId.value = null
  }

  function goToPage(page) {
    if (page === '...' || page < 1 || page > totalPages.value) return
    currentPage.value = page
    openFaqId.value = null
    document.querySelector('.faq-toolbar')?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }

  function enter(el) {
    el.style.height = '0'
    el.style.overflow = 'hidden'
    requestAnimationFrame(() => {
      el.style.height = `${el.scrollHeight}px`
      el.style.transition = 'height 0.3s cubic-bezier(0.4, 0, 0.2, 1)'
    })
  }

  function leave(el) {
    el.style.height = `${el.scrollHeight}px`
    el.style.overflow = 'hidden'
    requestAnimationFrame(() => {
      el.style.height = '0'
      el.style.transition = 'height 0.25s cubic-bezier(0.4, 0, 0.2, 1)'
    })
  }
</script>

<style scoped>
.faq-layout {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.75rem;
  max-width: 72rem;
  margin-inline: auto;
}

@media (min-width: 1024px) {
  .faq-layout {
    grid-template-columns: 16.5rem minmax(0, 1fr);
    gap: 2.5rem;
    align-items: start;
  }
}

.support-card__glow {
  position: absolute;
  width: 10rem;
  height: 10rem;
  right: -3rem;
  top: -3rem;
  border-radius: 9999px;
  background: rgb(var(--color-primary) / 0.3);
  filter: blur(36px);
  pointer-events: none;
}

.cat-link {
  @apply w-full flex items-center justify-between gap-2 px-3 py-2.5 rounded-xl text-left text-sm font-semibold text-secondary/70 transition-all;
}

.cat-link:hover {
  @apply bg-neutral-offwhite text-secondary;
}

.cat-link--active {
  @apply bg-primary/10 text-primary font-bold;
}

.cat-count {
  @apply shrink-0 min-w-[1.5rem] text-center text-[10px] font-bold px-1.5 py-0.5 rounded-md bg-neutral-offwhite text-secondary/50;
}

.cat-link--active .cat-count {
  @apply bg-primary/15 text-primary;
}

.chip {
  @apply px-4 py-2 rounded-full text-[10px] font-bold uppercase tracking-wider whitespace-nowrap transition-all flex-shrink-0 border-2;
}

.chip-active {
  @apply bg-secondary border-secondary text-neutral-white;
}

.chip-idle {
  @apply bg-neutral-white border-transparent text-secondary/60;
}

/* Single bordered list — much denser than individual cards */
.faq-row__trigger {
  @apply w-full flex items-start justify-between gap-3 px-4 py-3.5 text-left focus:outline-none focus-visible:bg-primary/5 transition-colors;
}

.faq-row__question {
  @apply font-bold text-secondary text-sm leading-snug flex-1 min-w-0;
}

.faq-row--open .faq-row__question {
  @apply text-primary;
}

.faq-row__meta {
  @apply flex items-center gap-2 shrink-0 pt-0.5;
}

.faq-row__badge {
  @apply hidden sm:inline-block px-2 py-0.5 rounded text-[9px] uppercase font-bold tracking-wider bg-primary/10 text-primary;
}

.faq-row__chevron {
  @apply w-7 h-7 rounded-full bg-neutral-offwhite text-secondary flex items-center justify-center transition-transform duration-200;
}

.faq-row__chevron--open {
  @apply bg-primary text-neutral-white rotate-180;
}

.faq-row__answer {
  @apply px-4 pb-4 pt-0;
}

.faq-row__answer p {
  @apply text-sm text-secondary/75 font-semibold leading-relaxed border-t border-neutral-offwhite pt-3 whitespace-pre-line;
}

.page-nav {
  @apply w-10 h-10 rounded-xl flex items-center justify-center bg-neutral-white text-secondary border border-black/5 shadow-sm hover:text-primary transition-all disabled:opacity-40 disabled:pointer-events-none;
}

.page-btn {
  @apply min-w-[2.5rem] h-10 px-2 rounded-xl flex items-center justify-center text-sm font-bold transition-all;
}

.page-btn--active {
  @apply bg-primary text-neutral-white shadow-md;
}

.page-btn--idle {
  @apply bg-neutral-white text-secondary border border-black/5 hover:shadow-sm;
}

.help-banner__orb--a {
  position: absolute;
  width: 14rem;
  height: 14rem;
  right: -4rem;
  top: -6rem;
  border-radius: 9999px;
  background: rgb(var(--color-primary) / 0.35);
  filter: blur(48px);
  pointer-events: none;
}

.hide-scrollbar {
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.hide-scrollbar::-webkit-scrollbar {
  display: none;
}

.accordion-enter-active,
.accordion-leave-active {
  overflow: hidden;
}

@media (prefers-reduced-motion: reduce) {
  .faq-row__chevron,
  .cat-link,
  .chip {
    transition: none !important;
  }
}
</style>
