<template>
  <div class="chatbot-container">
    <!-- Report button - navigates to report page -->
    <router-link to="/report" class="chat-button" aria-label="Report a Case">
      <!-- Chat bubble icon for reporting -->
      <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
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
