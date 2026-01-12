<template>
  <div class="bg-neutral-white min-h-screen font-sans">
    
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

    <!-- Path to Resolution Section (SVG Infographic) -->
    <section class="py-24 bg-white overflow-hidden relative">
       <!-- Decorative Background Blob -->
       <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-blue-50/50 rounded-full blur-3xl -z-10 pointer-events-none"></div>

       <div class="container-custom relative z-10">
          <div class="text-center max-w-3xl mx-auto mb-20">
             <h2 class="text-4xl md:text-5xl font-black text-secondary mb-6">Path to Resolution</h2>
             <p class="text-xl text-gray-500 font-medium">How we ensure every case leads to safety.</p>
          </div>

          <!-- Infographic Container -->
          <div class="flex justify-center items-center h-[700px] bg-transparent rounded-[3rem] shadow-none border-none">
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
                      <marker id="arrowhead-loop" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                         <polygon points="0 0, 10 3.5, 0 7" fill="#cbd5e1" />
                      </marker>
                   </defs>
                   <path 
                      v-for="(step, i) in resolutionSteps" 
                      :key="'arrow-'+i"
                      :d="getArrowPath(i)" 
                      :stroke="step.color" 
                      stroke-width="3" 
                      fill="none" 
                      marker-end="url(#arrowhead-loop)"
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
  RotateCcw
} from 'lucide-vue-next'

// --- Stores ---
const settingsStore = useSettingsStore()



// --- Data ---
const settings = computed(() => settingsStore.settings)



// --- Mock Data for Layout ---








// --- Infographic Logic ---
import { markRaw } from 'vue'

const activeStep = ref(null)

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

const getArrowPath = (i) => {
  const startAngle = getCoords(i).angle
  const stepRad = (Math.PI / 180) * 90
  
  // Clearance to ensure arrow starts/ends outside the step circles
  // Circle radius is 70px. Track radius 210px. 
  // Angle of circle edge = asin(70/210) ~= 0.34 rads.
  // We use 0.55 rads to give space (shortening the lines).
  const clearance = 0.55
  
  const actualStartAngle = startAngle + clearance
  const actualEndAngle = startAngle + stepRad - clearance
  
  const x1 = centerX + radius * Math.cos(actualStartAngle)
  const y1 = centerY + radius * Math.sin(actualStartAngle)
  
  const x2 = centerX + radius * Math.cos(actualEndAngle)
  const y2 = centerY + radius * Math.sin(actualEndAngle)
  
  // SVG Arc command: A rx ry x-axis-rotation large-arc-flag sweep-flag x y
  return `M ${x1} ${y1} A ${radius} ${radius} 0 0 1 ${x2} ${y2}`
}


// --- Fetching ---
onMounted(async () => {
  await Promise.all([
    settingsStore.fetchGlobalSettings(),
  ])
  
  // Custom fetches
  const [timelineRes] = await Promise.all([
    api.get('/content/timeline-events/'),
  ])
  
  timelineEvents.value = timelineRes.data.results || timelineRes.data || []
})

</script>