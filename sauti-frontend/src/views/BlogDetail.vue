<template>
  <div>
    <Loader v-if="loading" :fullScreen="true" message="Loading article..." />
    
    <article v-else-if="post" class="section-padding bg-white">
      <div class="container-custom max-w-4xl">
        <h1 class="mb-3 text-4xl md:text-5xl font-extrabold text-gray-900">{{ post.title }}</h1>
        <p class="text-sm text-secondary-600 mb-6">
          <span v-if="post.author">By {{ post.author.username }}</span>
          <span v-if="post.author"> | </span>
          Published on {{ formatDate(post.published_at) }}
        </p>
        <img v-if="post.featured_image" :src="post.featured_image" :alt="post.title" class="w-full h-96 object-cover rounded-xl mb-8" />
        <div class="prose prose-lg max-w-none" v-html="formattedContent"></div>

        <!-- Share icons minimal -->
        <div class="mt-8 border-t pt-4 text-right text-gray-400 text-sm">
          <span class="inline-flex items-center gap-4">
            <span class="sr-only">Share:</span>
            <span>●</span><span>●</span><span>●</span>
          </span>
        </div>
      </div>

      <!-- Related Posts -->
      <div class="container-custom max-w-5xl mt-16">
        <h2 class="text-2xl font-bold mb-6 text-center">Related Posts</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <router-link v-for="rp in related" :key="rp.id" :to="`/blog/${rp.slug}`" class="group">
            <div class="h-44 bg-gray-200 rounded-2xl overflow-hidden">
              <img :src="rp.featured_image" :alt="rp.title" class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform" @error="setPlaceholder($event, 700, 400)" />
            </div>
            <h3 class="mt-3 font-semibold group-hover:text-primary-600">{{ rp.title }}</h3>
            <p class="text-xs text-gray-600">{{ rp.excerpt }}</p>
          </router-link>
        </div>
      </div>
    </article>

    <div v-else class="section-padding text-center">
      <p class="text-gray-600">Article not found</p>
      <router-link to="/blog" class="pill pill-primary mt-4 inline-block">← Back to Blog</router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useBlogStore } from '@/store/blog'
import Loader from '@/components/common/Loader.vue'

const route = useRoute()
const blogStore = useBlogStore()
const post = ref(null)
const loading = ref(true)
const related = ref([
  {
    id: 101,
    slug: 'supporting-children-through-trauma',
    title: 'Supporting Children Through Trauma',
    excerpt: 'Learn how to help children cope with traumatic experiences.',
    featured_image: 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?q=80&w=1200&auto=format&fit=crop'
  },
  {
    id: 102,
    slug: 'building-resilience-in-young-minds',
    title: 'Building Resilience in Young Minds',
    excerpt: 'Strategies for fostering resilience and emotional strength in children.',
    featured_image: 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?q=80&w=1200&auto=format&fit=crop'
  },
])

onMounted(async () => {
  try {
    post.value = await blogStore.fetchPost(route.params.slug)
  } catch (error) {
    console.error('Failed to load post:', error)
  } finally {
    // Fallback to mock if nothing loaded
    if (!post.value) {
      const fallback = mockPosts().find(p => p.slug === route.params.slug)
      if (fallback) post.value = fallback
    }
    loading.value = false
  }
})

function formatDate(dateString) {
  return new Date(dateString).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
}

function setPlaceholder(e, w = 1200, h = 600) {
  e.target.src = `https://picsum.photos/${w}/${h}`
}

// Ensure content renders as paragraphs if raw text is provided
const formattedContent = computed(() => {
  if (!post.value?.content) return ''
  const raw = String(post.value.content)
  const hasTags = /<[^>]+>/.test(raw)
  if (!hasTags) {
    const parts = raw.split(/\n\n+/).map(p => p.trim()).filter(Boolean)
    return parts.map(p => `<p>${p}</p>`).join('')
  }
  // Convert headings and list items to paragraphs
  let html = raw
  html = html.replace(/<h[1-6][^>]*>([\s\S]*?)<\/h[1-6]>/gi, (_m, text) => `<p>${text}</p>`)
  html = html.replace(/<li[^>]*>([\s\S]*?)<\/li>/gi, (_m, text) => `<p>${text}</p>`)
  html = html.replace(/<\/?ul[^>]*>/gi, '')
  html = html.replace(/<\/?ol[^>]*>/gi, '')
  return html
})

function mockPosts() {
  return [
    {
      id: 1,
      slug: 'empowering-youth-voices',
      title: 'Empowering Youth Voices: A New Initiative',
      content: `
        <p>Sauti Uganda is launching a new initiative focused on <strong>youth empowerment</strong>. Our goal is to give young people the tools and confidence they need to advocate for their rights and support peers in their communities.</p>
        <h2>What’s Included</h2>
        <ul>
          <li>Community outreach and awareness sessions</li>
          <li>Training workshops on online safety and child protection</li>
          <li>Mentorship with experienced counsellors</li>
        </ul>
        <p>These activities are designed in collaboration with district partners and school leaders to ensure maximum impact and sustainability.</p>
        <h2>How You Can Help</h2>
        <p>You can support the program by sharing this message, volunteering as a mentor, or contributing resources. Every action brings us closer to a safer environment for children.</p>
      `,
      excerpt: 'Learn about our new youth empowerment program.',
      featured_image: 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?q=80&w=1200&auto=format&fit=crop',
      published_at: '2024-07-15',
      author: { username: 'Dr. Aisha Nakato' },
      category: { name: 'Child Protection', slug: 'child-protection' },
    },
    {
      id: 4,
      slug: 'success-story-victory',
      title: 'Success Story: From Vulnerability to Victory',
      content: `
        <p>This is the story of a young survivor who reached out through the helpline and received timely support from our team and district partners.</p>
        <h2>The Turning Point</h2>
        <p>After the initial call, our counsellors coordinated with child protection services to ensure immediate safety. Follow‑up support included medical care, psychosocial counselling, and school reintegration.</p>
        <blockquote>“I felt heard and protected. Thank you for helping me find my voice.”</blockquote>
        <p>Today, the child is thriving in school and actively participates in peer support clubs advocating for children’s rights.</p>
      `,
      excerpt: "A child's journey to safety and success.",
      featured_image: 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?q=80&w=1200&auto=format&fit=crop',
      published_at: '2024-07-05',
      author: { username: 'John' },
      category: { name: 'Migrant Workers', slug: 'migrants' },
    },
  ]
}
</script>
