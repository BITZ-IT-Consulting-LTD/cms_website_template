<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Enhanced Header -->
    <div class="bg-white border-b border-gray-200 sticky top-0 z-10">
      <div class="px-6 py-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-4">
            <button
              @click="$router.go(-1)"
              class="p-2 rounded-full hover:bg-gray-100 transition-colors"
            >
              <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
              </svg>
            </button>
            <div>
              <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">
                {{ isEditing ? 'Edit Blog Post' : 'Create New Blog Post' }}
              </h1>
              <p class="text-sm text-gray-500 mt-1">
                {{ isEditing ? 'Update your blog post content and settings' : 'Write and publish a new blog post' }}
              </p>
            </div>
          </div>
          
          <div class="flex items-center space-x-3">
            <button
              @click="previewPost"
              class="btn-outline flex items-center"
              :disabled="!form.title"
            >
              <EyeIcon class="h-4 w-4 mr-2" />
              Preview
            </button>
            
            <button
              @click="saveDraft"
              class="btn-secondary flex items-center"
              :disabled="loading"
            >
              <svg class="h-4 w-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"/>
              </svg>
              Save Draft
            </button>
            
            <button
              @click="updatePost"
              class="btn-primary flex items-center"
              :disabled="loading || !form.title"
            >
              <svg class="h-4 w-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/>
              </svg>
              {{ isEditing ? 'Update Post' : 'Publish Post' }}
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="p-6">

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <!-- Main Content Area (Left Column) -->
        <div class="lg:col-span-2 space-y-6">
          <!-- Enhanced Post Title -->
          <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div class="space-y-2">
              <label for="title" class="block text-sm font-semibold text-gray-900">
                Post Title *
              </label>
              <p class="text-xs text-gray-500">Write a compelling title that captures your audience's attention</p>
              <input
                id="title"
                v-model="form.title"
                type="text"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-xl text-lg font-medium focus:outline-none focus:ring-2 focus:ring-[#8B4000] focus:border-[#8B4000] transition-all duration-200 placeholder-gray-400"
                placeholder="Enter your post title..."
                style="font-family: 'Roboto', sans-serif;"
              />
              <div class="flex items-center justify-between text-xs text-gray-500">
                <span>{{ form.title.length }}/100 characters</span>
                <span class="text-green-600" v-if="form.title.length > 10">Good length</span>
              </div>
            </div>
          </div>

          <!-- Enhanced Rich Text Editor -->
          <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
            <div class="px-6 py-4 border-b border-gray-200 bg-gray-50">
              <div class="flex items-center justify-between">
                <div>
                  <label class="block text-sm font-semibold text-gray-900">
                    Main Content *
                  </label>
                  <p class="text-xs text-gray-500 mt-1">Write your blog post content with rich formatting</p>
                </div>
                <div class="flex items-center space-x-2 text-xs text-gray-500">
                  <span>{{ getWordCount() }} words</span>
                  <span>•</span>
                  <span>{{ getReadingTime() }} min read</span>
                </div>
              </div>
            </div>
          
            <!-- Enhanced Editor Toolbar -->
            <div class="px-4 py-3 bg-white border-b border-gray-200 flex items-center space-x-2 overflow-x-auto">
              <button
                type="button"
                @click="toggleBold"
                class="p-2 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-[#8B4000] transition-all duration-200"
                :class="{ 'bg-[#8B4000] text-white': isActive('bold'), 'text-gray-600': !isActive('bold') }"
                title="Bold (Ctrl+B)"
              >
                <strong class="text-sm font-bold">B</strong>
              </button>
              
              <button
                type="button"
                @click="toggleItalic"
                class="p-2 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-[#8B4000] transition-all duration-200"
                :class="{ 'bg-[#8B4000] text-white': isActive('italic'), 'text-gray-600': !isActive('italic') }"
                title="Italic (Ctrl+I)"
              >
                <em class="text-sm font-bold">I</em>
              </button>
              
              <button
                type="button"
                @click="toggleUnderline"
                class="p-2 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-[#8B4000] transition-all duration-200"
                :class="{ 'bg-[#8B4000] text-white': isActive('underline'), 'text-gray-600': !isActive('underline') }"
                title="Underline"
              >
                <u class="text-sm font-bold">U</u>
              </button>
            
              <div class="w-px h-6 bg-gray-300"></div>
              
              <button
                type="button"
                @click="toggleHeading(1)"
                class="px-3 py-2 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-[#8B4000] transition-all duration-200 text-sm font-semibold"
                :class="{ 'bg-[#8B4000] text-white': isActive('heading', { level: 1 }), 'text-gray-600': !isActive('heading', { level: 1 }) }"
                title="Heading 1"
              >
                H1
              </button>
              
              <button
                type="button"
                @click="toggleHeading(2)"
                class="px-3 py-2 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-[#8B4000] transition-all duration-200 text-sm font-semibold"
                :class="{ 'bg-[#8B4000] text-white': isActive('heading', { level: 2 }), 'text-gray-600': !isActive('heading', { level: 2 }) }"
                title="Heading 2"
              >
                H2
              </button>
            
              <div class="w-px h-6 bg-gray-300"></div>
              
              <button
                type="button"
                @click="toggleBulletList"
                class="p-2 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-[#8B4000] transition-all duration-200"
                :class="{ 'bg-[#8B4000] text-white': isActive('bulletList'), 'text-gray-600': !isActive('bulletList') }"
                title="Bullet List"
              >
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M3 4a1 1 0 000 2h12a1 1 0 100-2H3zM3 8a1 1 0 000 2h12a1 1 0 100-2H3zM3 12a1 1 0 100 2h12a1 1 0 100-2H3z" />
                </svg>
              </button>
              
              <button
                type="button"
                @click="toggleOrderedList"
                class="p-2 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-[#8B4000] transition-all duration-200"
                :class="{ 'bg-[#8B4000] text-white': isActive('orderedList'), 'text-gray-600': !isActive('orderedList') }"
                title="Numbered List"
              >
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M3 3a1 1 0 000 2h12a1 1 0 100-2H3zM3 7a1 1 0 000 2h12a1 1 0 100-2H3zM3 11a1 1 0 100 2h12a1 1 0 100-2H3z" />
                </svg>
              </button>
            
              <div class="w-px h-6 bg-gray-300"></div>
              
              <button
                type="button"
                @click="insertLink"
                class="p-2 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-[#8B4000] transition-all duration-200 text-gray-600"
                title="Insert Link"
              >
                <LinkIcon class="w-4 h-4" />
              </button>
              
              <button
                type="button"
                @click="insertImage"
                class="p-2 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-[#8B4000] transition-all duration-200 text-gray-600"
                title="Insert Image"
              >
                <PhotoIcon class="w-4 h-4" />
              </button>
            </div>
          
            <!-- Enhanced Editor Content Area -->
            <textarea
              ref="editor"
              v-model="form.content"
              class="min-h-96 p-6 focus:ring-2 focus:ring-[#8B4000] prose max-w-none editor-content w-full border border-gray-300 rounded-lg resize-none"
              style="direction: ltr !important; text-align: left !important; unicode-bidi: normal !important; writing-mode: horizontal-tb !important; font-family: 'Roboto', sans-serif; font-size: 16px; line-height: 1.6;"
              placeholder="Start typing your content here..."
              @input="handleContentChange"
              @paste="handlePaste"
              @keydown="handleKeydown"
              @focus="handleEditorFocus"
              @blur="handleEditorBlur"
              @keyup="handleKeyup"
            ></textarea>
          </div>
      </div>

        <!-- Enhanced Metadata Sidebar (Right Column) -->
        <div class="space-y-6">
          <!-- Enhanced Metadata Card -->
          <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div class="flex items-center space-x-2 mb-6">
              <svg class="w-5 h-5 text-[#8B4000]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
              </svg>
              <h3 class="text-lg font-semibold text-gray-900" style="font-family: 'Roboto', sans-serif;">Post Settings</h3>
            </div>
          
            <!-- Enhanced Author Field -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-900 mb-2">Author</label>
              <div class="relative">
                <input
                  v-model="form.author"
                  type="text"
                  readonly
                  class="w-full px-4 py-3 border border-gray-300 rounded-xl bg-gray-50 text-gray-600 font-medium"
                  style="font-family: 'Roboto', sans-serif;"
                />
                <div class="absolute inset-y-0 right-0 flex items-center pr-3">
                  <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                  </svg>
                </div>
              </div>
            </div>
            
            <!-- Enhanced Publication Date -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-900 mb-2">Publication Date</label>
              <input
                v-model="form.publishedAt"
                type="date"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#8B4000] focus:border-[#8B4000] transition-all duration-200"
                style="font-family: 'Roboto', sans-serif;"
              />
            </div>
          
            <!-- Enhanced Categories -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-900 mb-3">Categories</label>
              <div class="space-y-3 max-h-40 overflow-y-auto border border-gray-200 rounded-xl p-3 bg-gray-50">
                <label v-for="category in categories" :key="category.id" class="flex items-center p-2 rounded-lg hover:bg-white transition-colors cursor-pointer">
                  <input
                    v-model="form.categories"
                    :value="category.id"
                    type="checkbox"
                    class="rounded border-gray-300 text-[#8B4000] focus:ring-[#8B4000] focus:ring-2"
                  />
                  <span class="ml-3 text-sm font-medium text-gray-700">{{ category.name }}</span>
                </label>
              </div>
            </div>
            
            <!-- Enhanced Tags -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-900 mb-2">Tags</label>
              <div class="relative">
                <input
                  v-model="tagsInput"
                  type="text"
                  placeholder="helpline, children, safety, uganda"
                  class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#8B4000] focus:border-[#8B4000] transition-all duration-200 placeholder-gray-400"
                  style="font-family: 'Roboto', sans-serif;"
                />
                <div class="absolute inset-y-0 right-0 flex items-center pr-3">
                  <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z"/>
                  </svg>
                </div>
              </div>
              <p class="mt-2 text-xs text-gray-500">Separate tags with commas for better organization</p>
            </div>
        </div>

          <!-- Enhanced Featured Image Card -->
          <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div class="flex items-center space-x-2 mb-6">
              <svg class="w-5 h-5 text-[#8B4000]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
              </svg>
              <h3 class="text-lg font-semibold text-gray-900" style="font-family: 'Roboto', sans-serif;">Featured Image</h3>
            </div>
          
            <div v-if="form.featuredImage || imagePreview" class="relative mb-6">
              <img
                :src="imagePreview || form.featuredImage"
                alt="Featured image"
                class="w-full h-48 object-cover rounded-xl shadow-sm"
              />
              <button
                @click="removeImage"
                class="absolute top-3 right-3 p-2 bg-red-500 text-white rounded-full hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500 transition-all duration-200 shadow-lg"
                title="Remove image"
              >
                <XMarkIcon class="h-4 w-4" />
              </button>
            </div>
            
            <div v-else class="border-2 border-dashed border-gray-300 rounded-xl p-8 text-center bg-gray-50 hover:bg-gray-100 transition-colors">
              <PhotoIcon class="h-12 w-12 text-gray-400 mx-auto mb-3" />
              <p class="text-sm text-gray-500 font-medium">No image selected</p>
              <p class="text-xs text-gray-400 mt-1">Click below to upload an image</p>
            </div>
            
            <input
              ref="imageInput"
              type="file"
              accept="image/*"
              @change="handleImageUpload"
              class="hidden"
            />
            
            <button
              @click="$refs.imageInput.click()"
              class="w-full mt-4 px-4 py-3 border-2 border-dashed border-[#8B4000] rounded-xl text-sm font-semibold text-[#8B4000] hover:bg-[#8B4000] hover:text-white focus:outline-none focus:ring-2 focus:ring-[#8B4000] transition-all duration-200"
              style="font-family: 'Roboto', sans-serif;"
            >
              {{ form.featuredImage || imagePreview ? 'Change Image' : 'Upload Image' }}
            </button>
        </div>

          <!-- Enhanced Action Buttons -->
          <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div class="space-y-3">
              <button
                @click="updatePost"
                :disabled="loading || !form.title"
                class="w-full btn-primary flex items-center justify-center"
                style="font-family: 'Roboto', sans-serif;"
              >
                <svg v-if="loading" class="animate-spin -ml-1 mr-3 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <svg v-else class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/>
                </svg>
                {{ loading ? 'Saving...' : (isEditing ? 'Update Post' : 'Publish Post') }}
              </button>
              
              <button
                @click="$router.go(-1)"
                class="w-full px-4 py-3 text-gray-600 hover:text-gray-900 hover:bg-gray-50 rounded-xl transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-gray-300"
                style="font-family: 'Roboto', sans-serif;"
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { usePostsStore } from '@/stores/posts'
import { useAuthStore } from '@/stores/auth'
import { useToast } from 'vue-toastification'
import {
  EyeIcon,
  LinkIcon,
  PhotoIcon,
  XMarkIcon
} from '@heroicons/vue/24/outline'

const route = useRoute()
const router = useRouter()
const postsStore = usePostsStore()
const authStore = useAuthStore()
const toast = useToast()

// Refs
const editor = ref(null)
const imageInput = ref(null)
const autoSaveTimeout = ref(null)

// Reactive data
const loading = ref(false)
const imagePreview = ref(null)
const tagsInput = ref('')

const form = ref({
  title: '',
  content: '',
  excerpt: '',
  author: '',
  publishedAt: new Date().toISOString().split('T')[0],
  categories: [],
  tags: [],
  featuredImage: null,
  status: 'draft'
})

// Computed
const isEditing = computed(() => !!route.params.slug)
const categories = computed(() => postsStore.categories)

// Editor methods (simplified - would use TipTap in real implementation)
const toggleBold = () => {
  document.execCommand('bold', false, null)
}

const toggleItalic = () => {
  document.execCommand('italic', false, null)
}

const toggleUnderline = () => {
  document.execCommand('underline', false, null)
}

const toggleHeading = (level) => {
  document.execCommand('formatBlock', false, `h${level}`)
}

const toggleBulletList = () => {
  document.execCommand('insertUnorderedList', false, null)
}

const toggleOrderedList = () => {
  document.execCommand('insertOrderedList', false, null)
}

const insertLink = () => {
  const url = prompt('Enter the URL:')
  if (url) {
    document.execCommand('createLink', false, url)
  }
}

const insertImage = () => {
  imageInput.value.click()
}

const isActive = (command, options = {}) => {
  // Simplified active state check
  return document.queryCommandState(command)
}

const handleContentChange = (event) => {
  // For textarea, the content is already in form.value.content via v-model
  // Force text direction on every change
  if (editor.value) {
    editor.value.style.direction = 'ltr'
    editor.value.style.textAlign = 'left'
    editor.value.style.unicodeBidi = 'normal'
    editor.value.style.writingMode = 'horizontal-tb'
    editor.value.setAttribute('dir', 'ltr')
  }
  
  // Auto-save draft every 30 seconds
  if (autoSaveTimeout.value) {
    clearTimeout(autoSaveTimeout.value)
  }
  autoSaveTimeout.value = setTimeout(() => {
    if (form.value.title && form.value.content) {
      saveDraft()
    }
  }, 30000)
}

const handlePaste = (event) => {
  // For textarea, let the default paste behavior work
  // The v-model will handle the content update
  // No need to prevent default or use execCommand
}

const handleKeydown = (event) => {
  // Handle keyboard shortcuts
  if (event.ctrlKey || event.metaKey) {
    switch (event.key) {
      case 'b':
        event.preventDefault()
        toggleBold()
        break
      case 'i':
        event.preventDefault()
        toggleItalic()
        break
      case 's':
        event.preventDefault()
        saveDraft()
        break
    }
  }
}

const handleEditorClick = (event) => {
  // Ensure cursor is positioned correctly when clicking
  const range = document.createRange()
  const sel = window.getSelection()
  
  // If clicking on empty space, position cursor there
  if (event.target === editor.value) {
    range.setStart(event.target, 0)
    range.collapse(true)
    sel.removeAllRanges()
    sel.addRange(range)
  }
}

const handleEditorFocus = (event) => {
  // Force text direction to LTR when editor is focused
  if (editor.value) {
    editor.value.style.direction = 'ltr'
    editor.value.style.textAlign = 'left'
    editor.value.style.unicodeBidi = 'normal'
    editor.value.style.writingMode = 'horizontal-tb'
    
    // Also set the dir attribute
    editor.value.setAttribute('dir', 'ltr')
    
    // Force cursor to LTR position
    const selection = window.getSelection()
    if (selection.rangeCount > 0) {
      const range = selection.getRangeAt(0)
      range.collapse(false) // Move to end
      selection.removeAllRanges()
      selection.addRange(range)
    }
  }
}

const handleEditorBlur = (event) => {
  // Ensure text direction is maintained even when editor loses focus
  if (editor.value) {
    editor.value.style.direction = 'ltr'
    editor.value.style.textAlign = 'left'
    editor.value.style.unicodeBidi = 'normal'
    editor.value.style.writingMode = 'horizontal-tb'
    editor.value.setAttribute('dir', 'ltr')
  }
}

const handleKeyup = (event) => {
  // Force text direction on every keyup
  if (editor.value) {
    // Force immediate text direction correction
    editor.value.style.direction = 'ltr'
    editor.value.style.textAlign = 'left'
    editor.value.style.unicodeBidi = 'normal'
    editor.value.style.writingMode = 'horizontal-tb'
    editor.value.setAttribute('dir', 'ltr')
    
    // Force all child elements to be LTR
    const allElements = editor.value.querySelectorAll('*')
    allElements.forEach(el => {
      el.style.direction = 'ltr'
      el.style.textAlign = 'left'
      el.style.unicodeBidi = 'normal'
      el.setAttribute('dir', 'ltr')
    })
    
    // Force cursor position to be LTR
    const selection = window.getSelection()
    if (selection.rangeCount > 0) {
      const range = selection.getRangeAt(0)
      // Ensure cursor is at the end (LTR position)
      range.collapse(false)
      selection.removeAllRanges()
      selection.addRange(range)
    }
  }
}

// Helper methods for content analysis
const getWordCount = () => {
  if (!form.value.content) return 0
  const text = form.value.content.replace(/<[^>]*>/g, '').trim()
  return text.split(/\s+/).filter(word => word.length > 0).length
}

const getReadingTime = () => {
  const words = getWordCount()
  const wordsPerMinute = 200
  return Math.ceil(words / wordsPerMinute)
}

// Methods
const handleImageUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      imagePreview.value = e.target.result
      form.value.featuredImage = file
    }
    reader.readAsDataURL(file)
  }
}

const removeImage = () => {
  imagePreview.value = null
  form.value.featuredImage = null
  if (imageInput.value) {
    imageInput.value.value = ''
  }
}

const previewPost = () => {
  if (!form.value.title) {
    toast.warning('Please enter a title first')
    return
  }
  toast.info('Preview functionality coming soon')
}

const saveDraft = async () => {
  await savePost('draft')
}

const updatePost = async () => {
  await savePost('published')
}

const savePost = async (status) => {
  if (!form.value.title.trim()) {
    toast.error('Please enter a title')
    return
  }

  if (!form.value.content.trim()) {
    toast.error('Please enter some content')
    return
  }

  loading.value = true

  try {
    const postData = {
      ...form.value,
      status,
      tags: tagsInput.value.split(',').map(tag => tag.trim()).filter(Boolean),
      excerpt: form.value.excerpt || form.value.content.replace(/<[^>]*>/g, '').substring(0, 160) + '...'
    }

    if (isEditing.value) {
      await postsStore.updatePost(route.params.slug, postData)
      toast.success('Post updated successfully')
    } else {
      await postsStore.createPost(postData)
      toast.success('Post created successfully')
      router.push('/posts')
    }
  } catch (err) {
    console.error('Save error:', err)
    const errorMessage = err.response?.data?.detail || err.message || 'Failed to save post'
    toast.error(errorMessage)
  } finally {
    loading.value = false
  }
}

// Lifecycle
onMounted(async () => {
  try {
    // Set author
    form.value.author = authStore.userFullName

    // Load categories
    await postsStore.fetchCategories()

    // Load post data if editing
    if (isEditing.value) {
      const post = await postsStore.fetchPost(route.params.slug)
      form.value = {
        ...form.value,
        ...post,
        publishedAt: post.published_at ? post.published_at.split('T')[0] : form.value.publishedAt,
        categories: post.categories?.map(c => c.id) || [],
        featuredImage: post.featured_image
      }
      
      tagsInput.value = post.tags?.map(t => t.name).join(', ') || ''
      
      // Update editor content
      await nextTick()
      if (editor.value) {
        // Force text direction
        editor.value.style.direction = 'ltr'
        editor.value.style.textAlign = 'left'
        editor.value.style.unicodeBidi = 'normal'
        editor.value.style.writingMode = 'horizontal-tb'
        editor.value.setAttribute('dir', 'ltr')
        
        // For textarea, the content is already set via v-model
        // Just focus the editor
        editor.value.focus()
        
        // Move cursor to the end of the content
        const length = editor.value.value.length
        editor.value.setSelectionRange(length, length)
      }
    }
  } catch (err) {
    console.error('Failed to load post data:', err)
    toast.error('Failed to load post data')
  }
})
</script>

<style scoped>
/* Editor styles */
[contenteditable]:focus {
  outline: none;
}

[contenteditable]:empty:before {
  content: attr(placeholder);
  color: #9ca3af;
  pointer-events: none;
}

[contenteditable] {
  direction: ltr !important;
  text-align: left !important;
  unicode-bidi: normal !important;
  writing-mode: horizontal-tb !important;
}

.editor-content {
  direction: ltr !important;
  text-align: left !important;
  unicode-bidi: normal !important;
  writing-mode: horizontal-tb !important;
}

textarea.editor-content {
  direction: ltr !important;
  text-align: left !important;
  unicode-bidi: normal !important;
  writing-mode: horizontal-tb !important;
  font-family: 'Roboto', sans-serif !important;
}

.prose h1 {
  @apply text-2xl font-bold mt-6 mb-4 text-gray-900;
}

.prose h2 {
  @apply text-xl font-semibold mt-5 mb-3 text-gray-800;
}

.prose p {
  @apply mb-3 text-gray-700 leading-relaxed;
}

.prose ul, .prose ol {
  @apply mb-3 pl-6;
}

.prose li {
  @apply mb-1;
}

.prose strong {
  @apply font-semibold;
}

.prose em {
  @apply italic;
}

.prose u {
  @apply underline;
}

.prose a {
  @apply text-[#8B4000] hover:text-[#A0522D] underline;
}

.prose img {
  @apply max-w-full h-auto rounded-lg shadow-sm;
}
</style>
