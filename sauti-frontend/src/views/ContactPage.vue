<template>
  <div class="py-16 md:py-24 bg-sauti-neutral min-h-screen">
    <div class="container-custom">
      <!-- Header -->
      <div class="text-center mb-16 max-w-4xl mx-auto">
        <h1 class="text-4xl md:text-5xl lg:text-7xl font-black text-sauti-darkGreen mb-6 tracking-tight">{{
          settingsStore.settings.contact_title || 'Contact Us' }}</h1>
        <p class="text-xl md:text-2xl text-sauti-darkGreen/70 leading-relaxed font-bold">{{
          settingsStore.settings.contact_subtitle || "We're here to help 24/7. Reach out to us anytime." }}</p>
      </div>

      <div v-if="loading" class="text-center py-20">
        <div class="spinner border-t-blue-600 mx-auto"></div>
      </div>

      <div v-else class="space-y-16">
        <!-- 1. Urgent / Hotline Section (Dominant) -->
        <section aria-labelledby="hotline-heading" v-if="hotlines.length > 0">
          <div class="grid gap-8 max-w-5xl mx-auto">
            <div v-for="contact in hotlines" :key="contact.id"
              class="relative bg-sauti-white border-[6px] border-sauti-red rounded-[3rem] p-8 md:p-16 text-center transform hover:scale-[1.01] transition-all duration-500 shadow-2xl group overflow-hidden">

              <!-- Decorative background element -->
              <div
                class="absolute top-0 right-0 -mt-12 -mr-12 w-48 h-48 bg-sauti-red/5 rounded-full blur-3xl group-hover:bg-sauti-red/10 transition-colors">
              </div>

              <div class="relative z-10">
                <div
                  class="w-24 h-24 bg-sauti-neutral rounded-3xl flex items-center justify-center mx-auto mb-8 shadow-inner group-hover:scale-110 transition-transform duration-500">
                  <svg class="w-12 h-12 text-sauti-red" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                    <path
                      d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z" />
                  </svg>
                </div>

                <h2 id="hotline-heading" class="text-sauti-red font-black tracking-[0.3em] text-sm uppercase mb-4">
                  Emergency Hotline</h2>
                <h3 class="text-3xl font-black text-sauti-darkGreen mb-4">{{ contact.name }}</h3>

                <a :href="'tel:' + contact.value"
                  class="block text-6xl md:text-9xl font-black text-sauti-red tracking-tighter hover:text-sauti-darkGreen transition-colors py-4 focus:outline-none focus:ring-8 focus:ring-sauti-red/10 rounded-3xl"
                  aria-label="Call 116">
                  {{ contact.value }}
                </a>

                <p class="text-xl text-sauti-darkGreen font-bold mt-8 max-w-xl mx-auto opacity-80">{{
                  contact.description }}</p>
                <div class="mt-12">
                  <span
                    class="inline-flex items-center gap-3 px-8 py-4 bg-sauti-red text-sauti-white rounded-2xl text-lg font-black shadow-xl shadow-sauti-red/20 transform hover:-translate-y-1 transition-transform">
                    <span class="relative flex h-4 w-4">
                      <span
                        class="animate-ping absolute inline-flex h-full w-full rounded-full bg-sauti-white opacity-75"></span>
                      <span class="relative inline-flex rounded-full h-4 w-4 bg-sauti-white"></span>
                    </span>
                    24/7 TOLL FREE
                  </span>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- 2. Support Channels (Grid) -->
        <section aria-labelledby="support-heading" v-if="supportChannels.length > 0">
          <div class="max-w-6xl mx-auto">
            <h2 id="support-heading" class="text-3xl font-black text-sauti-darkGreen mb-10 text-center">Digital Support
              Channels</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              <div v-for="contact in supportChannels" :key="contact.id"
                class="group flex flex-col items-center p-10 bg-sauti-white border-2 border-sauti-neutral rounded-[2.5rem] hover:border-sauti-blue hover:shadow-2xl transition-all duration-500">

                <div :class="{
                  'bg-sauti-blue/10 text-sauti-blue': contact.type === 'email' || contact.icon === 'facebook' || contact.icon === 'twitter',
                  'bg-sauti-lightGreen/10 text-sauti-lightGreen': contact.icon === 'whatsapp'
                }"
                  class="w-20 h-20 rounded-2xl flex items-center justify-center mb-8 group-hover:rotate-6 transition-all duration-500 shadow-sm">
                  <!-- Icons -->
                  <svg v-if="contact.icon === 'whatsapp'" class="w-10 h-10" fill="currentColor" viewBox="0 0 24 24"
                    aria-hidden="true">
                    <path
                      d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" />
                  </svg>
                  <svg v-else-if="contact.icon === 'envelope'" class="w-10 h-10" fill="currentColor" viewBox="0 0 20 20"
                    aria-hidden="true">
                    <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
                    <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
                  </svg>
                  <svg v-else-if="contact.icon === 'facebook'" class="w-10 h-10" fill="currentColor" viewBox="0 0 24 24"
                    aria-hidden="true">
                    <path
                      d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z" />
                  </svg>
                  <svg v-else-if="contact.icon === 'twitter'" class="w-10 h-10" fill="currentColor" viewBox="0 0 24 24"
                    aria-hidden="true">
                    <path
                      d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z" />
                  </svg>
                  <svg v-else class="w-10 h-10 text-sauti-darkGreen/40" fill="currentColor" viewBox="0 0 24 24"
                    aria-hidden="true">
                    <path
                      d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17h2v-2h-2v2zm2-10H11V5h2v4z" />
                  </svg>
                </div>

                <h3 class="text-2xl font-black text-sauti-darkGreen mb-4">{{ contact.name }}</h3>
                <p
                  class="text-sauti-darkGreen/70 mb-8 h-12 line-clamp-2 text-center text-sm px-6 font-medium leading-relaxed">
                  {{ contact.description }}</p>

                <a v-if="contact.type === 'email'" :href="'mailto:' + contact.value"
                  class="btn btn-outline w-full text-center">
                  Email Us
                </a>
                <a v-else-if="contact.type === 'social'" :href="contact.value" target="_blank"
                  class="btn btn-outline w-full text-center">
                  {{ contact.icon === 'whatsapp' ? 'Start Chat' : 'Visit Profile' }}
                </a>
                <p v-else class="font-black text-sauti-blue text-lg">{{ contact.value }}</p>
              </div>
            </div>
          </div>
        </section>

        <!-- 3. Location / Office & Miscellaneous -->
        <section aria-labelledby="office-heading" v-if="locationContacts.length > 0 || otherContacts.length > 0">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto">
            <!-- Locations -->
            <div v-for="contact in locationContacts" :key="contact.id"
              class="flex flex-col md:flex-row items-center md:items-start text-center md:text-left gap-8 p-10 bg-sauti-white rounded-[3rem] border-2 border-sauti-neutral shadow-sm">
              <div
                class="w-16 h-16 bg-sauti-blue/10 rounded-2xl flex items-center justify-center flex-shrink-0 text-sauti-blue shadow-inner">
                <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                  <path fill-rule="evenodd"
                    d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z"
                    clip-rule="evenodd" />
                </svg>
              </div>
              <div>
                <h3 class="text-2xl font-black text-sauti-darkGreen mb-3">{{ contact.name }}</h3>
                <p class="text-sauti-darkGreen font-black text-xl mb-2">{{ contact.value }}</p>
                <p class="text-sauti-darkGreen/60 text-base font-bold leading-relaxed">{{ contact.description }}</p>
              </div>
            </div>

            <!-- Others/Fallback -->
            <div v-for="contact in otherContacts" :key="contact.id"
              class="flex flex-col md:flex-row items-center md:items-start text-center md:text-left gap-8 p-10 bg-sauti-white rounded-[3rem] border-2 border-sauti-neutral shadow-sm">
              <div
                class="w-16 h-16 bg-sauti-neutral/30 rounded-2xl flex items-center justify-center flex-shrink-0 text-sauti-darkGreen/40">
                <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                  <path
                    d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17h2v-2h-2v2zm2-10H11V5h2v4z" />
                </svg>
              </div>
              <div>
                <h3 class="text-2xl font-black text-sauti-darkGreen mb-3">{{ contact.name }}</h3>
                <p class="text-sauti-darkGreen font-black mb-2 text-xl">{{ contact.value }}</p>
                <p class="text-sauti-darkGreen/60 text-base font-bold leading-relaxed">{{ contact.description }}</p>
              </div>
            </div>
          </div>
        </section>

        <!-- 4. Feedback Form (Visual separation) -->
        <section aria-labelledby="feedback-heading">
          <div class="mt-16 max-w-4xl mx-auto">
            <div
              class="bg-sauti-white rounded-[3.5rem] border border-sauti-neutral overflow-hidden relative shadow-2xl">

              <!-- Brand accent -->
              <div class="h-3 w-full bg-sauti-blue"></div>

              <div class="p-8 md:p-16">
                <div class="text-center mb-12">
                  <div
                    class="inline-flex items-center justify-center w-16 h-16 bg-sauti-neutral rounded-2xl text-sauti-blue mb-6 shadow-inner">
                    <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                    </svg>
                  </div>
                  <h2 id="feedback-heading" class="text-3xl font-black text-sauti-darkGreen mb-3">General Feedback</h2>
                  <p class="text-sauti-darkGreen/60 font-bold text-lg">For non-emergency inquiries and website
                    suggestions</p>
                </div>

                <div class="bg-sauti-neutral border-l-8 border-sauti-blue p-8 rounded-r-3xl mb-12 shadow-sm">
                  <div class="flex items-start">
                    <div class="flex-shrink-0 mt-1">
                      <svg class="h-7 w-7 text-sauti-blue" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                        <path fill-rule="evenodd"
                          d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
                          clip-rule="evenodd" />
                      </svg>
                    </div>
                    <div class="ml-6">
                      <p class="text-sauti-darkGreen font-medium leading-relaxed">
                        <span class="font-black text-xl text-sauti-darkGreen block mb-2">Notice: Personal Privacy</span>
                        Do NOT use this form for reporting abuse. If you need immediate help, please call <span
                          class="font-black text-sauti-red underline">116</span> or use the <router-link to="/report"
                          class="btn btn-info inline-flex py-1 px-4 text-xs ml-2">Report Case</router-link> page.
                      </p>
                    </div>
                  </div>
                </div>

                <form v-if="!feedbackSubmitted" @submit.prevent="submitFeedback" class="space-y-8">
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div>
                      <label class="block text-sauti-darkGreen text-sm font-black uppercase tracking-widest mb-3 ml-2"
                        for="name">Name (Optional)</label>
                      <input v-model="feedbackForm.name"
                        class="form-input bg-sauti-neutral border-2 border-sauti-neutral focus:bg-sauti-white focus:border-sauti-blue py-4 px-6 rounded-2xl font-bold"
                        id="name" type="text" placeholder="Your Name">
                    </div>
                    <div>
                      <label class="block text-sauti-darkGreen text-sm font-black uppercase tracking-widest mb-3 ml-2"
                        for="email">Email (Optional)</label>
                      <input v-model="feedbackForm.email"
                        class="form-input bg-sauti-neutral border-2 border-sauti-neutral focus:bg-sauti-white focus:border-sauti-blue py-4 px-6 rounded-2xl font-bold"
                        id="email" type="email" placeholder="email@example.com">
                    </div>
                  </div>

                  <div>
                    <label class="block text-sauti-darkGreen text-sm font-black uppercase tracking-widest mb-3 ml-2"
                      for="message">Message <span class="text-sauti-red">*</span></label>
                    <textarea v-model="feedbackForm.message" required
                      class="form-input bg-sauti-neutral border-2 border-sauti-neutral focus:bg-sauti-white focus:border-sauti-blue py-4 px-6 rounded-2xl font-bold h-48 resize-none"
                      id="message" placeholder="How can we improve our services?"></textarea>
                  </div>

                  <div class="flex items-center justify-end">
                    <button :disabled="feedbackSubmitting" class="btn btn-info w-full md:w-auto px-12 py-4 text-lg"
                      type="submit">
                      {{ feedbackSubmitting ? 'Sending...' : 'Send Message' }}
                    </button>
                  </div>
                  <p v-if="feedbackError"
                    class="text-sauti-red font-black text-sm mt-6 text-center bg-sauti-red/5 py-4 rounded-2xl border border-sauti-red/20"
                    role="alert">{{ feedbackError }}</p>
                </form>

                <div v-else
                  class="text-center py-16 bg-sauti-lightGreen/10 rounded-[2.5rem] border-2 border-sauti-lightGreen/20">
                  <div
                    class="w-20 h-20 bg-sauti-lightGreen rounded-3xl flex items-center justify-center mx-auto mb-6 shadow-xl shadow-sauti-lightGreen/20">
                    <svg class="h-10 w-10 text-sauti-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                  <h3 class="text-3xl font-black text-sauti-darkGreen mb-4">Message Sent!</h3>
                  <p class="text-sauti-darkGreen font-bold mb-10 max-w-md mx-auto opacity-70">Thank you for your
                    feedback. We review all messages to improve our service.</p>
                  <button @click="resetFeedbackForm" class="btn btn-outline">Send another message</button>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { computed, onMounted, ref, reactive } from 'vue'
  import { useSettingsStore } from '@/store/settings'
  import { api } from '@/utils/axios'

  defineOptions({
    name: 'ContactPage'
  })

  const settingsStore = useSettingsStore()

  const contacts = ref([])
  const loading = ref(true)

  // Feedback Form State
  const feedbackForm = reactive({
    name: '',
    email: '',
    message: ''
  })
  const feedbackSubmitting = ref(false)
  const feedbackSubmitted = ref(false)
  const feedbackError = ref('')

  const fetchContacts = async () => {
    loading.value = true
    try {
      const response = await api.get('/content/contacts/')
      contacts.value = response.data
    } catch (error) {
      console.error('Error fetching contact items:', error)
      contacts.value = []
    } finally {
      loading.value = false
    }
  }

  const submitFeedback = async () => {
    if (!feedbackForm.message.trim()) return

    feedbackSubmitting.value = true
    feedbackError.value = ''

    try {
      await api.post('/contact/feedback/', feedbackForm)
      feedbackSubmitted.value = true
      feedbackForm.name = ''
      feedbackForm.email = ''
      feedbackForm.message = ''
    } catch (err) {
      console.error('Feedback submission error:', err)
      feedbackError.value = 'Failed to send message. Please try again or use the email above.'
    } finally {
      feedbackSubmitting.value = false
    }
  }

  const resetFeedbackForm = () => {
    feedbackSubmitted.value = false
    feedbackError.value = ''
  }

  onMounted(() => {
    settingsStore.fetchGlobalSettings()
    fetchContacts()
  })

  // Organization Computeds
  const hotlines = computed(() => {
    return contacts.value.filter(c => c.type === 'phone' || c.icon === 'phone')
  })

  const supportChannels = computed(() => {
    // Exclude phone to prevent duplication if type is ambiguous
    return contacts.value.filter(c => (c.type === 'email' || c.type === 'social') && c.type !== 'phone')
  })

  const locationContacts = computed(() => {
    return contacts.value.filter(c => c.type === 'location')
  })

  const otherContacts = computed(() => {
    return contacts.value.filter(c => !['phone', 'email', 'social', 'location'].includes(c.type))
  })
</script>