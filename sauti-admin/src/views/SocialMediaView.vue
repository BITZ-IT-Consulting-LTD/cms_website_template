<template>
  <div class="social-media-view">
    <div class="max-w-6xl mx-auto">
      <!-- Header -->
      <div class="mb-8">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">Social Media & Contact Management</h1>
        <p class="text-gray-600">
          Manage social media channels and contact information displayed across the website
        </p>
      </div>

      <!-- Tabs -->
      <div class="mb-6">
        <div class="border-b border-gray-200">
          <nav class="-mb-px flex space-x-8">
            <button
              @click="activeTab = 'channels'"
              :class="[
                activeTab === 'channels'
                  ? 'border-blue-500 text-blue-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
                'whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm'
              ]"
            >
              Featured Content Feed
            </button>
            <button
              @click="activeTab = 'contact'"
              :class="[
                activeTab === 'contact'
                  ? 'border-blue-500 text-blue-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
                'whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm'
              ]"
            >
              Official Profiles & Contact
            </button>
            <button
              @click="activeTab = 'additional'"
              :class="[
                activeTab === 'additional'
                  ? 'border-blue-500 text-blue-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
                'whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm'
              ]"
            >
              Additional Contact Lists
            </button>
          </nav>
        </div>
      </div>

      <!-- Social Media Channels Tab -->
      <div v-if="activeTab === 'channels'">
        <!-- Loading State -->
        <div v-if="channelsLoading" class="flex items-center justify-center py-12">
          <div class="text-center">
            <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
            <p class="text-gray-600">Loading channels...</p>
          </div>
        </div>

        <!-- Form -->
        <div v-else class="bg-white rounded-lg shadow-sm p-8">
          <div class="mb-6">
            <h2 class="text-xl font-bold text-gray-900 mb-2">Social Media Post URLs</h2>
            <p class="text-gray-600 text-sm">
              Add up to 4 social media post URLs to display on your homepage. These will automatically fetch and display the content.
            </p>
          </div>

          <form @submit.prevent="saveChannels">
            <div class="space-y-6">
              <!-- Channel 1 -->
              <div>
                <label for="channel1" class="block text-sm font-medium text-gray-700 mb-2">
                  Channel 1 URL
                </label>
                <div class="flex gap-2">
                  <input
                    id="channel1"
                    v-model="channels.channel_1_url"
                    type="url"
                    class="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="https://www.tiktok.com/..."
                  />
                  <button
                    type="button"
                    @click="fetchMetadata('channel_1')"
                    class="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 text-sm font-medium whitespace-nowrap"
                    :disabled="fetchingMetadata['channel_1']"
                  >
                    {{ fetchingMetadata['channel_1'] ? 'Fetching...' : 'Preview' }}
                  </button>
                </div>
                <!-- Preview Card 1 -->
                <div v-if="previews.channel_1" class="mt-3 p-4 bg-gray-50 rounded-lg border border-gray-200 flex gap-4">
                  <img v-if="previews.channel_1.image" :src="previews.channel_1.image" class="w-20 h-20 object-cover rounded shadow-sm" alt="Preview" />
                  <div class="flex-1 min-w-0">
                    <p class="font-bold text-gray-900 truncate">{{ previews.channel_1.title || 'No Title' }}</p>
                    <p class="text-sm text-gray-600 line-clamp-2 mt-1">{{ previews.channel_1.description || 'No description found' }}</p>
                    <span class="mt-2 inline-block px-2 py-0.5 bg-blue-100 text-blue-700 rounded text-xs font-medium">
                      {{ previews.channel_1.platform || 'General URL' }}
                    </span>
                  </div>
                </div>
              </div>

              <!-- Channel 2 -->
              <div>
                <label for="channel2" class="block text-sm font-medium text-gray-700 mb-2">
                  Channel 2 URL
                </label>
                <div class="flex gap-2">
                  <input
                    id="channel2"
                    v-model="channels.channel_2_url"
                    type="url"
                    class="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="https://www.youtube.com/watch?v=..."
                  />
                  <button
                    type="button"
                    @click="fetchMetadata('channel_2')"
                    class="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 text-sm font-medium whitespace-nowrap"
                    :disabled="fetchingMetadata['channel_2']"
                  >
                    {{ fetchingMetadata['channel_2'] ? 'Fetching...' : 'Preview' }}
                  </button>
                </div>
                <!-- Preview Card 2 -->
                <div v-if="previews.channel_2" class="mt-3 p-4 bg-gray-50 rounded-lg border border-gray-200 flex gap-4">
                  <img v-if="previews.channel_2.image" :src="previews.channel_2.image" class="w-20 h-20 object-cover rounded shadow-sm" alt="Preview" />
                  <div class="flex-1 min-w-0">
                    <p class="font-bold text-gray-900 truncate">{{ previews.channel_2.title || 'No Title' }}</p>
                    <p class="text-sm text-gray-600 line-clamp-2 mt-1">{{ previews.channel_2.description || 'No description found' }}</p>
                    <span class="mt-2 inline-block px-2 py-0.5 bg-red-100 text-red-700 rounded text-xs font-medium">
                      {{ previews.channel_2.platform || 'General URL' }}
                    </span>
                  </div>
                </div>
              </div>

              <!-- Channel 3 -->
              <div>
                <label for="channel3" class="block text-sm font-medium text-gray-700 mb-2">
                  Channel 3 URL
                </label>
                <div class="flex gap-2">
                  <input
                    id="channel3"
                    v-model="channels.channel_3_url"
                    type="url"
                    class="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="https://twitter.com/..."
                  />
                  <button
                    type="button"
                    @click="fetchMetadata('channel_3')"
                    class="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 text-sm font-medium whitespace-nowrap"
                    :disabled="fetchingMetadata['channel_3']"
                  >
                    {{ fetchingMetadata['channel_3'] ? 'Fetching...' : 'Preview' }}
                  </button>
                </div>
                <!-- Preview Card 3 -->
                <div v-if="previews.channel_3" class="mt-3 p-4 bg-gray-50 rounded-lg border border-gray-200 flex gap-4">
                  <img v-if="previews.channel_3.image" :src="previews.channel_3.image" class="w-20 h-20 object-cover rounded shadow-sm" alt="Preview" />
                  <div class="flex-1 min-w-0">
                    <p class="font-bold text-gray-900 truncate">{{ previews.channel_3.title || 'No Title' }}</p>
                    <p class="text-sm text-gray-600 line-clamp-2 mt-1">{{ previews.channel_3.description || 'No description found' }}</p>
                    <span class="mt-2 inline-block px-2 py-0.5 bg-sky-100 text-sky-700 rounded text-xs font-medium">
                      {{ previews.channel_3.platform || 'General URL' }}
                    </span>
                  </div>
                </div>
              </div>

              <!-- Channel 4 -->
              <div>
                <label for="channel4" class="block text-sm font-medium text-gray-700 mb-2">
                  Channel 4 URL
                </label>
                <div class="flex gap-2">
                  <input
                    id="channel4"
                    v-model="channels.channel_4_url"
                    type="url"
                    class="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="https://www.facebook.com/..."
                  />
                  <button
                    type="button"
                    @click="fetchMetadata('channel_4')"
                    class="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 text-sm font-medium whitespace-nowrap"
                    :disabled="fetchingMetadata['channel_4']"
                  >
                    {{ fetchingMetadata['channel_4'] ? 'Fetching...' : 'Preview' }}
                  </button>
                </div>
                <!-- Preview Card 4 -->
                <div v-if="previews.channel_4" class="mt-3 p-4 bg-gray-50 rounded-lg border border-gray-200 flex gap-4">
                  <img v-if="previews.channel_4.image" :src="previews.channel_4.image" class="w-20 h-20 object-cover rounded shadow-sm" alt="Preview" />
                  <div class="flex-1 min-w-0">
                    <p class="font-bold text-gray-900 truncate">{{ previews.channel_4.title || 'No Title' }}</p>
                    <p class="text-sm text-gray-600 line-clamp-2 mt-1">{{ previews.channel_4.description || 'No description found' }}</p>
                    <span class="mt-2 inline-block px-2 py-0.5 bg-indigo-100 text-indigo-700 rounded text-xs font-medium">
                      {{ previews.channel_4.platform || 'General URL' }}
                    </span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Actions -->
            <div class="mt-8 flex justify-end gap-4">
              <button
                type="button"
                @click="loadChannels"
                class="px-6 py-3 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 font-medium"
                :disabled="channelsSaving"
              >
                Reset
              </button>
              <button
                type="submit"
                class="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium disabled:opacity-50 disabled:cursor-not-allowed"
                :disabled="channelsSaving"
              >
                {{ channelsSaving ? 'Saving...' : 'Save Changes' }}
              </button>
            </div>
          </form>

          <!-- Last Updated -->
          <div v-if="channels.updated_at" class="mt-6 pt-6 border-t border-gray-200">
            <p class="text-sm text-gray-500">
              Last updated: {{ formatDate(channels.updated_at) }}
            </p>
          </div>
        </div>
      </div>

      <!-- Contact Information Tab -->
      <div v-if="activeTab === 'contact'">
        <!-- Loading State -->
        <div v-if="contactLoading" class="flex items-center justify-center py-12">
          <div class="text-center">
            <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
            <p class="text-gray-600">Loading contact information...</p>
          </div>
        </div>

        <!-- Form -->
        <div v-else class="bg-white rounded-lg shadow-sm p-8">
          <div class="mb-6">
            <h2 class="text-xl font-bold text-gray-900 mb-2">Contact Information</h2>
            <p class="text-gray-600 text-sm">
              Update contact details that appear in the footer and contact pages across your website
            </p>
          </div>

          <form @submit.prevent="saveContact">
            <div class="space-y-8">
              <!-- Email Addresses Section -->
              <div class="border-b border-gray-200 pb-6">
                <h3 class="text-lg font-semibold text-gray-900 mb-4">Email Addresses</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label for="primary_email" class="block text-sm font-medium text-gray-700 mb-2">
                      Primary Email
                    </label>
                    <input
                      id="primary_email"
                      v-model="contact.primary_email"
                      type="email"
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="info@sauti.org"
                    />
                  </div>
                  <div>
                    <label for="support_email" class="block text-sm font-medium text-gray-700 mb-2">
                      Support Email
                    </label>
                    <input
                      id="support_email"
                      v-model="contact.support_email"
                      type="email"
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="support@sauti.org"
                    />
                  </div>
                </div>
              </div>

              <!-- Phone Numbers Section -->
              <div class="border-b border-gray-200 pb-6">
                <h3 class="text-lg font-semibold text-gray-900 mb-4">Phone Numbers</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label for="primary_phone" class="block text-sm font-medium text-gray-700 mb-2">
                      Primary Phone
                    </label>
                    <input
                      id="primary_phone"
                      v-model="contact.primary_phone"
                      type="text"
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="+256 116 or 116"
                    />
                  </div>
                  <div>
                    <label for="whatsapp_number" class="block text-sm font-medium text-gray-700 mb-2">
                      WhatsApp Number
                    </label>
                    <input
                      id="whatsapp_number"
                      v-model="contact.whatsapp_number"
                      type="text"
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="+256 123 456 789"
                    />
                  </div>
                </div>
              </div>

              <!-- Address & Hours Section -->
              <div class="border-b border-gray-200 pb-6">
                <h3 class="text-lg font-semibold text-gray-900 mb-4">Office Details</h3>
                <div class="space-y-6">
                  <div>
                    <label for="office_address" class="block text-sm font-medium text-gray-700 mb-2">
                      Office Address
                    </label>
                    <textarea
                      id="office_address"
                      v-model="contact.office_address"
                      rows="3"
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="Enter physical office address"
                    ></textarea>
                  </div>
                  <div>
                    <label for="working_hours" class="block text-sm font-medium text-gray-700 mb-2">
                      Working Hours
                    </label>
                    <input
                      id="working_hours"
                      v-model="contact.working_hours"
                      type="text"
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="24/7 or Mon-Fri 8AM-5PM"
                    />
                  </div>
                </div>
              </div>

              <!-- Social Media Links Section -->
              <div>
                <h3 class="text-lg font-semibold text-gray-900 mb-1">Official Organization Profiles</h3>
                <p class="text-sm text-gray-500 mb-6 italic">
                  These links are the authoritative "Source of Truth" for the organization's social media presence across the entire website.
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label for="facebook_url" class="block text-sm font-medium text-gray-700 mb-2">
                      Facebook Page URL
                    </label>
                    <input
                      id="facebook_url"
                      v-model="contact.facebook_url"
                      type="url"
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="https://facebook.com/sauti116"
                    />
                  </div>
                  <div>
                    <label for="twitter_url" class="block text-sm font-medium text-gray-700 mb-2">
                      Twitter/X Profile URL
                    </label>
                    <input
                      id="twitter_url"
                      v-model="contact.twitter_url"
                      type="url"
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="https://twitter.com/sauti116"
                    />
                  </div>
                  <div>
                    <label for="instagram_url" class="block text-sm font-medium text-gray-700 mb-2">
                      Instagram Profile URL
                    </label>
                    <input
                      id="instagram_url"
                      v-model="contact.instagram_url"
                      type="url"
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="https://instagram.com/sauti116"
                    />
                  </div>
                  <div>
                    <label for="linkedin_url" class="block text-sm font-medium text-gray-700 mb-2">
                      LinkedIn Page URL
                    </label>
                    <input
                      id="linkedin_url"
                      v-model="contact.linkedin_url"
                      type="url"
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="https://linkedin.com/company/sauti116"
                    />
                  </div>
                  <div>
                    <label for="youtube_url" class="block text-sm font-medium text-gray-700 mb-2">
                      YouTube Channel URL
                    </label>
                    <input
                      id="youtube_url"
                      v-model="contact.youtube_url"
                      type="url"
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="https://youtube.com/@sauti116"
                    />
                  </div>
                  <div>
                    <label for="tiktok_url" class="block text-sm font-medium text-gray-700 mb-2">
                      TikTok Profile URL
                    </label>
                    <input
                      id="tiktok_url"
                      v-model="contact.tiktok_url"
                      type="url"
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="https://tiktok.com/@sauti116"
                    />
                  </div>
                  <div>
                    <label for="ureport_url" class="block text-sm font-medium text-gray-700 mb-2">
                      U-Report URL
                    </label>
                    <input
                      id="ureport_url"
                      v-model="contact.social_ureport"
                      type="url"
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="https://ureport.ug/..."
                    />
                  </div>
                  <div>
                    <label for="safepal_url" class="block text-sm font-medium text-gray-700 mb-2">
                      SafePal URL
                    </label>
                    <input
                      id="safepal_url"
                      v-model="contact.social_safepal"
                      type="url"
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="https://safepal.co/..."
                    />
                  </div>
                </div>
              </div>
            </div>

            <!-- Actions -->
            <div class="mt-8 flex justify-end gap-4">
              <button
                type="button"
                @click="loadContact"
                class="px-6 py-3 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 font-medium"
                :disabled="contactSaving"
              >
                Reset
              </button>
              <button
                type="submit"
                class="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium disabled:opacity-50 disabled:cursor-not-allowed"
                :disabled="contactSaving"
              >
                {{ contactSaving ? 'Saving...' : 'Save Changes' }}
              </button>
            </div>
          </form>

          <!-- Last Updated -->
          <div v-if="contact.updated_at" class="mt-6 pt-6 border-t border-gray-200">
            <p class="text-sm text-gray-500">
              Last updated: {{ formatDate(contact.updated_at) }}
            </p>
          </div>
          </div>
        </div>

        <!-- Additional Contacts Tab -->
        <div v-if="activeTab === 'additional'" class="p-8">
          <div class="mb-8">
            <h2 class="text-xl font-bold text-gray-900 mb-2">Extended Contact Registry</h2>
            <p class="text-gray-600 text-sm">
              Manage additional contact items such as regional offices, specific department emails, or secondary phone lines.
            </p>
          </div>
          <ContactItemList />
        </div>
      </div>
    </div>
  </template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'
import { 
  MagnifyingGlassIcon, 
  ArrowTopRightOnSquareIcon,
  InformationCircleIcon,
  GlobeAltIcon,
  PhoneIcon,
  EnvelopeIcon,
  ShareIcon
} from '@heroicons/vue/24/outline'
import { api } from '@/utils/api'
import ContactItemList from '@/components/contacts/ContactItemList.vue'

const toast = useToast()
const route = useRoute()
const router = useRouter()
const activeTab = ref(route.query.tab || 'channels')

watch(activeTab, (newTab) => {
  router.replace({ 
    query: { ...route.query, tab: newTab } 
  })
})

// Channels state
const channelsLoading = ref(true)
const channelsSaving = ref(false)
const channels = ref({
  channel_1_url: '',
  channel_2_url: '',
  channel_3_url: '',
  channel_4_url: '',
  updated_at: null
})

// Metadata fetching state
const fetchingMetadata = ref({
  channel_1: false,
  channel_2: false,
  channel_3: false,
  channel_4: false
})
const previews = ref({
  channel_1: null,
  channel_2: null,
  channel_3: null,
  channel_4: null
})

// Contact state
const contactLoading = ref(true)
const contactSaving = ref(false)
const contact = ref({
  primary_email: '',
  support_email: '',
  primary_phone: '',
  whatsapp_number: '',
  office_address: '',
  facebook_url: '',
  twitter_url: '',
  instagram_url: '',
  linkedin_url: '',
  youtube_url: '',
  tiktok_url: '',
  working_hours: '',
  updated_at: null
})

const loadChannels = async () => {
  channelsLoading.value = true
  try {
    const response = await api.socialMedia.channels.get()
    channels.value = response.data
  } catch (error) {
    console.error('Failed to load channels:', error)
    toast.error('Failed to load social media channels')
  } finally {
    channelsLoading.value = false
  }
}

const fetchMetadata = async (channelKey) => {
  const url = channels.value[`${channelKey}_url`]
  if (!url) {
    toast.warning('Please enter a URL first')
    return
  }

  fetchingMetadata.value[channelKey] = true
  previews.value[channelKey] = null
  
  try {
    const response = await api.socialMedia.fetchMetadata(url)
    previews.value[channelKey] = response.data
    toast.success('Metadata fetched successfully!')
  } catch (error) {
    console.error('Failed to fetch metadata:', error)
    toast.error(error.response?.data?.error || 'Failed to fetch metadata. The URL might be private or blocked.')
  } finally {
    fetchingMetadata.value[channelKey] = false
  }
}

const saveChannels = async () => {
  channelsSaving.value = true
  try {
    const response = await api.socialMedia.channels.update({
      channel_1_url: channels.value.channel_1_url || null,
      channel_2_url: channels.value.channel_2_url || null,
      channel_3_url: channels.value.channel_3_url || null,
      channel_4_url: channels.value.channel_4_url || null
    })
    channels.value = response.data
    toast.success('Social media channels updated successfully!')
  } catch (error) {
    console.error('Failed to save channels:', error)
    toast.error('Failed to save social media channels')
  } finally {
    channelsSaving.value = false
  }
}

const loadContact = async () => {
  contactLoading.value = true
  try {
    // Shifting to GlobalSettings as the authoritative source
    const response = await api.siteSettings.get()
    const gs = response.data
    
    // Map GlobalSettings fields to the local contact reactive object
    contact.value = {
      primary_email: gs.contact_email_info || '',
      support_email: gs.contact_email_sautichl || '',
      primary_phone: gs.contact_phone_main || '',
      whatsapp_number: gs.social_whatsapp || '',
      office_address: gs.office_address || '',
      working_hours: gs.operating_hours_text || '',
      facebook_url: gs.social_facebook || '',
      twitter_url: gs.social_twitter || '',
      instagram_url: gs.social_instagram || '',
      linkedin_url: gs.social_linkedin || '',
      youtube_url: gs.social_youtube || '',
      tiktok_url: gs.social_tiktok || '',
      social_ureport: gs.social_ureport || '',
      social_safepal: gs.social_safepal || '',
      updated_at: gs.updated_at || gs.last_updated
    }
  } catch (error) {
    console.error('Failed to load authoritative contact information:', error)
    toast.error('Failed to load contact information')
  } finally {
    contactLoading.value = false
  }
}

const saveContact = async () => {
  contactSaving.value = true
  try {
    // Map local state back to GlobalSettings schema
    const payload = {
      contact_email_info: contact.value.primary_email || null,
      contact_email_sautichl: contact.value.support_email || null,
      contact_phone_main: contact.value.primary_phone || null,
      social_whatsapp: contact.value.whatsapp_number || null,
      office_address: contact.value.office_address || null,
      operating_hours_text: contact.value.working_hours || null,
      social_facebook: contact.value.facebook_url || null,
      social_twitter: contact.value.twitter_url || null,
      social_instagram: contact.value.instagram_url || null,
      social_linkedin: contact.value.linkedin_url || null,
      social_youtube: contact.value.youtube_url || null,
      social_tiktok: contact.value.tiktok_url || null,
      social_ureport: contact.value.social_ureport || null,
      social_safepal: contact.value.social_safepal || null
    }

    await api.siteSettings.update(payload)
    toast.success('Authoritative settings updated successfully!')
    await loadContact()
  } catch (error) {
    console.error('Failed to save authoritative settings:', error)
    toast.error('Failed to save settings')
  } finally {
    contactSaving.value = false
  }
}

const formatDate = (dateString) => {
  if (!dateString) return 'Never'
  const date = new Date(dateString)
  return date.toLocaleString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

onMounted(async () => {
  await Promise.all([loadChannels(), loadContact()])
})
</script>

<style scoped>
.social-media-view {
  padding: 2rem;
}
</style>
