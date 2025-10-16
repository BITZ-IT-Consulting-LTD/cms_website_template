<template>
  <div class="p-6">
    <!-- Header -->
    <div class="flex items-center justify-between mb-6">
      <div>
        <h1 class="text-2xl font-bold text-gray-900">Content Management</h1>
        <p class="text-gray-600 mt-1">Manage blog posts and articles for the Sauti platform</p>
      </div>
      
      <router-link
        to="/posts/create"
        class="btn-primary flex items-center"
      >
        <PlusIcon class="h-4 w-4 mr-2" />
        Create New Post
      </router-link>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
      <div class="card p-4">
        <div class="flex items-center">
          <div class="p-2 bg-blue-100 rounded-lg">
            <DocumentTextIcon class="h-6 w-6 text-blue-600" />
          </div>
          <div class="ml-3">
            <p class="text-sm font-medium text-gray-500">Total Posts</p>
            <p class="text-xl font-semibold text-gray-900">{{ stats.total }}</p>
          </div>
        </div>
      </div>
      
      <div class="card p-4">
        <div class="flex items-center">
          <div class="p-2 bg-green-100 rounded-lg">
            <CheckCircleIcon class="h-6 w-6 text-green-600" />
          </div>
          <div class="ml-3">
            <p class="text-sm font-medium text-gray-500">Published</p>
            <p class="text-xl font-semibold text-gray-900">{{ stats.published }}</p>
          </div>
        </div>
      </div>
      
      <div class="card p-4">
        <div class="flex items-center">
          <div class="p-2 bg-yellow-100 rounded-lg">
            <ClockIcon class="h-6 w-6 text-yellow-600" />
          </div>
          <div class="ml-3">
            <p class="text-sm font-medium text-gray-500">Draft</p>
            <p class="text-xl font-semibold text-gray-900">{{ stats.draft }}</p>
          </div>
        </div>
      </div>
      
      <div class="card p-4">
        <div class="flex items-center">
          <div class="p-2 bg-primary-100 rounded-lg">
            <EyeIcon class="h-6 w-6 text-primary-600" />
          </div>
          <div class="ml-3">
            <p class="text-sm font-medium text-gray-500">Total Views</p>
            <p class="text-xl font-semibold text-gray-900">{{ formatNumber(stats.views) }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Filters and Search -->
    <div class="card p-4 mb-6">
      <div class="flex flex-col sm:flex-row gap-4">
        <!-- Search -->
        <div class="flex-1">
          <div class="relative">
            <MagnifyingGlassIcon class="h-5 w-5 text-gray-400 absolute left-3 top-1/2 transform -translate-y-1/2" />
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search posts..."
              class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
        </div>
        
        <!-- Status Filter -->
        <select
          v-model="statusFilter"
          class="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
        >
          <option value="">All Status</option>
          <option value="published">Published</option>
          <option value="draft">Draft</option>
          <option value="archived">Archived</option>
        </select>
        
        <!-- Category Filter -->
        <select
          v-model="categoryFilter"
          class="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
        >
          <option value="">All Categories</option>
          <option v-for="category in categories" :key="category" :value="category">
            {{ category }}
          </option>
        </select>
        
        <!-- Author Filter -->
        <select
          v-model="authorFilter"
          class="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
        >
          <option value="">All Authors</option>
          <option v-for="author in authors" :key="author" :value="author">
            {{ author }}
          </option>
        </select>
      </div>
    </div>

    <!-- Posts Table -->
    <div class="card overflow-hidden">
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Title
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Author
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Category
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Status
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Views
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Published
              </th>
              <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                Actions
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="post in filteredPosts" :key="post.id" class="hover:bg-gray-50">
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="flex items-center">
                  <div class="h-12 w-12 bg-gray-200 rounded-lg overflow-hidden mr-4 flex-shrink-0">
                    <img
                      v-if="post.featuredImage"
                      :src="post.featuredImage"
                      :alt="post.title"
                      class="h-full w-full object-cover"
                    />
                    <div v-else class="h-full w-full flex items-center justify-center">
                      <DocumentTextIcon class="h-6 w-6 text-gray-400" />
                    </div>
                  </div>
                  <div class="min-w-0">
                    <div class="text-sm font-medium text-gray-900 truncate">{{ post.title }}</div>
                    <div class="text-sm text-gray-500 truncate max-w-xs">{{ post.excerpt }}</div>
                  </div>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="flex items-center">
                  <div class="h-8 w-8 bg-gray-300 rounded-full flex items-center justify-center mr-2">
                    <span class="text-xs font-medium text-gray-600">
                      {{ post.author.split(' ').map(n => n[0]).join('').toUpperCase() }}
                    </span>
                  </div>
                  <span class="text-sm text-gray-900">{{ post.author }}</span>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ post.category }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span
                  class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
                  :class="{
                    'bg-green-100 text-green-800': post.status === 'published',
                    'bg-yellow-100 text-yellow-800': post.status === 'draft',
                    'bg-gray-100 text-gray-800': post.status === 'archived'
                  }"
                >
                  {{ post.status }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ formatNumber(post.views) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ formatDate(post.publishedAt || post.createdAt) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <div class="flex items-center justify-end space-x-2">
                  <button
                    @click="previewPost(post)"
                    class="text-blue-600 hover:text-blue-900"
                  >
                    <EyeIcon class="h-4 w-4" />
                  </button>
                  <router-link
                    :to="`/posts/${post.slug || post.id}/edit`"
                    class="text-primary-600 hover:text-primary-900"
                  >
                    <PencilIcon class="h-4 w-4" />
                  </router-link>
                  <button
                    @click="duplicatePost(post)"
                    class="text-green-600 hover:text-green-900"
                  >
                    <DocumentDuplicateIcon class="h-4 w-4" />
                  </button>
                  <button
                    @click="deletePost(post)"
                    class="text-red-600 hover:text-red-900"
                  >
                    <TrashIcon class="h-4 w-4" />
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <!-- Empty State -->
      <div v-if="filteredPosts.length === 0" class="text-center py-12">
        <DocumentTextIcon class="mx-auto h-12 w-12 text-gray-400" />
        <h3 class="mt-2 text-sm font-medium text-gray-900">No posts found</h3>
        <p class="mt-1 text-sm text-gray-500">
          {{ searchQuery ? 'Try adjusting your search criteria.' : 'Get started by creating your first post.' }}
        </p>
        <div class="mt-6" v-if="!searchQuery">
          <router-link to="/posts/create" class="btn-primary">
            <PlusIcon class="h-4 w-4 mr-2" />
            Create New Post
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useToast } from 'vue-toastification'
import {
  PlusIcon,
  DocumentTextIcon,
  CheckCircleIcon,
  ClockIcon,
  EyeIcon,
  MagnifyingGlassIcon,
  PencilIcon,
  TrashIcon,
  DocumentDuplicateIcon
} from '@heroicons/vue/24/outline'

const toast = useToast()

// Reactive data
const searchQuery = ref('')
const statusFilter = ref('')
const categoryFilter = ref('')
const authorFilter = ref('')

// Mock data
const posts = ref([
  {
    id: 1,
    title: 'Understanding Child Rights in Uganda',
    slug: 'understanding-child-rights-uganda',
    excerpt: 'A comprehensive guide to child rights and protection laws in Uganda, explaining how Sauti supports these fundamental principles.',
    featuredImage: null,
    author: 'Sarah Nakamura',
    category: 'Child Rights',
    status: 'published',
    views: 2847,
    createdAt: '2024-01-15T10:30:00Z',
    publishedAt: '2024-01-15T14:00:00Z'
  },
  {
    id: 2,
    title: 'The Impact of Community Support on Child Welfare',
    slug: 'impact-community-support-child-welfare',
    excerpt: 'How community involvement and support systems contribute to better outcomes for children in need of protection.',
    featuredImage: null,
    author: 'David Mugisha',
    category: 'Community Impact',
    status: 'published',
    views: 1923,
    createdAt: '2024-01-12T09:15:00Z',
    publishedAt: '2024-01-12T12:00:00Z'
  },
  {
    id: 3,
    title: 'Success Stories: How Sauti Changed Lives',
    slug: 'success-stories-sauti-changed-lives',
    excerpt: 'Real stories from children and families who found help and hope through the Sauti helpline services.',
    featuredImage: null,
    author: 'Grace Achieng',
    category: 'Success Stories',
    status: 'draft',
    views: 0,
    createdAt: '2024-01-10T16:45:00Z',
    publishedAt: null
  },
  {
    id: 4,
    title: 'Mental Health Resources for Young People',
    slug: 'mental-health-resources-young-people',
    excerpt: 'Essential mental health resources and support services available to young people through various channels.',
    featuredImage: null,
    author: 'Dr. James Okello',
    category: 'Mental Health',
    status: 'published',
    views: 3156,
    createdAt: '2024-01-08T11:20:00Z',
    publishedAt: '2024-01-08T15:30:00Z'
  },
  {
    id: 5,
    title: 'Digital Safety for Children and Teens',
    slug: 'digital-safety-children-teens',
    excerpt: 'Guidelines and tips for staying safe online, including how to report cyberbullying and inappropriate content.',
    featuredImage: null,
    author: 'Mary Kintu',
    category: 'Digital Safety',
    status: 'published',
    views: 1678,
    createdAt: '2024-01-05T08:00:00Z',
    publishedAt: '2024-01-05T10:00:00Z'
  },
  {
    id: 6,
    title: 'Building Resilience in Children',
    slug: 'building-resilience-children',
    excerpt: 'Strategies and approaches for helping children develop emotional resilience and coping skills.',
    featuredImage: null,
    author: 'Peter Ssemakula',
    category: 'Child Development',
    status: 'archived',
    views: 892,
    createdAt: '2023-12-28T14:15:00Z',
    publishedAt: '2023-12-30T09:00:00Z'
  }
])

const categories = ref([
  'Child Rights',
  'Community Impact',
  'Success Stories',
  'Mental Health',
  'Digital Safety',
  'Child Development',
  'Education',
  'Healthcare'
])

const authors = ref([
  'Sarah Nakamura',
  'David Mugisha',
  'Grace Achieng',
  'Dr. James Okello',
  'Mary Kintu',
  'Peter Ssemakula'
])

// Computed properties
const stats = computed(() => {
  const total = posts.value.length
  const published = posts.value.filter(p => p.status === 'published').length
  const draft = posts.value.filter(p => p.status === 'draft').length
  const views = posts.value.reduce((sum, p) => sum + p.views, 0)
  
  return { total, published, draft, views }
})

const filteredPosts = computed(() => {
  let filtered = posts.value

  // Search filter
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(post =>
      post.title.toLowerCase().includes(query) ||
      post.excerpt.toLowerCase().includes(query) ||
      post.author.toLowerCase().includes(query)
    )
  }

  // Status filter
  if (statusFilter.value) {
    filtered = filtered.filter(post => post.status === statusFilter.value)
  }

  // Category filter
  if (categoryFilter.value) {
    filtered = filtered.filter(post => post.category === categoryFilter.value)
  }

  // Author filter
  if (authorFilter.value) {
    filtered = filtered.filter(post => post.author === authorFilter.value)
  }

  return filtered.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt))
})

// Methods
const formatNumber = (num) => {
  return new Intl.NumberFormat().format(num)
}

const formatDate = (dateString) => {
  if (!dateString) return 'Not published'
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}

const previewPost = (post) => {
  toast.info(`Preview for "${post.title}" - Feature coming soon`)
}

const duplicatePost = (post) => {
  const newPost = {
    ...post,
    id: Math.max(...posts.value.map(p => p.id)) + 1,
    title: `${post.title} (Copy)`,
    status: 'draft',
    views: 0,
    createdAt: new Date().toISOString(),
    publishedAt: null
  }
  
  posts.value.unshift(newPost)
  toast.success('Post duplicated successfully')
}

const deletePost = (post) => {
  if (confirm(`Are you sure you want to delete "${post.title}"?`)) {
    const index = posts.value.findIndex(p => p.id === post.id)
    if (index > -1) {
      posts.value.splice(index, 1)
      toast.success('Post deleted successfully')
    }
  }
}

// Lifecycle
onMounted(() => {
  console.log('Posts page loaded')
})
</script>
