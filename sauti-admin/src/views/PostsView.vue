<template>
  <div class="p-6">
    <!-- Page Header -->
    <PageHeader title="Blog Posts" description="Create, edit, and manage blog posts and articles for the Sauti platform"
      action-label="Create Blog Post" :action-icon="PlusIcon" @action="$router.push('/posts/create')" />

    <!-- Mini Dashboard -->
    <StatsGrid>
      <StatCard label="Total Posts" :value="stats.total" subtitle="All blog posts" :icon="DocumentTextIcon"
        color="blue" />
      <StatCard label="Published" :value="stats.published" subtitle="Live on website" :icon="CheckCircleIcon"
        color="green" />
      <StatCard label="Drafts" :value="stats.draft" subtitle="Work in progress" :icon="ClockIcon" color="orange" />
      <StatCard label="Total Views" :value="formatNumber(stats.totalViews)" subtitle="All time views" :icon="EyeIcon"
        color="purple" />
    </StatsGrid>

    <!-- Tabs and Filters -->
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 mb-6 overflow-hidden">
      <div class="border-b border-gray-200 bg-white">
        <nav class="flex -mb-px px-6" aria-label="Tabs">
          <button v-for="tab in postTabs" :key="tab.id" @click="activeStatusTab = tab.id"
            class="whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm mr-8 transition-colors duration-200"
            :class="[
              activeStatusTab === tab.id
                ? 'border-blue-500 text-blue-600'
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
            ]">
            <div class="flex items-center">
              <component :is="tab.icon" class="h-5 w-5 mr-2" />
              {{ tab.name }}
              <span v-if="tab.count !== undefined" class="ml-2 py-0.5 px-2 rounded-full text-xs"
                :class="activeStatusTab === tab.id ? 'bg-blue-100 text-blue-600' : 'bg-gray-100 text-gray-600'">
                {{ tab.count }}
              </span>
            </div>
          </button>
        </nav>
      </div>

      <div class="p-4 bg-gray-50 flex flex-col md:flex-row gap-4">
        <div class="flex-1 relative">
          <MagnifyingGlassIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
          <input v-model="searchQuery" type="text" placeholder="Search by title, excerpt or content..."
            class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white shadow-sm transition-all" />
        </div>

        <div class="flex flex-wrap gap-2">
          <select v-model="categoryFilter"
            class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white min-w-[160px]">
            <option value="">All Categories</option>
            <option v-for="category in (Array.isArray(categories) ? categories : [])" :key="category.id"
              :value="category.name">
              {{ category.name }}
            </option>
          </select>

          <select v-model="authorFilter"
            class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white min-w-[160px]">
            <option value="">All Authors</option>
            <option v-for="author in authors" :key="author" :value="author">
              {{ author }}
            </option>
          </select>

          <select v-if="activeStatusTab === 'all'" v-model="statusFilter"
            class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white">
            <option value="">Any Status</option>
            <option value="PUBLISHED">Published</option>
            <option value="DRAFT">Draft</option>
            <option value="ARCHIVED">Archived</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="text-center py-12">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
      <p class="mt-2 text-sm text-gray-500">Loading posts...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="text-center py-12">
      <div class="text-red-600 mb-4">
        <DocumentTextIcon class="h-12 w-12 mx-auto mb-2" />
        <h3 class="text-lg font-medium">Failed to load posts</h3>
        <p class="text-sm text-gray-500">{{ error }}</p>
      </div>
      <button @click="fetchPosts" class="btn-primary">
        Try Again
      </button>
    </div>

    <!-- Posts Table -->
    <div v-else class="bg-white rounded-lg shadow-sm overflow-hidden">
      <div class="overflow-x-auto">
        <table class="min-w-full">
          <thead class="table-header">
            <tr>
              <th class="table-cell">Post</th>
              <th class="table-cell">Author</th>
              <th class="table-cell">Category</th>
              <th class="table-cell">Status</th>
              <th class="table-cell">Views</th>
              <th class="table-cell">Date</th>
              <th class="table-cell">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white">
            <tr v-for="post in filteredPosts" :key="post.id" class="table-row hover:bg-gray-50">
              <td class="px-6 py-4">
                <div class="flex items-center">
                  <div class="flex-shrink-0 h-12 w-12">
                    <div v-if="post.featured_image" class="h-12 w-12 rounded-lg overflow-hidden">
                      <img :src="post.featured_image" :alt="post.title" class="h-full w-full object-cover">
                    </div>
                    <div v-else class="h-12 w-12 bg-gray-100 rounded-lg flex items-center justify-center">
                      <DocumentTextIcon class="h-6 w-6 text-gray-400" />
                    </div>
                  </div>
                  <div class="ml-4">
                    <div class="text-sm font-medium text-gray-900 line-clamp-2">
                      {{ post.title }}
                    </div>
                    <div class="text-sm text-gray-500 line-clamp-1">
                      {{ post.excerpt || post.content?.substring(0, 100) + '...' }}
                    </div>
                  </div>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ post.author_name || 'Unknown' }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ post.category?.name || 'Uncategorized' }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span class="inline-flex px-2 py-1 text-xs font-semibold rounded-full" :class="{
                  'bg-green-100 text-green-800': post.status === 'PUBLISHED',
                  'bg-yellow-100 text-yellow-800': post.status === 'DRAFT',
                  'bg-gray-100 text-gray-800': post.status === 'ARCHIVED'
                }">
                  {{ post.status }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ formatNumber(post.views_count || 0) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ formatDate(post.published_at || post.created_at) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <div class="flex items-center justify-end space-x-2">
                  <button @click="previewPost(post)" class="text-blue-600 hover:text-blue-900" title="Preview">
                    <EyeIcon class="h-4 w-4" />
                  </button>
                  <router-link :to="`/posts/${post.slug || post.id}/edit`"
                    class="text-primary-600 hover:text-primary-900" title="Edit">
                    <PencilIcon class="h-4 w-4" />
                  </router-link>
                  <button @click="duplicatePost(post)" class="text-green-600 hover:text-green-900" title="Duplicate">
                    <DocumentDuplicateIcon class="h-4 w-4" />
                  </button>
                  <button @click="deletePost(post)" class="text-red-600 hover:text-red-900" title="Delete">
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
          {{ searchQuery ? 'Try adjusting your search criteria.' : 'Get started by creating your first blog post.' }}
        </p>
        <div class="mt-6" v-if="!searchQuery">
          <router-link to="/posts/create" class="btn-primary">
            <PlusIcon class="h-4 w-4 mr-2" />
            Create Blog Post
          </router-link>
        </div>
      </div>
    </div>

    <!-- Blog Preview Modal -->
    <BlogPreviewModal v-if="selectedPost" :isOpen="isPreviewOpen" :slug="selectedPost.slug" :postId="selectedPost.id"
      @close="closePreview" />
  </div>
</template>

<script setup>
  import { ref, computed, onMounted, watch } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import { useToast } from 'vue-toastification'
  import { usePostsStore } from '@/stores/posts'
  import { PageHeader, StatsGrid, StatCard } from '@/components/admin'
  import BlogPreviewModal from '@/components/previews/BlogPreviewModal.vue'
  import {
    PlusIcon,
    DocumentTextIcon,
    CheckCircleIcon,
    ClockIcon,
    EyeIcon,
    MagnifyingGlassIcon,
    PencilIcon,
    TrashIcon,
    DocumentDuplicateIcon,
    PencilSquareIcon
  } from '@heroicons/vue/24/outline'

  const toast = useToast()
  const route = useRoute()
  const postsStore = usePostsStore()

  // Reactive data
  const searchQuery = ref('')
  const statusFilter = ref('')
  const categoryFilter = ref('')
  const authorFilter = ref('')
  const activeStatusTab = ref(route.query.tab || 'all')
  const router = useRouter()

  watch(activeStatusTab, (newTab) => {
    router.replace({
      query: { ...route.query, tab: newTab }
    })
  })

  // Use store data
  const posts = computed(() => postsStore.posts)
  const loading = computed(() => postsStore.loading)
  const error = computed(() => postsStore.error)
  const categories = computed(() => postsStore.categories)
  const authors = ref([])

  // Computed properties
  const stats = computed(() => {
    const total = posts.value.length
    const published = posts.value.filter(p => p.status === 'PUBLISHED').length
    const draft = posts.value.filter(p => p.status === 'DRAFT').length
    const totalViews = posts.value.reduce((sum, p) => sum + (p.views_count || 0), 0)

    return {
      total,
      published,
      draft,
      totalViews
    }
  })

  const postTabs = computed(() => [
    { id: 'all', name: 'All Posts', icon: DocumentTextIcon, count: stats.value.total },
    { id: 'PUBLISHED', name: 'Published', icon: CheckCircleIcon, count: stats.value.published },
    { id: 'DRAFT', name: 'Drafts', icon: ClockIcon, count: stats.value.draft }
  ])

  const filteredPosts = computed(() => {
    let filtered = posts.value

    // Status Tab Filter
    if (activeStatusTab.value !== 'all') {
      filtered = filtered.filter(post => post.status === activeStatusTab.value)
    }

    // Filter by search query
    if (searchQuery.value) {
      const query = searchQuery.value.toLowerCase()
      filtered = filtered.filter(post =>
        post.title.toLowerCase().includes(query) ||
        (post.excerpt && post.excerpt.toLowerCase().includes(query)) ||
        (post.content && post.content.toLowerCase().includes(query))
      )
    }

    // Filter by status (secondary filter if on 'all' tab)
    if (activeStatusTab.value === 'all' && statusFilter.value) {
      filtered = filtered.filter(post => post.status === statusFilter.value)
    }

    // Filter by category
    if (categoryFilter.value) {
      filtered = filtered.filter(post => post.category?.name === categoryFilter.value)
    }

    // Filter by author
    if (authorFilter.value) {
      filtered = filtered.filter(post => post.author_name === authorFilter.value)
    }

    return filtered
  })

  // Methods
  const formatNumber = (num) => {
    if (num >= 1000000) {
      return (num / 1000000).toFixed(1) + 'M'
    } else if (num >= 1000) {
      return (num / 1000).toFixed(1) + 'K'
    }
    return num.toString()
  }

  const formatDate = (date) => {
    if (!date) return 'Recently'
    try {
      return new Date(date).toLocaleDateString()
    } catch (error) {
      return 'Recently'
    }
  }

  const isPreviewOpen = ref(false)
  const selectedPost = ref(null)

  const previewPost = (post) => {
    selectedPost.value = post
    isPreviewOpen.value = true
  }

  const closePreview = () => {
    isPreviewOpen.value = false
    selectedPost.value = null
  }

  const duplicatePost = async (post) => {
    try {
      const duplicateData = {
        ...post,
        title: `${post.title} (Copy)`,
        slug: `${post.slug}-copy-${Date.now()}`,
        status: 'DRAFT'
      }

      await postsStore.createPost(duplicateData)
      toast.success(`"${post.title}" duplicated successfully`)
    } catch (err) {
      console.error('Duplicate error:', err)
      toast.error('Failed to duplicate post')
    }
  }

  const deletePost = async (post) => {
    if (!confirm(`Are you sure you want to delete "${post.title}"?`)) {
      return
    }

    try {
      await postsStore.deletePost(post.slug || post.id)
      toast.success('Post deleted successfully')
    } catch (err) {
      console.error('Delete error:', err)
      toast.error('Failed to delete post')
    }
  }

  const fetchPosts = async () => {
    try {
      await postsStore.fetchPosts()
      await postsStore.fetchCategories()

      // Extract unique authors
      const uniqueAuthors = [...new Set(posts.value.map(p => p.author_name).filter(Boolean))]
      authors.value = uniqueAuthors
    } catch (err) {
      console.error('Failed to fetch posts:', err)
      toast.error('Failed to load posts')
    }
  }

  // Watch for route changes to refresh data
  watch(() => route.path, (newPath) => {
    if (newPath === '/posts') {
      fetchPosts()
    }
  })

  // Lifecycle
  onMounted(() => {
    fetchPosts()
  })
</script>