<template>
  <div class="timeline-section">
    <h2 class="text-3xl font-bold text-center mb-8">Our Journey</h2>
    <div class="relative wrap overflow-hidden p-10 h-full">
      <div class="border-2-2 absolute border-opacity-20 border-gray-700 h-full border" style="left: 50%"></div>
      <!-- Timeline Event -->
      <div v-for="(event, index) in timelineEvents" :key="event.id"
           :class="{'mb-8 flex justify-between flex-row-reverse items-center w-full left-timeline': index % 2 !== 0, 'mb-8 flex justify-between items-center w-full right-timeline': index % 2 === 0}">
        <div class="order-1 w-5/12"></div>
        <div class="z-20 flex items-center order-1 bg-gray-800 shadow-xl w-8 h-8 rounded-full">
          <h1 class="mx-auto font-semibold text-lg text-white">{{ event.year }}</h1>
        </div>
        <div :class="{'order-1 bg-red-400 rounded-lg shadow-xl w-5/12 px-6 py-4': index % 2 !== 0, 'order-1 bg-blue-400 rounded-lg shadow-xl w-5/12 px-6 py-4': index % 2 === 0}">
          <h3 class="mb-3 font-bold text-gray-800 text-xl">{{ event.title }}</h3>
          <p class="text-sm leading-snug tracking-wide text-gray-900 text-opacity-100">{{ event.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AppTimeline',
  data() {
    return {
      timelineEvents: []
    };
  },
  async created() {
    try {
      const response = await axios.get('/api/timeline/');
      this.timelineEvents = response.data.results;
    } catch (error) {
      console.error('Error fetching timeline events:', error);
    }
  }
};
</script>

<style scoped>
.timeline-section {
  font-family: 'Arial', sans-serif;
  color: #333;
}

.wrap {
  position: relative;
}

.wrap .border-2-2 { /* Corrected selector for the central line */
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  width: 2px;
  background-color: #e5e7eb; /* Tailwind gray-200 */
  transform: translateX(-50%);
}

.left-timeline {
  left: 0;
}

.right-timeline {
  left: 50%;
}

/* Adjust positioning for timeline items */
.left-timeline .order-1:first-child { /* This targets the empty div for spacing */
  width: 50%;
  margin-left: 0;
  margin-right: 0;
}

.left-timeline .order-1:last-child { /* This targets the content card */
  width: 45%; /* Slightly less than 50% to leave space for the line */
  margin-left: 0;
  margin-right: 5%; /* Space from the center line */
}

.right-timeline .order-1:first-child { /* This targets the empty div for spacing */
  width: 50%;
  margin-left: 0;
  margin-right: 0;
}

.right-timeline .order-1:last-child { /* This targets the content card */
  width: 45%; /* Slightly less than 50% to leave space for the line */
  margin-left: 5%; /* Space from the center line */
  margin-right: 0;
}

.left-timeline .z-20 {
  left: 50%;
  transform: translateX(-50%);
}

.right-timeline .z-20 {
  left: 50%;
  transform: translateX(-50%);
}

/* Small screens */
@media (max-width: 768px) {
  .wrap .border-2-2 {
    left: 20px;
    transform: translateX(0);
  }

  .left-timeline, .right-timeline {
    left: 0;
    margin-bottom: 20px;
    flex-direction: row; /* Ensure content flows correctly */
  }

  .left-timeline .order-1:first-child,
  .right-timeline .order-1:first-child {
    width: 0; /* Hide the empty div on small screens */
  }

  .left-timeline .order-1:last-child,
  .right-timeline .order-1:last-child {
    width: calc(100% - 60px); /* Adjust width to account for dot and line */
    margin-left: 60px; /* Space for the dot and line */
    margin-right: 0;
  }

  .left-timeline .z-20, .right-timeline .z-20 {
    left: 20px;
    transform: translateX(-50%);
  }
}
</style>
