<template>
  <div class="chat-window" :class="{ 'chat-minimized': props.minimized }">
    <!-- Chat Header with Navigation and Controls -->
    <div class="chat-header">
      <div class="header-controls">
        <!-- Back button for navigation between stages -->
        <button v-if="canGoBack" @click="goBack" class="back-button">
          <FontAwesomeIcon :icon="['fas', 'arrow-left']" />
        </button>
      </div>
      <div class="window-controls">
        <div class="chat-with-us-animated">
          <span class="static-text">MGLSD Support, </span>
          <span class="typing-text">We are here for you</span>
          <span class="cursor"></span>
        </div>
        <!-- Show minimize button when not minimized -->
        <button v-if="!props.minimized" @click="minimizeChat" class="minimize-button">
          <FontAwesomeIcon :icon="['fas', 'minus']" />
        </button>
        <!-- Show maximize button when minimized -->
        <button v-else @click="maximizeChat" class="maximize-button">
          <FontAwesomeIcon :icon="['fas', 'maximize']" />
        </button>
        <button @click="closeChat" class="close-button">
          <FontAwesomeIcon :icon="['fas', 'xmark']" />
        </button>
      </div>
    </div>

    <!-- Chat Profile Section -->
    <div class="chat-profile">
      <div class="bot-avatar">
        <img src="@/assets/call.png" alt="MGLSD Support" />
        <span class="status-indicator"></span>
      </div>
      <h3 class="bot-name">MGLSD Labor Support</h3>
      <p class="bot-subtitle">{{ getCurrentStageDescription() }}</p>
      <div class="progress-indicator">
        <div class="progress-bar">
          <div class="progress-fill" :style="{ width: progressPercentage + '%' }"></div>
        </div>
        <span class="progress-text">{{ progressText }}</span>
      </div>
      <!-- <div class="reaction-buttons">
        <button class="thumbs-up" @click="provideFeedback('positive')">
          <font-awesome-icon :icon="['fas', 'thumbs-up']" />
        </button>
        <button class="thumbs-down" @click="provideFeedback('negative')">
          <font-awesome-icon :icon="['fas', 'thumbs-down']" />
        </button>
      </div> -->
    </div>

    <!-- Chat Messages Area -->
    <div ref="chatBodyEl" class="chat-body">
      <div class="timestamp">{{ getCurrentTime() }}</div>

      <!-- Messages -->
      <div v-for="(message, index) in messages" :key="index"
        :class="['message-container', message.type === 'bot' ? 'bot-message' : 'user-message']">
        <!-- <div v-if="message.type === 'bot'" class="bot-avatar-small">
          <img src="../assets/call.png" alt="Bot" />
        </div> -->
        <div class="message-bubble">
          <p v-html="formatMessage(message.text)"></p>
          <span class="message-time" v-if="message.time">{{ message.time }}</span>
        </div>
      </div>

      <!-- Typing Indicator -->
      <div v-if="isSubmitting" class="message-container bot-message typing-indicator-container">
        <div class="bot-avatar-small">
          <img src="@/assets/call.png" alt="Bot" />
        </div>
        <div class="typing-indicator">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>

      <!-- Emergency Escalation Notice -->
      <div v-if="showEmergencyEscalation" class="emergency-notice">
        <div class="emergency-icon">
          <FontAwesomeIcon :icon="['fas', 'exclamation-triangle']" />
        </div>
        <p>Connecting you to emergency support...</p>
      </div>

      <!-- Location Detection Buttons -->
      <div
        v-if="currentQuestion && (currentQuestion.id === 'reporter_country' || currentQuestion.id === 'victim_country')"
        class="location-options">
        <button @click="handleLocationDetection" class="location-button" :disabled="isSubmitting">
          <FontAwesomeIcon :icon="['fas', 'map-marker-alt']" />
          Use My Current Location
        </button>
        <p class="location-note">Or enter manually below</p>
      </div>

      <!-- Choice Options for Current Question -->
      <div v-if="currentQuestion && currentQuestion.type === 'choice' && chatStage === 'standard-questions'"
        class="quick-actions">
        <button v-for="option in currentQuestion.options" :key="option" @click.prevent="handleResponse(option)"
          class="action-button choice-button">
          {{ option }}
        </button>
      </div>

      <!-- Multiple Choice for Categories -->
      <div v-if="currentQuestion && currentQuestion.type === 'multiple_choice' && chatStage === 'standard-questions'"
        class="category-selection">
        <div class="category-grid">
          <div v-for="categoryGroup in currentQuestion.options" :key="categoryGroup.category" class="category-group">
            <h4 class="category-title">{{ categoryGroup.category }}</h4>
            <div class="subcategory-options">
              <label v-for="caseItem in categoryGroup.cases" :key="caseItem" class="checkbox-option">
                <input type="checkbox" :value="caseItem" v-model="selectedCategories" />
                <span class="checkmark"></span>
                <span class="option-text">{{ caseItem }}</span>
              </label>
            </div>
          </div>
        </div>
        <button v-if="selectedCategories.length > 0" @click="submitSelectedCategories" class="submit-categories-btn">
          Continue with {{ selectedCategories.length }} selected issue{{ selectedCategories.length > 1 ? 's' : '' }}
        </button>
      </div>

      <!-- File Upload Area -->
      <div v-if="currentQuestion && currentQuestion.type === 'file_upload' && chatStage === 'standard-questions'"
        class="file-upload-area">
        <div class="upload-zone" @drop="handleFileDrop" @dragover.prevent @dragenter.prevent>
          <FontAwesomeIcon :icon="['fas', 'cloud-upload-alt']" class="upload-icon" />
          <p>Drag and drop files here or click to browse</p>
          <p class="upload-hint">Maximum file size: 16MB each</p>
          <input type="file" ref="fileInput" @change="handleFileSelect" multiple
            accept="image/*,document/*,audio/*,video/*" class="file-input" />
          <button @click="$refs.fileInput.click()" class="browse-btn">Browse Files</button>
        </div>

        <!-- Uploaded Files Display -->
        <div v-if="uploadedFiles.length > 0" class="uploaded-files">
          <h5>Uploaded Files:</h5>
          <div v-for="(file, index) in uploadedFiles" :key="index" class="file-item">
            <FontAwesomeIcon :icon="getFileIcon(file.type)" class="file-icon" />
            <span class="file-name">{{ file.name }}</span>
            <span class="file-size">({{ formatFileSize(file.size) }})</span>
            <button @click="removeFile(index)" class="remove-file-btn">
              <FontAwesomeIcon :icon="['fas', 'times']" />
            </button>
          </div>
        </div>

        <button @click="skipFileUpload" class="skip-upload-btn">Skip and Continue</button>
      </div>
    </div>

    <!-- Chat Input Area -->
    <div class="chat-footer">
      <!-- Emergency Banner (if needed) -->
      <div v-if="showEmergencyBanner" class="emergency-banner">
        <FontAwesomeIcon :icon="['fas', 'phone']" />
        <span>For immediate emergency, call: +256-800-HELP</span>
      </div>

      <!-- Standard Text Input -->
      <form
        v-if="showTextInput && currentQuestion && !['end', 'emergency_escalation', 'multiple_choice', 'file_upload'].includes(currentQuestion.type)"
        @submit.prevent="handleSubmit">
        <div class="message-input-container">
          <textarea v-if="currentQuestion.type === 'textarea'" v-model="userInput"
            :placeholder="currentQuestion.placeholder || 'Share your story in detail...'" :disabled="isSubmitting"
            class="message-input textarea-input" rows="3"></textarea>

          <input v-else v-model="userInput" :type="getInputType(currentQuestion)"
            :placeholder="currentQuestion.placeholder || getPlaceholderText(currentQuestion)" :disabled="isSubmitting"
            class="message-input" />

          <div class="input-actions">
            <button type="button" class="attach-button" @click="toggleVoiceRecording"
              :class="{ 'recording': showRecording }">
              <FontAwesomeIcon :icon="showRecording ? ['fas', 'microphone-slash'] : ['fas', 'microphone']" />
            </button>
            <button type="submit" class="send-button" :disabled="isSubmitting || !isInputValid">
              <font-awesome-icon :icon="['fas', 'paper-plane']" />
            </button>
          </div>
        </div>

        <!-- Skip Button -->
        <div v-if="showSkipButton" class="skip-button-container">
          <button type="button" @click="handleSkip" class="skip-button" :disabled="isSubmitting">
            <FontAwesomeIcon :icon="['fas', 'forward']" />
            Skip this question
          </button>
        </div>

        <!-- Validation Error Display -->
        <div v-if="validationError" class="validation-error">
          <FontAwesomeIcon :icon="['fas', 'exclamation-circle']" />
          {{ validationError }}
        </div>

        <!-- Input Hints -->
        <div v-if="getInputHint(currentQuestion)" class="input-hint">
          <FontAwesomeIcon :icon="['fas', 'info-circle']" />
          {{ getInputHint(currentQuestion) }}
        </div>

        <!-- Voice Recording Component -->
        <div class="other-inputs" v-if="showRecording">
          <VoiceCapture @capturedText="handleCapturedText" @recordingComplete="handleRecordingComplete" />
        </div>
      </form>

      <!-- Completion Screen -->
      <div v-else-if="currentQuestion && currentQuestion.type === 'end'" class="completion-message">
        <div class="completion-icon">
          <FontAwesomeIcon :icon="['fas', 'check-circle']" />
        </div>
        <h3>Report Submitted Successfully</h3>
        <p>{{ currentQuestion.question }}</p>
        <div class="completion-actions">
          <!-- <button @click="downloadReport" class="download-btn">
            <FontAwesomeIcon :icon="['fas', 'download']" />
            Download Copy
          </button> -->
          <button @click="restartConversation" class="restart-btn">
            <FontAwesomeIcon :icon="['fas', 'plus']" />
            New complaint
          </button>
        </div>
      </div>

      <!-- Anonymous Support Options -->
      <div v-else-if="currentQuestion && currentQuestion.id === 'anonymous_support'" class="anonymous-options">
        <div class="support-grid">
          <div class="support-option" @click="accessResources">
            <FontAwesomeIcon :icon="['fas', 'book']" />
            <span>Access Resources</span>
          </div>
          <div class="support-option" @click="liveChat">
            <FontAwesomeIcon :icon="['fas', 'comments']" />
            <span>Live Chat</span>
          </div>
          <div class="support-option" @click="contactInfo">
            <FontAwesomeIcon :icon="['fas', 'phone']" />
            <span>Contact Information</span>
          </div>
        </div>
      </div>

      <!-- Footer Info -->
      <div class="footer-info">
        <span class="privacy-notice">🔒 Your information is confidential and secure</span>
      </div>
    </div>
  </div>
</template>
<script setup>
  /* eslint-disable */
  import { ref, computed, onMounted, onBeforeUnmount, watch, nextTick, defineProps, defineEmits, defineAsyncComponent, h } from "vue";
  import { useRouter } from 'vue-router';
  import apiClient from "@/utils/giz-axios.js";

  // Import MGLSD questions
  import mglsdQuestions from "@/utils/mglsd-questions.js";
  const VoiceCapture = defineAsyncComponent(() =>
    import("@/components/giz/VoiceCapture.vue").catch(error => {
      console.error("Failed to load VoiceCapture:", error);
      return {
        render() {
          return h('div', 'Voice capture unavailable');
        }
      };
    })
  );

  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
  import {
    faMaximize, faMicrophone, faMicrophoneSlash, faMinus, faXmark, faPaperPlane,
    faThumbsUp, faThumbsDown, faArrowLeft, faExclamationTriangle, faCloudUploadAlt,
    faTimes, faPhone, faExclamationCircle, faInfoCircle, faCheckCircle, faDownload,
    faPlus, faBook, faComments, faFileAlt, faFileImage, faFileVideo, faFileAudio,
    faForward, faMapMarkerAlt
  } from '@fortawesome/free-solid-svg-icons';

  // Register the icons
  import { library } from '@fortawesome/fontawesome-svg-core';
  library.add(
    faMaximize, faMicrophone, faMicrophoneSlash, faMinus, faXmark, faPaperPlane,
    faThumbsUp, faThumbsDown, faArrowLeft, faExclamationTriangle, faCloudUploadAlt,
    faTimes, faPhone, faExclamationCircle, faInfoCircle, faCheckCircle, faDownload,
    faPlus, faBook, faComments, faFileAlt, faFileImage, faFileVideo, faFileAudio,
    faForward, faMapMarkerAlt
  );

  // Props and emits
  const props = defineProps({
    minimized: Boolean
  });

  const emit = defineEmits(["closeChat", "minimizeChat", "maximizeChat"]);

  // State variables
  const messages = ref([]);
  const userInput = ref("");
  const isSubmitting = ref(false);
  const showRecording = ref(false);
  const responses = ref({});
  const currentStep = ref("opening_message");
  const chatBodyEl = ref(null);
  const validationError = ref("");
  const chatStage = ref('standard-questions');
  const selectedCategories = ref([]);
  const uploadedFiles = ref([]);
  const showEmergencyEscalation = ref(false);
  const showEmergencyBanner = ref(false);
  const navigationHistory = ref([]);
  const fileInput = ref(null);

  // Router
  const router = useRouter();

  // Button handlers
  const minimizeChat = () => emit("minimizeChat");
  const maximizeChat = () => emit("maximizeChat");
  const closeChat = () => emit("closeChat");

  // Helper functions
  const getCurrentTime = () => {
    const now = new Date();
    return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  const getCurrentStageDescription = () => {
    if (!currentQuestion.value) return "Loading...";

    const stageDescriptions = {
      'opening_message': 'Welcome',
      'reporting_for_who': 'Information Collection',
      'reporter_names': 'Your Information',
      'victim_names': 'Victim Information',
      'job_title_self': 'Employment Details',
      'job_title_other': 'Employment Details',
      'perpetrator_names_self': 'Incident Details',
      'perpetrator_names_other': 'Incident Details',
      'complaint_categories': 'Issue Categories',
      'complaint_narrative': 'Your Story',
      'evidence_upload': 'Evidence Upload',
      'contact_preference': 'Contact Preferences'
    };

    return stageDescriptions[currentStep.value] || 'Information Collection';
  };

  const formatMessage = (text) => {
    return text.replace(/\n/g, '<br>');
  };

  const getInputType = (question) => {
    if (!question.validation) return 'text';

    // Check for date pattern first (specific to your DD/MM/YYYY format)
    if (question.validation.pattern &&
      (question.validation.pattern.includes('(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])') ||
        question.id.includes('dob') ||
        question.placeholder === '15/01/1990')) {
      return 'text'; // Date patterns should always use text input
    }

    // Check for pure number pattern (only digits, no special characters)
    if (question.validation.pattern === '^\\d+') return 'number';

    // Check for email pattern
    if (question.validation.pattern && question.validation.pattern.includes('@')) return 'email';

    // Check for phone pattern  
    if (question.validation.pattern && question.validation.pattern.includes('[+]')) return 'tel';

    // Default to text for everything else
    return 'text';
  };

  const getPlaceholderText = (question) => {
    // Use the placeholder from the question if it exists
    if (question.placeholder) {
      return question.placeholder;
    }

    const placeholders = {
      'reporter_names': 'surname, given names',
      'victim_names': 'surname, given names',
      'perpetrator_names_self': 'surname, given names',
      'perpetrator_names_other': 'surname, given names',
      'reporter_location': 'street, village, district, country',
      'victim_location': 'street, village, district, country',
      'work_location_self': 'street, village, district, country',
      'work_location_other': 'street, village, district, country',
      'perpetrator_location_self': 'street, village, district, country',
      'perpetrator_location_other': 'street, village, district, country',
      'job_title_self': 'e.g., Domestic Worker, Security Guard',
      'job_title_other': 'e.g., Domestic Worker, Security Guard',
      'employer_name_self': 'Company or employer name',
      'employer_name_other': 'Company or employer name',
      'employer_phone_self': '+256...',
      'employer_phone_other': '+256...',
      'employer_email_self': 'employer@company.com',
      'employer_email_other': 'employer@company.com',
      'complaint_narrative': 'Describe what happened in detail...'
    };
    return placeholders[question.id] || 'Type your response...';
  };

  const getInputHint = (question) => {
    const hints = {
      'employer_phone_self': 'Include country code if available',
      'employer_phone_other': 'Include country code if available',
      'complaint_narrative': 'Include dates, times, and specific details',
      'evidence_upload': 'Accepted formats: Images, Documents, Audio, Video'
    };
    return hints[question.id] || '';
  };

  const getFileIcon = (fileType) => {
    if (fileType.startsWith('image/')) return ['fas', 'file-image'];
    if (fileType.startsWith('video/')) return ['fas', 'file-video'];
    if (fileType.startsWith('audio/')) return ['fas', 'file-audio'];
    return ['fas', 'file-alt'];
  };

  const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  // Date validation function
  const validateDateFormat = (dateString) => {
    const dateRegex = /^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/\d{4}$/;

    if (!dateRegex.test(dateString)) {
      return false;
    }

    // Additional validation for actual date validity
    const parts = dateString.split('/');
    const day = parseInt(parts[0], 10);
    const month = parseInt(parts[1], 10);
    const year = parseInt(parts[2], 10);

    const date = new Date(year, month - 1, day);

    return date.getFullYear() === year &&
      date.getMonth() === month - 1 &&
      date.getDate() === day;
  };

  // Clean data function to replace "SKIPPED" with empty strings
  const cleanSkippedData = (data) => {
    const cleanedData = {};

    for (const [key, value] of Object.entries(data)) {
      if (value === "SKIPPED") {
        cleanedData[key] = "";
      } else if (Array.isArray(value)) {
        cleanedData[key] = value.filter(item => item !== "SKIPPED");
      } else {
        cleanedData[key] = value;
      }
    }

    return cleanedData;
  };

  // Computed properties
  const currentQuestion = computed(() => {
    const question = mglsdQuestions.find(q => q.id === currentStep.value);
    if (!question) {
      console.error(`Question with ID "${currentStep.value}" not found in mglsdQuestions`);
      console.log('Available questions:', mglsdQuestions.map(q => q.id));
      console.log('Current step:', currentStep.value);
      return {
        id: "error",
        question: "Sorry, there was an error. Please restart the conversation.",
        type: "end"
      };
    }

    console.log('Current question:', {
      id: question.id,
      type: question.type,
      hasOptions: !!question.options,
      hasNext: !!question.next,
      next: question.next,
      allowSkip: question.allowSkip
    });

    return question;
  });

  const showTextInput = computed(() => {
    if (!currentQuestion.value) return false;

    // Show text input for text, textarea, number, email, tel types
    const textInputTypes = ['text', 'textarea', 'email', 'tel', 'number'];
    const excludedTypes = ['end', 'multiple_choice', 'file_upload', 'choice', 'info'];

    // If it's explicitly a text input type, show it
    if (textInputTypes.includes(currentQuestion.value.type)) {
      return true;
    }

    // If it's not excluded and not a choice, show text input (default behavior)
    if (!excludedTypes.includes(currentQuestion.value.type)) {
      return true;
    }

    return false;
  });

  const showSkipButton = computed(() => {
    return currentQuestion.value && currentQuestion.value.allowSkip === true;
  });

  const isInputValid = computed(() => {
    // Ensure userInput.value is a string before calling trim
    const inputValue = userInput.value;

    // Handle null, undefined, or non-string values
    if (inputValue === null || inputValue === undefined) {
      return false;
    }

    // Convert to string if it's a number
    const stringValue = String(inputValue);

    if (!stringValue.trim()) {
      return false;
    }

    if (!currentQuestion.value || !currentQuestion.value.validation) {
      return true;
    }

    const { required, min_length } = currentQuestion.value.validation;

    if (required && !stringValue.trim()) {
      return false;
    }

    if (min_length && stringValue.length < min_length) {
      return false;
    }

    return true;
  });

  const progressPercentage = computed(() => {
    const totalSteps = mglsdQuestions.filter(q => q.type !== 'info' && q.type !== 'end').length;
    const currentIndex = mglsdQuestions.findIndex(q => q.id === currentStep.value);
    return Math.min((currentIndex / totalSteps) * 100, 100);
  });

  const progressText = computed(() => {
    const currentIndex = mglsdQuestions.findIndex(q => q.id === currentStep.value);
    const totalSteps = mglsdQuestions.filter(q => q.type !== 'info' && q.type !== 'end').length;
    return `Step ${Math.max(currentIndex, 1)} of ${totalSteps}`;
  });

  const canGoBack = computed(() => {
    return navigationHistory.value.length > 0 && currentStep.value !== 'opening_message';
  });

  // Core functionality
  const scrollToBottom = () => {
    if (chatBodyEl.value) {
      chatBodyEl.value.scrollTop = chatBodyEl.value.scrollHeight;
    }

    nextTick(() => {
      if (chatBodyEl.value) {
        chatBodyEl.value.scrollTop = chatBodyEl.value.scrollHeight;
        setTimeout(() => {
          if (chatBodyEl.value) {
            chatBodyEl.value.scrollTop = chatBodyEl.value.scrollHeight;
          }
        }, 100);
      }
    });
  };

  const moveToNextStep = (nextStepId) => {
    console.log('Moving to next step:', nextStepId);
    console.log('Current responses:', responses.value);

    // Verify the next step exists
    const nextQuestion = mglsdQuestions.find(q => q.id === nextStepId);
    if (!nextQuestion) {
      console.error(`Next step "${nextStepId}" not found in questions array`);
      console.log('Available question IDs:', mglsdQuestions.map(q => q.id));
      return;
    }

    // Add current step to navigation history
    if (currentStep.value !== nextStepId) {
      navigationHistory.value.push(currentStep.value);
    }

    // Update current step
    currentStep.value = nextStepId;

    // Save to localStorage
    responses.value.currentStep = nextStepId;
    localStorage.setItem("mglsd_responses", JSON.stringify(responses.value));
    localStorage.setItem("mglsd_navigation_history", JSON.stringify(navigationHistory.value));

    // Don't auto-submit unless we're actually at the final message
    if (nextStepId === 'final_message') {
      // Add the final message first
      setTimeout(() => {
        messages.value.push({
          text: nextQuestion.question,
          type: "bot",
          time: getCurrentTime()
        });
        scrollToBottom();

        // Then submit after showing the final message
        setTimeout(() => {
          sendToServer(responses.value);
        }, 2000);
      }, 500);
      return;
    }

    // Add bot message for regular questions
    if (nextQuestion && !['end'].includes(nextQuestion.type)) {
      setTimeout(() => {
        messages.value.push({
          text: nextQuestion.question,
          type: "bot",
          time: getCurrentTime()
        });
        scrollToBottom();

        // Auto-focus input for text questions
        focusInput();
      }, 500);
    }
  };

  // Clear all cache function
  const clearAllCache = () => {
    try {
      // Clear localStorage items
      localStorage.removeItem("mglsd_responses");
      localStorage.removeItem("mglsd_navigation_history");

      // Clear sessionStorage items (if any)
      sessionStorage.removeItem("mglsd_responses");
      sessionStorage.removeItem("mglsd_navigation_history");

      // Clear any other related cache items
      localStorage.removeItem("responses"); // Old format
      localStorage.removeItem("navigation_history"); // Old format

      console.log("Cache cleared successfully");
    } catch (error) {
      console.error("Error clearing cache:", error);
    }
  };

  // Clear cache on page reload/refresh
  const handlePageReload = () => {
    clearAllCache();
  };

  const initializeChat = () => {
    // Clear cache on fresh load (when tab is reloaded)
    const isPageReload = performance.navigation?.type === 1 ||
      performance.getEntriesByType('navigation')[0]?.type === 'reload';

    if (isPageReload) {
      console.log("Page reload detected - clearing cache");
      clearAllCache();
    }

    try {
      const savedResponses = localStorage.getItem("mglsd_responses");
      if (savedResponses && !isPageReload) {
        responses.value = JSON.parse(savedResponses);
        currentStep.value = responses.value.currentStep || "opening_message";

        const savedHistory = localStorage.getItem("mglsd_navigation_history");
        if (savedHistory) {
          navigationHistory.value = JSON.parse(savedHistory);
        }
      } else {
        responses.value = {};
        currentStep.value = "opening_message";
      }
    } catch (error) {
      console.error("Failed to load stored responses:", error);
      clearAllCache();
      responses.value = {};
      currentStep.value = "opening_message";
    }

    // Add opening message if no messages exist
    if (messages.value.length === 0) {
      const openingQuestion = mglsdQuestions.find(q => q.id === currentStep.value);
      if (openingQuestion) {
        messages.value.push({
          text: openingQuestion.question,
          type: "bot",
          time: getCurrentTime()
        });
      }
    }

    scrollToBottom();
    focusInput();
  };

  const validateInput = (input) => {
    if (!currentQuestion.value || !currentQuestion.value.validation) return "";

    // Ensure input is a string
    const stringInput = String(input || '');

    const { required, min_length, max_length, pattern, min, max, error_message } = currentQuestion.value.validation;

    if (required && !stringInput.trim()) {
      return "This field is required";
    }

    if (min_length && stringInput.length < min_length) {
      return `Please enter at least ${min_length} characters`;
    }

    if (max_length && stringInput.length > max_length) {
      return `Please enter no more than ${max_length} characters`;
    }

    if (pattern) {
      // Special handling for date validation
      if (pattern === "^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\\d{4}$") {
        console.log('Validating date format:', stringInput);
        if (!validateDateFormat(stringInput)) {
          return error_message || "Please enter date in DD/MM/YYYY format (e.g., 15/01/1990)";
        }
      } else {
        const regex = new RegExp(pattern);
        if (!regex.test(stringInput)) {
          if (pattern === "^\\d+$") return "Please enter a valid number";
          if (pattern.includes('@')) return "Please enter a valid email address";
          if (pattern.includes('[+]')) return "Please enter a valid phone number";
          return error_message || "Invalid format";
        }
      }
    }

    // For numeric validations, convert to number
    const numericInput = parseFloat(stringInput);

    if (min !== undefined && numericInput < min) {
      return `Value must be at least ${min}`;
    }

    if (max !== undefined && numericInput > max) {
      return `Value must be no more than ${max}`;
    }

    return "";
  };

  const handleSubmit = () => {
    // Ensure userInput.value is a string
    const inputValue = userInput.value;
    console.log('Handling submit for input:', inputValue, 'at step:', currentStep.value);
    if (inputValue === null || inputValue === undefined) {
      return;
    }

    // Convert to string and trim
    const stringValue = String(inputValue).trim();

    if (!stringValue) {
      return;
    }

    validationError.value = validateInput(stringValue);
    if (validationError.value) return;

    handleResponse(stringValue);
    userInput.value = "";
  };

  const handleResponse = (input) => {
    console.log('Handling response:', input, 'for step:', currentStep.value);
    console.log('Current question:', currentQuestion.value);

    validationError.value = "";

    // Add user message to chat
    messages.value.push({
      text: input,
      type: "user",
      time: getCurrentTime()
    });

    // Store response
    responses.value[currentStep.value] = input;
    // Logic check handled dynamically by handleInfoQuestion

    // Determine next step based on question type
    let nextStep;

    if (currentQuestion.value.type === "choice" && currentQuestion.value.next) {
      nextStep = currentQuestion.value.next[input];
      console.log('Choice mapping:', currentQuestion.value.next);
      console.log('Selected choice:', input);
      console.log('Mapped next step:', nextStep);

      if (!nextStep) {
        console.error(`No next step defined for choice "${input}" in question "${currentStep.value}"`);
        console.log('Available choices:', Object.keys(currentQuestion.value.next));
        return;
      }
    } else if (currentQuestion.value.next) {
      nextStep = currentQuestion.value.next;
      console.log('Direct next step:', nextStep);
    } else {
      console.error(`No next step defined for question "${currentStep.value}"`);
      console.log('Question object:', currentQuestion.value);
      return;
    }

    console.log('Final next step determined:', nextStep);

    // Show processing indicator
    isSubmitting.value = true;
    setTimeout(() => {
      isSubmitting.value = false;

      // Verify next step exists
      const nextQuestionExists = mglsdQuestions.some(q => q.id === nextStep);
      if (!nextQuestionExists) {
        console.error(`Next step "${nextStep}" does not exist in questions array`);
        console.log('Available questions:', mglsdQuestions.map(q => q.id));
        return;
      }

      moveToNextStep(nextStep);
    }, 800);
  };

  // Skip question functionality
  const handleSkip = () => {
    console.log('Skipping question:', currentStep.value);

    // Add skip message to chat
    messages.value.push({
      text: "Skipped",
      type: "user",
      time: getCurrentTime()
    });

    // Store skip response
    responses.value[currentStep.value] = "SKIPPED";

    // Get next step
    const nextStep = currentQuestion.value.next;

    if (!nextStep) {
      console.error(`No next step defined for skippable question "${currentStep.value}"`);
      return;
    }

    // Show processing indicator
    isSubmitting.value = true;
    setTimeout(() => {
      isSubmitting.value = false;
      moveToNextStep(nextStep);
    }, 600);
  };

  // Handle logic check for info questions and branching
  const handleInfoQuestion = () => {
    if (currentQuestion.value && currentQuestion.value.type === 'info') {
      setTimeout(() => {
        const nextStep = currentQuestion.value.next;
        if (nextStep) {
          moveToNextStep(nextStep);
        }
      }, 2000); // Give user time to read the info message
    }

    // Handle logic check questions (for branching after reporter details)
    if (currentQuestion.value && currentQuestion.value.type === 'logic_check') {
      const nextStep = currentQuestion.value.next(responses.value);
      if (nextStep) {
        setTimeout(() => {
          moveToNextStep(nextStep);
        }, 100);
      }
    }
  };

  // Category selection for multiple choice
  const submitSelectedCategories = () => {
    if (selectedCategories.value.length === 0) return;

    const categoriesText = selectedCategories.value.join(', ');
    responses.value.complaint_categories = selectedCategories.value;

    messages.value.push({
      text: `Selected issues: ${categoriesText}`,
      type: "user",
      time: getCurrentTime()
    });

    isSubmitting.value = true;

    setTimeout(() => {
      isSubmitting.value = false;
      const nextStep = currentQuestion.value.next;
      moveToNextStep(nextStep);
    }, 600);
  };

  // File handling - UPDATED with auto-progression
  const handleFileDrop = (event) => {
    event.preventDefault();
    const files = Array.from(event.dataTransfer.files);
    processFiles(files);
  };

  const handleFileSelect = (event) => {
    const files = Array.from(event.target.files);
    processFiles(files);
  };

  const processFiles = (files) => {
    const maxSize = 16 * 1024 * 1024; // 16MB
    const validFiles = [];

    files.forEach(file => {
      if (file.size > maxSize) {
        validationError.value = `File "${file.name}" is too large. Maximum size is 16MB.`;
        return;
      }
      validFiles.push(file);
    });

    uploadedFiles.value.push(...validFiles);

    if (validFiles.length > 0) {
      validationError.value = "";

      // AUTO-PROGRESSION: Move to next step automatically after file upload
      setTimeout(() => {
        responses.value.evidence_upload = uploadedFiles.value.map(f => ({
          name: f.name,
          size: f.size,
          type: f.type
        }));

        messages.value.push({
          text: `Uploaded ${validFiles.length} file${validFiles.length > 1 ? 's' : ''}`,
          type: "user",
          time: getCurrentTime()
        });

        const nextStep = currentQuestion.value.next;
        moveToNextStep(nextStep);
      }, 1000);
    }
  };

  const removeFile = (index) => {
    uploadedFiles.value.splice(index, 1);
  };

  const skipFileUpload = () => {
    responses.value.evidence_upload = "SKIPPED";

    messages.value.push({
      text: "Skipped file upload",
      type: "user",
      time: getCurrentTime()
    });

    const nextStep = currentQuestion.value.next;
    moveToNextStep(nextStep);
  };

  // Navigation
  const goBack = () => {
    if (navigationHistory.value.length > 0) {
      const previousStep = navigationHistory.value.pop();
      currentStep.value = previousStep;

      localStorage.setItem("mglsd_navigation_history", JSON.stringify(navigationHistory.value));
      localStorage.setItem("mglsd_responses", JSON.stringify(responses.value));
      focusInput();
    }
  };

  // Voice and other handlers
  const toggleVoiceRecording = () => {
    showRecording.value = !showRecording.value;
  };

  const handleCapturedText = (text) => {
    userInput.value = text;
    showRecording.value = false;
  };

  const handleRecordingComplete = (audioBlob) => {
    console.log("Recording complete:", audioBlob);
    showRecording.value = false;
  };

  const restartConversation = () => {
    clearAllCache();

    responses.value = {};
    messages.value = [];
    selectedCategories.value = [];
    uploadedFiles.value = [];
    navigationHistory.value = [];
    currentStep.value = "opening_message";
    showEmergencyEscalation.value = false;
    showEmergencyBanner.value = false;

    const openingQuestion = mglsdQuestions.find(q => q.id === currentStep.value);
    if (openingQuestion) {
      messages.value.push({
        text: openingQuestion.question,
        type: "bot",
        time: getCurrentTime()
      });
    }

    nextTick(() => scrollToBottom());
  };

  // Anonymous support options
  const accessResources = () => {
    console.log("Accessing resources");
  };

  const liveChat = () => {
    console.log("Connecting to live chat");
  };

  const contactInfo = () => {
    console.log("Showing contact info");
  };

  // UUID generator
  const generateUUID = () => {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
      const r = Math.random() * 16 | 0;
      const v = c === 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  };

  // Helper functions for API mapping
  const determineAgeGroupId = (age) => {
    if (!age || age === "SKIPPED") return "361953";
    const ageNum = parseInt(age);
    if (ageNum <= 18) return "361952";
    if (ageNum <= 30) return "361953";
    if (ageNum <= 45) return "361955";
    if (ageNum <= 60) return "361956";
    return "361957"; // 60+
  };

  // Updated geolocation function for Vue CLI (Webpack)
  const getCurrentLocation = () => {
    return new Promise((resolve, reject) => {
      if (!navigator.geolocation) {
        reject(new Error('Geolocation is not supported by this browser'));
        return;
      }

      navigator.geolocation.getCurrentPosition(
        async (position) => {
          const { latitude, longitude } = position.coords;

          try {
            // Get API key from environment variable (Vue CLI/Webpack syntax)
            const apiKey = process.env.VUE_APP_OPENCAGE_API_KEY;

            if (!apiKey) {
              reject(new Error('API key not configured. Please add VUE_APP_OPENCAGE_API_KEY to your .env file'));
              return;
            }

            // Reverse geocoding to get readable address
            const response = await fetch(
              `https://api.opencagedata.com/geocode/v1/json?q=${latitude}+${longitude}&key=${apiKey}&limit=1&no_annotations=1`
            );

            if (!response.ok) {
              throw new Error(`Geocoding API error: ${response.status}`);
            }

            const data = await response.json();

            if (data.results && data.results.length > 0) {
              const result = data.results[0];
              const components = result.components;

              // Format as: street, village, district, country
              const street = components.road || components.neighbourhood || components.suburb || '';
              const village = components.village || components.town || components.city || '';
              const district = components.county || components.state_district || components.state || '';
              const country = components.country || '';

              const formattedLocation = [street, village, district, country]
                .filter(Boolean)
                .join(', ');

              resolve({
                formatted: formattedLocation,
                street: street,
                village: village,
                district: district,
                country: country,
                fullAddress: result.formatted || '',
                coordinates: {
                  latitude: latitude,
                  longitude: longitude
                }
              });
            } else {
              reject(new Error('Could not get address from coordinates'));
            }
          } catch (error) {
            console.error('Geocoding error:', error);
            reject(new Error('Failed to get address details: ' + error.message));
          }
        },
        (error) => {
          let errorMessage = 'Location access denied';
          switch (error.code) {
            case 1:
              errorMessage = 'Location access denied by user';
              break;
            case 2:
              errorMessage = 'Location information unavailable';
              break;
            case 3:
              errorMessage = 'Location request timeout';
              break;
            default:
              errorMessage = 'Unknown location error';
          }
          console.error('Geolocation error:', error);
          reject(new Error(errorMessage));
        },
        {
          enableHighAccuracy: true,
          timeout: 15000, // 15 seconds timeout
          maximumAge: 300000 // 5 minutes cache
        }
      );
    });
  };

  // Function to handle location detection
  const handleLocationDetection = async () => {
    validationError.value = "";
    isSubmitting.value = true;

    // Debug: Check if env var is loaded
    console.log('API Key loaded:', process.env.VUE_APP_OPENCAGE_API_KEY ? 'Yes' : 'No');

    // Show loading message
    messages.value.push({
      text: "📍 Detecting your location...",
      type: "bot",
      time: getCurrentTime()
    });

    try {
      const location = await getCurrentLocation();

      // Auto-fill based on current question - only for reporter and victim locations
      if (currentStep.value === 'reporter_location') {
        responses.value.reporter_location = location.formatted;

        // Show success message
        messages.value.push({
          text: `📍 Location detected: ${location.formatted}`,
          type: "user",
          time: getCurrentTime()
        });

        // Auto-advance to next step
        setTimeout(() => {
          isSubmitting.value = false;
          moveToNextStep('check_reporting_type_for_passport');
        }, 1500);

      } else if (currentStep.value === 'victim_location') {
        responses.value.victim_location = location.formatted;

        // Show success message
        messages.value.push({
          text: `📍 Victim location detected: ${location.formatted}`,
          type: "user",
          time: getCurrentTime()
        });

        setTimeout(() => {
          isSubmitting.value = false;
          moveToNextStep('victim_passport');
        }, 1500);
      }

    } catch (error) {
      console.error('Location detection failed:', error);
      isSubmitting.value = false;

      // Show error message
      messages.value.push({
        text: `⚠️ ${error.message}`,
        type: "bot",
        time: getCurrentTime()
      });

      validationError.value = error.message + " Please enter your location manually below.";

      // Clear the loading message after a short delay
      setTimeout(() => {
        validationError.value = "";
      }, 5000);
    }
  };

  // Add this new function after your existing helper functions
  const focusInput = () => {
    nextTick(() => {
      // Small delay to let the question appear first
      setTimeout(() => {
        const inputElement = document.querySelector('.message-input');
        if (inputElement && showTextInput.value) {
          inputElement.focus();
        }
      }, 100); // 100ms delay so user sees the question first
    });
  };

  const determineGenderId = (gender) => {
    if (!gender || gender === "SKIPPED") return "";
    const genderLower = gender.toLowerCase();
    if (genderLower.includes("female") || genderLower === "f") return "120";
    if (genderLower.includes("male") || genderLower === "m") return "121";
    return "";
  };

  const determineGenderLabel = (gender) => {
    if (!gender || gender === "SKIPPED") return "";
    const genderLower = gender.toLowerCase();
    if (genderLower.includes("female") || genderLower === "f") return "^Female";
    if (genderLower.includes("male") || genderLower === "m") return "^Male";
    return "";
  };

  // Helper to determine if self-reporting or reporting for someone else
  const isSelfReporting = (data) => {
    return data.reporter_role === "I am the person affected (Victim/Worker)";
  };

  // Parse names function to split the single names field
  const parseNames = (namesString) => {
    if (!namesString || namesString === "SKIPPED") {
      return { surname: "", givenNames: "" };
    }

    // Split by comma and trim whitespace
    const parts = namesString.split(',').map(part => part.trim());

    if (parts.length >= 2) {
      return {
        surname: parts[0] || "",
        givenNames: parts.slice(1).join(' ') || ""
      };
    } else {
      // If no comma, treat the whole string as given names
      return {
        surname: "",
        givenNames: namesString.trim()
      };
    }
  };

  // Parse location function to split the single location field
  const parseLocation = (locationString) => {
    if (!locationString || locationString === "SKIPPED") {
      return { street: "", village: "", district: "", country: "" };
    }

    // Split by comma and trim whitespace
    const parts = locationString.split(',').map(part => part.trim());

    return {
      street: parts[0] || "",
      village: parts[1] || "",
      district: parts[2] || "",
      country: parts[3] || ""
    };
  };

  // Get victim data based on reporting type
  const getVictimData = (data) => {
    if (isSelfReporting(data)) {
      // Reporter is the victim - use reporter data
      const reporterNames = parseNames(data.reporter_names);
      const reporterLocation = parseLocation(data.reporter_location);

      return {
        "fname": reporterNames.givenNames || "",
        "age_t": "0",
        "age": "", // No age field in new structure
        "dob": data.reporter_dob || "",
        "age_group_id": "361953", // Default age group since no age
        "location_id": "258783", // Default location ID
        "sex_id": determineGenderId(data.reporter_sex),
        "landmark": reporterLocation.street || "",
        "nationality_id": "",
        "national_id_type_id": "",
        "national_id": data.reporter_passport || "",
        "lang_id": "",
        "tribe_id": "",
        "phone": data.contact_phone_also || data.contact_whatsapp || "",
        "phone2": "",
        "email": data.contact_email_also || data.contact_email || "",
        "other_names": reporterNames.surname || "",
        "middle_name": "",
        ".id": "86164"
      };
    } else {
      // Someone else is the victim - use victim data
      const victimNames = parseNames(data.victim_names);
      const victimLocation = parseLocation(data.victim_location);

      return {
        "fname": victimNames.givenNames || "",
        "age_t": "0",
        "age": "", // No age field in new structure
        "dob": data.victim_dob || "",
        "age_group_id": "361953", // Default age group since no age
        "location_id": "258783", // Default location ID
        "sex_id": determineGenderId(data.victim_sex),
        "landmark": victimLocation.street || "",
        "nationality_id": "",
        "national_id_type_id": "",
        "national_id": data.victim_passport || "",
        "lang_id": "",
        "tribe_id": "",
        "phone": "",
        "phone2": "",
        "email": "",
        "other_names": victimNames.surname || "",
        "middle_name": "",
        ".id": "86164"
      };
    }
  };

  // Get reporter data (person making the report)
  const getReporterData = (data) => {
    const reporterNames = parseNames(data.reporter_names);
    const reporterLocation = parseLocation(data.reporter_location);

    return {
      "fname": reporterNames.givenNames || "",
      "age_t": "0",
      "age": "", // No age field in new structure
      "dob": data.reporter_dob || "",
      "age_group_id": "361953", // Default age group since no age
      "location_id": "258783", // Default location ID
      "sex_id": determineGenderId(data.reporter_sex),
      "landmark": reporterLocation.street || "",
      "nationality_id": "",
      "national_id_type_id": "",
      "national_id": data.reporter_passport || "",
      "lang_id": "",
      "tribe_id": "",
      "phone": data.contact_phone_also || data.contact_whatsapp || "",
      "phone2": "",
      "email": data.contact_email_also || data.contact_email || "",
      "other_names": reporterNames.surname || "",
      "middle_name": "",
      ".id": "86164"
    };
  };

  // Get perpetrator data
  const getPerpetratorData = (data) => {
    const isSelf = isSelfReporting(data);
    const prefix = isSelf ? "_self" : "_other";

    const perpetratorNames = parseNames(data[`perpetrator_names${prefix}`]);
    const perpetratorLocation = parseLocation(data[`perpetrator_location${prefix}`]);

    return {
      "fname": perpetratorNames.givenNames || "",
      "age_t": "0",
      "age": "", // No age field in new structure
      "age_group": "", // No age field in new structure
      "dob": "",
      "age_group_id": "361953", // Default age group since no age
      "location_id": "",
      "sex_id": determineGenderId(data[`perpetrator_sex${prefix}`]),
      "sex": determineGenderLabel(data[`perpetrator_sex${prefix}`]),
      "landmark": perpetratorLocation.street || "",
      "nationality_id": "",
      "national_id_type_id": "",
      "national_id": "",
      "lang_id": "",
      "tribe_id": "",
      "phone": "",
      "phone2": "",
      "email": "",
      "relationship_id": "3556", // Default relationship ID
      "relationship": data[`perpetrator_relationship${prefix}`] || "",
      "shareshome_id": "",
      "health_id": "",
      "employment_id": "",
      "marital_id": "",
      "guardian_fullname": "",
      "notes": [
        data[`perpetrator_profession${prefix}`] ? `Profession: ${data[`perpetrator_profession${prefix}`]}` : "",
        perpetratorNames.surname ? `Surname: ${perpetratorNames.surname}` : "",
        perpetratorLocation.village ? `Village: ${perpetratorLocation.village}` : "",
        perpetratorLocation.district ? `District: ${perpetratorLocation.district}` : "",
        perpetratorLocation.country ? `Country: ${perpetratorLocation.country}` : ""
      ].filter(Boolean).join(". ") || "",
      "other_names": perpetratorNames.surname || "",
      "middle_name": "",
      ".id": ""
    };
  };

  // Get employment data
  const getEmploymentData = (data) => {
    const isSelf = isSelfReporting(data);
    const prefix = isSelf ? "_self" : "_other";

    const workLocation = parseLocation(data[`work_location${prefix}`]);

    return {
      "job_title": data[`job_title${prefix}`] || "",
      "employer_type": data[`employer_type${prefix}`] || "",
      "employer_name": data[`employer_name${prefix}`] || "",
      "employer_phone": data[`employer_phone${prefix}`] || "",
      "employer_email": data[`employer_email${prefix}`] || "",
      "work_country": workLocation.country || "",
      "work_town": workLocation.village || "",
      "work_street": workLocation.street || "",
      "work_district": workLocation.district || ""
    };
  };

  // Get all contact methods
  const getAllContactMethods = (data) => {
    return {
      "primary_method": data.contact_preference || "",
      "whatsapp": data.contact_whatsapp || data.contact_whatsapp_also || "",
      "email": data.contact_email || data.contact_email_also || "",
      "phone": data.contact_phone_also || "",
      "safe_time": data.safe_contact_time || ""
    };
  };

  // Helper to map specific categories to backend Report.Category choices
  const mapCategoryToBackend = (categories) => {
    if (!categories || categories.length === 0) return 'MIGRANT'; // Default

    const primary = categories[0];

    if (primary.includes('Sexual') || primary.includes('Rape') || primary.includes('Defilement')) {
      return 'GBV'; // Gender-Based Violence
    }

    if (primary.includes('Child')) {
      return 'CHILD_PROTECTION';
    }

    // Default for labor issues
    return 'MIGRANT';
  };

  // API submission - UPDATED for Sauti CMS Backend
  const sendToServer = async (data) => {
    isSubmitting.value = true;

    console.log("Original data:", data);

    const cleanedData = cleanSkippedData(data);
    const employment = getEmploymentData(cleanedData);
    const contacts = getAllContactMethods(cleanedData);

    // Construct a detailed description string from all collected data
    let fullDescription = `NARRATIVE:\n${cleanedData.complaint_narrative || 'No narrative provided.'}\n\n`;

    fullDescription += `--- CATEGORIES ---\n${cleanedData.complaint_categories?.join(', ') || 'None'}\n\n`;

    if (cleanedData.reporting_for_who === 'For someone else') {
      const victim = getVictimData(cleanedData);
      fullDescription += `--- VICTIM DETAILS ---\n`;
      fullDescription += `Name: ${victim.fname || ''} ${victim.other_names || ''}\n`;
      if (cleanedData.victim_sex) fullDescription += `Sex: ${cleanedData.victim_sex}\n`;
      if (cleanedData.victim_dob) fullDescription += `DOB: ${cleanedData.victim_dob}\n`;
      if (cleanedData.victim_location) fullDescription += `Location: ${cleanedData.victim_location}\n`;
      if (cleanedData.victim_passport) fullDescription += `Passport: ${cleanedData.victim_passport}\n\n`;
    }

    fullDescription += `--- EMPLOYMENT DETAILS ---\n`;
    fullDescription += `Job Title: ${employment.job_title}\n`;
    fullDescription += `Employer: ${employment.employer_name}\n`;
    if (employment.employer_phone || employment.employer_email) {
      fullDescription += `Employer Contact: ${employment.employer_phone || ''} / ${employment.employer_email || ''}\n`;
    }
    fullDescription += `Work Location: ${employment.work_town || ''}, ${employment.work_country || ''}\n\n`;

    fullDescription += `--- PERPETRATOR DETAILS ---\n`;
    const perp = getPerpetratorData(cleanedData);
    fullDescription += `Name: ${perp.fname || ''} ${perp.other_names || ''}\n`;
    fullDescription += `Relationship: ${perp.relationship || ''}\n`;
    fullDescription += `Notes: ${perp.notes || ''}\n`;

    const contactName = cleanedData.reporter_names || "Anonymous";
    const isAnonymous = contactName === "Anonymous";

    // Construct the payload matching ReportCreateSerializer
    const payload = {
      category: mapCategoryToBackend(cleanedData.complaint_categories),
      description: fullDescription,
      is_anonymous: isAnonymous,
      contact_name: contactName,
      contact_phone: contacts.phone || contacts.whatsapp || "",
      contact_email: contacts.email || "",
      location: cleanedData.reporter_location || "",
    };

    console.log("Final payload for /api/reports/:", payload);

    try {
      // Post to the Sauti CMS Reports endpoint
      const response = await apiClient.post("/reports/", payload);
      console.log("Server response:", response);

      // Default to PENDING if no ref number returned (though backend should generate one)
      const referenceNumber = response.data.reference_number || "PENDING";

      // Move to final message or success state
      if (currentStep.value !== 'final_message') {
        moveToNextStep('final_message');
      }

      messages.value.push({
        text: `✅ Report Submitted. Reference Number: ${referenceNumber}`,
        type: "bot",
        time: getCurrentTime()
      });

      messages.value.push({
        text: "We have received your report. Please keep this reference number safe.",
        type: "bot",
        time: getCurrentTime()
      });

      // Clear stored responses
      localStorage.removeItem("mglsd_responses");
      localStorage.removeItem("mglsd_navigation_history");

      setTimeout(() => {
        // Optional: Reset or close
      }, 5000);

    } catch (error) {
      console.error("Submission error:", error);

      let errorMsg = "I'm having trouble connecting to the server. Please try again later or call our hotline directly.";

      if (error.response && error.response.data) {
        console.error("Validation errors:", error.response.data);
      }

      messages.value.push({
        text: errorMsg,
        type: "bot",
        time: getCurrentTime()
      });
    } finally {
      isSubmitting.value = false;
    }
  };


  // Watchers
  watch(messages, () => {
    scrollToBottom();
  });

  // Check for info questions and logic checks when current question changes
  watch(currentQuestion, (newQuestion) => {
    if (newQuestion && (newQuestion.type === 'info' || newQuestion.type === 'logic_check')) {
      handleInfoQuestion();
    }

    // Auto-detect location for reporter and victim location questions
    if (newQuestion && (newQuestion.id === 'reporter_location' || newQuestion.id === 'victim_location')) {
      // Small delay to let the question appear first, then auto-detect
      setTimeout(() => {
        handleLocationDetection();
      }, 1000);
    }
  }, { immediate: true });

  // Lifecycle
  onMounted(() => {
    console.log('Component mounted, available questions:', mglsdQuestions.length);
    console.log('Question IDs:', mglsdQuestions.map(q => q.id));
    console.log('Environment check:');
    console.log('VUE_APP_OPENCAGE_API_KEY:', process.env.VUE_APP_OPENCAGE_API_KEY);

    initializeChat();

    // Listen for page reload/refresh events
    window.addEventListener("beforeunload", handlePageReload);
    window.addEventListener("pagehide", handlePageReload);

    // Also listen for regular beforeunload to save state
    window.addEventListener("beforeunload", () => {
      if (responses.value && Object.keys(responses.value).length > 0) {
        localStorage.setItem("mglsd_responses", JSON.stringify(responses.value));
        localStorage.setItem("mglsd_navigation_history", JSON.stringify(navigationHistory.value));
      }
    });

    scrollToBottom();
    setTimeout(scrollToBottom, 250);
    setTimeout(scrollToBottom, 500);
  });

  onBeforeUnmount(() => {
    window.removeEventListener("beforeunload", handlePageReload);
    window.removeEventListener("pagehide", handlePageReload);
    window.removeEventListener("beforeunload", () => { });
  });
</script>


<style scoped>

  /* Base Styles - Just increased width and height */
  .chat-window {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 420px;
    height: 750px;
    background: rgba(255, 255, 255, 0.95);
    /* Transparent background */
    backdrop-filter: blur(10px);
    /* Glassmorphism effect */
    border-radius: 20px;
    /* Rounded corners */
    overflow: hidden;
    display: flex;
    flex-direction: column;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
    font-family: inherit;
    transition: all 0.3s ease;
    z-index: 100000;
    border: none;
  }

  /* Header Styles */
  .chat-header {
    padding: 12px 18px;
    background: rgba(255, 255, 255, 0.8);
    color: #333;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    z-index: 10;
    border-bottom: none;
    /* Remove border */
  }

  .header-controls,
  .window-controls {
    display: flex;
    align-items: center;
    gap: 15px;
  }

  .chat-with-us-animated {
    display: flex;
    flex-direction: column;
  }

  .static-text {
    font-weight: 600;
    font-size: 16px;
  }

  .typing-text {
    font-size: 12px;
    opacity: 0.9;
  }

  .minimize-button,
  .maximize-button,
  .close-button,
  .back-button {
    background: none;
    border: none;
    color: #666;
    cursor: pointer;
    font-size: 16px;
    padding: 4px;
    transition: opacity 0.2s;
  }

  .minimize-button:hover,
  .maximize-button:hover,
  .close-button:hover,
  .back-button:hover {
    opacity: 0.8;
  }

  /* Chat Profile */
  .chat-profile {
    padding: 20px 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    background: transparent;
    border-bottom: none;
    /* Remove border */
    position: relative;
  }

  .chat-profile::after {
    display: none;
    /* Remove separator line */
  }

  .bot-avatar {
    position: relative;
    width: 65px;
    height: 65px;
    margin-bottom: 12px;
    border-radius: 50%;
    padding: 3px;
    border: 3px solid #f0f0f0;
    transition: all 0.3s ease;
  }

  .bot-avatar:hover {
    transform: scale(1.05);
    border-color: #e0e0e0;
  }

  .bot-avatar img {
    width: 100%;
    height: 100%;
    border-radius: 100%;
    object-fit: cover;
  }

  .status-indicator {
    position: absolute;
    width: 12px;
    height: 12px;
    background: #4CAF50;
    border-radius: 50%;
    bottom: 3px;
    right: 3px;
    border: 2px solid white;
    box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.3);
    animation: pulse 2s infinite;
  }

  @keyframes pulse {
    0% {
      box-shadow: 0 0 0 0 rgba(76, 175, 80, 0.5);
    }

    70% {
      box-shadow: 0 0 0 6px rgba(76, 175, 80, 0);
    }

    100% {
      box-shadow: 0 0 0 0 rgba(76, 175, 80, 0);
    }
  }

  .bot-name {
    margin: 5px 0;
    color: #333;
    font-size: 18px;
    font-weight: 600;
  }

  .bot-subtitle {
    margin: 0 0 12px 0;
    color: #666;
    font-size: 14px;
  }

  /* Progress Indicator - Simple addition */
  .progress-indicator {
    width: 80%;
    margin: 8px 0;
  }

  .progress-bar {
    width: 100%;
    height: 4px;
    background: #f0f0f0;
    border-radius: 2px;
    overflow: hidden;
    margin-bottom: 4px;
  }

  .progress-fill {
    height: 100%;
    background: #009EDB;
    border-radius: 2px;
    transition: width 0.5s ease;
  }

  .progress-text {
    font-size: 10px;
    color: #666;
    text-align: center;
    display: block;
  }

  .reaction-buttons {
    display: flex;
    gap: 12px;
    margin-top: 10px;
  }

  .thumbs-up,
  .thumbs-down {
    background: none;
    border: 1px solid #e0e0e0;
    border-radius: 20px;
    font-size: 16px;
    cursor: pointer;
    padding: 6px 12px;
    color: #666;
    transition: all 0.2s ease;
  }

  .thumbs-up:hover {
    color: #4CAF50;
    background-color: #f1f8e9;
    border-color: #4CAF50;
  }

  .thumbs-down:hover {
    color: #f44336;
    background-color: #ffebee;
    border-color: #f44336;
  }

  /* Messages Area - Original styling */
  .chat-body {
    flex: 1;
    overflow-y: auto;
    padding: 15px;
    background: #f8f9fa;
    display: flex;
    flex-direction: column;
    scroll-behavior: smooth;
    height: auto;
  }

  .timestamp {
    text-align: center;
    font-size: 12px;
    color: #9e9e9e;
    margin: 10px 0;
    padding: 4px 12px;
    background-color: rgba(255, 255, 255, 0.7);
    border-radius: 12px;
    align-self: center;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  }

  .message-container {
    display: flex;
    margin-bottom: 12px;
    max-width: 80%;
    animation: fadeIn 0.3s ease-out;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(10px);
    }

    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .bot-message {
    align-self: flex-start;
  }

  .user-message {
    align-self: flex-end;
    justify-content: flex-end;
  }

  .bot-avatar-small {
    width: 50px;
    height: 50px;
    margin-right: 8px;
    align-self: flex-end;
    border-radius: 100%;
  }

  .bot-avatar-small img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    border: 1px solid #e0e0e0;
  }

  .message-bubble {
    padding: 12px 16px;
    border-radius: 18px;
    font-size: 14px;
    line-height: 1.4;
    position: relative;
    transition: transform 0.2s ease;
  }

  .message-bubble:hover {
    transform: translateY(-2px);
  }

  .message-time {
    font-size: 0.7rem;
    margin-top: 4px;
    opacity: 0.7;
    display: block;
    text-align: right;
  }

  .bot-message .message-bubble {
    background: white;
    color: #333;
    border-bottom-left-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
  }

  .user-message .message-bubble {
    background: #009EDB;
    color: white;
    border-bottom-right-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }

  /* Typing indicator - Original */
  .typing-indicator-container {
    margin-bottom: 12px;
  }

  .typing-indicator {
    background-color: white;
    border-radius: 18px;
    padding: 10px 15px;
    display: flex;
    align-items: center;
    gap: 4px;
    border-bottom-left-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    width: 60px;
  }

  .typing-indicator span {
    display: inline-block;
    width: 8px;
    height: 8px;
    background-color: #888;
    border-radius: 50%;
    animation: typing-animation 1s infinite ease-in-out;
  }

  .typing-indicator span:nth-child(1) {
    animation-delay: 0s;
  }

  .typing-indicator span:nth-child(2) {
    animation-delay: 0.2s;
  }

  .typing-indicator span:nth-child(3) {
    animation-delay: 0.4s;
  }

  @keyframes typing-animation {

    0%,
    60%,
    100% {
      transform: translateY(0);
      opacity: 0.6;
    }

    30% {
      transform: translateY(-6px);
      opacity: 1;
    }
  }

  /* Emergency Notice - Simple addition */
  .emergency-notice {
    background: #dc3545;
    color: white;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    margin: 12px 0;
    box-shadow: 0 2px 5px rgba(220, 53, 69, 0.3);
  }

  .emergency-icon {
    font-size: 20px;
    margin-bottom: 8px;
  }

  .emergency-banner {
    background: #fff3cd;
    color: #856404;
    padding: 8px 12px;
    border-radius: 6px;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 12px;
  }

  /* Quick Action Buttons - Original styling */
  .quick-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 15px 0;
    align-self: center;
    width: 90%;
    justify-content: center;
  }

  .action-button {
    padding: 9px 14px;
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 20px;
    font-size: 13px;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.2s ease;
    color: #009EDB;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  }

  .action-button:hover {
    background-color: #f0f8ff;
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
    border-color: #009EDB;
  }

  /* Category Selection - New but keeping simple */
  .category-selection {
    margin: 15px 0;
  }

  .category-grid {
    display: grid;
    gap: 15px;
    max-height: 300px;
    overflow-y: auto;
    padding: 12px;
    background: white;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
  }

  .category-group {
    border-bottom: 1px solid #f0f0f0;
    padding-bottom: 12px;
  }

  .category-group:last-child {
    border-bottom: none;
  }

  .category-title {
    font-size: 14px;
    font-weight: 600;
    color: #009EDB;
    margin: 0 0 8px 0;
  }

  .subcategory-options {
    display: grid;
    gap: 6px;
  }

  .checkbox-option {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 6px 8px;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    background: #f8f9fa;
    font-size: 12px;
  }

  .checkbox-option:hover {
    background: #e9ecef;
  }

  .checkbox-option input[type="checkbox"] {
    display: none;
  }

  .checkmark {
    width: 16px;
    height: 16px;
    border: 1px solid #dee2e6;
    border-radius: 3px;
    position: relative;
    transition: all 0.2s ease;
    flex-shrink: 0;
  }

  .checkbox-option input[type="checkbox"]:checked+.checkmark {
    background: #009EDB;
    border-color: #009EDB;
  }

  .checkbox-option input[type="checkbox"]:checked+.checkmark::after {
    content: '';
    position: absolute;
    left: 4px;
    top: 1px;
    width: 4px;
    height: 8px;
    border: solid white;
    border-width: 0 2px 2px 0;
    transform: rotate(45deg);
  }

  .submit-categories-btn {
    background: #28a745;
    color: white;
    border: none;
    padding: 10px 16px;
    border-radius: 20px;
    font-size: 13px;
    cursor: pointer;
    margin-top: 12px;
    width: 100%;
    transition: all 0.2s ease;
  }

  .submit-categories-btn:hover {
    background: #218838;
    transform: translateY(-2px);
  }

  /* File Upload - Simple addition */
  .file-upload-area {
    margin: 15px 0;
  }

  .upload-zone {
    border: 2px dashed #009EDB;
    border-radius: 8px;
    padding: 30px 15px;
    text-align: center;
    background: rgba(0, 123, 255, 0.02);
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .upload-zone:hover {
    border-color: #0056b3;
    background: rgba(0, 123, 255, 0.05);
  }

  .upload-icon {
    font-size: 36px;
    color: #009EDB;
    margin-bottom: 12px;
  }

  .upload-hint {
    font-size: 11px;
    color: #666;
    margin-top: 6px;
  }

  .file-input {
    display: none;
  }

  .browse-btn {
    background: #009EDB;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 16px;
    margin-top: 8px;
    cursor: pointer;
    font-size: 12px;
  }

  .uploaded-files {
    margin-top: 12px;
    padding: 12px;
    background: white;
    border-radius: 6px;
    border: 1px solid #e0e0e0;
  }

  .file-item {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 6px;
    border-radius: 4px;
    margin-bottom: 6px;
    background: #f8f9fa;
    font-size: 12px;
  }

  .file-icon {
    color: #009EDB;
    font-size: 14px;
  }

  .file-name {
    flex: 1;
  }

  .file-size {
    font-size: 10px;
    color: #666;
  }

  .remove-file-btn {
    background: #dc3545;
    color: white;
    border: none;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    cursor: pointer;
    font-size: 10px;
  }

  .skip-upload-btn {
    background: #6c757d;
    color: white;
    border: none;
    padding: 6px 12px;
    border-radius: 12px;
    margin-top: 8px;
    cursor: pointer;
    width: 100%;
    font-size: 12px;
  }

  /* Input Area - Original styling */
  .chat-footer {
    padding: 12px 15px;
    background: white;
    border-top: 1px solid #f0f0f0;
  }

  .message-input-container {
    display: flex;
    background: #f7f7f7;
    border-radius: 25px;
    padding: 5px 10px;
    align-items: center;
    border: 1px solid #e0e0e0;
    transition: all 0.2s ease;
  }

  .message-input-container:focus-within {
    border-color: #009EDB;
    box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.1);
    background: white;
  }

  .message-input {
    flex: 1;
    border: none;
    background: transparent;
    padding: 10px;
    outline: none;
    font-size: 14px;
    resize: none;
  }

  .textarea-input {
    min-height: 50px;
    max-height: 100px;
    resize: vertical;
  }

  .input-actions {
    display: flex;
    gap: 8px;
  }

  .attach-button,
  .send-button {
    background: none;
    border: none;
    font-size: 16px;
    cursor: pointer;
    padding: 8px;
    width: 35px;
    height: 35px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
  }

  .attach-button {
    color: #2196F3;
  }

  .send-button {
    color: white;
    background-color: #009EDB;
  }

  .attach-button:hover {
    background-color: #e3f2fd;
  }

  .send-button:hover {
    background-color: #007BAA;
    transform: scale(1.05);
  }

  .send-button:disabled {
    background-color: #b3d7ff;
    cursor: not-allowed;
    transform: none;
  }

  /* Skip Button - New */
  .skip-button-container {
    margin-top: 8px;
    text-align: center;
  }

  .skip-button {
    background: #6c757d;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 12px;
    cursor: pointer;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }

  .skip-button:hover {
    background: #5a6268;
    transform: translateY(-1px);
  }

  .skip-button:disabled {
    background: #adb5bd;
    cursor: not-allowed;
    transform: none;
  }

  .validation-error {
    color: #dc3545;
    font-size: 0.85rem;
    margin-top: 8px;
    padding-left: 12px;
    animation: shakeError 0.4s ease-in-out;
  }

  @keyframes shakeError {

    0%,
    100% {
      transform: translateX(0);
    }

    25% {
      transform: translateX(-5px);
    }

    75% {
      transform: translateX(5px);
    }
  }

  .input-hint {
    color: #009EDB;
    font-size: 11px;
    margin-top: 6px;
    padding-left: 12px;
  }

  .other-inputs {
    margin-top: 12px;
    padding: 12px;
    border-radius: 12px;
    background-color: #f8f9fa;
    border: 1px solid #e0e0e0;
    animation: slideDown 0.3s ease-out;
  }

  /* Location Detection Styles */
  .location-options {
    margin: 15px 0;
    text-align: center;
    padding: 15px;
    background: #f8f9fa;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
  }

  .location-button {
    background: #28a745;
    color: white;
    border: none;
    padding: 12px 20px;
    border-radius: 25px;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 8px;
  }

  .location-button:hover {
    background: #218838;
    transform: translateY(-2px);
  }

  .location-button:disabled {
    background: #6c757d;
    cursor: not-allowed;
    transform: none;
  }

  .location-note {
    margin: 8px 0 0 0;
    font-size: 12px;
    color: #666;
  }

  @keyframes slideDown {
    from {
      opacity: 0;
      transform: translateY(-10px);
    }

    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  /* Completion Message - Original styling */
  .completion-message {
    padding: 20px;
    text-align: center;
    background-color: #f8f9fa;
    border-radius: 12px;
    margin: 10px 0;
    border: 1px solid #e0e0e0;
  }

  .completion-icon {
    font-size: 36px;
    margin-bottom: 12px;
    color: #28a745;
  }

  .completion-message h3 {
    margin: 0 0 8px 0;
    font-size: 16px;
    color: #333;
  }

  .completion-actions {
    display: flex;
    gap: 8px;
    justify-content: center;
    margin-top: 12px;
  }

  .download-btn,
  .restart-btn {
    padding: 8px 16px;
    border: none;
    border-radius: 16px;
    cursor: pointer;
    font-size: 12px;
    transition: all 0.2s ease;
  }

  .download-btn {
    background: #009EDB;
    color: white;
  }

  .restart-btn {
    background: #28a745;
    color: white;
  }

  .download-btn:hover,
  .restart-btn:hover {
    transform: translateY(-2px);
  }

  /* Anonymous Support - Simple */
  .anonymous-options {
    padding: 15px;
  }

  .support-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
    gap: 10px;
  }

  .support-option {
    padding: 15px;
    background: #f8f9fa;
    border-radius: 8px;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s ease;
    border: 1px solid #e0e0e0;
    font-size: 12px;
  }

  .support-option:hover {
    background: #009EDB;
    color: white;
    transform: translateY(-2px);
  }

  .footer-info {
    text-align: center;
    margin-top: 8px;
  }

  .privacy-notice {
    font-size: 10px;
    color: #666;
    padding: 4px 8px;
    background: #f8f9fa;
    border-radius: 12px;
    display: inline-block;
  }

  /* Responsive Design - MINIMAL changes, keeping original look */

  /* Desktop: 1200px+ - Just increased size */
  @media screen and (min-width: 1200px) {
    .chat-window {
      width: 450px;
      /* Slightly bigger on large screens */
      height: 700px;
    }
  }

  /* Tablet: 768px - 1199px */
  @media screen and (min-width: 768px) and (max-width: 1199px) {
    .chat-window {
      width: 400px;
      /* Slightly smaller but still bigger than original */
      height: 700px;
      bottom: 15px;
      right: 15px;
      max-height: 80vh;
    }

    .category-grid {
      max-height: 250px;
    }

    .completion-actions {
      flex-direction: column;
      gap: 6px;
    }
  }

  /* Mobile: 481px - 767px */
  @media screen and (max-width: 767px) {
    .chat-window {
      width: 100%;
      height: 100%;
      bottom: 0;
      right: 0;
      border-radius: 0;
    }

    .category-grid {
      max-height: 250px;
    }

    .action-button {
      font-size: 12px;
      padding: 8px 12px;
    }

    .completion-actions {
      flex-direction: column;
    }

    .support-grid {
      grid-template-columns: 1fr;
    }
  }

  /* Small Mobile: 320px - 480px */
  @media screen and (max-width: 480px) {
    .message-bubble {
      font-size: 13px;
      padding: 10px 14px;
    }

    .action-button {
      padding: 7px 10px;
      font-size: 11px;
    }

    .bot-avatar-small {
      width: 35px;
      height: 35px;
    }

    .category-grid {
      max-height: 200px;
      padding: 8px;
    }

    .checkbox-option {
      font-size: 11px;
      padding: 4px 6px;
    }

    .upload-zone {
      padding: 20px 10px;
    }

    .upload-icon {
      font-size: 28px;
    }
  }
</style>