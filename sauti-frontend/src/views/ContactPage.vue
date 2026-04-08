<template>
  <div class="min-h-screen bg-white">
    <!-- Hero Banner -->
    <header class="hero-banner" style="padding-top: clamp(70px, 15vw, 90px);">
      <div class="hero-overlay"></div>
      <div class="container-custom hero-content-wrapper">
        <div class="hero-text">
          <h1 class="hero-title">
            {{ siteContent.getContent('contact_page_title', 'Get in') }} <span class="text-accent-yellow">{{ siteContent.getContent('contact_page_title_highlight', 'Touch') }}</span>
          </h1>
          <p class="hero-subtitle">
            {{ siteContent.getContent('contact_page_description', 'Have a question or need to report a concern? Choose the channel that works best for you.') }}
          </p>
        </div>
      </div>
    </header>

    <div class="container-custom section-padding !pt-12">


      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 md:gap-12 lg:gap-16">
        <!-- Left Column: Contact Channels -->
        <div class="space-y-6 md:space-y-8">
          <div>
            <h2 class="text-lg md:text-2xl lg:text-3xl font-bold text-secondary mb-3 md:mb-4 lg:mb-6">{{ siteContent.getContent('contact_channels_title', 'Contact Channels') }}</h2>
            <p class="text-xs md:text-sm lg:text-base text-black/60 font-semibold mb-6 md:mb-8 lg:mb-10 leading-relaxed">
              {{ siteContent.getContent('contact_channels_description', 'Choose the best way to reach us for your needs.') }}
            </p>
          </div>

          <!-- Channel Cards -->
          <div v-if="loading" class="space-y-6">
            <AppLoader />
          </div>
          <div v-else class="space-y-4 md:space-y-6">
            <template v-for="contact in nonEmergencyContacts" :key="contact.id">
               <a :href="getLink(contact)"
                  :target="contact.type === 'location' ? '_blank' : '_self'"
                  class="block bg-neutral-offwhite rounded-xl lg:rounded-2xl p-5 md:p-6 lg:p-8 transition-colors hover:bg-neutral-offwhite/80 group">
                  <div class="flex items-start gap-3 md:gap-4 lg:gap-6">
                    <div class="w-10 h-10 md:w-12 md:h-12 lg:w-14 lg:h-14 rounded-xl lg:rounded-2xl bg-white text-primary flex items-center justify-center shrink-0">
                      <component :is="getIcon(contact)" class="w-4 h-4 md:w-5 md:h-5 lg:w-6 lg:h-6" />
                    </div>
                    <div>
                      <h3 class="text-base md:text-lg lg:text-xl font-bold text-secondary mb-1 md:mb-2">{{ contact.name }}</h3>
                      <p class="text-xs md:text-sm text-black/60 font-semibold leading-relaxed mb-2 md:mb-3 lg:mb-4">
                        {{ contact.description || 'Verified official support channel.' }}
                      </p>
                      <div class="flex items-center gap-2 text-primary font-bold text-[10px] md:text-xs lg:text-sm uppercase tracking-wider">
                        <span>{{ getActionLabel(contact) }}</span>
                        <ArrowRight class="w-3 h-3 md:w-3 md:h-3 lg:w-4 lg:h-4" />
                      </div>
                    </div>
                  </div>
               </a>
            </template>
            
            <!-- Default Fallback if no contacts -->
            <div v-if="nonEmergencyContacts.length === 0" class="bg-neutral-offwhite rounded-xl lg:rounded-2xl p-5 md:p-6 lg:p-8">
                <div class="flex items-start gap-3 md:gap-4 lg:gap-6">
                   <div class="w-10 h-10 md:w-12 md:h-12 lg:w-14 lg:h-14 rounded-xl lg:rounded-2xl bg-white text-primary flex items-center justify-center shrink-0">
                      <Mail class="w-4 h-4 md:w-5 md:h-5 lg:w-6 lg:h-6" />
                   </div>
                   <div>
                      <h3 class="text-base md:text-lg lg:text-xl font-bold text-secondary mb-1 md:mb-2">{{ siteContent.getContent('contact_fallback_email_title', 'Email Us') }}</h3>
                       <p class="text-xs md:text-sm text-black/60 font-semibold leading-relaxed mb-2 md:mb-3 lg:mb-4">
                        {{ siteContent.getContent('contact_fallback_email_description', 'For general inquiries and information.') }}
                      </p>
                      <a :href="`mailto:${siteContent.getContent('contact_fallback_email_address', 'info@sauti116.ug')}`" class="flex items-center gap-2 text-primary font-bold text-[10px] md:text-xs lg:text-sm uppercase tracking-wider">
                        <span>{{ siteContent.getContent('contact_action_send_email', 'Send Email') }}</span>
                        <ArrowRight class="w-3 h-3 md:w-3 md:h-3 lg:w-4 lg:h-4" />
                      </a>
                   </div>
                </div>
            </div>
          </div>
        </div>

        <!-- Right Column: Verification & Form -->
        <div class="space-y-6 md:space-y-8">
          <!-- Form Card -->
          <div class="bg-neutral-white border-2 border-neutral-offwhite rounded-xl lg:rounded-2xl p-5 md:p-6 lg:p-10 relative overflow-hidden">

            <div class="mb-5 md:mb-6 lg:mb-8">
              <h3 class="text-lg md:text-xl lg:text-2xl font-bold text-secondary mb-1 md:mb-2">{{ siteContent.getContent('contact_form_title', 'Send a Message') }}</h3>
              <p class="text-xs md:text-sm text-black/60 font-semibold">{{ siteContent.getContent('contact_form_subtitle', 'We typically respond within 24 hours.') }}</p>
            </div>

            <form v-if="!feedbackSubmitted" @submit.prevent="submitFeedback" class="space-y-4 md:space-y-6">
              <div class="space-y-2">
                <label for="name" class="text-[10px] md:text-xs font-black uppercase text-secondary/50 tracking-widest pl-3 md:pl-4">{{ siteContent.getContent('contact_form_name_label', 'Your Name') }}</label>
                <input v-model="feedbackForm.name" id="name" type="text" required :placeholder="siteContent.getContent('contact_form_name_placeholder', 'John Doe')"
                  class="w-full bg-neutral-offwhite border-none rounded-[1.5rem] py-3 md:py-4 px-4 md:px-6 text-sm md:text-base font-bold text-secondary placeholder:text-black/20 focus:ring-0 focus:bg-neutral-offwhite/80 transition-all" />
              </div>

              <div class="space-y-2">
                <label for="email" class="text-[10px] md:text-xs font-black uppercase text-secondary/50 tracking-widest pl-3 md:pl-4">{{ siteContent.getContent('contact_form_email_label', 'Email Address') }}</label>
                <input v-model="feedbackForm.email" id="email" type="email" :placeholder="siteContent.getContent('contact_form_email_placeholder', 'name@example.com')"
                  class="w-full bg-neutral-offwhite border-none rounded-[1.5rem] py-3 md:py-4 px-4 md:px-6 text-sm md:text-base font-bold text-secondary placeholder:text-black/20 focus:ring-0 focus:bg-neutral-offwhite/80 transition-all" />
              </div>

              <div class="space-y-2">
                <label for="message" class="text-[10px] md:text-xs font-black uppercase text-secondary/50 tracking-widest pl-3 md:pl-4">{{ siteContent.getContent('contact_form_message_label', 'How can we help?') }}</label>
                <textarea v-model="feedbackForm.message" id="message" required :placeholder="siteContent.getContent('contact_form_message_placeholder', 'Type your message here...')"
                  class="w-full h-32 md:h-40 bg-neutral-offwhite border-none rounded-[1.5rem] py-3 md:py-4 px-4 md:px-6 text-sm md:text-base font-bold text-secondary placeholder:text-black/20 focus:ring-0 focus:bg-neutral-offwhite/80 transition-all resize-none"></textarea>
              </div>

              <div class="pt-2 md:pt-4">
                 <button :disabled="feedbackSubmitting" type="submit"
                  class="w-full bg-secondary text-neutral-white text-sm md:text-base font-bold py-3 md:py-5 rounded-[2rem] hover:brightness-110 transition-all flex items-center justify-center gap-2 md:gap-3">
                  <span v-if="feedbackSubmitting">{{ siteContent.getContent('contact_form_sending', 'Sending...') }}</span>
                  <span v-else>{{ siteContent.getContent('contact_form_submit', 'Send Message') }}</span>
                  <ArrowRight class="w-4 h-4 md:w-5 md:h-5" v-if="!feedbackSubmitting" />
                </button>
              </div>
            </form>

            <div v-else class="py-8 md:py-10 lg:py-12 text-center">
              <div class="w-16 h-16 md:w-20 md:h-20 bg-secondary/10 rounded-full flex items-center justify-center mx-auto mb-4 md:mb-6 text-secondary">
                <CheckCircle class="w-8 h-8 md:w-10 md:h-10" />
              </div>
              <h3 class="text-xl md:text-2xl font-bold text-secondary mb-2">{{ siteContent.getContent('contact_success_title', 'Message Sent!') }}</h3>
              <p class="text-sm md:text-base text-black/50 font-bold mb-6 md:mb-8">{{ siteContent.getContent('contact_success_message', 'Thank you for reaching out. We will get back to you shortly.') }}</p>
              <button @click="resetFeedbackForm" class="text-sm md:text-base text-primary font-bold hover:underline">{{ siteContent.getContent('contact_send_another', 'Send another message') }}</button>
            </div>
          </div>

           <!-- Trust Signal -->
          <div class="px-4 md:px-6 flex items-start gap-3 md:gap-4 opacity-60">
             <ShieldCheck class="w-4 h-4 md:w-5 md:h-5 text-secondary shrink-0 mt-0.5 md:mt-1" />
             <p class="text-[10px] md:text-xs font-bold text-secondary leading-relaxed">
               {{ siteContent.getContent('contact_trust_signal', 'Your communication is secure. This service is operated under the mandate of the Ministry of Gender, Labour and Social Development.') }}
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
  import { useSiteContent } from '@/composables/useSiteContent'
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
    ShieldCheck,
    Globe,
    Video,
    Send
  } from 'lucide-vue-next'

  defineOptions({
    name: 'ContactPage'
  })

  const settingsStore = useSettingsStore()
  const siteContent = useSiteContent('contact')
  const contacts = ref([])
  const loading = ref(true)
  const feedbackForm = reactive({ name: '', email: '', message: '' })
  const feedbackSubmitting = ref(false)
  const feedbackSubmitted = ref(false)
  const feedbackError = ref('')

  const nonEmergencyContacts = computed(() => contacts.value.filter(c => c.type !== 'phone' && c.icon !== 'phone'))

  const getIcon = (contact) => {
    if (contact.type === 'email' || contact.icon === 'envelope') return Mail
    if (contact.type === 'location' || contact.icon === 'map-pin' || contact.icon === 'location-marker') return MapPin
    if (contact.icon === 'globe') return Globe
    if (contact.icon === 'video') return Video
    if (contact.icon === 'message-square') return MessageSquare
    if (contact.icon === 'send' || contact.icon === 'sms') return Send
    if (contact.icon === 'whatsapp') return MessageSquare
    if (contact.icon === 'phone') return Phone
    return Phone
  }

  const getLink = (contact) => {
    if (contact.type === 'email') return `mailto:${contact.value}`
    if (contact.type === 'location') return `https://maps.google.com/?q=${encodeURIComponent(contact.value)}`
    if (contact.type === 'phone') {
      if (contact.icon === 'whatsapp') return `https://wa.me/${contact.value.replace(/\s/g, '')}`
      return `tel:${contact.value}`
    }
    return contact.value
  }
  
  const getActionLabel = (contact) => {
     if (contact.type === 'email') return 'Email Us'
     if (contact.type === 'location') return 'Get Directions'
     if (contact.type === 'phone') {
       if (contact.icon === 'whatsapp') return 'Chat on WhatsApp'
       return 'Call Now'
     }
     if (contact.icon === 'globe') return 'Open Portal'
     if (contact.icon === 'message-square' || contact.icon === 'sms') return 'Send SMS'
     if (contact.icon === 'video') return 'Visit TikTok'
     if (contact.icon === 'facebook') return 'Visit Facebook'
     if (contact.icon === 'twitter') return 'Visit X (Twitter)'
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
        { id: 1, name: 'Call', type: 'phone', icon: 'phone', value: '116', description: 'Free, confidential hotline available 24/7' },
        { id: 2, name: 'WhatsApp', type: 'phone', icon: 'whatsapp', value: '0743889999', description: 'Chat with us on WhatsApp' },
        { id: 3, name: 'Email', type: 'email', icon: 'envelope', value: 'sautichl@mglsd.go.ug', description: 'Send us an email for inquiries' },
        { id: 4, name: 'Online Reporting', type: 'social', icon: 'globe', value: 'https://sauti.mglsd.go.ug', description: 'Report cases online through our portal' },
        { id: 5, name: 'SMS', type: 'other', icon: 'message-square', value: 'Hello to 116', description: 'Send SMS to 116 and follow chatbot prompts' },
        { id: 6, name: 'Facebook', type: 'social', icon: 'facebook', value: 'https://www.facebook.com/Sauti116Helpline', description: 'Follow us on Facebook' },
        { id: 7, name: 'Twitter', type: 'social', icon: 'twitter', value: 'https://x.com/sauti116', description: 'Follow us on X (Twitter)' },
        { id: 8, name: 'TikTok', type: 'social', icon: 'video', value: 'https://www.tiktok.com/@sauti116helplineuganda', description: 'Follow us on TikTok' },
        { id: 9, name: 'Office Location', type: 'location', icon: 'location-marker', value: 'Ministry of Gender, Labour & Social Development, Kampala, Uganda', description: 'Visit our head office' },
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

  onMounted(async () => {
    await siteContent.fetchContent()
    await settingsStore.fetchGlobalSettings()
    fetchContacts()
  })
</script>

<style scoped>
/* Hero Banner */
.hero-banner {
  position: relative;
  background: linear-gradient(135deg, rgb(var(--color-secondary)) 0%, rgb(var(--color-primary-dark)) 100%);
  min-height: clamp(200px, 25vh, 300px);
  display: flex;
  align-items: center;
  overflow: hidden;
  margin-top: 0;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800"><defs><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1"/></pattern></defs><rect width="1200" height="800" fill="url(%23grid)"/></svg>');
  opacity: 0.5;
}

.hero-content-wrapper {
  position: relative;
  z-index: 2;
  padding: clamp(1.25rem, 3vh, 2.5rem) 0;
}

.hero-text {
  text-align: center;
  margin-bottom: clamp(0.75rem, 2vw, 1rem);
}

.hero-title {
  font-size: clamp(1rem, 2vw, 1.75rem);
  font-weight: 900;
  color: white;
  margin-bottom: 0.375rem;
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.text-accent-yellow {
  color: rgb(var(--color-accent-yellow));
}

.hero-subtitle {
  font-size: clamp(0.75rem, 0.9vw, 0.875rem);
  color: rgba(255, 255, 255, 0.85);
  font-weight: 400;
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.4;
  padding: 0 1rem;
}
</style>