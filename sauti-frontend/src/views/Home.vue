<template>
  <div>
    <!-- Hero Section with Enhanced Typography and Spacing -->
    <section class="relative overflow-hidden bg-gradient-to-br from-[#FFF8DC] via-white to-[#F5F5DC]">
      <div class="absolute inset-0 bg-gradient-to-b from-white/80 via-white/60 to-transparent"></div>
      <div class="container-custom relative py-16 md:py-24 lg:py-32">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center">
          <div class="lg:col-span-7 space-y-8">
            <!-- Enhanced Typography Hierarchy -->
            <div class="space-y-6">
              <h1 class="text-5xl md:text-6xl lg:text-7xl font-extrabold tracking-tight text-gray-900 leading-tight">
                Every child deserves a 
                <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#8B4000] to-[#A0522D]">
                  safe voice.
                </span>
              </h1>
              <p class="text-xl md:text-2xl text-gray-600 max-w-3xl leading-relaxed">
                Sauti 116 is free, confidential and available 24/7 across all telecoms. 
                Report abuse, seek guidance, or get urgent help in your language.
              </p>
            </div>
            
            <!-- Enhanced CTA Section with Better Spacing -->
            <div class="space-y-6">
              <!-- Primary Action Buttons -->
              <div class="flex flex-col sm:flex-row gap-4">
                <a href="tel:116" class="btn-emergency text-lg px-6 py-4 rounded-full font-bold shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-200 flex items-center gap-2" aria-label="Call 116 now">
                  <svg class="w-5 h-5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                  </svg>
                  <span>Call 116 Now</span>
                </a>
                <router-link to="/report" class="btn-primary text-lg px-6 py-4 rounded-full font-bold shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-200 flex items-center gap-2" aria-label="Report a case">
                  <svg class="w-5 h-5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <span>Report a Case</span>
                </router-link>
              </div>
              
              <!-- Secondary Actions -->
              <div class="flex flex-wrap gap-3">
                <a href="https://wa.me/256123456789" target="_blank" rel="noopener" class="pill pill-outline hover:bg-green-50 hover:border-green-300 hover:text-green-700 transition-all duration-200" aria-label="Contact via WhatsApp">
                  <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.525 3.488"/>
                  </svg>
                  WhatsApp
                </a>
                <a href="https://ureport.in" target="_blank" rel="noopener" class="pill pill-outline hover:bg-blue-50 hover:border-blue-300 hover:text-blue-700 transition-all duration-200" aria-label="U-Report 8500">
                  <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                  </svg>
                  U-Report 8500
                </a>
              </div>
              
              <!-- Trust Indicators -->
              <div class="flex flex-wrap gap-4 pt-4">
                <span class="badge-blue text-sm px-4 py-2 rounded-full font-semibold">24/7 Available</span>
                <span class="badge-orange text-sm px-4 py-2 rounded-full font-semibold">All Telecoms</span>
                <span class="badge-teal text-sm px-4 py-2 rounded-full font-semibold">EN • LG • SW</span>
                <span class="badge-purple text-sm px-4 py-2 rounded-full font-semibold">Confidential</span>
              </div>
            </div>
          </div>
          
          <!-- Enhanced Hero Image -->
          <div class="lg:col-span-5">
            <div class="relative">
              <div class="card p-0 overflow-hidden shadow-2xl">
                <img 
                  src="https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?q=80&w=1600&auto=format&fit=crop" 
                  alt="Children in Uganda receiving support and care" 
                  class="w-full h-80 md:h-96 lg:h-[500px] object-cover" 
                  loading="eager"
                />
                <div class="absolute inset-0 bg-gradient-to-t from-black/30 to-transparent"></div>
                <!-- Overlay content -->
                <div class="absolute bottom-6 left-6 right-6 text-white">
                  <h3 class="text-xl font-bold mb-2">Safe Spaces for Every Child</h3>
                  <p class="text-sm opacity-90">24/7 support across Uganda</p>
                </div>
              </div>
              <!-- Floating Stats Card -->
              <div class="absolute -bottom-6 -left-6 bg-white rounded-2xl shadow-xl p-6 border border-gray-100">
                <div class="text-center">
                  <div class="text-3xl font-bold text-[#8B4000]">1M+</div>
                  <div class="text-sm text-gray-600 font-medium">Children Helped</div>
                </div>
              </div>
              <!-- Trust Badge -->
              <div class="absolute -top-4 -right-4 bg-gradient-to-r from-[#8B4000] to-[#A0522D] text-white rounded-full px-4 py-2 text-sm font-semibold shadow-lg">
                Trusted by UNICEF
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    

    <!-- Enhanced Quick Access Section -->
    <section class="section-padding bg-gradient-to-b from-gray-50 to-white">
      <div class="container-custom">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">Get Help & Information</h2>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
            Access our comprehensive support services and resources designed to protect and empower children across Uganda.
          </p>
        </div>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
          <router-link to="/report" class="group">
            <div class="avm-card hover:shadow-xl hover:scale-105 transition-all duration-300 border-2 border-transparent hover:border-blue-200">
              <div class="avm-icon bg-blue-100 text-blue-600 group-hover:bg-blue-200 transition-colors duration-300">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <h3 class="avm-title group-hover:text-blue-600 transition-colors duration-300">Report a Case</h3>
              <p class="avm-text">Confidential, fast, and supportive reporting system.</p>
            </div>
          </router-link>
          
          <router-link to="/resources" class="group">
            <div class="avm-card hover:shadow-xl hover:scale-105 transition-all duration-300 border-2 border-transparent hover:border-green-200">
              <div class="avm-icon bg-green-100 text-green-600 group-hover:bg-green-200 transition-colors duration-300">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                </svg>
              </div>
              <h3 class="avm-title group-hover:text-green-600 transition-colors duration-300">Resources</h3>
              <p class="avm-text">Guides, policies, and educational toolkits.</p>
            </div>
          </router-link>
          
          <router-link to="/faqs" class="group">
            <div class="avm-card hover:shadow-xl hover:scale-105 transition-all duration-300 border-2 border-transparent hover:border-purple-200">
              <div class="avm-icon bg-purple-100 text-purple-600 group-hover:bg-purple-200 transition-colors duration-300">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <h3 class="avm-title group-hover:text-purple-600 transition-colors duration-300">FAQs</h3>
              <p class="avm-text">Answers to common questions and concerns.</p>
            </div>
          </router-link>
          
          <router-link to="/partners" class="group">
            <div class="avm-card hover:shadow-xl hover:scale-105 transition-all duration-300 border-2 border-transparent hover:border-orange-200">
              <div class="avm-icon bg-orange-100 text-orange-600 group-hover:bg-orange-200 transition-colors duration-300">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
              </div>
              <h3 class="avm-title group-hover:text-orange-600 transition-colors duration-300">Partners</h3>
              <p class="avm-text">MGLSD, UNICEF, UCRNN, ITU collaboration.</p>
            </div>
          </router-link>
        </div>
      </div>
    </section>

    <!-- Enhanced Journey Timeline -->
    <section class="section-padding bg-white">
      <div class="container-custom">
        <div class="text-center mb-20">
          <h2 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">Our Journey</h2>
          <p class="text-xl text-gray-600 max-w-4xl mx-auto leading-relaxed">
            Key milestones in our history of child advocacy, including international recommendations and national designation of 116.
          </p>
        </div>
        
        <div class="relative max-w-5xl mx-auto">
          <!-- Enhanced Timeline Line -->
          <div class="timeline-line bg-gradient-to-b from-blue-300 via-blue-400 to-orange-300"></div>
          
          <!-- Timeline Items with Enhanced Spacing -->
          <div class="space-y-20">
          <div class="timeline-item left">
              <div class="timeline-dot bg-blue-500 border-blue-200"></div>
              <div class="timeline-card hover:shadow-lg transition-all duration-300">
                <div class="flex items-center gap-3 mb-4">
                  <h4 class="text-lg text-blue-600 font-bold bg-blue-50 px-3 py-1 rounded-full">2005</h4>
                  <div class="h-px bg-gray-200 flex-1"></div>
                </div>
                <h3 class="text-2xl font-bold mb-3 text-gray-900">Launch of Child Helpline Initiative</h3>
                <p class="text-gray-600 leading-relaxed">Inception of the national child protection helpline in partnership with NGOs and international agencies.</p>
              </div>
            </div>
            
            <div class="timeline-item right">
              <div class="timeline-dot bg-green-500 border-green-200"></div>
              <div class="timeline-card hover:shadow-lg transition-all duration-300">
                <div class="flex items-center gap-3 mb-4">
                  <h4 class="text-lg text-green-600 font-bold bg-green-50 px-3 py-1 rounded-full">2010</h4>
                  <div class="h-px bg-gray-200 flex-1"></div>
                </div>
                <h3 class="text-2xl font-bold mb-3 text-gray-900">Launch of Sauti Helpline</h3>
                <p class="text-gray-600 leading-relaxed">Established as a national child helpline, providing a critical first point of contact.</p>
          </div>
            </div>
            
            <div class="timeline-item left">
              <div class="timeline-dot bg-purple-500 border-purple-200"></div>
              <div class="timeline-card hover:shadow-lg transition-all duration-300">
                <div class="flex items-center gap-3 mb-4">
                  <h4 class="text-lg text-purple-600 font-bold bg-purple-50 px-3 py-1 rounded-full">2015</h4>
                  <div class="h-px bg-gray-200 flex-1"></div>
                </div>
                <h3 class="text-2xl font-bold mb-3 text-gray-900">Expansion of Services</h3>
                <p class="text-gray-600 leading-relaxed">Introduced counseling and legal support to offer more comprehensive assistance.</p>
          </div>
            </div>
            
            <div class="timeline-item right">
              <div class="timeline-dot bg-orange-500 border-orange-200"></div>
              <div class="timeline-card hover:shadow-lg transition-all duration-300">
                <div class="flex items-center gap-3 mb-4">
                  <h4 class="text-lg text-orange-600 font-bold bg-orange-50 px-3 py-1 rounded-full">2016</h4>
                  <div class="h-px bg-gray-200 flex-1"></div>
                </div>
                <h3 class="text-2xl font-bold mb-3 text-gray-900">Legal & Regulatory Backing</h3>
                <p class="text-gray-600 leading-relaxed">116 designated by UCC; strengthened by national child protection policies and frameworks.</p>
          </div>
            </div>
            
            <div class="timeline-item left">
              <div class="timeline-dot bg-red-500 border-red-200"></div>
              <div class="timeline-card hover:shadow-lg transition-all duration-300">
                <div class="flex items-center gap-3 mb-4">
                  <h4 class="text-lg text-red-600 font-bold bg-red-50 px-3 py-1 rounded-full">2020</h4>
                  <div class="h-px bg-gray-200 flex-1"></div>
                </div>
                <h3 class="text-2xl font-bold mb-3 text-gray-900">Reaching 1 Million Children</h3>
                <p class="text-gray-600 leading-relaxed">A landmark achievement, having provided assistance to over a million children across Uganda.</p>
          </div>
            </div>
          </div>
        </div>
        
        <div class="text-center mt-16">
          <p class="text-gray-500 text-lg leading-relaxed max-w-4xl mx-auto">
            Aligned with ITU recommendation for 116 child helplines; operated under MGLSD in collaboration with NGOs and UN partners.
          </p>
        </div>
      </div>
    </section>

    <!-- Enhanced Featured Content Section -->
    <section class="section-padding bg-gradient-to-b from-white to-gray-50">
      <div class="container-custom">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">Recent Publications</h2>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed mb-8">
            Latest articles, videos and resources to help children, families, and communities stay safe and informed.
          </p>
          <router-link to="/blog" class="inline-flex items-center gap-2 text-blue-600 hover:text-blue-700 font-semibold text-lg transition-colors duration-200">
            View all posts
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </router-link>
        </div>
        
        <!-- Loading State -->
        <Loader v-if="loadingVideos" message="Loading recent publications..." />
        
        <!-- Empty State -->
        <div v-else-if="!loadingVideos && latestVideos.length === 0" class="text-center py-16">
          <svg class="w-24 h-24 mx-auto text-gray-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
          </svg>
          <h3 class="text-xl font-semibold text-gray-900 mb-2">No publications yet</h3>
          <p class="text-gray-600">Check back soon for new content from Sauti Uganda.</p>
        </div>
        
        <!-- Publications Grid -->
        <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <article v-for="video in latestVideos" :key="video.id" class="group cursor-pointer">
            <div class="relative bg-gray-200 rounded-2xl overflow-hidden aspect-video shadow-lg hover:shadow-2xl transition-all duration-300 group-hover:scale-105">
              <img 
                :src="video.thumbnail" 
                :alt="video.title" 
                class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-110" 
                loading="lazy" 
                @error="useThumbPlaceholder($event)" 
              />
              <!-- Gradient Overlay -->
              <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
              
              <!-- Play Button Overlay -->
              <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                <div class="bg-white/95 rounded-full p-6 shadow-2xl transform group-hover:scale-110 transition-transform duration-300">
                  <svg class="w-10 h-10 text-[#8B4000]" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M8 5v14l11-7z"/>
                  </svg>
                </div>
              </div>
              
              <!-- Duration Badge -->
              <span class="absolute bottom-3 right-3 text-sm font-bold bg-black/90 text-white px-3 py-1 rounded-full backdrop-blur-sm border border-white/20">
                {{ video.duration }}
              </span>
              
              <!-- Category Badge -->
              <span class="absolute top-3 left-3 text-xs font-semibold bg-gradient-to-r from-[#8B4000] to-[#A0522D] text-white px-3 py-1 rounded-full shadow-lg">
                {{ video.category }}
              </span>
              
              <!-- Featured/Recent Badge -->
              <span v-if="video.featured" class="absolute top-3 right-3 text-xs font-bold bg-red-500 text-white px-2 py-1 rounded-full animate-pulse">
                Featured
              </span>
            </div>
            
            <div class="mt-6 space-y-4">
              <div class="flex items-start gap-4">
                <img 
                  :src="video.channelAvatar" 
                  :alt="video.channel" 
                  class="h-12 w-12 rounded-full object-cover border-2 border-[#8B4000] border-opacity-20" 
                  loading="lazy" 
                  @error="useAvatarPlaceholder($event)" 
                />
                <div class="min-w-0 flex-1">
                  <h3 class="text-lg font-bold text-gray-900 leading-tight line-clamp-2 group-hover:text-[#8B4000] transition-colors duration-200">
                    {{ video.title }}
                  </h3>
                  <p class="text-sm text-[#8B4000] mt-1 font-medium">{{ video.channel }}</p>
                  <div class="flex items-center gap-2 mt-2 text-sm text-gray-500">
                    <span class="flex items-center gap-1">
                      <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                      </svg>
                      {{ video.views }}
                    </span>
                    <span>•</span>
                    <span>{{ video.published }}</span>
                  </div>
                  
                  <!-- Engagement Stats -->
                  <div class="flex items-center gap-4 mt-3 text-xs text-gray-500">
                    <span class="flex items-center gap-1">
                      <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                      </svg>
                      Liked
                    </span>
                    <span class="flex items-center gap-1">
                      <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                      </svg>
                      Educational
                    </span>
                  </div>
                </div>
              </div>
              
              <!-- Action Buttons -->
              <div class="flex items-center gap-2 pt-2">
                <button class="flex items-center gap-2 px-3 py-1.5 bg-gray-100 hover:bg-gray-200 rounded-full text-sm font-medium transition-colors duration-200">
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                  </svg>
                  Like
                </button>
                <button class="flex items-center gap-2 px-3 py-1.5 bg-gray-100 hover:bg-gray-200 rounded-full text-sm font-medium transition-colors duration-200">
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92 1.61 0 2.92-1.31 2.92-2.92s-1.31-2.92-2.92-2.92z"/>
                  </svg>
                  Share
                </button>
                <button class="flex items-center gap-2 px-3 py-1.5 bg-gray-100 hover:bg-gray-200 rounded-full text-sm font-medium transition-colors duration-200">
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                  Save
                </button>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- Enhanced Trust Partners Section -->
    <section class="py-16 bg-white border-y border-gray-100">
      <div class="container-custom">
        <div class="text-center mb-12">
          <h3 class="text-2xl font-bold text-gray-900 mb-4">Trusted by Leading Organizations</h3>
          <p class="text-gray-600">Working in partnership with government and international agencies</p>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
          <div class="card p-6 text-center hover:shadow-lg transition-all duration-300 group">
            <div class="text-2xl font-bold text-blue-600 mb-2 group-hover:scale-110 transition-transform duration-300">MGLSD</div>
            <p class="text-sm text-gray-600">Ministry of Gender, Labour & Social Development</p>
          </div>
          <div class="card p-6 text-center hover:shadow-lg transition-all duration-300 group">
            <div class="text-2xl font-bold text-blue-500 mb-2 group-hover:scale-110 transition-transform duration-300">UNICEF</div>
            <p class="text-sm text-gray-600">United Nations Children's Fund</p>
          </div>
          <div class="card p-6 text-center hover:shadow-lg transition-all duration-300 group">
            <div class="text-2xl font-bold text-green-600 mb-2 group-hover:scale-110 transition-transform duration-300">UCRNN</div>
            <p class="text-sm text-gray-600">Uganda Child Rights NGO Network</p>
          </div>
          <div class="card p-6 text-center hover:shadow-lg transition-all duration-300 group">
            <div class="text-2xl font-bold text-purple-600 mb-2 group-hover:scale-110 transition-transform duration-300">ITU 116</div>
            <p class="text-sm text-gray-600">International Telecommunication Union</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Enhanced Final CTA Section -->
    <section class="section-padding bg-gradient-to-br from-blue-50 via-white to-orange-50">
      <div class="container-custom text-center">
        <div class="max-w-4xl mx-auto">
          <h2 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">Need Help Right Now?</h2>
          <p class="text-xl text-gray-600 mb-12 leading-relaxed">
            Accessible 24/7 across all telecom networks. Support in multiple local languages. 
            All services are free and confidential.
          </p>
          
          <!-- Primary CTA Buttons -->
          <div class="flex flex-col sm:flex-row gap-6 justify-center mb-12">
            <a href="tel:116" class="btn-emergency text-xl px-10 py-5 rounded-2xl font-bold shadow-xl hover:shadow-2xl transform hover:scale-105 transition-all duration-300">
              <span class="flex items-center gap-4">
                <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                </svg>
                Call 116 Now
              </span>
            </a>
            <router-link to="/report" class="btn-primary text-xl px-10 py-5 rounded-2xl font-bold shadow-xl hover:shadow-2xl transform hover:scale-105 transition-all duration-300">
              <span class="flex items-center gap-4">
                <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                Report a Case
              </span>
            </router-link>
            <router-link to="/contact" class="btn-outline text-xl px-10 py-5 rounded-2xl font-bold shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300">
              <span class="flex items-center gap-4">
                <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
                Contact Us
              </span>
            </router-link>
          </div>
          
          <!-- Service Information Cards -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="avm-card hover:shadow-lg transition-all duration-300">
              <div class="flex items-center gap-3 mb-4">
                <div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center">
                  <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
                  </svg>
                </div>
                <h4 class="text-lg font-bold text-gray-900">Channels</h4>
              </div>
              <p class="text-gray-600 leading-relaxed">
                <strong>116</strong> • WhatsApp • U-Report SMS • SafePal App • Email
              </p>
            </div>
            
            <div class="avm-card hover:shadow-lg transition-all duration-300">
              <div class="flex items-center gap-3 mb-4">
                <div class="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center">
                  <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129" />
                  </svg>
                </div>
                <h4 class="text-lg font-bold text-gray-900">Languages</h4>
              </div>
              <p class="text-gray-600 leading-relaxed">
                <strong>English</strong> • Luganda • Swahili • Local languages
              </p>
            </div>
            
            <div class="avm-card hover:shadow-lg transition-all duration-300">
              <div class="flex items-center gap-3 mb-4">
                <div class="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center">
                  <svg class="w-6 h-6 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <h4 class="text-lg font-bold text-gray-900">Availability</h4>
              </div>
              <p class="text-gray-600 leading-relaxed">
                <strong>24/7</strong> • Nationwide • All telecoms
              </p>
            </div>
        </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { usePartnersStore } from '@/store/partners'
import { useBlogStore } from '@/store/blog'
import GetHelpButton from '@/components/common/GetHelpButton.vue'
import Loader from '@/components/common/Loader.vue'

const partnersStore = usePartnersStore()
const blogStore = useBlogStore()

// Video data from backend
const latestVideos = ref([])
const loadingVideos = ref(false)

const partners = ref([])
const loadingPartners = ref(false)
const usePng = ref(true)
const pngUrl = ref('')

onMounted(async () => {
  // Fetch partners
  loadingPartners.value = true
  try {
    await partnersStore.fetchPartners()
    partners.value = partnersStore.partners
  } catch (error) {
    console.error('Failed to load partners:', error)
  } finally {
    loadingPartners.value = false
  }
  
  // Load recent publications from backend
  loadingVideos.value = true
  try {
    // Fetch most recent published posts (limit to 3)
    await blogStore.fetchPosts({ 
      status: 'PUBLISHED',
      ordering: '-published_at,-created_at', // Most recent first
      limit: 3 
    })
    
    // Transform posts to video format for display
    // Mark all top 3 recent posts as featured
    latestVideos.value = blogStore.posts.map((post, index) => ({
      id: post.id,
      title: post.title,
      channel: post.author?.username || post.author_name || 'Sauti Uganda',
      channelAvatar: 'https://i.pravatar.cc/48?img=12',
      views: `${post.views_count || 0} views`,
      published: formatDate(post.published_at || post.created_at),
      duration: '5:30', // Default duration, could be added to post model
      category: post.category?.name || 'Education',
      thumbnail: post.featured_image || 'https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?q=80&w=1200&auto=format&fit=crop',
      featured: true, // All top 3 recent posts are featured
      isLatest: index === 0 // First one is the latest
    }))
  } catch (error) {
    console.error('Failed to load recent publications:', error)
    latestVideos.value = []
  } finally {
    loadingVideos.value = false
  }
  
  // Helper function to format dates
  function formatDate(dateString) {
    const date = new Date(dateString)
    const now = new Date()
    const diffTime = Math.abs(now - date)
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
    
    if (diffDays === 1) return '1 day ago'
    if (diffDays < 7) return `${diffDays} days ago`
    if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`
    return `${Math.floor(diffDays / 30)} months ago`
  }
  
  // Try multiple filename variants to match the asset you placed
  const candidates = [
    new URL('@/assets/uganda mapping.png', import.meta.url).href,
    new URL('@/assets/uganda mapping .png', import.meta.url).href,
    new URL('@/assets/uganda maping.png', import.meta.url).href,
    new URL('@/assets/uganda maping .png', import.meta.url).href,
  ]
  usePng.value = false
  for (const candidate of candidates) {
    try {
      const res = await fetch(candidate, { method: 'HEAD' })
      if (res.ok) {
        pngUrl.value = candidate
        usePng.value = true
        break
      }
    } catch (_) { /* ignore and try next */ }
  }
})

function setPlaceholder(event) {
  const img = event.target
  const ph = img.getAttribute('data-ph') || 'https://picsum.photos/800/600'
  if (img.src !== ph) {
    img.src = ph
  }
}

function useThumbPlaceholder(e) {
  e.target.src = 'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?q=80&w=640&auto=format&fit=crop'
}

function useAvatarPlaceholder(e) {
  e.target.src = 'https://i.pravatar.cc/48'
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.aspect-video {
  position: relative;
  width: 100%;
  padding-bottom: 56.25%; /* 16:9 */
}
.aspect-video > img,
.aspect-video > video,
.aspect-video > div {
  position: absolute;
  inset: 0;
}
</style>
