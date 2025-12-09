<template>
  <div class="chatbot-container">
    <!-- Chatbot button - only visible when completely closed -->
    <button @click="toggleChat" class="chat-button" v-if="!isChatOpen && !isMinimized">
      <font-awesome-icon :icon="['fas', 'comment-dots']" />
    </button>
    
    <!-- Chat window - visible when open OR minimized -->
    <DynamicChatWindow 
      v-if="isChatOpen || isMinimized" 
      :minimized="isMinimized"
      @closeChat="closeChat" 
      @minimizeChat="minimizeChat"
      @maximizeChat="restoreChat" />
  </div>
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from "vue";
import DynamicChatWindow from "./DynamicChatWindow.vue";
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import emitter from '@/utils/eventBus.js';

import { library } from '@fortawesome/fontawesome-svg-core';
import { faCommentDots } from '@fortawesome/free-solid-svg-icons';

library.add(faCommentDots);

export default {
  name: 'FloatingChatBot',
  components: {
    DynamicChatWindow,
    FontAwesomeIcon
  },
  setup() {
    const isChatOpen = ref(false);
    const isMinimized = ref(false);

    const toggleChat = () => {
      isChatOpen.value = !isChatOpen.value;
      isMinimized.value = false;
    };

    const minimizeChat = () => {
      isMinimized.value = true;
      isChatOpen.value = false;
    };

    const restoreChat = () => {
      isChatOpen.value = true;
      isMinimized.value = false;
    };

    const closeChat = () => {
      isChatOpen.value = false;
      isMinimized.value = false;
      localStorage.removeItem("responses");
    };

    onMounted(() => {
      // Listen for the open-chat event from any component
      emitter.on('open-chat', () => {
        console.log('Received open-chat event');
        isChatOpen.value = true;
        isMinimized.value = false;
      });
    });

    onBeforeUnmount(() => {
      // Clean up
      emitter.off('open-chat');
    });

    return {
      isChatOpen,
      isMinimized,
      toggleChat,
      minimizeChat,
      restoreChat,
      closeChat
    };
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
  background-color: #009EDB; /* Sauti Blue */
  color: white;
  border: none;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  font-size: 24px;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(0, 158, 219, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.chat-button:hover {
  background-color: #007BAA; /* Darkened Sauti Blue */
  transform: scale(1.05);
  box-shadow: 0 6px 16px rgba(0, 158, 219, 0.4);
}

.chat-button:active {
  transform: scale(0.98);
}
</style>
