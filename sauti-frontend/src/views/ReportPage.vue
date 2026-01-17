<template>
  <div class="min-h-screen bg-gradient-to-b from-white via-white to-gray-50" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
    <!-- 1. Hero Section -->
    <header class="py-16 md:py-20 text-center relative overflow-hidden">
      <!-- Background Gradient Decoration -->
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-primary/5 rounded-full blur-3xl -z-10 opacity-60"></div>

      <div class="container-custom relative z-10 px-4">
        <h1 class="text-4xl md:text-5xl font-bold text-secondary mb-4 tracking-tight" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
          Report a <span class="text-primary">Case</span>
        </h1>
        <p class="text-lg md:text-xl text-gray-600 max-w-2xl mx-auto leading-relaxed mb-8" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
          A safe, confidential, and professional space to seek help. We are available 24/7 to support you.
        </p>
        
        <!-- Trust Badges -->
        <div class="flex flex-wrap justify-center gap-4 text-sm font-bold text-gray-500 uppercase tracking-wider" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
          <div class="flex items-center gap-2 px-6 py-2 bg-white rounded-full shadow-sm border border-gray-100">
            <Lock class="w-5 h-5 text-emerald-500" />
            <span>Secure</span>
          </div>
          <div class="flex items-center gap-2 px-6 py-2 bg-white rounded-full shadow-sm border border-gray-100">
            <Clock class="w-5 h-5 text-blue-500" />
            <span>24/7 Support</span>
          </div>
        </div>
      </div>
    </header>

    <!-- 2. Main Content Grid -->
    <div class="container-custom pb-24 px-4">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start">

        <!-- Left Column (Primary - 8 cols) -->
        <main class="lg:col-span-8 space-y-8 flex flex-col">
          
          <!-- Report Form Component (Prioritized on Mobile) -->
          <section aria-label="Reporting Interface" class="order-1">
            <ReportForm />
          </section>

          <!-- Contextual Steps (1-2-3 Guide) - Moved below form on mobile/desktop flow -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8 order-2 mt-8">
            <div class="bg-white p-6 rounded-3xl shadow-sm border border-gray-100 relative group hover:border-primary/20 transition-all">
              <span class="absolute -top-4 -left-4 w-10 h-10 bg-primary text-white rounded-xl flex items-center justify-center font-bold text-lg shadow-lg rotate-3 group-hover:rotate-6 transition-transform" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">1</span>
              <h3 class="font-bold text-secondary text-lg mb-2 mt-2" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Provide Details</h3>
              <p class="text-sm text-gray-500 leading-relaxed" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Chat with our secure assistant to share what happened at your own pace.</p>
            </div>
            <div class="bg-white p-6 rounded-3xl shadow-sm border border-gray-100 relative group hover:border-primary/20 transition-all">
              <span class="absolute -top-4 -left-4 w-10 h-10 bg-primary text-white rounded-xl flex items-center justify-center font-bold text-lg shadow-lg -rotate-3 group-hover:-rotate-6 transition-transform" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">2</span>
              <h3 class="font-bold text-secondary text-lg mb-2 mt-2" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Submit Securely</h3>
              <p class="text-sm text-gray-500 leading-relaxed" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Your report is encrypted and sent directly to our protection team.</p>
            </div>
            <div class="bg-white p-6 rounded-3xl shadow-sm border border-gray-100 relative group hover:border-primary/20 transition-all">
              <span class="absolute -top-4 -left-4 w-10 h-10 bg-primary text-white rounded-xl flex items-center justify-center font-bold text-lg shadow-lg rotate-3 group-hover:rotate-6 transition-transform" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">3</span>
              <h3 class="font-bold text-secondary text-lg mb-2 mt-2" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">We Follow Up</h3>
              <p class="text-sm text-gray-500 leading-relaxed" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">A professional caseworker reviews your case and contacts you for support.</p>
            </div>
          </div>

        </main>

        <!-- Right Column (Sidebar - 4 cols) -->
        <aside class="lg:col-span-4 space-y-6">

          <!-- Immediate Help Card -->
          <div class="bg-red-50 rounded-[2.5rem] p-8 shadow-sm border border-red-100">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 bg-red-100 rounded-full flex items-center justify-center text-red-600">
                <TriangleAlert class="w-5 h-5" />
              </div>
              <h3 class="font-bold text-red-900 text-lg" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Immediate Danger?</h3>
            </div>
            <p class="text-red-800/70 text-sm font-medium leading-relaxed mb-8" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
              If you or someone else is in immediate physical danger, do not use this form. Get instant help now.
            </p>
            <div class="space-y-4">
              <a href="tel:116" class="flex items-center justify-center gap-3 w-full py-4 bg-red-600 hover:bg-red-700 text-white font-bold rounded-2xl shadow-lg shadow-red-200 transition-all active:scale-95" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
                <Phone class="w-5 h-5" />
                <span>Call 116 Free</span>
              </a>
              <a href="https://wa.me/256743889999" class="flex items-center justify-center gap-3 w-full py-4 bg-white border-2 border-green-500 text-green-600 hover:bg-green-50 font-bold rounded-2xl transition-all" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
                <MessageCircle class="w-5 h-5" />
                <span>WhatsApp Chat</span>
              </a>
            </div>
          </div>

          <!-- Other Channels -->
          <div class="bg-gray-50 rounded-[2.5rem] p-8 border border-gray-100">
            <h3 class="font-bold text-secondary text-lg mb-6" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Other Ways to Report</h3>
            <div class="space-y-4">
              <div class="flex items-center gap-4 p-4 bg-white rounded-2xl shadow-sm border border-gray-100">
                <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
                  <MessageSquareText class="w-5 h-5" />
                </div>
                <div>
                  <p class="text-xs font-bold text-gray-400 uppercase tracking-wide" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">SMS Shortcode</p>
                  <p class="font-bold text-secondary" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Text to 8500</p>
                </div>
              </div>
              <div class="flex items-center gap-4 p-4 bg-white rounded-2xl shadow-sm border border-gray-100">
                <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center">
                  <Smartphone class="w-5 h-5" />
                </div>
                <div>
                  <p class="text-xs font-bold text-gray-400 uppercase tracking-wide" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Mobile App</p>
                  <p class="font-bold text-secondary" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">SafePal App</p>
                </div>
              </div>
              <div class="flex items-center gap-4 p-4 bg-white rounded-2xl shadow-sm border border-gray-100">
                <div class="w-10 h-10 rounded-xl bg-orange-50 text-orange-600 flex items-center justify-center">
                  <Mail class="w-5 h-5" />
                </div>
                <div>
                  <p class="text-xs font-bold text-gray-400 uppercase tracking-wide" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Email</p>
                  <p class="font-bold text-secondary break-all text-sm" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">info@sauti.mglsd.go.ug</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Privacy Footer Link -->
          <div class="text-center py-4">
            <router-link to="/privacy" class="inline-flex items-center gap-2 text-xs font-bold text-gray-400 hover:text-primary transition-colors uppercase tracking-widest" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
              <Lock class="w-3 h-3" />
              View Full Privacy Policy
            </router-link>
          </div>

        </aside>
      </div>
    </div>
  </div>
</template>

<script setup>
  import ReportForm from '@/components/reports/ReportForm.vue'

  import {
    ShieldCheck,
    Phone,
    MessageCircle,
    MessageSquareText,
    Mail,
    Globe,
    TriangleAlert,
    Smartphone,
    Lock,
    Clock
  } from 'lucide-vue-next'

  defineOptions({
    name: 'ReportPage'
  })
</script>
