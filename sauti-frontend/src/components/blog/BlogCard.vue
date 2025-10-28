<template>
  <article class="group">
    <router-link :to="`/blog/${post.slug}`" class="block">
      <!-- Featured Image (YouTube-style) -->
      <div class="relative bg-gray-200 rounded-xl overflow-hidden aspect-video cursor-pointer">
        <img
          v-if="post.featured_image"
          :src="post.featured_image"
          :alt="post.title"
          class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
          loading="lazy"
          @error="setPlaceholder"
          data-ph="https://images.unsplash.com/photo-1578662996442-48f60103fc96?q=80&w=1200&auto=format&fit=crop"
        />
        <div v-else class="w-full h-full flex items-center justify-center bg-gradient-to-br from-primary-400 to-primary-600">
          <svg class="w-16 h-16 text-white opacity-50" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z" clip-rule="evenodd"/>
          </svg>
        </div>
        
        <!-- Hover overlay -->
        <div class="absolute inset-0 bg-black/0 group-hover:bg-black/10 transition-colors duration-300"></div>
        
        <!-- Category Badge -->
        <div v-if="post.category" class="absolute top-2 left-2">
          <span class="text-xs font-bold bg-black/80 text-white px-2 py-0.5 rounded">
            {{ post.category.name }}
          </span>
        </div>
        
        <!-- Featured Badge -->
        <div v-if="post.is_featured" class="absolute top-2 right-2">
          <span class="bg-secondary-500 text-white px-2 py-0.5 rounded text-xs font-semibold">
            Featured
          </span>
        </div>
      </div>

      <!-- Content (YouTube-style) -->
      <div class="mt-3 flex gap-3">
        <!-- Author Avatar -->
        <div class="h-9 w-9 rounded-full bg-[#8B4000] flex items-center justify-center text-white font-bold text-sm flex-shrink-0">
          {{ getAuthorInitial() }}
        </div>
        
        <!-- Post Info -->
        <div class="min-w-0">
          <!-- Title -->
          <h3 class="text-sm font-semibold text-gray-900 leading-5 line-clamp-2 group-hover:text-[#8B4000] transition-colors">
            {{ post.title }}
          </h3>
          
          <!-- Author Name -->
          <p class="text-xs text-gray-600 mt-1">
            {{ post.author?.username || post.author_name || 'Sauti Uganda' }}
          </p>
          
          <!-- Views & Date -->
          <p class="text-xs text-gray-500">
            {{ formatViews(post.views_count) }} • {{ formatTimeAgo(post.published_at) }}
          </p>
        </div>
      </div>
    </router-link>
  </article>
</template>

<script setup>
import { defineProps } from 'vue'

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
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
  
  if (diffDays === 1) return '1 day ago'
  if (diffDays < 7) return `${diffDays} days ago`
  if (diffDays < 30) return `${Math.ceil(diffDays / 7)} weeks ago`
  if (diffDays < 365) return `${Math.ceil(diffDays / 30)} months ago`
  return `${Math.ceil(diffDays / 365)} years ago`
}

function setPlaceholder(event) {
  const img = event.target
  const ph = img.getAttribute('data-ph') || 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?q=80&w=1200&auto=format&fit=crop'
  if (img.src !== ph) {
    img.src = ph
  }
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.aspect-video {
  position: relative;
  width: 100%;
  padding-bottom: 56.25%; /* 16:9 */
}

.aspect-video > img,
.aspect-video > div {
  position: absolute;
  inset: 0;
}
</style>
