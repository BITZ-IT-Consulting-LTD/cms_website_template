<template>
  <div class="timeline-section relative font-sans p-4 md:p-8">
    <div class="relative max-w-5xl mx-auto">
      <!-- Central Dotted Line -->
      <div class="absolute left-4 md:left-1/2 top-0 bottom-0 w-1 border-l-4 border-dotted border-gray-300 md:-translate-x-1/2 z-0"></div>

      <div 
        v-for="(event, index) in sortedEvents" 
        :key="event.id" 
        class="relative mb-24 flex flex-col md:flex-row items-start md:items-center w-full group"
      >
        
        <!-- Center Node (Year Indicator) -->
        <div class="hidden md:flex absolute left-1/2 -translate-x-1/2 items-center justify-center z-10">
           <div class="w-16 h-16 rounded-full bg-white border-4 shadow-md flex items-center justify-center font-bold text-gray-600 text-sm transition-transform group-hover:scale-110"
                :style="{ borderColor: getEventColor(index) }">
              {{ getYear(event) }}
           </div>
        </div>

        <!-- Mobile: Left Node -->
         <div class="md:hidden absolute left-4 -translate-x-1/2 flex items-center justify-center z-10 top-0">
           <div class="w-12 h-12 rounded-full bg-white border-4 shadow-md flex items-center justify-center font-bold text-gray-600 text-[10px]"
                :style="{ borderColor: getEventColor(index) }">
              {{ getYear(event) }}
           </div>
        </div>

        <!-- LEFT SIDE CONTENT (For Even Index on Desktop) -->
        <div class="w-full md:w-1/2 pl-12 md:pl-0 md:pr-16 text-left md:text-right flex flex-col items-start md:items-end order-2 md:order-1" 
             v-if="index % 2 === 0 || isMobile">
          
          <!-- Leaf Container (Left Side) -->
          <div class="leaf relative flex items-center justify-center" 
               :style="{ backgroundColor: getEventColor(index), borderRadius: '0% 100% 0% 100%' }">
            <!-- Content Wrapper: Centered with padding -->
            <div class="p-8 md:p-10 text-white text-center flex flex-col justify-center h-full relative z-10 w-full">
              <p class="font-black text-lg md:text-xl leading-tight mb-2 shadow-sm">{{ event.title }}</p>
              <p class="text-xs font-bold opacity-90 uppercase tracking-widest">{{ getYear(event) }}</p>
            </div>
          </div>

          <!-- Description Text (Outside Leaf) -->
          <div class="mt-4 max-w-xs text-sm md:text-base font-medium text-gray-500 leading-relaxed md:text-right">
            {{ event.description }}
          </div>
        </div>
        
        <!-- EMPTY FILLER FOR DESKTOP GRID -->
        <div class="hidden md:block w-1/2 order-2" v-if="index % 2 === 0"></div>


        <!-- RIGHT SIDE CONTENT (For Odd Index on Desktop) -->
        <div class="hidden md:block w-1/2 order-1" v-if="index % 2 !== 0"></div>

        <div class="w-full md:w-1/2 pl-12 md:pl-16 flex flex-col items-start order-2" 
             v-if="index % 2 !== 0">
           
           <!-- Leaf Container (Right Side) -->
          <div class="leaf relative flex items-center justify-center" 
               :style="{ backgroundColor: getEventColor(index), borderRadius: '100% 0% 100% 0%' }">
            <!-- Content Wrapper: Centered with padding -->
            <div class="p-8 md:p-10 text-white text-center flex flex-col justify-center h-full relative z-10 w-full">
              <p class="font-black text-lg md:text-xl leading-tight mb-2 shadow-sm">{{ event.title }}</p>
              <p class="text-xs font-bold opacity-90 uppercase tracking-widest">{{ getYear(event) }}</p>
            </div>
          </div>

          <!-- Description Text (Outside Leaf) -->
          <div class="mt-4 max-w-xs text-sm md:text-base font-medium text-gray-500 leading-relaxed text-left">
            {{ event.description }}
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
  import { computed } from 'vue'

  export default {
    name: 'AppTimeline',
    props: {
      timelineEvents: {
        type: Array,
        required: true,
        default: () => []
      }
    },
    setup(props) {
        // Updated Color Palette from the requested design + extras for variety
        const colors = [
            '#8db724', // Lime
            '#0091ff', // Blue
            '#fdd808', // Yellow
            '#ff8a00', // Orange
            '#ff4b12', // Red-Orange
            '#9b248d', // Purple
            '#10b981', // Emerald
            '#6366f1'  // Indigo
        ]

        const getEventColor = (index) => {
            return colors[index % colors.length]
        }

        const isMobile = computed(() => {
            if (typeof window !== 'undefined') {
                return window.innerWidth < 768
            }
            return false
        })

        const sortedEvents = computed(() => {
            if (!Array.isArray(props.timelineEvents)) return [];
            // Sort ascending
            return [...props.timelineEvents].sort((a, b) => {
                const yearA = getYear(a);
                const yearB = getYear(b);
                return yearA - yearB;
            });
        });

        const getYear = (event) => {
            if (!event) return '';
            if (event.year) return event.year.toString();
            if (event.date) {
                const d = new Date(event.date);
                if (!isNaN(d.getTime())) return d.getFullYear();
                if (/^\d{4}$/.test(event.date)) return event.date;
            }
            return '';
        }

        return {
            sortedEvents,
            getEventColor,
            getYear,
            isMobile
        }
    }
  };
</script>

<style scoped>
.leaf {
  width: 100%;
  max-width: 300px; /* Increased max-width */
  min-height: 160px; /* Increased min-height for better fit */
  display: flex;
  align-items: center;
  justify-content: center; /* Center content exactly */
  box-shadow: 15px 15px 30px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}

.leaf:hover {
  transform: scale(1.05);
}

/* Creating the diagonal stem line for each leaf */
.leaf::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, transparent 48%, rgba(255,255,255,0.2) 49%, rgba(255,255,255,0.2) 51%, transparent 52%);
  pointer-events: none;
}
</style>