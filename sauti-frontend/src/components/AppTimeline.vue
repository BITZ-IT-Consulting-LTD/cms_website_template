<template>
  <div class="timeline-section relative font-sans">
    <div class="relative wrap overflow-hidden p-4 md:p-10 h-full max-w-6xl mx-auto">
      
      <!-- Vertical Line -->
      <!-- Desktop: Center -->
      <div class="hidden md:block absolute border-opacity-20 border-gray-400 h-full border-l-4"
        style="left: 50%; transform: translateX(-50%);"></div>
      <!-- Mobile: Left -->
      <div class="md:hidden absolute border-opacity-20 border-gray-400 h-full border-l-4" 
        style="left: 2rem;"></div>

      <!-- Timeline Events -->
      <div 
        v-for="(event, index) in sortedEvents" 
        :key="event.id" 
        class="mb-12 flex justify-between items-center w-full relative z-10"
        :class="{ 'md:flex-row-reverse': index % 2 !== 0 }"
      >

        <!-- Empty Space for Desktop layout balance -->
        <div class="hidden md:block w-5/12"></div>

        <!-- Dot / Year Indicator -->
        <div class="z-20 flex items-center justify-center order-1 bg-gray-800 shadow-xl w-12 h-12 rounded-full border-4 border-white transition-transform duration-300 hover:scale-125 shrink-0 relative">
          <span class="font-black text-xs text-white">{{ getYear(event) }}</span>
        </div>

        <!-- Content Card -->
        <!-- 
             Odd (Left on desktop usually, but order depends on flex-row-reverse):
             If index % 2 === 0 (Even index, 1st item): Standard order. Card is on Right (or Left if we want standard timeline flow).
             Wait, standard vertical timeline usually alternates Left/Right.
             
             Let's stick to the visual provided:
             Odd Items (Index 0, 2... wait, 1st item is Index 0): 
             Let's say Index 0 is "1st Item" (Odd in human counting).
             
             Current Code Logic:
             :class="{ 'md:flex-row-reverse': index % 2 !== 0 }"
             Index 0: No reverse. Order: Space - Dot - Card. (Card on Right).
             Index 1: Reverse. Order: Card - Dot - Space. (Card on Left).
             
             User Request:
             Odd Items (1st, 3rd... Index 0, 2): Blue Gradient.
             Even Items (2nd, 4th... Index 1, 3): Orange Gradient.
        -->
        <div
          class="order-1 rounded-2xl shadow-lg w-[calc(100%-4rem)] ml-6 md:ml-0 md:w-5/12 px-6 py-8 transition-all duration-300 hover:-translate-y-1 group relative bg-gradient-to-br"
          :class="[
            index % 2 === 0 
              ? 'from-[#1e40af] to-[#3b82f6]' // Blue for Odd (1st) item
              : 'from-[#c2410c] to-[#f97316]' // Orange for Even (2nd) item
          ]"
        >
          <h3 class="mb-3 font-black text-white text-xl md:text-2xl tracking-tight leading-none">{{ event.title }}</h3>
          <p class="text-base md:text-lg leading-relaxed text-white/90 font-medium">
            {{ event.description }}
          </p>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'AppTimeline',
    props: {
      timelineEvents: {
        type: Array,
        required: true,
        default: () => []
      }
    },
    computed: {
      sortedEvents() {
        if (!Array.isArray(this.timelineEvents)) return [];
        return [...this.timelineEvents].sort((a, b) => {
          const yearA = this.getYear(a);
          const yearB = this.getYear(b);
          // Sort ascending (Oldest first)
          return yearA - yearB;
        });
      }
    },
    methods: {
      getYear(event) {
        if (!event) return '';
        // If year is explicitly provided
        if (event.year) return event.year.toString();
        
        // Try to parse date
        if (event.date) {
          const d = new Date(event.date);
          if (!isNaN(d.getTime())) return d.getFullYear();
          // Fallback if date is just a year string e.g. "2014"
          if (/^\d{4}$/.test(event.date)) return event.date;
        }
        
        return 'Year';
      }
    }
  };
</script>

<style scoped>
/* No specific styles needed as Tailwind covers it */
</style>