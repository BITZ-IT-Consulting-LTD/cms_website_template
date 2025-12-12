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
              Social Media Channels
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
              Contact Information
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
                <input
                  id="channel1"
                  v-model="channels.channel_1_url"
                  type="url"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="https://www.tiktok.com/@sauti116/video/..."
                />
                <p class="mt-1 text-sm text-gray-500">
                  Paste your TikTok, YouTube, Twitter, Facebook, or Instagram post URL
                </p>
              </div>

              <!-- Channel 2 -->
              <div>
                <label for="channel2" class="block text-sm font-medium text-gray-700 mb-2">
                  Channel 2 URL
                </label>
                <input
                  id="channel2"
                  v-model="channels.channel_2_url"
                  type="url"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="https://www.youtube.com/watch?v=..."
                />
              </div>

              <!-- Channel 3 -->
              <div>
                <label for="channel3" class="block text-sm font-medium text-gray-700 mb-2">
                  Channel 3 URL
                </label>
                <input
                  id="channel3"
                  v-model="channels.channel_3_url"
                  type="url"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="https://twitter.com/sauti116/status/..."
                />
              </div>

              <!-- Channel 4 -->
              <div>
                <label for="channel4" class="block text-sm font-medium text-gray-700 mb-2">
                  Channel 4 URL
                </label>
                <input
                  id="channel4"
                  v-model="channels.channel_4_url"
                  type="url"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="https://www.facebook.com/sauti116/posts/..."
                />
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
                <h3 class="text-lg font-semibold text-gray-900 mb-4">Social Media Links</h3>
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
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { api } from '@/utils/api'
import { useToast } from 'vue-toastification'

const toast = useToast()
const activeTab = ref('channels')

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
    const response = await api.socialMedia.contact.get()
    contact.value = response.data
  } catch (error) {
    console.error('Failed to load contact information:', error)
    toast.error('Failed to load contact information')
  } finally {
    contactLoading.value = false
  }
}

const saveContact = async () => {
  contactSaving.value = true
  try {
    const response = await api.socialMedia.contact.update({
      primary_email: contact.value.primary_email || null,
      support_email: contact.value.support_email || null,
      primary_phone: contact.value.primary_phone || null,
      whatsapp_number: contact.value.whatsapp_number || null,
      office_address: contact.value.office_address || null,
      facebook_url: contact.value.facebook_url || null,
      twitter_url: contact.value.twitter_url || null,
      instagram_url: contact.value.instagram_url || null,
      linkedin_url: contact.value.linkedin_url || null,
      youtube_url: contact.value.youtube_url || null,
      tiktok_url: contact.value.tiktok_url || null,
      working_hours: contact.value.working_hours || null
    })
    contact.value = response.data
    toast.success('Contact information updated successfully!')
  } catch (error) {
    console.error('Failed to save contact information:', error)
    toast.error('Failed to save contact information')
  } finally {
    contactSaving.value = false
  }
}

const formatDate = (dateString) => {
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
