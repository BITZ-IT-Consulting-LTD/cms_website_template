<template>
  <div class="min-h-screen bg-neutral-offwhite/40">
    <!-- Loading State -->
    <AppLoader v-if="loading" :fullScreen="true" message="Loading article..." />

    <!-- Article + sidebar -->
    <div v-else-if="post" class="container-custom py-5 lg:py-8">
      <!-- Utility bar: return path on the left, article search on the right -->
      <div class="flex flex-col sm:flex-row sm:items-center gap-3 sm:gap-4 mb-5">
        <router-link :to="backTo"
          class="inline-flex items-center gap-2 text-sm font-semibold text-secondary hover:text-primary transition-colors">
          <ArrowLeftIcon class="w-4 h-4" />
          {{ backLabel }}
        </router-link>

        <form @submit.prevent="submitSearch" class="sm:ml-auto w-full sm:w-72">
          <div
            class="flex items-center gap-2 bg-neutral-white rounded-xl border border-black/5 px-3 py-2 focus-within:ring-2 focus-within:ring-primary/25 transition-shadow">
            <MagnifyingGlassIcon class="w-4 h-4 text-black/35 shrink-0" />
            <input v-model="searchTerm" type="search" :placeholder="`Search ${collectionNoun.toLowerCase()}...`"
              :aria-label="`Search ${collectionNoun.toLowerCase()}`"
              class="w-full bg-transparent border-0 p-0 text-sm text-secondary placeholder:text-black/30 focus:ring-0 focus:outline-none" />
          </div>
        </form>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 lg:gap-7">
        <!-- ============ Main column ============ -->
        <main class="lg:col-span-8 min-w-0">
          <article class="bg-neutral-white rounded-2xl border border-black/5 shadow-sm p-5 sm:p-7 lg:p-9">
            <!-- Title -->
            <h1 class="text-2xl sm:text-3xl lg:text-[2.125rem] font-bold leading-[1.2] text-secondary mb-3">
              {{ post.title }}
            </h1>

            <!-- Byline: author, category, exact date and time -->
            <div class="flex flex-wrap items-center gap-x-3 gap-y-2 text-xs sm:text-sm text-black/55 pb-5 mb-6 border-b border-black/5">
              <span class="inline-flex items-center gap-2 font-semibold text-secondary">
                <span
                  class="w-6 h-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-[11px] font-bold">
                  {{ authorInitial }}
                </span>
                {{ authorName }}
              </span>
              <span v-if="post.category?.name" class="text-black/20">•</span>
              <span v-if="post.category?.name" class="font-semibold text-primary">{{ post.category.name }}</span>
              <span v-if="publishedLabel" class="text-black/20">•</span>
              <time v-if="publishedLabel" :datetime="publishedISO">{{ publishedLabel }}</time>
              <span class="text-black/20">•</span>
              <span class="inline-flex items-center gap-1">
                <ClockIcon class="w-3.5 h-3.5" />{{ readingTime }} min read
              </span>
              <span class="text-black/20">•</span>
              <span class="inline-flex items-center gap-1">
                <EyeIcon class="w-3.5 h-3.5" />{{ formatViews(post.views_count) }}
              </span>
            </div>

            <p v-if="updatedLabel" class="-mt-3 mb-6 text-xs text-black/45 italic">Updated {{ updatedLabel }}</p>

            <!-- Lead image -->
            <figure v-if="post.featured_image" class="mb-7">
              <img :src="post.featured_image_medium || post.featured_image" :alt="post.title" width="1200" height="675" loading="eager"
                fetchpriority="high" decoding="async"
                class="w-full aspect-[16/9] object-cover rounded-xl bg-neutral-offwhite" @error="setPlaceholder" />
            </figure>

            <!-- Standfirst -->
            <p v-if="post.excerpt" class="text-base sm:text-lg leading-relaxed text-black/70 mb-7">
              {{ post.excerpt }}
            </p>

            <!-- Body -->
            <div class="relative">
              <div class="prose-sauti" :class="{ 'content-collapsed': isLongContent && !contentExpanded }"
                v-html="formattedContent"></div>
              <div v-if="isLongContent && !contentExpanded" class="content-fade"></div>
            </div>
            <div v-if="isLongContent" class="mt-4">
              <button type="button" @click="contentExpanded = !contentExpanded"
                class="text-sm font-bold text-primary hover:text-secondary transition-colors">
                {{ contentExpanded ? 'Show less' : 'Read full article' }}
              </button>
            </div>

            <!-- Legacy single extra image, kept for posts created before galleries -->
            <figure v-if="post.secondary_image" class="mt-8">
              <img :src="post.secondary_image" :alt="post.title" width="1200" height="675" loading="lazy"
                decoding="async" class="w-full aspect-[16/9] object-cover rounded-xl bg-neutral-offwhite"
                @error="setPlaceholder" />
            </figure>

            <!-- Gallery: a grid that grows by rows, so 2 images and 30 images
                 both lay out sensibly. Clicking one opens the full-screen viewer. -->
            <section v-if="galleryImages.length" class="mt-9 pt-7 border-t border-black/5">
              <div class="flex items-baseline justify-between gap-4 mb-4">
                <h2 class="text-sm font-bold uppercase tracking-wider text-secondary">Gallery</h2>
                <span class="text-xs text-black/45">{{ galleryImages.length }}
                  {{ galleryImages.length === 1 ? 'image' : 'images' }}</span>
              </div>

              <ul class="grid grid-cols-2 sm:grid-cols-3 gap-2.5 list-none p-0 m-0">
                <li v-for="(img, idx) in galleryImages" :key="img.id || idx">
                  <button type="button" @click="openLightbox(idx)"
                    class="group relative block w-full overflow-hidden rounded-lg bg-neutral-offwhite focus:outline-none focus-visible:ring-2 focus-visible:ring-primary"
                    :aria-label="`Open image ${idx + 1} of ${galleryImages.length}${img.caption ? ': ' + img.caption : ''}`">
                    <img :src="img.image_thumbnail || img.image"
                      :alt="img.alt_text || img.caption || `${post.title} — image ${idx + 1}`"
                      width="400" height="300" loading="lazy" decoding="async"
                      class="w-full aspect-[4/3] object-cover transition-transform duration-300 group-hover:scale-[1.04]"
                      @error="setPlaceholder" />
                    <span
                      class="absolute inset-0 bg-secondary/0 group-hover:bg-secondary/15 transition-colors"></span>
                  </button>
                  <p v-if="img.caption" class="mt-1.5 text-[11px] leading-snug text-black/50 line-clamp-2">
                    {{ img.caption }}
                  </p>
                </li>
              </ul>
            </section>

            <!-- Tags -->
            <div v-if="post.tags?.length" class="mt-9 pt-7 border-t border-black/5 flex flex-wrap gap-2">
              <span v-for="tag in post.tags" :key="tag.id"
                class="px-3 py-1 rounded-lg bg-neutral-offwhite/60 text-[11px] font-bold uppercase tracking-wide text-primary">
                #{{ tag.name }}
              </span>
            </div>

            <!-- Author -->
            <div class="mt-9 pt-7 border-t border-black/5 flex items-start gap-4">
              <div
                class="w-11 h-11 rounded-full bg-primary text-neutral-white flex items-center justify-center font-bold shrink-0">
                {{ authorInitial }}
              </div>
              <div class="min-w-0">
                <p class="text-[11px] font-bold uppercase tracking-wider text-black/40 mb-1">Written by</p>
                <p class="text-base font-bold text-secondary">{{ authorName }}</p>
                <p class="text-sm text-black/60 leading-relaxed mt-1">
                  Contributing writer at the Sauti 116 Helpline, covering child protection and safety across Uganda.
                </p>
              </div>
            </div>
          </article>
        </main>

        <!-- ============ Sidebar ============ -->
        <aside class="lg:col-span-4 min-w-0 space-y-5 lg:sticky lg:top-24 lg:self-start">
          <!-- Share -->
          <section class="bg-neutral-white rounded-2xl border border-black/5 shadow-sm p-5">
            <h2 class="text-sm font-bold uppercase tracking-wider text-secondary mb-4">Share to</h2>
            <ul class="flex flex-wrap gap-2 list-none p-0 m-0">
              <li v-for="target in shareTargets" :key="target.label">
                <button type="button" @click="target.action"
                  class="w-10 h-10 rounded-full flex items-center justify-center bg-neutral-offwhite/60 hover:bg-neutral-offwhite transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-2"
                  :title="target.label" :aria-label="target.label">
                  <BrandIcon :name="target.brand" class="w-[18px] h-[18px]" />
                </button>
              </li>
              <li>
                <button type="button" @click="copyLink"
                  class="w-10 h-10 rounded-full flex items-center justify-center border border-primary/30 text-primary bg-neutral-white transition-transform hover:scale-105 focus:outline-none focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-2"
                  :title="linkCopied ? 'Link copied' : 'Copy link'"
                  :aria-label="linkCopied ? 'Link copied' : 'Copy link'">
                  <CheckIcon v-if="linkCopied" class="w-[18px] h-[18px]" />
                  <LinkIcon v-else class="w-[18px] h-[18px]" />
                </button>
              </li>
            </ul>
            <!-- Instagram and TikTok have no web share URL, so route them through
                 the device share sheet where it exists and copy-to-clipboard where
                 it does not, rather than offering a button that does nothing. -->
            <button type="button" @click="shareToApps"
              class="mt-4 w-full text-left text-xs font-semibold text-primary hover:text-secondary transition-colors">
              {{ appShareLabel }}
            </button>
            <p v-if="shareNotice" class="mt-2 text-xs text-black/55">{{ shareNotice }}</p>
          </section>

          <!-- Related -->
          <section class="bg-neutral-white rounded-2xl border border-black/5 shadow-sm p-5">
            <h2 class="text-sm font-bold uppercase tracking-wider text-secondary mb-4">Related articles</h2>

            <div v-if="loadingRelated" class="py-6 flex justify-center">
              <div class="spinner"></div>
            </div>

            <ul v-else-if="relatedPosts.length" class="list-none p-0 m-0 divide-y divide-black/5">
              <li v-for="related in relatedPosts" :key="related.id">
                <router-link :to="`/blogs/${related.slug}`" class="group flex gap-3 py-3">
                  <img :src="related.featured_image_thumbnail || related.featured_image" :alt="related.title" width="80" height="64" loading="lazy"
                    decoding="async"
                    class="w-20 h-16 rounded-lg object-cover bg-neutral-offwhite shrink-0" @error="setPlaceholder" />
                  <div class="min-w-0">
                    <p
                      class="text-sm font-bold leading-snug text-secondary group-hover:text-primary transition-colors line-clamp-2">
                      {{ related.title }}
                    </p>
                    <p class="mt-1 text-[11px] font-semibold uppercase tracking-wide text-black/40">
                      {{ related.category_name || collectionNoun }}
                    </p>
                  </div>
                </router-link>
              </li>
            </ul>

            <p v-else class="text-sm text-black/45 py-2">No related articles yet.</p>
          </section>
        </aside>
      </div>
    </div>

    <!-- Not Found -->
    <div v-else class="min-h-screen flex items-center justify-center p-6">
      <div class="max-w-lg w-full bg-neutral-white rounded-2xl border border-black/5 shadow-sm p-10 text-center">
        <div
          class="w-14 h-14 bg-primary/10 rounded-xl flex items-center justify-center mx-auto mb-5 text-primary">
          <DocumentTextIcon class="w-7 h-7" />
        </div>
        <h1 class="text-2xl font-bold text-secondary mb-3">Article not found</h1>
        <p class="text-base text-black/60 mb-8">This article doesn't exist, or it has been removed.</p>
        <BaseCTA href="/news" variant="primary" class="inline-flex items-center gap-3">
          <ArrowLeftIcon class="w-4 h-4" />
          Back to news
        </BaseCTA>
      </div>
    </div>

    <!-- Full-screen image viewer -->
    <div v-if="lightboxOpen" class="fixed inset-0 z-[100] bg-neutral-black/92 flex flex-col" role="dialog"
      aria-modal="true" :aria-label="`Image ${lightboxIndex + 1} of ${galleryImages.length}`" @click.self="closeLightbox">
      <div class="flex items-center justify-between gap-4 px-4 py-3 text-neutral-white/80 text-sm shrink-0">
        <span>{{ lightboxIndex + 1 }} / {{ galleryImages.length }}</span>
        <button ref="lightboxCloseButton" type="button" @click="closeLightbox" aria-label="Close image viewer"
          class="w-9 h-9 rounded-full bg-neutral-white/10 hover:bg-neutral-white/20 flex items-center justify-center transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-neutral-white">
          <XMarkIcon class="w-5 h-5" />
        </button>
      </div>

      <div class="flex-1 min-h-0 flex items-center justify-center px-4 pb-2" @click.self="closeLightbox">
        <img :src="activeGalleryImage?.image_medium || activeGalleryImage?.image"
          :alt="activeGalleryImage?.alt_text || activeGalleryImage?.caption || post?.title"
          class="max-h-full max-w-full object-contain rounded-lg" />
      </div>

      <div class="shrink-0 px-4 pb-5 pt-2 flex items-center justify-between gap-4">
        <button v-if="galleryImages.length > 1" type="button" @click="stepLightbox(-1)" aria-label="Previous image"
          class="w-10 h-10 rounded-full bg-neutral-white/10 text-neutral-white hover:bg-neutral-white/20 flex items-center justify-center transition-colors shrink-0 focus:outline-none focus-visible:ring-2 focus-visible:ring-neutral-white">
          <ChevronLeftIcon class="w-5 h-5" />
        </button>
        <p class="flex-1 text-center text-sm text-neutral-white/85 leading-snug">
          {{ activeGalleryImage?.caption || '' }}
        </p>
        <button v-if="galleryImages.length > 1" type="button" @click="stepLightbox(1)" aria-label="Next image"
          class="w-10 h-10 rounded-full bg-neutral-white/10 text-neutral-white hover:bg-neutral-white/20 flex items-center justify-center transition-colors shrink-0 focus:outline-none focus-visible:ring-2 focus-visible:ring-neutral-white">
          <ChevronRightIcon class="w-5 h-5" />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted, onBeforeUnmount, computed, watch, nextTick } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import { useBlogStore } from '@/store/blog'
  import AppLoader from '@/components/common/AppLoader.vue'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import BrandIcon from '@/components/common/BrandIcon.vue'
  import {
    ClockIcon,
    EyeIcon,
    LinkIcon,
    CheckIcon,
    ArrowLeftIcon,
    DocumentTextIcon,
    ChevronLeftIcon,
    ChevronRightIcon,
    XMarkIcon,
    MagnifyingGlassIcon
  } from '@heroicons/vue/24/outline'
  import helplineAction from '@/assets/helpline-action.png'

  defineOptions({
    name: 'BlogDetailPage'
  })

  const route = useRoute()
  const router = useRouter()
  const blogStore = useBlogStore()

  const post = ref(null)
  const loading = ref(true)
  const relatedPosts = ref([])
  const loadingRelated = ref(false)
  const linkCopied = ref(false)
  const contentExpanded = ref(false)
  const searchTerm = ref('')
  const shareNotice = ref('')

  /* ---------------- Author / meta ---------------- */

  const authorName = computed(() =>
    post.value?.author?.username || post.value?.author_name || 'Sauti Uganda Team'
  )

  const authorInitial = computed(() => authorName.value.charAt(0).toUpperCase())

  // NEWS and BLOG posts share this detail route, so derive the return path from
  // the post's own type rather than assuming the reader came from one of them.
  const collectionNoun = computed(() => (post.value?.post_type === 'BLOG' ? 'Blog' : 'News'))
  const backTo = computed(() => (post.value?.post_type === 'BLOG' ? '/blogs' : '/news'))
  const backLabel = computed(() => `Back to ${collectionNoun.value.toLowerCase()}`)

  const readingTime = computed(() => {
    if (!post.value?.content) return 1
    const words = String(post.value.content).replace(/<[^>]+>/g, ' ').trim().split(/\s+/).length
    return Math.max(1, Math.ceil(words / 200))
  })

  /* ---------------- Dates ----------------
     Always an explicit date and time. `published_at` can be null on posts that
     were never formally published, so fall back to `created_at` instead of
     printing a vague "Recently". */

  const publishedSource = computed(() => post.value?.published_at || post.value?.created_at || null)
  const publishedISO = computed(() => publishedSource.value || undefined)
  const publishedLabel = computed(() => formatDateTime(publishedSource.value))

  const updatedLabel = computed(() => {
    const updated = post.value?.updated_at
    if (!updated || !publishedSource.value) return ''
    if (new Date(updated).getTime() - new Date(publishedSource.value).getTime() < 60000) return ''
    return formatDateTime(updated)
  })

  function formatDateTime(dateString) {
    if (!dateString) return ''
    const date = new Date(dateString)
    if (Number.isNaN(date.getTime())) return ''
    return date.toLocaleString('en-GB', {
      day: 'numeric', month: 'long', year: 'numeric',
      hour: '2-digit', minute: '2-digit', hour12: false
    })
  }

  function formatViews(views) {
    if (!views) return '0 views'
    if (views >= 1000000) return `${(views / 1000000).toFixed(1)}M views`
    if (views >= 1000) return `${(views / 1000).toFixed(1)}K views`
    return `${views} ${views === 1 ? 'view' : 'views'}`
  }

  /* ---------------- Body ---------------- */

  const isLongContent = computed(() =>
    String(post.value?.content || '').replace(/<[^>]+>/g, '').length > 2500
  )

  const formattedContent = computed(() => {
    if (!post.value?.content) return ''
    const raw = String(post.value.content)
    if (/<[^>]+>/.test(raw)) return raw
    return raw.split(/\n\n+/).map(p => p.trim()).filter(Boolean).map(p => `<p>${p}</p>`).join('')
  })

  /* ---------------- Gallery + viewer ---------------- */

  const galleryImages = computed(() => Array.isArray(post.value?.images) ? post.value.images : [])
  const lightboxOpen = ref(false)
  const lightboxIndex = ref(0)
  const lightboxCloseButton = ref(null)
  const activeGalleryImage = computed(() => galleryImages.value[lightboxIndex.value] || null)

  async function openLightbox(index) {
    lightboxIndex.value = index
    lightboxOpen.value = true
    document.body.style.overflow = 'hidden'
    await nextTick()
    lightboxCloseButton.value?.focus()
  }

  function closeLightbox() {
    lightboxOpen.value = false
    document.body.style.overflow = ''
  }

  function stepLightbox(delta) {
    const total = galleryImages.value.length
    if (!total) return
    lightboxIndex.value = (lightboxIndex.value + delta + total) % total
  }

  function onKeydown(event) {
    if (!lightboxOpen.value) return
    if (event.key === 'Escape') closeLightbox()
    else if (event.key === 'ArrowLeft') stepLightbox(-1)
    else if (event.key === 'ArrowRight') stepLightbox(1)
  }

  watch(() => post.value?.id, () => { lightboxIndex.value = 0 })

  /* ---------------- Sharing ----------------
     Share links are built from the canonical public base URL when one is
     configured, so a link shared from a dev host or a raw IP still points at
     the public site instead of an address nobody else can open. */

  const shareUrl = computed(() => {
    const configured = String(import.meta.env.VITE_PUBLIC_BASE_URL || '').trim().replace(/\/+$/, '')
    if (typeof window === 'undefined') return configured
    if (!configured) return window.location.href
    return `${configured}${window.location.pathname}${window.location.search}`
  })

  const shareTitle = computed(() => post.value?.title || 'Sauti 116 Helpline')

  const shareTargets = computed(() => [
    {
      label: 'Share on Facebook', brand: 'facebook',
      action: () => openShareWindow(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(shareUrl.value)}`)
    },
    {
      label: 'Share on X', brand: 'x',
      action: () => openShareWindow(`https://twitter.com/intent/tweet?url=${encodeURIComponent(shareUrl.value)}&text=${encodeURIComponent(shareTitle.value)}`)
    },
    {
      label: 'Share on WhatsApp', brand: 'whatsapp',
      action: () => openShareWindow(`https://wa.me/?text=${encodeURIComponent(`${shareTitle.value} ${shareUrl.value}`)}`)
    },
    {
      label: 'Share on LinkedIn', brand: 'linkedin',
      action: () => openShareWindow(`https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(shareUrl.value)}`)
    },
    {
      label: 'Share on Telegram', brand: 'telegram',
      action: () => openShareWindow(`https://t.me/share/url?url=${encodeURIComponent(shareUrl.value)}&text=${encodeURIComponent(shareTitle.value)}`)
    },
    {
      label: 'Share by email', brand: 'email',
      action: () => { window.location.href = `mailto:?subject=${encodeURIComponent(shareTitle.value)}&body=${encodeURIComponent(shareUrl.value)}` }
    }
  ])

  const canUseAppShare = computed(() => typeof navigator !== 'undefined' && typeof navigator.share === 'function')

  const appShareLabel = computed(() =>
    canUseAppShare.value ? 'Share to Instagram, TikTok or another app' : 'Copy link for Instagram or TikTok'
  )

  function openShareWindow(url) {
    window.open(url, '_blank', 'noopener,noreferrer,width=640,height=520')
  }

  async function shareToApps() {
    if (canUseAppShare.value) {
      try {
        await navigator.share({ title: shareTitle.value, text: shareTitle.value, url: shareUrl.value })
        return
      } catch {
        // The reader dismissed the share sheet, or it is unavailable here.
      }
    }
    await writeToClipboard()
    shareNotice.value = 'Link copied. Paste it into your Instagram or TikTok post.'
    setTimeout(() => { shareNotice.value = '' }, 6000)
  }

  async function writeToClipboard() {
    try {
      await navigator.clipboard.writeText(shareUrl.value)
      return true
    } catch {
      return false
    }
  }

  async function copyLink() {
    const copied = await writeToClipboard()
    if (copied) {
      linkCopied.value = true
      setTimeout(() => { linkCopied.value = false }, 2000)
    } else {
      shareNotice.value = 'Copying is blocked in this browser. Copy the address bar instead.'
      setTimeout(() => { shareNotice.value = '' }, 6000)
    }
  }

  /* ---------------- Search ---------------- */

  function submitSearch() {
    const term = searchTerm.value.trim()
    router.push({ path: backTo.value, query: term ? { search: term } : {} })
  }

  /* ---------------- Data ---------------- */

  function setPlaceholder(event) {
    event.target.src = helplineAction
  }

  async function loadRelated() {
    loadingRelated.value = true
    try {
      const params = { status: 'PUBLISHED', limit: 8 }
      if (post.value.category?.slug) params.category = post.value.category.slug
      if (post.value.post_type) params.post_type = post.value.post_type
      const response = await blogStore.fetchPosts(params)
      const data = response.results || response
      relatedPosts.value = (Array.isArray(data) ? data : [])
        .filter(p => p.slug !== post.value.slug)
        .slice(0, 6)
    } catch (error) {
      console.error('Failed to load related posts:', error)
      relatedPosts.value = []
    } finally {
      loadingRelated.value = false
    }
  }

  async function loadPost(slug) {
    loading.value = true
    try {
      post.value = await blogStore.fetchPost(slug)
      if (post.value) await loadRelated()
    } catch (error) {
      console.error('Failed to load post:', error)
      post.value = null
    } finally {
      loading.value = false
    }
  }

  onMounted(() => {
    window.addEventListener('keydown', onKeydown)
    loadPost(route.params.slug)
  })

  onBeforeUnmount(() => {
    window.removeEventListener('keydown', onKeydown)
    document.body.style.overflow = ''
  })

  // Clicking a related article changes only the slug, so the component is
  // reused and needs to refetch rather than showing the previous article.
  watch(() => route.params.slug, (slug) => {
    if (!slug) return
    closeLightbox()
    contentExpanded.value = false
    window.scrollTo({ top: 0, behavior: 'auto' })
    loadPost(slug)
  })
</script>

<style scoped>
  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  /* Article body: read like an article, not a poster. Regular weight, normal
     line length, left-aligned (justified text opens rivers on narrow columns). */
  :deep(.prose-sauti) {
    font-size: 1.0625rem;
    line-height: 1.75;
    color: rgba(0, 0, 0, 0.8);
  }

  :deep(.prose-sauti p) {
    margin-bottom: 1.25rem;
  }

  :deep(.prose-sauti h2) {
    @apply font-bold text-secondary normal-case tracking-tight;
    font-size: 1.375rem;
    line-height: 1.3;
    margin: 2rem 0 0.75rem;
  }

  :deep(.prose-sauti h3) {
    @apply font-bold text-secondary normal-case;
    font-size: 1.125rem;
    line-height: 1.4;
    margin: 1.5rem 0 0.5rem;
  }

  :deep(.prose-sauti blockquote) {
    @apply border-l-4 border-primary bg-neutral-offwhite/40 rounded-r-lg italic;
    padding: 1rem 1.25rem;
    margin: 1.5rem 0;
  }

  :deep(.prose-sauti img) {
    @apply rounded-xl;
    margin: 1.75rem 0;
    max-width: 100%;
    height: auto;
  }

  :deep(.prose-sauti ul),
  :deep(.prose-sauti ol) {
    margin: 1.25rem 0;
    padding-left: 1.5rem;
  }

  :deep(.prose-sauti ul li) {
    @apply list-disc;
    margin-bottom: 0.5rem;
  }

  :deep(.prose-sauti ol li) {
    @apply list-decimal;
    margin-bottom: 0.5rem;
  }

  :deep(.prose-sauti a) {
    @apply font-semibold text-primary underline underline-offset-2 hover:text-secondary transition-colors;
  }

  :deep(.prose-sauti table) {
    display: block;
    overflow-x: auto;
    max-width: 100%;
  }

  .content-collapsed {
    max-height: 32rem;
    overflow: hidden;
  }

  .content-fade {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 6rem;
    pointer-events: none;
    background: linear-gradient(to bottom, rgba(255, 255, 255, 0), rgba(255, 255, 255, 1));
  }

  @media (prefers-reduced-motion: reduce) {

    :deep(*),
    :deep(*)::before,
    :deep(*)::after {
      transition-duration: 0.01ms !important;
      animation-duration: 0.01ms !important;
    }
  }
</style>
