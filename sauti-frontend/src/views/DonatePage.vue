<template>
  <div class="bg-sauti-neutral min-h-screen">
    <!-- Hero Section -->
    <section class="relative overflow-hidden pt-16 md:pt-24 lg:pt-32 pb-24 lg:pb-40 bg-sauti-darkGreen">
      <div class="absolute inset-0 bg-gradient-to-br from-sauti-blue/10 to-transparent"></div>
      <div class="container-custom relative z-10">
        <div class="max-w-4xl mx-auto text-center">
          <div
            class="inline-flex items-center justify-center w-24 h-24 bg-sauti-blue rounded-[2.5rem] mb-10 shadow-2xl shadow-sauti-blue/20">
            <svg class="w-12 h-12 text-sauti-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3"
                d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
            </svg>
          </div>
          <h1 class="text-4xl md:text-5xl lg:text-8xl font-black mb-8 leading-tight text-sauti-white tracking-tight">
            Protecting Our <span class="text-sauti-blue">Children</span>
          </h1>
          <p class="text-xl md:text-2xl text-sauti-white/70 max-w-2xl mx-auto leading-relaxed mb-12 font-bold">
            Your contribution powers the 116 Helpline, ensuring every child in Uganda has a safe voice and a protective
            hand.
          </p>
          <div class="flex flex-col sm:flex-row gap-6 justify-center items-center">
            <a href="#donate-options" @click.prevent="scrollToSection('donate-options')"
              class="group relative px-12 py-5 bg-sauti-blue text-sauti-white rounded-2xl font-black text-xl shadow-xl shadow-sauti-blue/30 hover:scale-105 transition-all">
              Donate Now
            </a>
            <router-link to="/contact"
              class="px-12 py-5 bg-sauti-white/5 backdrop-blur-md text-sauti-white border-2 border-sauti-white/20 rounded-2xl font-black text-xl hover:bg-sauti-white/10 transition-all">
              Learn More
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Impact Statistics -->
    <section class="relative -mt-16 lg:-mt-24">
      <div class="container-custom">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-8">
          <div v-for="(stat, idx) in [
            { val: '1M+', label: 'Children Helped', icon: 'sauti-blue' },
            { val: '24/7', label: 'Support Always', icon: 'sauti-orange' },
            { val: '116', label: 'Toll-Free Helpline', icon: 'sauti-lightGreen' },
            { val: '15+', label: 'Years Of Impact', icon: 'sauti-red' }
          ]" :key="idx"
            class="bg-sauti-white p-8 rounded-[2.5rem] border-2 border-sauti-neutral text-center shadow-2xl shadow-sauti-darkGreen/5 transform hover:-translate-y-2 transition-all duration-500">
            <div :class="['text-3xl md:text-5xl font-black mb-2', `text-${stat.icon}`]">{{ stat.val }}</div>
            <div class="text-xs md:text-sm text-sauti-darkGreen/60 font-black uppercase tracking-widest">{{ stat.label
              }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Why Donate Section -->
    <section class="py-24 lg:py-32 bg-sauti-white rounded-t-[5rem]">
      <div class="container-custom">
        <div class="max-w-4xl mx-auto text-center mb-20">
          <h2 class="text-4xl md:text-5xl font-black text-sauti-darkGreen mb-6">{{
            settingsStore.settings.donate_why_title || 'Why Your Support Matters' }}</h2>
          <p class="text-xl text-sauti-darkGreen/70 max-w-2xl mx-auto font-bold leading-relaxed">
            Every contribution directly funds the infrastructure that keeps children safe 24 hours a day.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-10 max-w-6xl mx-auto">
          <div v-for="(reason, idx) in [
            { title: 'Support Children', text: 'Help us provide 24/7 helpline services to vulnerable children across Uganda, offering them a safe voice when they need it most.', color: 'sauti-blue', icon: 'M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z' },
            { title: 'Enable Services', text: 'Your donation helps us maintain counseling, legal support, and referral services that save lives and protect vulnerable individuals.', color: 'sauti-lightGreen', icon: 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z' },
            { title: 'Expand Reach', text: 'Help us reach more communities and provide training and awareness programs that prevent abuse and protect children.', color: 'sauti-orange', icon: 'M12 8v13m0-13V6a2 2 0 112 2h-2zm0 0V5.5A2.5 2.5 0 109.5 8H12zm-7 4h14M5 12a2 2 0 110-4h14a2 2 0 110 4M5 12v7a2 2 0 002 2h10a2 2 0 002-2v-7' }
          ]" :key="idx"
            class="bg-sauti-neutral/30 p-10 rounded-[3rem] text-center border-2 border-transparent hover:border-sauti-neutral hover:bg-sauti-white transition-all duration-500 group shadow-sm hover:shadow-2xl hover:shadow-sauti-darkGreen/5">
            <div
              :class="['inline-flex items-center justify-center w-20 h-20 rounded-2xl mb-8 shadow-lg group-hover:scale-110 transition-transform', `bg-${reason.color}`]">
              <svg class="w-10 h-10 text-sauti-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" :d="reason.icon" />
              </svg>
            </div>
            <h3 class="text-2xl font-black text-sauti-darkGreen mb-4">{{ reason.title }}</h3>
            <p class="text-sauti-darkGreen/60 font-bold leading-relaxed">{{ reason.text }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Donation Options Section -->
    <section id="donate-options" class="section-padding bg-sauti-neutral/10">
      <div class="container-custom max-w-6xl">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl lg:text-5xl font-black text-sauti-darkGreen mb-4">How to Donate</h2>
          <p class="text-lg md:text-xl text-sauti-darkGreen/70 max-w-2xl mx-auto font-medium">
            Choose the donation method that's most convenient for you. All contributions directly support our programs.
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12">
          <!-- Bank Transfer Card -->
          <div class="bg-sauti-white p-8 lg:p-12 rounded-[3.5rem] border border-sauti-neutral shadow-sm">
            <div class="flex items-center mb-10">
              <div class="inline-flex items-center justify-center w-16 h-16 bg-sauti-blue rounded-2xl mr-6 shadow-lg">
                <svg class="w-8 h-8 text-sauti-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" />
                </svg>
              </div>
              <h3 class="text-3xl font-black text-sauti-darkGreen">Bank Transfer</h3>
            </div>

            <div class="space-y-6 mb-10">
              <div class="bg-sauti-neutral p-6 rounded-2xl border-l-4 border-sauti-blue">
                <div class="text-xs font-black text-sauti-blue uppercase tracking-widest mb-2">Bank Name</div>
                <div class="text-lg font-bold text-sauti-darkGreen">Ministry of Gender, Labour & Social Development
                </div>
              </div>
              <div class="bg-sauti-neutral p-6 rounded-2xl border-l-4 border-sauti-orange">
                <div class="text-xs font-black text-sauti-orange uppercase tracking-widest mb-2">Account Name</div>
                <div class="text-lg font-bold text-sauti-darkGreen">Sauti 116 helpline</div>
              </div>
              <div class="bg-sauti-neutral p-6 rounded-2xl border-l-4 border-sauti-blue">
                <div class="text-xs font-black text-sauti-blue uppercase tracking-widest mb-2">Account Number</div>
                <div class="text-lg font-bold text-sauti-darkGreen">Please call for secure details</div>
              </div>
            </div>

            <a href="tel:116" class="btn btn-info w-full text-center" aria-label="Call 116 for bank account details">
              <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
              </svg>
              Call 116 for Details
            </a>
          </div>

          <!-- Mobile Money Card -->
          <div class="bg-sauti-white p-8 lg:p-12 rounded-[3.5rem] border border-sauti-neutral shadow-sm">
            <div class="flex items-center mb-10">
              <div class="inline-flex items-center justify-center w-16 h-16 bg-sauti-orange rounded-2xl mr-6 shadow-lg">
                <svg class="w-8 h-8 text-sauti-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
                </svg>
              </div>
              <h3 class="text-3xl font-black text-sauti-darkGreen">Mobile Money</h3>
            </div>

            <div class="space-y-6 mb-10">
              <div
                class="bg-sauti-neutral p-6 rounded-2xl border border-sauti-neutral hover:shadow-xl transition-all duration-500">
                <div class="flex items-center justify-between mb-4">
                  <div class="flex items-center">
                    <div class="w-12 h-12 bg-[#FFD700] rounded-xl flex items-center justify-center mr-4 shadow-sm">
                      <span class="text-sauti-darkGreen font-black text-xs">MTN</span>
                    </div>
                    <span class="font-bold text-sauti-darkGreen text-lg">MTN Mobile Money</span>
                  </div>
                </div>
                <div class="text-2xl font-black text-sauti-blue uppercase tracking-tight">Call 116 for details</div>
                <div class="text-xs text-sauti-darkGreen/50 font-bold mt-2 uppercase">Secure Direct Line</div>
              </div>

              <div
                class="bg-sauti-neutral p-6 rounded-2xl border border-sauti-neutral hover:shadow-xl transition-all duration-500">
                <div class="flex items-center justify-between mb-4">
                  <div class="flex items-center">
                    <div class="w-12 h-12 bg-sauti-red rounded-xl flex items-center justify-center mr-4 shadow-sm">
                      <span class="text-sauti-white font-black text-xs">A</span>
                    </div>
                    <span class="font-bold text-sauti-darkGreen text-lg">Airtel Money</span>
                  </div>
                </div>
                <div class="text-2xl font-black text-sauti-blue uppercase tracking-tight">Call 116 for details</div>
                <div class="text-xs text-sauti-darkGreen/50 font-bold mt-2 uppercase">Secure Direct Line</div>
              </div>
            </div>

            <a href="tel:116" class="btn btn-emergency w-full text-center"
              aria-label="Call 116 for mobile money details">
              <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
              </svg>
              Contact Mobile Donation
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Other Ways to Support -->
    <section class="section-padding bg-sauti-white">
      <div class="container-custom max-w-4xl">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl lg:text-5xl font-black text-sauti-darkGreen mb-4">Other Ways to Support</h2>
          <p class="text-lg text-sauti-darkGreen/70 font-medium">There are many ways you can make a difference</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
          <div
            class="bg-sauti-neutral/30 p-8 rounded-3xl text-center border border-sauti-neutral hover:scale-105 transition-all duration-300">
            <div class="inline-flex items-center justify-center w-14 h-14 bg-sauti-blue rounded-2xl mb-6 shadow-lg">
              <svg class="w-7 h-7 text-sauti-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
              </svg>
            </div>
            <h3 class="font-bold text-sauti-darkGreen text-xl mb-3">Volunteer</h3>
            <p class="text-sm text-sauti-darkGreen/70 font-medium">Share your time and expertise with us</p>
          </div>

          <div
            class="bg-sauti-neutral/30 p-8 rounded-3xl text-center border border-sauti-neutral hover:scale-105 transition-all duration-300">
            <div class="inline-flex items-center justify-center w-14 h-14 bg-sauti-orange rounded-2xl mb-6 shadow-lg">
              <svg class="w-7 h-7 text-sauti-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M17 20h5v-2a3 3 0 00-5.196-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.196-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
              </svg>
            </div>
            <h3 class="font-bold text-sauti-darkGreen text-xl mb-3">Partner</h3>
            <p class="text-sm text-sauti-darkGreen/70 font-medium">Partner with us for programs and initiatives</p>
          </div>

          <div
            class="bg-sauti-neutral/30 p-8 rounded-3xl text-center border border-sauti-neutral hover:scale-105 transition-all duration-300">
            <div
              class="inline-flex items-center justify-center w-14 h-14 bg-sauti-lightGreen rounded-2xl mb-6 shadow-lg">
              <svg class="w-7 h-7 text-sauti-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
              </svg>
            </div>
            <h3 class="font-bold text-sauti-darkGreen text-xl mb-3">Spread Awareness</h3>
            <p class="text-sm text-sauti-darkGreen/70 font-medium">Help us reach more people in your community</p>
          </div>
        </div>

        <div class="bg-sauti-neutral p-10 rounded-[3rem] border-2 border-sauti-blue shadow-xl">
          <div class="flex items-start">
            <div class="flex-shrink-0">
              <svg class="w-10 h-10 text-sauti-blue" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <div class="ml-6">
              <h3 class="text-2xl font-black text-sauti-darkGreen mb-4">Transparency & Accountability</h3>
              <p class="text-sauti-darkGreen leading-relaxed mb-8 font-medium italic">
                All donations directly support the operations of Sauti 116 helpline. We are committed to transparency
                and accountability. Receipts will be provided for all contributions, and we regularly report on how
                funds are used to maximize impact.
              </p>
              <div class="flex flex-col sm:flex-row gap-4">
                <router-link to="/contact" class="btn btn-outline text-center" aria-label="Contact us page">
                  Message Support
                </router-link>
                <a href="tel:116" class="btn btn-info text-center" aria-label="Call 116 helpline">
                  Call 116
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
  import { onMounted } from 'vue'

  defineOptions({
    name: 'DonatePage'
  })

  // Smooth scroll to section
  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId)
    if (element) {
      const offset = 80 // Account for any fixed headers
      const elementPosition = element.getBoundingClientRect().top
      const offsetPosition = elementPosition + window.pageYOffset - offset

      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      })
    }
  }

  // Handle anchor links on page load
  onMounted(() => {
    // Check if there's a hash in the URL
    if (window.location.hash) {
      const hash = window.location.hash.substring(1) // Remove the #
      setTimeout(() => {
        scrollToSection(hash)
      }, 100)
    }
  })
</script>

<style scoped>

  /* Smooth scroll behavior */
  html {
    scroll-behavior: smooth;
  }
</style>
