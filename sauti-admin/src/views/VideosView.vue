<template>
  <div class="p-6">
    <!-- Page Header -->
    <PageHeader title="Videos" description="Manage video content for the Sauti platform" action-label="Add New Video"
      :action-icon="PlusIcon" @action="$router.push('/videos/create')" />

    <!-- Mini Dashboard -->
    <StatsGrid>
      <StatCard label="Total Videos" :value="stats.total" :icon="VideoCameraIcon" color="blue" />
      <StatCard label="Published" :value="stats.published" :icon="CheckCircleIcon" color="green" />
      <StatCard label="Drafts" :value="stats.draft" :icon="ClockIcon" color="orange" />
      <StatCard label="Total Views" :value="formatNumber(stats.totalViews)" :icon="EyeIcon" color="purple" />
    </StatsGrid>

    <!-- Filters -->
    <FilterBar v-model="filters" search-placeholder="Search videos..." :status-options="statusOptions"
      status-label="All Status" :custom-options="categoryOptions" custom-label="All Categories" />

    <!-- Loading State -->
    <LoadingState v-if="loading" message="Loading videos..." />

    <!-- Error State -->
    <div v-else-if="error" class="text-center py-12">
      <div class="text-red-600 mb-4">
        <VideoCameraIcon class="h-12 w-12 mx-auto mb-2" />
        <h3 class="text-lg font-medium">Failed to load videos</h3>
        <p class="text-sm text-gray-500">{{ error }}</p>
      </div>
      <button @click="fetchVideos" class="btn-primary">
        Try Again
      </button>
    </div>

    <!-- Videos Table -->
    <div v-else class="bg-white rounded-lg shadow-sm overflow-hidden">
      <div class="overflow-x-auto">
        <table class="min-w-full">
          <thead class="table-header">
            <tr>
              <th class="table-cell">Video</th>
              <th class="table-cell">Category</th>
              <th class="table-cell">Status</th>
              <th class="table-cell">Views</th>
              <th class="table-cell">Duration</th>
              <th class="table-cell">Date</th>
              <th class="table-cell">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white">
            <tr v-for="video in filteredVideos" :key="video.id" class="table-row hover:bg-gray-50">
              <td class="px-6 py-4">
                <div class="flex items-center">
                  <div class="flex-shrink-0 h-12 w-12">
                    <div v-if="video.thumbnail" class="h-12 w-12 rounded-lg overflow-hidden">
                      <img :src="video.thumbnail" :alt="video.title" class="h-full w-full object-cover">
                    </div>
                    <div v-else-if="video.youtube_thumbnail_url" class="h-12 w-12 rounded-lg overflow-hidden">
                      <img :src="video.youtube_thumbnail_url" :alt="video.title" class="h-full w-full object-cover">
                    </div>
                    <div v-else class="h-12 w-12 bg-gray-100 rounded-lg flex items-center justify-center">
                      <VideoCameraIcon class="h-6 w-6 text-gray-400" />
                    </div>
                  </div>
                  <div class="ml-4">
                    <div class="text-sm font-medium text-gray-900 line-clamp-2">
                      {{ video.title }}
                    </div>
                    <div class="text-sm text-gray-500 line-clamp-1">
                      {{ video.description || 'No description' }}
                    </div>
                  </div>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ video.category?.name || 'Uncategorized' }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span class="inline-flex px-2 py-1 text-xs font-semibold rounded-full" :class="{
                  'bg-green-100 text-green-800': video.status?.toUpperCase() === 'PUBLISHED',
                  'bg-yellow-100 text-yellow-800': video.status?.toUpperCase() === 'DRAFT'
                }">
                  {{ video.status?.toUpperCase() || 'UNKNOWN' }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ formatNumber(video.views_count || 0) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ video.duration || 'N/A' }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ formatDate(video.published_at || video.created_at) }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <div class="flex items-center justify-end space-x-2">
                  <button @click="previewVideo(video)" class="text-blue-600 hover:text-blue-900" title="Preview">
                    <EyeIcon class="h-4 w-4" />
                  </button>
                  <router-link :to="`/videos/${video.slug || video.id}/edit`"
                    class="text-primary-600 hover:text-primary-900" title="Edit">
                    <PencilIcon class="h-4 w-4" />
                  </router-link>
                  <button @click="deleteVideo(video)" class="text-red-600 hover:text-red-900" title="Delete">
                    <TrashIcon class="h-4 w-4" />
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Empty State -->
      <EmptyState v-if="filteredVideos.length === 0" :icon="VideoCameraIcon" title="No videos found"
        :message="searchQuery || filters.status || filters.custom ? 'Try adjusting your search criteria.' : 'Get started by creating your first video.'"
        :action-label="!searchQuery && !filters.status && !filters.custom ? 'Add New Video' : null"
        :action-icon="PlusIcon" @action="$router.push('/videos/create')" />
    </div>
  </div>
</template>

<script setup>
  import { ref, computed, onMounted, watch } from 'vue'
  import { useRoute } from 'vue-router'
  import { useToast } from 'vue-toastification'
  import { useVideosStore } from '@/stores/videos'
  import { PageHeader, StatsGrid, StatCard, FilterBar, LoadingState, EmptyState } from '@/components/admin'
  import {
    PlusIcon,
    VideoCameraIcon,
    CheckCircleIcon,
    ClockIcon,
    EyeIcon,
    MagnifyingGlassIcon,
    PencilIcon,
    TrashIcon
  } from '@heroicons/vue/24/outline'

  const toast = useToast()
  const route = useRoute()
  const videosStore = useVideosStore()

  // Reactive data - using filters object for FilterBar
  const filters = ref({
    search: '',
    status: '',
    custom: ''
  })

  // Backward compatibility refs
  const searchQuery = computed({
    get: () => filters.value.search,
    set: (val) => { filters.value.search = val }
  })
  const statusFilter = computed({
    get: () => filters.value.status,
    set: (val) => { filters.value.status = val }
  })
  const categoryFilter = computed({
    get: () => filters.value.custom,
    set: (val) => { filters.value.custom = val }
  })

  // Use store data
  const videos = computed(() => videosStore.videos)
  const loading = computed(() => videosStore.loading)
  const error = computed(() => videosStore.error)
  const categories = computed(() => videosStore.categories)

  // Filter options for FilterBar
  const statusOptions = [
    { value: 'published', label: 'Published' },
    { value: 'draft', label: 'Draft' }
  ]

  const categoryOptions = computed(() => {
    if (!Array.isArray(categories.value)) return []
    return categories.value
      .filter(c => c && c.id)
      .map(c => ({ value: c.name, label: c.name }))
  })

  // Computed properties
  const stats = computed(() => {
    const total = videos.value.length
    const published = videos.value.filter(v => v.status?.toUpperCase() === 'PUBLISHED').length
    const draft = videos.value.filter(v => v.status?.toUpperCase() === 'DRAFT').length
    const totalViews = videos.value.reduce((sum, v) => sum + (v.views_count || 0), 0)

    return {
      total,
      published,
      draft,
      totalViews
    }
  })

  const filteredVideos = computed(() => {
    let filtered = videos.value

    // Filter by search query
    if (searchQuery.value) {
      const query = searchQuery.value.toLowerCase()
      filtered = filtered.filter(video =>
        video.title.toLowerCase().includes(query) ||
        (video.description && video.description.toLowerCase().includes(query))
      )
    }

    // Filter by status
    if (statusFilter.value) {
      filtered = filtered.filter(video => video.status?.toUpperCase() === statusFilter.value.toUpperCase())
    }

    // Filter by category
    if (categoryFilter.value) {
      filtered = filtered.filter(video => video.category?.name === categoryFilter.value)
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

  const previewVideo = (video) => {
    if (video.status === 'draft') {
      toast.warning('Cannot preview draft content')
      return
    }

    if (video.youtube_url) {
      window.open(video.youtube_url, '_blank')
    } else {
      toast.info('No video URL available')
    }
  }

  const deleteVideo = async (video) => {
    if (!confirm(`Are you sure you want to delete "${video.title}"?`)) {
      return
    }

    try {
      await videosStore.deleteVideo(video.slug || video.id)
      toast.success('Video deleted successfully')
    } catch (err) {
      console.error('Delete error:', err)
      toast.error('Failed to delete video')
    }
  }

  const fetchVideos = async () => {
    try {
      // Fetch categories first, then videos
      await videosStore.fetchCategories()
      await videosStore.fetchVideos()
    } catch (err) {
      console.error('Failed to fetch videos:', err)
      toast.error('Failed to load videos')
    }
  }

  // Watch for route changes to refresh data
  watch(() => route.path, (newPath) => {
    if (newPath === '/videos') {
      fetchVideos()
    }
  })

  // Lifecycle
  onMounted(() => {
    fetchVideos()
  })
</script>