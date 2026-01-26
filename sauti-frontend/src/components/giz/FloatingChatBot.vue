<template>
  <div class="chatbot-container">
    <!-- Report button - navigates to report page -->
    <router-link to="/report" class="chat-button" aria-label="Report a Case">
      <!-- Chat bubble icon for reporting -->
      <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
      </svg>
      <!-- Tooltip text - WhatsApp style bubble -->
      <span class="tooltip-text">Report a case here</span>
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
  background-color: rgb(198, 40, 40); /* Red matching Call 116 button */
  color: white;
  border: none;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(198, 40, 40, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  text-decoration: none;
}

.chat-button:hover {
  background-color: rgb(178, 36, 36); /* Darker red on hover */
  transform: scale(1.05);
  box-shadow: 0 6px 16px rgba(198, 40, 40, 0.4);
}

.chat-button:active {
  transform: scale(0.98);
}

/* Tooltip styles - WhatsApp message bubble style */
.chat-button {
  position: relative;
}

.tooltip-text {
  position: absolute;
  right: 0; /* Align to the right edge of button */
  bottom: 75px; /* Position above the button */
  transform-origin: bottom right; /* Pop from top-left of button */
  /* Red theme background matching Call 116 button */
  background-color: rgb(198, 40, 40); /* Red background */
  color: white; /* White text */
  padding: 10px 16px; /* Similar to !py-2.5 !px-6 from header button */
  border-radius: 7.5px 7.5px 7.5px 0; /* Speech bubble rounded corners with tail at bottom-right */
  font-size: 14px; /* !text-sm from header button */
  font-weight: 700; /* !font-bold from header button */
  white-space: nowrap;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.25s cubic-bezier(0.4, 0, 0.2, 1),
              visibility 0.25s cubic-bezier(0.4, 0, 0.2, 1),
              transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  transform: translateY(8px) scale(0.95);
  pointer-events: none;
  z-index: 2147483648; /* Above the button */
  /* Red shadow matching red theme */
  box-shadow: 0 4px 20px rgba(198, 40, 40, 0.3);
  /* Subtle border like buttons */
  border: 1px solid rgba(0, 0, 0, 0.1);
}

/* Speech bubble tail/pointer pointing down to top-left of button */
.tooltip-text::after {
  content: '';
  position: absolute;
  right: 0; /* Align to right edge (top-left of button) */
  bottom: -8px; /* Position below the bubble */
  width: 0;
  height: 0;
  /* Create curved tail pointing down-right */
  border: 8px solid transparent;
  border-top-color: rgb(198, 40, 40); /* Match red bubble background */
  border-right-width: 0;
  border-left-width: 12px;
  border-top-width: 8px;
  border-bottom-width: 0;
  /* Position the tail to connect smoothly at the corner */
  transform: translateX(0);
}

/* Shadow for the tail */
.tooltip-text::before {
  content: '';
  position: absolute;
  right: -1px;
  bottom: -9px;
  width: 0;
  height: 0;
  border: 9px solid transparent;
  border-top-color: rgba(0, 0, 0, 0.08);
  border-right-width: 0;
  border-left-width: 13px;
  border-top-width: 9px;
  border-bottom-width: 0;
  z-index: -1;
}

.chat-button:hover .tooltip-text {
  opacity: 1;
  visibility: visible;
  transform: translateY(0) scale(1);
  /* Enhanced red shadow on hover */
  box-shadow: 0 8px 30px rgba(198, 40, 40, 0.4);
}
</style>
