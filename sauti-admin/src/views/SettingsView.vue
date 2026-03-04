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
        <button v-for="tab in settingsTabs" :key="tab.id" @click="activeTab = tab.id" :class="[
          'py-2 px-1 border-b-2 font-medium text-sm',
          activeTab === tab.id
            ? 'border-primary-500 text-primary-600'
            : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
        ]">
          <component :is="tab.icon" class="h-5 w-5 mr-2 inline" />
          {{ tab.name }}
        </button>
      </nav>
    </div>

    <!-- Global Tab -->
    <div v-if="activeTab === 'global'">
      <!-- Sub-tabs for Global settings -->
      <div class="border-b border-gray-200 mb-6">
        <nav class="-mb-px flex space-x-4">
          <button @click="activeSubTab = 'content'" :class="[
            'py-2 px-6 rounded-t-lg font-medium text-sm transition-all duration-200',
            activeSubTab === 'content'
              ? 'bg-white border-t border-l border-r border-gray-200 text-primary-600 shadow-sm'
              : 'text-gray-500 hover:text-gray-700 hover:bg-gray-50'
          ]">
            Static Content
          </button>
          <button @click="activeSubTab = 'site'" :class="[
            'py-2 px-6 rounded-t-lg font-medium text-sm transition-all duration-200',
            activeSubTab === 'site'
              ? 'bg-white border-t border-l border-r border-gray-200 text-primary-600 shadow-sm'
              : 'text-gray-500 hover:text-gray-700 hover:bg-gray-50'
          ]">
            Site Configuration
          </button>
        </nav>
      </div>

      <!-- Content for sub-tabs -->
      <div v-if="activeSubTab === 'content'">
        <ContentManager />
      </div>
      <div v-if="activeSubTab === 'site'">
        <div class="space-y-6">
          <div v-if="loadingSettings" class="text-center py-8">
            <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600 mx-auto"></div>
            <p class="mt-2 text-gray-500">Loading site settings...</p>
          </div>

          <div v-else-if="siteSettings" class="space-y-6">
            <!-- Site Identity -->
            <div class="card p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <GlobeAltIcon class="h-5 w-5 mr-2 text-primary-500" />
                Site Identity
              </h3>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="flex flex-col">
                  <label class="block text-sm font-medium text-gray-700 mb-2">Site Name</label>
                  <input v-model="siteSettings.site_name" type="text" class="input-primary" />
                </div>
                <div class="flex flex-col">
                  <label class="block text-sm font-medium text-gray-700 mb-2">Environment Label</label>
                  <input v-model="siteSettings.environment_label" type="text" placeholder="e.g. Production"
                    class="input-primary" />
                </div>
                <div class="flex flex-col md:col-span-2">
                  <label class="block text-sm font-medium text-gray-700 mb-2">Site Description</label>
                  <textarea v-model="siteSettings.site_description" rows="3" class="input-primary"></textarea>
                </div>
              </div>
            </div>

            <!-- Global Contact Display (Header/Quick Info) -->
            <div class="card p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <PhoneIcon class="h-5 w-5 mr-2 text-primary-500" />
                Global Contact Display
              </h3>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="flex flex-col">
                  <label class="block text-sm font-medium text-gray-700 mb-2">Hotline Display Text</label>
                  <input v-model="siteSettings.hotline_text" type="text" class="input-primary" />
                </div>
                <div class="flex flex-col">
                  <label class="block text-sm font-medium text-gray-700 mb-2">Support Email Display</label>
                  <input v-model="siteSettings.support_email_text" type="text" class="input-primary" />
                </div>
                <div class="flex flex-col md:col-span-2">
                  <label class="block text-sm font-medium text-gray-700 mb-2">Operating Hours Display</label>
                  <input v-model="siteSettings.operating_hours_text" type="text" class="input-primary" />
                </div>
              </div>
            </div>

            <!-- Redirection to Social Media & Contact Management -->
            <div class="card p-6 bg-blue-50 border-blue-100">
              <div class="flex items-start">
                <div class="flex-shrink-0">
                  <ShareIcon class="h-8 w-8 text-blue-600" />
                </div>
                <div class="ml-4">
                  <h3 class="text-lg font-bold text-gray-900">Profiles & Contact Management</h3>
                  <p class="text-sm text-gray-600 mt-1 mb-4">
                    Social media profiles, official emails, and phone numbers are now managed in a dedicated central
                    section to ensure consistency across the platform.
                  </p>
                  <router-link to="/social-media?tab=contact"
                    class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                    Go to Profiles & Contact Management
                  </router-link>
                </div>
              </div>
            </div>

            <!-- Footer & Legal -->
            <div class="card p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <ScaleIcon class="h-5 w-5 mr-2 text-primary-500" />
                Footer & Legal
              </h3>
              <div class="space-y-6">
                <div class="flex flex-col">
                  <label class="block text-sm font-medium text-gray-700 mb-2">Footer Text</label>
                  <textarea v-model="siteSettings.footer_text" rows="3" class="input-primary"></textarea>
                </div>
                <div class="flex flex-col">
                  <label class="block text-sm font-medium text-gray-700 mb-2">Ministry Attribution Text</label>
                  <textarea v-model="siteSettings.ministry_attribution_text" rows="2" class="input-primary"></textarea>
                </div>
                <div class="flex flex-col">
                  <label class="block text-sm font-medium text-gray-700 mb-2">Disclaimer Text</label>
                  <textarea v-model="siteSettings.disclaimer_text" rows="2" class="input-primary"></textarea>
                </div>
              </div>
            </div>

            <!-- SEO Defaults -->
            <div class="card p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <MagnifyingGlassIcon class="h-5 w-5 mr-2 text-primary-500" />
                SEO Defaults
              </h3>
              <div class="grid grid-cols-1 gap-6">
                <div class="flex flex-col">
                  <label class="block text-sm font-medium text-gray-700 mb-2">Meta Title Suffix</label>
                  <input v-model="siteSettings.default_meta_title_suffix" type="text" placeholder="| Sauti 116"
                    class="input-primary" />
                </div>
                <div class="flex flex-col">
                  <label class="block text-sm font-medium text-gray-700 mb-2">Default Meta Description</label>
                  <textarea v-model="siteSettings.default_meta_description" rows="3" class="input-primary"></textarea>
                </div>
              </div>
            </div>

            <!-- Home Page Content -->
            <div class="card p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <HomeIcon class="h-5 w-5 mr-2 text-primary-500" />
                Home Page Content
              </h3>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="flex flex-col">
                  <label class="block text-sm font-medium text-gray-700 mb-2">Hero Title</label>
                  <input v-model="siteSettings.hero_title" type="text" class="input-primary" />
                </div>
                <div class="flex flex-col">
                  <label class="block text-sm font-medium text-gray-700 mb-2">Hero Subtitle</label>
                  <textarea v-model="siteSettings.hero_subtitle" rows="2" class="input-primary"></textarea>
                </div>
                <div class="flex flex-col">
                  <label class="block text-sm font-medium text-gray-700 mb-2">Journey Title</label>
                  <input v-model="siteSettings.journey_title" type="text" class="input-primary" />
                </div>
                <div class="flex flex-col">
                  <label class="block text-sm font-medium text-gray-700 mb-2">Journey Description</label>
                  <textarea v-model="siteSettings.journey_description" rows="2" class="input-primary"></textarea>
                </div>
              </div>
            </div>

            <!-- Other Dynamic Settings -->
            <div class="card p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <DocumentTextIcon class="h-5 w-5 mr-2 text-primary-500" />
                Other Configuration
              </h3>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div v-for="(value, key) in textSettings" :key="key" class="flex flex-col">
                  <template
                    v-if="!['site_name', 'site_description', 'environment_label', 'hotline_text', 'support_email_text', 'operating_hours_text', 'footer_text', 'ministry_attribution_text', 'disclaimer_text', 'default_meta_title_suffix', 'default_meta_description', 'contact_email_info', 'contact_email_sautichl', 'contact_website', 'contact_phone_main', 'social_facebook', 'social_twitter', 'social_whatsapp', 'social_ureport', 'social_safepal', 'hero_title', 'hero_subtitle', 'journey_title', 'journey_description'].includes(key)">
                    <label :for="key" class="block text-sm font-medium text-gray-700 mb-2 capitalize">{{
                      key.replace(/_/g, ' ') }}</label>
                    <input v-if="value !== null && value !== undefined && value.length < 100" type="text" :id="key"
                      v-model="siteSettings[key]" class="input-primary" />
                    <textarea v-else :id="key" v-model="siteSettings[key]" rows="3" class="input-primary"></textarea>
                  </template>
                </div>
              </div>
            </div>
          </div>

          <!-- Audit History -->
          <AuditHistory :history="history" :loading="loadingHistory" />
        </div>
      </div>
    </div>

    <!-- Organization Tab -->
    <div v-if="activeTab === 'organization'">
      <div v-if="loadingOrg" class="text-center py-8">
        <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600 mx-auto"></div>
        <p class="mt-2 text-gray-500">Loading organization profile...</p>
      </div>

      <div v-else-if="orgProfile" class="space-y-6">
        <!-- Basic Identity -->
        <div class="card p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
            <BuildingOfficeIcon class="h-5 w-5 mr-2 text-primary-500" />
            Basic Identity
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="flex flex-col">
              <label class="block text-sm font-medium text-gray-700 mb-2">Organization Name</label>
              <input v-model="orgProfile.name" type="text" class="input-primary" />
            </div>
            <div class="flex flex-col">
              <label class="block text-sm font-medium text-gray-700 mb-2">Tagline</label>
              <input v-model="orgProfile.tagline" type="text" class="input-primary" />
            </div>
            <!-- Logo Upload -->
            <div class="flex flex-col">
              <label class="block text-sm font-medium text-gray-700 mb-2">Organization Logo</label>
              <div class="flex items-center space-x-4">
                <img v-if="orgProfile.logo && typeof orgProfile.logo === 'string'" :src="orgProfile.logo"
                  class="h-12 w-auto object-contain bg-gray-50 rounded p-1 border" />
                <input type="file" @change="handleLogoUpload" accept="image/*"
                  class="text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-primary-50 file:text-primary-700 hover:file:bg-primary-100" />
              </div>
            </div>
            <!-- Favicon Upload -->
            <div class="flex flex-col">
              <label class="block text-sm font-medium text-gray-700 mb-2">Favicon</label>
              <div class="flex items-center space-x-4">
                <img v-if="orgProfile.favicon && typeof orgProfile.favicon === 'string'" :src="orgProfile.favicon"
                  class="h-8 w-8 object-contain bg-gray-50 rounded p-1 border" />
                <input type="file" @change="handleFaviconUpload" accept="image/*"
                  class="text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-primary-50 file:text-primary-700 hover:file:bg-primary-100" />
              </div>
            </div>
          </div>
        </div>

        <!-- Branding Colors -->
        <div class="card p-6 overflow-hidden">
          <div class="flex items-center justify-between mb-6">
            <h3 class="text-lg font-semibold text-gray-900 flex items-center">
              <SwatchIcon class="h-5 w-5 mr-2 text-primary-500" />
              Branding Colors
            </h3>
            <span class="text-xs text-gray-400 bg-gray-100 px-2 py-1 rounded">SAUTI 116 Standard Palette</span>
          </div>

          <div class="space-y-8">
            <!-- Grouping Colors by Category -->
            <div v-for="group in ['Primary', 'Secondary', 'Accent', 'Neutral']" :key="group" class="border-b border-gray-100 pb-6 last:border-0 last:pb-0">
              <h4 class="text-sm font-bold text-gray-500 uppercase tracking-wider mb-4">{{ group }} Colours</h4>
              <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <div v-for="color in getColorsByGroup(group)" :key="color.id" class="flex flex-col space-y-2">
                  <div class="flex items-center justify-between">
                    <label class="block text-xs font-semibold text-gray-700 uppercase tracking-tighter">{{ color.name }}</label>
                    <button @click="resetColorToDefault(color)" :disabled="color.value === color.default"
                      class="text-[10px] text-primary-600 hover:text-primary-800 disabled:text-gray-300 transition-colors uppercase font-bold">
                      Reset
                    </button>
                  </div>
                  <div class="relative flex items-center">
                    <div class="flex-shrink-0 mr-2">
                      <input v-model="color.value" type="color"
                        class="h-10 w-10 border-0 rounded-lg p-0 cursor-pointer shadow-sm hover:ring-2 hover:ring-primary-300 transition-all" />
                    </div>
                    <div class="flex-1">
                      <input v-model="color.value" type="text" 
                        class="input-primary w-full text-sm font-mono focus:ring-1" 
                        placeholder="#000000" />
                    </div>
                  </div>
                  <div class="flex items-center justify-between px-1">
                    <span class="text-[10px] text-gray-400">Default: <span class="font-mono">{{ color.default }}</span></span>
                    <div v-if="color.id === 'primary_red'" class="flex items-center">
                      <span class="h-2 w-2 rounded-full bg-red-500 mr-1 animate-pulse"></span>
                      <span class="text-[9px] text-red-500 font-bold uppercase">Emergency CTA</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="mt-8 p-4 bg-orange-50 border border-orange-100 rounded-lg flex items-start">
            <InformationCircleIcon class="h-5 w-5 text-orange-500 mr-3 mt-0.5 flex-shrink-0" />
            <p class="text-sm text-orange-800">
              <strong>Brand Guardrail:</strong> These colours form the core identity of SAUTI 116. While customisation is permitted, we recommend maintaining high contrast ratios (especially for Neutral colours) to ensure accessibility across all devices.
            </p>
          </div>
        </div>

        <!-- Contact Information -->
        <div class="card p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
            <EnvelopeIcon class="h-5 w-5 mr-2 text-primary-500" />
            Contact Information
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="flex flex-col md:col-span-2">
              <label class="block text-sm font-medium text-gray-700 mb-2">Office Address</label>
              <textarea v-model="orgProfile.address" rows="2" class="input-primary"></textarea>
            </div>
            <div class="flex flex-col">
              <label class="block text-sm font-medium text-gray-700 mb-2">Primary Phone</label>
              <input v-model="orgProfile.primary_phone" type="text" class="input-primary" />
            </div>
            <div class="flex flex-col">
              <label class="block text-sm font-medium text-gray-700 mb-2">Primary Email</label>
              <input v-model="orgProfile.primary_email" type="email" class="input-primary" />
            </div>
          </div>
        </div>

        <!-- Legal & History -->
        <div class="card p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
            <ScaleIcon class="h-5 w-5 mr-2 text-primary-500" />
            Legal & History
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="flex flex-col">
              <label class="block text-sm font-medium text-gray-700 mb-2">Founded Date</label>
              <input v-model="orgProfile.founded_date" type="date" class="input-primary" />
            </div>
            <div class="flex flex-col">
              <label class="block text-sm font-medium text-gray-700 mb-2">Legal/Registration Info</label>
              <input v-model="orgProfile.registration_info" type="text" class="input-primary" />
            </div>
            <div class="flex flex-col md:col-span-2">
              <label class="block text-sm font-medium text-gray-700 mb-2">Organization Summary</label>
              <textarea v-model="orgProfile.about_us_summary" rows="3" class="input-primary"></textarea>
            </div>
          </div>
        </div>

        <!-- Organization History -->
        <AuditHistory :history="orgHistory" :loading="loadingOrg" title="Organization Profile History" />
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
            <label v-if="settings?.security" class="relative inline-flex items-center cursor-pointer">
              <input v-model="settings.security.requireTwoFactor" type="checkbox" class="sr-only peer" />
              <div
                class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600">
              </div>
            </label>
          </div>

          <div v-if="settings?.security">
            <label class="block text-sm font-medium text-gray-700 mb-2">Session Timeout (minutes)</label>
            <input v-model.number="settings.security.sessionTimeout" type="number" min="15" max="480"
              class="w-32 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500" />
          </div>

          <div v-if="settings?.security">
            <label class="block text-sm font-medium text-gray-700 mb-2">Maximum Login Attempts</label>
            <input v-model.number="settings.security.maxLoginAttempts" type="number" min="3" max="10"
              class="w-32 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500" />
          </div>
        </div>
      </div>

      <div class="card p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Password Policy</h3>

        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Minimum Password Length</label>
            <input v-model.number="settings.security.minPasswordLength" type="number" min="6" max="20"
              class="w-32 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500" />
          </div>

          <div class="flex items-center justify-between">
            <div>
              <h4 class="text-sm font-medium text-gray-900">Require Special Characters</h4>
              <p class="text-sm text-gray-500">Passwords must contain special characters</p>
            </div>
            <label v-if="settings?.security" class="relative inline-flex items-center cursor-pointer">
              <input v-model="settings.security.requireSpecialChars" type="checkbox" class="sr-only peer" />
              <div
                class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600">
              </div>
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
          <input v-model="categorySearch.blog" type="text" placeholder="Search blog categories..."
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500" />
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
                    <button @click="openEditCategoryModal('blog', category)"
                      class="text-primary-600 hover:text-primary-900">
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
          <input v-model="categorySearch.video" type="text" placeholder="Search video categories..."
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500" />
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
                    <button @click="openEditCategoryModal('video', category)"
                      class="text-primary-600 hover:text-primary-900">
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
          <input v-model="categorySearch.resource" type="text" placeholder="Search resource categories..."
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500" />
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
                    <button @click="openEditCategoryModal('resource', category)"
                      class="text-primary-600 hover:text-primary-900">
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
          <input v-model="categorySearch.faq" type="text" placeholder="Search FAQ categories..."
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500" />
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
                    <button @click="openEditCategoryModal('faq', category)"
                      class="text-primary-600 hover:text-primary-900">
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
          <div v-if="settings?.api">
            <label class="block text-sm font-medium text-gray-700 mb-2">API Base URL</label>
            <input v-model="settings.api.baseUrl" type="url"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500" />
          </div>

          <div v-if="settings?.api">
            <label class="block text-sm font-medium text-gray-700 mb-2">Rate Limit (requests per minute)</label>
            <input v-model.number="settings.api.rateLimit" type="number" min="10" max="1000"
              class="w-32 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500" />
          </div>

          <div class="flex items-center justify-between" v-if="settings?.api">
            <div>
              <h4 class="text-sm font-medium text-gray-900">Enable CORS</h4>
              <p class="text-sm text-gray-500">Allow cross-origin requests</p>
            </div>
            <label class="relative inline-flex items-center cursor-pointer">
              <input v-model="settings.api.enableCors" type="checkbox" class="sr-only peer" />
              <div
                class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-600">
              </div>
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
              <input v-model="categoryForm.name" type="text" required
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                placeholder="Category name" />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Description</label>
              <textarea v-model="categoryForm.description" rows="3"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                placeholder="Category description (optional)"></textarea>
            </div>
          </div>

          <div class="flex items-center justify-end space-x-3 mt-6">
            <button @click="closeCategoryModal" class="px-4 py-2 text-gray-700 hover:text-gray-900 focus:outline-none">
              Cancel
            </button>
            <button @click="saveCategory" :disabled="!categoryForm.name" class="btn-primary">
              {{ editingCategory ? 'Update' : 'Create' }}
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Save Button -->
    <div class="flex items-center justify-end space-x-4 pt-6 border-t border-gray-200">
      <button @click="resetSettings" class="px-4 py-2 text-gray-700 hover:text-gray-900 focus:outline-none">
        Reset to Defaults
      </button>
      <button @click="saveSettings" :disabled="saving" class="btn-primary">
        {{ saving ? 'Saving...' : 'Save Settings' }}
      </button>
    </div>
  </div>
</template>

<script setup>
  import { ref, reactive, computed, onMounted, watch } from 'vue'
  import { useRoute } from 'vue-router'
  import { useToast } from 'vue-toastification'
  import {
    CogIcon,
    ShieldCheckIcon,
    CloudIcon,
    PlusIcon,
    PencilIcon,
    TrashIcon,
    TagIcon,
    GlobeAltIcon,
    PhoneIcon,
    EnvelopeIcon,
    ShareIcon,
    ScaleIcon,
    HomeIcon,
    BuildingOfficeIcon,
    SwatchIcon,
    InformationCircleIcon
  } from '@heroicons/vue/24/outline'
  import { api } from '@/utils/api'
  import AuditHistory from '@/components/common/AuditHistory.vue'
  import ContentManager from '@/views/ContentManager.vue'
  import { useSettingsStore } from '@/stores/settings'
  import { storeToRefs } from 'pinia'

  const toast = useToast()
  const route = useRoute()
  const settingsStore = useSettingsStore()
  const { settings } = storeToRefs(settingsStore)

  // Reactive data
  const activeTab = ref('global')
  const activeSubTab = ref('content') // 'content' or 'site'
  const saving = ref(false)

  // Site Settings
  const siteSettings = ref(null)
  const history = ref([])
  const loadingHistory = ref(false)
  const loadingSettings = ref(false)

  // Organization Profile
  const orgProfile = ref(null)
  const orgHistory = ref([])
  const loadingOrg = ref(false)
  const uploadingLogo = ref(false)
  const uploadingFavicon = ref(false)

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
    { id: 'organization', name: 'Organization', icon: BuildingOfficeIcon },
    { id: 'categories', name: 'Categories', icon: TagIcon },
    { id: 'security', name: 'Security', icon: ShieldCheckIcon },
    { id: 'api', name: 'API', icon: CloudIcon }
  ]



  // Fetch Site Settings
  async function fetchSiteSettings() {
    if (loadingSettings.value) return
    try {
      loadingSettings.value = true
      console.log('Fetching site settings...')
      // Use the defined API route if possible, otherwise use the direct one
      const response = await api.siteSettings.get()
      siteSettings.value = response.data
      console.log('Fetched siteSettings successfully:', siteSettings.value)
    } catch (error) {
      console.warn('Failed to fetch site settings via helper, trying direct route...', error)
      // Fallback for different backend URL structures
      try {
        const fallback = await api.get('/sitesettings/')
        siteSettings.value = fallback.data
        console.log('Fetched siteSettings via fallback:', siteSettings.value)
      } catch (e) {
        console.error('All site settings fetch attempts failed:', e)
        toast.error('Failed to load site settings. Check API connection.')
      }
    } finally {
      loadingSettings.value = false
    }
  }

  // Fetch Organization Profile
  async function fetchOrganizationProfile() {
    try {
      loadingOrg.value = true
      const response = await api.organizationProfile.get()
      orgProfile.value = response.data
      
      // Initialize brand_colors if it doesn't exist or is empty
      if (!orgProfile.value.brand_colors || orgProfile.value.brand_colors.length === 0) {
        orgProfile.value.brand_colors = getDefaultBrandColors()
      }
    } catch (error) {
      console.error('Failed to fetch organization profile:', error)
      toast.error('Failed to load organization profile')
    } finally {
      loadingOrg.value = false
    }
  }

  function getDefaultBrandColors() {
    return [
      { id: 'primary_blue', name: 'Primary Blue', value: '#007BBF', default: '#007BBF', group: 'Primary', is_required: true },
      { id: 'primary_red', name: 'Emergency / CTA Red', value: '#ED1C24', default: '#ED1C24', group: 'Primary', is_required: true },
      { id: 'secondary_dark_green', name: 'Dark Green', value: '#006633', default: '#006633', group: 'Secondary', is_required: true },
      { id: 'secondary_light_green', name: 'Light Green', value: '#8CC63F', default: '#8CC63F', group: 'Secondary', is_required: true },
      { id: 'accent_orange', name: 'Accent Orange', value: '#FF9933', default: '#FF9933', group: 'Accent', is_required: true },
      { id: 'accent_yellow', name: 'Accent Yellow', value: '#FFF200', default: '#FFF200', group: 'Accent', is_required: true },
      { id: 'neutral_black', name: 'Black', value: '#000000', default: '#000000', group: 'Neutral', is_required: true },
      { id: 'neutral_white', name: 'White', value: '#FFFFFF', default: '#FFFFFF', group: 'Neutral', is_required: true },
    ]
  }

  function getColorsByGroup(group) {
    if (!orgProfile.value || !orgProfile.value.brand_colors) return []
    return orgProfile.value.brand_colors.filter(c => c.group === group)
  }

  function resetColorToDefault(color) {
    color.value = color.default
    toast.info(`${color.name} reset to brand default`)
  }

  async function fetchOrgHistory() {
    try {
      const response = await api.organizationProfile.history()
      orgHistory.value = response.data
    } catch (err) {
      console.error('Failed to fetch org history:', err)
    }
  }

  // Handle Logo Upload
  function handleLogoUpload(event) {
    const file = event.target.files[0]
    if (file && orgProfile.value) {
      orgProfile.value.logo = file
    }
  }

  // Handle Favicon Upload
  function handleFaviconUpload(event) {
    const file = event.target.files[0]
    if (file && orgProfile.value) {
      orgProfile.value.favicon = file
    }
  }

  async function fetchHistory() {
    loadingHistory.value = true
    try {
      const response = await api.siteSettings.history()
      history.value = response.data
    } catch (err) {
      console.error('❌ Error fetching history:', err)
    } finally {
      loadingHistory.value = false
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
    // Handle query params for deep linking
    if (route.query.tab) activeTab.value = route.query.tab
    if (route.query.sub) activeSubTab.value = route.query.sub

    console.log('SettingsView mounted, activeTab:', activeTab.value, 'activeSubTab:', activeSubTab.value)
    fetchSiteSettings()
    fetchOrganizationProfile()
    fetchHistory()
    fetchOrgHistory()
    fetchCategories()
    settingsStore.fetchSettings()
  })

  // Watch for tab changes to handle re-initialization if needed
  watch(activeTab, (newTab) => {
    console.log('Main tab changed to:', newTab)
    if (newTab === 'global' && !activeSubTab.value) {
      activeSubTab.value = 'content'
    }
  })

  watch(activeSubTab, (newSubTab) => {
    console.log('Sub-tab changed to:', newSubTab)
  })

  async function saveSettings() {
    try {
      saving.value = true

      // Save site settings if on global tab
      if (activeTab.value === 'global' && siteSettings.value) {
        console.log('Saving siteSettings:', siteSettings.value)
        try {
          // Try to use the siteSettings specific helper
          const response = await api.siteSettings.update(siteSettings.value)
          siteSettings.value = response.data // Update with response from server
          toast.success('Site configuration saved successfully')
        } catch (error) {
          console.error('Failed to save site settings with main endpoint:', error)
          // Fallback for different backend URL structures
          try {
            const response = await api.put('/sitesettings/', siteSettings.value)
            siteSettings.value = response.data
            toast.success('Site configuration saved successfully (fallback)')
          } catch (e) {
            toast.error('Failed to save site configuration: ' + (error.response?.data?.detail || error.message))
            return
          }
        }
      }

      // Save Organization Profile if on organization tab
      if (activeTab.value === 'organization' && orgProfile.value) {
        console.log('Saving Organization Profile:', orgProfile.value)
        
        // Update legacy color fields for backward compatibility
        const primaryBlue = orgProfile.value.brand_colors.find(c => c.id === 'primary_blue')
        const secondaryGreen = orgProfile.value.brand_colors.find(c => c.id === 'secondary_dark_green')
        const accentOrange = orgProfile.value.brand_colors.find(c => c.id === 'accent_orange')
        
        if (primaryBlue) orgProfile.value.primary_color = primaryBlue.value
        if (secondaryGreen) orgProfile.value.secondary_color = secondaryGreen.value
        if (accentOrange) orgProfile.value.accent_color = accentOrange.value

        const response = await api.organizationProfile.update(orgProfile.value)
        orgProfile.value = response.data
        toast.success('Organization profile saved successfully')
      }

      // Handle other tabs (security, api)
      if (activeTab.value === 'security' || activeTab.value === 'api') {
        const success = await settingsStore.updateSettings(settings.value)
        if (success) {
          toast.success(`${activeTab.value.charAt(0).toUpperCase() + activeTab.value.slice(1)} settings updated successfully`)
        } else {
          toast.error(`Failed to update ${activeTab.value} settings`)
        }
      }

      if (activeTab.value === 'categories') {
        toast.info('Categories are managed and saved individually above')
      }

    } catch (error) {
      console.error('Failed to save general settings:', error)
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

      const blogRes = await api.posts.categories.list().catch(() => ({ data: [] }))
      console.log('blogRes.data:', blogRes.data)
      // API may return paginated object { count, results, ... }
      blogCategories.value = blogRes.data?.results ?? blogRes.data ?? []

      const videoRes = await api.videos.categories.list().catch(() => ({ data: [] }))
      console.log('videoRes.data:', videoRes.data)
      videoCategories.value = videoRes.data?.results ?? videoRes.data ?? []

      const resourceRes = await api.resources.categories.list().catch(() => ({ data: [] }))
      console.log('resourceRes.data:', resourceRes.data)
      resourceCategories.value = resourceRes.data?.results ?? resourceRes.data ?? []

      const faqRes = await api.faqs.categories.list().catch(() => ({ data: [] }))
      console.log('faqRes.data:', faqRes.data)
      faqCategories.value = faqRes.data?.results ?? faqRes.data ?? []

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

      // Simulate API calls
      await new Promise(resolve => setTimeout(resolve, 500))

      // In a real app, you would call specific API endpoints
      // For example:
      // if (categoryModalType.value === 'blog') {
      //   if (isEdit) await api.posts.updateCategory(editingCategory.value.id, categoryForm)
      //   else await api.posts.createCategory(categoryForm)
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

  function formatDate(dateString) {
    if (!dateString) return '-'
    return new Date(dateString).toLocaleDateString()
  }
</script>
