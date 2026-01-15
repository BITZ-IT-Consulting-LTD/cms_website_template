<template>
  <Teleport to="body">
    <Transition name="modal">
      <div
        v-if="isOpen"
        class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm"
        @click.self="close"
      >
        <div class="relative w-full max-w-4xl max-h-[90vh] overflow-y-auto bg-white rounded-xl shadow-2xl">
          <!-- Close Button -->
          <button
            @click="close"
            class="sticky top-4 right-4 float-right z-10 p-2 bg-black/50 hover:bg-black/70 rounded-full text-white transition-colors"
            aria-label="Close story details"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>

          <!-- Story Content -->
          <div class="p-8">
            <!-- Featured Image -->
            <div v-if="story.thumbnail" class="rounded-lg overflow-hidden mb-8">
              <img
                :src="story.thumbnail"
                :alt="story.title"
                class="w-full h-auto object-cover max-h-96"
              />
            </div>

            <!-- Category Badge -->
            <div v-if="story.category" class="mb-4">
              <span class="inline-block px-3 py-1 bg-primary/10 text-primary font-bold text-sm tracking-widest uppercase rounded-full">
                {{ story.category }}
              </span>
            </div>

            <!-- Title -->
            <h1 class="text-4xl md:text-5xl font-bold text-secondary mb-6 leading-tight">
              {{ story.title }}
            </h1>

            <!-- Meta Information -->
            <div class="flex flex-wrap items-center gap-6 pb-6 border-b border-gray-200 mb-8 text-sm text-gray-600">
              <div v-if="story.date" class="flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
                <span>{{ story.date }}</span>
              </div>
              <div v-if="story.author" class="flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <span>by {{ story.author }}</span>
              </div>
            </div>

            <!-- Excerpt -->
            <div v-if="story.excerpt" class="mb-8">
              <p class="text-lg text-gray-700 italic leading-relaxed">
                {{ story.excerpt }}
              </p>
            </div>

            <!-- Full Content -->
            <div v-if="story.content" class="prose prose-lg max-w-none text-gray-700 leading-relaxed space-y-6">
              <p v-for="(paragraph, index) in story.content.split('\n\n')" :key="index" class="text-base text-gray-700">
                {{ paragraph }}
              </p>
            </div>

            <!-- Fallback if no content -->
            <div v-else-if="!story.excerpt" class="text-center py-12 text-gray-500">
              <p>No additional details available for this story.</p>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { watch } from 'vue'

const props = defineProps({
  isOpen: {
    type: Boolean,
    default: false
  },
  story: {
    type: Object,
    default: () => ({})
  }
})

const emit = defineEmits(['close'])

const close = () => {
  emit('close')
}

// Close on Escape key
watch(() => props.isOpen, (isOpen) => {
  if (isOpen) {
    const handleEscape = (e) => {
      if (e.key === 'Escape') {
        close()
      }
    }
    document.addEventListener('keydown', handleEscape)
    // Prevent body scroll when modal is open
    document.body.style.overflow = 'hidden'

    return () => {
      document.removeEventListener('keydown', handleEscape)
      document.body.style.overflow = ''
    }
  } else {
    document.body.style.overflow = ''
  }
})
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-active .relative,
.modal-leave-active .relative {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.modal-enter-from .relative,
.modal-leave-to .relative {
  transform: scale(0.9);
  opacity: 0;
}

/* Basic prose styling for content */
.prose {
  color: inherit;
}

.prose p {
  margin-bottom: 1em;
}

.prose strong {
  font-weight: 600;
}

.prose em {
  font-style: italic;
}
</style>
