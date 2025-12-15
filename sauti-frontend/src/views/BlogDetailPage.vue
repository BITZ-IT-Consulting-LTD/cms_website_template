<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Loading State -->
    <AppLoader v-if="loading" :fullScreen="true" message="Loading article..." />

    <!-- Article Content -->
    <article v-else-if="post" class="bg-white">
      <!-- Hero Section -->
      <div class="relative h-[60vh] min-h-[400px] max-h-[600px] overflow-hidden bg-gradient-to-br from-gray-900 to-gray-800">
        <img
          v-if="post.featured_image"
          :src="post.featured_image"
          :alt="post.title"
          class="absolute inset-0 w-full h-full object-cover opacity-40"
          @error="setPlaceholder"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent"></div>

        <!-- Hero Content -->
        <div class="relative h-full container-custom flex flex-col justify-end pb-16">
          <!-- Category Badge -->
          <div v-if="post.category" class="mb-4">
            <span class="inline-block px-4 py-1.5 bg-[#8B4000] text-white text-sm font-bold rounded-full">
              {{ post.category.name }}
            </span>
          </div>

          <!-- Title -->
          <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-white leading-tight mb-6 max-w-4xl">
            {{ post.title }}
          </h1>

          <!-- Meta Info -->
          <div class="flex flex-wrap items-center gap-4 text-gray-200">
            <!-- Author -->
            <div class="flex items-center gap-3">
              <div class="w-12 h-12 rounded-full bg-[#8B4000] flex items-center justify-center text-white font-bold text-lg">
                {{ getAuthorInitial() }}
              </div>
              <div>
                <p class="font-semibold text-white">
                  {{ post.author?.username || post.author_name || 'Sauti Uganda' }}
                </p>
                <p class="text-sm text-gray-300">
                  {{ formatDate(post.published_at) }}
                </p>
              </div>
            </div>

            <!-- Separator -->
            <span class="text-gray-400">•</span>

            <!-- Reading Time -->
            <div class="flex items-center gap-2">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <span class="text-sm">{{ readingTime }} min read</span>
            </div>

            <!-- Views -->
            <span class="text-gray-400">•</span>
            <div class="flex items-center gap-2">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
              </svg>
              <span class="text-sm">{{ formatViews(post.views_count) }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Article Body -->
      <div class="section-padding">
        <div class="container-custom max-w-4xl">
          <!-- Excerpt -->
          <div v-if="post.excerpt" class="mb-12">
            <p class="text-xl md:text-2xl text-gray-700 leading-relaxed font-medium border-l-4 border-[#8B4000] pl-6 py-2">
              {{ post.excerpt }}
            </p>
          </div>

          <!-- Tags -->
          <div v-if="post.tags && post.tags.length > 0" class="flex flex-wrap gap-2 mb-8">
            <span
              v-for="tag in post.tags"
              :key="tag.id"
              class="px-3 py-1 bg-gray-100 text-gray-700 text-sm rounded-full hover:bg-gray-200 transition-colors"
            >
              #{{ tag.name }}
            </span>
          </div>

          <!-- Main Content -->
          <div class="prose prose-lg prose-headings:font-bold prose-headings:text-gray-900 prose-p:text-gray-700 prose-p:leading-relaxed prose-a:text-[#8B4000] prose-a:no-underline hover:prose-a:underline prose-strong:text-gray-900 prose-img:rounded-xl prose-img:shadow-lg max-w-none mb-12" v-html="formattedContent"></div>

          <!-- Share Section -->
          <div class="border-t border-b border-gray-200 py-8 my-12">
            <div class="flex flex-col md:flex-row items-center justify-between gap-6">
              <div class="text-center md:text-left">
                <h3 class="text-lg font-bold text-gray-900 mb-2">Share this article</h3>
                <p class="text-sm text-gray-600">Help spread awareness about child protection</p>
              </div>

              <div class="flex items-center gap-3">
                <!-- Facebook -->
                <button
                  @click="shareOnFacebook"
                  class="w-12 h-12 rounded-full bg-blue-600 text-white flex items-center justify-center hover:bg-blue-700 transition-colors shadow-lg hover:shadow-xl"
                  aria-label="Share on Facebook"
                >
                  <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M22.675 0H1.325C.593 0 0 .593 0 1.325v21.351C0 23.407.593 24 1.325 24H12.82v-9.294H9.692V11.09h3.129V8.413c0-3.1 1.893-4.788 4.659-4.788 1.325 0 2.463.099 2.795.143v3.24l-1.918.001c-1.503 0-1.794.715-1.794 1.763v2.316h3.587l-.467 3.616h-3.12V24h6.116C23.407 24 24 23.407 24 22.676V1.325C24 .593 23.407 0 22.675 0z"/></svg>
                </button>

                <!-- Twitter/X -->
                <button
                  @click="shareOnTwitter"
                  class="w-12 h-12 rounded-full bg-black text-white flex items-center justify-center hover:bg-gray-800 transition-colors shadow-lg hover:shadow-xl"
                  aria-label="Share on Twitter"
                >
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M18.244 2H21l-6.52 7.455L22.5 22h-6.9l-4.5-6.22L5.7 22H3l7.03-8.036L1.5 2h7.02l4.08 5.64L18.244 2zm-2.41 18h1.6L8.28 4h-1.6l9.155 16z"/></svg>
                </button>

                <!-- WhatsApp -->
                <button
                  @click="shareOnWhatsApp"
                  class="w-12 h-12 rounded-full bg-green-600 text-white flex items-center justify-center hover:bg-green-700 transition-colors shadow-lg hover:shadow-xl"
                  aria-label="Share on WhatsApp"
                >
                  <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.525 3.488"/></svg>
                </button>

                <!-- Copy Link -->
                <button
                  @click="copyLink"
                  class="w-12 h-12 rounded-full bg-gray-200 text-gray-700 flex items-center justify-center hover:bg-gray-300 transition-colors shadow-lg hover:shadow-xl"
                  aria-label="Copy link"
                  :title="linkCopied ? 'Copied!' : 'Copy link'"
                >
                  <svg v-if="!linkCopied" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"/></svg>
                  <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                </button>
              </div>
            </div>
          </div>

          <!-- Author Bio -->
          <div class="bg-gradient-to-br from-[#FFF8DC] to-white rounded-2xl p-8 mb-12 border border-[#8B4000]/10">
            <div class="flex items-start gap-6">
              <div class="w-20 h-20 rounded-full bg-[#8B4000] flex items-center justify-center text-white font-bold text-3xl flex-shrink-0">
                {{ getAuthorInitial() }}
              </div>
              <div class="flex-1">
                <h3 class="text-xl font-bold text-gray-900 mb-2">
                  {{ post.author?.username || post.author_name || 'Sauti Uganda' }}
                </h3>
                <p class="text-gray-600 leading-relaxed">
                  Contributing writer at Sauti 116 Helpline, dedicated to raising awareness about child protection and safety across Uganda.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Related Posts Section -->
      <div class="bg-gray-50 section-padding">
        <div class="container-custom max-w-6xl">
          <h2 class="text-3xl font-bold text-gray-900 mb-8 text-center">Related Articles</h2>

          <!-- Loading Related -->
          <div v-if="loadingRelated" class="flex justify-center py-12">
            <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-[#8B4000]"></div>
          </div>

          <!-- Related Posts Grid -->
          <div v-else-if="relatedPosts.length > 0" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <router-link
              v-for="related in relatedPosts"
              :key="related.id"
              :to="`/blog/${related.slug}`"
              class="group bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1"
            >
              <!-- Image -->
              <div class="relative h-48 bg-gray-200 overflow-hidden">
                <img
                  :src="related.featured_image"
                  :alt="related.title"
                  class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300"
                  @error="setPlaceholder"
                />
                <div class="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent"></div>

                <!-- Category Badge -->
                <span v-if="related.category" class="absolute top-3 left-3 px-3 py-1 bg-[#8B4000] text-white text-xs font-bold rounded-full">
                  {{ related.category.name }}
                </span>
              </div>

              <!-- Content -->
              <div class="p-5">
                <h3 class="font-bold text-lg text-gray-900 mb-2 line-clamp-2 group-hover:text-[#8B4000] transition-colors">
                  {{ related.title }}
                </h3>
                <p class="text-sm text-gray-600 line-clamp-2 mb-3">
                  {{ related.excerpt }}
                </p>
                <div class="flex items-center justify-between text-xs text-gray-500">
                  <span>{{ formatTimeAgo(related.published_at) }}</span>
                  <span class="flex items-center gap-1">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                    {{ formatViews(related.views_count) }}
                  </span>
                </div>
              </div>
            </router-link>
          </div>

          <!-- Empty Related -->
          <div v-else class="text-center py-12 text-gray-500">
            <p>No related articles found</p>
          </div>
        </div>
      </div>
    </article>

    <!-- Not Found State -->
    <div v-else class="section-padding text-center">
      <svg class="w-24 h-24 mx-auto text-gray-400 mb-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
      </svg>
      <h2 class="text-2xl font-bold text-gray-900 mb-4">Article Not Found</h2>
      <p class="text-gray-600 mb-8">The article you're looking for doesn't exist or has been removed.</p>
      <router-link to="/blogs" class="inline-flex items-center gap-2 px-6 py-3 bg-[#8B4000] text-white rounded-full font-bold hover:bg-[#A0522D] transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
        Back to Blog
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useBlogStore } from '@/store/blog'
import AppLoader from '@/components/common/AppLoader.vue'

defineOptions({
  name: 'BlogDetailPage'
})

const route = useRoute()
const blogStore = useBlogStore()

const post = ref(null)
const loading = ref(true)
const relatedPosts = ref([])
const loadingRelated = ref(false)
const linkCopied = ref(false)

// Calculate reading time based on content length
const readingTime = computed(() => {
  if (!post.value?.content) return 5
  const wordsPerMinute = 200
  const words = post.value.content.split(/\s+/).length
  return Math.ceil(words / wordsPerMinute)
})

// Format content with proper HTML
const formattedContent = computed(() => {
  if (!post.value?.content) return ''
  const raw = String(post.value.content)
  const hasTags = /<[^>]+>/.test(raw)

  if (!hasTags) {
    // Convert plain text to HTML paragraphs
    const parts = raw.split(/\n\n+/).map(p => p.trim()).filter(Boolean)
    return parts.map(p => `<p>${p}</p>`).join('')
  }

  return raw
})

onMounted(async () => {
  try {
    // Fetch the blog post
    post.value = await blogStore.fetchPost(route.params.slug)

    // Fetch related posts (same category or latest)
    if (post.value) {
      loadingRelated.value = true
      try {
        const params = {
          status: 'PUBLISHED',
          limit: 3
        }

        // Try to get posts from same category
        if (post.value.category?.slug) {
          params.category = post.value.category.slug
        }

        const response = await blogStore.fetchPosts(params)
        const data = response.results || response

        // Filter out current post
        relatedPosts.value = (Array.isArray(data) ? data : [])
          .filter(p => p.slug !== post.value.slug)
          .slice(0, 3)
      } catch (error) {
        console.error('Failed to load related posts:', error)
      } finally {
        loadingRelated.value = false
      }
    }
  } catch (error) {
    console.error('Failed to load post:', error)
    post.value = null
  } finally {
    loading.value = false
  }
})

function getAuthorInitial() {
  if (!post.value) return 'S'
  const author = post.value.author?.username || post.value.author_name || 'Sauti'
  return author.charAt(0).toUpperCase()
}

function formatDate(dateString) {
  if (!dateString) return 'Recently'
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
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

function formatViews(views) {
  if (!views) return '0 views'
  if (views >= 1000000) return `${(views / 1000000).toFixed(1)}M views`
  if (views >= 1000) return `${(views / 1000).toFixed(1)}K views`
  return `${views} views`
}

function setPlaceholder(event) {
  event.target.src = 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?q=80&w=1200&auto=format&fit=crop'
}

// Social sharing functions
function shareOnFacebook() {
  const url = encodeURIComponent(window.location.href)
  window.open(`https://www.facebook.com/sharer/sharer.php?u=${url}`, '_blank', 'width=600,height=400')
}

function shareOnTwitter() {
  const url = encodeURIComponent(window.location.href)
  const text = encodeURIComponent(post.value?.title || '')
  window.open(`https://twitter.com/intent/tweet?url=${url}&text=${text}`, '_blank', 'width=600,height=400')
}

function shareOnWhatsApp() {
  const url = encodeURIComponent(window.location.href)
  const text = encodeURIComponent(post.value?.title || '')
  window.open(`https://wa.me/?text=${text}%20${url}`, '_blank')
}

function copyLink() {
  navigator.clipboard.writeText(window.location.href).then(() => {
    linkCopied.value = true
    setTimeout(() => {
      linkCopied.value = false
    }, 2000)
  })
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.prose {
  font-size: 1.125rem;
  line-height: 1.75;
}

.prose p {
  margin-bottom: 1.5em;
}

.prose h2 {
  font-size: 1.875rem;
  margin-top: 2em;
  margin-bottom: 1em;
}

.prose h3 {
  font-size: 1.5rem;
  margin-top: 1.5em;
  margin-bottom: 0.75em;
}

.prose ul,
.prose ol {
  margin-top: 1em;
  margin-bottom: 1em;
  padding-left: 1.5em;
}

.prose li {
  margin-bottom: 0.5em;
}

.prose blockquote {
  border-left: 4px solid #8B4000;
  padding-left: 1.5em;
  font-style: italic;
  margin: 2em 0;
  color: #555;
}

.prose img {
  margin: 2em 0;
}

.prose a {
  font-weight: 600;
}
</style>
