<template>
  <div>
    <Loader v-if="loading" :fullScreen="true" message="Loading article..." />
    
    <article v-else-if="post" class="section-padding">
      <div class="container-custom max-w-4xl">
        <img v-if="post.featured_image" :src="post.featured_image" :alt="post.title" class="w-full h-96 object-cover rounded-xl mb-8" />
        <h1 class="mb-4">{{ post.title }}</h1>
        <div class="flex items-center text-gray-600 mb-8 space-x-4">
          <span>{{ formatDate(post.published_at) }}</span>
          <span>·</span>
          <span v-if="post.author">By {{ post.author.username }}</span>
          <span v-if="post.category" class="badge-blue">{{ post.category.name }}</span>
        </div>
        <div class="prose prose-lg max-w-none" v-html="post.content"></div>
      </div>
    </article>

    <div v-else class="section-padding text-center">
      <p class="text-gray-600">Article not found</p>
      <router-link to="/blog" class="btn-primary mt-4">← Back to Blog</router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useBlogStore } from '@/store/blog'
import Loader from '@/components/common/Loader.vue'

const route = useRoute()
const blogStore = useBlogStore()
const post = ref(null)
const loading = ref(true)

onMounted(async () => {
  try {
    post.value = await blogStore.fetchPost(route.params.slug)
  } catch (error) {
    console.error('Failed to load post:', error)
  } finally {
    loading.value = false
  }
})

function formatDate(dateString) {
  return new Date(dateString).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
}
</script>
