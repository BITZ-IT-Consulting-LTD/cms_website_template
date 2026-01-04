<template>
  <div class="bg-sauti-neutral min-h-screen font-sans text-sauti-darkGreen">
    <!-- 1. EMERGENCY HERO SECTION -->
    <!-- Goal: Immediate action for distressed users. High contrast, zero confusion. -->
    <header class="bg-white border-b border-sauti-blue/10 pt-8 pb-12 md:py-20">
      <div class="container-custom max-w-4xl mx-auto text-center px-6">
        <!-- Trust Signal -->
        <div class="inline-flex items-center gap-2 mb-6 opacity-80">
          <div class="w-2 h-2 rounded-full bg-sauti-green animate-pulse"></div>
          <span class="text-xs font-bold uppercase tracking-widest text-sauti-darkGreen">Official Government Helpline •
            24/7 Confidential Support</span>
        </div>

        <!-- Headline -->
        <h1 class="font-sans font-bold text-4xl md:text-6xl mb-6 text-sauti-darkGreen leading-tight tracking-tight">
          In danger or need help?
        </h1>

        <p class="text-lg md:text-xl text-sauti-darkGreen/70 mb-10 max-w-2xl mx-auto font-normal leading-relaxed">
          Our trained counselors are ready to listen and support you. The call is free, private, and does not show on
          your phone bill.
        </p>

        <!-- Primary Emergency CTA -->
        <div class="flex flex-col items-center">
          <a href="tel:116"
            class="group relative inline-flex items-center justify-center gap-4 bg-sauti-red text-white py-6 px-12 md:px-16 rounded-full transition-transform duration-200 active:scale-95 focus:outline-none focus:ring-4 focus:ring-sauti-red/30 shadow-lg hover:shadow-xl w-full md:w-auto">
            <span class="sr-only">Call Emergency Helpline</span>
            <PhoneIcon class="w-8 h-8 md:w-10 md:h-10 text-white fill-current" />
            <span class="font-sans font-bold text-4xl md:text-5xl tracking-tighter">CALL 116</span>
            <span
              class="absolute -top-3 right-8 bg-sauti-yellow text-sauti-darkGreen text-[10px] font-bold uppercase px-2 py-1 rounded shadow-sm transform rotate-2">Toll
              Free</span>
          </a>
          <p class="mt-4 text-sm font-bold text-sauti-darkGreen/50">Available 24 hours a day, 7 days a week.</p>
        </div>
      </div>
    </header>

    <div class="container-custom py-16 md:py-24">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-20 max-w-7xl mx-auto">

        <!-- 2. CONTACT OPTIONS (Left Column) -->
        <div class="lg:col-span-7 space-y-12">

          <!-- Section Title -->
          <div>
            <h2 class="font-sans font-bold text-3xl mb-2 text-sauti-darkGreen">Support Channels</h2>
            <p class="text-sauti-darkGreen/70 font-normal">Choose the way you feel most comfortable reaching us.</p>
          </div>

          <!-- Cards Layout -->
          <div class="grid gap-4 md:grid-cols-2">
            <!-- Dynamic Contacts -->
            <a v-for="contact in nonEmergencyContacts" :key="contact.id" :href="getLink(contact)"
              :target="contact.type === 'location' ? '_blank' : '_self'"
              class="bg-white p-8 rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 group flex flex-col items-start relative overflow-hidden cursor-pointer">

              <!-- Hover Accent -->
              <div
                class="absolute top-0 left-0 w-1 h-full bg-sauti-blue opacity-0 group-hover:opacity-100 transition-opacity">
              </div>

              <div class="mb-6 p-4 rounded-xl bg-sauti-neutral group-hover:bg-sauti-blue/10 transition-colors">
                <component :is="getIcon(contact)" class="w-8 h-8 text-sauti-blue" />
              </div>

              <h3 class="font-bold text-xl mb-2 text-sauti-darkGreen">{{ contact.name }}</h3>
              <p class="text-sm text-sauti-darkGreen/60 mb-0 font-normal leading-relaxed line-clamp-2">
                {{ contact.description || 'Verified official support channel.' }}
              </p>

              <!-- Hidden visual indicator that appears on hover/focus if needed, but keeping primarily clean -->
              <div class="absolute bottom-6 right-6 opacity-0 group-hover:opacity-100 transition-opacity">
                <ArrowRightIcon class="w-5 h-5 text-sauti-blue" />
              </div>
            </a>

            <!-- Fallback Static Office Card if no generic contacts -->
            <div v-if="nonEmergencyContacts.length === 0"
              class="bg-white p-8 rounded-2xl shadow-md group flex flex-col items-start relative overflow-hidden">
              <div class="mb-6 p-4 rounded-xl bg-sauti-neutral">
                <BuildingOfficeIcon class="w-8 h-8 text-sauti-blue" />
              </div>
              <h3 class="font-bold text-xl mb-2">Head Office</h3>
              <p class="text-sm text-sauti-darkGreen/60 mb-0 font-normal">Ministry of Gender, Labour and Social
                Development.</p>
            </div>
          </div>

          <!-- Trust / Authority Signal -->
          <div class="bg-sauti-blue/5 p-8 rounded-2xl shadow-sm flex items-start gap-4">
            <div class="p-2 bg-white rounded-full shrink-0 shadow-sm">
              <CheckBadgeIcon class="w-6 h-6 text-sauti-blue" />
            </div>
            <div>
              <h4 class="font-bold text-lg mb-1">Official Government Service</h4>
              <p class="text-sm text-sauti-darkGreen/70 leading-relaxed font-normal">
                Operated under the mandate of the Ministry of Gender, Labour and Social Development. All services are
                regulated, free, and secure.
              </p>
            </div>
          </div>
        </div>

        <!-- 3. SECONDARY CONTACT FORM (Right Column) -->
        <!-- Explicitly visually distinct from emergency options -->
        <div class="lg:col-span-5">
          <div class="bg-white p-8 md:p-10 rounded-3xl shadow-lg relative">

            <div class="mb-8">
              <span
                class="inline-block py-1 px-3 rounded bg-sauti-neutral text-sauti-darkGreen/50 text-[10px] font-bold uppercase tracking-widest mb-4">Non-Emergency
                Only</span>
              <h2 class="font-sans font-bold text-3xl mb-2 text-sauti-darkGreen">Send a Message</h2>
              <p class="text-sauti-darkGreen/60 text-sm font-normal">For general inquiries, partnerships, or feedback.
                Do not use this for reporting immediate danger.</p>
            </div>

            <form v-if="!feedbackSubmitted" @submit.prevent="submitFeedback" class="space-y-6">
              <!-- Name -->
              <div>
                <label for="name"
                  class="block text-xs font-bold uppercase text-sauti-darkGreen mb-2 tracking-wide">Your Name
                  (Optional)</label>
                <input v-model="feedbackForm.name" id="name" type="text" placeholder="John Doe"
                  class="w-full bg-sauti-neutral/50 border-2 border-transparent focus:border-sauti-blue focus:bg-white rounded-xl py-3 px-4 font-bold text-sauti-darkGreen placeholder-sauti-darkGreen/30 outline-none transition-all" />
              </div>

              <!-- Email -->
              <div>
                <label for="email"
                  class="block text-xs font-bold uppercase text-sauti-darkGreen mb-2 tracking-wide">Email Address
                  (Optional)</label>
                <input v-model="feedbackForm.email" id="email" type="email" placeholder="name@example.com"
                  class="w-full bg-sauti-neutral/50 border-2 border-transparent focus:border-sauti-blue focus:bg-white rounded-xl py-3 px-4 font-bold text-sauti-darkGreen placeholder-sauti-darkGreen/30 outline-none transition-all" />
              </div>

              <!-- Message -->
              <div>
                <label for="message"
                  class="block text-xs font-bold uppercase text-sauti-darkGreen mb-2 tracking-wide">Message <span
                    class="text-sauti-red">*</span></label>
                <textarea v-model="feedbackForm.message" id="message" required placeholder="How can we help?"
                  class="w-full h-32 bg-sauti-neutral/50 border-2 border-transparent focus:border-sauti-blue focus:bg-white rounded-xl py-3 px-4 font-bold text-sauti-darkGreen placeholder-sauti-darkGreen/30 outline-none transition-all resize-none"></textarea>
              </div>

              <div class="pt-2">
                <button :disabled="feedbackSubmitting" type="submit"
                  class="w-full bg-sauti-darkGreen text-white font-bold py-4 rounded-xl hover:bg-opacity-90 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2">
                  <span v-if="feedbackSubmitting">Sending...</span>
                  <span v-else>Send Message</span>
                </button>
              </div>

              <p v-if="feedbackError" class="text-sauti-red text-xs font-bold text-center bg-sauti-red/5 py-2 rounded">
                {{ feedbackError }}</p>
            </form>

            <!-- Success State -->
            <div v-else class="text-center py-12">
              <div
                class="w-16 h-16 bg-sauti-green/10 text-sauti-green rounded-full flex items-center justify-center mx-auto mb-6">
                <CheckBadgeIcon class="w-10 h-10" />
              </div>
              <h3 class="font-bold text-2xl text-sauti-darkGreen mb-2">Message Sent</h3>
              <p class="text-sauti-darkGreen/60 text-sm mb-8 font-normal">Thank you for contacting us. We will review
                your message shortly.</p>
              <button @click="resetFeedbackForm"
                class="text-sauti-blue font-bold text-sm hover:text-sauti-darkGreen transition-colors">Send another
                message</button>
            </div>

          </div>

          <!-- Minimal Privacy Note -->
          <p class="text-center text-[10px] text-sauti-darkGreen/40 mt-6 max-w-xs mx-auto font-normal">
            Your privacy is important to us. Information shared via this form is processed in accordance with our Data
            Protection Policy.
          </p>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
  import { computed, onMounted, ref, reactive } from 'vue'
  import { useSettingsStore } from '@/store/settings'
  import { api } from '@/utils/axios'
  import {
    PhoneIcon,
    EnvelopeIcon,
    MapPinIcon,
    BuildingOfficeIcon,
    ChatBubbleBottomCenterTextIcon,
    ArrowRightIcon,
    CheckBadgeIcon
  } from '@heroicons/vue/24/solid'

  defineOptions({
    name: 'ContactPage'
  })

  const settingsStore = useSettingsStore()
  const contacts = ref([])
  const loading = ref(true)

  // Form State
  const feedbackForm = reactive({ name: '', email: '', message: '' })
  const feedbackSubmitting = ref(false)
  const feedbackSubmitted = ref(false)
  const feedbackError = ref('')

  // Computed Collections
  const hotlines = computed(() => contacts.value.filter(c => c.type === 'phone' || c.icon === 'phone'))
  const nonEmergencyContacts = computed(() => {
    // Return all non-phone contacts (email, location, social, other)
    return contacts.value.filter(c => c.type !== 'phone' && c.icon !== 'phone')
  })

  // Helper Display Logic
  const getIcon = (contact) => {
    if (contact.type === 'email' || contact.icon === 'envelope') return EnvelopeIcon
    if (contact.type === 'location' || contact.icon === 'map-pin') return MapPinIcon
    return ChatBubbleBottomCenterTextIcon
  }

  const getActionLabel = (contact) => {
    if (contact.type === 'email') return 'Send Email'
    if (contact.type === 'location') return 'Get Directions'
    return 'Connect'
  }

  const getLink = (contact) => {
    if (contact.type === 'email') return `mailto:${contact.value}`
    if (contact.type === 'location') return `https://maps.google.com/?q=${encodeURIComponent(contact.value)}`
    return contact.value
  }


  // Actions
  const fetchContacts = async () => {
    loading.value = true
    try {
      const response = await api.get('/content/contacts/')
      contacts.value = response.data || []
    } catch (error) {
      console.error('Error fetching contacts:', error)
      // Fallback data for mockup if API fails or is empty
      contacts.value = [
        { id: 1, name: 'General Inquiries', type: 'email', value: 'info@sauti116.ug', description: 'For general questions and partnerships.' },
        { id: 2, name: 'Head Office', type: 'location', value: 'Kampala, Uganda', description: 'Ministry of Gender, Labour and Social Development.' }
      ]
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
      feedbackError.value = 'Failed to deliver message. Please try again.'
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
</script>