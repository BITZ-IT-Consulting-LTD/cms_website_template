<template>
  <article class="post-card group">
    <router-link :to="`/blogs/${post.slug}`" class="block h-full"
      @mouseenter="prefetchArticle" @focus="prefetchArticle">
      <!-- Featured Image -->
      <div class="relative bg-neutral-offwhite rounded-xl lg:rounded-2xl overflow-hidden aspect-[16/9] mb-3 shadow-sm ring-1 ring-black/[0.04]">
        <img
          :src="post.featured_image_thumbnail || post.featured_image || helplineAction"
          :alt="post.title"
          width="480"
          height="300"
          class="w-full h-full object-cover transition-all duration-500 group-hover:scale-105"
          loading="lazy"
          decoding="async"
          @error="setPlaceholder"
        />

        <div class="absolute inset-0 bg-gradient-to-t from-black/45 via-black/5 to-transparent opacity-80 group-hover:opacity-100 transition-opacity"></div>

        <div v-if="post.is_featured" class="absolute top-3 left-3 sm:top-4 sm:left-4">
          <span class="bg-primary text-neutral-white px-3 py-1.5 rounded-full text-[10px] font-bold uppercase tracking-wider shadow-lg">
            Featured
          </span>
        </div>

        <div
          v-if="categoryLabel"
          class="absolute bottom-3 left-3 sm:bottom-4 sm:left-4"
        >
          <span class="bg-neutral-white/95 text-secondary px-2.5 py-1 rounded-lg text-[10px] font-bold uppercase tracking-wider backdrop-blur-sm">
            {{ categoryLabel }}
          </span>
        </div>
      </div>

      <!-- Content -->
      <div class="px-0.5 sm:px-1 space-y-2">
        <h3 class="text-base sm:text-lg font-bold text-secondary leading-snug line-clamp-2 group-hover:text-primary transition-colors">
          {{ post.title }}
        </h3>

        <p v-if="excerpt" class="text-sm text-black/50 font-semibold leading-relaxed line-clamp-2 hidden sm:block">
          {{ excerpt }}
        </p>

        <p class="text-xs text-secondary/45 font-semibold pt-0.5">
          {{ formatPostTime(post) }}
        </p>
      </div>
    </router-link>
  </article>
</template>

<script setup>
  import { computed } from 'vue'
  import helplineAction from '@/assets/helpline-action.png'
  import { useBlogStore } from '@/store/blog'

  const props = defineProps({
    post: {
      type: Object,
      required: true,
    },
  })

  const blogStore = useBlogStore()

  // Hover/focus intent prefetch: by the time a reader actually clicks, the
  // article's data and its full-size lead image are already warm, so the
  // detail page renders instantly instead of showing its own loading state.
  // Only fires once per card (prefetchPost/preloadedImage below both guard
  // against repeat calls), so rapid mouse movement across many cards doesn't
  // fire a burst of redundant requests.
  let imagePreloaded = false

  function prefetchArticle() {
    if (!props.post?.slug) return
    blogStore.prefetchPost(props.post.slug)

    if (imagePreloaded) return
    const src = props.post.featured_image_medium || props.post.featured_image
    if (!src) return
    imagePreloaded = true
    const img = new Image()
    img.src = src
  }

  const categoryLabel = computed(() => {
    const cat = props.post.category
    if (!cat) return ''
    if (typeof cat === 'string') return cat
    return cat.name || cat.title || ''
  })

  const excerpt = computed(() => {
    const raw = props.post.excerpt || props.post.summary || props.post.description || ''
    return String(raw).replace(/<[^>]+>/g, '').trim()
  })

  function formatDate(dateString) {
    if (!dateString) return ''
    return new Date(dateString).toLocaleString('en-GB', {
      year: 'numeric', month: 'short', day: 'numeric',
      hour: '2-digit', minute: '2-digit'
    })
  }

  function formatPostTime(post) {
    const publishedAt = post?.published_at
    const createdAt = post?.created_at
    const updatedAt = post?.updated_at

    const base = publishedAt || createdAt
    if (!base) return 'Recently'

    if (updatedAt && publishedAt && updatedAt !== publishedAt) {
      return `${formatDate(base)} · Updated ${formatDate(updatedAt)}`
    }

    return formatDate(base)
  }

  function setPlaceholder(event) {
    const img = event.target
    const ph = helplineAction
    if (img.src !== ph) {
      img.src = ph
    }
  }
</script>

<style scoped>
  .post-card {
    transition: transform 0.3s ease;
  }

  .post-card:hover {
    transform: translateY(-6px);
  }

  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  @media (max-width: 640px) {
    .post-card:hover {
      transform: translateY(-3px);
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .post-card,
    .post-card img {
      transition: none !important;
    }

    .post-card:hover {
      transform: none;
    }
  }
</style>
