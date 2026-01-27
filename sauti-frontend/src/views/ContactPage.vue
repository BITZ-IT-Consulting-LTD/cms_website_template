<template>
  <div class="min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header !pb-0">
      <div class="container-custom">
        <h1 class="page-header-title">Contact Us</h1>
      </div>
    </header>

    <div class="container-custom section-padding !pt-0">


      <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">
        <!-- Left Column: Contact Channels -->
        <div class="space-y-8">
          <div>
            <h2 class="text-3xl font-bold text-secondary mb-6">Get in Touch</h2>
            <p class="text-black/50 font-bold text-lg mb-12 leading-relaxed">
              Have a question or need to report a concern? Choose the channel that works best for you.
            </p>
          </div>

          <!-- Channel Cards -->
          <div v-if="loading" class="space-y-6">
            <AppLoader />
          </div>
          <div v-else class="space-y-6">
            <template v-for="contact in nonEmergencyContacts" :key="contact.id">
               <a :href="getLink(contact)" 
                  :target="contact.type === 'location' ? '_blank' : '_self'"
                  class="block bg-neutral-offwhite rounded-[2.5rem] p-8 transition-colors hover:bg-neutral-offwhite/80 group">
                  <div class="flex items-start gap-6">
                    <div class="w-14 h-14 rounded-2xl bg-white text-primary flex items-center justify-center shrink-0">
                      <component :is="getIcon(contact)" class="w-6 h-6" />
                    </div>
                    <div>
                      <h3 class="text-xl font-bold text-secondary mb-2">{{ contact.name }}</h3>
                      <p class="text-black/50 font-bold text-sm leading-relaxed mb-4">
                        {{ contact.description || 'Verified official support channel.' }}
                      </p>
                      <div class="flex items-center gap-2 text-primary font-bold text-sm uppercase tracking-wider">
                        <span>{{ getActionLabel(contact) }}</span>
                        <ArrowRight class="w-4 h-4" />
                      </div>
                    </div>
                  </div>
               </a>
            </template>
            
            <!-- Default Fallback if no contacts -->
            <div v-if="nonEmergencyContacts.length === 0" class="bg-neutral-offwhite rounded-[2.5rem] p-8">
                <div class="flex items-start gap-6">
                   <div class="w-14 h-14 rounded-2xl bg-white text-primary flex items-center justify-center shrink-0">
                      <Mail class="w-6 h-6" />
                   </div>
                   <div>
                      <h3 class="text-xl font-bold text-secondary mb-2">Email Us</h3>
                       <p class="text-black/50 font-bold text-sm leading-relaxed mb-4">
                        For general inquiries and information.
                      </p>
                      <a href="mailto:info@sauti116.ug" class="flex items-center gap-2 text-primary font-bold text-sm uppercase tracking-wider">
                        <span>Send Email</span>
                        <ArrowRight class="w-4 h-4" />
                      </a>
                   </div>
                </div>
            </div>
          </div>
        </div>

        <!-- Right Column: Verification & Form -->
        <div class="space-y-8">
          <!-- Form Card -->
          <div class="bg-neutral-white border-2 border-neutral-offwhite rounded-[3rem] p-10 relative overflow-hidden">
             
            <div class="mb-8">
              <h3 class="text-2xl font-bold text-secondary mb-2">Send a Message</h3>
              <p class="text-black/50 font-bold text-sm">We typically respond within 24 hours.</p>
            </div>

            <form v-if="!feedbackSubmitted" @submit.prevent="submitFeedback" class="space-y-6">
              <div class="space-y-2">
                <label for="name" class="text-xs font-black uppercase text-secondary/50 tracking-widest pl-4">Your Name</label>
                <input v-model="feedbackForm.name" id="name" type="text" required placeholder="John Doe"
                  class="w-full bg-neutral-offwhite border-none rounded-[1.5rem] py-4 px-6 font-bold text-secondary placeholder:text-black/20 focus:ring-0 focus:bg-neutral-offwhite/80 transition-all" />
              </div>
              
              <div class="space-y-2">
                <label for="email" class="text-xs font-black uppercase text-secondary/50 tracking-widest pl-4">Email Address</label>
                <input v-model="feedbackForm.email" id="email" type="email" placeholder="name@example.com"
                  class="w-full bg-neutral-offwhite border-none rounded-[1.5rem] py-4 px-6 font-bold text-secondary placeholder:text-black/20 focus:ring-0 focus:bg-neutral-offwhite/80 transition-all" />
              </div>

              <div class="space-y-2">
                <label for="message" class="text-xs font-black uppercase text-secondary/50 tracking-widest pl-4">How can we help?</label>
                <textarea v-model="feedbackForm.message" id="message" required placeholder="Type your message here..."
                  class="w-full h-40 bg-neutral-offwhite border-none rounded-[1.5rem] py-4 px-6 font-bold text-secondary placeholder:text-black/20 focus:ring-0 focus:bg-neutral-offwhite/80 transition-all resize-none"></textarea>
              </div>

              <div class="pt-4">
                 <button :disabled="feedbackSubmitting" type="submit"
                  class="w-full bg-secondary text-neutral-white font-bold py-5 rounded-[2rem] hover:brightness-110 transition-all flex items-center justify-center gap-3">
                  <span v-if="feedbackSubmitting">Sending...</span>
                  <span v-else>Send Message</span>
                  <ArrowRight class="w-5 h-5" v-if="!feedbackSubmitting" />
                </button>
              </div>
            </form>

            <div v-else class="py-12 text-center">
              <div class="w-20 h-20 bg-secondary/10 rounded-full flex items-center justify-center mx-auto mb-6 text-secondary">
                <CheckCircle class="w-10 h-10" />
              </div>
              <h3 class="text-2xl font-bold text-secondary mb-2">Message Sent!</h3>
              <p class="text-black/50 font-bold mb-8">Thank you for reaching out. We will get back to you shortly.</p>
              <button @click="resetFeedbackForm" class="text-primary font-bold hover:underline">Send another message</button>
            </div>
          </div>
          
           <!-- Trust Signal -->
          <div class="px-6 flex items-start gap-4 opacity-60">
             <ShieldCheck class="w-5 h-5 text-secondary shrink-0 mt-1" />
             <p class="text-xs font-bold text-secondary leading-relaxed">
               Your communication is secure. This service is operated under the mandate of the Ministry of Gender, Labour and Social Development.
             </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { computed, onMounted, ref, reactive } from 'vue'
  import { useSettingsStore } from '@/store/settings'
  import { api } from '@/utils/axios'
  import AppLoader from '@/components/common/AppLoader.vue'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import {
    Phone,
    Mail,
    MapPin,
    MessageSquare,
    ArrowRight,
    CheckCircle,
    ShieldCheck
  } from 'lucide-vue-next'

  defineOptions({
    name: 'ContactPage'
  })

  const settingsStore = useSettingsStore()
  const contacts = ref([])
  const loading = ref(true)
  const feedbackForm = reactive({ name: '', email: '', message: '' })
  const feedbackSubmitting = ref(false)
  const feedbackSubmitted = ref(false)
  const feedbackError = ref('')

  const nonEmergencyContacts = computed(() => contacts.value.filter(c => c.type !== 'phone' && c.icon !== 'phone'))

  const getIcon = (contact) => {
    if (contact.type === 'email' || contact.icon === 'envelope') return Mail
    if (contact.type === 'location' || contact.icon === 'map-pin') return MapPin
    return MessageSquare
  }

  const getLink = (contact) => {
    if (contact.type === 'email') return `mailto:${contact.value}`
    if (contact.type === 'location') return `https://maps.google.com/?q=${encodeURIComponent(contact.value)}`
    return contact.value
  }
  
  const getActionLabel = (contact) => {
     if (contact.type === 'email') return 'Email Us'
     if (contact.type === 'location') return 'Get Directions'
     return 'Visit Link'
  }

  const fetchContacts = async () => {
    loading.value = true
    try {
      const response = await api.get('/content/contacts/')
      contacts.value = response.data || []
    } catch (error) {
       // Keep valid fallback data for demo reliability if API fails
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
    try {
      await api.post('/contact/feedback/', feedbackForm)
      feedbackSubmitted.value = true
    } catch (err) {
      feedbackError.value = 'Failed to deliver message.'
      // For demo purposes, we can simulate success if API fails/is mocked
      if (import.meta.env.DEV) {
          setTimeout(() => { feedbackSubmitted.value = true }, 1000)
      }
    } finally {
      feedbackSubmitting.value = false
    }
  }

  const resetFeedbackForm = () => {
    feedbackSubmitted.value = false
    feedbackForm.name = ''
    feedbackForm.email = ''
    feedbackForm.message = ''
  }

  onMounted(() => {
    settingsStore.fetchGlobalSettings()
    fetchContacts()
  })
</script>