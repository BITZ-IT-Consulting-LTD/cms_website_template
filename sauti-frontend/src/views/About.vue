<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-b from-white via-white to-gray-50"></div>
      <div class="container-custom relative py-16 md:py-24">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
          <div class="lg:col-span-7">
            <h1 class="mb-4">About Sauti Child Helpline</h1>
            <p class="text-xl text-gray-600 max-w-2xl">
              Uganda's national child helpline—free, confidential and accessible 24/7 across all telecoms.
              We protect and empower children, GBV survivors and migrant workers with rapid, compassionate support.
            </p>
            <div class="mt-6 flex flex-wrap gap-3">
              <a href="tel:116" class="pill pill-primary" aria-label="Call the 116 helpline">Call 116</a>
              <router-link to="/report" class="pill pill-outline">Report a Case</router-link>
            </div>
            <div class="mt-6 flex flex-wrap gap-3 text-sm text-gray-600">
              <span class="badge-blue">24/7</span>
              <span class="badge-orange">All Telecoms</span>
              <span class="badge-teal">EN • LG • SW</span>
            </div>
          </div>
          <div class="lg:col-span-5">
            <div class="card p-0 overflow-hidden">
              <img src="https://images.unsplash.com/photo-1578662996442-48f60103fc96?q=80&w=1600&auto=format&fit=crop" alt="Children receiving support and care in Uganda" class="w-full h-72 md:h-96 object-cover" />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Stats / At-a-glance -->
    <section class="section-padding">
      <div class="container-custom">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
          <div class="avm-card text-center"><h3 class="text-3xl font-extrabold">116</h3><p class="text-gray-600">Toll-free</p></div>
          <div class="avm-card text-center"><h3 class="text-3xl font-extrabold">24/7</h3><p class="text-gray-600">Availability</p></div>
          <div class="avm-card text-center"><h3 class="text-3xl font-extrabold">3+</h3><p class="text-gray-600">Languages</p></div>
          <div class="avm-card text-center"><h3 class="text-3xl font-extrabold">Nationwide</h3><p class="text-gray-600">All telecoms</p></div>
        </div>
      </div>
    </section>

    <!-- Mission & Services -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 items-start">
          <div>
            <h2 class="mb-3">Our Mission</h2>
            <p class="text-gray-700 leading-relaxed">
              To protect and empower vulnerable populations through accessible, confidential, and
              professional support services available 24/7.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-6">
              <div class="service-card p-5">
                <h4 class="mb-1">Telephone counseling</h4>
                <p class="text-gray-600 text-sm">Immediate, confidential support via 116.</p>
              </div>
              <div class="service-card p-5">
                <h4 class="mb-1">Walk-in support</h4>
                <p class="text-gray-600 text-sm">On-site help and rapid referrals.</p>
              </div>
              <div class="service-card p-5">
                <h4 class="mb-1">Media & U-Report</h4>
                <p class="text-gray-600 text-sm">Engagement via broadcast and U-Report 8500.</p>
              </div>
              <div class="service-card p-5">
                <h4 class="mb-1">Guidance & referral</h4>
                <p class="text-gray-600 text-sm">Connections to specialized services.</p>
              </div>
              <div class="service-card p-5 sm:col-span-2">
                <h4 class="mb-1">Community sensitization</h4>
                <p class="text-gray-600 text-sm">Awareness and advocacy in communities.</p>
              </div>
            </div>
          </div>
          <div>
            <h2 class="mb-3">Core Values</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div class="avm-card">
                <div class="avm-icon bg-blue-50 text-blue-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11c0 1.657-1.343 3-3 3S6 12.657 6 11s1.343-3 3-3 3 1.343 3 3z"/></svg></div>
                <h3 class="avm-title">Confidentiality</h3>
                <p class="avm-text">Your privacy is protected at every step.</p>
              </div>
              <div class="avm-card">
                <div class="avm-icon bg-teal-50 text-teal-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4"/></svg></div>
                <h3 class="avm-title">Responsiveness</h3>
                <p class="avm-text">Rapid, empathetic assistance 24/7.</p>
              </div>
              <div class="avm-card">
                <div class="avm-icon bg-orange-50 text-orange-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v12"/></svg></div>
                <h3 class="avm-title">Compassion</h3>
                <p class="avm-text">We listen with care and dignity.</p>
              </div>
              <div class="avm-card">
                <div class="avm-icon bg-purple-50 text-purple-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14"/></svg></div>
                <h3 class="avm-title">Integrity</h3>
                <p class="avm-text">We act with honesty and accountability.</p>
              </div>
              <div class="avm-card">
                <div class="avm-icon bg-blue-50 text-blue-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7H7v6h6V7z"/></svg></div>
                <h3 class="avm-title">Empowerment</h3>
                <p class="avm-text">We enable informed, safe choices.</p>
              </div>
              <div class="avm-card">
                <div class="avm-icon bg-teal-50 text-teal-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5V4H2v16h5"/></svg></div>
                <h3 class="avm-title">Collaboration</h3>
                <p class="avm-text">We partner across sectors for impact.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- History Timeline -->
    <section class="section-padding">
      <div class="container-custom">
        <h2 class="text-center mb-3">Our History</h2>
        <p class="text-center text-gray-600 mb-10">From early NGO partnerships to national designation and global alignment with ITU 116.</p>
        <div class="relative max-w-4xl mx-auto">
          <div class="timeline-line"></div>
          <div class="timeline-item left">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm text-primary-600 font-bold">2005</h4>
              <h3 class="text-lg font-bold mb-1">Origins</h3>
              <p class="text-gray-600">Child helpline initiative launched with NGOs and UN partners.</p>
            </div>
          </div>
          <div class="timeline-item right">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm text-primary-600 font-bold">2010</h4>
              <h3 class="text-lg font-bold mb-1">Sauti Established</h3>
              <p class="text-gray-600">National rollout of the Sauti helpline service.</p>
            </div>
          </div>
          <div class="timeline-item left">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm text-primary-600 font-bold">2016</h4>
              <h3 class="text-lg font-bold mb-1">Legal & Regulatory</h3>
              <p class="text-gray-600">UCC assigns 116; alignment with ITU recommendations and national child protection frameworks.</p>
            </div>
          </div>
          <div class="timeline-item right">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm text-primary-600 font-bold">Today</h4>
              <h3 class="text-lg font-bold mb-1">Government-led</h3>
              <p class="text-gray-600">Operated by MGLSD with UNICEF, UCRNN and partners for nationwide impact.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Partners / Legitimacy -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom">
        <h2 class="text-center mb-8">Partners & Affiliations</h2>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 items-center">
          <div class="card p-6 text-center">MGLSD</div>
          <div class="card p-6 text-center">UNICEF</div>
          <div class="card p-6 text-center">UCRNN</div>
          <div class="card p-6 text-center">ITU 116</div>
        </div>
        <p class="text-center text-gray-500 text-sm mt-6">Legally designated 116 child helpline; compliant with national and international standards.</p>
      </div>
    </section>

    <!-- CTA -->
    <section class="section-padding">
      <div class="container-custom text-center">
        <h2 class="mb-3">Need help or ready to partner?</h2>
        <p class="text-gray-600 max-w-2xl mx-auto">Reach out any time. Your call or message could change a life.</p>
        <div class="mt-6 flex flex-wrap justify-center gap-3">
          <a href="tel:116" class="pill pill-primary">Call 116</a>
          <router-link to="/report" class="pill pill-outline">Report a Case</router-link>
          <router-link to="/contact" class="pill pill-light">Contact Us</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
</script>
