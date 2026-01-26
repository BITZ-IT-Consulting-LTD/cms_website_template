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
        
        <!-- Center Node (Year Indicator) - Desktop -->
        <div class="hidden md:flex absolute left-1/2 -translate-x-1/2 items-center justify-center z-20">
           <div class="date-circle">
              <span class="date-text">{{ getYear(event) }}</span>
           </div>
        </div>

        <!-- Mobile: Left Node -->
         <div class="md:hidden absolute left-4 -translate-x-1/2 flex items-center justify-center z-20 top-0">
           <div class="date-circle-mobile">
              <span class="date-text-mobile">{{ getYear(event) }}</span>
           </div>
        </div>

        <!-- LEFT SIDE CONTENT (For Even Index on Desktop) -->
        <div class="w-full md:w-1/2 pl-12 md:pl-0 md:pr-16 text-left md:text-right flex flex-col items-start md:items-end order-2 md:order-1"
             v-if="index % 2 === 0 || isMobile">

          <!-- Message Bubble Container (Left Side - White Background with Dark Green Text) -->
          <div class="message-bubble message-bubble-left relative flex items-center justify-center">
            <!-- Content Wrapper: Centered with padding -->
            <div class="p-8 md:p-10 text-center flex flex-col justify-center h-full relative z-10 w-full">
              <p class="font-black text-lg md:text-xl leading-tight mb-2 text-[#006837]">{{ event.title }}</p>
              <p class="text-xs font-bold opacity-70 uppercase tracking-widest text-[#006837]">{{ getYear(event) }}</p>
            </div>
          </div>

          <!-- Description Text (Outside Bubble) -->
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

           <!-- Message Bubble Container (Right Side - Dark Green Background with White Text) -->
          <div class="message-bubble message-bubble-right relative flex items-center justify-center">
            <!-- Content Wrapper: Centered with padding -->
            <div class="p-8 md:p-10 text-center flex flex-col justify-center h-full relative z-10 w-full">
              <p class="font-black text-lg md:text-xl leading-tight mb-2 text-white">{{ event.title }}</p>
              <p class="text-xs font-bold opacity-90 uppercase tracking-widest text-white">{{ getYear(event) }}</p>
            </div>
          </div>

          <!-- Description Text (Outside Bubble) -->
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
/* Date Circle Styles - Desktop */
.date-circle {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background-color: #FFFFFF;
  border: 2px solid #006837; /* Dark green border */
  box-shadow: 0 4px 12px rgba(0, 104, 55, 0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.date-circle:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 16px rgba(0, 104, 55, 0.25);
}

.date-text {
  font-weight: 700;
  font-size: 0.875rem; /* 14px */
  color: #006837; /* Dark green text */
  text-align: center;
  line-height: 1.3;
  padding: 0 8px;
  word-wrap: break-word;
  max-width: 100%;
}

/* Date Circle Styles - Mobile */
.date-circle-mobile {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background-color: #FFFFFF;
  border: 2px solid #006837; /* Dark green border */
  box-shadow: 0 3px 10px rgba(0, 104, 55, 0.15);
  display: flex;
  align-items: center;
  justify-content: center;
}

.date-text-mobile {
  font-weight: 700;
  font-size: 0.625rem; /* 10px */
  color: #006837; /* Dark green text */
  text-align: center;
  line-height: 1.2;
  padding: 0 4px;
  word-wrap: break-word;
  max-width: 100%;
}

/* Base Message Bubble Styles */
.message-bubble {
  width: 100%;
  max-width: 300px;
  min-height: 160px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 7.5px; /* Rounded corners as specified */
  box-shadow: 0 2px 8px rgba(0, 104, 55, 0.1); /* Green-tinted shadow */
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
}

.message-bubble:hover {
  transform: translateY(-2px); /* Slight lift on hover */
  box-shadow: 0 4px 12px rgba(0, 104, 55, 0.2);
}

/* Left Side Bubbles - White Background with Dark Green Text and Border */
.message-bubble-left {
  background-color: #FFFFFF;
  border: 2px solid #006837; /* Dark green border */
}

/* Left bubble tail pointing RIGHT (toward center date circle) */
.message-bubble-left::after {
  content: '';
  position: absolute;
  right: -12px; /* Position on right side of bubble */
  top: 50%;
  transform: translateY(-50%);
  width: 0;
  height: 0;
  border: 12px solid transparent;
  border-left-color: #FFFFFF; /* White tail matching bubble background */
  border-right-width: 0;
  border-top-width: 12px;
  border-bottom-width: 12px;
  filter: drop-shadow(1px 0px 1px rgba(0, 104, 55, 0.1));
}

/* Border for the tail */
.message-bubble-left::before {
  content: '';
  position: absolute;
  right: -14px;
  top: 50%;
  transform: translateY(-50%);
  width: 0;
  height: 0;
  border: 12px solid transparent;
  border-left-color: #006837; /* Dark green border for tail */
  border-right-width: 0;
  border-top-width: 12px;
  border-bottom-width: 12px;
  z-index: -1;
}

/* Right Side Bubbles - Dark Green Background with White Text */
.message-bubble-right {
  background-color: #006837; /* Dark green background */
}

/* Right bubble tail pointing LEFT (toward center date circle) */
.message-bubble-right::after {
  content: '';
  position: absolute;
  left: -12px; /* Position on left side of bubble */
  top: 50%;
  transform: translateY(-50%);
  width: 0;
  height: 0;
  border: 12px solid transparent;
  border-right-color: #006837; /* Dark green tail matching bubble background */
  border-left-width: 0;
  border-top-width: 12px;
  border-bottom-width: 12px;
  filter: drop-shadow(-1px 0px 1px rgba(0, 104, 55, 0.2));
}
</style>