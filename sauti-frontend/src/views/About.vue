<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-b from-white via-white to-gray-50"></div>
      <div class="container-custom relative py-16 md:py-24">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
          <div class="lg:col-span-7">
            <h1 class="mb-4">About Sauti 116 helpline</h1>
            <p class="text-xl max-w-2xl" style="color: #555555;">
              Uganda's national child helpline—free, confidential and accessible 24/7 across all telecoms.
              We protect and empower children, GBV survivors and migrant workers with rapid, compassionate support.
            </p>
            <div class="mt-6 flex flex-wrap gap-3">
              <a href="tel:116" class="pill pill-primary" aria-label="Call the 116 helpline">Call 116</a>
              <router-link to="/report" class="pill pill-outline">Report a Case</router-link>
            </div>
            <div class="mt-6 flex flex-wrap gap-3 text-sm" style="color: #555555;">
              <span class="badge-blue">24/7</span>
              <span class="badge-orange">All Telecoms</span>
              <span class="badge-teal">EN • LG • SW</span>
            </div>
          </div>
          <div class="lg:col-span-5">
            <div class="card p-0 overflow-hidden">
              <img :src="sautiAboutpage" alt="African children in Uganda - happy children receiving support and care through Sauti 116 helpline services" class="w-full h-72 md:h-96 object-cover" />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Stats / At-a-glance -->
    <section class="section-padding">
      <div class="container-custom">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
          <div class="avm-card text-center"><h3 class="text-3xl font-extrabold">116</h3><p style="color: #555555;">Toll-free</p></div>
          <div class="avm-card text-center"><h3 class="text-3xl font-extrabold">24/7</h3><p style="color: #555555;">Availability</p></div>
          <div class="avm-card text-center"><h3 class="text-3xl font-extrabold">3+</h3><p style="color: #555555;">Languages</p></div>
          <div class="avm-card text-center"><h3 class="text-3xl font-extrabold">Nationwide</h3><p style="color: #555555;">All telecoms</p></div>
        </div>
      </div>
    </section>

    <!-- Mission & Services -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 items-start">
          <div>
            <h2 class="mb-3">Our Mission</h2>
            <p class="leading-relaxed" style="color: #222222;">
              To protect and empower vulnerable populations through accessible, confidential, and
              professional support services available 24/7.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-6">
              <div class="service-card p-5">
                <h4 class="mb-1">Telephone counseling</h4>
                <p class="text-sm" style="color: #555555;">Immediate, confidential support via 116.</p>
              </div>
              <div class="service-card p-5">
                <h4 class="mb-1">Walk-in support</h4>
                <p class="text-sm" style="color: #555555;">On-site help and rapid referrals.</p>
              </div>
              <div class="service-card p-5">
                <h4 class="mb-1">Media & U-Report</h4>
                <p class="text-sm" style="color: #555555;">Engagement via broadcast and U-Report 8500.</p>
              </div>
              <div class="service-card p-5">
                <h4 class="mb-1">Guidance & referral</h4>
                <p class="text-sm" style="color: #555555;">Connections to specialized services.</p>
              </div>
              <div class="service-card p-5 sm:col-span-2">
                <h4 class="mb-1">Community sensitization</h4>
                <p class="text-sm" style="color: #555555;">Awareness and advocacy in communities.</p>
              </div>
            </div>
          </div>
          <div>
            <h2 class="mb-3">Core Values</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div class="avm-card">
                <div class="avm-icon bg-blue-50 text-blue-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11c0 1.657-1.343 3-3 3S6 12.657 6 11s1.343-3 3-3 3 1.343 3 3z"/></svg></div>
                <h3 class="avm-title">Confidentiality</h3>
                <p class="avm-text">We are committed to handling all reported cases with the utmost confidence, ensuring your privacy and safety throughout the process.</p>
              </div>
              <div class="avm-card">
                <div class="avm-icon bg-teal-50 text-teal-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4"/></svg></div>
                <h3 class="avm-title">Responsiveness</h3>
                <p class="avm-text">Our promise is to be responsive, ensuring that we acknowledge and act upon every case reported to our service.</p>
              </div>
              <div class="avm-card">
                <div class="avm-icon bg-orange-50 text-orange-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v12"/></svg></div>
                <h3 class="avm-title">Compassion</h3>
                <p class="avm-text">We approach our work with deep compassion, recognizing that issues of abuse are deeply personal and require us to handle every case uniquely.</p>
              </div>
              <div class="avm-card">
                <div class="avm-icon bg-purple-50 text-purple-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14"/></svg></div>
                <h3 class="avm-title">Integrity</h3>
                <p class="avm-text">We operate with integrity in all we do, upholding moral uprightness in our work and interactions.</p>
              </div>
              <div class="avm-card">
                <div class="avm-icon bg-blue-50 text-blue-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7H7v6h6V7z"/></svg></div>
                <h3 class="avm-title">Empowerment</h3>
                <p class="avm-text">We are committed to empowerment by sharing essential knowledge on child rights—enabling children and communities to make informed decisions.</p>
              </div>
              <div class="avm-card">
                <div class="avm-icon bg-teal-50 text-teal-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5V4H2v16h5"/></svg></div>
                <h3 class="avm-title">Collaboration</h3>
                <p class="avm-text">Our service is built on collaboration. We work with diverse service sectors, valuing every input to realize and protect the rights of each child in Uganda.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Internal Value Cards -->
    <section class="section-padding">
      <div class="container-custom">
        <h2 class="mb-3">Internal Value Cards (How We Work Together)</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div class="avm-card">
            <div class="avm-icon bg-blue-50 text-blue-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11c0 1.657-1.343 3-3 3S6 12.657 6 11s1.343-3 3-3 3 1.343 3 3z"/></svg></div>
            <h3 class="avm-title">Confidentiality</h3>
            <p class="avm-text">We maintain strict internal confidentiality. Case information is only shared with organizations or people directly involved in its resolution.</p>
          </div>
          <div class="avm-card">
            <div class="avm-icon bg-indigo-50 text-indigo-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-4.553a1.5 1.5 0 00-2.121-2.121L12.879 7.58M9 14l-4.553 4.553a1.5 1.5 0 102.121 2.121L11.121 16.42"/></svg></div>
            <h3 class="avm-title">Innovativeness</h3>
            <p class="avm-text">We embrace new methods and technologies to reach and support as many people as possible, especially children.</p>
          </div>
          <div class="avm-card">
            <div class="avm-icon bg-yellow-50 text-yellow-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17v-6h6v6M9 9V7a3 3 0 016 0v2"/></svg></div>
            <h3 class="avm-title">Accountability</h3>
            <p class="avm-text">We practice full accountability for all cases reported to Sauti, taking responsibility from intake to resolution.</p>
          </div>
          <div class="avm-card">
            <div class="avm-icon bg-teal-50 text-teal-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5V4H2v16h5"/></svg></div>
            <h3 class="avm-title">Collaboration</h3>
            <p class="avm-text">We value every partner's input and work closely across sectors to protect the rights of each child in Uganda.</p>
          </div>
          <div class="avm-card">
            <div class="avm-icon bg-green-50 text-green-600"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg></div>
            <h3 class="avm-title">Transparency</h3>
            <p class="avm-text">We commit to transparency across partnerships—ensuring all Sauti partners are transparent and accountable to each other.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Background / Our Journey -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom">
        <h2 class="text-center mb-4">Background</h2>
        <div class="max-w-5xl mx-auto">
          <ul class="space-y-4 text-lg" style="color: #222222;">
            <li>In early 2013, MGLSD in partnership with UCRNN and UNICEF lobbied for 116 to be designated as a child helpline number.</li>
            <li>August 2013, 116 was officially designated as an emergency and toll‑free number by UCC.</li>
            <li>On 4th November 2013, the first call was received by UCHL on the code 116.</li>
            <li>In December 2014, government (MGLSD) took over the management of UCHL from UCRNN.</li>
            <li>UCHL was instituted by law (Children’s Act cap 59 2016, as amended) section 42 C.</li>
            <li>In 2021, GBV response was integrated into Sauti’s work.</li>
          </ul>
          <p class="text-sm mt-6" style="color: #555555;">Note: In October 2007, ITU asked all countries around the world to allocate 116 to Child Helplines.</p>
        </div>
      </div>
    </section>

    <!-- Our Journey (Milestones) -->
    <section class="section-padding">
      <div class="container-custom">
        <h2 class="text-center mb-4">Our Journey</h2>
        <p class="text-center mb-10" style="color: #555555;">Key milestones in our history of child advocacy and the national designation of 116.</p>
        <div class="relative max-w-5xl mx-auto py-8">
          <div class="timeline-line"></div>
          <!-- 2013 (Lobbying) -->
          <div class="timeline-item left">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm font-bold mb-2" style="color: #009EDB;">2013</h4>
              <h3 class="text-2xl font-bold mb-3" style="color: #222222;">Lobbying & Designation Effort</h3>
              <p class="leading-relaxed" style="color: #555555;">MGLSD, with UCRNN and UNICEF, lobbied for 116 to be designated as Uganda’s child helpline number.</p>
            </div>
          </div>
          <!-- Aug 2013 (UCC Designation) -->
          <div class="timeline-item right">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm font-bold mb-2" style="color: #009EDB;">Aug 2013</h4>
              <h3 class="text-2xl font-bold mb-3" style="color: #222222;">Official Toll‑Free Number</h3>
              <p class="leading-relaxed" style="color: #555555;">UCC officially designated 116 as an emergency and toll‑free number.</p>
            </div>
          </div>
          <!-- Nov 2013 (First Call) -->
          <div class="timeline-item left">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm font-bold mb-2" style="color: #009EDB;">Nov 2013</h4>
              <h3 class="text-2xl font-bold mb-3" style="color: #222222;">First Call Received</h3>
              <p class="leading-relaxed" style="color: #555555;">UCHL received the first call on code 116 on 4th November 2013.</p>
            </div>
          </div>
          <!-- Dec 2014 (Govt takeover) -->
          <div class="timeline-item right">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm font-bold mb-2" style="color: #009EDB;">Dec 2014</h4>
              <h3 class="text-2xl font-bold mb-3" style="color: #222222;">Government Takes Over</h3>
              <p class="leading-relaxed" style="color: #555555;">MGLSD took over the management of UCHL from UCRNN.</p>
            </div>
          </div>
          <!-- 2016 (Legal framework) -->
          <div class="timeline-item left">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm font-bold mb-2" style="color: #009EDB;">2016</h4>
              <h3 class="text-2xl font-bold mb-3" style="color: #222222;">Legal & Regulatory Framework</h3>
              <p class="leading-relaxed" style="color: #555555;">UCHL instituted by law (Children’s Act cap 59 2016, as amended) section 42 C.</p>
            </div>
          </div>
          <!-- 2021 (GBV Integration) -->
          <div class="timeline-item right">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
              <h4 class="text-sm font-bold mb-2" style="color: #009EDB;">2021</h4>
              <h3 class="text-2xl font-bold mb-3" style="color: #222222;">GBV Response Integrated</h3>
              <p class="leading-relaxed" style="color: #555555;">Gender‑based violence response integrated into Sauti’s work nationwide.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Operations -->
    <section class="section-padding">
      <div class="container-custom">
        <h2 class="mb-4">Operations</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-lg" style="color: #222222;">
          <div>
            <ul class="space-y-3">
              <li>Sauti is a Swahili word that means “voice”.</li>
              <li>Operates on short code 116 (toll‑free), accessible from any telecom network.</li>
              <li>Operational 24/7 and accessible from every part of the country.</li>
              <li>The counselors speak a total of 26 local languages.</li>
            </ul>
          </div>
          <div class="hidden md:block"></div>
        </div>
      </div>
    </section>

    <!-- Path to Resolution (Case Flow) -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom">
        <h2 class="text-center mb-10">Path to Resolution</h2>
        <div class="max-w-3xl mx-auto">
          <div class="space-y-6">
            <div class="card p-5 text-center">
              <h3 class="text-xl font-bold" style="color: #222222;">Caller</h3>
              <p class="text-sm" style="color: #555555;">Case reported</p>
            </div>
            <div class="text-center">⬇️</div>
            <div class="card p-5 text-center">
              <h3 class="text-xl font-bold" style="color: #222222;">Call Center</h3>
            </div>
            <div class="text-center">⬇️</div>
            <div class="card p-5 text-center">
              <h3 class="text-xl font-bold" style="color: #222222;">Case Management Department</h3>
            </div>
            <div class="text-center">⬇️</div>
            <div class="card p-5 text-center">
              <h3 class="text-xl font-bold" style="color: #226B5E;">Probation Offices (DACs)</h3>
              <p class="text-sm" style="color: #555555;">Supported by partners & CSOs, police, court, etc.</p>
            </div>
            <div class="text-center">⬇️</div>
            <div class="card p-5 text-center">
              <h3 class="text-xl font-bold" style="color: #222222;">Local Leaders, CDOs, Para‑Social Workers, VHTs, etc.</h3>
              <p class="text-sm" style="color: #555555;">Feedback shared back through the chain.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Partners / Legitimacy -->
    <section class="section-padding">
      <div class="container-custom">
        <h2 class="text-center mb-8">Partners & Affiliations</h2>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 items-center">
          <div class="card p-6 text-center">MGLSD</div>
          <div class="card p-6 text-center">UNICEF</div>
          <div class="card p-6 text-center">UCRNN</div>
          <div class="card p-6 text-center">ITU 116</div>
        </div>
        <p class="text-center text-sm mt-6" style="color: #555555;">Legally designated 116 child helpline; compliant with national and international standards.</p>
      </div>
    </section>

    <!-- CTA -->
    <section class="section-padding">
      <div class="container-custom text-center">
        <h2 class="mb-3">Need help or ready to partner?</h2>
        <p class="max-w-2xl mx-auto" style="color: #555555;">Reach out any time. Your call or message could change a life.</p>
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
import sautiAboutpage from '@/assets/sauti-aboutpage.webp'
</script>
