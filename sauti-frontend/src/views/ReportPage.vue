<template>
  <div class="min-h-screen bg-gradient-to-b from-white via-white to-gray-50 overflow-x-hidden" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
    <!-- 1. Hero Section -->
    <header class="py-6 md:py-8 text-center relative overflow-hidden">
      <!-- Background Gradient Decoration -->
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-primary/5 rounded-full blur-3xl -z-10 opacity-60"></div>

      <div class="container-custom relative z-10 px-4">
        <h1 class="text-lg md:text-2xl lg:text-3xl font-bold text-secondary mb-2 md:mb-3 tracking-tight break-words" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
          Report a <span class="text-primary">Case</span>
        </h1>
        <p class="text-xs md:text-sm lg:text-base text-gray-600 max-w-2xl mx-auto leading-relaxed mb-4 md:mb-6 break-words" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
          A safe, confidential, and professional space to seek help. We are available 24/7 to support you.
        </p>

        <!-- Trust Badges -->
        <div class="flex flex-wrap justify-center gap-2 md:gap-3 text-[10px] md:text-xs font-bold text-gray-500 uppercase tracking-wider" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
          <div class="flex items-center gap-2 px-3 md:px-4 py-1 md:py-2 bg-white rounded-full shadow-sm border border-gray-100">
            <Lock class="w-4 h-4 md:w-5 md:h-5 text-emerald-500" />
            <span>Secure</span>
          </div>
          <div class="flex items-center gap-2 px-3 md:px-4 py-1 md:py-2 bg-white rounded-full shadow-sm border border-gray-100">
            <Clock class="w-4 h-4 md:w-5 md:h-5 text-blue-500" />
            <span>24/7 Support</span>
          </div>
        </div>
      </div>
    </header>

    <!-- 2. Main Content Grid -->
    <div class="container-custom pb-12 md:pb-16 px-4">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 md:gap-6 lg:gap-8 items-start">

        <!-- Left Column (Primary - 8 cols) -->
        <main class="lg:col-span-8 space-y-4 md:space-y-6 flex flex-col">
          
          <!-- Report Form Component (Prioritized on Mobile) -->
          <section aria-label="Reporting Interface" class="order-1">
            <ReportForm />
          </section>

          <!-- Contextual Steps (1-2-3 Guide) - Moved below form on mobile/desktop flow -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-3 md:gap-4 mb-4 md:mb-6 order-2 mt-4 md:mt-6">
            <div class="bg-white p-4 md:p-5 rounded-2xl md:rounded-3xl shadow-sm border border-gray-100 relative group hover:border-primary/20 transition-all">
              <span class="absolute -top-3 -left-3 w-8 h-8 md:w-10 md:h-10 bg-primary text-white rounded-xl flex items-center justify-center font-bold text-sm md:text-base shadow-lg rotate-3 group-hover:rotate-6 transition-transform" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">1</span>
              <h3 class="font-bold text-secondary text-sm md:text-base lg:text-lg mb-1 md:mb-2 mt-2 break-words" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Provide Details</h3>
              <p class="text-xs md:text-sm text-gray-500 leading-relaxed break-words" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Chat with our secure assistant to share what happened at your own pace.</p>
            </div>
            <div class="bg-white p-4 md:p-5 rounded-2xl md:rounded-3xl shadow-sm border border-gray-100 relative group hover:border-primary/20 transition-all">
              <span class="absolute -top-3 -left-3 w-8 h-8 md:w-10 md:h-10 bg-primary text-white rounded-xl flex items-center justify-center font-bold text-sm md:text-base shadow-lg -rotate-3 group-hover:-rotate-6 transition-transform" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">2</span>
              <h3 class="font-bold text-secondary text-sm md:text-base lg:text-lg mb-1 md:mb-2 mt-2 break-words" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Submit Securely</h3>
              <p class="text-xs md:text-sm text-gray-500 leading-relaxed break-words" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Your report is encrypted and sent directly to our protection team.</p>
            </div>
            <div class="bg-white p-4 md:p-5 rounded-2xl md:rounded-3xl shadow-sm border border-gray-100 relative group hover:border-primary/20 transition-all">
              <span class="absolute -top-3 -left-3 w-8 h-8 md:w-10 md:h-10 bg-primary text-white rounded-xl flex items-center justify-center font-bold text-sm md:text-base shadow-lg rotate-3 group-hover:rotate-6 transition-transform" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">3</span>
              <h3 class="font-bold text-secondary text-sm md:text-base lg:text-lg mb-1 md:mb-2 mt-2 break-words" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">We Follow Up</h3>
              <p class="text-xs md:text-sm text-gray-500 leading-relaxed break-words" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">A professional caseworker reviews your case and contacts you for support.</p>
            </div>
          </div>

        </main>

        <!-- Right Column (Sidebar - 4 cols) -->
        <aside class="lg:col-span-4 space-y-4 md:space-y-6">

          <!-- Immediate Help Card -->
          <div class="bg-red-50 rounded-2xl md:rounded-3xl p-5 md:p-6 shadow-sm border border-red-100">
            <div class="flex items-center gap-2 md:gap-3 mb-2 md:mb-3">
              <div class="w-8 h-8 md:w-10 md:h-10 bg-red-100 rounded-full flex items-center justify-center text-red-600">
                <TriangleAlert class="w-4 h-4 md:w-5 md:h-5" />
              </div>
              <h3 class="font-bold text-red-900 text-sm md:text-base lg:text-lg break-words" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Immediate Danger?</h3>
            </div>
            <p class="text-red-800/70 text-xs md:text-sm font-medium leading-relaxed mb-4 md:mb-6 break-words" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
              If you or someone else is in immediate physical danger, do not use this form. Get instant help now.
            </p>
            <div class="space-y-2 md:space-y-3">
              <a :href="phoneHref" class="flex items-center justify-center gap-2 md:gap-3 w-full py-3 md:py-4 bg-red-600 hover:bg-red-700 text-white font-bold rounded-xl md:rounded-2xl shadow-lg shadow-red-200 transition-all active:scale-95 text-sm md:text-base" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
                <Phone class="w-4 h-4 md:w-5 md:h-5" />
                <span>Call {{ phoneValue }} Free</span>
              </a>
              <a :href="whatsappHref" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-2 md:gap-3 w-full py-3 md:py-4 bg-white border-2 border-green-500 text-green-600 hover:bg-green-50 font-bold rounded-xl md:rounded-2xl transition-all text-sm md:text-base" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
                <MessageCircle class="w-4 h-4 md:w-5 md:h-5" />
                <span>WhatsApp Chat</span>
              </a>
            </div>
          </div>

          <!-- Other Channels -->
          <div class="bg-gray-50 rounded-2xl md:rounded-3xl p-5 md:p-6 border border-gray-100">
            <h3 class="font-bold text-secondary text-sm md:text-base lg:text-lg mb-3 md:mb-4 break-words" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Other Ways to Report</h3>
            <div class="space-y-2 md:space-y-3">
              <div class="flex items-center gap-3 md:gap-4 p-3 md:p-4 bg-white rounded-xl md:rounded-2xl shadow-sm border border-gray-100">
                <div class="w-8 h-8 md:w-10 md:h-10 rounded-lg md:rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center flex-shrink-0">
                  <MessageSquareText class="w-4 h-4 md:w-5 md:h-5" />
                </div>
                <div class="min-w-0 flex-1">
                  <p class="text-[10px] md:text-xs font-bold text-gray-400 uppercase tracking-wide" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">SMS Shortcode</p>
                  <p class="font-bold text-secondary text-xs md:text-sm break-words" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ smsLabel }}</p>
                </div>
              </div>
              <div class="flex items-center gap-3 md:gap-4 p-3 md:p-4 bg-white rounded-xl md:rounded-2xl shadow-sm border border-gray-100">
                <div class="w-8 h-8 md:w-10 md:h-10 rounded-lg md:rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center flex-shrink-0">
                  <Smartphone class="w-4 h-4 md:w-5 md:h-5" />
                </div>
                <div class="min-w-0 flex-1">
                  <p class="text-[10px] md:text-xs font-bold text-gray-400 uppercase tracking-wide" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Mobile App</p>
                  <p class="font-bold text-secondary text-xs md:text-sm break-words" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ appLabel }}</p>
                </div>
              </div>
              <div class="flex items-center gap-3 md:gap-4 p-3 md:p-4 bg-white rounded-xl md:rounded-2xl shadow-sm border border-gray-100">
                <div class="w-8 h-8 md:w-10 md:h-10 rounded-lg md:rounded-xl bg-orange-50 text-orange-600 flex items-center justify-center flex-shrink-0">
                  <Mail class="w-4 h-4 md:w-5 md:h-5" />
                </div>
                <div class="min-w-0 flex-1">
                  <p class="text-[10px] md:text-xs font-bold text-gray-400 uppercase tracking-wide" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Email</p>
                  <a :href="emailHref" class="font-bold text-secondary break-all text-xs md:text-sm" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">{{ emailValue }}</a>
                </div>
              </div>
            </div>
          </div>

          <!-- Privacy Footer Link -->
          <div class="text-center py-2 md:py-3">
            <router-link to="/privacy" class="inline-flex items-center gap-2 text-[10px] md:text-xs font-bold text-gray-400 hover:text-primary transition-colors uppercase tracking-widest" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
              <Lock class="w-3 h-3 md:w-4 md:h-4" />
              View Full Privacy Policy
            </router-link>
          </div>

        </aside>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue'
  import { api } from '@/utils/axios'
  import { toWaMeNumber } from '@/utils/phone'
  import ReportForm from '@/components/reports/ReportForm.vue'

  import {
    ShieldCheck,
    Phone,
    MessageCircle,
    MessageSquareText,
    Mail,
    Globe,
    TriangleAlert,
    Smartphone,
    Lock,
    Clock
  } from 'lucide-vue-next'

  defineOptions({
    name: 'ReportPage'
  })

  // Hardcoded fallbacks — used whenever the CMS is unreachable or a matching
  // Contact record doesn't exist. Admin > Contact Info (the `/content/contacts/`
  // endpoint) is the source of truth for everything else below.
  const FALLBACKS = {
    phone: '116',
    whatsapp: '256743889999',
    sms: 'Text to 8500',
    app: 'SafePal App',
    email: 'info@sauti.mglsd.go.ug',
  }

  const contacts = ref([])

  const findContact = (predicate) => contacts.value.find(predicate)

  // "Call 116 Free" — Contact record: type 'phone', icon 'phone'.
  const phoneContact = computed(() => findContact(c => c.type === 'phone' && c.icon === 'phone'))
  const phoneValue = computed(() => phoneContact.value?.value || FALLBACKS.phone)
  const phoneHref = computed(() => `tel:${phoneValue.value.replace(/\s+/g, '')}`)

  // WhatsApp — Contact record: icon 'whatsapp'.
  // NOTE: CMS values are frequently entered in Uganda LOCAL format (e.g.
  // '0743889999'), which is NOT valid for a wa.me link (needs full
  // international format with no leading '0'/'+'). toWaMeNumber() handles
  // that normalisation — don't just strip non-digits here.
  const whatsappContact = computed(() => findContact(c => c.icon === 'whatsapp'))
  const whatsappValue = computed(() => whatsappContact.value?.value || FALLBACKS.whatsapp)
  const whatsappHref = computed(() => `https://wa.me/${toWaMeNumber(whatsappValue.value)}`)

  // SMS Shortcode — no CMS Contact record for this exists in the seed data
  // (icon 'message-square'/'send' records seen in the wild are the "Hello to
  // 116" chatbot number, not the "8500" shortcode), so this always falls
  // back to the hardcoded label unless an admin later adds a matching one.
  const smsContact = computed(() => findContact(c => c.icon === 'message-square' || c.icon === 'send'))
  const smsLabel = computed(() => smsContact.value?.value || FALLBACKS.sms)

  // Mobile App — the admin Contact Info icon list has no dedicated "app"
  // icon/type, so there is no reliable CMS record to resolve this from; kept
  // as a best-effort name match with the hardcoded label as fallback.
  const appContact = computed(() => findContact(c => /app/i.test(c.name || '')))
  const appLabel = computed(() => appContact.value?.value || appContact.value?.name || FALLBACKS.app)

  // Email — Contact record: type 'email', icon 'envelope'.
  const emailContact = computed(() => findContact(c => c.type === 'email' || c.icon === 'envelope'))
  const emailValue = computed(() => emailContact.value?.value || FALLBACKS.email)
  const emailHref = computed(() => `mailto:${emailValue.value}`)

  const fetchContacts = async () => {
    try {
      const response = await api.get('/content/contacts/')
      contacts.value = response.data || []
    } catch (error) {
      // Leave contacts empty — every computed above falls back to the
      // hardcoded value so this page never renders blank/broken.
      contacts.value = []
    }
  }

  onMounted(fetchContacts)
</script>
