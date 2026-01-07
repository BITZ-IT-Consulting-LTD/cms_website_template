<template>
  <div class="bg-neutral-offwhite min-h-screen font-sans text-secondary">
    <!-- 1. EMERGENCY HERO SECTION (Sanctuary Layout) -->
    <header class="page-header !py-24 md:!py-32">
      <div class="container-custom max-w-4xl mx-auto text-center px-6">
        <!-- High-Trust, Low-Noise Signal -->
        <div
          class="inline-flex items-center gap-3 mb-10 bg-secondary/5 px-6 py-2 rounded-full border border-secondary/10">
          <CheckBadgeIcon class="w-4 h-4 text-secondary-light" />
          <span class="text-[10px] font-black uppercase tracking-[0.2em] text-black">Official Government
            Service</span>
        </div>

        <h1 class="mb-10 text-secondary">
          Reach Our Expert Team <span class="text-primary">Anytime</span>.
        </h1>

        <!-- Quick Summary for Your Peace of Mind (Flash Pattern) -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16 text-left">
          <div class="bg-neutral-white p-6 rounded-3xl border border-primary/5 shadow-sm">
            <p class="text-black font-black text-sm uppercase tracking-widest mb-2">Toll-Free</p>
            <p class="text-black text-sm leading-relaxed text-[13px]">The call is 100% free from any phone network in
              Uganda.</p>
          </div>
          <div class="bg-neutral-white p-6 rounded-3xl border border-primary/5 shadow-sm">
            <p class="text-black font-black text-sm uppercase tracking-widest mb-2">Private</p>
            <p class="text-black text-sm leading-relaxed text-[13px]">No record of this call will appear on your monthly
              phone bill.</p>
          </div>
          <div class="bg-neutral-white p-6 rounded-3xl border border-primary/5 shadow-sm">
            <p class="text-black font-black text-sm uppercase tracking-widest mb-2">Expert Care</p>
            <p class="text-black text-sm leading-relaxed text-[13px]">You will speak directly with a trained protection
              counselor.</p>
          </div>
        </div>

        <div class="flex flex-col items-center">
          <BaseCTA :href="`tel:${settingsStore.settings.hotline_number || '116'}`" variant="emergency" size="hero"
            class="w-full max-w-lg !py-8 shadow-2xl ring-8 ring-white/10 group" external>
            <div class="flex items-center justify-center gap-6">
              <div class="bg-white/20 p-4 rounded-2xl group-hover:rotate-12 transition-transform">
                <PhoneIcon class="w-12 h-12 text-white" stroke-width="2.5" />
              </div>
              <div class="text-left">
                <span class="text-xs font-black tracking-[0.3em] opacity-80 block mb-1 uppercase">Immediate Help</span>
                <span class="text-4xl md:text-5xl font-black tracking-tighter uppercase leading-none">CALL {{
                  settingsStore.settings.hotline_number || '116' }}</span>
              </div>
            </div>
          </BaseCTA>
          <p class="mt-6 text-sm font-black text-black/40 uppercase tracking-[0.2em]">Available 24/7 Nationwide</p>
        </div>
      </div>
    </header>

    <div class="container-custom py-24 md:py-40">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-16 lg:gap-24 max-w-7xl mx-auto">
        <!-- 2. CONTACT OPTIONS -->
        <div class="lg:col-span-12 xl:col-span-7 space-y-16">
          <div class="max-w-2xl">
            <h2 class="mb-4">Your Path to <span class="text-primary">Expert Support</span></h2>
            <p class="text-xl font-bold text-black/60">Choose the channel that feels safest for you. All messages
              are encrypted and private.</p>
          </div>

          <div class="grid gap-6 md:grid-cols-2">
            <a v-for="contact in nonEmergencyContacts" :key="contact.id" :href="getLink(contact)"
              :target="contact.type === 'location' ? '_blank' : '_self'"
              class="bg-neutral-white p-10 rounded-[2.5rem] border border-primary/5 hover:border-primary/20 hover:shadow-xl transition-all duration-500 group flex flex-col items-start relative overflow-hidden cursor-pointer">
              <div class="mb-8 p-6 rounded-2xl bg-primary/5 group-hover:bg-primary/10 transition-colors">
                <component :is="getIcon(contact)" class="w-10 h-10 text-primary" />
              </div>
              <h3 class="mb-3">{{ contact.name }}</h3>
              <p class="text-sm line-clamp-2">
                {{ contact.description || 'Verified official support channel managed by MGLSD experts.' }}
              </p>
              <div class="absolute bottom-6 right-6 opacity-0 group-hover:opacity-100 transition-opacity">
                <ArrowRightIcon class="w-5 h-5 text-primary" />
              </div>
            </a>
          </div>

          <!-- Refined Trust Signal -->
          <div class="bg-primary/5 p-8 rounded-2xl shadow-sm flex items-start gap-4">
            <div class="p-2 bg-neutral-white rounded-full shrink-0 shadow-sm border border-primary/10">
              <CheckBadgeIcon class="w-6 h-6 text-primary" />
            </div>
            <div>
              <h4 class="font-black text-xs uppercase tracking-[0.2em] text-secondary mb-2">Legal Mandate & Governance
              </h4>
              <p class="text-sm text-black/70 leading-relaxed font-bold">
                Operated under the exclusive mandate of the **Ministry of Gender, Labour and Social Development**. All
                interventions are regulated, strictly confidential, and provided at no cost to the public.
              </p>
            </div>
          </div>
        </div>

        <!-- 3. SECONDARY CONTACT FORM -->
        <div class="lg:col-span-5">
          <div class="bg-neutral-white p-8 md:p-10 rounded-3xl shadow-lg relative">
            <div class="mb-8 p-6 bg-accent-yellow/10 rounded-2xl border-l-4 border-accent-yellow">
              <div class="flex items-center gap-3 mb-4">
                <ShieldCheckIcon class="w-6 h-6 text-primary" aria-hidden="true" />
                <span class="text-xs font-bold uppercase tracking-widest text-black">Secure & Private Message</span>
              </div>
              <h2 class="text-secondary mb-2">Share Your Question</h2>
              <p class="text-black/60 text-sm font-bold leading-relaxed">
                Everything you write here is encrypted and read only by our core protection team.
                <span class="text-hotline block mt-2 font-black uppercase tracking-widest text-[10px]">For immediate
                  danger, please call 116.</span>
              </p>
            </div>

            <form v-if="!feedbackSubmitted" @submit.prevent="submitFeedback" class="space-y-6">
              <div>
                <label for="name" class="block text-xs font-bold uppercase text-black mb-2 tracking-wide">Name
                  (Optional)</label>
                <input v-model="feedbackForm.name" id="name" type="text" placeholder="Your name or initials"
                  class="w-full bg-neutral-offwhite border-2 border-transparent focus:border-primary focus:bg-neutral-white rounded-xl py-3 px-4 font-bold text-secondary outline-none transition-all" />
              </div>
              <div>
                <label for="email" class="block text-xs font-bold uppercase text-black mb-2 tracking-wide">Contact
                  Address</label>
                <input v-model="feedbackForm.email" id="email" type="email" placeholder="email@example.com"
                  class="w-full bg-neutral-offwhite border-2 border-transparent focus:border-primary focus:bg-neutral-white rounded-xl py-3 px-4 font-bold text-secondary outline-none transition-all" />
              </div>
              <div>
                <label for="message" class="block text-xs font-bold uppercase text-black mb-2 tracking-wide">Message
                  <span class="text-emergency">*</span></label>
                <textarea v-model="feedbackForm.message" id="message" required placeholder="How can we help?"
                  class="w-full h-32 bg-neutral-offwhite border-2 border-transparent focus:border-primary focus:bg-neutral-white rounded-xl py-3 px-4 font-bold text-secondary outline-none transition-all resize-none"></textarea>
              </div>
              <button :disabled="feedbackSubmitting" type="submit"
                class="w-full bg-secondary text-neutral-white font-bold py-4 rounded-xl hover:shadow-lg transition-all flex items-center justify-center gap-2">
                <span v-if="feedbackSubmitting">Sending...</span>
                <span v-else>Send Message</span>
              </button>
            </form>

            <div v-else class="text-center py-12">
              <CheckBadgeIcon class="w-16 h-16 text-secondary-light mx-auto mb-6 opacity-30" />
              <h3 class="font-bold text-2xl text-secondary mb-2">Message Delivered</h3>
              <p class="text-black/60 text-sm mb-8 font-normal">Your message has been securely sent to our team.</p>
              <button @click="resetFeedbackForm" class="text-primary font-bold text-sm">Send another</button>
            </div>
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
  import {
    PhoneIcon,
    EnvelopeIcon,
    MapPinIcon,
    BuildingOfficeIcon,
    ChatBubbleBottomCenterTextIcon,
    ArrowRightIcon,
    CheckBadgeIcon,
    ShieldCheckIcon
  } from '@heroicons/vue/24/solid'

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
    if (contact.type === 'email' || contact.icon === 'envelope') return EnvelopeIcon
    if (contact.type === 'location' || contact.icon === 'map-pin') return MapPinIcon
    return ChatBubbleBottomCenterTextIcon
  }

  const getLink = (contact) => {
    if (contact.type === 'email') return `mailto:${contact.value}`
    if (contact.type === 'location') return `https://maps.google.com/?q=${encodeURIComponent(contact.value)}`
    return contact.value
  }

  const fetchContacts = async () => {
    loading.value = true
    try {
      const response = await api.get('/content/contacts/')
      contacts.value = response.data || []
    } catch (error) {
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