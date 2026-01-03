<template>
  <article
    class="group bg-sauti-white p-4 rounded-[2rem] border-2 border-sauti-neutral transition-all duration-500 hover:shadow-2xl hover:shadow-sauti-blue/10 hover:border-sauti-blue/30">
    <router-link :to="`/blogs/${post.slug}`" class="block">
      <!-- Featured Image -->
      <div class="relative bg-sauti-neutral rounded-2xl overflow-hidden aspect-video cursor-pointer">
        <img :src="post.featured_image || `https://picsum.photos/seed/${post.id + 116}/800/450`" :alt="post.title"
          class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" loading="lazy"
          @error="setPlaceholder" />

        <!-- Category Badge -->
        <div v-if="post.category" class="absolute top-4 left-4">
          <span
            class="text-[10px] font-black uppercase tracking-widest bg-sauti-darkGreen text-sauti-white px-3 py-1.5 rounded-xl shadow-lg">
            {{ post.category.name }}
          </span>
        </div>

        <!-- Featured Badge -->
        <div v-if="post.is_featured" class="absolute top-4 right-4">
          <span
            class="bg-sauti-blue text-sauti-white px-3 py-1.5 rounded-xl text-[10px] font-black uppercase tracking-widest shadow-lg">
            Featured
          </span>
        </div>
      </div>

      <!-- Content -->
      <div class="mt-6 flex gap-4">
        <!-- Author Avatar -->
        <div
          class="h-10 w-10 rounded-xl bg-sauti-orange flex items-center justify-center text-sauti-white font-black text-sm flex-shrink-0 shadow-lg shadow-sauti-orange/20 transition-transform group-hover:scale-110">
          {{ getAuthorInitial() }}
        </div>

        <!-- Post Info -->
        <div class="min-w-0">
          <!-- Title -->
          <h3
            class="text-base font-black text-sauti-darkGreen leading-tight mb-2 line-clamp-2 group-hover:text-sauti-blue transition-colors">
            {{ post.title }}
          </h3>

          <!-- Meta -->
          <div class="flex flex-wrap items-center gap-x-3 gap-y-1">
            <span class="text-[10px] text-sauti-darkGreen/60 font-black uppercase tracking-widest whitespace-nowrap">
              {{ post.author?.username || post.author_name || 'Sauti Uganda' }}
            </span>
            <span class="w-1 h-1 bg-sauti-neutral rounded-full"></span>
            <span class="text-[10px] text-sauti-darkGreen/40 font-black uppercase tracking-widest whitespace-nowrap">
              {{ formatViews(post.views_count) }} • {{ formatTimeAgo(post.published_at) }}
            </span>
          </div>
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
    // Using Picsum for more reliable varied placeholders
    const ph = `https://picsum.photos/seed/${props.post.id + 116}/800/450`
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
</style>
