<template>
  <div>
    <template v-for="section in aboutSections" :key="section.key">
      <component :is="section.component" :data="section.data"
        v-if="section.data && Object.keys(section.data).length > 0" />
    </template>
  </div>
</template>

<script setup>
  import { onMounted, ref, h, computed, resolveComponent } from 'vue'
  import { useSettingsStore } from '@/store/settings'
  import { api } from '@/utils/axios'
  import sautiAboutpage from '@/assets/sauti-aboutpage.webp'
  import AppTimeline from '@/components/AppTimeline.vue' // AppTimeline will be rendered dynamically
  import AppServiceCard from '@/components/AppServiceCard.vue'

  // Import icons for dynamic rendering
  import {
    PhoneIcon, ClockIcon, GlobeAltIcon, CurrencyDollarIcon,
    LockClosedIcon, BoltIcon, HeartIcon, ShieldCheckIcon, UsersIcon,
    ChatBubbleBottomCenterTextIcon, DocumentTextIcon, LightBulbIcon, AcademicCapIcon,
    BriefcaseIcon, ChartBarIcon, ClipboardDocumentListIcon,
    Squares2X2Icon, CubeTransparentIcon, ComputerDesktopIcon, DevicePhoneMobileIcon,
    FaceSmileIcon, ExclamationCircleIcon, EyeIcon, ForwardIcon,
    FilmIcon, FingerPrintIcon, FireIcon, FlagIcon, FolderOpenIcon,
    GiftIcon, GlobeAmericasIcon, HandRaisedIcon, HashtagIcon, HomeIcon,
    InboxArrowDownIcon, InformationCircleIcon, KeyIcon,
    LinkIcon, MapPinIcon,
    EnvelopeIcon, Bars3Icon, MicrophoneIcon, MinusCircleIcon, MoonIcon,
    NewspaperIcon, BuildingOfficeIcon, PaperAirplaneIcon, PaperClipIcon,
    PencilSquareIcon, PhotoIcon, PlayIcon, PlusCircleIcon,
    PresentationChartBarIcon, PrinterIcon, PuzzlePieceIcon, QrCodeIcon,
    QuestionMarkCircleIcon, ReceiptRefundIcon, ArrowPathIcon, ChatBubbleLeftRightIcon,
    BackwardIcon, RssIcon, ScaleIcon, MagnifyingGlassIcon,
    ShareIcon, ShoppingBagIcon, ShoppingCartIcon, SparklesIcon, MegaphoneIcon,
    StarIcon, SunIcon, LifebuoyIcon, TagIcon, RectangleStackIcon,
    CommandLineIcon, HandThumbDownIcon, HandThumbUpIcon, TicketIcon, LanguageIcon,
    TrashIcon, ArrowTrendingDownIcon, ArrowTrendingUpIcon, TruckIcon, ArrowUpTrayIcon,
    UserGroupIcon, UserIcon, ViewColumnsIcon, SquaresPlusIcon,
    ListBulletIcon, SpeakerWaveIcon, WifiIcon, XCircleIcon, MagnifyingGlassPlusIcon, MagnifyingGlassMinusIcon
  } from '@heroicons/vue/24/outline'

  const heroicons = {
    PhoneIcon, ClockIcon, GlobeAltIcon, CurrencyDollarIcon,
    LockClosedIcon, BoltIcon, HeartIcon, ShieldCheckIcon, UsersIcon,
    ChatBubbleBottomCenterTextIcon, DocumentTextIcon, LightBulbIcon, AcademicCapIcon,
    BriefcaseIcon, ChartBarIcon, ClipboardDocumentListIcon,
    Squares2X2Icon, CubeTransparentIcon, ComputerDesktopIcon, DevicePhoneMobileIcon,
    FaceSmileIcon, ExclamationCircleIcon, EyeIcon, ForwardIcon,
    FilmIcon, FingerPrintIcon, FireIcon, FlagIcon, FolderOpenIcon,
    GiftIcon, GlobeAmericasIcon, HandRaisedIcon, HashtagIcon, HomeIcon,
    InboxArrowDownIcon, InformationCircleIcon, KeyIcon,
    LinkIcon, MapPinIcon,
    EnvelopeIcon, Bars3Icon, MicrophoneIcon, MinusCircleIcon, MoonIcon,
    NewspaperIcon, BuildingOfficeIcon, PaperAirplaneIcon, PaperClipIcon,
    PencilSquareIcon, PhotoIcon, PlayIcon, PlusCircleIcon,
    PresentationChartBarIcon, PrinterIcon, PuzzlePieceIcon, QrCodeIcon,
    QuestionMarkCircleIcon, ReceiptRefundIcon, ArrowPathIcon, ChatBubbleLeftRightIcon,
    BackwardIcon, RssIcon, ScaleIcon, MagnifyingGlassIcon,
    ShareIcon, ShoppingBagIcon, ShoppingCartIcon, SparklesIcon, MegaphoneIcon,
    StarIcon, SunIcon, LifebuoyIcon, TagIcon, RectangleStackIcon,
    CommandLineIcon, HandThumbDownIcon, HandThumbUpIcon, TicketIcon, LanguageIcon,
    TrashIcon, ArrowTrendingDownIcon, ArrowTrendingUpIcon, TruckIcon, ArrowUpTrayIcon,
    UserGroupIcon, UserIcon, ViewColumnsIcon, SquaresPlusIcon,
    ListBulletIcon, SpeakerWaveIcon, WifiIcon, XCircleIcon, MagnifyingGlassPlusIcon, MagnifyingGlassMinusIcon,

    // v1 Aliases for compatibility
    AnnotationIcon: ChatBubbleBottomCenterTextIcon,
    LightningBoltIcon: BoltIcon,
    ChatAlt2Icon: ChatBubbleLeftRightIcon,
    ClipboardListIcon: ClipboardDocumentListIcon,
    CollectionIcon: Squares2X2Icon,
    DesktopComputerIcon: ComputerDesktopIcon,
    DeviceMobileIcon: DevicePhoneMobileIcon,
    EmojiHappyIcon: FaceSmileIcon,
    FastForwardIcon: ForwardIcon,
    GlobeIcon: GlobeAmericasIcon,
    HandIcon: HandRaisedIcon,
    InboxInIcon: InboxArrowDownIcon,
    LocationMarkerIcon: MapPinIcon,
    MailIcon: EnvelopeIcon,
    MenuIcon: Bars3Icon,
    PencilAltIcon: PencilSquareIcon,
    PhotographIcon: PhotoIcon,
    PuzzleIcon: PuzzlePieceIcon,
    RefreshIcon: ArrowPathIcon,
    SearchIcon: MagnifyingGlassIcon,
    SpeakerphoneIcon: MegaphoneIcon,
    SupportIcon: LifebuoyIcon,
    TemplateIcon: RectangleStackIcon,
    TerminalIcon: CommandLineIcon,
    ThumbDownIcon: HandThumbDownIcon,
    ThumbUpIcon: HandThumbUpIcon,
    TranslateIcon: LanguageIcon,
    TrendingDownIcon: ArrowTrendingDownIcon,
    TrendingUpIcon: ArrowTrendingUpIcon,
    UploadIcon: ArrowUpTrayIcon,
    ViewBoardsIcon: ViewColumnsIcon,
    ViewGridAddIcon: SquaresPlusIcon,
    ViewGridIcon: Squares2X2Icon,
    ViewListIcon: ListBulletIcon
  }

  defineOptions({
    name: 'AboutPage'
  })

  const settingsStore = useSettingsStore()
  const aboutImage = sautiAboutpage;

  // Core Values
  const coreValues = ref([])
  const loadingCoreValues = ref(false)

  // Timeline Events
  const timelineEvents = ref([])
  const loadingTimelineEvents = ref(false)

  // Protection Approaches
  const protectionApproaches = ref([])
  const loadingProtectionApproaches = ref(false)

  // Team Members
  const teamMembers = ref([])
  const loadingTeamMembers = ref(false)

  // Services
  const services = ref([])
  const loadingServices = ref(false)

  // Icon components map
  const getIconComponent = (iconName) => {
    const icon = heroicons[`${iconName}Icon`]
    return icon || heroicons['ShieldCheckIcon']
  }

  // Fetch services
  const fetchServices = async () => {
    loadingServices.value = true
    try {
      const response = await api.get('/services/')
      let data = response.data
      if (data && data.results && Array.isArray(data.results)) {
        data = data.results
      }
      services.value = Array.isArray(data) ? data : []
    } catch (error) {
      console.error('Failed to fetch services:', error)
      services.value = []
    } finally {
      loadingServices.value = false
    }
  }

  // Fetch core values
  const fetchCoreValues = async () => {
    loadingCoreValues.value = true
    try {
      const response = await api.get('/content/core-values/')
      let data = response.data
      if (data && data.results && Array.isArray(data.results)) {
        data = data.results
      }
      coreValues.value = Array.isArray(data) ? data : []
    } catch (error) {
      console.error('Failed to fetch core values:', error)
      coreValues.value = []
    } finally {
      loadingCoreValues.value = false
    }
  }

  // Fetch timeline events
  const fetchTimelineEvents = async () => {
    loadingTimelineEvents.value = true
    try {
      const response = await api.get('/content/timeline-events/')
      let data = response.data
      if (data && data.results && Array.isArray(data.results)) {
        data = data.results
      }
      timelineEvents.value = Array.isArray(data) ? data : []
      console.log('Timeline events fetched:', timelineEvents.value.length)
    } catch (error) {
      console.error('Failed to fetch timeline events:', error)
      timelineEvents.value = []
    } finally {
      loadingTimelineEvents.value = false
    }
  }

  // Fetch protection approaches
  const fetchProtectionApproaches = async () => {
    loadingProtectionApproaches.value = true
    try {
      const response = await api.get('/content/protection-approach/')
      let data = response.data
      if (data && data.results && Array.isArray(data.results)) {
        data = data.results
      }
      protectionApproaches.value = Array.isArray(data) ? data : []
    } catch (error) {
      console.error('Failed to fetch protection approaches:', error)
      protectionApproaches.value = []
    } finally {
      loadingProtectionApproaches.value = false
    }
  }

  // Fetch team members
  const fetchTeamMembers = async () => {
    loadingTeamMembers.value = true
    try {
      const response = await api.get('/content/team-members/')
      let data = response.data
      if (data && data.results && Array.isArray(data.results)) {
        data = data.results
      }
      teamMembers.value = Array.isArray(data) ? data : []
    } catch (error) {
      console.error('Failed to fetch team members:', error)
      teamMembers.value = []
    } finally {
      loadingTeamMembers.value = false
    }
  }

  // Computed property to structure About Page sections
  const aboutSections = computed(() => {
    const settings = settingsStore.settings
    const sections = []

    // 1. Hero Section
    const heroData = {
      title: settings.about_hero_title || settings.about_title,
      description: settings.about_hero_description || settings.about_description,
      image: settings.about_hero_image || aboutImage,
      ctaCall: settings.about_hero_cta_call,
      ctaReport: settings.about_hero_cta_report,
      badges: [
        { text: settings.about_hero_badge1_text, class: settings.about_hero_badge1_class },
        { text: settings.about_hero_badge2_text, class: settings.about_hero_badge2_class },
        { text: settings.about_hero_badge3_text, class: settings.about_hero_badge3_class },
      ].filter(b => b.text),
    }
    if (heroData.title || heroData.description || heroData.image) {
      sections.push({
        key: 'hero',
        component: h('section', { class: 'relative overflow-hidden' }, [
          h('div', { class: 'absolute inset-0 bg-gradient-to-b from-white via-white to-gray-50' }),
          h('div', { class: 'container-custom relative py-16 md:py-24' }, [
            h('div', { class: 'grid grid-cols-1 lg:grid-cols-12 gap-10 items-center' }, [
              h('div', { class: 'lg:col-span-7' }, [
                heroData.title ? h('h1', { class: 'mb-4' }, heroData.title) : null,
                heroData.description ? h('p', { class: 'text-xl max-w-2xl', style: 'color: #555555;' }, heroData.description) : null,
                h('div', { class: 'mt-6 flex flex-wrap gap-3' }, [
                  heroData.ctaCall ? h('a', { href: 'tel:116', class: 'pill pill-primary', 'aria-label': 'Call the 116 helpline' }, heroData.ctaCall) : null,
                  heroData.ctaReport ? h(resolveComponent('router-link'), { to: '/report', class: 'pill pill-outline' }, heroData.ctaReport) : null,
                ]),
                h('div', { class: 'mt-6 flex flex-wrap gap-3 text-sm', style: 'color: #555555;' },
                  heroData.badges.map(badge => h('span', { class: badge.class }, badge.text))
                ),
              ]),
              h('div', { class: 'lg:col-span-5' }, [
                heroData.image ? h('div', { class: 'card p-0 overflow-hidden' }, [
                  h('img', { src: heroData.image, alt: heroData.title, class: 'w-full h-72 md:h-96 object-cover' })
                ]) : null,
              ]),
            ]),
          ]),
        ]),
        data: heroData,
      })
    }

    // 2. Identity Section (Who We Are) - Using existing stats for now
    const identityStats = []
    for (let i = 1; i <= 4; i++) {
      const title = settings[`about_stat${i}_title`]
      const text = settings[`about_stat${i}_text`]
      const icon = settings[`about_stat${i}_icon`]
      const colorFrom = settings[`about_stat${i}_color_from`]
      const colorTo = settings[`about_stat${i}_color_to`]
      if (title || text) {
        identityStats.push({ title, text, icon, colorFrom, colorTo })
      }
    }

    if (identityStats.length > 0) {
      sections.push({
        key: 'identity',
        component: h('section', { class: 'section-padding' }, [
          h('div', { class: 'container-custom' }, [
            h('div', { class: 'grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6' },
              identityStats.map(stat =>
                h('div', { class: 'relative group' }, [
                  h('div', { class: `absolute inset-0 bg-gradient-to-br from-${stat.colorFrom || 'blue-500'} to-${stat.colorTo || 'blue-600'} rounded-2xl opacity-90 group-hover:opacity-100 transition-opacity` }),
                  h('div', { class: 'relative p-8 text-center text-white' }, [
                    stat.icon ? h('div', { class: 'mb-3' }, [
                      h(getIconComponent(stat.icon), { class: 'w-12 h-12 mx-auto opacity-80' })
                    ]) : null,
                    stat.title ? h('h3', { class: 'text-4xl font-extrabold mb-2' }, stat.title) : null,
                    stat.text ? h('p', { class: 'text-white/90 text-sm font-medium' }, stat.text) : null,
                  ]),
                ])
              )
            ),
          ]),
        ]),
        data: { stats: identityStats },
      })
    }

    // 3. Services Section (What We Do)
    const servicesTitle = settings.about_services_title || 'Our Comprehensive Support Services'
    const servicesDescription = settings.about_services_description || 'We provide a wide range of support options to ensure every child has access to the help they need.'

    if (services.value.length > 0) {
      sections.push({
        key: 'services',
        component: h('section', { class: 'section-padding bg-gray-50' }, [
          h('div', { class: 'container-custom' }, [
            h('div', { class: 'text-center mb-12' }, [
              h('h2', { class: 'mb-3 font-extrabold text-[#222222]' }, servicesTitle),
              h('p', { class: 'max-w-3xl mx-auto leading-relaxed text-gray-600' }, servicesDescription),
            ]),
            h('div', { class: 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8' }, 
              services.value.map(service => 
                h(AppServiceCard, { 
                  key: service.id, 
                  service: service, 
                  icon: service.icon,
                  color: service.icon === 'phone' ? 'blue' : 
                         service.icon === 'shield' ? 'orange' : 
                         service.icon === 'guidance' ? 'purple' : 
                         service.icon === 'document' ? 'teal' : 
                         service.icon === 'community' ? 'green' : 
                         'blue'
                })
              )
            ),
            h('div', { class: 'mt-16' }, [
              // Core Values Header (Integrated into the same section background)
              settings.about_values_title ? h('h2', { class: 'text-center mb-10 font-extrabold text-[#222222]' }, settings.about_values_title) : null,
              loadingCoreValues.value ? h('div', { class: 'text-center py-8' }, [
                h('div', { class: 'animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto' })
              ]) : h('div', { class: 'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6' },
                coreValues.value.map(value =>
                  h('div', {
                    key: value.id,
                    class: `group relative bg-gradient-to-br from-white rounded-2xl p-6 shadow-lg hover:shadow-2xl transition-all duration-300 border overflow-hidden to-${value.color_from.split('-')[0]}-50/30 border-${value.border_color}/50`
                  }, [
                    h('div', { class: `absolute top-0 right-0 w-32 h-32 rounded-full -mr-16 -mt-16 group-hover:scale-150 transition-transform duration-500 bg-${value.border_color}/20` }),
                    h('div', { class: 'relative' }, [
                      h('div', { class: `inline-flex items-center justify-center h-14 w-14 rounded-xl bg-gradient-to-br text-white mb-4 shadow-lg from-${value.color_from} to-${value.color_to}` }, [
                        h(getIconComponent(value.icon), { class: 'w-7 h-7' })
                      ]),
                      h('h3', { class: 'text-xl font-bold mb-3 text-gray-900' }, value.title),
                      h('p', { class: 'text-sm leading-relaxed', style: 'color: #555555;' }, value.description),
                    ]),
                  ])
                )
              ),
            ]),
          ]),
        ]),
        data: { services: services.value, coreValues: coreValues.value },
      })
    }

    // 4. Impact Section (Why it matters) - Using existing background/journey for now
    const impactData = {
      title: settings.about_impact_title || settings.about_background_title,
      description: settings.about_impact_description,
      items: [],
      note: settings.about_background_note,
    }
    for (let i = 1; i <= 6; i++) {
      const item = settings[`about_background_item${i}`]
      if (item) {
        impactData.items.push(item)
      }
    }

    if (impactData.title || impactData.items.length > 0) {
      sections.push({
        key: 'impact',
        component: h('section', { class: 'section-padding bg-gray-50' }, [
          h('div', { class: 'container-custom' }, [
            impactData.title ? h('h2', { class: 'text-center mb-4' }, impactData.title) : null,
            impactData.description ? h('p', { class: 'text-center max-w-3xl mx-auto mb-8', style: 'color: #555555;' }, impactData.description) : null,
            h('div', { class: 'max-w-5xl mx-auto' }, [
              h('ul', { class: 'space-y-4 text-lg', style: 'color: #222222;' },
                impactData.items.map(item => h('li', item))
              ),
              impactData.note ? h('p', { class: 'text-sm mt-6', style: 'color: #555555;' }, impactData.note) : null,
            ]),
          ]),
        ]),
        data: impactData,
      })
    }

    // Our Journey (Milestones) - Dynamic from API
    if (timelineEvents.value.length > 0) {
      sections.push({
        key: 'timeline',
        component: h('section', { class: 'section-padding' }, [
          h('div', { class: 'container-custom' }, [
            h('h2', { class: 'text-center mb-12' }, settings.about_timeline_title || 'Our Journey'),
            loadingTimelineEvents.value ? h('div', { class: 'text-center py-8' }, [
              h('div', { class: 'animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto' })
            ]) : (
              console.log('Timeline Events being passed to AppTimeline:', timelineEvents.value),
              h(AppTimeline, { timelineEvents: timelineEvents.value })
            ),
          ]),
        ]),
        data: { timelineEvents: timelineEvents.value },
      })
    }

    // 5. Protection Approach Section (How We Work) - Dynamic from API
    if (protectionApproaches.value.length > 0) {
      sections.push({
        key: 'protection_approach',
        component: h('section', { class: 'section-padding bg-gray-50' }, [
          h('div', { class: 'container-custom' }, [
            h('h2', { class: 'text-center mb-12' }, settings.about_protection_approach_title || 'Our Protection Approach'),
            loadingProtectionApproaches.value ? h('div', { class: 'text-center py-8' }, [
              h('div', { class: 'animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto' })
            ]) : h('div', { class: 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8' },
              protectionApproaches.value.map(approach =>
                h('div', { key: approach.id, class: 'card p-6 text-center' }, [
                  h('div', { class: 'flex items-center justify-center w-16 h-16 rounded-full bg-blue-100 text-blue-600 mx-auto mb-4' }, [
                    h(getIconComponent(approach.icon), { class: 'w-8 h-8' })
                  ]),
                  h('h3', { class: 'text-xl font-bold mb-2' }, approach.title),
                  h('p', { class: 'text-gray-700' }, approach.description),
                ])
              )
            ),
          ]),
        ]),
        data: { protectionApproaches: protectionApproaches.value },
      })
    }

    // 6. Team Section - Dynamic from API
    if (teamMembers.value.length > 0) {
      sections.push({
        key: 'team',
        component: h('section', { class: 'section-padding' }, [
          h('div', { class: 'container-custom' }, [
            h('h2', { class: 'text-center mb-12' }, settings.about_team_title || 'Meet Our Team'),
            loadingTeamMembers.value ? h('div', { class: 'text-center py-8' }, [
              h('div', { class: 'animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto' })
            ]) : h('div', { class: 'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8' },
              teamMembers.value.map(member =>
                h('div', { key: member.id, class: 'card p-6 text-center' }, [
                  member.image ? h('img', { src: member.image, alt: member.name, class: 'w-32 h-32 rounded-full mx-auto mb-4 object-cover' }) : null,
                  h('h3', { class: 'text-xl font-bold text-gray-900' }, member.name),
                  h('p', { class: 'text-blue-600 font-medium mb-2' }, member.role),
                  member.bio ? h('p', { class: 'text-gray-700 text-sm' }, member.bio) : null,
                ])
              )
            ),
          ]),
        ]),
        data: { teamMembers: teamMembers.value },
      })
    }

    // 7. Trust Signals (Partners)
    const trustSignalsData = {
      title: settings.about_trust_signals_title || settings.about_partners_title,
      description: settings.about_trust_signals_description || settings.about_partners_text,
      partners: [],
    }
    for (let i = 1; i <= 4; i++) {
      const partner = settings[`about_partner${i}`]
      if (partner) {
        trustSignalsData.partners.push(partner)
      }
    }

    if (trustSignalsData.title || trustSignalsData.partners.length > 0) {
      sections.push({
        key: 'trust_signals',
        component: h('section', { class: 'section-padding' }, [
          h('div', { class: 'container-custom' }, [
            trustSignalsData.title ? h('h2', { class: 'text-center mb-8' }, trustSignalsData.title) : null,
            h('div', { class: 'grid grid-cols-2 md:grid-cols-4 gap-6 items-center' },
              trustSignalsData.partners.map(partner =>
                h('div', { class: 'card p-6 text-center' }, partner)
              )
            ),
            trustSignalsData.description ? h('p', { class: 'text-center text-sm mt-6', style: 'color: #555555;' }, trustSignalsData.description) : null,
          ]),
        ]),
        data: trustSignalsData,
      })
    }

    // 8. Call to Action
    const ctaData = {
      title: settings.about_cta_title,
      description: settings.about_cta_text,
      ctaCall: settings.about_cta_call,
      ctaReport: settings.about_cta_report,
      ctaContact: settings.about_cta_contact,
    }
    if (ctaData.title || ctaData.description) {
      sections.push({
        key: 'call_to_action',
        component: h('section', { class: 'section-padding' }, [
          h('div', { class: 'container-custom text-center' }, [
            ctaData.title ? h('h2', { class: 'mb-3' }, ctaData.title) : null,
            ctaData.description ? h('p', { class: 'max-w-2xl mx-auto', style: 'color: #555555;' }, ctaData.description) : null,
            h('div', { class: 'mt-6 flex flex-wrap justify-center gap-3' }, [
              ctaData.ctaCall ? h('a', { href: 'tel:116', class: 'pill pill-primary' }, ctaData.ctaCall) : null,
              ctaData.ctaReport ? h(resolveComponent('router-link'), { to: '/report', class: 'pill pill-outline' }, ctaData.ctaReport) : null,
              ctaData.ctaContact ? h(resolveComponent('router-link'), { to: '/contact', class: 'pill pill-light' }, ctaData.ctaContact) : null,
            ]),
          ]),
        ]),
        data: ctaData,
      })
    }

    return sections
  })

  onMounted(async () => {
    await settingsStore.fetchGlobalSettings()
    await fetchCoreValues()
    await fetchTimelineEvents()
    await fetchProtectionApproaches()
    await fetchTeamMembers()
    await fetchServices()
  })
</script>

<style scoped>
  /* Add any component-specific styles here */
</style>
