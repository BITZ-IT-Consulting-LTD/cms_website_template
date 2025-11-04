<template>
  <div>
    <!-- Hero Section -->
    <section class="relative overflow-hidden bg-gradient-to-br from-[#8B4000] via-[#A0522D] to-[#D2691E] py-16 md:py-24 lg:py-32">
      <div class="absolute inset-0 bg-black/10"></div>
      <div class="container-custom relative z-10">
        <div class="max-w-4xl mx-auto text-center text-white">
          <div class="inline-flex items-center justify-center mb-6">
            <svg class="w-16 h-16 md:w-20 md:h-20" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
          </div>
          <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold mb-6 leading-tight">
            Make a Difference Today
          </h1>
          <p class="text-xl md:text-2xl text-white/90 max-w-3xl mx-auto leading-relaxed mb-8">
            Your donation helps us provide critical support to children, GBV survivors, and migrant workers across Uganda. Every contribution creates lasting impact.
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <a 
              href="#donate-options" 
              @click.prevent="scrollToSection('donate-options')"
              class="pill bg-white text-[#8B4000] hover:bg-[#FFF8DC] hover:scale-105 cursor-pointer"
              aria-label="Scroll to donation options"
            >
              Donate Now
            </a>
            <router-link 
              to="/contact" 
              class="pill bg-white/10 backdrop-blur-sm text-white border-2 border-white/30 hover:bg-white/20"
            >
              Learn More
            </router-link>
          </div>
        </div>
      </div>
      <!-- Decorative Elements -->
      <div class="absolute bottom-0 left-0 right-0 h-24 bg-white"></div>
    </section>

    <!-- Impact Statistics -->
    <section class="relative -mt-12 md:-mt-16">
      <div class="container-custom">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
          <div class="card text-center p-6 transform hover:scale-105 transition-all duration-300">
            <div class="text-3xl md:text-4xl font-bold text-[#8B4000] mb-2">1M+</div>
            <div class="text-sm md:text-base text-gray-600">Children Helped</div>
          </div>
          <div class="card text-center p-6 transform hover:scale-105 transition-all duration-300">
            <div class="text-3xl md:text-4xl font-bold text-[#A0522D] mb-2">24/7</div>
            <div class="text-sm md:text-base text-gray-600">Available Support</div>
          </div>
          <div class="card text-center p-6 transform hover:scale-105 transition-all duration-300">
            <div class="text-3xl md:text-4xl font-bold text-[#8B4000] mb-2">116</div>
            <div class="text-sm md:text-base text-gray-600">Free Helpline</div>
          </div>
          <div class="card text-center p-6 transform hover:scale-105 transition-all duration-300">
            <div class="text-3xl md:text-4xl font-bold text-[#A0522D] mb-2">15+</div>
            <div class="text-sm md:text-base text-gray-600">Years Serving</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Why Donate Section -->
    <section class="section-padding bg-gradient-to-b from-white to-[#FFF8DC]/30">
      <div class="container-custom">
        <div class="max-w-4xl mx-auto text-center mb-12">
          <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold mb-4">Why Your Support Matters</h2>
          <p class="text-lg md:text-xl text-gray-600 max-w-2xl mx-auto">
            Every donation directly supports our mission to protect and empower vulnerable children across Uganda.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-8 max-w-6xl mx-auto">
          <div class="card p-8 text-center transform hover:scale-105 transition-all duration-300">
            <div class="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-blue-500 to-blue-600 rounded-2xl mb-6 shadow-lg">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/>
              </svg>
            </div>
            <h3 class="text-xl font-bold text-gray-900 mb-3">Support Children</h3>
            <p class="text-gray-600 leading-relaxed">
              Help us provide 24/7 helpline services to vulnerable children across Uganda, offering them a safe voice when they need it most.
            </p>
          </div>

          <div class="card p-8 text-center transform hover:scale-105 transition-all duration-300">
            <div class="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-teal-500 to-teal-600 rounded-2xl mb-6 shadow-lg">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <h3 class="text-xl font-bold text-gray-900 mb-3">Enable Services</h3>
            <p class="text-gray-600 leading-relaxed">
              Your donation helps us maintain counseling, legal support, and referral services that save lives and protect vulnerable individuals.
            </p>
          </div>

          <div class="card p-8 text-center transform hover:scale-105 transition-all duration-300">
            <div class="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-purple-500 to-purple-600 rounded-2xl mb-6 shadow-lg">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v13m0-13V6a2 2 0 112 2h-2zm0 0V5.5A2.5 2.5 0 109.5 8H12zm-7 4h14M5 12a2 2 0 110-4h14a2 2 0 110 4M5 12v7a2 2 0 002 2h10a2 2 0 002-2v-7"/>
              </svg>
            </div>
            <h3 class="text-xl font-bold text-gray-900 mb-3">Expand Reach</h3>
            <p class="text-gray-600 leading-relaxed">
              Help us reach more communities and provide training and awareness programs that prevent abuse and protect children.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Donation Options Section -->
    <section id="donate-options" class="section-padding bg-white">
      <div class="container-custom max-w-6xl">
        <div class="text-center mb-12">
          <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold mb-4">How to Donate</h2>
          <p class="text-lg md:text-xl text-gray-600 max-w-2xl mx-auto">
            Choose the donation method that's most convenient for you. All contributions directly support our programs.
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12">
          <!-- Bank Transfer Card -->
          <div class="card p-8 lg:p-10">
            <div class="flex items-center mb-6">
              <div class="inline-flex items-center justify-center w-14 h-14 bg-gradient-to-br from-green-500 to-green-600 rounded-xl mr-4 shadow-lg">
                <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"/>
                </svg>
              </div>
              <h3 class="text-2xl font-bold text-gray-900">Bank Transfer</h3>
            </div>
            
            <div class="space-y-4 mb-6">
              <div class="bg-gradient-to-r from-gray-50 to-gray-100 p-5 rounded-xl border-l-4 border-[#8B4000]">
                <div class="text-sm text-gray-600 mb-1">Bank Name</div>
                <div class="text-base font-semibold text-gray-900">Ministry of Gender, Labour & Social Development</div>
              </div>
              <div class="bg-gradient-to-r from-gray-50 to-gray-100 p-5 rounded-xl border-l-4 border-[#A0522D]">
                <div class="text-sm text-gray-600 mb-1">Account Name</div>
                <div class="text-base font-semibold text-gray-900">Sauti Child Helpline</div>
              </div>
              <div class="bg-gradient-to-r from-gray-50 to-gray-100 p-5 rounded-xl border-l-4 border-[#8B4000]">
                <div class="text-sm text-gray-600 mb-1">Account Number</div>
                <div class="text-base font-semibold text-gray-900">Contact for details</div>
              </div>
            </div>
            
            <a 
              href="tel:116" 
              class="pill pill-primary w-full text-center justify-center"
              aria-label="Call 116 for bank account details"
            >
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
              </svg>
              Call 116 for Account Details
            </a>
          </div>

          <!-- Mobile Money Card -->
          <div class="card p-8 lg:p-10">
            <div class="flex items-center mb-6">
              <div class="inline-flex items-center justify-center w-14 h-14 bg-gradient-to-br from-yellow-500 to-orange-500 rounded-xl mr-4 shadow-lg">
                <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"/>
                </svg>
              </div>
              <h3 class="text-2xl font-bold text-gray-900">Mobile Money</h3>
            </div>
            
            <div class="space-y-4 mb-6">
              <div class="bg-gradient-to-r from-yellow-50 to-orange-50 p-6 rounded-xl border border-yellow-200 hover:shadow-lg transition-all duration-300">
                <div class="flex items-center justify-between mb-3">
                  <div class="flex items-center">
                    <div class="w-10 h-10 bg-yellow-500 rounded-lg flex items-center justify-center mr-3">
                      <span class="text-white font-bold text-sm">MTN</span>
                    </div>
                    <span class="font-semibold text-gray-900">MTN Mobile Money</span>
                  </div>
                </div>
                <div class="text-2xl font-bold text-[#8B4000]">Contact for number</div>
                <div class="text-sm text-gray-600 mt-1">Available 24/7</div>
              </div>
              
              <div class="bg-gradient-to-r from-red-50 to-pink-50 p-6 rounded-xl border border-red-200 hover:shadow-lg transition-all duration-300">
                <div class="flex items-center justify-between mb-3">
                  <div class="flex items-center">
                    <div class="w-10 h-10 bg-red-600 rounded-lg flex items-center justify-center mr-3">
                      <span class="text-white font-bold text-sm">A</span>
                    </div>
                    <span class="font-semibold text-gray-900">Airtel Money</span>
                  </div>
                </div>
                <div class="text-2xl font-bold text-[#8B4000]">Contact for number</div>
                <div class="text-sm text-gray-600 mt-1">Available 24/7</div>
              </div>
            </div>
            
            <a 
              href="tel:116" 
              class="pill pill-primary w-full text-center justify-center"
              aria-label="Call 116 for mobile money details"
            >
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
              </svg>
              Call 116 for Mobile Money Details
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Other Ways to Support -->
    <section class="section-padding bg-gradient-to-b from-[#FFF8DC]/50 to-white">
      <div class="container-custom max-w-4xl">
        <div class="text-center mb-12">
          <h2 class="text-3xl md:text-4xl font-bold mb-4">Other Ways to Support</h2>
          <p class="text-lg text-gray-600">There are many ways you can make a difference</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div class="card p-6 text-center hover:scale-105 transition-all duration-300">
            <div class="inline-flex items-center justify-center w-12 h-12 bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl mb-4 shadow-lg">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/>
              </svg>
            </div>
            <h3 class="font-semibold text-gray-900 mb-2">Volunteer</h3>
            <p class="text-sm text-gray-600">Share your time and expertise with us</p>
          </div>

          <div class="card p-6 text-center hover:scale-105 transition-all duration-300">
            <div class="inline-flex items-center justify-center w-12 h-12 bg-gradient-to-br from-purple-500 to-purple-600 rounded-xl mb-4 shadow-lg">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.196-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.196-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
              </svg>
            </div>
            <h3 class="font-semibold text-gray-900 mb-2">Partner</h3>
            <p class="text-sm text-gray-600">Partner with us for programs and initiatives</p>
          </div>

          <div class="card p-6 text-center hover:scale-105 transition-all duration-300">
            <div class="inline-flex items-center justify-center w-12 h-12 bg-gradient-to-br from-green-500 to-green-600 rounded-xl mb-4 shadow-lg">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/>
              </svg>
            </div>
            <h3 class="font-semibold text-gray-900 mb-2">Spread Awareness</h3>
            <p class="text-sm text-gray-600">Help us reach more people in your community</p>
          </div>
        </div>

        <div class="card p-8 bg-gradient-to-br from-blue-50 to-indigo-50 border-2 border-blue-200">
          <div class="flex items-start">
            <div class="flex-shrink-0">
              <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <div class="ml-4">
              <h3 class="text-lg font-bold text-gray-900 mb-2">Transparency & Accountability</h3>
              <p class="text-gray-700 leading-relaxed mb-4">
                All donations directly support the operations of Sauti Child Helpline. We are committed to transparency and accountability. Receipts will be provided for all contributions, and we regularly report on how funds are used to maximize impact.
              </p>
              <div class="flex flex-col sm:flex-row gap-3">
                <router-link 
                  to="/contact" 
                  class="pill pill-outline text-center justify-center"
                  aria-label="Contact us page"
                >
                  Contact Us
                </router-link>
                <a 
                  href="tel:116" 
                  class="pill pill-primary text-center justify-center"
                  aria-label="Call 116 helpline"
                >
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
