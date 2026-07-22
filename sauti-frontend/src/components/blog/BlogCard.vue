<template>
  <article class="group cursor-pointer">
    <router-link :to="`/blogs/${post.slug}`" class="block">
      <!-- Featured Image -->
      <div class="relative bg-neutral-offwhite rounded-xl overflow-hidden aspect-video mb-3 shadow-md">
        <img :src="post.featured_image || helplineAction" :alt="post.title"
          class="w-full h-full object-cover transition-all duration-300 group-hover:scale-105 group-hover:brightness-110" loading="lazy"
          @error="setPlaceholder" />

        <!-- Gradient Overlay -->
        <div class="absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent"></div>

        <!-- Featured Badge -->
        <div v-if="post.is_featured" class="absolute top-3 left-3">
          <span class="bg-primary text-white px-3 py-1.5 rounded-lg text-[10px] font-bold uppercase tracking-wider shadow-lg">
            Featured
          </span>
        </div>
      </div>

      <!-- Content -->
      <div class="px-1">
        <!-- Title -->
        <h3 class="text-sm font-bold text-secondary leading-tight mb-2 line-clamp-2 group-hover:text-primary transition-colors">
          {{ post.title }}
        </h3>

        <!-- Meta -->
        <p class="text-xs text-gray-600 font-medium">
          {{ formatPostTime(post) }}
        </p>
      </div>
    </router-link>
  </article>
</template>

<script setup>
  import { defineProps } from 'vue'
  import helplineAction from '@/assets/helpline-action.png'

  const props = defineProps({
    post: {
      type: Object,
      required: true,
    },
  })

  function getAuthorInitial() {
    const author = props.post.author?.username || props.post.author_name || 'Sauti'
    return author.charAt(0).toUpperCase()
  }

  function formatViews(views) {
    if (!views) return '0 views'
    if (views >= 1000000) {
      return `${(views / 1000000).toFixed(1)}M views`
    } else if (views >= 1000) {
      return `${(views / 1000).toFixed(1)}K views`
    }
    return `${views} views`
  }

  function formatTimeAgo(dateString) {
    if (!dateString) return 'Recently'
    const date = new Date(dateString)
    const now = new Date()
    const diffTime = Math.abs(now - date)

    const diffMinutes = Math.floor(diffTime / (1000 * 60))
    const diffHours = Math.floor(diffTime / (1000 * 60 * 60))
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24))

    if (diffMinutes < 1) return 'Just now'
    if (diffMinutes < 60) return `${diffMinutes} minute${diffMinutes !== 1 ? 's' : ''} ago`
    if (diffHours < 24) return `${diffHours} hour${diffHours !== 1 ? 's' : ''} ago`
    if (diffDays === 1) return '1 day ago'
    if (diffDays < 7) return `${diffDays} days ago`
    if (diffDays < 30) return `${Math.floor(diffDays / 7)} week${Math.floor(diffDays / 7) !== 1 ? 's' : ''} ago`
    if (diffDays < 365) return `${Math.floor(diffDays / 30)} month${Math.floor(diffDays / 30) !== 1 ? 's' : ''} ago`
    return `${Math.floor(diffDays / 365)} year${Math.floor(diffDays / 365) !== 1 ? 's' : ''} ago`
  }

  function formatDate(dateString) {
    if (!dateString) return ''
    return new Date(dateString).toLocaleDateString('en-GB', {
      year: 'numeric', month: 'short', day: 'numeric'
    })
  }

  function formatPostTime(post) {
    // Show the specific posting date (not a relative "X months ago"), which
    // reporters asked for. Prefer published_at, falling back to created_at.
    const publishedAt = post?.published_at
    const createdAt = post?.created_at
    const updatedAt = post?.updated_at

    const base = publishedAt || createdAt
    if (!base) return 'Recently'

    // If the post was meaningfully edited after publishing, note the edit date.
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
  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  article {
    transition: transform 0.2s ease;
  }

  article:hover {
    transform: translateY(-4px);
  }

  @media (max-width: 640px) {
    h3 {
      font-size: 0.8125rem;
      -webkit-line-clamp: 1;
    }

    article:hover {
      transform: translateY(-2px);
    }
  }
</style>
