<template>
  <div class="timeline-section">
    <div class="relative wrap overflow-hidden p-4 md:p-10 h-full">
      <!-- Vertical Line -->
      <div class="absolute border-opacity-20 border-gray-700 h-full border hidden md:block"
        style="left: 50%; width: 1px; transform: translateX(-50%);"></div>
      <div class="absolute border-opacity-20 border-gray-700 h-full border md:hidden" style="left: 2rem; width: 1px;">
      </div>

      <!-- Timeline Events -->
      <div v-for="(event, index) in sortedEvents" :key="event.id" class="mb-12 flex justify-between items-center w-full"
        :class="{ 'md:flex-row-reverse': index % 2 !== 0 }">

        <!-- Empty Space for Desktop -->
        <div class="hidden md:block w-5/12"></div>

        <!-- Dot / Year Indicator -->
        <div
          class="z-20 flex items-center order-1 bg-gray-800 shadow-xl w-12 h-12 rounded-full border-4 border-white transition-transform hover:scale-110">
          <h1 class="mx-auto font-bold text-xs text-white">{{ getYear(event) }}</h1>
        </div>

        <!-- Content Card -->
        <div
          class="order-1 rounded-2xl shadow-lg w-[calc(100%-4rem)] ml-16 md:ml-0 md:w-5/12 px-6 py-6 transition-all duration-300 hover:shadow-2xl hover:-translate-y-1"
          :class="index % 2 !== 0 ? 'bg-gradient-to-br from-[#1e40af] to-[#3b82f6]' : 'bg-gradient-to-br from-[#c2410c] to-[#f97316]'">
          <h3 class="mb-2 font-bold text-white text-xl">{{ event.title }}</h3>
          <p class="text-sm leading-relaxed text-white/90">{{ event.description }}</p>
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
          return yearA - yearB;
        });
      }
    },
    methods: {
      getYear(event) {
        if (!event) return '';
        // Try date first
        if (event.date) {
          const d = new Date(event.date);
          if (!isNaN(d.getTime())) return d.getFullYear();
          // If it's just a year string "2014"
          if (/^\d{4}$/.test(event.date)) return parseInt(event.date).toString();
        }
        // Try year property
        if (event.year) return event.year.toString();
        return '';
      }
    }
  };
</script>

<style scoped>
  .timeline-section {
    font-family: inherit;
  }

  .wrap {
    position: relative;
  }

  .z-20 {
    transition: all 0.3s ease;
  }

  @media (max-width: 767px) {
    /* Mobile adjustments handled by inline classes */
  }
</style>