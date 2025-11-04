<template>
  <div class="p-6 max-w-6xl mx-auto">
    <!-- Header -->
    <div class="mb-6">
      <h1 class="text-2xl font-bold text-gray-900" style="font-family: 'Roboto', sans-serif;">Settings</h1>
      <p class="text-gray-600 mt-1">Manage system configuration and user settings</p>
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

    <!-- General Settings Tab -->
    <div v-show="activeTab === 'general'" class="space-y-6">
      <div class="card p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Site Configuration</h3>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Site Name</label>
            <input
              v-model="settings.general.siteName"
              type="text"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Site URL</label>
            <input
              v-model="settings.general.siteUrl"
              type="url"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
          
          <div class="md:col-span-2">
            <label class="block text-sm font-medium text-gray-700 mb-2">Site Description</label>
            <textarea
              v-model="settings.general.siteDescription"
              rows="3"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            ></textarea>
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Admin Email</label>
            <input
              v-model="settings.general.adminEmail"
              type="email"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Timezone</label>
            <select
              v-model="settings.general.timezone"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            >
              <option value="Africa/Kampala">Africa/Kampala (UTC+3)</option>
              <option value="UTC">UTC (UTC+0)</option>
              <option value="America/New_York">America/New_York (UTC-5)</option>
              <option value="Europe/London">Europe/London (UTC+0)</option>
            </select>
          </div>
        </div>
      </div>

      <div class="card p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Content Settings</h3>
        
        <div class="space-y-4">
          <div class="flex items-center justify-between">
            <div>
              <h4 class="text-sm font-medium text-gray-900">Allow Comments</h4>
              <p class="text-sm text-gray-500">Enable comments on blog posts</p>
            </div>
            <label class="relative inline-flex items-center cursor-pointer">
              <input
                v-model="settings.content.allowComments"
                type="checkbox"
                class="sr-only peer"
              />
              <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600"></div>
            </label>
          </div>
          
          <div class="flex items-center justify-between">
            <div>
              <h4 class="text-sm font-medium text-gray-900">Moderate Comments</h4>
              <p class="text-sm text-gray-500">Require admin approval for comments</p>
            </div>
            <label class="relative inline-flex items-center cursor-pointer">
              <input
                v-model="settings.content.moderateComments"
                type="checkbox"
                class="sr-only peer"
              />
              <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600"></div>
            </label>
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Posts per Page</label>
            <input
              v-model.number="settings.content.postsPerPage"
              type="number"
              min="1"
              max="50"
              class="w-32 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- User Management Tab -->
    <div v-show="activeTab === 'users'" class="space-y-6">
      <div class="card p-6">
        <div class="flex items-center justify-between mb-4">
          <h3 class="text-lg font-semibold text-gray-900">User Management</h3>
          <button @click="showAddUserModal = true" class="btn-primary">
            <PlusIcon class="h-4 w-4 mr-2" />
            Add User
          </button>
        </div>
        
        <div class="overflow-x-auto">
          <table class="min-w-full">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  User
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Role
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Status
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Last Login
                </th>
                <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Actions
                </th>
              </tr>
            </thead>
            <tbody class="bg-white">
              <tr v-for="user in users" :key="user.id" class="hover:bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="h-8 w-8 bg-gray-300 rounded-full flex items-center justify-center mr-3">
                      <span class="text-xs font-medium text-gray-600">
                        {{ user.name.split(' ').map(n => n[0]).join('').toUpperCase() }}
                      </span>
                    </div>
                    <div>
                      <div class="text-sm font-medium text-gray-900">{{ user.name }}</div>
                      <div class="text-sm text-gray-500">{{ user.email }}</div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span
                    class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
                    :class="{
                      'bg-purple-100 text-purple-800': user.role === 'ADMIN',
                      'bg-blue-100 text-blue-800': user.role === 'EDITOR',
                      'bg-green-100 text-green-800': user.role === 'AUTHOR',
                      'bg-gray-100 text-gray-800': user.role === 'VIEWER'
                    }"
                  >
                    {{ user.role }}
                  </span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span
                    class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
                    :class="{
                      'bg-green-100 text-green-800': user.status === 'active',
                      'bg-red-100 text-red-800': user.status === 'inactive'
                    }"
                  >
                    {{ user.status }}
                  </span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ formatDate(user.lastLogin) }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                  <div class="flex items-center justify-end space-x-2">
                    <button
                      @click="editUser(user)"
                      class="text-primary-600 hover:text-primary-900"
                    >
                      <PencilIcon class="h-4 w-4" />
                    </button>
                    <button
                      @click="deleteUser(user)"
                      class="text-red-600 hover:text-red-900"
                      :disabled="user.role === 'ADMIN'"
                    >
                      <TrashIcon class="h-4 w-4" />
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
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
  UsersIcon,
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
const activeTab = ref('general')
const saving = ref(false)
const showAddUserModal = ref(false)

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
  { id: 'general', name: 'General', icon: CogIcon },
  { id: 'categories', name: 'Categories', icon: TagIcon },
  { id: 'users', name: 'Users', icon: UsersIcon },
  { id: 'security', name: 'Security', icon: ShieldCheckIcon },
  { id: 'api', name: 'API', icon: CloudIcon }
]

// Settings data
const settings = reactive({
  general: {
    siteName: 'Sauti Child Helpline',
    siteUrl: 'https://sauti.org',
    siteDescription: 'A safe and accessible helpline for children in Uganda.',
    adminEmail: 'admin@sauti.org',
    timezone: 'Africa/Kampala'
  },
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
    baseUrl: 'http://localhost:8000/api',
    rateLimit: 100,
    enableCors: true
  }
})

// Mock users data
const users = ref([
  {
    id: 1,
    name: 'Admin User',
    email: 'admin@sauti.org',
    role: 'ADMIN',
    status: 'active',
    lastLogin: '2024-01-15T10:30:00Z'
  },
  {
    id: 2,
    name: 'Sarah Nakamura',
    email: 'sarah@sauti.org',
    role: 'EDITOR',
    status: 'active',
    lastLogin: '2024-01-14T15:20:00Z'
  },
  {
    id: 3,
    name: 'David Mugisha',
    email: 'david@sauti.org',
    role: 'AUTHOR',
    status: 'active',
    lastLogin: '2024-01-13T09:45:00Z'
  },
  {
    id: 4,
    name: 'Grace Achieng',
    email: 'grace@sauti.org',
    role: 'AUTHOR',
    status: 'inactive',
    lastLogin: '2024-01-10T14:15:00Z'
  }
])

// Methods
const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const saveSettings = async () => {
  saving.value = true
  
  try {
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    toast.success('Settings saved successfully')
  } catch (error) {
    console.error('Save error:', error)
    toast.error('Failed to save settings')
  } finally {
    saving.value = false
  }
}

const resetSettings = () => {
  if (confirm('Are you sure you want to reset all settings to defaults?')) {
    // Reset logic here
    toast.info('Settings reset to defaults')
  }
}

const editUser = (user) => {
  toast.info(`Edit user "${user.name}" - Feature coming soon`)
}

const deleteUser = (user) => {
  if (user.role === 'ADMIN') {
    toast.error('Cannot delete admin user')
    return
  }
  
  if (confirm(`Are you sure you want to delete user "${user.name}"?`)) {
    const index = users.value.findIndex(u => u.id === user.id)
    if (index > -1) {
      users.value.splice(index, 1)
      toast.success('User deleted successfully')
    }
  }
}

// Computed properties for filtered categories
const filteredBlogCategories = computed(() => {
  if (!categorySearch.value.blog) return blogCategories.value
  const search = categorySearch.value.blog.toLowerCase()
  return blogCategories.value.filter(cat => 
    cat.name.toLowerCase().includes(search) ||
    cat.slug.toLowerCase().includes(search) ||
    (cat.description && cat.description.toLowerCase().includes(search))
  )
})

const filteredVideoCategories = computed(() => {
  if (!categorySearch.value.video) return videoCategories.value
  const search = categorySearch.value.video.toLowerCase()
  return videoCategories.value.filter(cat => 
    cat.name.toLowerCase().includes(search) ||
    cat.slug.toLowerCase().includes(search) ||
    (cat.description && cat.description.toLowerCase().includes(search))
  )
})

const filteredResourceCategories = computed(() => {
  if (!categorySearch.value.resource) return resourceCategories.value
  const search = categorySearch.value.resource.toLowerCase()
  return resourceCategories.value.filter(cat => 
    cat.name.toLowerCase().includes(search) ||
    cat.slug.toLowerCase().includes(search) ||
    (cat.description && cat.description.toLowerCase().includes(search))
  )
})

const filteredFaqCategories = computed(() => {
  if (!categorySearch.value.faq) return faqCategories.value
  const search = categorySearch.value.faq.toLowerCase()
  return faqCategories.value.filter(cat => 
    cat.name.toLowerCase().includes(search) ||
    cat.slug.toLowerCase().includes(search) ||
    (cat.description && cat.description.toLowerCase().includes(search))
  )
})

// Category management methods
const fetchCategories = async () => {
  loadingCategories.value = true
  try {
    const [blogRes, videoRes, resourceRes, faqRes] = await Promise.all([
      api.posts.categories.list().catch(() => ({ data: [] })),
      api.videos.categories.list().catch(() => ({ data: [] })),
      api.resources.categories.list().catch(() => ({ data: [] })),
      api.faqs.categories.list().catch(() => ({ data: [] }))
    ])
    
    blogCategories.value = Array.isArray(blogRes.data) ? blogRes.data : (blogRes.data.results || [])
    videoCategories.value = Array.isArray(videoRes.data) ? videoRes.data : (videoRes.data.results || [])
    resourceCategories.value = Array.isArray(resourceRes.data) ? resourceRes.data : (resourceRes.data.results || [])
    faqCategories.value = Array.isArray(faqRes.data) ? faqRes.data : (faqRes.data.results || [])
  } catch (error) {
    console.error('Failed to fetch categories:', error)
    toast.error('Failed to load categories')
  } finally {
    loadingCategories.value = false
  }
}

const openCategoryModal = (type) => {
  categoryModalType.value = type
  editingCategory.value = null
  categoryForm.name = ''
  categoryForm.description = ''
  showCategoryModal.value = true
}

const openEditCategoryModal = (type, category) => {
  categoryModalType.value = type
  editingCategory.value = category
  categoryForm.name = category.name
  categoryForm.description = category.description || ''
  showCategoryModal.value = true
}

const closeCategoryModal = () => {
  showCategoryModal.value = false
  editingCategory.value = null
  categoryForm.name = ''
  categoryForm.description = ''
}

const getCategoryTypeName = () => {
  const typeMap = {
    'blog': 'Blog',
    'video': 'Video',
    'resource': 'Resource',
    'faq': 'FAQ'
  }
  return typeMap[categoryModalType.value] || 'Category'
}

const getApiEndpoint = () => {
  const endpointMap = {
    'blog': api.posts.categories,
    'video': api.videos.categories,
    'resource': api.resources.categories,
    'faq': api.faqs.categories
  }
  return endpointMap[categoryModalType.value]
}

const saveCategory = async () => {
  if (!categoryForm.name.trim()) {
    toast.error('Category name is required')
    return
  }

  try {
    const apiEndpoint = getApiEndpoint()
    
    const data = {
      name: categoryForm.name.trim(),
      description: categoryForm.description.trim() || ''
    }

    if (editingCategory.value) {
      // Update category
      try {
        await apiEndpoint.update(editingCategory.value.id, data)
        toast.success(`${getCategoryTypeName()} category updated successfully`)
      } catch (error) {
        if (error.message === 'Delete endpoint not available') {
          toast.info('Update endpoint not available. Please use the Django admin panel.')
          return
        }
        throw error
      }
    } else {
      // Create category
      await apiEndpoint.create(data)
      toast.success(`${getCategoryTypeName()} category created successfully`)
    }

    closeCategoryModal()
    await fetchCategories()
  } catch (error) {
    console.error('Failed to save category:', error)
    const message = error.response?.data?.name?.[0] || error.response?.data?.detail || 'Failed to save category'
    toast.error(message)
  }
}

const deleteCategory = async (type, category) => {
  if (!confirm(`Are you sure you want to delete "${category.name}"? This action cannot be undone.`)) {
    return
  }

  try {
    const endpointMap = {
      'blog': api.posts.categories,
      'video': api.videos.categories,
      'resource': api.resources.categories,
      'faq': api.faqs.categories
    }
    const apiEndpoint = endpointMap[type]
    const typeName = type.charAt(0).toUpperCase() + type.slice(1)
    
    try {
      await apiEndpoint.delete(category.id)
      toast.success(`${typeName} category deleted successfully`)
      await fetchCategories()
    } catch (error) {
      if (error.message === 'Delete endpoint not available' || error.response?.status === 404) {
        toast.info('Delete endpoint not available. Please use the Django admin panel.')
      } else {
        throw error
      }
    }
  } catch (error) {
    console.error('Failed to delete category:', error)
    const message = error.response?.data?.detail || 'Failed to delete category'
    toast.error(message)
  }
}

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
</script>
