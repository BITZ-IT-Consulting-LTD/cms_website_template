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
      <h1 class="text-3xl md:text-4xl lg:text-5xl font-bold text-secondary mb-4 leading-tight">
        {{ post.title }}
      </h1>

      <!-- Meta Information -->
      <div class="flex flex-wrap items-center text-sm text-black/60 mb-6 space-x-4">
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
      <div v-if="post.excerpt" class="text-xl text-black/70 mb-6 italic border-l-4 border-primary pl-4">
        {{ post.excerpt }}
      </div>

      <!-- Content -->
      <div 
        class="prose prose-lg max-w-none"
        v-html="post.content"
      ></div>

      <!-- Tags -->
      <div v-if="post.tags && post.tags.length > 0" class="mt-8 pt-6 border-t border-primary/15">
        <h3 class="text-sm font-semibold text-black/70 mb-3">Tags:</h3>
        <div class="flex flex-wrap gap-2">
          <span
            v-for="tag in post.tags"
            :key="tag.slug"
            class="inline-block px-3 py-1 text-sm bg-primary/10 text-black/70 rounded-full hover:bg-secondary/10 transition-colors"
          >
            #{{ tag.name }}
          </span>
        </div>
      </div>

      <!-- Share Buttons -->
      <div class="mt-8 pt-6 border-t border-primary/15">
        <h3 class="text-sm font-semibold text-black/70 mb-3">Share this post:</h3>
        <div class="flex flex-wrap gap-3">
          <button
            v-for="social in socialShareButtons"
            :key="social.name"
            @click="social.action"
            class="flex items-center space-x-2 px-4 py-2 bg-white border border-black/10 text-secondary rounded-lg hover:border-primary hover:shadow-sm transition-colors"
            :aria-label="`Share on ${social.label}`"
          >
            <BrandIcon :name="social.name" class="w-5 h-5" />
            <span>{{ social.label }}</span>
          </button>

          <button
            @click="copyLink()"
            class="flex items-center space-x-2 px-4 py-2 bg-white border border-primary text-primary rounded-lg hover:bg-primary/5 transition-colors"
            aria-label="Copy link"
          >
            <svg v-if="!linkCopied" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 010 5.656l-3 3a4 4 0 01-5.656-5.656l1.5-1.5M10.172 13.828a4 4 0 010-5.656l3-3a4 4 0 015.656 5.656l-1.5 1.5" />
            </svg>
            <svg v-else class="w-5 h-5 text-secondary-light" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            <span>{{ linkCopied ? 'Copied!' : 'Copy link' }}</span>
          </button>
        </div>

        <p v-if="shareToast" role="status" class="mt-3 text-sm font-semibold text-secondary bg-secondary/10 rounded-lg py-2 px-3 inline-block">
          {{ shareToast }}
        </p>
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
import { ref, computed } from 'vue'
import BrandIcon from '@/components/common/BrandIcon.vue'

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

// Local inline SVG fallback (no third-party network request) shown when a post's
// featured image URL fails to load.
const PLACEHOLDER_FEATURED_IMAGE = 'data:image/svg+xml;charset=UTF-8,' + encodeURIComponent(
  '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="400" viewBox="0 0 800 400">' +
  '<rect width="800" height="400" fill="#E9F5FC"/>' +
  '<g transform="translate(360,160)" fill="none" stroke="#0087CF" stroke-width="4" stroke-opacity="0.5">' +
  '<rect x="0" y="0" width="80" height="60" rx="6"/>' +
  '<circle cx="20" cy="20" r="8"/>' +
  '<path d="M0 55 L25 30 L45 45 L60 25 L80 45" />' +
  '</g></svg>'
)

// Image error handling
const handleImageError = (event) => {
  // Guard against a repeated error loop: only swap to the local placeholder once.
  if (event.target.dataset.fallbackApplied) return
  event.target.dataset.fallbackApplied = 'true'
  event.target.src = PLACEHOLDER_FEATURED_IMAGE
}

// --- Share URL -------------------------------------------------------
// Built from the canonical public base URL (VITE_PUBLIC_BASE_URL) so a link
// shared from a dev host/IP still resolves to the real public site for the
// recipient. window.location is only a last-resort fallback (used when the
// env var isn't set, e.g. local development).
const shareUrl = computed(() => {
  const configuredBase = (import.meta.env.VITE_PUBLIC_BASE_URL || '').replace(/\/+$/, '')
  const base = configuredBase || (window.location.origin + (import.meta.env.BASE_URL || '/').replace(/\/+$/, ''))
  const slug = props.post?.slug
  return slug ? `${base}/blogs/${slug}` : `${base}${window.location.pathname}`
})

const linkCopied = ref(false)
const shareToast = ref('')

function flashToast(message) {
  shareToast.value = message
  setTimeout(() => { shareToast.value = '' }, 2500)
}

const shareOnFacebook = () => {
  window.open(
    `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(shareUrl.value)}`,
    '_blank',
    'width=600,height=400'
  )
}

const shareOnTwitter = () => {
  const text = props.post.title
  window.open(
    `https://twitter.com/intent/tweet?url=${encodeURIComponent(shareUrl.value)}&text=${encodeURIComponent(text)}`,
    '_blank',
    'width=600,height=400'
  )
}

const shareOnWhatsApp = () => {
  const text = `${props.post.title} - ${shareUrl.value}`
  window.open(
    `https://wa.me/?text=${encodeURIComponent(text)}`,
    '_blank'
  )
}

const shareOnLinkedIn = () => {
  window.open(
    `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(shareUrl.value)}`,
    '_blank',
    'width=600,height=500'
  )
}

const shareOnTelegram = () => {
  window.open(
    `https://t.me/share/url?url=${encodeURIComponent(shareUrl.value)}&text=${encodeURIComponent(props.post.title || '')}`,
    '_blank'
  )
}

const shareByEmail = () => {
  window.location.href = `mailto:?subject=${encodeURIComponent(props.post.title || 'Sauti 116')}&body=${encodeURIComponent(shareUrl.value)}`
}

// Instagram and TikTok have no web share-intent URL. Prefer the native share
// sheet (which surfaces the reader's installed apps, Instagram/TikTok
// included); fall back to copy-link with an explicit toast so the button
// never silently does nothing.
async function shareViaNativeOrCopy(platformLabel) {
  if (navigator.share) {
    try {
      await navigator.share({ title: props.post.title || 'Sauti 116', url: shareUrl.value })
      return
    } catch (err) {
      if (err?.name === 'AbortError') return
    }
  }
  await copyLink(`Link copied — paste it in ${platformLabel}`)
}

const shareOnInstagram = () => shareViaNativeOrCopy('Instagram')
const shareOnTikTok = () => shareViaNativeOrCopy('TikTok')

async function copyLink(message = 'Link copied') {
  const text = shareUrl.value
  try {
    if (navigator.clipboard?.writeText) {
      await navigator.clipboard.writeText(text)
    } else {
      window.prompt('Copy this link:', text)
    }
  } catch (err) {
    window.prompt('Copy this link:', text)
  }
  linkCopied.value = true
  flashToast(message)
  setTimeout(() => { linkCopied.value = false }, 2500)
}

const socialShareButtons = [
  { name: 'facebook', label: 'Facebook', action: shareOnFacebook },
  { name: 'x', label: 'X', action: shareOnTwitter },
  { name: 'whatsapp', label: 'WhatsApp', action: shareOnWhatsApp },
  { name: 'linkedin', label: 'LinkedIn', action: shareOnLinkedIn },
  { name: 'telegram', label: 'Telegram', action: shareOnTelegram },
  { name: 'instagram', label: 'Instagram', action: shareOnInstagram },
  { name: 'tiktok', label: 'TikTok', action: shareOnTikTok },
  { name: 'email', label: 'Email', action: shareByEmail },
]
</script>

<style scoped>
/* Prose styles for blog content */
:deep(.prose) {
  @apply text-black/70;
}

:deep(.prose h2) {
  @apply text-2xl font-bold text-secondary mt-8 mb-4;
}

:deep(.prose h3) {
  @apply text-xl font-bold text-secondary mt-6 mb-3;
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
  @apply border-l-4 border-primary pl-4 italic my-4 text-black/60;
}

:deep(.prose img) {
  @apply rounded-lg my-6 shadow-md;
}

:deep(.prose strong) {
  @apply font-bold text-secondary;
}

:deep(.prose em) {
  @apply italic;
}
</style>
