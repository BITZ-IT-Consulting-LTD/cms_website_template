<template>
  <div class="section-padding">
    <div class="container-custom">
      <div class="flex items-center justify-between mb-6">
        <h2 class="text-2xl font-bold">Videos</h2>
        <router-link to="/resources" class="text-primary-600 hover:text-primary-700">Resources →</router-link>
      </div>

      <!-- Search and filters -->
      <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-4 mb-6">
        <div class="flex items-center gap-3">
          <div class="flex-1">
            <input class="form-input" placeholder="Search videos..." v-model="query" />
          </div>
          <button class="pill pill-primary" @click="applySearch">Search</button>
        </div>
        <div class="mt-3 flex flex-wrap gap-2">
          <button v-for="chip in chips" :key="chip" class="px-3 py-1 rounded-full text-sm bg-gray-100 hover:bg-gray-200" @click="setChip(chip)">{{ chip }}</button>
        </div>
      </div>

      <!-- Video grid (YouTube-like) -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        <article v-for="video in filteredVideos" :key="video.id" class="group">
          <div class="relative bg-gray-200 rounded-xl overflow-hidden aspect-video">
            <img :src="video.thumbnail" :alt="video.title" class="w-full h-full object-cover" loading="lazy" @error="useThumbPlaceholder($event)" />
            <span class="absolute bottom-2 right-2 text-xs font-bold bg-black/80 text-white px-1.5 py-0.5 rounded">{{ video.duration }}</span>
          </div>
          <div class="mt-3 flex gap-3">
            <img :src="video.channelAvatar" :alt="video.channel" class="h-9 w-9 rounded-full object-cover" loading="lazy" @error="useAvatarPlaceholder($event)" />
            <div class="min-w-0">
              <h3 class="text-sm font-semibold text-gray-900 leading-5 line-clamp-2 group-hover:text-primary-600">{{ video.title }}</h3>
              <p class="text-xs text-gray-600 mt-1">{{ video.channel }}</p>
              <p class="text-xs text-gray-500">{{ video.views }} • {{ video.published }}</p>
            </div>
          </div>
        </article>
      </div>
    </div>
  </div>
  
</template>

<script setup>
import { ref, computed } from 'vue'

const query = ref('')
const chips = ['All', 'Education', 'Safety', 'Support', 'Recency', 'Popular']
const activeChip = ref('All')

const videos = ref([
  {
    id: 1,
    title: 'Understanding Child Rights',
    channel: 'Sauti Uganda',
    channelAvatar: 'https://i.pravatar.cc/48?img=12',
    views: '12K views',
    published: '2 weeks ago',
    duration: '12:45',
    category: 'Education',
    thumbnail: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=1200&auto=format&fit=crop'
  },
  {
    id: 2,
    title: 'Safety Tips for Children',
    channel: 'Sauti Uganda',
    channelAvatar: 'https://i.pravatar.cc/48?img=32',
    views: '15K views',
    published: '1 month ago',
    duration: '8:22',
    category: 'Safety',
    thumbnail: 'https://images.unsplash.com/photo-1512428559087-560fa5ceab42?q=80&w=1200&auto=format&fit=crop'
  },
  {
    id: 3,
    title: 'How to Report Abuse',
    channel: 'Sauti Uganda',
    channelAvatar: 'https://i.pravatar.cc/48?img=15',
    views: '8K views',
    published: '1 month ago',
    duration: '15:03',
    category: 'Support',
    thumbnail: 'https://images.unsplash.com/photo-1499355942262-97b58a6195b4?q=80&w=1200&auto=format&fit=crop'
  },
  {
    id: 4,
    title: 'Educational Resources for Parents',
    channel: 'Sauti Uganda',
    channelAvatar: 'https://i.pravatar.cc/48?img=19',
    views: '7K views',
    published: '3 months ago',
    duration: '11:30',
    category: 'Education',
    thumbnail: 'https://images.unsplash.com/photo-1511632765486-a01980e01a18?q=80&w=1200&auto=format&fit=crop'
  }
])

const filteredVideos = computed(() => {
  const q = query.value.trim().toLowerCase()
  return videos.value.filter(v => {
    const matchQuery = !q || v.title.toLowerCase().includes(q) || v.channel.toLowerCase().includes(q)
    const matchChip = activeChip.value === 'All' || v.category === activeChip.value || (activeChip.value === 'Popular' && v.views.includes('K'))
    return matchQuery && matchChip
  })
})

function setChip(chip) {
  activeChip.value = chip
}

function applySearch() {}

function useThumbPlaceholder(e) {
  e.target.src = 'https://picsum.photos/640/360?blur=2'
}

function useAvatarPlaceholder(e) {
  e.target.src = 'https://i.pravatar.cc/48'
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
.aspect-video > video,
.aspect-video > div {
  position: absolute;
  inset: 0;
}
</style>

