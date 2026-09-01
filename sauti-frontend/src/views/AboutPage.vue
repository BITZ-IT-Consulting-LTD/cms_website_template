<template>
  <div class="min-h-screen font-sans overflow-x-hidden">

    <!-- A. Hero Section -->
    <!-- A. Hero Section (Centralized Floating Grid) -->
    <!-- A. Hero Section (Grid Moodboard Layout) -->
    <section class="relative bg-[#F9FAFB] flex flex-col items-center justify-center overflow-hidden" style="min-height: auto; padding-top: clamp(5rem, 12vh, 9rem); padding-bottom: clamp(2rem, 6vh, 6rem); padding-left: clamp(1rem, 4vw, 2rem); padding-right: clamp(1rem, 4vw, 2rem);">
      <!-- Grid Container -->
      <!-- min-height moved out of the inline style (which would always beat a
           responsive class on the same property) and into responsive
           classes instead: the side photo columns are hidden below md:, so
           the mobile-only value is shrunk to fit just the center 2x2 grid +
           badge, rather than the taller value sized for all three columns. -->
      <div class="grid grid-cols-1 md:grid-cols-[1fr_4fr_1fr] gap-4 w-full max-w-7xl min-h-[clamp(300px,52vh,420px)] md:min-h-[clamp(400px,60vh,800px)]" style="aspect-ratio: auto;">
        
        <!-- Left Side Column -->
        <div class="hidden md:grid grid-rows-3 gap-4">
           <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
              <img :src="heroImage1" width="400" height="300" loading="eager" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Community" />
           </div>
           <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
              <img :src="heroImage2" width="400" height="300" loading="eager" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Helpline" />
           </div>
           <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
              <img :src="heroImage3" width="400" height="300" loading="eager" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Family" />
           </div>
        </div>

        <!-- Center Wrapper -->
        <div class="relative flex flex-col items-center justify-center">
            <!-- Center Grid (Background for Circle) -->
            <div class="grid grid-cols-2 grid-rows-2 gap-4 w-full h-full">
               <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
                 <img :src="heroImageTeam" width="400" height="400" loading="eager" decoding="async" fetchpriority="high" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Team" />
               </div>
               <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
                 <img :src="heroImage4" width="400" height="400" loading="eager" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Happy Students" />
               </div>
               <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
                 <img :src="heroImage5" width="400" height="400" loading="eager" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Action" />
               </div>
               <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
                 <img :src="heroImage6" width="400" height="400" loading="eager" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Protection" />
               </div>
            </div>

            <!-- The Circle (Overlay) -->
            <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
              <div class="bg-white rounded-full shadow-2xl flex flex-col items-center justify-center text-center z-10 border-[8px] border-[#F9FAFB]" :style="{ width: 'clamp(14rem, 56vw, 26rem)', height: 'clamp(14rem, 56vw, 26rem)', padding: 'clamp(1.5rem, 6vw, 3rem)' }">
                  <span class="inline-block px-3 py-1 bg-gray-100 rounded-full font-black tracking-widest text-[#005f99] mb-4" :style="{ fontSize: 'clamp(0.6875rem, 2.2vw, 0.75rem)' }">{{ siteContent.getContent('about_hero_badge', 'Who we are') }}</span>
                  <h1 class="font-black text-[#0f172a] leading-tight mb-2" :style="{ fontSize: 'clamp(2.25rem, 7.5vw, 3.5rem)' }">
                    {{ siteContent.getContent('about_hero_title', 'About\nSauti 116') }}
                  </h1>
                  <p class="font-bold text-gray-400" :style="{ fontSize: 'clamp(0.875rem, 2.4vw, 1rem)' }">{{ siteContent.getContent('about_hero_tagline', 'From Uganda, For Children.') }}</p>
              </div>
            </div>
        </div>

        <!-- Right Side Column -->
        <div class="hidden md:grid grid-rows-3 gap-4">
           <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
              <img :src="heroImage7" width="400" height="300" loading="eager" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Operations" />
           </div>
           <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
               <img :src="heroImage8" width="400" height="300" loading="eager" decoding="async" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Inclusive" />
           </div>
           <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
              <div class="w-full h-full bg-blue-50 flex items-center justify-center p-4">
                 <p class="text-center text-[#005f99] font-black text-sm">{{ siteContent.getContent('about_hero_right_column', 'Every Voice Matters') }}</p>
              </div>
           </div>
        </div>

      </div>
    </section>









    <!-- E. Timeline Section ("Our Journey") -->
    <section class="mb-8 md:mb-16 !pt-6 md:!pt-8 bg-primary/5">
       <div class="container-custom">
          <div class="text-center mb-8 md:mb-10">
             <h2 class="text-lg md:text-2xl lg:text-3xl font-black text-secondary mb-1 md:mb-2 break-words text-center">{{ siteContent.getContent('about_journey_title', 'Our Journey') }}</h2>
             <p class="text-xs md:text-sm lg:text-base text-black/60 font-bold break-words text-center mx-auto">{{ siteContent.getContent('about_journey_subtitle', 'Milestones that define our commitment.') }}</p>
          </div>
          <AppTimeline :timeline-events="timelineEvents" />
       </div>
    </section>

    <!-- Reach Across The Nation Statistics Section. Contained as a rounded
         card within the page (matching how every other section here reads
         as "a card in the page flow") rather than a full-bleed color block --
         that hard-edged rectangle was the actual source of the jarring
         white -> green -> white transition. -->
    <section class="mb-8 md:mb-16">
       <div class="container-custom">
          <div class="rounded-[2rem] md:rounded-[2.5rem] !pt-8 md:!pt-10 pb-8 md:pb-10 px-4 md:px-8 bg-gradient-to-br from-[#00693e] to-[#004d2e] relative overflow-hidden">
             <!-- Decorative background elements -->
             <div class="absolute top-0 left-0 w-96 h-96 bg-white/5 rounded-full blur-3xl -translate-x-1/2 -translate-y-1/2"></div>
             <div class="absolute bottom-0 right-0 w-96 h-96 bg-white/5 rounded-full blur-3xl translate-x-1/2 translate-y-1/2"></div>

             <div class="relative z-10">
                <!-- Section Header -->
                <div class="text-center mb-6 md:mb-8">
                   <div class="inline-flex items-center gap-2 px-3 md:px-4 py-1 md:py-1.5 bg-white/10 backdrop-blur-sm rounded-full mb-3 md:mb-4 border border-white/20">
                      <Globe class="w-3 h-3 md:w-4 md:h-4 text-white" />
                      <span class="text-white/90 font-bold text-[10px] md:text-xs tracking-widest uppercase">National Impact</span>
                   </div>
                   <h2 class="text-lg md:text-2xl lg:text-3xl font-black text-white mb-2 md:mb-3 break-words">
                      {{ siteContent.getContent('about_stats_title', 'Reach Across The Nation') }}
                   </h2>
                   <p class="text-white/80 text-xs md:text-sm lg:text-base font-medium max-w-2xl mx-auto break-words">
                      {{ siteContent.getContent('about_stats_subtitle', 'How we are helping people across Uganda every day.') }}
                   </p>
                </div>

               <!-- Statistics Grid: compact tiles -- the number is the point,
                    everything else stays out of its way. -->
               <div class="grid grid-cols-2 lg:grid-cols-6 gap-2.5 md:gap-3 max-w-5xl mx-auto">
                  <div
                    v-for="(stat, index) in impactStats"
                    :key="`${stat.value}-${stat.label}-${index}`"
                    class="stat-card group bg-white/[0.07] rounded-xl p-3 md:p-4 text-center hover:bg-white/[0.12] transition-colors duration-300 border border-white/10"
                  >
                     <component :is="getStatIcon(stat, index)" class="w-4 h-4 text-white/50 mx-auto mb-1.5" />
                     <div class="stat-number text-lg md:text-xl font-black text-white leading-none tracking-tight break-words">
                        {{ stat.value }}
                     </div>
                     <div class="text-white/65 font-bold leading-snug text-[10px] md:text-[11px] mt-1 break-words">
                        {{ stat.label }}
                     </div>
                  </div>
               </div>
             </div>
          </div>
       </div>
    </section>

    <!-- Path to Resolution Section -->
    <section class="mb-8 md:mb-16 !pt-6 md:!pt-8 bg-transparent overflow-hidden relative">
       <!-- Decorative Background Blob -->
       <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-blue-50/50 rounded-full blur-3xl -z-10 pointer-events-none"></div>

       <div class="container-custom relative z-10">
          <div class="text-center max-w-3xl mx-auto mb-6 md:mb-12">
             <h2 class="text-lg md:text-2xl lg:text-3xl font-black text-secondary mb-2 md:mb-3 break-words">{{ siteContent.getContent('about_resolution_title', 'Path to Resolution') }}</h2>
             <p class="text-xs md:text-sm lg:text-base text-gray-500 font-medium px-4 break-words">{{ siteContent.getContent('about_resolution_subtitle', 'How we ensure every case leads to safety.') }}</p>
          </div>

          <!-- Mobile Layout: Vertical Steps -->
          <div class="md:hidden flex flex-col gap-4 md:gap-6 px-4">
             <div v-for="(step, i) in resolutionSteps" :key="'m-step-'+i" class="flex flex-col items-center text-center bg-white p-5 md:p-8 lg:p-10 rounded-2xl md:rounded-3xl shadow-lg border border-gray-100 relative">
                <!-- Icon -->
                <div class="w-12 h-12 md:w-16 md:h-16 rounded-xl md:rounded-2xl flex items-center justify-center text-white mb-2 md:mb-3 shadow-md" :style="{ backgroundColor: step.color }">
                   <component :is="step.icon" class="w-6 h-6 md:w-8 md:h-8" />
                </div>
                <!-- Content -->
                <h3 class="text-sm md:text-base lg:text-lg font-black text-gray-800 mb-0.5 md:mb-1 break-words">{{ step.title }}</h3>
                <span v-if="step.subtitle" class="text-[10px] md:text-xs font-bold tracking-widest text-gray-400 mb-2 md:mb-3 break-words">{{ step.subtitle }}</span>
                <p class="text-xs md:text-sm text-gray-600 leading-relaxed break-words">{{ step.description }}</p>

                <!-- Arrow pointing down (except last item) -->
                <div v-if="i < resolutionSteps.length - 1" class="absolute -bottom-6 md:-bottom-10 left-1/2 -translate-x-1/2 text-gray-300">
                   <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 md:w-8 md:h-8 animate-bounce" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
                   </svg>
                </div>
             </div>

             <!-- Arrow from the last resolution step into the goal card. The
                  per-step arrows above only render between consecutive steps
                  (i < length - 1), so the connector into the goal itself was
                  missing on mobile -- desktop already has this via its
                  connector rendering after every card, including the last.
                  One-way only, pointing toward the goal -- no return arrow. -->
             <div v-if="resolutionSteps.length" class="flex justify-center text-gray-300 -mb-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 md:w-8 md:h-8 animate-bounce" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                   <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
                </svg>
             </div>

             <!-- Final Goal Card Mobile -->
             <div class="mt-2 md:mt-4 flex flex-col items-center text-center bg-green-50 p-5 md:p-8 rounded-2xl md:rounded-3xl border-2 border-green-100">
                 <strong class="text-base md:text-xl lg:text-2xl font-black text-[#00ac46] mb-1 md:mb-2 break-words">{{ siteContent.getContent('about_resolution_central_goal', 'Safe Child') }}</strong>
                 <p class="text-xs md:text-sm text-gray-600 break-words">{{ siteContent.getContent('about_resolution_mobile_goal_text', 'The ultimate goal of our journey.') }}</p>
             </div>
          </div>

          <!-- Desktop Layout: Horizontal process flow -->
          <div class="hidden md:flex items-stretch justify-center gap-2 lg:gap-3 max-w-6xl mx-auto">
             <template v-for="(step, i) in resolutionSteps" :key="'d-step-'+i">
                <div class="flex-1 min-w-0 bg-white rounded-3xl shadow-lg border border-gray-100 p-5 lg:p-7 flex flex-col items-center text-center hover:-translate-y-1 hover:shadow-xl transition-all duration-300"
                   :style="{ borderTop: '4px solid ' + step.color }">
                   <div class="w-14 h-14 rounded-2xl flex items-center justify-center text-white mb-4 shadow-md" :style="{ backgroundColor: step.color }">
                      <component :is="step.icon" class="w-7 h-7" />
                   </div>
                   <span class="text-[10px] font-black tracking-[0.2em] text-gray-400 mb-1">STEP {{ i + 1 }}</span>
                   <h3 class="text-base lg:text-lg font-black text-gray-800 mb-1 break-words" :style="{ color: step.color }">{{ step.title }}</h3>
                   <span v-if="step.subtitle" class="text-[10px] font-bold tracking-widest text-gray-400 mb-2 break-words">{{ step.subtitle }}</span>
                   <p class="text-xs text-gray-600 leading-relaxed break-words">{{ step.description }}</p>
                </div>
                <!-- Connector: a decorative "<>" between steps, but the final
                     connector into the goal stays a single one-way ">" --
                     it's the one arrow that actually means "leads to the
                     goal", so it shouldn't look the same as the purely
                     decorative in-between markers. -->
                <div class="flex items-center text-gray-300 shrink-0" aria-hidden="true">
                   <svg v-if="i === resolutionSteps.length - 1" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
                   </svg>
                   <svg v-else class="w-8 h-6" fill="none" viewBox="0 0 32 24" stroke="currentColor" stroke-width="2.5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M17 5l7 7-7 7" />
                   </svg>
                </div>
             </template>

             <!-- Final Goal Card -->
             <div class="flex-1 min-w-0 bg-green-50 rounded-3xl border-2 border-green-100 p-5 lg:p-7 flex flex-col items-center justify-center text-center">
                <div class="w-14 h-14 rounded-2xl bg-[#00ac46] flex items-center justify-center text-white mb-4 shadow-md">
                   <svg viewBox="0 0 64 64" width="30" fill="currentColor" aria-hidden="true">
                      <path d="M32 30a8 8 0 1 0-8-8 8 8 0 0 0 8 8zm16 4h-4.2a16 16 0 0 1-23.6 0H16a16 16 0 0 0-16 16v4h64v-4a16 16 0 0 0-16-16z"/>
                   </svg>
                </div>
                <strong class="text-lg font-black text-[#00ac46] mb-1 break-words">{{ siteContent.getContent('about_resolution_central_goal', 'Safe Child') }}</strong>
                <span class="text-[10px] font-black tracking-widest text-[#005f99]">{{ siteContent.getContent('about_resolution_central_text', 'Our Goal') }}</span>
             </div>
          </div>
       </div>
    </section>

    <!-- F. Meet Our Team Section -->
    <section class="mb-8 md:mb-16 !pt-6 md:!pt-8 bg-transparent relative z-10" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
      <div class="container-custom">
        <div class="text-center mb-6 md:mb-12">
          <h2 class="text-lg md:text-2xl lg:text-3xl font-black text-secondary mb-2 md:mb-3 break-words">{{ siteContent.getContent('about_team_title', 'Meet Our Team') }}</h2>
          <p class="text-xs md:text-sm lg:text-base text-secondary/70 font-bold max-w-2xl mx-auto break-words">{{ siteContent.getContent('about_team_subtitle', 'Dedicated professionals committed to the safety and well-being of every child.') }}</p>
        </div>

        <!-- Loading State -->
        <div v-if="teamLoading" class="text-center py-12">
          <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
          <p class="text-gray-500 mt-4 font-bold">Loading team members...</p>
        </div>

        <!-- Empty State -->
        <div v-else-if="teamMembers.length === 0" class="text-center py-12">
          <p class="text-gray-500 font-bold">No team members available at the moment.</p>
        </div>

        <!-- Team Members Grid -->
        <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 md:gap-6 max-w-7xl mx-auto">
          <div v-for="member in teamMembers" :key="member.id" class="group bg-white rounded-2xl p-5 md:p-6 lg:p-7 text-center shadow-sm hover:shadow-xl transition-all duration-300 border border-gray-100 flex flex-col">
            <div class="w-24 h-24 md:w-32 md:h-32 mx-auto rounded-full overflow-hidden mb-3 md:mb-4 border-4 border-primary/10 group-hover:border-primary transition-colors bg-gray-100 flex items-center justify-center flex-shrink-0">
              <img
                v-if="member.image_thumbnail_url || member.image_url || member.image"
                :src="member.image_thumbnail_url || member.image_url || member.image"
                :alt="member.name"
                width="128"
                height="128"
                class="w-full h-full object-cover"
                @error="handleImageError($event, member)"
                loading="lazy"
                decoding="async"
              />
              <User v-else class="w-12 h-12 md:w-16 md:h-16 text-gray-400" />
            </div>
            <h3 class="text-sm md:text-base lg:text-lg font-bold text-secondary mb-0.5 md:mb-1 break-words">{{ member.name }}</h3>
            <p class="text-primary font-bold text-[10px] md:text-xs tracking-widest mb-2 md:mb-3 break-words">{{ member.role }}</p>
            <!-- No hardcoded fallback: a generic canned bio here had no admin
                 field it came from, so it silently repeated on every member
                 with no bio set and nobody could edit or remove it. A member
                 with no bio filled in just doesn't show this line at all. -->
            <p v-if="member.bio" class="text-gray-600 text-xs md:text-sm leading-relaxed line-clamp-4 break-words">{{ member.bio }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- G. Core Values Section. Rebuilt to match the same "centered header
         above, full-width grid below" pattern every other section on this
         page uses -- this was the one section still using a sticky sidebar
         + narrow 2-column grid, which is why its cards read oversized: they
         were stretching to fill half of an already-narrow 2/3-width column
         instead of sizing to their own content. -->
    <section class="mb-8 md:mb-16 py-10 md:py-16 bg-gradient-to-br from-gray-50 via-white to-primary/5 relative overflow-hidden">
      <!-- Decorative elements -->
      <div class="absolute top-0 right-0 w-96 h-96 bg-primary/5 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
      <div class="absolute bottom-0 left-0 w-64 h-64 bg-secondary/5 rounded-full blur-3xl translate-y-1/2 -translate-x-1/2"></div>

      <div class="container-custom relative z-10">
        <!-- Section Header -->
        <div class="text-center mb-6 md:mb-10 px-4">
          <span class="inline-flex items-center gap-2 px-3 md:px-4 py-1 md:py-1.5 bg-primary/10 rounded-full text-[10px] md:text-xs font-bold tracking-widest mb-3 md:mb-4 border border-primary/20 text-primary">
            <Heart class="w-3 h-3" />
            {{ siteContent.getContent('about_values_badge', 'Our Principles') }}
          </span>
          <h2 class="text-lg md:text-2xl lg:text-3xl font-bold text-secondary tracking-tight break-words">
            {{ siteContent.getContent('about_values_title', 'Our Core Values') }}
          </h2>
          <div class="w-16 h-1 bg-primary mx-auto mt-2 md:mt-4 rounded-full"></div>
          <p class="text-xs md:text-sm lg:text-base text-black/60 font-semibold mt-2 md:mt-4 max-w-2xl mx-auto break-words">
            {{ siteContent.getContent('about_values_description', 'Our core values guide every interaction, decision, and intervention. They are the foundation of our trust with the community.') }}
          </p>

          <!-- Stats: inline pills under the description instead of a whole
               sidebar column for just two numbers. -->
          <div class="flex flex-wrap justify-center gap-3 md:gap-4 mt-4 md:mt-6">
            <div class="flex items-center gap-2.5 bg-white rounded-full pl-2 pr-4 py-2 border border-gray-100 shadow-sm">
              <div class="w-8 h-8 rounded-full bg-gradient-to-br from-primary to-primary/80 flex items-center justify-center font-black text-white text-[10px] shrink-0">
                {{ siteContent.getContent('about_values_stat_1_value', '1M+') }}
              </div>
              <span class="font-bold text-xs md:text-sm text-secondary">{{ siteContent.getContent('about_values_stat_1_label', 'Lives Impacted') }}</span>
            </div>
            <div class="flex items-center gap-2.5 bg-white rounded-full pl-2 pr-4 py-2 border border-gray-100 shadow-sm">
              <div class="w-8 h-8 rounded-full bg-gradient-to-br from-secondary to-secondary/80 flex items-center justify-center font-black text-white text-[10px] shrink-0">
                {{ siteContent.getContent('about_values_stat_2_value', '10+') }}
              </div>
              <span class="font-bold text-xs md:text-sm text-secondary">{{ siteContent.getContent('about_values_stat_2_label', 'Years of Service') }}</span>
            </div>
          </div>
        </div>

        <!-- Loading State -->
        <div v-if="coreValuesLoading" class="text-center py-12">
          <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
          <p class="text-gray-500 mt-4 font-bold">Loading core values...</p>
        </div>

        <!-- Core Values Grid: full page width, sizes to content instead of
             stretching to fill a narrow column. -->
        <div v-else class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3 md:gap-5 max-w-5xl mx-auto">
          <div
            v-for="(value, index) in coreValues"
            :key="value.id"
            class="core-value-card group bg-white p-4 md:p-5 rounded-2xl border border-gray-100 shadow-sm hover:shadow-xl hover:border-primary/20 transition-all duration-300 hover:-translate-y-1 relative overflow-hidden text-center"
            :style="{ animationDelay: `${index * 100}ms` }"
          >
            <!-- Subtle gradient overlay on hover -->
            <div class="absolute inset-0 bg-gradient-to-br from-primary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>

            <!-- Content -->
            <div class="relative z-10">
              <!-- Icon -->
              <div
                class="w-10 h-10 md:w-11 md:h-11 rounded-xl flex items-center justify-center mb-2.5 mx-auto group-hover:scale-110 transition-transform duration-300 shadow-sm"
                :class="[getColorClasses(coreValueColorKey(value)).bg, getColorClasses(coreValueColorKey(value)).text]"
              >
                <component :is="getIconComponent(value.icon || 'ShieldCheck')" class="w-5 h-5" />
              </div>

              <!-- Title -->
              <h3 class="text-sm md:text-base font-bold mb-1.5 text-secondary group-hover:text-primary transition-colors duration-300 break-words">
                {{ value.title }}
              </h3>

              <!-- Description -->
              <p class="text-xs md:text-sm text-gray-500 leading-relaxed break-words">
                {{ value.description }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>






  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useSettingsStore } from '@/store/settings'
import { useSiteContent } from '@/composables/useSiteContent'

// Fallback images for About hero grid
import imgChildrenUganda from '@/assets/children-uganda-1.jpeg'
import imgHelplineCenter from '@/assets/helpline-center.png'
import imgHeroFamily from '@/assets/hero-family.png'
import imgSautiAboutpage from '@/assets/sauti-aboutpage.webp'
import imgHappyStudents from '@/assets/sauti_happy_students.png'
import imgHelplineAction from '@/assets/helpline-action.png'
import imgCommunityProtection from '@/assets/community-protection.png'
import imgDiverseOperations from '@/assets/diverse_helpline_operations.png'
import imgInclusiveProtection from '@/assets/inclusive_community_protection.png'

import { api } from '@/utils/axios'
import BaseCTA from '@/components/common/BaseCTA.vue'
import AppTimeline from '@/components/AppTimeline.vue'

import {
  ShieldCheck,
  Phone,
  Clock,
  Globe,
  Heart,
  Users,
  AlertTriangle,
  History,
  Check,
  Shield,
  Zap,
  RotateCcw,
  User,
  Calendar,
  TrendingUp,
  MapPin,
  PhoneCall,
  Target
} from 'lucide-vue-next'

// --- Stores ---
const settingsStore = useSettingsStore()
const siteContent = useSiteContent('about')

// --- Data ---
const settings = computed(() => settingsStore.settings)

// Who We Are Images from dedicated API
const whoWeAreImages = ref([])

// Hero grid images with CMS override capability (using dedicated API)
// Each computed directly accesses whoWeAreImages.value to ensure reactivity
const heroImage1 = computed(() => {
  const img = whoWeAreImages.value.find(i => i.position === 1)
  return img?.image_url || imgChildrenUganda
})
const heroImage2 = computed(() => {
  const img = whoWeAreImages.value.find(i => i.position === 2)
  return img?.image_url || imgHelplineCenter
})
const heroImage3 = computed(() => {
  const img = whoWeAreImages.value.find(i => i.position === 3)
  return img?.image_url || imgHeroFamily
})
const heroImageTeam = computed(() => {
  const img = whoWeAreImages.value.find(i => i.position === 4)
  return img?.image_url || settings.value.org_team_photo || imgSautiAboutpage
})
const heroImage4 = computed(() => {
  const img = whoWeAreImages.value.find(i => i.position === 5)
  return img?.image_url || imgHappyStudents
})
const heroImage5 = computed(() => {
  const img = whoWeAreImages.value.find(i => i.position === 6)
  return img?.image_url || imgHelplineAction
})
const heroImage6 = computed(() => {
  const img = whoWeAreImages.value.find(i => i.position === 7)
  return img?.image_url || imgCommunityProtection
})
const heroImage7 = computed(() => {
  const img = whoWeAreImages.value.find(i => i.position === 8)
  return img?.image_url || imgDiverseOperations
})
const heroImage8 = computed(() => {
  const img = whoWeAreImages.value.find(i => i.position === 9)
  return img?.image_url || imgInclusiveProtection
})

const teamMembers = ref([])
const teamLoading = ref(false)
const coreValues = ref([])
const coreValuesLoading = ref(false)

const defaultImpactStats = [
  { value: 'Nov 2013', label: 'Established' },
  { value: '2.7M+', label: 'Calls Received Countrywide Since Nov 2021' },
  { value: '40,000', label: 'Cases Handled Since Nov 2021' },
  { value: '120/143', label: 'District Action Centres Established in Uganda' },
  { value: '1500-2000', label: 'Calls Received Daily on Average' },
  { value: '50+', label: 'New Cases Handled Daily on Average' },
]

const impactStats = computed(() => {
  const contentMap = siteContent.allContent.value || {}
  const statsByIndex = {}
  // `icon` is optional: an admin adding a new stat via ContentManager can set
  // about_stats_stat_<n>_icon to any name from STAT_ICON_MAP below to pick
  // its icon; if they don't, it falls back to the positional default so
  // existing stats look exactly as before this field existed.
  const regex = /^about_stats_stat_(\d+)_(value|label|icon)$/

  Object.entries(contentMap).forEach(([key, item]) => {
    const match = key.match(regex)
    if (!match) return
    const index = parseInt(match[1], 10)
    const field = match[2]
    if (!statsByIndex[index]) {
      statsByIndex[index] = { index, value: '', label: '', icon: '' }
    }
    statsByIndex[index][field] = item?.value ?? ''
  })

  const indices = Object.keys(statsByIndex)
    .map(Number)
    .filter(Number.isFinite)
    .sort((a, b) => a - b)

  if (indices.length === 0) {
    return defaultImpactStats
  }

  return indices
    .map((index) => {
      const fallback = defaultImpactStats[index - 1] || { value: '', label: '' }
      const stat = statsByIndex[index]
      return {
        value: stat.value || fallback.value,
        label: stat.label || fallback.label,
        icon: stat.icon || '',
      }
    })
    .filter(stat => stat.value || stat.label)
})


// --- Stats Icon Mapping ---
// Positional defaults, kept only as the fallback for stats that don't set
// their own `icon` (existing content predates that field, and it's still
// optional per-stat). A stat with an explicit icon name always wins.
const DEFAULT_STAT_ICONS = [Calendar, TrendingUp, Target, MapPin, PhoneCall, Users]

const getStatIcon = (stat, index) => {
  if (stat?.icon) return getIconComponent(stat.icon)
  return DEFAULT_STAT_ICONS[index % DEFAULT_STAT_ICONS.length]
}

// --- Mock Data for Layout ---








// --- Infographic Logic ---
import { markRaw } from 'vue'

const activeStep = ref(null)
const timelineEvents = ref([])

const defaultResolutionSteps = [
  {
    title: 'Caller',
    subtitle: 'Case reported',
    description: 'A concerned community member, child, or parent calls the 116 helpline to report a case of abuse or concern.',
    color: '#005f99',
    icon: markRaw(Phone)
  },
  {
    title: 'Call Center',
    subtitle: 'Assessment',
    description: 'Our professional counselors receive the call, provide immediate counseling, and assess the severity of the case.',
    color: '#00ac46',
    icon: markRaw(Clock)
  },
  {
    title: 'Case Mgmt.',
    subtitle: 'Coordination',
    description: 'The Case Management team coordinates with local authorities ensuring the child receives medical, legal, and psychosocial support.',
    color: '#7c3aed',
    icon: markRaw(ShieldCheck)
  },
  {
    title: 'Probation',
    subtitle: 'Support',
    description: 'Probation works with police and partners to ensure long-term safety, justice, and family reintegration where possible.',
    color: '#ea580c',
    icon: markRaw(Users)
  }
]

const resolutionSteps = ref(defaultResolutionSteps)

const centerX = 300
const centerY = 300
const radius = 210
const circleSize = 140

const getCoords = (index) => {
  // Distribute items evenly around the circle, starting from top (-90 degrees)
  const total = resolutionSteps.value.length || 1
  const angle = (index * (360 / total) - 90) * (Math.PI / 180)
  return {
    x: centerX + radius * Math.cos(angle),
    y: centerY + radius * Math.sin(angle),
    angle: angle
  }
}

const getCircleStyle = (i, color) => {
  const { x, y } = getCoords(i)
  return {
    left: `${x}px`,
    top: `${y}px`,
    borderColor: color,
  }
}

const getArrowPath = (i, radiusOffset = 0) => {
  const total = resolutionSteps.value.length || 1
  const startAngle = getCoords(i).angle
  const stepRad = (Math.PI / 180) * (360 / total)

  // Clearance to ensure arrow starts/ends outside the step circles
  // Circle radius is 70px. Track radius 210px.
  // Angle of circle edge = asin(70/210) ~= 0.34 rads.
  // We use 0.55 rads to give space (shortening the lines).
  const clearance = 0.55

  const actualStartAngle = startAngle + clearance
  const actualEndAngle = startAngle + stepRad - clearance

  // Adjust radius for bidirectional arrows (offset creates inner/outer arcs)
  const adjustedRadius = radius + radiusOffset

  const x1 = centerX + adjustedRadius * Math.cos(actualStartAngle)
  const y1 = centerY + adjustedRadius * Math.sin(actualStartAngle)

  const x2 = centerX + adjustedRadius * Math.cos(actualEndAngle)
  const y2 = centerY + adjustedRadius * Math.sin(actualEndAngle)

  // SVG Arc command: A rx ry x-axis-rotation large-arc-flag sweep-flag x y
  return `M ${x1} ${y1} A ${adjustedRadius} ${adjustedRadius} 0 0 1 ${x2} ${y2}`
}


// --- Fetch Who We Are Images ---
const fetchWhoWeAreImages = async () => {
  try {
    const response = await api.get('/content/who-we-are-images/')
    whoWeAreImages.value = Array.isArray(response.data)
      ? response.data
      : (response.data.results || [])
    console.log('Who We Are images fetched:', whoWeAreImages.value.length)
  } catch (error) {
    console.error('Failed to fetch Who We Are images:', error)
    whoWeAreImages.value = []
  }
}

// --- Fetch Team Members ---
const fetchTeamMembers = async () => {
  teamLoading.value = true
  try {
    const response = await api.teamMembers.list({ is_active: true })
    teamMembers.value = Array.isArray(response.data)
      ? response.data
      : (response.data.results || [])

    // Sort by order field
    teamMembers.value.sort((a, b) => (a.order || 0) - (b.order || 0))

    // Log for debugging
    console.log('Team members fetched:', teamMembers.value.length)
    if (teamMembers.value.length > 0) {
      console.log('Sample member:', teamMembers.value[0])
    }
  } catch (error) {
    console.error('Failed to fetch team members:', error)
    teamMembers.value = []
  } finally {
    teamLoading.value = false
  }
}

// Handle image loading errors
const handleImageError = (event, member) => {
  console.error(`Failed to load image for ${member.name}:`, member.image)
  // Hide the broken image
  event.target.style.display = 'none'
  // Show User icon fallback instead
  const parent = event.target.parentElement
  if (parent) {
    parent.innerHTML = '<svg class="w-16 h-16 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>'
  }
}

// --- Fetch Core Values ---
const defaultCoreValues = [
  {
    id: 1,
    title: 'Integrity',
    description: 'Acting with honesty, transparency and accountability in all we do.',
    icon: 'ShieldCheck',
    color: 'orange'
  },
  {
    id: 2,
    title: 'Compassion',
    description: 'Serving every child and survivor with deep empathy, kindness, and care.',
    icon: 'Heart',
    color: 'blue'
  },
  {
    id: 3,
    title: 'Collaboration',
    description: 'Working together with partners and communities for holistic protection.',
    icon: 'Users',
    color: 'green'
  },
  {
    id: 4,
    title: 'Excellence',
    description: 'Striving for the highest standards of quality in our service delivery.',
    icon: 'Check',
    color: 'purple'
  }
]

const fetchCoreValues = async () => {
  coreValuesLoading.value = true
  try {
    const response = await api.coreValues.list({ is_active: true })
    const data = Array.isArray(response.data)
      ? response.data
      : (response.data.results || [])

    // Use fallback if API returns empty array
    coreValues.value = data.length > 0 ? data : defaultCoreValues

    // Sort by order field
    coreValues.value.sort((a, b) => (a.order || 0) - (b.order || 0))

    console.log('Core values loaded:', coreValues.value.length)
  } catch (error) {
    console.error('Failed to fetch core values:', error)
    // Fallback to hardcoded values if API fails
    coreValues.value = defaultCoreValues
  } finally {
    coreValuesLoading.value = false
  }
}

// Helper to get icon component by name
const getIconComponent = (iconName) => {
  const iconMap = {
    ShieldCheck,
    Heart,
    Users,
    Check,
    Shield,
    Globe,
    Zap,
    Phone,
    Clock,
    Calendar,
    TrendingUp,
    Target,
    MapPin,
    PhoneCall,
  }
  return iconMap[iconName] || ShieldCheck
}

// --- Fetch Protection Approach (Path to Resolution steps) ---
const fetchProtectionApproaches = async () => {
  try {
    const response = await api.get('/content/protection-approach/')
    const data = Array.isArray(response.data)
      ? response.data
      : (response.data.results || [])

    if (data.length > 0) {
      data.sort((a, b) => (a.order || 0) - (b.order || 0))
      resolutionSteps.value = data.map(item => ({
        title: item.title,
        subtitle: '',
        description: item.description,
        color: item.color,
        icon: markRaw(getIconComponent(item.icon))
      }))
    } else {
      resolutionSteps.value = defaultResolutionSteps
    }
  } catch (error) {
    console.error('Failed to fetch protection approach steps:', error)
    resolutionSteps.value = defaultResolutionSteps
  }
}

// Real API core values store their color as a Tailwind shade token
// (e.g. "purple-500" on color_from); mock fallback data uses a bare
// color name (e.g. "purple"). Normalize to the bare name either way.
const coreValueColorKey = (value) => {
  const raw = value.color_from || value.color || 'blue'
  return raw.split('-')[0]
}

// Helper to get color classes by color name
const getColorClasses = (color) => {
  const colorMap = {
    orange: { bg: 'bg-orange-100', text: 'text-orange-600' },
    blue: { bg: 'bg-blue-100', text: 'text-blue-600' },
    green: { bg: 'bg-green-100', text: 'text-green-600' },
    purple: { bg: 'bg-purple-100', text: 'text-purple-600' },
    gray: { bg: 'bg-gray-100', text: 'text-gray-600' },
    red: { bg: 'bg-red-100', text: 'text-red-600' }
  }
  return colorMap[color] || colorMap.blue
}

// --- Fetching ---
onMounted(async () => {
  // Fire ALL fetches in parallel instead of sequential waterfall
  const results = await Promise.allSettled([
    siteContent.fetchContent(),
    settingsStore.fetchGlobalSettings(),
    fetchTeamMembers(),
    fetchCoreValues(),
    fetchProtectionApproaches(),
    fetchWhoWeAreImages(),
    api.get('/content/timeline-events/').then(res => res.data.results || res.data || [])
  ])
  const timelineResult = results[6]

  // Handle timeline data with fallback
  if (timelineResult.status === 'fulfilled' && timelineResult.value?.length) {
    timelineEvents.value = timelineResult.value
  } else {
    timelineEvents.value = [
      { id: 1, year: 2014, title: 'Inception', description: 'Sauti 116 was established as a toll-free helpline to bridge the gap between children in need and child protection services in Uganda.' },
      { id: 2, year: 2016, title: 'National Expansion', description: 'Partnered with the government to expand coverage nationwide, ensuring children from all districts could access safety.' },
      { id: 3, year: 2018, title: 'Digital Integration', description: 'Launched the integrated Case Management System to track cases in real-time and improve response coordination.' },
      { id: 4, year: 2021, title: 'Community Outreach', description: 'Initiated community-based child protection committees to strengthen safety networks at the village level.' },
      { id: 5, year: 2024, title: 'A Decade of Impact', description: 'Celebrating 10 years of service, having supported over 1 million children through counseling and rescue missions.' }
    ]
  }
})

</script>

<style scoped>
/* Core Value Cards Animation */
.core-value-card {
  animation: fadeInUp 0.5s ease-out forwards;
  opacity: 0;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Stat Items Animation */
.stat-item {
  animation: fadeIn 0.6s ease-out forwards;
  opacity: 0;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
</style>