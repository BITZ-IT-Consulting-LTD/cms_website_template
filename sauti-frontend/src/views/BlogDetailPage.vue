<template>
  <div class="min-h-screen bg-neutral-white">
    <!-- Loading State -->
    <AppLoader v-if="loading" :fullScreen="true" message="Loading article..." />

    <!-- Article Content -->
    <article v-else-if="post" class="bg-neutral-white">
      <!-- 1. Article Hero Section -->
      <section class="relative h-[60vh] min-h-[500px] overflow-hidden bg-secondary">
        <img v-if="post.featured_image" :src="post.featured_image" :alt="post.title"
          class="absolute inset-0 w-full h-full object-cover opacity-60 scale-105" @error="setPlaceholder" />
        <div class="absolute inset-0 bg-gradient-to-t from-secondary via-secondary/40 to-transparent"></div>

        <div class="relative h-full container-custom flex flex-col justify-end pb-16 md:pb-24">
          <!-- Category Pill -->
          <div v-if="post.category" class="mb-8">
            <span class="pill bg-hotline text-neutral-white text-[10px] shadow-xl">
              {{ post.category.name }}
            </span>
          </div>

          <!-- Title -->
          <h1 class="page-header-title text-neutral-white !mb-10 max-w-5xl">
            {{ post.title }}
          </h1>

          <!-- Meta Info -->
          <div class="flex flex-wrap items-center gap-8">
            <!-- Author Card -->
            <div class="flex items-center gap-4">
              <div
                class="w-14 h-14 rounded-2xl bg-neutral-white/10 backdrop-blur-md flex items-center justify-center text-neutral-white font-bold text-xl border border-neutral-white/20">
                {{ getAuthorInitial() }}
              </div>
              <div>
                <p class="campaign-header text-[10px] text-neutral-white mb-1">
                  {{ post.author?.username || post.author_name || 'Sauti Uganda' }}
                </p>
                <p class="campaign-header text-[10px] text-neutral-white/40">
                  {{ formatDate(post.published_at) }}
                </p>
              </div>
            </div>

            <div class="hidden sm:block w-px h-8 bg-neutral-white/20"></div>

            <!-- Reading Time -->
            <div class="flex items-center gap-3 campaign-header text-[10px] text-neutral-white/70">
              <ClockIcon class="w-5 h-5 text-primary" />
              <span>{{ readingTime }} min read</span>
            </div>

            <div class="hidden sm:block w-px h-8 bg-neutral-white/20"></div>

            <!-- Views -->
            <div class="flex items-center gap-3 campaign-header text-[10px] text-neutral-white/70">
              <EyeIcon class="w-5 h-5 text-secondary-light" />
              <span>{{ formatViews(post.views_count) }}</span>
            </div>
          </div>
        </div>
      </section>

      <!-- 2. Article Body Wrapper -->
      <div class="section-padding bg-neutral-white">
        <div class="container-custom max-w-4xl">
          <!-- Excerpt / Summary -->
          <div v-if="post.excerpt" class="mb-20">
            <p
              class="text-2xl md:text-3xl text-secondary font-bold leading-relaxed border-l-8 border-primary pl-10 py-4 opacity-80">
              {{ post.excerpt }}
            </p>
          </div>

          <!-- Main Typography Content -->
          <div class="prose-sauti max-w-none mb-24" v-html="formattedContent"></div>

          <!-- Tags -->
          <div v-if="post.tags && post.tags.length > 0"
            class="flex flex-wrap gap-3 mb-16 pt-12 border-t-2 border-neutral-offwhite">
            <span v-for="tag in post.tags" :key="tag.id"
              class="px-5 py-2 bg-neutral-offwhite/30 text-primary text-[10px] font-bold uppercase tracking-widest rounded-xl hover:bg-primary hover:text-neutral-white transition-all cursor-pointer">
              #{{ tag.name }}
            </span>
          </div>

          <!-- Share Action Group -->
          <div class="bg-neutral-offwhite/30 rounded-[3rem] p-10 md:p-16 border-2 border-neutral-offwhite">
            <div class="flex flex-col md:flex-row items-center justify-between gap-12">
              <div class="text-center md:text-left">
                <h3 class="campaign-header text-2xl text-secondary mb-3">Share this article</h3>
                <p class="text-lg font-bold text-black/50">Help spread awareness about child protection in
                  Uganda.</p>
              </div>

              <div class="flex items-center gap-4">
                <button v-for="social in [
                  { icon: 'Facebook', color: 'bg-[#1877F2]', action: shareOnFacebook, label: 'Facebook' },
                  { icon: 'Twitter', color: 'bg-secondary', action: shareOnTwitter, label: 'Twitter' },
                  { icon: 'WhatsApp', color: 'bg-[#25D366]', action: shareOnWhatsApp, label: 'WhatsApp' }
                ]" :key="social.icon" @click="social.action"
                  :class="['w-14 h-14 rounded-2xl text-neutral-white flex items-center justify-center hover:scale-110 transition-all shadow-xl', social.color]"
                  :aria-label="`Share on ${social.label}`">
                  <span class="sr-only">{{ social.label }}</span>
                  <component :is="social.icon === 'Facebook' ? ShareIcon : ShareIcon" class="w-6 h-6" />
                </button>

                <button @click="copyLink"
                  class="w-14 h-14 rounded-2xl bg-neutral-white border-2 border-primary text-primary flex items-center justify-center hover:scale-110 transition-all shadow-xl"
                  aria-label="Copy link">
                  <LinkIcon v-if="!linkCopied" class="w-6 h-6" />
                  <CheckIcon v-else class="w-6 h-6 text-secondary-light" />
                </button>
              </div>
            </div>
          </div>

          <!-- Author Biography -->
          <div
            class="mt-20 flex flex-col md:flex-row items-center md:items-start text-center md:text-left gap-10 p-10 bg-primary/5 rounded-[3rem] border-2 border-primary/10">
            <div
              class="w-24 h-24 rounded-[2rem] bg-primary flex items-center justify-center text-neutral-white font-bold text-4xl shadow-xl shrink-0">
              {{ getAuthorInitial() }}
            </div>
            <div class="flex-1">
              <p class="campaign-header text-[10px] text-black/40 mb-3">Written By</p>
              <h4 class="campaign-header text-2xl text-secondary mb-4">
                {{ post.author?.username || post.author_name || 'Sauti Uganda Team' }}
              </h4>
              <p class="text-lg font-bold text-black/60 leading-relaxed">
                Contributing writer at Sauti 116 Helpline, dedicated to raising awareness about child protection and
                safety across Uganda.
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- 3. Related Content Section -->
      <section class="section-padding bg-neutral-offwhite/20 border-t-2 border-neutral-offwhite">
        <div class="container-custom">
          <div class="text-center mb-16">
            <p class="campaign-header text-[10px] text-primary mb-4">Keep Reading</p>
            <h2 class="campaign-header text-4xl text-secondary">Related Articles</h2>
          </div>

          <div v-if="loadingRelated" class="flex justify-center py-20">
            <div class="spinner"></div>
          </div>

          <div v-else-if="relatedPosts.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
            <router-link v-for="related in relatedPosts" :key="related.id" :to="`/blog/${related.slug}`"
              class="card-base group overflow-hidden !p-0">
              <div class="relative h-64 overflow-hidden">
                <img :src="related.featured_image" :alt="related.title"
                  class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
                  @error="setPlaceholder" />
                <div
                  class="absolute inset-0 bg-gradient-to-t from-secondary/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500">
                </div>
                <span v-if="related.category"
                  class="absolute top-6 left-6 pill bg-secondary text-neutral-white text-[10px]">
                  {{ related.category.name }}
                </span>
              </div>

              <div class="p-8">
                <h3
                  class="campaign-header text-xl text-secondary mb-4 leading-tight group-hover:text-primary transition-colors line-clamp-2">
                  {{ related.title }}
                </h3>
                <p class="text-base font-bold text-black/50 mb-8 line-clamp-2">
                  {{ related.excerpt }}
                </p>
                <div class="flex items-center justify-between pt-6 border-t-2 border-neutral-offwhite">
                  <span class="campaign-header text-[10px] text-secondary/30">{{
                    formatTimeAgo(related.published_at) }}</span>
                  <div class="flex items-center gap-2 campaign-header text-[10px] text-secondary/30">
                    <EyeIcon class="w-4 h-4" />
                    {{ formatViews(related.views_count) }}
                  </div>
                </div>
              </div>
            </router-link>
          </div>

          <div v-else
            class="text-center py-20 bg-neutral-white rounded-[3rem] border-2 border-dashed border-neutral-offwhite">
            <p class="campaign-header text-black/30">No related articles found</p>
          </div>
        </div>
      </section>
    </article>

    <!-- 4. Not Found State -->
    <div v-else class="min-h-screen bg-neutral-white flex items-center justify-center p-10">
      <div
        class="max-w-2xl w-full bg-neutral-white rounded-[4rem] p-16 text-center shadow-2xl border-2 border-primary">
        <div
          class="w-24 h-24 bg-primary/10 border-2 border-primary rounded-3xl flex items-center justify-center mx-auto mb-10 text-primary">
          <DocumentTextIcon class="w-12 h-12" />
        </div>
        <h2 class="campaign-header text-4xl text-secondary mb-6">Article Not Found</h2>
        <p class="text-xl font-bold text-black/50 mb-12">The article you're looking for doesn't exist or has
          been removed from our records.</p>
        <BaseCTA href="/blogs" variant="primary" class="inline-flex items-center gap-4 !px-12">
          <ArrowLeftIcon class="w-5 h-5" />
          Back to Blog
        </BaseCTA>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted, computed } from 'vue'
  import { useRoute } from 'vue-router'
  import { useBlogStore } from '@/store/blog'
  import AppLoader from '@/components/common/AppLoader.vue'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import {
    ClockIcon,
    EyeIcon,
    LinkIcon,
    CheckIcon,
    ShareIcon,
    ArrowLeftIcon,
    DocumentTextIcon
  } from '@heroicons/vue/24/outline'
  import helplineAction from '@/assets/helpline-action.png'

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

  const readingTime = computed(() => {
    if (!post.value?.content) return 5
    const wordsPerMinute = 200
    const words = post.value.content.split(/\s+/).length
    return Math.ceil(words / wordsPerMinute)
  })

  const formattedContent = computed(() => {
    if (!post.value?.content) return ''
    const raw = String(post.value.content)
    const hasTags = /<[^>]+>/.test(raw)

    if (!hasTags) {
      const parts = raw.split(/\n\n+/).map(p => p.trim()).filter(Boolean)
      return parts.map(p => `<p>${p}</p>`).join('')
    }
    return raw
  })

  onMounted(async () => {
    try {
      post.value = await blogStore.fetchPost(route.params.slug)
      if (post.value) {
        loadingRelated.value = true
        try {
          const params = { status: 'PUBLISHED', limit: 3 }
          if (post.value.category?.slug) params.category = post.value.category.slug
          const response = await blogStore.fetchPosts(params)
          const data = response.results || response
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
      year: 'numeric', month: 'long', day: 'numeric'
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
    return `${Math.ceil(diffDays / 30)} months ago`
  }

  function formatViews(views) {
    if (!views) return '0 views'
    if (views >= 1000000) return `${(views / 1000000).toFixed(1)}M views`
    if (views >= 1000) return `${(views / 1000).toFixed(1)}K views`
    return `${views} views`
  }

  function setPlaceholder(event) {
    event.target.src = helplineAction
  }

  function shareOnFacebook() {
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(window.location.href)}`, '_blank', 'width=600,height=400')
  }

  function shareOnTwitter() {
    window.open(`https://twitter.com/intent/tweet?url=${encodeURIComponent(window.location.href)}&text=${encodeURIComponent(post.value?.title || '')}`, '_blank', 'width=600,height=400')
  }

  function shareOnWhatsApp() {
    window.open(`https://wa.me/?text=${encodeURIComponent(post.value?.title || '')}%20${encodeURIComponent(window.location.href)}`, '_blank')
  }

  function copyLink() {
    navigator.clipboard.writeText(window.location.href).then(() => {
      linkCopied.value = true
      setTimeout(() => linkCopied.value = false, 2000)
    })
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

  :deep(.prose-sauti) {
    @apply text-xl md:text-2xl text-secondary leading-loose font-bold opacity-90;
  }

  :deep(.prose-sauti p) {
    @apply mb-10;
  }

  :deep(.prose-sauti h2) {
    @apply font-sans font-bold text-4xl text-secondary mt-20 mb-10 tracking-tight normal-case;
  }

  :deep(.prose-sauti h3) {
    @apply font-sans font-bold text-2xl text-secondary mt-16 mb-8 normal-case;
  }

  :deep(.prose-sauti blockquote) {
    @apply border-l-8 border-hotline bg-neutral-offwhite/30 p-12 rounded-r-[3rem] italic font-bold text-2xl my-16 border-2 border-neutral-offwhite;
  }

  :deep(.prose-sauti img) {
    @apply my-20 rounded-[4rem] border-4 border-primary shadow-2xl;
  }

  :deep(.prose-sauti ul),
  :deep(.prose-sauti ol) {
    @apply my-10 pl-10;
  }

  :deep(.prose-sauti li) {
    @apply mb-6 list-disc;
  }

  :deep(.prose-sauti a) {
    @apply font-bold text-primary underline underline-offset-8 decoration-4 hover:text-secondary transition-all;
  }
</style>
