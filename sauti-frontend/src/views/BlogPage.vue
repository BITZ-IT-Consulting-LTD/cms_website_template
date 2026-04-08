<template>
  <PostListPage
    post-type="BLOG"
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
  name: 'BlogPage'
})

const settingsStore = useSettingsStore()
const siteContent = useSiteContent('blog')

onMounted(async () => {
  await siteContent.fetchContent()
  await settingsStore.fetchGlobalSettings()
})

// Content from CMS with sensible defaults
const titlePrefix = computed(() =>
  siteContent.getContent('blog_page_title', 'Latest')
)

const titleHighlight = computed(() =>
  siteContent.getContent('blog_page_title_highlight', 'Blog Posts')
)

const subtitle = computed(() =>
  siteContent.getContent('blog_page_subtitle', 'Stay informed with the latest stories, news, and insights from the Sauti 116 Helpline.')
)

const searchPlaceholder = computed(() =>
  settingsStore.settings.blog_search_placeholder || 'Search articles...'
)

const loadingMessage = computed(() =>
  settingsStore.settings.blog_loading || 'Loading stories...'
)

const emptyTitle = computed(() =>
  settingsStore.settings.blog_no_results || 'No stories found'
)

const emptySubtitle = computed(() =>
  settingsStore.settings.blog_no_results_subtitle || 'Try adjusting your filters or check back later for new content.'
)

const searchButtonText = computed(() =>
  siteContent.getContent('blog_search_button', 'Search')
)

const allFilterText = computed(() =>
  siteContent.getContent('blog_all_filter', 'ALL')
)

const allCategoriesText = computed(() =>
  siteContent.getContent('blog_all_categories', 'All Categories')
)

const clearFiltersText = computed(() =>
  siteContent.getContent('blog_clear_filters', 'Clear all filters')
)
</script>
