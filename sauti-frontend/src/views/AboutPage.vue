<template>
  <div class="min-h-screen font-sans">
    
    <!-- A. Hero Section -->
    <!-- A. Hero Section (Centralized Floating Grid) -->
    <!-- A. Hero Section (Grid Moodboard Layout) -->
    <section class="relative bg-[#F9FAFB] min-h-screen flex flex-col items-center justify-center pt-32 pb-16 px-4 md:pt-48 md:px-8 overflow-hidden">
      <!-- Grid Container -->
      <div class="grid grid-cols-1 md:grid-cols-[1fr_4fr_1fr] gap-4 w-full max-w-7xl aspect-auto md:aspect-[16/10]">
        
        <!-- Left Side Column -->
        <div class="hidden md:grid grid-rows-3 gap-4">
           <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
              <img src="@/assets/children-uganda-1.jpeg" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Community" />
           </div>
           <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
              <img src="@/assets/helpline-center.png" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Helpline" />
           </div>
           <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
              <img src="@/assets/hero-family.png" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Family" />
           </div>
        </div>

        <!-- Center Wrapper -->
        <div class="relative flex flex-col items-center justify-center">
            <!-- Center Grid (Background for Circle) -->
            <div class="grid grid-cols-2 grid-rows-2 gap-4 w-full h-full">
               <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
                 <img src="@/assets/sauti-aboutpage.webp" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Team" />
               </div>
               <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
                 <img src="@/assets/sauti_happy_students.png" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Happy Students" />
               </div>
               <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
                 <img src="@/assets/helpline-action.png" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Action" />
               </div>
               <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
                 <img src="@/assets/community-protection.png" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Protection" />
               </div>
            </div>

            <!-- The Circle (Overlay) -->
            <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
              <div class="w-64 h-64 md:w-80 md:h-80 bg-white rounded-full shadow-2xl flex flex-col items-center justify-center text-center p-8 z-10 border-[8px] border-[#F9FAFB]">
                  <span class="inline-block px-3 py-1 bg-gray-100 rounded-full text-[10px] font-black uppercase tracking-widest text-[#005f99] mb-4">Who we are</span>
                  <h1 class="text-3xl md:text-4xl font-black text-[#0f172a] leading-tight mb-2">
                    About<br/><span class="text-[#005f99]">Sauti 116</span>
                  </h1>
                  <p class="text-sm font-bold text-gray-400">From Uganda, For Children.</p>
              </div>
            </div>
        </div>

        <!-- Right Side Column -->
        <div class="hidden md:grid grid-rows-3 gap-4">
           <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
              <img src="@/assets/diverse_helpline_operations.png" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Operations" />
           </div>
           <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
               <img src="@/assets/inclusive_community_protection.png" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="Inclusive" />
           </div>
           <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden relative group">
              <div class="w-full h-full bg-blue-50 flex items-center justify-center p-4">
                 <p class="text-center text-[#005f99] font-black text-sm">Every Child Matters</p>
              </div>
           </div>
        </div>

      </div>
    </section>









    <!-- E. Timeline Section ("Our Journey") -->
    <section class="py-24 bg-primary/5">
       <div class="container-custom">
          <div class="text-center mb-16">
             <h2 class="text-4xl font-black text-secondary mb-4">Our Journey</h2>
             <p class="text-black/60 font-bold">Milestones that define our commitment.</p>
          </div>
          <AppTimeline :timeline-events="timelineEvents" />
       </div>
    </section>

    <!-- Reach Across The Nation Statistics Section -->
    <section class="py-20 md:py-28 bg-[#006633] relative overflow-hidden">
       <!-- Ripped Paper Effect - Top -->
       <div class="absolute top-0 left-0 w-full overflow-hidden leading-[0]" style="transform: translateY(-1px);">
          <svg class="relative block w-full h-[60px]" viewBox="0 0 1200 120" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
             <path d="M0,0 L50,15 L100,5 L150,20 L200,8 L250,18 L300,12 L350,22 L400,10 L450,25 L500,15 L550,8 L600,20 L650,12 L700,18 L750,25 L800,10 L850,20 L900,15 L950,8 L1000,22 L1050,12 L1100,18 L1150,25 L1200,15 L1200,120 L0,120 Z" 
                   fill="currentColor" 
                   class="text-[#006633]">
             </path>
          </svg>
       </div>

       <!-- Decorative background elements -->
       <div class="absolute top-0 left-0 w-96 h-96 bg-white/5 rounded-full blur-3xl -translate-x-1/2 -translate-y-1/2"></div>
       <div class="absolute bottom-0 right-0 w-96 h-96 bg-white/5 rounded-full blur-3xl translate-x-1/2 translate-y-1/2"></div>
       
       <div class="container-custom relative z-10">
          <!-- Section Header -->
          <div class="text-center mb-16">
             <h2 class="text-4xl md:text-5xl font-black text-white mb-4 md:mb-6" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
                REACH ACROSS THE NATION
             </h2>
             <p class="text-white/90 text-lg md:text-xl font-medium max-w-2xl mx-auto" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
                How we are helping people across Uganda every day.
             </p>
          </div>

          <!-- Statistics Grid -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 md:gap-8">
             <!-- Stat Card 1: Children Supported -->
             <div class="bg-white/10 backdrop-blur-sm rounded-3xl p-8 text-center hover:bg-white/15 transition-all duration-300 border border-white/20">
                <div class="stat-number text-5xl md:text-6xl font-black text-white mb-3" style="font-family: 'Roboto', sans-serif;">
                   12,000+
                </div>
                <div class="text-white/80 text-sm md:text-base font-bold uppercase tracking-widest" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif; letter-spacing: 0.15em;">
                   Children Supported
                </div>
             </div>

             <!-- Stat Card 2: Districts Covered -->
             <div class="bg-white/10 backdrop-blur-sm rounded-3xl p-8 text-center hover:bg-white/15 transition-all duration-300 border border-white/20">
                <div class="stat-number text-5xl md:text-6xl font-black text-white mb-3" style="font-family: 'Roboto', sans-serif;">
                   135
                </div>
                <div class="text-white/80 text-sm md:text-base font-bold uppercase tracking-widest" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif; letter-spacing: 0.15em;">
                   Districts Covered
                </div>
             </div>

             <!-- Stat Card 3: Calls Answered -->
             <div class="bg-white/10 backdrop-blur-sm rounded-3xl p-8 text-center hover:bg-white/15 transition-all duration-300 border border-white/20">
                <div class="stat-number text-5xl md:text-6xl font-black text-white mb-3" style="font-family: 'Roboto', sans-serif;">
                   500K+
                </div>
                <div class="text-white/80 text-sm md:text-base font-bold uppercase tracking-widest" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif; letter-spacing: 0.15em;">
                   Calls Answered
                </div>
             </div>

             <!-- Stat Card 4: Partners -->
             <div class="bg-white/10 backdrop-blur-sm rounded-3xl p-8 text-center hover:bg-white/15 transition-all duration-300 border border-white/20">
                <div class="stat-number text-5xl md:text-6xl font-black text-white mb-3" style="font-family: 'Roboto', sans-serif;">
                   50+
                </div>
                <div class="text-white/80 text-sm md:text-base font-bold uppercase tracking-widest" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif; letter-spacing: 0.15em;">
                   Partners
                </div>
             </div>
          </div>
       </div>

       <!-- Ripped Paper Effect - Bottom -->
       <div class="absolute bottom-0 left-0 w-full overflow-hidden leading-[0]" style="transform: translateY(1px);">
          <svg class="relative block w-full h-[60px]" viewBox="0 0 1200 120" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
             <path d="M0,0 L50,12 L100,20 L150,8 L200,18 L250,10 L300,22 L350,15 L400,25 L450,12 L500,20 L550,15 L600,8 L650,25 L700,18 L750,10 L800,20 L850,12 L900,22 L950,15 L1000,8 L1050,20 L1100,12 L1150,18 L1200,10 L1200,0 L0,0 Z" 
                   fill="currentColor" 
                   class="text-[#006633]">
             </path>
          </svg>
       </div>
    </section>

    <!-- Path to Resolution Section -->
    <section class="py-16 md:py-24 bg-transparent overflow-hidden relative">
       <!-- Decorative Background Blob -->
       <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-blue-50/50 rounded-full blur-3xl -z-10 pointer-events-none"></div>

       <div class="container-custom relative z-10">
          <div class="text-center max-w-3xl mx-auto mb-12 md:mb-20">
             <h2 class="text-4xl md:text-5xl font-black text-secondary mb-4 md:mb-6">Path to Resolution</h2>
             <p class="text-lg md:text-xl text-gray-500 font-medium px-4">How we ensure every case leads to safety.</p>
          </div>

          <!-- Mobile Layout: Vertical Steps -->
          <div class="md:hidden flex flex-col gap-8 px-4">
             <div v-for="(step, i) in resolutionSteps" :key="'m-step-'+i" class="flex flex-col items-center text-center bg-white p-8 rounded-3xl shadow-lg border border-gray-100 relative">
                <!-- Icon -->
                <div class="w-16 h-16 rounded-2xl flex items-center justify-center text-white text-2xl mb-4 shadow-md" :style="{ backgroundColor: step.color }">
                   <component :is="step.icon" class="w-8 h-8" />
                </div>
                <!-- Content -->
                <h3 class="text-xl font-black text-gray-800 mb-1">{{ step.title }}</h3>
                <span class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-4">{{ step.subtitle }}</span>
                <p class="text-gray-600 leading-relaxed">{{ step.description }}</p>
                
                <!-- Arrow pointing down (except last item) -->
                <div v-if="i < resolutionSteps.length - 1" class="absolute -bottom-10 left-1/2 -translate-x-1/2 text-gray-300">
                   <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8 animate-bounce" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
                   </svg>
                </div>
             </div>
             
             <!-- Final Goal Card Mobile -->
             <div class="mt-4 flex flex-col items-center text-center bg-green-50 p-8 rounded-3xl border-2 border-green-100">
                 <strong class="text-2xl font-black text-[#00ac46] mb-2">Safe Child</strong>
                 <p class="text-gray-600">The ultimate goal of our journey.</p>
             </div>
          </div>

          <!-- Desktop Layout: Circular Infographic -->
          <div class="hidden md:flex justify-center items-center h-[700px] bg-transparent rounded-[3rem] shadow-none border-none">
             <div class="relative w-[600px] h-[600px]">
                
                <!-- Central Node -->
                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-center z-10 text-gray-500 flex flex-col items-center justify-center p-8 bg-white rounded-full shadow-[0_10px_40px_rgba(0,0,0,0.08)] border border-gray-100 w-48 h-48 transition-all duration-300">
                   <transition name="fade" mode="out-in">
                      <div v-if="activeStep !== null" :key="activeStep" class="text-sm leading-tight px-2">
                         <strong class="text-lg block mb-2" :style="{ color: resolutionSteps[activeStep].color }">
                            {{ resolutionSteps[activeStep].title }}
                         </strong>
                         <p class="text-xs text-slate-600 font-medium leading-relaxed">
                            {{ resolutionSteps[activeStep].description }}
                         </p>
                      </div>
                      <div v-else key="default" class="text-sm leading-tight">
                         <div class="mb-2 text-[#005f99] flex justify-center">
                            <svg viewBox="0 0 64 64" width="50" fill="currentColor">
                               <path d="M32 30a8 8 0 1 0-8-8 8 8 0 0 0 8 8zm16 4h-4.2a16 16 0 0 1-23.6 0H16a16 16 0 0 0-16 16v4h64v-4a16 16 0 0 0-16-16z"/>
                            </svg>
                         </div>
                         <strong class="text-lg block text-slate-800 mb-1">Safe Child</strong>
                         <span class="text-xs uppercase tracking-widest text-[#005f99]">Our Goal</span>
                      </div>
                   </transition>
                </div>

                <!-- Arrows Layer -->
                <svg class="absolute top-0 left-0 w-full h-full z-0 pointer-events-none" viewBox="0 0 600 600">
                   <defs>
                      <!-- Forward arrowhead -->
                      <marker id="arrowhead-forward" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                         <polygon points="0 0, 10 3.5, 0 7" fill="#cbd5e1" />
                      </marker>
                      <!-- Reverse arrowhead - same color as forward for consistency -->
                      <marker id="arrowhead-reverse" markerWidth="10" markerHeight="7" refX="1" refY="3.5" orient="auto">
                         <polygon points="10 0, 0 3.5, 10 7" fill="#cbd5e1" />
                      </marker>
                   </defs>

                   <!-- Forward arrows (outer arc) -->
                   <path
                      v-for="(step, i) in resolutionSteps"
                      :key="'arrow-forward-'+i"
                      :d="getArrowPath(i, 0)"
                      :stroke="step.color"
                      stroke-width="3"
                      fill="none"
                      marker-end="url(#arrowhead-forward)"
                      stroke-linecap="round"
                      stroke-dasharray="8 4"
                      class="opacity-60"
                   />

                   <!-- Return arrows (inner arc) - positioned slightly offset -->
                   <path
                      v-for="(step, i) in resolutionSteps"
                      :key="'arrow-return-'+i"
                      :d="getArrowPath(i, -15)"
                      :stroke="step.color"
                      stroke-width="3"
                      fill="none"
                      marker-start="url(#arrowhead-reverse)"
                      stroke-linecap="round"
                      stroke-dasharray="8 4"
                      class="opacity-60"
                   />
                </svg>

                <!-- Steps -->
                <div 
                   v-for="(step, i) in resolutionSteps" 
                   :key="'step-'+i"
                   @mouseenter="activeStep = i"
                   @mouseleave="activeStep = null"
                   class="absolute -translate-x-1/2 -translate-y-1/2 bg-white rounded-full border-[1.5px] shadow-[0_10px_20px_rgba(0,0,0,0.05)] flex items-center justify-center z-10 hover:scale-110 transition-transform duration-300 w-[140px] h-[140px] cursor-pointer"
                   :style="getCircleStyle(i, step.color)"
                >
                   <div class="text-center p-2">
                      <div class="mb-2 flex justify-center" :style="{ color: step.color }">
                         <component :is="step.icon" class="w-8 h-8" />
                      </div>
                      <div class="leading-tight">
                         <h4 class="m-0 text-sm font-black text-slate-700" :style="{ color: step.color }">{{ step.title }}</h4>
                         <p class="m-0 text-[10px] text-gray-400 font-bold mt-1 uppercase tracking-wide">{{ step.subtitle }}</p>
                      </div>
                   </div>
                </div>

             </div>
          </div>
       </div>
    </section>

    <!-- F. Meet Our Team Section -->
    <section class="py-24 bg-transparent relative z-10" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
      <div class="container-custom">
        <div class="text-center mb-16">
          <h2 class="text-4xl font-black text-secondary mb-4">Meet Our Team</h2>
          <p class="text-secondary/70 font-bold max-w-2xl mx-auto">Dedicated professionals committed to the safety and well-being of every child.</p>
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
        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div v-for="member in teamMembers" :key="member.id" class="group bg-white rounded-[2rem] p-6 text-center shadow-sm hover:shadow-xl transition-all duration-300 border border-gray-100">
            <div class="w-32 h-32 mx-auto rounded-full overflow-hidden mb-6 border-4 border-primary/10 group-hover:border-primary transition-colors bg-gray-100 flex items-center justify-center">
              <img
                v-if="member.image"
                :src="member.image"
                :alt="member.name"
                class="w-full h-full object-cover"
                @error="handleImageError($event, member)"
                loading="lazy"
              />
              <User v-else class="w-16 h-16 text-gray-400" />
            </div>
            <h3 class="text-xl font-bold text-secondary mb-1">{{ member.name }}</h3>
            <p class="text-primary font-bold text-xs uppercase tracking-widest mb-4">{{ member.role }}</p>
            <p class="text-gray-600 text-sm leading-relaxed">{{ member.bio || 'Dedicated to the mission of Sauti 116.' }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- G. Core Values Section -->
    <section class="py-24 bg-transparent relative overflow-hidden" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
      <!-- Decorative background -->
      <div class="absolute top-0 right-0 w-96 h-96 bg-primary/5 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
      
      <div class="container-custom relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <div>
            <span class="inline-block px-4 py-1 bg-secondary/10 rounded-full text-xs font-bold uppercase tracking-widest mb-6 border border-secondary/20 text-secondary">Our Principles</span>
            <h2 class="text-4xl md:text-5xl font-black mb-8 leading-tight text-secondary">Driven by Values,<br/>United by Purpose.</h2>
            <p class="text-lg text-gray-600 leading-relaxed mb-8">
              Our core values guide every interaction, decision, and intervention. They are the foundation of our trust with the community.
            </p>
            <!-- Call to Action (Optional) -->
            <div class="flex gap-4">
              <div class="flex items-center gap-2">
                 <div class="w-10 h-10 rounded-full bg-primary flex items-center justify-center font-bold text-white">10+</div>
                 <span class="font-bold text-sm text-secondary">Years of Service</span>
              </div>
               <div class="flex items-center gap-2">
                 <div class="w-10 h-10 rounded-full bg-primary flex items-center justify-center font-bold text-white">1M+</div>
                 <span class="font-bold text-sm text-secondary">Lives Impacted</span>
              </div>
            </div>
          </div>

          <!-- Loading State -->
          <div v-if="coreValuesLoading" class="text-center py-12">
            <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
            <p class="text-gray-500 mt-4 font-bold">Loading core values...</p>
          </div>

          <!-- Core Values Grid -->
          <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div
              v-for="value in coreValues"
              :key="value.id"
              class="bg-gray-50 p-6 rounded-3xl border border-gray-100 hover:shadow-lg transition-all duration-300 group"
            >
              <div
                class="w-12 h-12 rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform"
                :class="[getColorClasses(value.color || 'blue').bg, getColorClasses(value.color || 'blue').text]"
              >
                <component :is="getIconComponent(value.icon || 'ShieldCheck')" class="w-6 h-6" />
              </div>
              <h3 class="text-xl font-bold mb-2 text-secondary">{{ value.title }}</h3>
              <p class="text-sm text-gray-500">{{ value.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>






  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useSettingsStore } from '@/store/settings'

 
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
  User
} from 'lucide-vue-next'

// --- Stores ---
const settingsStore = useSettingsStore()

// --- Data ---
const settings = computed(() => settingsStore.settings)
const teamMembers = ref([])
const teamLoading = ref(false)
const coreValues = ref([])
const coreValuesLoading = ref(false)



// --- Mock Data for Layout ---








// --- Infographic Logic ---
import { markRaw } from 'vue'

const activeStep = ref(null)
const timelineEvents = ref([])

const resolutionSteps = [
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

const centerX = 300
const centerY = 300
const radius = 210
const circleSize = 140

const getCoords = (index) => {
  // Distribute 4 items starting from top (-90 degrees)
  // 4 items = 90 degrees each
  const angle = (index * 90 - 90) * (Math.PI / 180)
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
  const startAngle = getCoords(i).angle
  const stepRad = (Math.PI / 180) * 90

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
const fetchCoreValues = async () => {
  coreValuesLoading.value = true
  try {
    const response = await api.coreValues.list({ is_active: true })
    coreValues.value = Array.isArray(response.data)
      ? response.data
      : (response.data.results || [])

    // Sort by order field
    coreValues.value.sort((a, b) => (a.order || 0) - (b.order || 0))

    console.log('Core values fetched:', coreValues.value.length)
  } catch (error) {
    console.error('Failed to fetch core values:', error)
    // Fallback to hardcoded values if API fails
    coreValues.value = [
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
    Zap
  }
  return iconMap[iconName] || ShieldCheck
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
// --- Fetching ---
onMounted(async () => {
  try {
    await settingsStore.fetchGlobalSettings()
  } catch (error) {
    console.warn('Failed to fetch settings:', error)
  }

  // Fetch team members and core values
  await fetchTeamMembers()
  await fetchCoreValues()

  // Custom fetches with fallback
  try {
    const timelineRes = await api.get('/content/timeline-events/')
    timelineEvents.value = timelineRes.data.results || timelineRes.data || []
  } catch (error) {
    console.warn('Failed to fetch timeline events, using mock data:', error)
    timelineEvents.value = [] // Reset to empty to trigger fallback below
  }

  // Ensure timelineEvents has data (Mockup fallback)
  if (!timelineEvents.value || timelineEvents.value.length === 0) {
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