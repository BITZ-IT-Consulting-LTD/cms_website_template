<template>
  <section class="section-padding bg-gradient-to-b from-white to-blue-50 relative overflow-hidden">
    <!-- Background Decorative Elements -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full max-w-7xl opacity-30">
        <svg viewBox="0 0 100 100" preserveAspectRatio="none" class="w-full h-full text-blue-100 fill-current">
          <path d="M50 0 C60 20 40 40 50 60 C60 80 40 100 50 100" stroke="currentColor" stroke-width="40" fill="none" class="blur-3xl" />
        </svg>
      </div>
    </div>

    <div class="container relative z-10">
      <div class="section-header text-center mb-20">
        <span class="text-blue-600 font-bold tracking-wider uppercase text-sm bg-blue-50 px-4 py-1 rounded-full">Our History</span>
        <h2 class="section-title mt-4 text-4xl md:text-5xl">The Sauti Journey</h2>
        <p class="section-subtitle max-w-2xl mx-auto mt-4 text-lg text-gray-600">Growing from a pilot project to a national lifeline for every child in Uganda.</p>
      </div>
      
      <div class="relative max-w-5xl mx-auto">
        <!-- Central Trunk Line -->
        <div class="absolute left-1/2 transform -translate-x-1/2 h-full w-1 bg-gradient-to-b from-blue-200 via-blue-400 to-green-400 rounded-full"></div>
        
        <!-- Timeline Items -->
        <div class="space-y-24">
          <!-- Item 1 -->
          <div class="relative flex items-center justify-between group">
            <div class="w-5/12 text-right pr-12">
              <div class="card bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-lg border border-white/50 hover:shadow-xl transition-all duration-300 transform group-hover:-translate-y-1">
                <h3 class="text-xl font-bold text-gray-900 group-hover:text-blue-600 transition-colors">Lobbying & Designation</h3>
                <p class="text-gray-600 mt-2 text-sm leading-relaxed">MGLSD, with UCRNN and UNICEF, lobbied for 116 to be designated as the national child helpline number.</p>
              </div>
            </div>
            <!-- Branch Connector Left -->
            <div class="absolute left-1/2 top-1/2 -translate-y-1/2 -translate-x-full w-12 h-0.5 bg-blue-300 origin-right transform scale-x-0 group-hover:scale-x-100 transition-transform duration-500"></div>
            
            <!-- Central Node -->
            <div class="absolute left-1/2 transform -translate-x-1/2 w-12 h-12 bg-white border-4 border-blue-500 rounded-full z-10 flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300">
              <span class="text-xs font-bold text-blue-600">2013</span>
            </div>
            
            <div class="w-5/12 pl-12">
              <span class="text-6xl font-bold text-blue-100/50 absolute top-1/2 -translate-y-1/2 left-12 select-none pointer-events-none group-hover:text-blue-200/50 transition-colors">2013</span>
            </div>
          </div>

          <!-- Item 2 -->
          <div class="relative flex items-center justify-between group flex-row-reverse">
            <div class="w-5/12 text-left pl-12">
              <div class="card bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-lg border border-white/50 hover:shadow-xl transition-all duration-300 transform group-hover:-translate-y-1">
                <h3 class="text-xl font-bold text-gray-900 group-hover:text-green-600 transition-colors">Official Toll-Free Number</h3>
                <p class="text-gray-600 mt-2 text-sm leading-relaxed">UCC officially designated 116 as an emergency and toll-free number.</p>
              </div>
            </div>
            <!-- Branch Connector Right -->
            <div class="absolute left-1/2 top-1/2 -translate-y-1/2 w-12 h-0.5 bg-green-300 origin-left transform scale-x-0 group-hover:scale-x-100 transition-transform duration-500"></div>

            <div class="absolute left-1/2 transform -translate-x-1/2 w-12 h-12 bg-white border-4 border-green-500 rounded-full z-10 flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300">
              <svg class="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" /></svg>
            </div>
            
            <div class="w-5/12 text-right pr-12">
              <span class="text-6xl font-bold text-green-100/50 absolute top-1/2 -translate-y-1/2 right-12 select-none pointer-events-none group-hover:text-green-200/50 transition-colors">Aug</span>
            </div>
          </div>

          <!-- Item 3 -->
          <div class="relative flex items-center justify-between group">
            <div class="w-5/12 text-right pr-12">
              <div class="card bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-lg border border-white/50 hover:shadow-xl transition-all duration-300 transform group-hover:-translate-y-1">
                <h3 class="text-xl font-bold text-gray-900 group-hover:text-purple-600 transition-colors">First Call Received</h3>
                <p class="text-gray-600 mt-2 text-sm leading-relaxed">UCHL received the first call on code 116 on 4th November 2013.</p>
              </div>
            </div>
            <div class="absolute left-1/2 top-1/2 -translate-y-1/2 -translate-x-full w-12 h-0.5 bg-purple-300 origin-right transform scale-x-0 group-hover:scale-x-100 transition-transform duration-500"></div>

            <div class="absolute left-1/2 transform -translate-x-1/2 w-12 h-12 bg-white border-4 border-purple-500 rounded-full z-10 flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300">
              <svg class="w-6 h-6 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" /></svg>
            </div>
            
            <div class="w-5/12 pl-12">
              <span class="text-6xl font-bold text-purple-100/50 absolute top-1/2 -translate-y-1/2 left-12 select-none pointer-events-none group-hover:text-purple-200/50 transition-colors">Nov</span>
            </div>
          </div>

          <!-- Item 4 -->
          <div class="relative flex items-center justify-between group flex-row-reverse">
            <div class="w-5/12 text-left pl-12">
              <div class="card bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-lg border border-white/50 hover:shadow-xl transition-all duration-300 transform group-hover:-translate-y-1">
                <h3 class="text-xl font-bold text-gray-900 group-hover:text-orange-600 transition-colors">Government Takes Over</h3>
                <p class="text-gray-600 mt-2 text-sm leading-relaxed">MGLSD took over the management of UCHL from UCRNN.</p>
              </div>
            </div>
            <div class="absolute left-1/2 top-1/2 -translate-y-1/2 w-12 h-0.5 bg-orange-300 origin-left transform scale-x-0 group-hover:scale-x-100 transition-transform duration-500"></div>

            <div class="absolute left-1/2 transform -translate-x-1/2 w-12 h-12 bg-white border-4 border-orange-500 rounded-full z-10 flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300">
              <svg class="w-6 h-6 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" /></svg>
            </div>
            
            <div class="w-5/12 text-right pr-12">
              <span class="text-6xl font-bold text-orange-100/50 absolute top-1/2 -translate-y-1/2 right-12 select-none pointer-events-none group-hover:text-orange-200/50 transition-colors">2014</span>
            </div>
          </div>

           <!-- Item 5 -->
          <div class="relative flex items-center justify-between group">
            <div class="w-5/12 text-right pr-12">
              <div class="card bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-lg border border-white/50 hover:shadow-xl transition-all duration-300 transform group-hover:-translate-y-1">
                <h3 class="text-xl font-bold text-gray-900 group-hover:text-red-600 transition-colors">Legal Framework</h3>
                <p class="text-gray-600 mt-2 text-sm leading-relaxed">UCHL instituted by law (Children’s Act cap 59 2016, as amended) section 42 C.</p>
              </div>
            </div>
            <div class="absolute left-1/2 top-1/2 -translate-y-1/2 -translate-x-full w-12 h-0.5 bg-red-300 origin-right transform scale-x-0 group-hover:scale-x-100 transition-transform duration-500"></div>

            <div class="absolute left-1/2 transform -translate-x-1/2 w-12 h-12 bg-white border-4 border-red-500 rounded-full z-10 flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300">
              <svg class="w-6 h-6 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3" /></svg>
            </div>
            
            <div class="w-5/12 pl-12">
              <span class="text-6xl font-bold text-red-100/50 absolute top-1/2 -translate-y-1/2 left-12 select-none pointer-events-none group-hover:text-red-200/50 transition-colors">2016</span>
            </div>
          </div>

           <!-- Item 6 -->
          <div class="relative flex items-center justify-between group flex-row-reverse">
            <div class="w-5/12 text-left pl-12">
              <div class="card bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-lg border border-white/50 hover:shadow-xl transition-all duration-300 transform group-hover:-translate-y-1">
                <h3 class="text-xl font-bold text-gray-900 group-hover:text-teal-600 transition-colors">GBV Integration</h3>
                <p class="text-gray-600 mt-2 text-sm leading-relaxed">Gender-based violence response integrated into Sauti’s work nationwide.</p>
              </div>
            </div>
            <div class="absolute left-1/2 top-1/2 -translate-y-1/2 w-12 h-0.5 bg-teal-300 origin-left transform scale-x-0 group-hover:scale-x-100 transition-transform duration-500"></div>

            <div class="absolute left-1/2 transform -translate-x-1/2 w-12 h-12 bg-white border-4 border-teal-500 rounded-full z-10 flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300">
              <svg class="w-6 h-6 text-teal-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
            </div>
            
            <div class="w-5/12 text-right pr-12">
              <span class="text-6xl font-bold text-teal-100/50 absolute top-1/2 -translate-y-1/2 right-12 select-none pointer-events-none group-hover:text-teal-200/50 transition-colors">2021</span>
            </div>
          </div>
        </div>
      </div>
      
      <div class="text-center mt-24">
        <p class="text-gray-500 text-lg leading-relaxed max-w-4xl mx-auto italic">
          "Aligned with ITU recommendation for 116 child helplines; operated under MGLSD in collaboration with NGOs and UN partners."
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
// No script needed for this static component
</script>

<style scoped>
/* Custom animations if needed */
</style>
