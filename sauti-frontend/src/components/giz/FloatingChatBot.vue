<template>
  <div class="chatbot-container">
    <!-- Report button - navigates to report page -->
    <router-link to="/report" class="chat-button" aria-label="Report a Case">
      <!-- Child calling icon -->
      <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <!-- Child head silhouette -->
        <circle cx="12" cy="8" r="4" stroke-width="2"/>
        <!-- Body/neck -->
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16c0-2 2-4 4-4s4 2 4 4"/>
        <!-- Sound waves from mouth -->
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M16 8c1.5 0 2 .5 3 1.5M19 9c2 1 2.5 2 3 3.5M22 11c2 1.5 2.5 3 3 5"/>
      </svg>
    </router-link>
  </div>
</template>

<script>
import { onMounted, onBeforeUnmount } from "vue";
import { useRouter } from 'vue-router';
import emitter from '@/utils/eventBus.js';

export default {
  name: 'FloatingChatBot',
  setup() {
    const router = useRouter();

    onMounted(() => {
      // Listen for the open-chat event and redirect to report page
      emitter.on('open-chat', () => {
        console.log('Received open-chat event - redirecting to report page');
        router.push('/report');
      });
    });

    onBeforeUnmount(() => {
      // Clean up
      emitter.off('open-chat');
    });

    return {};
  }
}
</script>

<style scoped>
/* Import Giz base and layout styles to ensure proper rendering within the scoped component */
@import url('@/assets/giz-css/base.css');
@import url('@/assets/giz-css/layout.css');

.chatbot-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 2147483647; /* Max z-index to ensure visibility */
}

.chat-button {
  background-color: #DC2626; /* Red */
  color: white;
  border: none;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(220, 38, 38, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  text-decoration: none;
}

.chat-button:hover {
  background-color: #B91C1C; /* Darker red */
  transform: scale(1.05);
  box-shadow: 0 6px 16px rgba(220, 38, 38, 0.4);
}

.chat-button:active {
  transform: scale(0.98);
}
</style>
