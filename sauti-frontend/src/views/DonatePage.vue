<template>
  <div class="bg-neutral-white min-h-screen">
    <!-- 1. Hero / Header Section -->
    <header class="relative overflow-hidden pt-24 pb-32 bg-secondary">
      <img src="@/assets/community-protection.png" alt="Sauti 116 Child Protection in Community"
        class="absolute inset-0 w-full h-full object-cover opacity-40" />
      <div class="absolute inset-0 bg-gradient-to-br from-primary/40 to-secondary/80"></div>
      <div class="container-custom relative z-10 text-center">
        <div class="max-w-4xl mx-auto">
          <div
            class="inline-flex items-center justify-center w-24 h-24 bg-primary rounded-[2.5rem] mb-12 shadow-2xl shadow-primary/30">
            <HeartIcon class="w-12 h-12 text-neutral-white" />
          </div>
          <h1 class="text-5xl md:text-7xl lg:text-8xl font-bold mb-8 leading-tight text-neutral-white tracking-tight">
            Protecting Our <span class="text-primary">Children</span>
          </h1>
          <p class="text-xl md:text-2xl text-neutral-white/90 max-w-2xl mx-auto leading-relaxed mb-12 font-bold">
            Your contribution powers the 116 Helpline, ensuring every child in Uganda has a safe voice and a protective
            hand.
          </p>
          <div class="cta-group justify-center">
            <BaseCTA href="#donate-options" variant="primary" class="!px-12 !py-5"
              @click="scrollToSection('donate-options')">
              Donate Now
            </BaseCTA>
            <BaseCTA href="/contact" variant="outline"
              class="!px-12 !py-5 text-neutral-white border-neutral-white/20 hover:bg-neutral-white/10">
              Learn More
            </BaseCTA>
          </div>
        </div>
      </div>
    </header>

    <!-- 2. Impact Statistics Overlay -->
    <section class="relative -mt-16 lg:-mt-24 z-20">
      <div class="container-custom">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 md:gap-8">
          <div v-for="(stat, idx) in [
            { val: '1M+', label: 'Children Helped', color: 'text-primary' },
            { val: '24/7', label: 'Support Always', color: 'text-accent-orange' },
            { val: '116', label: 'Toll-Free Help', color: 'text-secondary-light' },
            { val: '15+', label: 'Years Of Impact', color: 'text-secondary-light' }
          ]" :key="idx"
            class="bg-neutral-white p-8 rounded-[3rem] border-2 border-neutral-offwhite text-center shadow-2xl transition-all duration-500 hover:border-primary">
            <div :class="['text-4xl md:text-5xl font-bold mb-2', stat.color]">{{ stat.val }}</div>
            <div class="campaign-header text-[10px] text-secondary/40">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <div class="section-padding !pt-0">
      <div class="container-custom">
        <!-- Giving in a Flash (Flash Pattern) -->
        <section class="bg-primary/5 p-8 md:p-12 rounded-[3.5rem] border-2 border-primary/10 mb-16 shadow-sm">
          <h2 class="campaign-header text-xl text-primary mb-6 flex items-center gap-3">
            <ShieldCheckIcon class="w-6 h-6 text-primary" />
            Giving in a Flash
          </h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
            <div class="space-y-4">
              <p class="text-secondary font-bold text-lg">100% Direct Impact</p>
              <p class="text-secondary/60 text-sm leading-relaxed">Every shilling powers **24/7 rescue operations** for
                children.</p>
            </div>
            <div class="space-y-4">
              <p class="text-secondary font-bold text-lg">Fully Transparent</p>
              <p class="text-secondary/60 text-sm leading-relaxed">Official government receipts provided for **every
                contribution**.</p>
            </div>
            <div class="space-y-4">
              <p class="text-secondary font-bold text-lg">Secure Channels</p>
              <p class="text-secondary/60 text-sm leading-relaxed">Donations are handled through **authorized MGLSD
                accounts**.</p>
            </div>
          </div>
        </section>
      </div>

      <div>
        <!-- 3. Why Your Support Matters -->
        <section aria-labelledby="why-heading" class="section-padding bg-neutral-white">
          <div class="container-custom">
            <div class="text-center mb-20">
              <h2 id="why-heading" class="campaign-header text-4xl text-secondary mb-6">How Your Gift Saves Lives</h2>
              <p class="text-xl text-secondary max-w-2xl mx-auto font-bold opacity-70">
                Every contribution directly funds the infrastructure that keeps children safe 24 hours a day.
              </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
              <div v-for="(reason, idx) in [
                { title: 'Support Children', text: 'Help us provide 24/7 helpline services to vulnerable children across Uganda, offering them a safe voice when they need it most.', colorToken: 'primary', icon: UserGroupIcon },
                { title: 'Enable Services', text: 'Your donation helps us maintain counseling, legal support, and referral services that save lives and protect vulnerable individuals.', colorToken: 'secondary-light', icon: ShieldCheckIcon },
                { title: 'Expand Reach', text: 'Help us reach more communities and provide training and awareness programs that prevent abuse and protect children.', colorToken: 'accent-orange', icon: ShareIcon }
              ]" :key="idx" class="card-base group text-center">
                <div
                  :class="['inline-flex items-center justify-center w-20 h-20 rounded-2xl mb-8 transition-transform group-hover:scale-110 shadow-lg', `bg-${reason.colorToken}/10 text-${reason.colorToken}`]">
                  <component :is="reason.icon" class="w-10 h-10" />
                </div>
                <h3 class="campaign-header text-2xl text-secondary mb-4">{{ reason.title }}</h3>
                <p class="text-secondary/60 font-bold leading-relaxed">{{ reason.text }}</p>
              </div>
            </div>
          </div>
        </section>

        <!-- 4. Donation Options -->
        <section id="donate-options" aria-labelledby="options-heading" class="section-padding bg-primary/5">
          <div class="container-custom">
            <div class="text-center mb-20">
              <h2 id="options-heading" class="campaign-header text-4xl text-secondary mb-6">Secure Ways to Help</h2>
              <p class="text-xl text-secondary max-w-2xl mx-auto font-bold opacity-70">
                Choose the method most convenient for you. All contributions directly support our programs.
              </p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-10">
              <!-- Bank Card -->
              <div class="bg-neutral-white p-10 md:p-16 rounded-[4rem] border-2 border-primary shadow-sm">
                <div class="flex items-center mb-12">
                  <div
                    class="w-16 h-16 bg-primary rounded-2xl flex items-center justify-center text-neutral-white shadow-xl mr-6">
                    <CreditCardIcon class="w-8 h-8" />
                  </div>
                  <h3 class="campaign-header text-3xl text-secondary">Bank Transfer</h3>
                </div>

                <div class="space-y-6 mb-12">
                  <div v-for="info in [
                    { label: 'Bank Name', val: 'Ministry of Gender, Labour & Social Development', colorToken: 'primary' },
                    { label: 'Account Name', val: 'Sauti 116 Helpline', colorToken: 'accent-orange' },
                    { label: 'Account Number', val: 'Confidential - Call 116 to verify', colorToken: 'primary' }
                  ]" :key="info.label" class="p-6 bg-neutral-offwhite/30 rounded-2xl border-l-[12px] shadow-sm"
                    :class="`border-${info.colorToken}`">
                    <div class="campaign-header text-[10px] text-secondary/40 mb-2">{{ info.label }}</div>
                    <div class="text-lg font-bold text-secondary">{{ info.val }}</div>
                  </div>
                </div>

                <BaseCTA href="tel:116" variant="info" class="w-full justify-center gap-3">
                  <PhoneIcon class="w-5 h-5" />
                  Call 116 for Details
                </BaseCTA>
              </div>

              <!-- Mobile Card -->
              <div class="bg-neutral-white p-10 md:p-16 rounded-[4rem] border-2 border-accent-orange shadow-sm">
                <div class="flex items-center mb-12">
                  <div
                    class="w-16 h-16 bg-accent-orange rounded-2xl flex items-center justify-center text-neutral-white shadow-xl mr-6">
                    <DevicePhoneMobileIcon class="w-8 h-8" />
                  </div>
                  <h3 class="campaign-header text-3xl text-secondary">Mobile Money</h3>
                </div>

                <div class="space-y-6 mb-12">
                  <div v-for="net in [
                    { name: 'MTN Mobile Money', colorToken: 'accent-yellow', textToken: 'text-secondary' },
                    { name: 'Airtel Money', colorToken: 'primary-red', textToken: 'text-neutral-white' }
                  ]" :key="net.name"
                    class="p-8 bg-neutral-offwhite/30 rounded-3xl border-2 border-transparent hover:border-primary transition-all">
                    <div class="flex items-center gap-6 mb-4">
                      <div
                        :class="['w-12 h-12 rounded-xl flex items-center justify-center font-bold text-xs shadow-sm', `bg-${net.colorToken} ${net.textToken}`]">
                        {{ net.name.includes('MTN') ? 'MTN' : 'A' }}
                      </div>
                      <span class="text-xl font-bold text-secondary">{{ net.name }}</span>
                    </div>
                    <p class="campaign-header text-lg text-primary">Call 116 for Secure Merchant Code</p>
                  </div>
                </div>

                <BaseCTA href="tel:116" variant="emergency" class="w-full justify-center gap-3">
                  <PhoneIcon class="w-5 h-5" />
                  Contact Mobile Donation
                </BaseCTA>
              </div>
            </div>
          </div>
        </section>

        <!-- 5. Transparency / Footer -->
        <section aria-labelledby="transparency-heading" class="section-padding bg-neutral-white">
          <div class="container-custom">
            <div
              class="bg-secondary p-12 md:p-20 rounded-[4rem] text-neutral-white shadow-2xl relative overflow-hidden">
              <div class="absolute -right-20 -bottom-20 w-80 h-80 bg-neutral-white/5 rounded-full blur-3xl"></div>

              <div class="relative z-10 flex flex-col md:flex-row items-start gap-12">
                <div
                  class="w-20 h-20 bg-neutral-white/10 rounded-[2rem] flex items-center justify-center shrink-0 border border-neutral-white/20">
                  <ShieldCheckIcon class="w-10 h-10 text-primary" />
                </div>
                <div>
                  <h3 id="transparency-heading" class="campaign-header text-3xl text-neutral-white mb-6">Our Commitment
                    to
                    Accountability</h3>
                  <p class="text-xl text-neutral-white/70 font-bold leading-relaxed mb-10 italic">
                    All donations directly support the operations of Sauti 116 helpline. We are committed to
                    transparency
                    and accountability. Receipts will be provided for all contributions via official government
                    channels.
                  </p>
                  <div class="cta-group">
                    <BaseCTA href="/contact" variant="primary"
                      class="!bg-neutral-white !text-secondary hover:!bg-primary hover:!text-neutral-white">Message
                      Support</BaseCTA>
                    <BaseCTA href="tel:116" variant="outline" class="text-neutral-white border-neutral-white/20">Call
                      Helpline
                    </BaseCTA>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>


<script setup>
  import { onMounted } from 'vue'
  import { useSettingsStore } from '@/store/settings'
  import BaseCTA from '@/components/common/BaseCTA.vue'
  import {
    HeartIcon,
    UserGroupIcon,
    ShieldCheckIcon,
    ShareIcon,
    CreditCardIcon,
    DevicePhoneMobileIcon,
    PhoneIcon
  } from '@heroicons/vue/24/outline'

  defineOptions({
    name: 'DonatePage'
  })

  const settingsStore = useSettingsStore()

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId)
    if (element) {
      const offset = 100
      const elementPosition = element.getBoundingClientRect().top
      const offsetPosition = elementPosition + window.pageYOffset - offset
      window.scrollTo({ top: offsetPosition, behavior: 'smooth' })
    }
  }

  onMounted(() => {
    settingsStore.fetchGlobalSettings()
    if (window.location.hash) {
      const hash = window.location.hash.substring(1)
      setTimeout(() => scrollToSection(hash), 500)
    }
  })
</script>
