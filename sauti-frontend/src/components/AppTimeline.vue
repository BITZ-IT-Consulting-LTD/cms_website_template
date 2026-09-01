<template>
  <div class="timeline-wrapper">
    <!-- Mobile & Tablet: Vertical Timeline -->
    <div class="lg:hidden space-y-6 md:space-y-8">
      <div
        v-for="(event, index) in sortedEvents"
        :key="event.id"
        class="timeline-item group"
      >
        <!-- Card -->
        <div class="timeline-card bg-white rounded-2xl p-5 md:p-6 shadow-sm hover:shadow-lg border border-gray-100 transition-all duration-300 relative"
             :style="{ borderTopWidth: '4px', borderTopColor: getEventColor(index) }">

          <!-- Year Badge -->
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full mb-3 md:mb-4"
               :style="{ backgroundColor: getEventColor(index) + '14', color: getEventColor(index) }">
            <Calendar class="w-3 h-3 md:w-3.5 md:h-3.5" />
            <span class="font-black text-xs md:text-sm">{{ getYear(event) }}</span>
          </div>

          <!-- Content -->
          <div class="text-center">
            <h3 class="text-base md:text-lg font-black text-gray-800 mb-2 md:mb-3 leading-tight">
              {{ event.title }}
            </h3>
            <p class="text-xs md:text-sm text-gray-500 leading-relaxed">
              {{ event.description }}
            </p>
          </div>

          <!-- Progress Indicator -->
          <div v-if="index < sortedEvents.length - 1" class="absolute -bottom-6 md:-bottom-8 left-1/2 -translate-x-1/2">
            <div class="w-0.5 h-6 md:h-8 bg-gradient-to-b from-gray-300 to-transparent"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Desktop: Horizontal Timeline -->
    <div class="hidden lg:block relative">
      <!-- Timeline Track -->
      <div class="relative pt-8 pb-8">
        <!-- Progress Bar -->
        <div class="absolute top-12 left-0 right-0 h-1 bg-gray-200 rounded-full">
          <div class="h-full bg-gradient-to-r from-primary via-secondary to-primary rounded-full"
               :style="{ width: '100%' }"></div>
        </div>

        <!-- Timeline Items -->
        <div class="grid gap-8" :style="{ gridTemplateColumns: `repeat(${sortedEvents.length}, 1fr)` }">
          <div
            v-for="(event, index) in sortedEvents"
            :key="event.id"
            class="timeline-item-desktop group relative"
          >
            <!-- Milestone Marker -->
            <div class="absolute top-8 left-1/2 -translate-x-1/2 z-10">
              <div class="relative w-12 h-12 rounded-full shadow-lg flex items-center justify-center border-4 border-white group-hover:scale-110 transition-transform duration-300"
                   :style="{ backgroundColor: getEventColor(index) }">
                <Calendar class="w-5 h-5 text-white" />
              </div>
            </div>

            <!-- Content Card -->
            <div class="pt-24 relative">
              <div class="bg-white rounded-2xl p-5 shadow-sm hover:shadow-lg border border-gray-100 transition-all duration-300 group-hover:-translate-y-1"
                   :style="{ borderTopWidth: '4px', borderTopColor: getEventColor(index) }">

                <!-- Year Badge -->
                <div class="inline-flex items-center px-3 py-1 rounded-full mb-3"
                     :style="{ backgroundColor: getEventColor(index) + '14', color: getEventColor(index) }">
                  <span class="font-black text-xs">{{ getYear(event) }}</span>
                </div>

                <!-- Title -->
                <h3 class="text-sm font-black text-gray-800 mb-2 leading-tight text-center">
                  {{ event.title }}
                </h3>

                <!-- Description -->
                <p class="text-xs text-gray-500 leading-relaxed text-center line-clamp-4">
                  {{ event.description }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'
import { Calendar } from 'lucide-vue-next'

export default {
  name: 'AppTimeline',
  components: { Calendar },
  props: {
    timelineEvents: {
      type: Array,
      required: true,
      default: () => []
    }
  },
  setup(props) {
    // Alternating brand colors (green and blue)
    const colors = [
      '#006633', // Brand Green
      '#005f99', // Brand Blue
    ]

    const getEventColor = (index) => {
      return colors[index % colors.length]
    }

    const sortedEvents = computed(() => {
      if (!Array.isArray(props.timelineEvents)) return []
      return [...props.timelineEvents].sort((a, b) => {
        const yearA = getYear(a)
        const yearB = getYear(b)
        return yearA - yearB
      })
    })

    const getYear = (event) => {
      if (!event) return ''
      if (event.year) return event.year.toString()
      if (event.date) {
        const d = new Date(event.date)
        if (!isNaN(d.getTime())) return d.getFullYear()
        if (/^\d{4}$/.test(event.date)) return event.date
      }
      return ''
    }

    return {
      sortedEvents,
      getEventColor,
      getYear,
      Calendar
    }
  }
}
</script>

<style scoped>
.timeline-wrapper {
  @apply relative;
}

/* Smooth animations */
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

.timeline-item,
.timeline-item-desktop {
  animation: fadeInUp 0.6s ease-out backwards;
}

.timeline-item:nth-child(1),
.timeline-item-desktop:nth-child(1) {
  animation-delay: 0.1s;
}

.timeline-item:nth-child(2),
.timeline-item-desktop:nth-child(2) {
  animation-delay: 0.2s;
}

.timeline-item:nth-child(3),
.timeline-item-desktop:nth-child(3) {
  animation-delay: 0.3s;
}

.timeline-item:nth-child(4),
.timeline-item-desktop:nth-child(4) {
  animation-delay: 0.4s;
}

.timeline-item:nth-child(5),
.timeline-item-desktop:nth-child(5) {
  animation-delay: 0.5s;
}

/* Line clamp utility */
.line-clamp-4 {
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
