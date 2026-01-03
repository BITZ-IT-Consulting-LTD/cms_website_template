<template>
  <div class="bg-sauti-neutral min-h-screen">
    <section class="py-16 md:py-24">
      <div class="container-custom text-center">
        <h1 class="text-4xl md:text-5xl lg:text-7xl font-black text-sauti-darkGreen mb-4 tracking-tight">
          Our Operational <span class="text-sauti-blue">Excellence</span>
        </h1>
        <p class="text-xl text-sauti-darkGreen/70 font-medium max-w-3xl mx-auto leading-relaxed">{{ operationsSubtitle
          }}</p>
      </div>
    </section>

    <section class="pb-16 md:pb-24">
      <div class="container-custom">
        <div
          class="bg-sauti-white rounded-[4rem] shadow-2xl shadow-sauti-blue/5 border-4 border-sauti-neutral overflow-hidden group">
          <img :src="operationsImage" alt="Our operations and case flow - Sauti 116 helpline process diagram"
            class="w-full h-[400px] md:h-[600px] object-cover transition-transform duration-700 group-hover:scale-105" />
        </div>
      </div>
    </section>

    <section class="py-16 md:py-24 bg-sauti-white rounded-[5rem] shadow-inner">
      <div class="container-custom">
        <div class="text-center mb-20">
          <h2 class="text-3xl md:text-5xl font-black text-sauti-darkGreen mb-4">{{ operationsPathTitle }}</h2>
          <p class="text-lg text-sauti-darkGreen/60 font-bold max-w-2xl mx-auto">{{ operationsPathSubtitle }}</p>
        </div>

        <!-- Desktop Flow - Horizontal with connecting lines -->
        <div class="hidden lg:block relative mb-32">
          <!-- Animated Connecting Line -->
          <div class="absolute top-24 left-0 right-0 h-2 bg-sauti-neutral rounded-full"
            style="width: 75%; margin-left: 12.5%;"></div>

          <div
            class="absolute top-24 left-0 h-2 bg-gradient-to-r from-sauti-blue via-sauti-orange via-sauti-lightGreen to-sauti-red rounded-full progress-bar opacity-30"
            style="width: 75%; margin-left: 12.5%;"></div>

          <!-- Arrow Indicators Between Steps -->
          <div class="absolute top-20 left-[31.25%] transform -translate-x-1/2">
            <div
              class="w-10 h-10 bg-sauti-white rounded-full flex items-center justify-center border-2 border-sauti-neutral text-sauti-blue animate-bounce-slow">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </div>
          </div>
          <div class="absolute top-20 left-[50%] transform -translate-x-1/2">
            <div
              class="w-10 h-10 bg-sauti-white rounded-full flex items-center justify-center border-2 border-sauti-neutral text-sauti-orange animate-bounce-slow"
              style="animation-delay: 0.2s">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </div>
          </div>
          <div class="absolute top-20 left-[68.75%] transform -translate-x-1/2">
            <div
              class="w-10 h-10 bg-sauti-white rounded-full flex items-center justify-center border-2 border-sauti-neutral text-sauti-lightGreen animate-bounce-slow"
              style="animation-delay: 0.4s">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </div>
          </div>

          <div class="grid grid-cols-4 gap-4 relative">
            <!-- Step 1: Initial Contact -->
            <div class="flex flex-col items-center group">
              <div
                class="w-20 h-20 rounded-3xl bg-sauti-blue flex items-center justify-center text-sauti-white font-black text-3xl shadow-xl shadow-sauti-blue/30 mb-8 relative z-10 transition-transform group-hover:scale-110">
                1</div>
              <div
                class="bg-sauti-neutral/30 p-8 rounded-[3rem] border-2 border-sauti-neutral h-full transition-all group-hover:bg-sauti-white group-hover:border-sauti-blue group-hover:shadow-2xl group-hover:shadow-sauti-blue/10">
                <div
                  class="w-12 h-12 bg-sauti-white rounded-xl flex items-center justify-center text-sauti-blue mb-6 shadow-sm">
                  <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                      d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                  </svg>
                </div>
                <h4 class="text-xl font-black text-sauti-darkGreen mb-3">{{ operationsStep1Title }}</h4>
                <p class="text-sauti-darkGreen/70 font-bold text-sm leading-relaxed mb-4">{{ operationsStep1Text }}</p>
                <div class="inline-flex items-center gap-2 px-3 py-1 bg-sauti-blue/10 rounded-full">
                  <span class="w-1.5 h-1.5 bg-sauti-blue rounded-full animate-pulse"></span>
                  <span class="text-[10px] uppercase font-black tracking-widest text-sauti-blue">{{ operationsStep1Tag
                    }}</span>
                </div>
              </div>
            </div>

            <!-- Step 2: Counselor Support -->
            <div class="flex flex-col items-center group">
              <div
                class="w-20 h-20 rounded-3xl bg-sauti-orange flex items-center justify-center text-sauti-white font-black text-3xl shadow-xl shadow-sauti-orange/30 mb-8 relative z-10 transition-transform group-hover:scale-110">
                2</div>
              <div
                class="bg-sauti-neutral/30 p-8 rounded-[3rem] border-2 border-sauti-neutral h-full transition-all group-hover:bg-sauti-white group-hover:border-sauti-orange group-hover:shadow-2xl group-hover:shadow-sauti-orange/10">
                <div
                  class="w-12 h-12 bg-sauti-white rounded-xl flex items-center justify-center text-sauti-orange mb-6 shadow-sm">
                  <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                      d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                  </svg>
                </div>
                <h4 class="text-xl font-black text-sauti-darkGreen mb-3">{{ operationsStep2Title }}</h4>
                <p class="text-sauti-darkGreen/70 font-bold text-sm leading-relaxed mb-4">{{ operationsStep2Text }}</p>
                <div class="inline-flex items-center gap-2 px-3 py-1 bg-sauti-orange/10 rounded-full">
                  <span class="w-1.5 h-1.5 bg-sauti-orange rounded-full animate-pulse"></span>
                  <span class="text-[10px] uppercase font-black tracking-widest text-sauti-orange">{{ operationsStep2Tag
                    }}</span>
                </div>
              </div>
            </div>

            <!-- Step 3: Case Assessment -->
            <div class="flex flex-col items-center group">
              <div
                class="w-20 h-20 rounded-3xl bg-sauti-lightGreen flex items-center justify-center text-sauti-white font-black text-3xl shadow-xl shadow-sauti-lightGreen/30 mb-8 relative z-10 transition-transform group-hover:scale-110">
                3</div>
              <div
                class="bg-sauti-neutral/30 p-8 rounded-[3rem] border-2 border-sauti-neutral h-full transition-all group-hover:bg-sauti-white group-hover:border-sauti-lightGreen group-hover:shadow-2xl group-hover:shadow-sauti-lightGreen/10">
                <div
                  class="w-12 h-12 bg-sauti-white rounded-xl flex items-center justify-center text-sauti-lightGreen mb-6 shadow-sm">
                  <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                      d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
                  </svg>
                </div>
                <h4 class="text-xl font-black text-sauti-darkGreen mb-3">{{ operationsStep3Title }}</h4>
                <p class="text-sauti-darkGreen/70 font-bold text-sm leading-relaxed mb-4">{{ operationsStep3Text }}</p>
                <div class="inline-flex items-center gap-2 px-3 py-1 bg-sauti-lightGreen/10 rounded-full">
                  <span class="w-1.5 h-1.5 bg-sauti-lightGreen rounded-full animate-pulse"></span>
                  <span class="text-[10px] uppercase font-black tracking-widest text-sauti-lightGreen">{{
                    operationsStep3Tag }}</span>
                </div>
              </div>
            </div>

            <!-- Step 4: Referral & Follow-up -->
            <div class="flex flex-col items-center group">
              <div
                class="w-20 h-20 rounded-3xl bg-sauti-red flex items-center justify-center text-sauti-white font-black text-3xl shadow-xl shadow-sauti-red/30 mb-8 relative z-10 transition-transform group-hover:scale-110">
                4</div>
              <div
                class="bg-sauti-neutral/30 p-8 rounded-[3rem] border-2 border-sauti-neutral h-full transition-all group-hover:bg-sauti-white group-hover:border-sauti-red group-hover:shadow-2xl group-hover:shadow-sauti-red/10">
                <div
                  class="w-12 h-12 bg-sauti-white rounded-xl flex items-center justify-center text-sauti-red mb-6 shadow-sm">
                  <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                      d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <h4 class="text-xl font-black text-sauti-darkGreen mb-3">{{ operationsStep4Title }}</h4>
                <p class="text-sauti-darkGreen/70 font-bold text-sm leading-relaxed mb-4">{{ operationsStep4Text }}</p>
                <div class="inline-flex items-center gap-2 px-3 py-1 bg-sauti-red/10 rounded-full">
                  <span class="w-1.5 h-1.5 bg-sauti-red rounded-full animate-pulse"></span>
                  <span class="text-[10px] uppercase font-black tracking-widest text-sauti-red">{{ operationsStep4Tag
                    }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Mobile Flow - Vertical -->
        <div class="md:hidden space-y-6">
          <div v-for="(step, idx) in [
            { title: operationsStep1Title, text: operationsStep1Text, tag: operationsStep1Tag, color: 'sauti-blue', icon: 'M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z' },
            { title: operationsStep2Title, text: operationsStep2Text, tag: operationsStep2Tag, color: 'sauti-orange', icon: 'M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z' },
            { title: operationsStep3Title, text: operationsStep3Text, tag: operationsStep3Tag, color: 'sauti-lightGreen', icon: 'M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01' },
            { title: operationsStep4Title, text: operationsStep4Text, tag: operationsStep4Tag, color: 'sauti-red', icon: 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z' }
          ]" :key="idx" class="relative pl-12">
            <div class="absolute left-4 top-10 bottom-0 w-1 bg-sauti-neutral" v-if="idx < 3"></div>
            <div
              :class="['absolute left-0 top-0 w-8 h-8 rounded-full flex items-center justify-center text-sauti-white font-black text-sm z-10', `bg-${step.color}`]">
              {{ idx + 1 }}
            </div>
            <div class="bg-sauti-neutral/30 p-6 rounded-3xl border-2 border-sauti-neutral">
              <div class="flex items-center gap-4 mb-4">
                <div
                  :class="['w-10 h-10 bg-sauti-white rounded-xl flex items-center justify-center shadow-sm', `text-${step.color}`]">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" :d="step.icon" />
                  </svg>
                </div>
                <h4 class="text-xl font-black text-sauti-darkGreen leading-none">{{ step.title }}</h4>
              </div>
              <p class="text-sauti-darkGreen/70 font-bold text-sm leading-relaxed mb-4">{{ step.text }}</p>
              <div
                :class="['inline-flex items-center gap-2 px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest', `bg-${step.color}/10`, `text-${step.color}`]">
                {{ step.tag }}
              </div>
            </div>
          </div>
        </div>

        <!-- Key Metrics Banner -->
        <div class="mt-24 bg-sauti-darkGreen rounded-[3rem] p-12 text-sauti-white shadow-2xl shadow-sauti-darkGreen/20">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-12 text-center">
            <div class="space-y-2">
              <div class="text-6xl font-black text-sauti-blue">{{ operationsMetrics1Title }}</div>
              <div class="text-lg font-bold text-sauti-white/60 tracking-widest uppercase">{{ operationsMetrics1Text }}
              </div>
            </div>
            <div class="space-y-2 relative">
              <div class="hidden md:block absolute -left-6 top-1/2 -translate-y-1/2 w-0.5 h-12 bg-sauti-white/10"></div>
              <div class="text-6xl font-black text-sauti-orange">{{ operationsMetrics2Title }}</div>
              <div class="text-lg font-bold text-sauti-white/60 tracking-widest uppercase">{{ operationsMetrics2Text }}
              </div>
              <div class="hidden md:block absolute -right-6 top-1/2 -translate-y-1/2 w-0.5 h-12 bg-sauti-white/10">
              </div>
            </div>
            <div class="space-y-2">
              <div class="text-6xl font-black text-sauti-lightGreen">{{ operationsMetrics3Title }}</div>
              <div class="text-lg font-bold text-sauti-white/60 tracking-widest uppercase">{{ operationsMetrics3Text }}
              </div>
            </div>
          </div>
        </div>


      </div>
    </section>

    <section class="py-16 md:py-24">
      <div class="container-custom">
        <h3 class="text-4xl md:text-5xl font-black text-center text-sauti-darkGreen mb-16">{{ operationsHighlightsTitle
          }}</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="(h, idx) in [
            { title: operationsHighlight1Title, text: operationsHighlight1Text, color: 'sauti-blue' },
            { title: operationsHighlight2Title, text: operationsHighlight2Text, color: 'sauti-orange' },
            { title: operationsHighlight3Title, text: operationsHighlight3Text, color: 'sauti-lightGreen' },
            { title: operationsHighlight4Title, text: operationsHighlight4Text, color: 'sauti-red' },
            { title: operationsHighlight5Title, text: operationsHighlight5Text, color: 'sauti-blue' },
            { title: operationsHighlight6Title, text: operationsHighlight6Text, color: 'sauti-orange' }
          ]" :key="idx"
            class="group bg-sauti-white p-10 rounded-[3rem] border-2 border-sauti-neutral transition-all duration-300 hover:border-sauti-darkGreen hover:shadow-2xl hover:shadow-sauti-darkGreen/5">
            <div
              :class="['w-12 h-12 rounded-2xl mb-6 flex items-center justify-center text-sauti-white shadow-lg', `bg-${h.color}`]">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
              </svg>
            </div>
            <h4 class="text-2xl font-black text-sauti-darkGreen mb-4">{{ h.title }}</h4>
            <p class="text-sauti-darkGreen/60 font-bold text-lg leading-relaxed">{{ h.text }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
  import { computed, onMounted } from 'vue'
  import { useSettingsStore } from '@/store/settings'
  import operationsImage from '@/assets/operations-case-flow.jpg'

  defineOptions({
    name: 'OperationsPage'
  })

  const settingsStore = useSettingsStore()



  onMounted(() => {
    settingsStore.fetchGlobalSettings()
  })

  const operationsTitle = computed(() => settingsStore.settings.operations_title || 'Our Operations and Case Flow')
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

  /* Custom animations for Path to Resolution */
  @keyframes progress-bar {
    0% {
      width: 0%;
      opacity: 0.6;
    }

    50% {
      opacity: 1;
    }

    100% {
      width: 85%;
      opacity: 0.8;
    }
  }

  @keyframes bounce-slow {

    0%,
    100% {
      transform: translateX(0);
    }

    50% {
      transform: translateX(10px);
    }
  }

  @keyframes float {

    0%,
    100% {
      transform: translateY(0);
    }

    50% {
      transform: translateY(-10px);
    }
  }

  @keyframes pulse-glow {

    0%,
    100% {
      box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }

    50% {
      box-shadow: 0 8px 24px rgba(59, 130, 246, 0.6);
    }
  }

  .progress-bar {
    animation: progress-bar 3s ease-in-out infinite;
  }

  .animate-bounce-slow {
    animation: bounce-slow 2s ease-in-out infinite;
  }

  /* Add floating animation to step icons */
  .bg-white.rounded-2xl:hover .w-24.h-24 {
    animation: float 2s ease-in-out infinite;
  }

  /* Add glow effect to step numbers on hover */
  .bg-white.rounded-2xl:hover .w-16.h-16 {
    animation: pulse-glow 2s ease-in-out infinite;
  }

  /* Decorative background patterns */
  .section-padding.bg-gradient-to-b {
    background-image:
      radial-gradient(circle at 20% 30%, rgba(59, 130, 246, 0.03) 0%, transparent 50%),
      radial-gradient(circle at 80% 70%, rgba(168, 85, 247, 0.03) 0%, transparent 50%);
  }
</style>
