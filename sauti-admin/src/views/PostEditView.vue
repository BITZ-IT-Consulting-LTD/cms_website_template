<template>
  <div class="p-6">
    <!-- Header Actions -->
    <div class="flex items-center justify-between mb-6">
      <h1 class="text-2xl font-bold text-gray-900">
        {{ isEditing ? 'Edit Blog Post' : 'Create Blog Post' }}
      </h1>
      
      <div class="flex items-center space-x-3">
        <button
          @click="previewPost"
          class="btn-secondary flex items-center"
          :disabled="!form.title"
        >
          <EyeIcon class="h-4 w-4 mr-2" />
          Preview
        </button>
        
        <button
          @click="saveDraft"
          class="btn-secondary"
          :disabled="loading"
        >
          Save Draft
        </button>
        
        <button
          @click="updatePost"
          class="btn-success"
          :disabled="loading || !form.title"
        >
          {{ isEditing ? 'Update' : 'Publish' }}
        </button>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- Main Content Area (Left Column) -->
      <div class="lg:col-span-2 space-y-6">
        <!-- Post Title -->
        <div class="card p-6">
          <label for="title" class="block text-sm font-medium text-gray-700 mb-2">
            Post Title *
          </label>
          <input
            id="title"
            v-model="form.title"
            type="text"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md text-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            placeholder="Enter your post title..."
          />
        </div>

        <!-- Rich Text Editor -->
        <div class="card p-6">
          <label class="block text-sm font-medium text-gray-700 mb-4">
            Main Content *
          </label>
          
          <!-- Editor Toolbar -->
          <div class="border border-gray-300 rounded-t-md bg-gray-50 px-4 py-2 flex items-center space-x-2 overflow-x-auto">
            <button
              type="button"
              @click="toggleBold"
              class="p-1.5 rounded hover:bg-gray-200 focus:outline-none"
              :class="{ 'bg-gray-200': isActive('bold') }"
              title="Bold"
            >
              <strong class="text-sm">B</strong>
            </button>
            
            <button
              type="button"
              @click="toggleItalic"
              class="p-1.5 rounded hover:bg-gray-200 focus:outline-none"
              :class="{ 'bg-gray-200': isActive('italic') }"
              title="Italic"
            >
              <em class="text-sm">I</em>
            </button>
            
            <button
              type="button"
              @click="toggleUnderline"
              class="p-1.5 rounded hover:bg-gray-200 focus:outline-none"
              :class="{ 'bg-gray-200': isActive('underline') }"
              title="Underline"
            >
              <u class="text-sm">U</u>
            </button>
            
            <div class="w-px h-6 bg-gray-300"></div>
            
            <button
              type="button"
              @click="toggleHeading(1)"
              class="px-2 py-1.5 rounded hover:bg-gray-200 focus:outline-none text-sm font-medium"
              :class="{ 'bg-gray-200': isActive('heading', { level: 1 }) }"
              title="Heading 1"
            >
              H1
            </button>
            
            <button
              type="button"
              @click="toggleHeading(2)"
              class="px-2 py-1.5 rounded hover:bg-gray-200 focus:outline-none text-sm font-medium"
              :class="{ 'bg-gray-200': isActive('heading', { level: 2 }) }"
              title="Heading 2"
            >
              H2
            </button>
            
            <div class="w-px h-6 bg-gray-300"></div>
            
            <button
              type="button"
              @click="toggleBulletList"
              class="p-1.5 rounded hover:bg-gray-200 focus:outline-none"
              :class="{ 'bg-gray-200': isActive('bulletList') }"
              title="Bullet List"
            >
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path d="M3 4a1 1 0 000 2h12a1 1 0 100-2H3zM3 8a1 1 0 000 2h12a1 1 0 100-2H3zM3 12a1 1 0 100 2h12a1 1 0 100-2H3z" />
              </svg>
            </button>
            
            <button
              type="button"
              @click="toggleOrderedList"
              class="p-1.5 rounded hover:bg-gray-200 focus:outline-none"
              :class="{ 'bg-gray-200': isActive('orderedList') }"
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
              class="p-1.5 rounded hover:bg-gray-200 focus:outline-none"
              title="Insert Link"
            >
              <LinkIcon class="w-4 h-4" />
            </button>
            
            <button
              type="button"
              @click="insertImage"
              class="p-1.5 rounded hover:bg-gray-200 focus:outline-none"
              title="Insert Image"
            >
              <PhotoIcon class="w-4 h-4" />
            </button>
          </div>
          
          <!-- Editor Content Area -->
          <div
            ref="editor"
            class="min-h-96 p-4 border-l border-r border-b border-gray-300 rounded-b-md focus-within:ring-2 focus-within:ring-primary-500 focus-within:border-primary-500 prose max-w-none"
            contenteditable
            @input="handleContentChange"
            v-html="form.content"
          ></div>
        </div>
      </div>

      <!-- Metadata Sidebar (Right Column) -->
      <div class="space-y-6">
        <!-- Metadata -->
        <div class="card p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Metadata</h3>
          
          <!-- Author -->
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">Author</label>
            <input
              v-model="form.author"
              type="text"
              readonly
              class="w-full px-3 py-2 border border-gray-300 rounded-md bg-gray-50 text-gray-500"
            />
          </div>
          
          <!-- Publication Date -->
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">Publication Date</label>
            <input
              v-model="form.publishedAt"
              type="date"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
          
          <!-- Categories -->
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">Categories</label>
            <div class="space-y-2 max-h-32 overflow-y-auto">
              <label v-for="category in categories" :key="category.id" class="flex items-center">
                <input
                  v-model="form.categories"
                  :value="category.id"
                  type="checkbox"
                  class="rounded border-gray-300 text-primary-500 focus:ring-primary-500"
                />
                <span class="ml-2 text-sm text-gray-700">{{ category.name }}</span>
              </label>
            </div>
          </div>
          
          <!-- Tags -->
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">Tags</label>
            <input
              v-model="tagsInput"
              type="text"
              placeholder="helpline, children, safety, uganda"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
            <p class="mt-1 text-xs text-gray-500">Separate tags with commas</p>
          </div>
        </div>

        <!-- Featured Image -->
        <div class="card p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Featured Image</h3>
          
          <div v-if="form.featuredImage || imagePreview" class="relative mb-4">
            <img
              :src="imagePreview || form.featuredImage"
              alt="Featured image"
              class="w-full h-48 object-cover rounded-lg"
            />
            <button
              @click="removeImage"
              class="absolute top-2 right-2 p-1 bg-red-500 text-white rounded-full hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500"
              title="Remove image"
            >
              <XMarkIcon class="h-4 w-4" />
            </button>
          </div>
          
          <div v-else class="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center">
            <PhotoIcon class="h-12 w-12 text-gray-400 mx-auto mb-2" />
            <p class="text-sm text-gray-500">No image selected</p>
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
            class="w-full mt-4 px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
          >
            Change Image
          </button>
        </div>

        <!-- Action Buttons -->
        <div class="space-y-3">
          <button
            @click="updatePost"
            :disabled="loading || !form.title"
            class="w-full btn-primary"
          >
            {{ loading ? 'Saving...' : 'Save Changes' }}
          </button>
          
          <button
            @click="$router.go(-1)"
            class="w-full px-4 py-2 text-gray-700 hover:text-gray-900 focus:outline-none"
          >
            Cancel
          </button>
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
  form.value.content = event.target.innerHTML
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

  loading.value = true

  try {
    const postData = {
      ...form.value,
      status,
      tags: tagsInput.value.split(',').map(tag => tag.trim()).filter(Boolean)
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
    toast.error('Failed to save post')
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
        editor.value.innerHTML = post.content || ''
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

.prose h1 {
  @apply text-2xl font-bold mt-6 mb-4;
}

.prose h2 {
  @apply text-xl font-semibold mt-5 mb-3;
}

.prose p {
  @apply mb-3;
}

.prose ul, .prose ol {
  @apply ml-6 mb-3;
}

.prose ul {
  @apply list-disc;
}

.prose ol {
  @apply list-decimal;
}

.prose a {
  @apply text-primary-500 hover:text-primary-600 underline;
}
</style>
