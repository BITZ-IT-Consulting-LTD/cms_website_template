<template>
  <div class="min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <h1 class="page-header-title">
          Our Operational <span class="text-primary">Excellence</span>
        </h1>
        <p class="page-header-subtitle">
          {{ operationsSubtitle }}
        </p>
      </div>
    </header>

    <div class="section-padding !pt-0">
      <div class="container-custom">
        <!-- Operations in a Flash (Flash Pattern) -->
        <section class="bg-primary/5 p-8 md:p-12 rounded-[3rem] border-2 border-primary/10 mb-16 shadow-sm">
          <h2 class="campaign-header text-xl text-primary mb-8 flex items-center gap-3">
            <ShieldCheckIcon class="w-6 h-6 text-primary" />
            Operations at a Glance
          </h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
            <div class="space-y-4">
              <p class="text-black font-bold text-lg">Real-Time Response</p>
              <p class="text-muted text-sm leading-relaxed">Our call center in Kampala is <strong>active
                  24/7</strong> with certified counselors.</p>
            </div>
            <div class="space-y-4">
              <p class="text-black font-bold text-lg">Multi-Channel Intake</p>
              <p class="text-muted text-sm leading-relaxed">We process reports from <strong>Phone, WhatsApp, SMS,
                  and Walk-ins</strong>.</p>
            </div>
            <div class="space-y-4">
              <p class="text-black font-bold text-lg">Expert Oversight</p>
              <p class="text-muted text-sm leading-relaxed">Every case is reviewed and verified by <strong>MGLSD
                  protection leads</strong>.</p>
            </div>
          </div>
        </section>
      </div>

      <div>
        <!-- 2. Main Visual -->
        <section aria-label="Process Overview" class="section-padding bg-neutral-white">
          <div class="container-custom">
            <div
              class="relative bg-neutral-white rounded-[4rem] shadow-2xl border-2 border-primary overflow-hidden group max-w-6xl mx-auto">
              <img src="@/assets/helpline-center.png" alt="Sauti 116 Helpline Operations Center"
                class="w-full h-[400px] md:h-[600px] object-cover transition-transform duration-700 group-hover:scale-105" />
              <!-- Brand Overlay -->
              <div class="absolute inset-0 bg-gradient-to-t from-secondary/40 via-transparent to-transparent"></div>
              <div class="absolute bottom-12 left-12">
                <div class="pill bg-primary text-neutral-white shadow-xl">Live Operations</div>
              </div>
            </div>
          </div>
        </section>

        <!-- 3. Path to Resolution -->
        <section aria-labelledby="path-heading" class="section-padding bg-primary/5">
          <div class="container-custom">
            <div class="text-center mb-20">
              <h2 id="path-heading" class="campaign-header text-4xl text-secondary mb-6">{{ operationsPathTitle }}</h2>
              <p class="text-xl text-black max-w-2xl mx-auto font-bold opacity-70">{{ operationsPathSubtitle }}</p>
            </div>

            <!-- Desktop Flow - Horizontal -->
            <div class="hidden lg:block relative mb-32">
              <!-- Animated Connecting Line -->
              <div class="absolute top-10 left-0 right-0 h-1.5 bg-primary/10 rounded-full"
                style="width: 75%; margin-left: 12.5%;"></div>

              <div
                class="absolute top-10 left-0 h-1.5 bg-gradient-to-r from-primary via-hotline via-secondary-light to-primary rounded-full progress-bar transition-all"
                style="width: 75%; margin-left: 12.5%;"></div>

              <div class="grid grid-cols-4 gap-4 relative">
                <div v-for="(step, idx) in [
                  { title: operationsStep1Title, text: operationsStep1Text, tag: operationsStep1Tag, colorToken: 'primary', icon: PhoneIcon },
                  { title: operationsStep2Title, text: operationsStep2Text, tag: operationsStep2Tag, colorToken: 'hotline', icon: UserGroupIcon },
                  { title: operationsStep3Title, text: operationsStep3Text, tag: operationsStep3Tag, colorToken: 'secondary-light', icon: DocumentTextIcon },
                  { title: operationsStep4Title, text: operationsStep4Text, tag: operationsStep4Tag, colorToken: 'primary', icon: CheckBadgeIcon }
                ]" :key="idx" class="flex flex-col items-center group">
                  <div
                    :class="['w-20 h-20 rounded-3xl flex items-center justify-center text-neutral-white font-bold text-3xl shadow-xl mb-12 relative z-10 transition-transform group-hover:scale-110', `bg-${step.colorToken}`]">
                    {{ idx + 1 }}
                  </div>
                  <div class="card-base h-full group-hover:border-secondary">
                    <div
                      :class="['w-12 h-12 bg-neutral-white rounded-xl flex items-center justify-center mb-6 shadow-sm border-2', `border-${step.colorToken}/20 text-${step.colorToken}`]">
                      <component :is="step.icon" class="w-7 h-7" />
                    </div>
                    <h4 class="campaign-header text-xl text-secondary mb-4">{{ step.title }}</h4>
                    <p class="text-black/70 font-bold text-sm leading-relaxed mb-6">{{ step.text }}</p>
                    <div
                      :class="['pill text-[10px] font-bold uppercase tracking-widest', `bg-${step.colorToken}/10 text-${step.colorToken}`]">
                      {{ step.tag }}
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Mobile Flow - Vertical -->
            <div class="lg:hidden space-y-6">
              <div v-for="(step, idx) in [
                { title: operationsStep1Title, text: operationsStep1Text, tag: operationsStep1Tag, colorToken: 'primary', icon: PhoneIcon },
                { title: operationsStep2Title, text: operationsStep2Text, tag: operationsStep2Tag, colorToken: 'hotline', icon: UserGroupIcon },
                { title: operationsStep3Title, text: operationsStep3Text, tag: operationsStep3Tag, colorToken: 'secondary-light', icon: DocumentTextIcon },
                { title: operationsStep4Title, text: operationsStep4Text, tag: operationsStep4Tag, colorToken: 'primary', icon: CheckBadgeIcon }
              ]" :key="idx" class="relative pl-12">
                <div class="absolute left-4 top-10 bottom-0 w-1 bg-primary/10" v-if="idx < 3"></div>
                <div
                  :class="['absolute left-0 top-0 w-8 h-8 rounded-full flex items-center justify-center text-neutral-white font-bold text-sm z-10', `bg-${step.colorToken}`]">
                  {{ idx + 1 }}
                </div>
                <div class="card-base">
                  <div class="flex items-center gap-4 mb-4">
                    <div
                      :class="['w-10 h-10 bg-neutral-white rounded-xl flex items-center justify-center shadow-sm border', `text-${step.colorToken}`]">
                      <component :is="step.icon" class="w-6 h-6" />
                    </div>
                    <h4 class="campaign-header text-xl text-secondary leading-none">{{ step.title }}</h4>
                  </div>
                  <p class="text-black/70 font-bold text-sm leading-relaxed mb-6">{{ step.text }}</p>
                  <div
                    :class="['pill inline-flex text-[10px] font-bold uppercase tracking-widest', `bg-${step.colorToken}/10 text-${step.colorToken}`]">
                    {{ step.tag }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- 4. Key Metrics Banner -->
        <section aria-label="Key Metrics" class="section-padding bg-neutral-white">
          <div class="container-custom">
            <div
              class="bg-secondary rounded-[4rem] p-12 md:p-20 text-neutral-white shadow-2xl relative overflow-hidden">
              <div class="absolute -left-20 -top-20 w-80 h-80 bg-primary/10 rounded-full blur-3xl"></div>
              <div class="relative z-10 grid grid-cols-1 md:grid-cols-3 gap-16 md:gap-12 text-center">
                <div class="space-y-4">
                  <div class="text-6xl md:text-8xl font-bold text-primary">{{ operationsMetrics1Title }}</div>
                  <div class="campaign-header text-lg text-neutral-white/60">{{ operationsMetrics1Text }}</div>
                </div>
                <div class="space-y-4 relative">
                  <div class="hidden md:block absolute -left-6 top-1/2 -translate-y-1/2 w-px h-16 bg-white/10"></div>
                  <div class="text-6xl md:text-8xl font-bold text-hotline">{{ operationsMetrics2Title }}</div>
                  <div class="campaign-header text-lg text-neutral-white/60">{{ operationsMetrics2Text }}</div>
                  <div class="hidden md:block absolute -right-6 top-1/2 -translate-y-1/2 w-px h-16 bg-white/10"></div>
                </div>
                <div class="space-y-4">
                  <div class="text-6xl md:text-8xl font-bold text-secondary-light">{{ operationsMetrics3Title }}</div>
                  <div class="campaign-header text-lg text-neutral-white/60">{{ operationsMetrics3Text }}</div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- 5. Operational Highlights -->
        <section aria-labelledby="highlights-heading" class="section-padding bg-neutral-offwhite">
          <div class="container-custom">
            <h3 id="highlights-heading" class="campaign-header text-4xl text-center text-secondary mb-16">{{
              operationsHighlightsTitle }}</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              <div v-for="(h, idx) in [
                { title: operationsHighlight1Title, text: operationsHighlight1Text, colorToken: 'primary' },
                { title: operationsHighlight2Title, text: operationsHighlight2Text, colorToken: 'hotline' },
                { title: operationsHighlight3Title, text: operationsHighlight3Text, colorToken: 'secondary-light' },
                { title: operationsHighlight4Title, text: operationsHighlight4Text, colorToken: 'hotline' },
                { title: operationsHighlight5Title, text: operationsHighlight5Text, colorToken: 'primary' },
                { title: operationsHighlight6Title, text: operationsHighlight6Text, colorToken: 'hotline' }
              ]" :key="idx" class="card-base group hover:border-secondary">
                <div
                  :class="['w-12 h-12 rounded-2xl mb-6 flex items-center justify-center text-neutral-white shadow-xl group-hover:scale-110 transition-transform', `bg-${h.colorToken}`]">
                  <CheckIcon class="w-6 h-6" stroke-width="3" />
                </div>
                <h4 class="campaign-header text-2xl text-secondary mb-4 leading-tight">{{ h.title }}</h4>
                <p class="text-muted font-bold text-lg leading-relaxed">{{ h.text }}</p>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { computed, onMounted } from 'vue'
  import { useSettingsStore } from '@/store/settings'
  import operationsImage from '@/assets/operations-case-flow.jpg'
  import {
    PhoneIcon,
    UserGroupIcon,
    DocumentTextIcon,
    CheckBadgeIcon,
    CheckIcon,
    ShieldCheckIcon
  } from '@heroicons/vue/24/outline'

  defineOptions({
    name: 'OperationsPage'
  })

  const settingsStore = useSettingsStore()

  onMounted(() => {
    settingsStore.fetchGlobalSettings()
  })

  const operationsSubtitle = computed(() => settingsStore.settings.operations_subtitle || 'A transparent look into how we handle every call to ensure every child\'s voice is heard and acted upon with care and urgency.')
  const operationsPathTitle = computed(() => settingsStore.settings.operations_path_title || 'The Path to Resolution')
  const operationsPathSubtitle = computed(() => settingsStore.settings.operations_path_subtitle || 'Our streamlined process from report to resolution, ensuring every case receives the attention and action it deserves.')
  const operationsStep1Title = computed(() => settingsStore.settings.operations_step_1_title || 'Initial Contact')
  const operationsStep1Text = computed(() => settingsStore.settings.operations_step_1_text || 'A child or concerned individual calls the toll-free 116 helpline or reaches out via WhatsApp.')
  const operationsStep1Tag = computed(() => settingsStore.settings.operations_step_1_tag || 'Immediate Response')
  const operationsStep2Title = computed(() => settingsStore.settings.operations_step_2_title || 'Counselor Support')
  const operationsStep2Text = computed(() => settingsStore.settings.operations_step_2_text || 'Trained counselors provide immediate emotional support and gather essential information with empathy.')
  const operationsStep2Tag = computed(() => settingsStore.settings.operations_step_2_tag || 'Professional Care')
  const operationsStep3Title = computed(() => settingsStore.settings.operations_step_3_title || 'Case Assessment')
  const operationsStep3Text = computed(() => settingsStore.settings.operations_step_3_text || 'The case is documented, assessed for urgency level, and classified according to protection needs.')
  const operationsStep3Tag = computed(() => settingsStore.settings.operations_step_3_tag || 'Detailed Documentation')
  const operationsStep4Title = computed(() => settingsStore.settings.operations_step_4_title || 'Referral & Follow-up')
  const operationsStep4Text = computed(() => settingsStore.settings.operations_step_4_text || 'Referrals are made to relevant authorities and continuous follow-up ensures case resolution.')
  const operationsStep4Tag = computed(() => settingsStore.settings.operations_step_4_tag || 'Action & Closure')
  const operationsMetrics1Title = computed(() => settingsStore.settings.operations_metrics_1_title || '24/7')
  const operationsMetrics1Text = computed(() => settingsStore.settings.operations_metrics_1_text || 'Always Available')
  const operationsMetrics2Title = computed(() => settingsStore.settings.operations_metrics_2_title || '100%')
  const operationsMetrics2Text = computed(() => settingsStore.settings.operations_metrics_2_text || 'Confidential')
  const operationsMetrics3Title = computed(() => settingsStore.settings.operations_metrics_3_title || 'Free')
  const operationsMetrics3Text = computed(() => settingsStore.settings.operations_metrics_3_text || 'Toll-Free Service')
  const operationsHighlightsTitle = computed(() => settingsStore.settings.operations_highlights_title || 'Operational Highlights')
  const operationsHighlight1Title = computed(() => settingsStore.settings.operations_highlight_1_title || '116 Toll-Free Helpline')
  const operationsHighlight1Text = computed(() => settingsStore.settings.operations_highlight_1_text || 'Accessible nationwide across all telecom networks.')
  const operationsHighlight2Title = computed(() => settingsStore.settings.operations_highlight_2_title || '24/7 Availability')
  const operationsHighlight2Text = computed(() => settingsStore.settings.operations_highlight_2_text || 'Help any time of day, all year round.')
  const operationsHighlight3Title = computed(() => settingsStore.settings.operations_highlight_3_title || 'Language Support')
  const operationsHighlight3Text = computed(() => settingsStore.settings.operations_highlight_3_text || 'English, Luganda, Swahili, and additional local languages.')
  const operationsHighlight4Title = computed(() => settingsStore.settings.operations_highlight_4_title || 'Strict Confidentiality')
  const operationsHighlight4Text = computed(() => settingsStore.settings.operations_highlight_4_text || 'Handled with the utmost privacy.')
  const operationsHighlight5Title = computed(() => settingsStore.settings.operations_highlight_5_title || 'Trained Professionals')
  const operationsHighlight5Text = computed(() => settingsStore.settings.operations_highlight_5_text || 'Counselors undergo rigorous training.')
  const operationsHighlight6Title = computed(() => settingsStore.settings.operations_highlight_6_title || 'Multiple Channels')
  const operationsHighlight6Text = computed(() => settingsStore.settings.operations_highlight_6_text || 'WhatsApp, U-Report, SafePal App, email, and walk-ins.')
</script>

<style scoped>
  @keyframes progress-bar {
    0% {
      transform: scaleX(0);
      opacity: 0;
    }

    50% {
      opacity: 1;
    }

    100% {
      transform: scaleX(1);
      opacity: 0.8;
    }
  }

  .progress-bar {
    animation: progress-bar 3s ease-in-out infinite;
    transform-origin: left;
  }
</style>
