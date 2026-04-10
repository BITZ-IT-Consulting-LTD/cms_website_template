<template>
  <PostListPage
    post-type="NEWS"
    :title-prefix="titlePrefix"
    :title-highlight="titleHighlight"
    :subtitle="subtitle"
    :search-placeholder="searchPlaceholder"
    :show-filters="true"
    :loading-message="loadingMessage"
    :empty-title="emptyTitle"
    :empty-subtitle="emptySubtitle"
    :search-button-text="searchButtonText"
    :all-filter-text="allFilterText"
    :all-categories-text="allCategoriesText"
    :clear-filters-text="clearFiltersText"
  />
</template>

<script setup>
import { computed, onMounted } from 'vue'
import PostListPage from '@/components/posts/PostListPage.vue'
import { useSettingsStore } from '@/store/settings'
import { useSiteContent } from '@/composables/useSiteContent'

defineOptions({
  name: 'NewsPage'
})

const settingsStore = useSettingsStore()
const siteContent = useSiteContent('news')

onMounted(async () => {
  await siteContent.fetchContent()
  await settingsStore.fetchGlobalSettings()
})

// Content from CMS with sensible defaults
const titlePrefix = computed(() =>
  siteContent.getContent('news_page_title', 'Sauti')
)

const titleHighlight = computed(() =>
  siteContent.getContent('news_page_title_highlight', 'News & Updates')
)

const subtitle = computed(() =>
  siteContent.getContent('news_page_subtitle', 'Latest official updates, press releases and announcements from the Sauti 116 Helpline.')
)

const searchPlaceholder = computed(() =>
  settingsStore.settings.news_search_placeholder || 'Search news...'
)

const loadingMessage = computed(() =>
  settingsStore.settings.news_loading || 'Locating official updates...'
)

const emptyTitle = computed(() =>
  settingsStore.settings.news_no_results || 'No archives found'
)

const emptySubtitle = computed(() =>
  settingsStore.settings.news_no_results_subtitle || 'Adjust your filters or search keywords to find specific official news items.'
)

const searchButtonText = computed(() =>
  siteContent.getContent('news_search_button', 'Search')
)

const allFilterText = computed(() =>
  siteContent.getContent('news_all_filter', 'ALL')
)

const allCategoriesText = computed(() =>
  siteContent.getContent('news_all_categories', 'All Categories')
)

const clearFiltersText = computed(() =>
  siteContent.getContent('news_clear_filters', 'Clear all filters')
)
</script>
