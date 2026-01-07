<template>
  <div class="bg-white rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300 overflow-hidden group">
    <!-- Thumbnail/Icon -->
    <div
      class="relative h-48 bg-gradient-to-br from-primary/80 to-primary flex items-center justify-center overflow-hidden">
      <img v-if="resource.thumbnail" :src="resource.thumbnail" :alt="resource.title"
        class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300"
        @error="handleImageError" />
      <div v-else class="text-center">
        <!-- File Type Icon -->
        <svg v-if="resource.file_type === 'pdf'" class="w-20 h-20 mx-auto text-white" fill="currentColor"
          viewBox="0 0 20 20">
          <path fill-rule="evenodd"
            d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z"
            clip-rule="evenodd" />
        </svg>
        <svg v-else-if="resource.file_type === 'doc' || resource.file_type === 'docx'"
          class="w-20 h-20 mx-auto text-white" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd"
            d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z"
            clip-rule="evenodd" />
        </svg>
        <svg v-else class="w-20 h-20 mx-auto text-white" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd"
            d="M8 4a3 3 0 00-3 3v4a5 5 0 0010 0V7a1 1 0 112 0v4a7 7 0 11-14 0V7a5 5 0 0110 0v4a3 3 0 11-6 0V7a1 1 0 012 0v4a1 1 0 102 0V7a3 3 0 00-3-3z"
            clip-rule="evenodd" />
        </svg>
        <p class="text-white text-sm mt-2 font-semibold uppercase">{{ resource.file_type || 'File' }}</p>
      </div>

      <!-- Category Badge -->
      <div v-if="resource.category" class="absolute top-3 left-3">
        <span class="inline-block px-3 py-1 text-xs font-bold bg-white text-black rounded-full shadow-md">
          {{ resource.category.name }}
        </span>
      </div>

      <!-- Language Badge -->
      <div v-if="resource.language" class="absolute top-3 right-3">
        <span class="inline-block px-2 py-1 text-xs font-black bg-white/90 text-primary rounded-full">
          {{ getLanguageName(resource.language) }}
        </span>
      </div>
    </div>

    <!-- Content -->
    <div class="p-6">
      <!-- Title -->
      <h3 class="text-lg font-bold text-neutral-black mb-2 line-clamp-2 group-hover:text-primary transition-colors">
        {{ resource.title }}
      </h3>
      [diff_block_start]
      <!-- Description -->
      <p class="text-sm text-neutral-black/80 mb-4 line-clamp-3 font-medium">
        {{ resource.description }}
      </p>
      [diff_block_end]
      <!-- Meta Information -->
      <div class="flex items-center justify-between text-xs text-muted mb-4">
        <!-- File Size -->
        <div v-if="resource.file_size" class="flex items-center space-x-1">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd"
              d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z"
              clip-rule="evenodd" />
          </svg>
          <span>{{ formatFileSize(resource.file_size) }}</span>
        </div>

        <!-- Downloads Count -->
        <div v-if="resource.download_count" class="flex items-center space-x-1">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path d="M10 12a2 2 0 100-4 2 2 0 000 4z" />
            <path fill-rule="evenodd"
              d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z"
              clip-rule="evenodd" />
          </svg>
          <span>{{ resource.download_count }} downloads</span>
        </div>
      </div>

      <!-- Download Button -->
      <a :href="resource.file" :download="resource.title" target="_blank"
        class="btn-primary w-full inline-flex items-center justify-center space-x-2 group/btn" @click="trackDownload"
        :aria-label="`Download ${resource.title}`">
        <svg class="w-5 h-5 group-hover/btn:animate-bounce" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd"
            d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z"
            clip-rule="evenodd" />
        </svg>
        <span>Download {{ resource.file_type ? resource.file_type.toUpperCase() : '' }}</span>
      </a>

      <!-- Published Date -->
      <div v-if="resource.published_at" class="mt-3 text-[10px] text-black/40 text-center font-bold">
        Published: {{ formatDate(resource.published_at) }}
      </div>
    </div>
  </div>
</template>

<script setup>
  const props = defineProps({
    resource: {
      type: Object,
      required: true
    }
  })

  const emit = defineEmits(['download'])

  // Language name mapping
  const getLanguageName = (code) => {
    const languages = {
      en: 'English',
      lg: 'Luganda',
      sw: 'Swahili'
    }
    return languages[code] || code
  }

  // Format file size
  const formatFileSize = (bytes) => {
    if (!bytes) return 'Unknown'

    const sizes = ['Bytes', 'KB', 'MB', 'GB']
    if (bytes === 0) return '0 Bytes'

    const i = Math.floor(Math.log(bytes) / Math.log(1024))
    return Math.round(bytes / Math.pow(1024, i) * 100) / 100 + ' ' + sizes[i]
  }

  // Format date
  const formatDate = (dateString) => {
    const options = { year: 'numeric', month: 'short', day: 'numeric' }
    return new Date(dateString).toLocaleDateString('en-US', options)
  }

  // Handle image error
  const handleImageError = (event) => {
    event.target.style.display = 'none'
  }

  // Track download
  const trackDownload = () => {
    emit('download', props.resource)
  }
</script>

<style scoped>
  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .line-clamp-3 {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
</style>
