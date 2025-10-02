<template>
  <article class="bg-white rounded-lg shadow-lg overflow-hidden">
    <!-- Featured Image -->
    <div v-if="post.featured_image" class="relative h-64 md:h-96 w-full overflow-hidden">
      <img
        :src="post.featured_image"
        :alt="post.title"
        class="w-full h-full object-cover"
        @error="handleImageError"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent"></div>
    </div>

    <!-- Content -->
    <div class="p-6 md:p-8 lg:p-12">
      <!-- Category Badge -->
      <div v-if="post.category" class="mb-4">
        <span class="inline-block px-3 py-1 text-sm font-semibold rounded-full bg-primary/10 text-primary">
          {{ post.category.name }}
        </span>
      </div>

      <!-- Title -->
      <h1 class="text-3xl md:text-4xl lg:text-5xl font-bold text-gray-900 mb-4 leading-tight">
        {{ post.title }}
      </h1>

      <!-- Meta Information -->
      <div class="flex flex-wrap items-center text-sm text-gray-600 mb-6 space-x-4">
        <!-- Author -->
        <div v-if="post.author" class="flex items-center space-x-2">
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
          </svg>
          <span>{{ post.author.username }}</span>
        </div>

        <!-- Date -->
        <div v-if="post.published_at" class="flex items-center space-x-2">
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd" />
          </svg>
          <span>{{ formatDate(post.published_at) }}</span>
        </div>

        <!-- Views -->
        <div v-if="post.views_count" class="flex items-center space-x-2">
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path d="M10 12a2 2 0 100-4 2 2 0 000 4z" />
            <path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd" />
          </svg>
          <span>{{ post.views_count }} views</span>
        </div>

        <!-- Language -->
        <div v-if="post.language" class="flex items-center space-x-2">
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M7 2a1 1 0 011 1v1h3a1 1 0 110 2H9.578a18.87 18.87 0 01-1.724 4.78c.29.354.596.696.914 1.026a1 1 0 11-1.44 1.389c-.188-.196-.373-.396-.554-.6a19.098 19.098 0 01-3.107 3.567 1 1 0 01-1.334-1.49 17.087 17.087 0 003.13-3.733 18.992 18.992 0 01-1.487-2.494 1 1 0 111.79-.89c.234.47.489.928.764 1.372.417-.934.752-1.913.997-2.927H3a1 1 0 110-2h3V3a1 1 0 011-1zm6 6a1 1 0 01.894.553l2.991 5.982a.869.869 0 01.02.037l.99 1.98a1 1 0 11-1.79.895L15.383 16h-4.764l-.724 1.447a1 1 0 11-1.788-.894l.99-1.98.019-.038 2.99-5.982A1 1 0 0113 8zm-1.382 6h2.764L13 11.236 11.618 14z" clip-rule="evenodd" />
          </svg>
          <span>{{ getLanguageName(post.language) }}</span>
        </div>
      </div>

      <!-- Excerpt -->
      <div v-if="post.excerpt" class="text-xl text-gray-700 mb-6 italic border-l-4 border-primary pl-4">
        {{ post.excerpt }}
      </div>

      <!-- Content -->
      <div 
        class="prose prose-lg max-w-none"
        v-html="post.content"
      ></div>

      <!-- Tags -->
      <div v-if="post.tags && post.tags.length > 0" class="mt-8 pt-6 border-t border-gray-200">
        <h3 class="text-sm font-semibold text-gray-700 mb-3">Tags:</h3>
        <div class="flex flex-wrap gap-2">
          <span
            v-for="tag in post.tags"
            :key="tag.slug"
            class="inline-block px-3 py-1 text-sm bg-gray-100 text-gray-700 rounded-full hover:bg-gray-200 transition-colors"
          >
            #{{ tag.name }}
          </span>
        </div>
      </div>

      <!-- Share Buttons -->
      <div class="mt-8 pt-6 border-t border-gray-200">
        <h3 class="text-sm font-semibold text-gray-700 mb-3">Share this post:</h3>
        <div class="flex space-x-3">
          <button
            @click="shareOnFacebook"
            class="flex items-center space-x-2 px-4 py-2 bg-[#1877F2] text-white rounded-lg hover:bg-[#1664D9] transition-colors"
            aria-label="Share on Facebook"
          >
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
            </svg>
            <span>Facebook</span>
          </button>

          <button
            @click="shareOnTwitter"
            class="flex items-center space-x-2 px-4 py-2 bg-[#1DA1F2] text-white rounded-lg hover:bg-[#1A8CD8] transition-colors"
            aria-label="Share on Twitter"
          >
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/>
            </svg>
            <span>Twitter</span>
          </button>

          <button
            @click="shareOnWhatsApp"
            class="flex items-center space-x-2 px-4 py-2 bg-[#25D366] text-white rounded-lg hover:bg-[#20BA5A] transition-colors"
            aria-label="Share on WhatsApp"
          >
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>
            </svg>
            <span>WhatsApp</span>
          </button>
        </div>
      </div>

      <!-- Back Button -->
      <div class="mt-8">
        <router-link
          to="/blog"
          class="inline-flex items-center space-x-2 text-primary hover:text-blue-600 transition-colors"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
          </svg>
          <span>Back to all posts</span>
        </router-link>
      </div>
    </div>
  </article>
</template>

<script setup>
const props = defineProps({
  post: {
    type: Object,
    required: true
  }
})

// Date formatting
const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric' }
  return new Date(dateString).toLocaleDateString('en-US', options)
}

// Language name mapping
const getLanguageName = (code) => {
  const languages = {
    en: 'English',
    lg: 'Luganda',
    sw: 'Swahili'
  }
  return languages[code] || code
}

// Image error handling
const handleImageError = (event) => {
  event.target.src = 'https://via.placeholder.com/800x400?text=Sauti+Child+Helpline'
}

// Share functions
const shareOnFacebook = () => {
  const url = window.location.href
  window.open(
    `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`,
    '_blank',
    'width=600,height=400'
  )
}

const shareOnTwitter = () => {
  const url = window.location.href
  const text = props.post.title
  window.open(
    `https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}&text=${encodeURIComponent(text)}`,
    '_blank',
    'width=600,height=400'
  )
}

const shareOnWhatsApp = () => {
  const url = window.location.href
  const text = `${props.post.title} - ${url}`
  window.open(
    `https://wa.me/?text=${encodeURIComponent(text)}`,
    '_blank'
  )
}
</script>

<style scoped>
/* Prose styles for blog content */
:deep(.prose) {
  @apply text-gray-700;
}

:deep(.prose h2) {
  @apply text-2xl font-bold text-gray-900 mt-8 mb-4;
}

:deep(.prose h3) {
  @apply text-xl font-bold text-gray-900 mt-6 mb-3;
}

:deep(.prose p) {
  @apply mb-4 leading-relaxed;
}

:deep(.prose ul),
:deep(.prose ol) {
  @apply my-4 ml-6;
}

:deep(.prose li) {
  @apply mb-2;
}

:deep(.prose a) {
  @apply text-primary hover:text-blue-600 underline;
}

:deep(.prose blockquote) {
  @apply border-l-4 border-primary pl-4 italic my-4 text-gray-600;
}

:deep(.prose img) {
  @apply rounded-lg my-6 shadow-md;
}

:deep(.prose strong) {
  @apply font-bold text-gray-900;
}

:deep(.prose em) {
  @apply italic;
}
</style>
