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
          
          
            <!-- Enhanced Main Content Input with Paragraph Support -->
            <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
              <div class="space-y-2">
                <label class="block text-sm font-semibold text-gray-900">
                  Main Content *
                </label>
                <p class="text-xs text-gray-500">Write your blog post content with paragraph formatting</p>
                <textarea
            ref="editor"
                  v-model="form.content"
                  required
                  rows="8"
                  class="w-full px-4 py-3 border border-gray-300 rounded-xl text-base font-medium focus:outline-none focus:ring-2 focus:ring-[#8B4000] focus:border-[#8B4000] transition-all duration-200 placeholder-gray-400 resize-y"
                  placeholder="Start typing your content here...

You can create paragraphs by pressing Enter twice.

Each paragraph will be properly formatted when displayed."
                  style="font-family: 'Roboto', sans-serif; line-height: 1.6; min-height: 200px;"
            @input="handleContentChange"
                  @focus="handleEditorFocus"
                  @blur="handleEditorBlur"
                  @keydown="handleKeydown"
                ></textarea>
                <div class="flex items-center justify-between text-xs text-gray-500">
                  <span>{{ getWordCount() }} words • {{ getReadingTime() }} min read</span>
                  <span class="text-green-600" v-if="form.content.length > 50">Good length</span>
                </div>
              </div>
            </div>
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
                <label v-for="category in categories.filter(c => c && c.id)" :key="category.id" class="flex items-center p-2 rounded-lg hover:bg-white transition-colors cursor-pointer">
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
          
          <!-- Enhanced Status -->
          <div class="mb-6">
            <label class="block text-sm font-semibold text-gray-900 mb-2">Status</label>
            <select
              v-model="form.status"
              class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#8B4000] focus:border-[#8B4000] transition-all duration-200"
              style="font-family: 'Roboto', sans-serif;"
            >
              <option value="DRAFT">Draft</option>
              <option value="PUBLISHED">Published</option>
            </select>
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
            @click="imageInput.click()"
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
  status: 'DRAFT'
})

// Computed
const isEditing = computed(() => !!route.params.slug)
const categories = computed(() => {
  const cats = postsStore.categories || []
  return cats.filter(c => c && c.id)
})
const tags = computed(() => {
  const tagList = postsStore.tags
  if (!Array.isArray(tagList)) return []
  return tagList.filter(t => t && t.id)
})

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
}

const handleKeydown = (event) => {
  // Handle keyboard shortcuts for textarea
  if (event.ctrlKey || event.metaKey) {
    switch (event.key) {
      case 's':
        event.preventDefault()
        saveDraft()
        break
    }
  }
  
  // Handle Enter key for paragraph formatting
  if (event.key === 'Enter') {
    // Allow normal Enter behavior for line breaks
    // Double Enter will create paragraph separation
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
  // For textarea, no special handling needed
  // Textarea naturally handles LTR text direction and paragraphs
}

const handleEditorBlur = (event) => {
  // For textarea, no special handling needed
  // Textarea naturally handles LTR text direction and paragraphs
}

const handleKeyup = (event) => {
  // For textarea, no special handling needed
  // Textarea naturally handles LTR text direction and paragraphs
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

const getTagIds = (tagNames) => {
  if (!tagNames || !tagNames.trim()) return []
  
  const tagNameList = tagNames.split(',').map(tag => tag.trim()).filter(Boolean)
  const tagIds = []
  
  for (const tagName of tagNameList) {
    const tag = tags.value.find(t => t.name.toLowerCase() === tagName.toLowerCase())
    if (tag) {
      tagIds.push(tag.id)
    } else {
      console.warn(`Tag not found: ${tagName}`)
    }
  }
  
  return tagIds
}

// Methods
const handleImageUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    // Validate file type
    if (!file.type.startsWith('image/')) {
      toast.error('Please select an image file')
      return
    }
    
    // Validate file size (max 5MB)
    if (file.size > 5 * 1024 * 1024) {
      toast.error('Image size must be less than 5MB')
      return
    }
    
    const reader = new FileReader()
    reader.onload = (e) => {
      imagePreview.value = e.target.result
      form.value.featuredImage = file
      toast.success('Image uploaded successfully')
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

const savedSlug = ref(null)

const previewPost = async () => {
  if (!form.value.title) {
    toast.warning('Please enter a title first')
    return
  }
  
  // Use current slug if editing, or saved slug from create
  const slug = route.params.slug || savedSlug.value
  if (slug) {
    const previewUrl = `http://localhost:3003/blog/${slug}`
    window.open(previewUrl, '_blank')
    toast.info('Opening preview in new window...')
  } else {
    toast.warning('Please save the post first to preview it')
  }
}

const saveDraft = async () => {
  form.value.status = 'DRAFT'
  await savePost()
}

const updatePost = async () => {
  await savePost()
}

const savePost = async () => {
  if (!form.value.title || !form.value.title.trim()) {
    toast.error('Please enter a title')
    return
  }

  if (!form.value.content || !form.value.content.trim()) {
    toast.error('Please enter some content')
    return
  }

  loading.value = true

  try {
    const postData = {
      title: form.value.title || '',
      content: form.value.content || '',
      excerpt: form.value.excerpt || (form.value.content ? form.value.content.replace(/<[^>]*>/g, '').substring(0, 160) + '...' : ''),
      category: form.value.categories && form.value.categories.length > 0 ? form.value.categories[0] : null,
      tags: getTagIds(tagsInput.value),
      featured_image: form.value.featuredImage || null,
      status: form.value.status || 'DRAFT',
      language: 'en'
    }

    if (isEditing.value) {
      await postsStore.updatePost(route.params.slug, postData)
      toast.success('Post updated successfully')
    } else {
      const createdPost = await postsStore.createPost(postData)
      // Store slug for preview
      savedSlug.value = createdPost.slug
      toast.success('Post created successfully')
      // Stay on page after creation for preview ability
      // router.push('/posts')
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
    form.value.author = authStore.userFullName || 'Admin'

    await postsStore.fetchCategories()
    await postsStore.fetchTags()

    if (isEditing.value) {
      const post = await postsStore.fetchPost(route.params.slug)
      
      form.value = {
        title: post.title || '',
        content: post.content || '',
        excerpt: post.excerpt || '',
        author: post.author_name || authStore.userFullName || 'Admin',
        publishedAt: post.published_at ? post.published_at.split('T')[0] : new Date().toISOString().split('T')[0],
        categories: post.category ? [post.category.id] : [],
        tags: post.tags?.map(t => t.id) || [],
        featuredImage: post.featured_image || null,
        status: post.status || 'DRAFT'
      }
      
      tagsInput.value = post.tags?.map(t => t.name).join(', ') || ''
      
      // Update editor content
      await nextTick()
      if (editor.value) {
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
  white-space: pre-wrap !important;
  word-wrap: break-word !important;
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
