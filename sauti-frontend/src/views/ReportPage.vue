<template>
  <div class="bg-neutral-white min-h-screen">
    <!-- 1. Page Header -->
    <header class="page-header">
      <div class="container-custom">
        <h1 class="page-header-title">
          Report <span class="text-primary">a Case</span>
        </h1>
        <p class="page-header-subtitle">
          Professional, Secure, and Immediate Response to Any Form of Violence.
        </p>
        <div class="mt-8 flex justify-center">
          <div class="pill bg-primary/10 text-primary">Support Available in: EN • LG • SW • LS</div>
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
            <div class="bg-neutral-offwhite rounded-[3rem] p-10 md:p-12 shadow-sm">
              <h2 id="process-heading" class="campaign-header text-sm text-secondary mb-10 opacity-50">How the
                reporting process works</h2>
              <ol class="grid grid-cols-1 md:grid-cols-3 gap-10">
                <li v-for="(step, idx) in [
                  { title: 'Share Your Story', text: 'Tell us as much as you can. You can remain completely anonymous.', color: 'primary' },
                  { title: 'Encrypted Protection', text: 'Your data is locked and handled with extreme care by the MGLSD.', color: 'hotline' },
                  { title: 'Path to Safety', text: 'Our experts review and coordinate support for you immediately.', color: 'secondary-light' }
                ]" :key="idx" class="flex flex-col gap-6">
                  <span
                    :class="['inline-flex h-12 w-12 items-center justify-center rounded-2xl text-neutral-white font-bold text-xl shadow-lg', `bg-${step.color}`]">
                    {{ idx + 1 }}
                  </span>
                  <div>
                    <h3 class="campaign-header text-lg text-secondary mb-2">{{ step.title }}</h3>
                    <p class="text-muted text-sm font-bold leading-relaxed">{{ step.text }}</p>
                  </div>
                </li>
              </ol>
            </div>
          </section>

          <!-- Confidentiality Notice -->
          <div class="bg-secondary-light/10 p-8 rounded-[2.5rem] flex items-start gap-6">
            <div
              class="w-12 h-12 bg-neutral-white rounded-2xl flex items-center justify-center text-secondary-light shrink-0 shadow-sm border border-secondary-light/20">
              <ShieldCheckIcon class="w-7 h-7" />
            </div>
            <p class="text-black font-bold text-lg leading-relaxed pt-1">
              Your voice is safe with us. All information is kept <span
                class="text-primary underline decoration-2 decoration-primary/20">strictly private</span>.
              We are government experts dedicated to your protection, and you have the right to remain <span
                class="font-bold">anonymous</span> at every step.
            </p>
          </div>

          <!-- Report Form Component -->
          <section aria-labelledby="form-heading">
            <div class="bg-primary/5 rounded-[3rem] overflow-hidden shadow-sm">
              <div class="bg-primary/5 p-8 border-b-2 border-primary/10">
                <h2 id="form-heading" class="campaign-header text-xl text-secondary">Formal Incident Report</h2>
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
          <div class="bg-emergency/5 rounded-[3rem] p-10 shadow-sm">
            <h3 class="campaign-header text-xl text-secondary mb-4">Urgent Help?</h3>
            <p class="text-black font-bold leading-relaxed opacity-70 mb-8">
              If someone is in immediate danger, do not wait. Use our priority channels for instant response.
            </p>
            <div class="space-y-4">
              <BaseCTA href="tel:116" variant="emergency" class="w-full justify-center gap-3">
                <PhoneIcon class="w-5 h-5" />
                Call 116 Now
              </BaseCTA>
              <BaseCTA href="https://wa.me/256743889999" variant="outline"
                class="w-full justify-center gap-3 !border-hotline !text-hotline hover:!bg-hotline hover:!text-neutral-white">
                <ChatBubbleLeftRightIcon class="w-5 h-5" />
                WhatsApp Chat
              </BaseCTA>
            </div>
          </div>

          <!-- Other Channels -->
          <div class="bg-neutral-offwhite rounded-[3rem] p-10 shadow-sm">
            <h3 class="campaign-header text-xl text-secondary mb-6">Secondary Channels</h3>
            <div class="space-y-6">
              <div v-for="channel in [
                { label: 'U-Report SMS', val: '8500', icon: ChatBubbleBottomCenterTextIcon, color: 'text-primary' },
                { label: 'Official Email', val: 'info@sauti.mglsd.go.ug', icon: EnvelopeIcon, color: 'text-primary' }
              ]" :key="channel.label"
                class="flex items-start gap-4 p-4 hover:bg-neutral-offwhite/30 rounded-2xl transition-colors">
                <div
                  :class="['w-10 h-10 rounded-xl bg-neutral-white border border-neutral-offwhite flex items-center justify-center shrink-0 shadow-sm', channel.color]">
                  <component :is="channel.icon" class="w-5 h-5" />
                </div>
                <div>
                  <p class="campaign-header text-[10px] text-black/40 mb-1">{{ channel.label }}</p>
                  <p class="text-black font-bold break-all">{{ channel.val }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Privacy & Safety Footer -->
          <div class="bg-secondary rounded-[3rem] p-10 shadow-xl text-neutral-white relative overflow-hidden">
            <div class="absolute -right-10 -bottom-10 w-40 h-40 bg-neutral-white/5 rounded-full blur-2xl"></div>
            <h3 class="campaign-header text-lg text-neutral-white mb-4">Safety First</h3>
            <p class="text-sm opacity-70 leading-relaxed font-bold mb-6">
              Your safety is our priority. We never share your data without legal necessity or absolute prevention of
              harm.
            </p>
            <router-link to="/privacy"
              class="text-primary font-bold uppercase text-[10px] tracking-widest hover:text-neutral-white transition-colors">
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
