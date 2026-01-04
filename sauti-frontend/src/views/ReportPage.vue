<template>
  <div class="bg-sauti-white min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <h1 class="page-header-title">
          Report <span class="text-sauti-blue">a Case</span>
        </h1>
        <p class="page-header-subtitle">
          Professional, Secure, and Immediate Response to Any Form of Violence.
        </p>
        <div class="mt-8 flex justify-center">
          <div class="pill bg-sauti-blue/10 text-sauti-blue">Support Available in: EN • LG • SW • LS</div>
        </div>
      </div>
    </header>

    <!-- 2. Main Content Grid -->
    <div class="container-custom section-padding">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">

        <!-- Left Column: Form & Instructions -->
        <div class="lg:col-span-8 section-rhythm">

          <!-- Stepper / Process -->
          <section aria-labelledby="process-heading">
            <div class="bg-sauti-neutral rounded-[3rem] p-10 md:p-12 shadow-sm">
              <h2 id="process-heading" class="campaign-header text-sm text-sauti-darkGreen mb-10 opacity-50">How the
                reporting process works</h2>
              <ol class="grid grid-cols-1 md:grid-cols-3 gap-10">
                <li v-for="(step, idx) in [
                  { title: 'Fill in details', text: 'Provide as much as you can. Anonymous reports are welcome.', color: 'sauti-blue' },
                  { title: 'Submit securely', text: 'Information is encrypted and strictly confidential.', color: 'sauti-orange' },
                  { title: 'We follow up', text: 'Our team of experts reviews and initiates action immediately.', color: 'sauti-lightGreen' }
                ]" :key="idx" class="flex flex-col gap-6">
                  <span
                    :class="['inline-flex h-12 w-12 items-center justify-center rounded-2xl text-sauti-white font-bold text-xl shadow-lg', `bg-sauti-${step.color.split('-')[1]}`]">
                    {{ idx + 1 }}
                  </span>
                  <div>
                    <p class="campaign-header text-lg text-sauti-darkGreen mb-2">{{ step.title }}</p>
                    <p class="text-sauti-darkGreen/60 text-sm font-bold leading-relaxed">{{ step.text }}</p>
                  </div>
                </li>
              </ol>
            </div>
          </section>

          <!-- Confidentiality Notice -->
          <div class="bg-sauti-lightGreen/10 p-8 rounded-[2.5rem] flex items-start gap-6">
            <div
              class="w-12 h-12 bg-sauti-white rounded-2xl flex items-center justify-center text-sauti-lightGreen shrink-0 shadow-sm border border-sauti-lightGreen/20">
              <ShieldCheckIcon class="w-7 h-7" />
            </div>
            <p class="text-sauti-darkGreen font-bold text-lg leading-relaxed pt-1">
              All information is kept <span class="font-bold">strictly confidential</span> and handled with care by
              government experts. You may choose to remain <span class="font-bold">anonymous</span> throughout the
              process.
            </p>
          </div>

          <!-- Report Form Component -->
          <section aria-labelledby="form-heading">
            <div class="bg-sauti-blue/5 rounded-[3rem] overflow-hidden shadow-sm">
              <div class="bg-sauti-blue/5 p-8 border-b-2 border-sauti-blue/10">
                <h2 id="form-heading" class="campaign-header text-xl text-sauti-darkGreen">Formal Incident Report</h2>
              </div>
              <div class="p-8 md:p-12">
                <ReportForm />
              </div>
            </div>
          </section>
        </div>

        <!-- Right Column: Sidebar -->
        <aside class="lg:col-span-4 space-y-8">

          <!-- Immediate Help Card -->
          <div class="bg-sauti-red/5 rounded-[3rem] p-10 shadow-sm">
            <h3 class="campaign-header text-xl text-sauti-darkGreen mb-4">Urgent Help?</h3>
            <p class="text-sauti-darkGreen font-bold leading-relaxed opacity-70 mb-8">
              If someone is in immediate danger, do not wait. Use our priority channels for instant response.
            </p>
            <div class="space-y-4">
              <BaseCTA href="tel:116" variant="emergency" class="w-full justify-center gap-3">
                <PhoneIcon class="w-5 h-5" />
                Call 116 Now
              </BaseCTA>
              <BaseCTA href="https://wa.me/256743889999" variant="outline"
                class="w-full justify-center gap-3 !border-sauti-orange !text-sauti-orange hover:!bg-sauti-orange hover:!text-white">
                <ChatBubbleLeftRightIcon class="w-5 h-5" />
                WhatsApp Chat
              </BaseCTA>
            </div>
          </div>

          <!-- Other Channels -->
          <div class="bg-sauti-neutral rounded-[3rem] p-10 shadow-sm">
            <h3 class="campaign-header text-xl text-sauti-darkGreen mb-6">Secondary Channels</h3>
            <div class="space-y-6">
              <div v-for="channel in [
                { label: 'U-Report SMS', val: '8500', icon: ChatBubbleBottomCenterTextIcon, color: 'text-sauti-blue' },
                { label: 'Official Email', val: 'info@sauti.mglsd.go.ug', icon: EnvelopeIcon, color: 'text-sauti-blue' }
              ]" :key="channel.label"
                class="flex items-start gap-4 p-4 hover:bg-sauti-neutral/30 rounded-2xl transition-colors">
                <div
                  :class="['w-10 h-10 rounded-xl bg-sauti-white border border-sauti-neutral flex items-center justify-center shrink-0 shadow-sm', channel.color]">
                  <component :is="channel.icon" class="w-5 h-5" />
                </div>
                <div>
                  <p class="campaign-header text-[10px] text-sauti-darkGreen/40 mb-1">{{ channel.label }}</p>
                  <p class="text-sauti-darkGreen font-bold break-all">{{ channel.val }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Privacy & Safety Footer -->
          <div class="bg-sauti-darkGreen rounded-[3rem] p-10 shadow-xl text-sauti-white relative overflow-hidden">
            <div class="absolute -right-10 -bottom-10 w-40 h-40 bg-white/5 rounded-full blur-2xl"></div>
            <h3 class="campaign-header text-lg text-white mb-4">Safety First</h3>
            <p class="text-sm opacity-70 leading-relaxed font-bold mb-6">
              Your safety is our priority. We never share your data without legal necessity or absolute prevention of
              harm.
            </p>
            <router-link to="/privacy"
              class="text-sauti-blue font-bold uppercase text-[10px] tracking-widest hover:text-white transition-colors">
              Read Safety Protocol →
            </router-link>
          </div>
        </aside>
      </div>
    </div>
  </div>
</template>

<script setup>
  import ReportForm from '@/components/reports/ReportForm.vue'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import {
    ShieldCheckIcon,
    PhoneIcon,
    ChatBubbleLeftRightIcon,
    ChatBubbleBottomCenterTextIcon,
    EnvelopeIcon
  } from '@heroicons/vue/24/outline'

  defineOptions({
    name: 'ReportPage'
  })
</script>
