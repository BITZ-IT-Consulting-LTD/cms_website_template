<template>
  <div class="min-h-screen bg-sauti-neutral">
    <!-- Loading State -->
    <AppLoader v-if="loading" :fullScreen="true" message="Loading article..." />

    <!-- Article Content -->
    <article v-else-if="post" class="bg-sauti-white">
      <!-- Hero Section -->
      <div class="relative h-[70vh] min-h-[500px] max-h-[800px] overflow-hidden bg-sauti-darkGreen">
        <img v-if="post.featured_image" :src="post.featured_image" :alt="post.title"
          class="absolute inset-0 w-full h-full object-cover opacity-60 scale-105" @error="setPlaceholder" />
        <div class="absolute inset-0 bg-gradient-to-t from-sauti-darkGreen via-sauti-darkGreen/40 to-transparent"></div>

        <!-- Hero Content -->
        <div class="relative h-full container-custom flex flex-col justify-end pb-24">
          <!-- Category Badge -->
          <div v-if="post.category" class="mb-8">
            <span
              class="inline-block px-6 py-2 bg-sauti-orange text-sauti-white text-[10px] font-black uppercase tracking-[0.2em] rounded-xl shadow-xl shadow-sauti-orange/20">
              {{ post.category.name }}
            </span>
          </div>

          <!-- Title -->
          <h1
            class="text-4xl md:text-6xl lg:text-7xl font-black text-sauti-white leading-[1.1] mb-10 max-w-5xl tracking-tight">
            {{ post.title }}
          </h1>

          <!-- Meta Info -->
          <div class="flex flex-wrap items-center gap-8 text-sauti-white/70">
            <!-- Author -->
            <div class="flex items-center gap-4">
              <div
                class="w-14 h-14 rounded-2xl bg-sauti-orange flex items-center justify-center text-sauti-white font-black text-xl shadow-lg shadow-sauti-orange/20">
                {{ getAuthorInitial() }}
              </div>
              <div>
                <p class="text-[10px] font-black uppercase tracking-widest text-sauti-white mb-1">
                  {{ post.author?.username || post.author_name || 'Sauti Uganda' }}
                </p>
                <p class="text-[10px] font-black uppercase tracking-widest text-sauti-white/40">
                  {{ formatDate(post.published_at) }}
                </p>
              </div>
            </div>

            <!-- Separator -->
            <div class="w-1 h-1 bg-sauti-white/20 rounded-full"></div>

            <!-- Reading Time -->
            <div class="flex items-center gap-3 text-[10px] font-black uppercase tracking-[0.2em]">
              <svg class="w-5 h-5 text-sauti-blue" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                  d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span>{{ readingTime }} min read</span>
            </div>

            <!-- Separator -->
            <div class="w-1 h-1 bg-sauti-white/20 rounded-full"></div>

            <!-- Views -->
            <div class="flex items-center gap-3 text-[10px] font-black uppercase tracking-[0.2em]">
              <svg class="w-5 h-5 text-sauti-lightGreen" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                  d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                  d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
              </svg>
              <span>{{ formatViews(post.views_count) }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Article Body -->
      <div class="py-20 bg-sauti-white">
        <div class="container-custom max-w-4xl">
          <!-- Excerpt -->
          <div v-if="post.excerpt" class="mb-16">
            <p
              class="text-2xl md:text-3xl text-sauti-darkGreen/80 leading-relaxed font-bold border-l-8 border-sauti-orange pl-10 py-4">
              {{ post.excerpt }}
            </p>
          </div>

          <!-- Tags -->
          <div v-if="post.tags && post.tags.length > 0" class="flex flex-wrap gap-3 mb-12">
            <span v-for="tag in post.tags" :key="tag.id"
              class="px-4 py-1.5 bg-sauti-neutral text-sauti-darkGreen/40 text-[10px] font-black uppercase tracking-widest rounded-xl hover:bg-sauti-blue/10 hover:text-sauti-blue transition-all cursor-pointer">
              #{{ tag.name }}
            </span>
          </div>

          <!-- Main Content -->
          <div class="prose-sauti max-w-none mb-20" v-html="formattedContent"></div>

          <!-- Share Section -->
          <div class="border-y-2 border-sauti-neutral py-12 my-16">
            <div class="flex flex-col md:flex-row items-center justify-between gap-10">
              <div class="text-center md:text-left">
                <h3 class="text-2xl font-black text-sauti-darkGreen mb-2">Share this article</h3>
                <p class="text-lg font-bold text-sauti-darkGreen/50">Help spread awareness about child protection</p>
              </div>

              <div class="flex items-center gap-4">
                <!-- Facebook -->
                <button @click="shareOnFacebook"
                  class="w-14 h-14 rounded-2xl bg-[#1877F2] text-sauti-white flex items-center justify-center hover:scale-110 transition-all shadow-xl shadow-[#1877F2]/20"
                  aria-label="Share on Facebook">
                  <svg class="w-7 h-7" fill="currentColor" viewBox="0 0 24 24">
                    <path
                      d="M22.675 0H1.325C.593 0 0 .593 0 1.325v21.351C0 23.407.593 24 1.325 24H12.82v-9.294H9.692V11.09h3.129V8.413c0-3.1 1.893-4.788 4.659-4.788 1.325 0 2.463.099 2.795.143v3.24l-1.918.001c-1.503 0-1.794.715-1.794 1.763v2.316h3.587l-.467 3.616h-3.12V24h6.116C23.407 24 24 23.407 24 22.676V1.325C24 .593 23.407 0 22.675 0z" />
                  </svg>
                </button>

                <!-- Twitter/X -->
                <button @click="shareOnTwitter"
                  class="w-14 h-14 rounded-2xl bg-sauti-darkGreen text-sauti-white flex items-center justify-center hover:scale-110 transition-all shadow-xl shadow-sauti-darkGreen/20"
                  aria-label="Share on X">
                  <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                    <path
                      d="M18.244 2H21l-6.52 7.455L22.5 22h-6.9l-4.5-6.22L5.7 22H3l7.03-8.036L1.5 2h7.02l4.08 5.64L18.244 2zm-2.41 18h1.6L8.28 4h-1.6l9.155 16z" />
                  </svg>
                </button>

                <!-- WhatsApp -->
                <button @click="shareOnWhatsApp"
                  class="w-14 h-14 rounded-2xl bg-[#25D366] text-sauti-white flex items-center justify-center hover:scale-110 transition-all shadow-xl shadow-[#25D366]/20"
                  aria-label="Share on WhatsApp">
                  <svg class="w-7 h-7" fill="currentColor" viewBox="0 0 24 24">
                    <path
                      d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.525 3.488" />
                  </svg>
                </button>

                <!-- Copy Link -->
                <button @click="copyLink"
                  class="w-14 h-14 rounded-2xl bg-sauti-neutral text-sauti-darkGreen flex items-center justify-center hover:scale-110 transition-all shadow-xl"
                  aria-label="Copy link" :title="linkCopied ? 'Copied!' : 'Copy link'">
                  <svg v-if="!linkCopied" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                      d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
                  </svg>
                  <svg v-else class="w-6 h-6 text-sauti-lightGreen" fill="none" stroke="currentColor"
                    viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                  </svg>
                </button>
              </div>
            </div>
          </div>

          <!-- Author Bio -->
          <div class="bg-sauti-neutral/30 rounded-[2.5rem] p-10 mb-20 border-2 border-sauti-neutral">
            <div class="flex flex-col md:flex-row items-center md:items-start text-center md:text-left gap-8">
              <div
                class="w-24 h-24 rounded-[2rem] bg-sauti-orange flex items-center justify-center text-sauti-white font-black text-4xl shadow-xl shadow-sauti-orange/20 flex-shrink-0">
                {{ getAuthorInitial() }}
              </div>
              <div class="flex-1">
                <p class="text-[10px] font-black uppercase tracking-widest text-sauti-darkGreen/40 mb-2">About the
                  Author</p>
                <h3 class="text-2xl font-black text-sauti-darkGreen mb-4">
                  {{ post.author?.username || post.author_name || 'Sauti Uganda' }}
                </h3>
                <p class="text-lg font-bold text-sauti-darkGreen/60 leading-relaxed">
                  Contributing writer at Sauti 116 Helpline, dedicated to raising awareness about child protection and
                  safety across Uganda.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </article>

    <!-- Related Posts Section -->
    <div class="bg-sauti-neutral py-32">
      <div class="container-custom max-w-6xl">
        <div class="text-center mb-16">
          <p class="text-[10px] font-black uppercase tracking-[0.4em] text-sauti-blue mb-4">Keep Reading</p>
          <h2 class="text-4xl md:text-5xl font-black text-sauti-darkGreen">Related Articles</h2>
        </div>

        <!-- Loading Related -->
        <div v-if="loadingRelated" class="flex justify-center py-20">
          <div class="animate-spin rounded-full h-16 w-16 border-b-4 border-sauti-blue"></div>
        </div>

        <!-- Related Posts Grid -->
        <div v-else-if="relatedPosts.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
          <router-link v-for="related in relatedPosts" :key="related.id" :to="`/blog/${related.slug}`"
            class="group bg-sauti-white rounded-[2.5rem] overflow-hidden border-2 border-sauti-neutral hover:border-sauti-blue/30 transition-all duration-500 shadow-sm hover:shadow-2xl hover:shadow-sauti-blue/10 transform hover:-translate-y-2">
            <!-- Image -->
            <div class="relative h-64 overflow-hidden">
              <img :src="related.featured_image" :alt="related.title"
                class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
                @error="setPlaceholder" />
              <div
                class="absolute inset-0 bg-gradient-to-t from-sauti-darkGreen/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500">
              </div>

              <!-- Category Badge -->
              <span v-if="related.category"
                class="absolute top-6 left-6 px-4 py-1.5 bg-sauti-darkGreen text-sauti-white text-[10px] font-black uppercase tracking-widest rounded-xl shadow-lg">
                {{ related.category.name }}
              </span>
            </div>

            <!-- Content -->
            <div class="p-8">
              <h3
                class="text-xl font-black text-sauti-darkGreen mb-4 leading-tight group-hover:text-sauti-blue transition-colors line-clamp-2">
                {{ related.title }}
              </h3>
              <p class="text-base font-bold text-sauti-darkGreen/50 mb-6 line-clamp-2">
                {{ related.excerpt }}
              </p>
              <div class="flex items-center justify-between pt-6 border-t border-sauti-neutral">
                <span class="text-[10px] font-black uppercase tracking-widest text-sauti-darkGreen/30">{{
                  formatTimeAgo(related.published_at) }}</span>
                <span
                  class="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-sauti-darkGreen/30">
                  <svg class="w-4 h-4 text-sauti-blue" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                      d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                  {{ formatViews(related.views_count) }}
                </span>
              </div>
            </div>
          </router-link>
        </div>

        <!-- Empty Related -->
        <div v-else class="text-center py-20 bg-sauti-white rounded-[3rem] border-2 border-dashed border-sauti-neutral">
          <p class="text-lg font-black text-sauti-darkGreen/30 uppercase tracking-[0.2em]">No related articles found</p>
        </div>
      </div>
    </div>
  </div>

  <!-- Not Found State -->
  <div v-else class="min-h-screen bg-sauti-neutral flex items-center justify-center p-10">
    <div
      class="max-w-2xl w-full bg-sauti-white rounded-[4rem] p-16 text-center shadow-2xl shadow-sauti-darkGreen/5 border-2 border-sauti-neutral">
      <div class="w-24 h-24 bg-sauti-neutral rounded-3xl flex items-center justify-center mx-auto mb-10">
        <svg class="w-12 h-12 text-sauti-darkGreen/30" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
            d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
        </svg>
      </div>
      <h2 class="text-4xl font-black text-sauti-darkGreen mb-4 tracking-tight">Article Not Found</h2>
      <p class="text-xl font-bold text-sauti-darkGreen/50 mb-12">The article you're looking for doesn't exist or has
        been removed.</p>
      <router-link to="/blogs"
        class="inline-flex items-center gap-4 px-10 py-5 bg-sauti-darkGreen text-sauti-white rounded-2xl font-black uppercase tracking-widest text-xs shadow-2xl shadow-sauti-darkGreen/20 hover:scale-105 transition-all">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
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
    if (diffDays < 365) return `${Math.ceil(diffDays / 365)} months ago`
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
    line-clamp: 2;
    overflow: hidden;
  }

  .line-clamp-3 {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    line-clamp: 3;
    overflow: hidden;
  }

  .prose-sauti {
    font-family: 'Cronos Pro', sans-serif;
    font-size: 1.25rem;
    line-height: 1.8;
    color: theme('colors.sauti-darkGreen');
    opacity: 0.8;
    font-weight: 500;
  }

  :deep(.prose-sauti p) {
    margin-bottom: 2em;
  }

  :deep(.prose-sauti h2) {
    font-size: 2.25rem;
    font-weight: 900;
    margin-top: 2.5em;
    margin-bottom: 1.25em;
    color: theme('colors.sauti-darkGreen');
    letter-spacing: -0.02em;
  }

  :deep(.prose-sauti h3) {
    font-size: 1.75rem;
    font-weight: 900;
    margin-top: 2em;
    margin-bottom: 1em;
    color: theme('colors.sauti-darkGreen');
  }

  :deep(.prose-sauti ul),
  :deep(.prose-sauti ol) {
    margin: 1.5em 0;
    padding-left: 1.5em;
  }

  :deep(.prose-sauti li) {
    margin-bottom: 1em;
    position: relative;
  }

  :deep(.prose-sauti blockquote) {
    border-left: 8px solid theme('colors.sauti-orange');
    background: theme('colors.sauti-neutral');
    padding: 2.5rem 3rem;
    border-radius: 0 2.5rem 2.5rem 0;
    font-style: italic;
    font-weight: 700;
    margin: 3rem 0;
    color: theme('colors.sauti-darkGreen');
    opacity: 0.9;
  }

  :deep(.prose-sauti img) {
    margin: 4rem 0;
    border-radius: 3rem;
    border: 2px solid theme('colors.sauti-neutral');
    box-shadow: 0 25px 50px -12px rgba(0, 43, 82, 0.15);
  }

  :deep(.prose-sauti a) {
    font-weight: 900;
    color: theme('colors.sauti-blue');
    text-decoration: underline;
    text-underline-offset: 4px;
  }
</style>
