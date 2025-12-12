<template>
  <div>
    <section class="section-padding bg-gray-50">
      <div class="container-custom text-center">
        <h2 class="mb-2">Our Operations and Case Flow</h2>
        <p class="text-gray-600 max-w-3xl mx-auto">A transparent look into how we handle every call to ensure every child's voice is heard and acted upon with care and urgency.</p>
      </div>
    </section>

    <section class="section-padding">
      <div class="container-custom">
        <div class="bg-white rounded-3xl shadow-sm border border-gray-100 overflow-hidden">
          <img :src="operationsImage" alt="Our operations and case flow - Sauti 116 helpline process diagram" class="w-full h-96 object-cover" />
        </div>
      </div>
    </section>

    <section class="section-padding bg-gradient-to-b from-gray-50 to-white">
      <div class="container-custom">
        <div class="text-center mb-16">
          <h3 class="mb-2">The Path to Resolution</h3>
          <p class="text-gray-600 max-w-2xl mx-auto">Our streamlined process from report to resolution, ensuring every case receives the attention and action it deserves.</p>
        </div>

        <!-- Desktop Flow - Horizontal with connecting lines -->
        <div class="hidden md:block relative">
          <!-- Animated Connecting Line -->
          <div class="absolute top-20 left-0 right-0 h-1 bg-gradient-to-r from-blue-200 via-teal-200 via-orange-200 to-purple-200 animate-pulse" style="width: 85%; margin-left: 7.5%;"></div>

          <!-- Animated Progress Overlay -->
          <div class="absolute top-20 left-0 h-1 bg-gradient-to-r from-blue-500 via-teal-500 via-orange-500 to-purple-500 progress-bar" style="width: 85%; margin-left: 7.5%;"></div>

          <!-- Arrow Indicators Between Steps -->
          <div class="absolute top-16 left-1/4 transform -translate-x-1/2">
            <svg class="w-8 h-8 text-teal-400 animate-bounce-slow" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M13 7l5 5m0 0l-5 5m5-5H6"/>
            </svg>
          </div>
          <div class="absolute top-16 left-1/2 transform -translate-x-1/2">
            <svg class="w-8 h-8 text-orange-400 animate-bounce-slow" style="animation-delay: 0.2s" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M13 7l5 5m0 0l-5 5m5-5H6"/>
            </svg>
          </div>
          <div class="absolute top-16 left-3/4 transform -translate-x-1/2">
            <svg class="w-8 h-8 text-purple-400 animate-bounce-slow" style="animation-delay: 0.4s" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M13 7l5 5m0 0l-5 5m5-5H6"/>
            </svg>
          </div>

          <div class="grid grid-cols-4 gap-8 relative">
            <!-- Step 1: Initial Contact -->
            <div class="relative">
              <div class="flex flex-col items-center">
                <!-- Step Number Circle -->
                <div class="relative z-10 w-16 h-16 rounded-full bg-gradient-to-br from-blue-500 to-blue-600 flex items-center justify-center shadow-lg mb-6">
                  <span class="text-white text-2xl font-bold">1</span>
                </div>

                <!-- Icon Circle -->
                <div class="w-24 h-24 rounded-full bg-gradient-to-br from-blue-50 to-blue-100 flex items-center justify-center mb-4 shadow-md border-4 border-white">
                  <svg class="w-12 h-12 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                  </svg>
                </div>

                <div class="bg-white rounded-2xl p-6 shadow-lg border-t-4 border-blue-500 hover:shadow-xl transition-all duration-300 h-full relative overflow-hidden">
                  <!-- Decorative corner accent -->
                  <div class="absolute top-0 right-0 w-20 h-20 bg-blue-50 rounded-bl-full opacity-50"></div>
                  <div class="absolute bottom-0 left-0 w-16 h-16 bg-blue-100 rounded-tr-full opacity-30"></div>

                  <div class="relative z-10">
                    <div class="flex items-center justify-between mb-3">
                      <h4 class="font-bold text-lg text-blue-600">Initial Contact</h4>
                      <span class="text-xs bg-blue-100 text-blue-600 px-2 py-1 rounded-full font-semibold">Step 1</span>
                    </div>
                    <p class="text-gray-600 text-sm leading-relaxed">A child or concerned individual calls the toll-free 116 helpline or reaches out via WhatsApp.</p>
                    <div class="mt-4 flex items-center gap-2">
                      <div class="w-2 h-2 bg-blue-500 rounded-full animate-pulse"></div>
                      <span class="text-xs text-blue-600 font-semibold">⏱️ Immediate Response</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Step 2: Counselor Support -->
            <div class="relative">
              <div class="flex flex-col items-center">
                <!-- Step Number Circle -->
                <div class="relative z-10 w-16 h-16 rounded-full bg-gradient-to-br from-teal-500 to-teal-600 flex items-center justify-center shadow-lg mb-6">
                  <span class="text-white text-2xl font-bold">2</span>
                </div>

                <!-- Icon Circle -->
                <div class="w-24 h-24 rounded-full bg-gradient-to-br from-teal-50 to-teal-100 flex items-center justify-center mb-4 shadow-md border-4 border-white">
                  <svg class="w-12 h-12 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                  </svg>
                </div>

                <div class="bg-white rounded-2xl p-6 shadow-lg border-t-4 border-teal-500 hover:shadow-xl transition-all duration-300 h-full relative overflow-hidden">
                  <!-- Decorative corner accent -->
                  <div class="absolute top-0 right-0 w-20 h-20 bg-teal-50 rounded-bl-full opacity-50"></div>
                  <div class="absolute bottom-0 left-0 w-16 h-16 bg-teal-100 rounded-tr-full opacity-30"></div>

                  <div class="relative z-10">
                    <div class="flex items-center justify-between mb-3">
                      <h4 class="font-bold text-lg text-teal-600">Counselor Support</h4>
                      <span class="text-xs bg-teal-100 text-teal-600 px-2 py-1 rounded-full font-semibold">Step 2</span>
                    </div>
                    <p class="text-gray-600 text-sm leading-relaxed">Trained counselors provide immediate emotional support and gather essential information with empathy.</p>
                    <div class="mt-4 flex items-center gap-2">
                      <div class="w-2 h-2 bg-teal-500 rounded-full animate-pulse"></div>
                      <span class="text-xs text-teal-600 font-semibold">🎯 Professional Care</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Step 3: Case Assessment -->
            <div class="relative">
              <div class="flex flex-col items-center">
                <!-- Step Number Circle -->
                <div class="relative z-10 w-16 h-16 rounded-full bg-gradient-to-br from-orange-500 to-orange-600 flex items-center justify-center shadow-lg mb-6">
                  <span class="text-white text-2xl font-bold">3</span>
                </div>

                <!-- Icon Circle -->
                <div class="w-24 h-24 rounded-full bg-gradient-to-br from-orange-50 to-orange-100 flex items-center justify-center mb-4 shadow-md border-4 border-white">
                  <svg class="w-12 h-12 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
                  </svg>
                </div>

                <div class="bg-white rounded-2xl p-6 shadow-lg border-t-4 border-orange-500 hover:shadow-xl transition-all duration-300 h-full relative overflow-hidden">
                  <!-- Decorative corner accent -->
                  <div class="absolute top-0 right-0 w-20 h-20 bg-orange-50 rounded-bl-full opacity-50"></div>
                  <div class="absolute bottom-0 left-0 w-16 h-16 bg-orange-100 rounded-tr-full opacity-30"></div>

                  <div class="relative z-10">
                    <div class="flex items-center justify-between mb-3">
                      <h4 class="font-bold text-lg text-orange-600">Case Assessment</h4>
                      <span class="text-xs bg-orange-100 text-orange-600 px-2 py-1 rounded-full font-semibold">Step 3</span>
                    </div>
                    <p class="text-gray-600 text-sm leading-relaxed">The case is documented, assessed for urgency level, and classified according to protection needs.</p>
                    <div class="mt-4 flex items-center gap-2">
                      <div class="w-2 h-2 bg-orange-500 rounded-full animate-pulse"></div>
                      <span class="text-xs text-orange-600 font-semibold">📋 Detailed Documentation</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Step 4: Referral & Follow-up -->
            <div class="relative">
              <div class="flex flex-col items-center">
                <!-- Step Number Circle -->
                <div class="relative z-10 w-16 h-16 rounded-full bg-gradient-to-br from-purple-500 to-purple-600 flex items-center justify-center shadow-lg mb-6">
                  <span class="text-white text-2xl font-bold">4</span>
                </div>

                <!-- Icon Circle -->
                <div class="w-24 h-24 rounded-full bg-gradient-to-br from-purple-50 to-purple-100 flex items-center justify-center mb-4 shadow-md border-4 border-white">
                  <svg class="w-12 h-12 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>

                <div class="bg-white rounded-2xl p-6 shadow-lg border-t-4 border-purple-500 hover:shadow-xl transition-all duration-300 h-full relative overflow-hidden">
                  <!-- Decorative corner accent -->
                  <div class="absolute top-0 right-0 w-20 h-20 bg-purple-50 rounded-bl-full opacity-50"></div>
                  <div class="absolute bottom-0 left-0 w-16 h-16 bg-purple-100 rounded-tr-full opacity-30"></div>

                  <!-- Success badge for final step -->
                  <div class="absolute top-4 left-4 w-12 h-12 bg-green-100 rounded-full flex items-center justify-center opacity-20">
                    <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"/>
                    </svg>
                  </div>

                  <div class="relative z-10">
                    <div class="flex items-center justify-between mb-3">
                      <h4 class="font-bold text-lg text-purple-600">Referral & Follow-up</h4>
                      <span class="text-xs bg-purple-100 text-purple-600 px-2 py-1 rounded-full font-semibold">Step 4</span>
                    </div>
                    <p class="text-gray-600 text-sm leading-relaxed">Referrals are made to relevant authorities and continuous follow-up ensures case resolution.</p>
                    <div class="mt-4 flex items-center gap-2">
                      <div class="w-2 h-2 bg-purple-500 rounded-full animate-pulse"></div>
                      <span class="text-xs text-purple-600 font-semibold">✅ Action & Closure</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Mobile Flow - Vertical -->
        <div class="md:hidden space-y-8">
          <!-- Step 1 -->
          <div class="relative pl-16">
            <div class="absolute left-6 top-0 bottom-0 w-1 bg-gradient-to-b from-blue-400 to-teal-400"></div>
            <div class="absolute left-0 top-0 w-12 h-12 rounded-full bg-gradient-to-br from-blue-500 to-blue-600 flex items-center justify-center shadow-lg z-10">
              <span class="text-white text-xl font-bold">1</span>
            </div>
            <div class="bg-white rounded-xl p-6 shadow-lg border-l-4 border-blue-500">
              <div class="flex items-center gap-3 mb-3">
                <div class="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center">
                  <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                  </svg>
                </div>
                <h4 class="font-bold text-blue-600">Initial Contact</h4>
              </div>
              <p class="text-gray-600 text-sm">A child or concerned individual calls the toll-free 116 helpline or reaches out via WhatsApp.</p>
            </div>
          </div>

          <!-- Step 2 -->
          <div class="relative pl-16">
            <div class="absolute left-6 top-0 bottom-0 w-1 bg-gradient-to-b from-teal-400 to-orange-400"></div>
            <div class="absolute left-0 top-0 w-12 h-12 rounded-full bg-gradient-to-br from-teal-500 to-teal-600 flex items-center justify-center shadow-lg z-10">
              <span class="text-white text-xl font-bold">2</span>
            </div>
            <div class="bg-white rounded-xl p-6 shadow-lg border-l-4 border-teal-500">
              <div class="flex items-center gap-3 mb-3">
                <div class="w-12 h-12 rounded-full bg-teal-50 flex items-center justify-center">
                  <svg class="w-6 h-6 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                  </svg>
                </div>
                <h4 class="font-bold text-teal-600">Counselor Support</h4>
              </div>
              <p class="text-gray-600 text-sm">Trained counselors provide immediate emotional support and gather essential information with empathy.</p>
            </div>
          </div>

          <!-- Step 3 -->
          <div class="relative pl-16">
            <div class="absolute left-6 top-0 bottom-0 w-1 bg-gradient-to-b from-orange-400 to-purple-400"></div>
            <div class="absolute left-0 top-0 w-12 h-12 rounded-full bg-gradient-to-br from-orange-500 to-orange-600 flex items-center justify-center shadow-lg z-10">
              <span class="text-white text-xl font-bold">3</span>
            </div>
            <div class="bg-white rounded-xl p-6 shadow-lg border-l-4 border-orange-500">
              <div class="flex items-center gap-3 mb-3">
                <div class="w-12 h-12 rounded-full bg-orange-50 flex items-center justify-center">
                  <svg class="w-6 h-6 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
                  </svg>
                </div>
                <h4 class="font-bold text-orange-600">Case Assessment</h4>
              </div>
              <p class="text-gray-600 text-sm">The case is documented, assessed for urgency level, and classified according to protection needs.</p>
            </div>
          </div>

          <!-- Step 4 -->
          <div class="relative pl-16">
            <div class="absolute left-0 top-0 w-12 h-12 rounded-full bg-gradient-to-br from-purple-500 to-purple-600 flex items-center justify-center shadow-lg z-10">
              <span class="text-white text-xl font-bold">4</span>
            </div>
            <div class="bg-white rounded-xl p-6 shadow-lg border-l-4 border-purple-500">
              <div class="flex items-center gap-3 mb-3">
                <div class="w-12 h-12 rounded-full bg-purple-50 flex items-center justify-center">
                  <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <h4 class="font-bold text-purple-600">Referral & Follow-up</h4>
              </div>
              <p class="text-gray-600 text-sm">Referrals are made to relevant authorities and continuous follow-up ensures case resolution.</p>
            </div>
          </div>
        </div>

        <!-- Key Metrics Banner -->
        <div class="mt-16 bg-gradient-to-r from-blue-600 to-purple-600 rounded-2xl p-8 text-white shadow-xl">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-center">
            <div>
              <div class="text-4xl font-bold mb-2">24/7</div>
              <div class="text-blue-100">Always Available</div>
            </div>
            <div>
              <div class="text-4xl font-bold mb-2">100%</div>
              <div class="text-blue-100">Confidential</div>
            </div>
            <div>
              <div class="text-4xl font-bold mb-2">Free</div>
              <div class="text-blue-100">Toll-Free Service</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section-padding">
      <div class="container-custom">
        <h3 class="text-center mb-10">Operational Highlights</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="avm-card"><h4 class="font-semibold mb-1">116 Toll-Free Helpline</h4><p class="text-gray-600 text-sm">Accessible nationwide across all telecom networks.</p></div>
          <div class="avm-card"><h4 class="font-semibold mb-1">24/7 Availability</h4><p class="text-gray-600 text-sm">Help any time of day, all year round.</p></div>
          <div class="avm-card"><h4 class="font-semibold mb-1">Language Support</h4><p class="text-gray-600 text-sm">English, Luganda, Swahili, and additional local languages.</p></div>
          <div class="avm-card"><h4 class="font-semibold mb-1">Strict Confidentiality</h4><p class="text-gray-600 text-sm">Handled with the utmost privacy.</p></div>
          <div class="avm-card"><h4 class="font-semibold mb-1">Trained Professionals</h4><p class="text-gray-600 text-sm">Counselors undergo rigorous training.</p></div>
          <div class="avm-card"><h4 class="font-semibold mb-1">Multiple Channels</h4><p class="text-gray-600 text-sm">WhatsApp, U-Report, SafePal App, email, and walk-ins.</p></div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import operationsImage from '@/assets/operations-case-flow.jpg'
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
  0%, 100% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(10px);
  }
}

@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

@keyframes pulse-glow {
  0%, 100% {
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
