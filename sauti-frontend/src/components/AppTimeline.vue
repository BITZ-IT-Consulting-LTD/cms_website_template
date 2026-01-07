<template>
  <div class="timeline-section relative">
    <div class="relative wrap overflow-hidden p-4 md:p-10 h-full">
      <!-- Vertical Line -->
      <div class="absolute border-opacity-30 border-primary h-full border-l-2 hidden md:block"
        style="left: 50%; transform: translateX(-50%);"></div>
      <div class="absolute border-opacity-30 border-primary h-full border-l-2 md:hidden" style="left: 2rem;">
      </div>

      <!-- Timeline Events -->
      <div v-for="(event, index) in sortedEvents" :key="event.id" class="mb-12 flex justify-between items-center w-full"
        :class="{ 'md:flex-row-reverse': index % 2 !== 0 }">

        <!-- Empty Space for Desktop -->
        <div class="hidden md:block w-5/12"></div>

        <!-- Dot / Year Indicator -->
        <div
          class="z-20 flex items-center justify-center order-1 bg-neutral-white shadow-lg w-14 h-14 rounded-full border-4 border-primary transition-transform hover:scale-110 shrink-0">
          <span class="font-bold text-sm text-primary">{{ getYear(event) }}</span>
        </div>

        <!-- Content Card -->
        <div
          class="order-1 rounded-[2.5rem] shadow-sm bg-neutral-white w-[calc(100%-5rem)] ml-[4.5rem] md:ml-0 md:w-5/12 px-8 py-10 transition-all duration-500 hover:shadow-2xl border-2 border-neutral-offwhite hover:border-primary relative group">

          <!-- Connector arrow (desktop only) -->
          <div
            class="hidden md:block absolute top-1/2 -translate-y-1/2 w-4 h-4 bg-neutral-white border-t border-l border-neutral-offwhite rotate-45 transform group-hover:bg-neutral-offwhite/20 transition-colors"
            :class="index % 2 !== 0 ? '-right-2 border-r-0 border-b-0' : '-left-2 border-r-0 border-b-0'"></div>

          <h3 class="mb-4 font-bold text-secondary text-2xl tracking-tight">{{ event.title }}</h3>
          <p class="text-lg leading-relaxed text-secondary/70 font-bold">{{ event.description }}</p>
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
</style>