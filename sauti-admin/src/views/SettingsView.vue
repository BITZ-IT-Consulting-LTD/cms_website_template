<template>
  <div class="p-6 max-w-6xl mx-auto">
    <!-- Header -->
    <div class="mb-6">
      <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">Settings</h1>
      <p class="text-gray-600 mt-1">Manage system configuration</p>
    </div>

    <!-- Settings Tabs -->
    <div class="border-b border-gray-200 mb-6">
      <nav class="-mb-px flex space-x-8">
        <button
          v-for="tab in settingsTabs"
          :key="tab.id"
          @click="activeTab = tab.id"
          :class="[
            'py-2 px-1 border-b-2 font-medium text-sm',
            activeTab === tab.id
              ? 'border-primary-500 text-primary-600'
              : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
          ]"
        >
          <component :is="tab.icon" class="h-5 w-5 mr-2 inline" />
          {{ tab.name }}
        </button>
      </nav>
    </div>

    <!-- General Settings Tab (Site Settings) -->
    <div v-show="activeTab === 'general'" class="space-y-6">
      <div v-if="loadingSettings" class="text-center py-8">
        <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600 mx-auto"></div>
        <p class="mt-2 text-gray-500">Loading site settings...</p>
      </div>

      <div v-else class="card p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Site Configuration</h3>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div v-for="(value, key) in textSettings" :key="key" class="flex flex-col">
            <label :for="key" class="block text-sm font-medium text-gray-700 mb-2 capitalize">{{ key.replace(/_/g, ' ') }}</label>
            <input
              v-if="key !== 'site_description' && key !== 'footer_text' && key !== 'ministry_attribution_text' && key !== 'disclaimer_text' && key !== 'default_meta_description'"
              type="text"
              :id="key"
              v-model="siteSettings[key]"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
            <textarea
              v-else
              :id="key"
              v-model="siteSettings[key]"
              rows="3"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            ></textarea>
          </div>
        </div>
      </div>

    <div v-if="loading" class="text-center">
      <p>Loading settings...</p>
    </div>

    <div v-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
      <strong class="font-bold">Error!</strong>
      <span class="block sm:inline">{{ error }}</span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="setting in filteredSettings" :key="setting.key" class="bg-white rounded-lg shadow-md p-6 flex flex-col justify-between">
        <div>
          <h2 class="text-xl font-semibold mb-2">
            {{ setting.label || setting.key.replace(/_/g, ' ').split(' ').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join(' ') }}
          </h2>
          <p class="text-gray-600 mb-4">{{ setting.description }}</p>
          <div class="bg-gray-100 rounded-md p-4 text-gray-800">
            <p class="truncate">{{ setting.value }}</p>
          </div>
        </div>
        <button @click="openEditModal(setting)" class="mt-6 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-md transition duration-300">
          Edit
        </button>
      </div>
    </div>

    <!-- Edit Modal -->
    <div v-if="showModal" class="fixed z-10 inset-0 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 transition-opacity" aria-hidden="true">
          <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
        </div>

        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>

        <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <h3 class="text-lg leading-6 font-medium text-gray-900 mb-4">
              Edit Setting: {{ currentSetting.label || currentSetting.key.replace(/_/g, ' ').split(' ').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join(' ') }}
            </h3>
            <div class="mt-2">
              <textarea v-model="currentSetting.value" rows="10" class="w-full border border-gray-300 rounded-md p-2"></textarea>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
            <button @click="saveSetting" type="button" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm">
              Save
            </button>
            <button @click="closeModal" type="button" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
    </div>

    <!-- Security Tab -->
    <div v-show="activeTab === 'security'" class="space-y-6">
      <div class="card p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Authentication Settings</h3>
        
        <div class="space-y-4">
          <div class="flex items-center justify-between">
            <div>
              <h4 class="text-sm font-medium text-gray-900">Two-Factor Authentication</h4>
              <p class="text-sm text-gray-500">Require 2FA for all admin users</p>
            </div>
            <label class="relative inline-flex items-center cursor-pointer">
              <input
                v-model="settings.security.requireTwoFactor"
                type="checkbox"
                class="sr-only peer"
              />
              <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600"></div>
            </label>
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Session Timeout (minutes)</label>
            <input
              v-model.number="settings.security.sessionTimeout"
              type="number"
              min="15"
              max="480"
              class="w-32 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Maximum Login Attempts</label>
            <input
              v-model.number="settings.security.maxLoginAttempts"
              type="number"
              min="3"
              max="10"
              class="w-32 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
        </div>
      </div>
      
      <div class="card p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Password Policy</h3>
        
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Minimum Password Length</label>
            <input
              v-model.number="settings.security.minPasswordLength"
              type="number"
              min="6"
              max="20"
              class="w-32 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
          
          <div class="flex items-center justify-between">
            <div>
              <h4 class="text-sm font-medium text-gray-900">Require Special Characters</h4>
              <p class="text-sm text-gray-500">Passwords must contain special characters</p>
            </div>
            <label class="relative inline-flex items-center cursor-pointer">
              <input
                v-model="settings.security.requireSpecialChars"
                type="checkbox"
                class="sr-only peer"
              />
              <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600"></div>
            </label>
          </div>
        </div>
      </div>
    </div>

    <!-- Categories Tab -->
    <div v-show="activeTab === 'categories'" class="space-y-6">
      <!-- Blog Categories Section -->
      <div class="card p-6">
        <div class="flex items-center justify-between mb-6">
          <div>
            <h3 class="text-lg font-semibold text-gray-900">Blog Categories</h3>
            <p class="text-sm text-gray-500 mt-1">Manage categories for blog posts</p>
          </div>
          <button @click="openCategoryModal('blog')" class="btn-primary">
            <PlusIcon class="h-4 w-4 mr-2" />
            Add Category
          </button>
        </div>
        
        <!-- Search -->
        <div class="mb-4">
          <input
            v-model="categorySearch.blog"
            type="text"
            placeholder="Search blog categories..."
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        </div>
        
        <!-- Categories List -->
        <div v-if="loadingCategories" class="text-center py-8">
          <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600 mx-auto"></div>
        </div>
        <div v-else-if="filteredBlogCategories.length" class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Name</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Slug</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Description</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Created</th>
                <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="category in filteredBlogCategories" :key="category.id" class="hover:bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm font-medium text-gray-900">{{ category.name }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-500">{{ category.slug }}</div>
                </td>
                <td class="px-6 py-4">
                  <div class="text-sm text-gray-500 max-w-md truncate">{{ category.description || '-' }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ formatDate(category.created_at) }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                  <div class="flex items-center justify-end space-x-2">
                    <button @click="openEditCategoryModal('blog', category)" class="text-primary-600 hover:text-primary-900">
                      <PencilIcon class="h-4 w-4" />
                    </button>
                    <button @click="deleteCategory('blog', category)" class="text-red-600 hover:text-red-900">
                      <TrashIcon class="h-4 w-4" />
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div v-else class="text-center py-8 text-gray-500">
          No blog categories found. Create one to get started.
        </div>
      </div>
      
      <!-- Video Categories Section -->
      <div class="card p-6">
        <div class="flex items-center justify-between mb-6">
          <div>
            <h3 class="text-lg font-semibold text-gray-900">Video Categories</h3>
            <p class="text-sm text-gray-500 mt-1">Manage categories for videos</p>
          </div>
          <button @click="openCategoryModal('video')" class="btn-primary">
            <PlusIcon class="h-4 w-4 mr-2" />
            Add Category
          </button>
        </div>
        
        <!-- Search -->
        <div class="mb-4">
          <input
            v-model="categorySearch.video"
            type="text"
            placeholder="Search video categories..."
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        </div>
        
        <!-- Categories List -->
        <div v-if="loadingCategories" class="text-center py-8">
          <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600 mx-auto"></div>
        </div>
        <div v-else-if="filteredVideoCategories.length" class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Name</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Slug</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Description</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Created</th>
                <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="category in filteredVideoCategories" :key="category.id" class="hover:bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm font-medium text-gray-900">{{ category.name }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-500">{{ category.slug }}</div>
                </td>
                <td class="px-6 py-4">
                  <div class="text-sm text-gray-500 max-w-md truncate">{{ category.description || '-' }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ formatDate(category.created_at) }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                  <div class="flex items-center justify-end space-x-2">
                    <button @click="openEditCategoryModal('video', category)" class="text-primary-600 hover:text-primary-900">
                      <PencilIcon class="h-4 w-4" />
                    </button>
                    <button @click="deleteCategory('video', category)" class="text-red-600 hover:text-red-900">
                      <TrashIcon class="h-4 w-4" />
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div v-else class="text-center py-8 text-gray-500">
          No video categories found. Create one to get started.
        </div>
      </div>
      
      <!-- Resource Categories Section -->
      <div class="card p-6">
        <div class="flex items-center justify-between mb-6">
          <div>
            <h3 class="text-lg font-semibold text-gray-900">Resource Categories</h3>
            <p class="text-sm text-gray-500 mt-1">Manage categories for downloadable resources</p>
          </div>
          <button @click="openCategoryModal('resource')" class="btn-primary">
            <PlusIcon class="h-4 w-4 mr-2" />
            Add Category
          </button>
        </div>
        
        <!-- Search -->
        <div class="mb-4">
          <input
            v-model="categorySearch.resource"
            type="text"
            placeholder="Search resource categories..."
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        </div>
        
        <!-- Categories List -->
        <div v-if="loadingCategories" class="text-center py-8">
          <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600 mx-auto"></div>
        </div>
        <div v-else-if="filteredResourceCategories.length" class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Name</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Slug</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Description</th>
                <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="category in filteredResourceCategories" :key="category.id" class="hover:bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm font-medium text-gray-900">{{ category.name }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-500">{{ category.slug }}</div>
                </td>
                <td class="px-6 py-4">
                  <div class="text-sm text-gray-500 max-w-md truncate">{{ category.description || '-' }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                  <div class="flex items-center justify-end space-x-2">
                    <button @click="openEditCategoryModal('resource', category)" class="text-primary-600 hover:text-primary-900">
                      <PencilIcon class="h-4 w-4" />
                    </button>
                    <button @click="deleteCategory('resource', category)" class="text-red-600 hover:text-red-900">
                      <TrashIcon class="h-4 w-4" />
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div v-else class="text-center py-8 text-gray-500">
          No resource categories found. Create one to get started.
        </div>
      </div>
      
      <!-- FAQ Categories Section -->
      <div class="card p-6">
        <div class="flex items-center justify-between mb-6">
          <div>
            <h3 class="text-lg font-semibold text-gray-900">FAQ Categories</h3>
            <p class="text-sm text-gray-500 mt-1">Manage categories for frequently asked questions</p>
          </div>
          <button @click="openCategoryModal('faq')" class="btn-primary">
            <PlusIcon class="h-4 w-4 mr-2" />
            Add Category
          </button>
        </div>
        
        <!-- Search -->
        <div class="mb-4">
          <input
            v-model="categorySearch.faq"
            type="text"
            placeholder="Search FAQ categories..."
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        </div>
        
        <!-- Categories List -->
        <div v-if="loadingCategories" class="text-center py-8">
          <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600 mx-auto"></div>
        </div>
        <div v-else-if="filteredFaqCategories.length" class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Name</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Slug</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Description</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Order</th>
                <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="category in filteredFaqCategories" :key="category.id" class="hover:bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm font-medium text-gray-900">{{ category.name }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-500">{{ category.slug }}</div>
                </td>
                <td class="px-6 py-4">
                  <div class="text-sm text-gray-500 max-w-md truncate">{{ category.description || '-' }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-500">{{ category.order || 0 }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                  <div class="flex items-center justify-end space-x-2">
                    <button @click="openEditCategoryModal('faq', category)" class="text-primary-600 hover:text-primary-900">
                      <PencilIcon class="h-4 w-4" />
                    </button>
                    <button @click="deleteCategory('faq', category)" class="text-red-600 hover:text-red-900">
                      <TrashIcon class="h-4 w-4" />
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div v-else class="text-center py-8 text-gray-500">
          No FAQ categories found. Create one to get started.
        </div>
      </div>
    </div>

    <!-- API Settings Tab -->
    <div v-show="activeTab === 'api'" class="space-y-6">
      <div class="card p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">API Configuration</h3>
        
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">API Base URL</label>
            <input
              v-model="settings.api.baseUrl"
              type="url"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Rate Limit (requests per minute)</label>
            <input
              v-model.number="settings.api.rateLimit"
              type="number"
              min="10"
              max="1000"
              class="w-32 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
          
          <div class="flex items-center justify-between">
            <div>
              <h4 class="text-sm font-medium text-gray-900">Enable CORS</h4>
              <p class="text-sm text-gray-500">Allow cross-origin requests</p>
            </div>
            <label class="relative inline-flex items-center cursor-pointer">
              <input
                v-model="settings.api.enableCors"
                type="checkbox"
                class="sr-only peer"
              />
              <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600"></div>
            </label>
          </div>
        </div>
      </div>
    </div>

    <!-- Category Modal -->
    <div v-if="showCategoryModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg shadow-xl max-w-md w-full mx-4">
        <div class="p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">
            {{ editingCategory ? 'Edit' : 'Create' }} {{ getCategoryTypeName() }} Category
          </h3>
          
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Name *</label>
              <input
                v-model="categoryForm.name"
                type="text"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                placeholder="Category name"
              />
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Description</label>
              <textarea
                v-model="categoryForm.description"
                rows="3"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                placeholder="Category description (optional)"
              ></textarea>
            </div>
          </div>
          
          <div class="flex items-center justify-end space-x-3 mt-6">
            <button
              @click="closeCategoryModal"
              class="px-4 py-2 text-gray-700 hover:text-gray-900 focus:outline-none"
            >
              Cancel
            </button>
            <button
              @click="saveCategory"
              :disabled="!categoryForm.name"
              class="btn-primary"
            >
              {{ editingCategory ? 'Update' : 'Create' }}
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Save Button -->
    <div class="flex items-center justify-end space-x-4 pt-6 border-t border-gray-200">
      <button
        @click="resetSettings"
        class="px-4 py-2 text-gray-700 hover:text-gray-900 focus:outline-none"
      >
        Reset to Defaults
      </button>
      <button
        @click="saveSettings"
        :disabled="saving"
        class="btn-primary"
      >
        {{ saving ? 'Saving...' : 'Save Settings' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted, watch } from 'vue'
import { useToast } from 'vue-toastification'
import {
  CogIcon,
  ShieldCheckIcon,
  CloudIcon,
  PlusIcon,
  PencilIcon,
  TrashIcon,
  TagIcon
} from '@heroicons/vue/24/outline'
import { api } from '@/utils/api'

const toast = useToast()

// Reactive data
const activeTab = ref('global')
const saving = ref(false)

// Site Settings
const siteSettings = ref(null)
const loadingSettings = ref(false)

// Category management
const blogCategories = ref([])
const videoCategories = ref([])
const resourceCategories = ref([])
const faqCategories = ref([])
const loadingCategories = ref(false)
const showCategoryModal = ref(false)
const categoryModalType = ref('blog') // 'blog', 'video', 'resource', or 'faq'
const editingCategory = ref(null)
const categoryForm = reactive({
  name: '',
  description: ''
})
const categorySearch = ref({ blog: '', video: '', resource: '', faq: '' })

// Settings tabs
const settingsTabs = [
  { id: 'global', name: 'Global', icon: CogIcon },
  { id: 'categories', name: 'Categories', icon: TagIcon },
  { id: 'security', name: 'Security', icon: ShieldCheckIcon },
  { id: 'api', name: 'API', icon: CloudIcon }
]

// Settings data
const settings = reactive({
  // Removed hardcoded general settings
  content: {
    allowComments: true,
    moderateComments: true,
    postsPerPage: 10
  },
  security: {
    requireTwoFactor: false,
    sessionTimeout: 60,
    maxLoginAttempts: 5,
    minPasswordLength: 8,
    requireSpecialChars: true
  },
  api: {
    baseUrl: '/api',
    rateLimit: 100,
    enableCors: true
  }
})

// Fetch Site Settings
async function fetchSiteSettings() {
  try {
    loadingSettings.value = true
    const response = await api.get('/api/sitesettings/settings/')
    siteSettings.value = response.data
  } catch (error) {
    console.error('Failed to fetch site settings:', error)
    toast.error('Failed to load site settings')
  } finally {
    loadingSettings.value = false
  }
}

// Compute text settings for dynamic rendering
const textSettings = computed(() => {
  if (!siteSettings.value) return {}
  const excludedKeys = ['id']
  const filtered = {}
  for (const key in siteSettings.value) {
    if (!excludedKeys.includes(key)) {
      filtered[key] = siteSettings.value[key]
    }
  }
  return filtered
})

// Lifecycle
onMounted(() => {
  fetchSiteSettings()
  fetchCategories()
})

async function saveSettings() {
  try {
    saving.value = true
    
    // Save site settings if on general tab
    if (activeTab.value === 'general' && siteSettings.value) {
      await api.put('/api/sitesettings/settings/', siteSettings.value)
    }

    // Here you would also save the client-side settings to local storage or backend if needed
    // For now we just simulate saving other settings
    if (activeTab.value !== 'general') {
        await new Promise(resolve => setTimeout(resolve, 1000))
    }
    
    toast.success('Settings saved successfully')
  } catch (error) {
    console.error('Failed to save settings:', error)
    toast.error('Failed to save settings')
  } finally {
    saving.value = false
  }
}

function resetSettings() {
  if (confirm('Are you sure you want to reset all settings to defaults?')) {
    // Reset logic here
    toast.info('Settings reset to defaults')
    fetchSiteSettings() // Reload site settings
  }
}

// Category Management Functions
async function fetchCategories() {
  try {
    loadingCategories.value = true
    
    const [blogRes, videoRes, resourceRes, faqRes] = await Promise.all([
      api.posts.categories().catch(() => ({ data: [] })),
      api.videos.categories().catch(() => ({ data: [] })),
      api.resources.categories().catch(() => ({ data: [] })),
      api.faqs.categories().catch(() => ({ data: [] }))
    ])
    
    blogCategories.value = blogRes.data
    videoCategories.value = videoRes.data
    resourceCategories.value = resourceRes.data
    faqCategories.value = faqRes.data
  } catch (error) {
    console.error('Failed to fetch categories:', error)
    toast.error('Failed to load categories')
  } finally {
    loadingCategories.value = false
  }
}

const filteredBlogCategories = computed(() => {
  return blogCategories.value.filter(cat => 
    cat.name.toLowerCase().includes(categorySearch.value.blog.toLowerCase())
  )
})

const filteredVideoCategories = computed(() => {
  return videoCategories.value.filter(cat => 
    cat.name.toLowerCase().includes(categorySearch.value.video.toLowerCase())
  )
})

const filteredResourceCategories = computed(() => {
  return resourceCategories.value.filter(cat => 
    cat.name.toLowerCase().includes(categorySearch.value.resource.toLowerCase())
  )
})

const filteredFaqCategories = computed(() => {
  return faqCategories.value.filter(cat => 
    cat.name.toLowerCase().includes(categorySearch.value.faq.toLowerCase())
  )
})

function getCategoryTypeName() {
  switch (categoryModalType.value) {
    case 'blog': return 'Blog'
    case 'video': return 'Video'
    case 'resource': return 'Resource'
    case 'faq': return 'FAQ'
    default: return ''
  }
}

function openCategoryModal(type) {
  categoryModalType.value = type
  editingCategory.value = null
  categoryForm.name = ''
  categoryForm.description = ''
  showCategoryModal.value = true
}

function openEditCategoryModal(type, category) {
  categoryModalType.value = type
  editingCategory.value = category
  categoryForm.name = category.name
  categoryForm.description = category.description || ''
  showCategoryModal.value = true
}

function closeCategoryModal() {
  showCategoryModal.value = false
  editingCategory.value = null
  categoryForm.name = ''
  categoryForm.description = ''
}

async function saveCategory() {
  try {
    const isEdit = !!editingCategory.value
    const data = { ...categoryForm }
    
    // Simulate API calls
    await new Promise(resolve => setTimeout(resolve, 500))
    
    // In a real app, you would call specific API endpoints
    // For example:
    // if (categoryModalType.value === 'blog') {
    //   if (isEdit) await api.posts.updateCategory(editingCategory.value.id, data)
    //   else await api.posts.createCategory(data)
    // }
    
    toast.success(`${getCategoryTypeName()} category ${isEdit ? 'updated' : 'created'} successfully`)
    closeCategoryModal()
    fetchCategories() // Refresh list
  } catch (error) {
    console.error('Failed to save category:', error)
    toast.error('Failed to save category')
  }
}

async function deleteCategory(type, category) {
  if (!confirm(`Are you sure you want to delete "${category.name}"?`)) return
  
  try {
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 500))
    
    toast.success('Category deleted successfully')
    fetchCategories()
  } catch (error) {
    console.error('Failed to delete category:', error)
    toast.error('Failed to delete category')
  }
}

<<<<<<< Updated upstream
// Watch for tab changes to fetch categories when needed
watch(activeTab, (newTab) => {
  if (newTab === 'categories' && blogCategories.value.length === 0 && videoCategories.value.length === 0 && resourceCategories.value.length === 0 && faqCategories.value.length === 0) {
    fetchCategories()
  }
})

// Lifecycle
onMounted(() => {
  console.log('Settings page loaded')
  // Fetch categories if categories tab is active
  if (activeTab.value === 'categories') {
    fetchCategories()
  }
})

const loading = ref(false)
const error = ref(null)
const showModal = ref(false)
const currentSetting = ref(null)
const activePage = ref('general') // Default active page
const allSettings = ref([]) // Stores all settings fetched from the API
const rawGlobalSettings = ref({}) // Stores the raw object from API for saving

const pages = [
  { value: 'general', label: 'General' },
  { value: 'home', label: 'Home Page' },
  { value: 'about', label: 'About Page' },
  { value: 'resources', label: 'Resources' },
  { value: 'contact', label: 'Contact Info' },
  { value: 'footer', label: 'Footer' },
  { value: 'social', label: 'Social Media' },
  { value: 'seo', label: 'SEO' },
  { value: 'operations', label: 'Operations' },
  { value: 'header', label: 'Header' },
]

const filteredSettings = computed(() => {
  return allSettings.value.filter(setting => setting.page === activePage.value)
})

const fetchSettings = async () => {
  loading.value = true
  error.value = null
  try {
    const [globalRes, contentRes] = await Promise.all([
      api.get('/sitesettings/'),
      api.get('/content/site-content/')
    ])

    const rawSettings = Array.isArray(globalRes.data) ? globalRes.data[0] : globalRes.data;
    rawGlobalSettings.value = rawSettings;
    
    // Transform GlobalSettings
    const globalTransformed = Object.keys(rawSettings).map(key => {
      let page = 'general'; 
      const homePrefixes = ['hero_', 'quick_access_', 'card_', 'journey_', 'publications_', 'trust_partners_', 'final_cta_'];
      
      if (key.startsWith('contact_')) page = 'contact';
      else if (key.startsWith('social_')) page = 'social';
      else if (key.startsWith('resources_')) page = 'resources';
      else if (key.startsWith('about_')) page = 'about';
      else if (homePrefixes.some(p => key.startsWith(p))) page = 'home';
      else if (['footer_text', 'ministry_attribution_text', 'disclaimer_text'].includes(key)) page = 'footer';
      else if (key.includes('meta_') || key.includes('seo')) page = 'seo';
      else if (['hotline_text', 'support_email_text', 'operating_hours_text'].includes(key)) page = 'contact';
      
      return {
        key: key,
        value: rawSettings[key],
        page: page,
        description: `Setting for ${key.replace(/_/g, ' ')}`,
        model: 'GlobalSettings'
      };
    });

    // Transform SiteContent
    const siteContentItems = Array.isArray(contentRes.data) ? contentRes.data : (contentRes.data.results || []);
    const contentTransformed = siteContentItems.map(item => ({
      id: item.id,
      key: item.key,
      value: item.value,
      page: item.page,
      label: item.label,
      description: item.description || item.label,
      model: 'SiteContent'
    }));

    // Unified list with deduplication (GlobalSettings takes precedence)
    const combined = [...globalTransformed];
    const globalKeys = new Set(globalTransformed.map(s => s.key));
    
    contentTransformed.forEach(item => {
      if (!globalKeys.has(item.key)) {
        combined.push(item);
      }
    });

    allSettings.value = combined;
  } catch (err) {
    console.error('Error fetching site settings:', err)
    error.value = 'Failed to load site settings.'
  } finally {
    loading.value = false
  }
}

onMounted(async () => {
  await fetchSettings()
})

function openEditModal(setting) {
  currentSetting.value = { ...setting }
  showModal.value = true
}

function closeModal() {
  showModal.value = false
  currentSetting.value = null
}

async function saveSetting() {
  if (currentSetting.value && currentSetting.value.key) {
    loading.value = true
    error.value = null
    try {
      if (currentSetting.value.model === 'GlobalSettings') {
        const payload = { 
          ...rawGlobalSettings.value,
          [currentSetting.value.key]: currentSetting.value.value 
        };
        await api.put('/sitesettings/', payload)
      } else {
        // SiteContent
        await api.put(`/content/site-content/${currentSetting.value.id}/`, {
          key: currentSetting.value.key,
          value: currentSetting.value.value,
          label: currentSetting.value.label,
          page: currentSetting.value.page
        })
      }
      
      toast.success('Setting updated successfully')
      closeModal()
      await fetchSettings()
    } catch (err) {
      console.error('Error saving setting:', err)
      error.value = 'Failed to save setting.'
      toast.error('Failed to update setting')
    } finally {
      loading.value = false
    }
  }
=======
function formatDate(dateString) {
  if (!dateString) return '-'
  return new Date(dateString).toLocaleDateString()
>>>>>>> Stashed changes
}
</script>
