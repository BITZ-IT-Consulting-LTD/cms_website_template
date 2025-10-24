<template>
  <article class="group">
    <router-link :to="`/blog/${post.slug}`">
      <!-- Featured Image -->
      <div class="relative h-52 bg-gray-200 overflow-hidden rounded-2xl">
        <img
          v-if="post.featured_image"
          :src="post.featured_image"
          :alt="post.title"
          class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform"
          loading="lazy"
          @error="setPlaceholder"
          data-ph="https://picsum.photos/800/480?blur=2"
        />
        <div v-else class="w-full h-full flex items-center justify-center bg-gradient-to-br from-primary-400 to-primary-600">
          <svg class="w-16 h-16 text-white opacity-50" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z" clip-rule="evenodd"/>
          </svg>
        </div>
        
        <!-- Category Badge -->
        <div v-if="post.category" class="absolute top-3 left-3">
          <span class="badge-blue">
            {{ post.category.name }}
          </span>
        </div>
        
        <!-- Featured Badge -->
        <div v-if="post.is_featured" class="absolute top-3 right-3">
          <span class="bg-secondary-500 text-white px-2 py-1 rounded text-xs font-semibold">
            Featured
          </span>
        </div>
      </div>

      <!-- Content -->
      <div class="pt-4">
        <!-- Meta Info -->
        <div class="flex items-center text-xs text-gray-500 mb-2 flex-wrap gap-2">
          <time :datetime="post.published_at">
            {{ formatDate(post.published_at) }}
          </time>
          <span>·</span>
          <span v-if="post.author">Article</span>
          <span v-if="post.views_count" class="flex items-center">
            <svg class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
              <path d="M10 12a2 2 0 100-4 2 2 0 000 4z"/>
              <path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"/>
            </svg>
            {{ post.views_count }}
          </span>
        </div>

        <!-- Title -->
        <h3 class="text-lg font-bold text-gray-900 mb-2 line-clamp-2 group-hover:text-primary-600 transition-colors">
          {{ post.title }}
        </h3>

        <!-- Excerpt -->
        <p v-if="post.excerpt" class="text-gray-600 line-clamp-3">
          {{ post.excerpt }}
        </p>

        <div class="h-6"></div>
      </div>
    </router-link>
  </article>
</template>

<script setup>
import { defineProps } from 'vue'

defineProps({
  post: {
    type: Object,
    required: true,
  },
})

function formatDate(dateString) {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
}

function setPlaceholder(event) {
  const img = event.target
  const ph = img.getAttribute('data-ph') || 'https://picsum.photos/800/480'
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

.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
