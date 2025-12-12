<template>
  <div class="chat-container max-w-2xl mx-auto">
    <!-- Chat Messages Area -->
    <div ref="messagesContainer" class="chat-messages bg-gradient-to-b from-gray-50 to-white rounded-2xl p-6 mb-4 h-[600px] overflow-y-auto scroll-smooth">
      <!-- Welcome Message -->
      <div class="message-group mb-6">
        <div class="bot-message">
          <div class="avatar bg-blue-500">
            <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
              <path d="M2 5a2 2 0 012-2h7a2 2 0 012 2v4a2 2 0 01-2 2H9l-3 3v-3H4a2 2 0 01-2-2V5z"/>
              <path d="M15 7v2a4 4 0 01-4 4H9.828l-1.766 1.767c.28.149.599.233.938.233h2l3 3v-3h2a2 2 0 002-2V9a2 2 0 00-2-2h-1z"/>
            </svg>
          </div>
          <div class="message-bubble bot">
            <p class="font-semibold mb-2">👋 Hello! I'm here to help you report a case.</p>
            <p class="text-sm">This conversation is confidential and secure. You can remain anonymous if you wish. Let's start...</p>
          </div>
        </div>
      </div>

      <!-- Dynamic Messages -->
      <div v-for="(message, index) in messages" :key="index" class="message-group mb-6">
        <!-- Bot Message -->
        <div v-if="message.type === 'bot'" class="bot-message">
          <div class="avatar bg-blue-500">
            <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
              <path d="M2 5a2 2 0 012-2h7a2 2 0 012 2v4a2 2 0 01-2 2H9l-3 3v-3H4a2 2 0 01-2-2V5z"/>
            </svg>
          </div>
          <div class="message-bubble bot">
            <p v-html="message.text"></p>
          </div>
        </div>

        <!-- User Message -->
        <div v-if="message.type === 'user'" class="user-message">
          <div class="message-bubble user">
            <p>{{ message.text }}</p>
          </div>
        </div>

        <!-- Options (Category, Incident Type) -->
        <div v-if="message.type === 'options'" class="bot-message">
          <div class="avatar bg-blue-500">
            <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
              <path d="M2 5a2 2 0 012-2h7a2 2 0 012 2v4a2 2 0 01-2 2H9l-3 3v-3H4a2 2 0 01-2-2V5z"/>
            </svg>
          </div>
          <div class="message-bubble bot">
            <p class="mb-3" v-html="message.question"></p>
            <div class="space-y-2">
              <button
                v-for="option in message.options"
                :key="option.value"
                @click="selectOption(message.field, option.value, option.label)"
                class="option-button"
              >
                <span v-if="option.icon" class="mr-2">{{ option.icon }}</span>
                <div class="text-left flex-1">
                  <div class="font-medium">{{ option.label }}</div>
                  <div v-if="option.description" class="text-xs text-gray-500 mt-0.5">{{ option.description }}</div>
                </div>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Typing Indicator -->
      <div v-if="isTyping" class="bot-message">
        <div class="avatar bg-blue-500">
          <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
            <path d="M2 5a2 2 0 012-2h7a2 2 0 012 2v4a2 2 0 01-2 2H9l-3 3v-3H4a2 2 0 01-2-2V5z"/>
          </svg>
        </div>
        <div class="message-bubble bot">
          <div class="typing-indicator">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>
      </div>

      <!-- Success Message -->
      <div v-if="submitted" class="message-group">
        <div class="bot-message">
          <div class="avatar bg-green-500">
            <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
            </svg>
          </div>
          <div class="message-bubble bot bg-green-50 border-green-200">
            <p class="font-semibold text-green-800 mb-2">✓ Report Submitted Successfully</p>
            <p class="text-sm text-green-700">Your reference number is: <strong>{{ referenceNumber }}</strong></p>
            <p class="text-sm text-green-700 mt-2">Our team will review your report and may reach out if you provided contact information. Thank you for trusting us.</p>
            <button @click="resetForm" class="mt-4 px-4 py-2 bg-green-600 text-white rounded-lg text-sm font-medium hover:bg-green-700 transition-colors">
              Submit Another Report
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Input Area -->
    <div v-if="!submitted" class="chat-input bg-white rounded-2xl shadow-lg p-4">
      <form @submit.prevent="handleSubmit">
        <div class="flex gap-3">
          <textarea
            v-if="currentStep < conversationFlow.length && conversationFlow[currentStep]?.multiline"
            v-model="userInput"
            :placeholder="currentPlaceholder"
            :disabled="isTyping || waitingForOption"
            class="flex-1 px-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 disabled:bg-gray-100 disabled:cursor-not-allowed resize-none"
            ref="inputField"
            rows="4"
          ></textarea>
          <input
            v-else
            v-model="userInput"
            :placeholder="currentPlaceholder"
            :disabled="isTyping || waitingForOption"
            class="flex-1 px-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 disabled:bg-gray-100 disabled:cursor-not-allowed"
            ref="inputField"
          />
          <button
            type="submit"
            :disabled="!userInput.trim() || isTyping || waitingForOption"
            class="px-6 py-3 bg-blue-500 text-white rounded-xl font-medium hover:bg-blue-600 transition-colors disabled:bg-gray-300 disabled:cursor-not-allowed flex items-center gap-2 self-start"
          >
            <span>Send</span>
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/>
            </svg>
          </button>
        </div>
        <!-- Character Counter for Narrative -->
        <div v-if="currentStep < conversationFlow.length && conversationFlow[currentStep]?.showCounter" class="mt-2 text-right">
          <span class="text-sm" :class="userInput.length > 0 ? 'text-blue-600' : 'text-gray-400'">
            {{ userInput.length }} characters
          </span>
        </div>
      </form>
      <p v-if="error" class="text-red-600 text-sm mt-2">{{ error }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, nextTick, onMounted } from 'vue'
import { api } from '@/utils/axios'

const messagesContainer = ref(null)
const inputField = ref(null)
const userInput = ref('')
const messages = ref([])
const isTyping = ref(false)
const waitingForOption = ref(false)
const submitted = ref(false)
const referenceNumber = ref('')
const error = ref('')

const form = ref({
  reporting_for: '',
  category: '',
  contact_name: '',
  contact_phone: '',
  victim_name: '',
  victim_sex: '',
  victim_age: '',
  location: '',
  description: '',
  incident_type: ''
})

const conversationFlow = [
  // Step 1: Names - Who is reporting and victim name
  {
    step: 'reporting_for',
    type: 'options',
    question: 'Are you reporting for yourself or on behalf of someone else?',
    field: 'reporting_for',
    options: [
      { value: 'SELF', label: 'For Myself', icon: '👤', description: 'I am the person affected' },
      { value: 'BEHALF', label: 'On Behalf of Someone', icon: '👥', description: 'I am reporting for someone else' }
    ]
  },
  {
    step: 'victim_name',
    type: 'input',
    question: 'What is the name of the victim? <span class="text-sm text-red-500">[Required]</span>',
    field: 'victim_name',
    placeholder: 'Enter victim\'s name',
    required: true
  },
  // Step 2: Category
  {
    step: 'category',
    type: 'options',
    question: 'What type of case would you like to report?',
    field: 'category',
    options: [
      { value: 'CHILD_PROTECTION', label: 'Child Protection', icon: '👶', description: 'Abuse, neglect, or exploitation of a child' },
      { value: 'GBV', label: 'Gender-Based Violence', icon: '🚨', description: 'Violence based on gender' },
      { value: 'MIGRANT', label: 'Migrant Issues', icon: '✈️', description: 'Issues related to migration and labor' },
      { value: 'PSEA', label: 'Sexual Exploitation & Abuse', icon: '⚠️', description: 'Sexual exploitation or abuse' }
    ]
  },
  {
    step: 'incident_type',
    type: 'options',
    question: 'What type of incident occurred?',
    field: 'incident_type',
    options: [
      { value: 'physical', label: 'Physical Abuse', icon: '🤕' },
      { value: 'sexual', label: 'Sexual Abuse', icon: '⚠️' },
      { value: 'emotional', label: 'Emotional Abuse', icon: '💔' },
      { value: 'neglect', label: 'Neglect', icon: '🏚️' },
      { value: 'exploitation', label: 'Exploitation', icon: '⛓️' },
      { value: 'other', label: 'Other', icon: '📝' }
    ]
  },
  // Step 3: Contacts
  {
    step: 'ask_name',
    type: 'input',
    question: 'May I have your name? <span class="text-sm text-gray-500">(Optional - you can skip this)</span>',
    field: 'contact_name',
    placeholder: 'Your name or type "skip" to remain anonymous',
    skippable: true
  },
  {
    step: 'ask_phone',
    type: 'input',
    question: 'Please provide a phone number where we can reach you. <span class="text-sm text-red-500">[Required]</span>',
    field: 'contact_phone',
    placeholder: 'Enter phone number',
    required: true
  },
  // Step 4: Sex
  {
    step: 'victim_sex',
    type: 'options',
    question: 'What is the sex of the victim?',
    field: 'victim_sex',
    options: [
      { value: 'MALE', label: 'Male', icon: '♂️' },
      { value: 'FEMALE', label: 'Female', icon: '♀️' }
    ]
  },
  {
    step: 'victim_age',
    type: 'input',
    question: 'What is the approximate age of the victim? <span class="text-sm text-red-500">[Required]</span>',
    field: 'victim_age',
    placeholder: 'Enter age (e.g., 12 years old)',
    required: true
  },
  // Step 5: Location
  {
    step: 'location',
    type: 'input',
    question: 'Where are you? Please provide your location (District, Village/Town, or area). <span class="text-sm text-red-500">[Required]</span>',
    field: 'location',
    placeholder: 'e.g., Kampala, Nakawa Division or Gulu, Bardege Village',
    required: true
  },
  // Step 6: Narrative (moved after phone call)
  {
    step: 'description',
    type: 'input',
    question: 'Please describe what happened in as much detail as you feel comfortable sharing. <span class="text-sm text-gray-500">Who was involved? When did it happen?</span>',
    field: 'description',
    placeholder: 'Describe the incident...',
    multiline: true,
    showCounter: true
  }
]

let currentStep = 0

const currentPlaceholder = computed(() => {
  const step = conversationFlow[currentStep]
  return step?.placeholder || 'Type your response...'
})

const scrollToBottom = async () => {
  await nextTick()
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}

const addBotMessage = (text) => {
  messages.value.push({ type: 'bot', text })
  scrollToBottom()
}

const addUserMessage = (text) => {
  messages.value.push({ type: 'user', text })
  scrollToBottom()
}

const addOptionsMessage = (question, options, field) => {
  messages.value.push({ type: 'options', question, options, field })
  waitingForOption.value = true
  scrollToBottom()
}

const typeMessage = async (callback, delay = 1000) => {
  isTyping.value = true
  await scrollToBottom()
  setTimeout(() => {
    isTyping.value = false
    callback()
  }, delay)
}

const selectOption = async (field, value, label) => {
  // Handle confirmation response separately
  if (field === 'confirm') {
    waitingForOption.value = false
    addUserMessage(label)

    if (value === 'yes') {
      await typeMessage(() => {
        addBotMessage('Thank you. Submitting your report securely...')
        setTimeout(() => submitReport(), 1000)
      }, 800)
    } else {
      await typeMessage(() => {
        addBotMessage('No problem! Let\'s start fresh.')
        setTimeout(() => resetForm(), 1000)
      }, 800)
    }
    return
  }

  // Handle regular option selection
  waitingForOption.value = false
  form.value[field] = value
  addUserMessage(label)

  await typeMessage(() => {
    proceedToNextStep()
  }, 800)
}

const handleSubmit = async () => {
  if (!userInput.value.trim()) return

  const step = conversationFlow[currentStep]
  const value = userInput.value.trim()

  // Check if user wants to skip (only for skippable fields)
  if (step.skippable && (value.toLowerCase() === 'skip' || value.toLowerCase() === 'anonymous')) {
    addUserMessage('Skip')
    userInput.value = ''
    await typeMessage(() => {
      addBotMessage('No problem, moving on...')
      setTimeout(() => proceedToNextStep(), 500)
    }, 500)
    return
  }

  // Validate required fields - don't allow "skip", "unknown", empty-like responses
  if (step.required) {
    const invalidResponses = ['skip', 'unknown', 'none', 'n/a', 'na', 'no', '-', '.']
    const isInvalidResponse = invalidResponses.includes(value.toLowerCase()) || value.length < 2

    if (isInvalidResponse) {
      userInput.value = ''
      await typeMessage(() => {
        addBotMessage('I need this information to help you. Please provide a valid response.')
        nextTick(() => inputField.value?.focus())
      }, 500)
      return
    }

    // Special validation for phone numbers - should contain digits
    if (step.field === 'contact_phone') {
      const hasDigits = /\d/.test(value)
      if (!hasDigits) {
        userInput.value = ''
        await typeMessage(() => {
          addBotMessage('Please provide a valid phone number with digits.')
          nextTick(() => inputField.value?.focus())
        }, 500)
        return
      }
    }
  }

  // Save the input
  form.value[step.field] = value
  addUserMessage(value)
  userInput.value = ''

  await typeMessage(() => {
    proceedToNextStep()
  }, 800)
}

const proceedToNextStep = () => {
  currentStep++

  if (currentStep >= conversationFlow.length) {
    // Show review and submit
    showReview()
    return
  }

  const nextStep = conversationFlow[currentStep]

  // Get question (could be a function or string)
  const question = typeof nextStep.question === 'function'
    ? nextStep.question()
    : nextStep.question

  if (nextStep.type === 'options') {
    addOptionsMessage(question, nextStep.options, nextStep.step)
  } else {
    addBotMessage(question)
  }

  // Focus input if it's a text input step
  if (nextStep.type === 'input') {
    nextTick(() => inputField.value?.focus())
  }
}

const showReview = () => {
  const reportingFor = conversationFlow.find(s => s.step === 'reporting_for')?.options.find(o => o.value === form.value.reporting_for)?.label
  const category = conversationFlow.find(s => s.step === 'category')?.options.find(o => o.value === form.value.category)?.label
  const incidentType = conversationFlow.find(s => s.step === 'incident_type')?.options.find(o => o.value === form.value.incident_type)?.label
  const victimSex = conversationFlow.find(s => s.step === 'victim_sex')?.options.find(o => o.value === form.value.victim_sex)?.label

  addBotMessage(`
    <div class="space-y-2">
      <p class="font-semibold">Let me confirm the details:</p>
      <p><strong>Reporting:</strong> ${reportingFor}</p>
      <p><strong>Victim Name:</strong> ${form.value.victim_name}</p>
      <p><strong>Category:</strong> ${category}</p>
      <p><strong>Incident Type:</strong> ${incidentType}</p>
      ${form.value.contact_name ? `<p><strong>Your Name:</strong> ${form.value.contact_name}</p>` : '<p><em>Reporting anonymously</em></p>'}
      ${form.value.contact_phone ? `<p><strong>Phone:</strong> ${form.value.contact_phone}</p>` : ''}
      <p><strong>Victim Sex:</strong> ${victimSex}</p>
      ${form.value.victim_age ? `<p><strong>Victim Age:</strong> ${form.value.victim_age}</p>` : ''}
      <p><strong>Location:</strong> ${form.value.location}</p>
      <p><strong>Description:</strong> ${form.value.description}</p>
    </div>
  `)

  setTimeout(() => {
    addOptionsMessage(
      'Is this information correct?',
      [
        { value: 'yes', label: 'Yes, submit my report', icon: '✓' },
        { value: 'no', label: 'No, let me start over', icon: '↺' }
      ],
      'confirm'
    )
  }, 1500)
}

const submitReport = async () => {
  try {
    isTyping.value = true
    error.value = ''

    const reportingForLabel = form.value.reporting_for === 'SELF' ? 'Reporting for self' : 'Reporting on behalf of someone else'
    const sexLabel = form.value.victim_sex === 'MALE' ? 'Male' : 'Female'

    const reportData = {
      category: form.value.category,
      contact_name: form.value.contact_name || 'Anonymous',
      contact_phone: form.value.contact_phone,
      incident_type: form.value.incident_type,
      description: `${reportingForLabel}\n\nVictim Name: ${form.value.victim_name}\nVictim Sex: ${sexLabel}\nVictim Age: ${form.value.victim_age}\nLocation: ${form.value.location}\n\n${form.value.description}`,
      status: 'PENDING',
      source: 'ONLINE'
    }

    const response = await api.reports.submit(reportData)
    referenceNumber.value = response.data.reference_number
    submitted.value = true
    scrollToBottom()
  } catch (err) {
    error.value = 'Failed to submit report. Please try again.'
    console.error('Error submitting report:', err)
  } finally {
    isTyping.value = false
  }
}

const resetForm = () => {
  messages.value = []
  currentStep = 0
  form.value = {
    reporting_for: '',
    category: '',
    contact_name: '',
    contact_phone: '',
    victim_name: '',
    victim_sex: '',
    victim_age: '',
    location: '',
    description: '',
    incident_type: ''
  }
  submitted.value = false
  referenceNumber.value = ''
  error.value = ''
  startConversation()
}

const startConversation = async () => {
  await typeMessage(() => {
    const firstStep = conversationFlow[0]
    addOptionsMessage(firstStep.question, firstStep.options, firstStep.step)
  }, 1500)
}

onMounted(() => {
  startConversation()
})
</script>

<style scoped>
.chat-messages::-webkit-scrollbar {
  width: 6px;
}

.chat-messages::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 10px;
}

.chat-messages::-webkit-scrollbar-thumb {
  background: #cbd5e0;
  border-radius: 10px;
}

.chat-messages::-webkit-scrollbar-thumb:hover {
  background: #a0aec0;
}

.message-group {
  animation: fadeIn 0.3s ease-in;
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
  display: flex;
  gap: 12px;
  align-items: flex-start;
}

.user-message {
  display: flex;
  justify-content: flex-end;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.message-bubble {
  max-width: 80%;
  padding: 14px 18px;
  border-radius: 18px;
  line-height: 1.5;
}

.message-bubble.bot {
  background: white;
  border: 1px solid #e2e8f0;
  color: #2d3748;
  border-bottom-left-radius: 4px;
}

.message-bubble.user {
  background: #3b82f6;
  color: white;
  border-bottom-right-radius: 4px;
}

.option-button {
  width: 100%;
  display: flex;
  align-items: center;
  padding: 12px 16px;
  background: #f7fafc;
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  text-align: left;
  transition: all 0.2s;
  cursor: pointer;
}

.option-button:hover {
  background: #edf2f7;
  border-color: #3b82f6;
  transform: translateX(4px);
}

.typing-indicator {
  display: flex;
  gap: 4px;
  padding: 4px;
}

.typing-indicator span {
  width: 8px;
  height: 8px;
  background: #cbd5e0;
  border-radius: 50%;
  animation: typing 1.4s infinite;
}

.typing-indicator span:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-indicator span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes typing {
  0%, 60%, 100% {
    transform: translateY(0);
    opacity: 0.7;
  }
  30% {
    transform: translateY(-10px);
    opacity: 1;
  }
}
</style>
