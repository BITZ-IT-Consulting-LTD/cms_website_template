<template>
  <div class="flex flex-col h-[600px] w-full bg-gradient-to-b from-white to-gray-50 rounded-[2rem] shadow-sm border border-gray-200 overflow-hidden relative" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
    
    <!-- Header -->
    <div class="p-4 flex items-center justify-between sticky top-0 z-10">
      <div class="flex items-center gap-3">
        <div>
           <h2 class="font-bold text-secondary text-2xl leading-tight" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Sauti Assistant</h2>
        </div>
      </div>
      <button @click="resetChat" class="text-gray-400 hover:text-secondary transition-colors" title="Restart">
        <RotateCcw class="w-5 h-5" />
      </button>
    </div>

    <!-- Chat Area -->
    <div ref="chatContainer" class="flex-1 overflow-y-auto p-4 space-y-4 scroll-smooth">
      <div class="space-y-4 pb-4">
        
        <!-- Render Messages -->
        <template v-for="(msg, i) in messages" :key="i">
          
          <!-- Bot Message -->
          <div v-if="msg.sender === 'bot'" class="flex gap-3 items-end animate-fade-in-up">
             <div class="w-8 h-8 rounded-full bg-secondary flex-shrink-0 flex items-center justify-center text-white text-xs font-bold" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">S</div>
             <div class="flex flex-col gap-2 max-w-[85%]">
               <div class="bg-white p-4 rounded-2xl rounded-bl-none shadow-sm border border-gray-100 text-gray-700 text-sm leading-relaxed whitespace-pre-line" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;" v-html="msg.text"></div>
               
               <!-- Options -->
               <div v-if="msg.options && !msg.responded" class="flex flex-wrap gap-2 mt-1">
                 <button v-for="opt in msg.options" :key="opt.val" 
                   @click="handleOption(opt)"
                   class="px-4 py-2 bg-white border border-gray-200 text-secondary text-sm font-bold rounded-xl hover:bg-secondary hover:text-white transition-all shadow-sm hover:shadow-md text-left" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
                   {{ opt.label }}
                 </button>
               </div>
             </div>
          </div>

          <!-- User Message -->
          <div v-else class="flex justify-end animate-fade-in-up">
             <div class="bg-[#006633] text-white p-4 rounded-2xl rounded-br-none shadow-md max-w-[85%] text-sm leading-relaxed" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
               {{ msg.text }}
             </div>
          </div>
        </template>

        <!-- Typing Indicator -->
        <div v-if="isTyping" class="flex gap-3 items-end animate-fade-in-up">
           <div class="w-8 h-8 rounded-full bg-secondary flex-shrink-0 flex items-center justify-center text-white text-xs font-bold" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">S</div>
           <div class="bg-white p-4 rounded-2xl rounded-bl-none shadow-sm border border-gray-100 w-16">
             <div class="flex gap-1 justify-center">
               <span class="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce"></span>
               <span class="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce delay-100"></span>
               <span class="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce delay-200"></span>
             </div>
           </div>
        </div>

      </div>
    </div>

    <!-- Input Area -->
    <div class="p-4 bg-white border-t border-gray-100">
      <form @submit.prevent="handleSubmit" class="relative">
        <textarea 
          v-if="currentInputType === 'textarea'"
          v-model="userInput"
          :disabled="isTyping || isFinished || waitingForOption"
          placeholder="Please describe what happened..."
          class="w-full pl-5 pr-14 py-4 bg-gray-50 rounded-[1.5rem] border border-gray-200 focus:bg-white focus:border-secondary focus:ring-2 focus:ring-secondary/10 outline-none transition-all text-gray-800 text-sm resize-none h-32"
          style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;"
          ref="inputRef"
        ></textarea>
        
        <input 
          v-else
          v-model="userInput"
          :type="currentInputType"
          :disabled="isTyping || isFinished || waitingForOption"
          :placeholder="inputPlaceholder"
          class="w-full pl-5 pr-14 py-4 bg-gray-50 rounded-full border border-gray-200 focus:bg-white focus:border-secondary focus:ring-2 focus:ring-secondary/10 outline-none transition-all text-gray-800 text-sm"
          style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;"
          ref="inputRef"
          autofocus
        />

        <button 
          v-if="!isFinished && !waitingForOption"
          type="submit" 
          :disabled="!userInput.trim()"
          class="absolute right-2 bottom-2 w-10 h-10 bg-secondary rounded-full flex items-center justify-center text-white shadow-lg hover:bg-emerald-800 disabled:opacity-50 disabled:cursor-not-allowed transition-all">
          <Send class="w-5 h-5" />
        </button>
      </form>
      <div v-if="validationError" class="text-red-500 text-xs font-bold mt-2 ml-2 flex items-center gap-1" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
        <AlertCircle class="w-4 h-4" />
        {{ validationError }}
      </div>
    </div>

    <!-- Success Overlay -->
    <div v-if="isSuccess" class="absolute inset-0 bg-white/95 backdrop-blur-sm flex flex-col items-center justify-center p-8 text-center z-50 animate-fade-in-up">
      <div class="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center text-green-600 mb-6 shadow-lg shadow-green-100">
        <CheckCircle class="w-12 h-12" />
      </div>
      <h3 class="text-2xl font-bold text-secondary mb-2" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Report Submitted</h3>
      <p class="text-gray-600 mb-6 text-sm" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">Your secure reference number is:</p>
      <div class="bg-gray-100 px-6 py-3 rounded-xl font-mono font-bold text-xl text-black mb-8 select-all border border-gray-200 tracking-wider" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
        {{ referenceNumber }}
      </div>
      <button @click="resetChat" class="px-8 py-3 bg-secondary text-white rounded-full font-bold shadow-lg hover:shadow-xl transition-all active:scale-95" style="font-family: var(--font-cronos), 'cronos-pro', 'Cronos Pro', Georgia, serif;">
        Start New Report
      </button>
    </div>

  </div>
</template>

<script setup>
import { ref, nextTick, onMounted } from 'vue'
import { api } from '@/utils/axios'
import { RotateCcw, Send, CheckCircle, AlertCircle } from 'lucide-vue-next'

const messages = ref([])
const isTyping = ref(false)
const userInput = ref('')
const currentStep = ref(0)
const isFinished = ref(false)
const isSuccess = ref(false)
const referenceNumber = ref('')
const validationError = ref('')
const waitingForOption = ref(false)
const currentInputType = ref('text')
const inputPlaceholder = ref('Type your answer...')
const inputRef = ref(null)

const chatContainer = ref(null)

// Data Store
const formData = ref({
  identity: '',
  victim_name: '',
  category: '',
  incident_type: '',
  reporter_name: '',
  reporter_phone: '',
  has_alternative_contact: '', // Yes/No for alternative contact
  alternative_contact: '', // Alternative contact information
  victim_sex: '',
  victim_age: '',
  victim_location: '', // Where the victim/person is located
  incident_location: '', // Where the incident happened
  description: ''
})

// Flow Definition
const FLOW = [
  {
    key: 'identity',
    question: "Welcome to Sauti 116. I am the Sauti Automated Assistant. \n\nTo start, are you reporting for yourself or on behalf of someone else?",
    type: 'options',
    options: [
      { label: 'For Myself', val: 'SELF' },
      { label: 'For Someone Else', val: 'OTHERS' }
    ]
  },
  // FOR SOMEONE ELSE FLOW
  {
    key: 'reporter_contact',
    condition: (data) => data.identity === 'OTHERS',
    question: "As the reporter, may we have your name? (You can type 'Skip' to remain anonymous)",
    type: 'input',
    placeholder: "Your Name",
    allowSkip: true
  },
  {
    key: 'victim_name',
    condition: (data) => data.identity === 'OTHERS',
    question: "What is the name of the victim you are reporting for? <span class='text-red-500'>[Required]</span>",
    type: 'input',
    placeholder: "Type full name...",
    required: true
  },
  {
    key: 'victim_age',
    condition: (data) => data.identity === 'OTHERS',
    question: "Age of the victim (in years)?",
    type: 'input',
    inputType: 'number',
    placeholder: "e.g. 24",
    required: true
  },
  {
    key: 'victim_demographics_sex',
    condition: (data) => data.identity === 'OTHERS',
    question: "What is the victim's sex?",
    type: 'options',
    options: [
      { label: 'Male', val: 'MALE' },
      { label: 'Female', val: 'FEMALE' }
    ]
  },
  {
    key: 'victim_location',
    condition: (data) => data.identity === 'OTHERS',
    question: "What is the location of the victim?",
    type: 'input',
    placeholder: "e.g. Kampala, Nakawa, or place...",
    required: true
  },
  {
    key: 'reporter_phone',
    condition: (data) => data.identity === 'OTHERS',
    question: "Please provide a phone number where we can reach you for follow-up. <span class='text-red-500'>[Required]</span>",
    type: 'input',
    inputType: 'tel',
    placeholder: "+256 7XX XXX XXX (or +[country code] [number])",
    required: true,
    validator: (val) => {
      if (!val || !val.trim()) {
        return "Phone number is required"
      }
      // Remove spaces, dashes, and parentheses for validation
      const cleaned = val.replace(/[\s\-\(\)]/g, '')
      
      // International phone number pattern (E.164 format)
      // Must start with + followed by country code (1-3 digits) and number (4-14 digits)
      // Total length: 7-15 digits after the +
      const internationalPattern = /^\+[1-9]\d{6,14}$/
      
      // Uganda-specific patterns (for backward compatibility and default)
      const ugandaPattern = /^(\+?256|0)?(7[0-9]|20|3[1-9])[0-9]{7}$/
      
      // Check if it's a valid international format
      if (internationalPattern.test(cleaned)) {
        return true
      }
      
      // Check if it's a valid Uganda format (will be formatted to +256)
      if (ugandaPattern.test(cleaned)) {
        return true
      }
      
      // Check if it's a local format that can be converted (9-10 digits starting with 0 or 7-9)
      const localPattern = /^(0[1-9]|[7-9])[0-9]{8,9}$/
      if (localPattern.test(cleaned) && cleaned.length >= 9 && cleaned.length <= 10) {
        return true
      }
      
      return "Please enter a valid phone number with country code (e.g., +256 7XX XXX XXX, +1 555 123 4567, or 077XXXXXXX for Uganda)"
    },
    formatValue: (val) => {
      if (!val || !val.trim()) return val
      // Remove spaces, dashes, and parentheses for formatting
      const cleaned = val.replace(/[\s\-\(\)]/g, '')
      
      // Already has international format with +
      if (cleaned.startsWith('+') && /^\+[1-9]\d{6,14}$/.test(cleaned)) {
        return cleaned
      }
      
      // Uganda-specific formatting (default)
      // Already has +256
      if (cleaned.startsWith('+256') && cleaned.length === 13) {
        return cleaned
      }
      // Has 256 without +
      if (cleaned.startsWith('256') && cleaned.length === 12) {
        return '+' + cleaned
      }
      // Starts with 0 (local Uganda format)
      if (cleaned.startsWith('0') && cleaned.length === 10) {
        return '+256' + cleaned.substring(1)
      }
      // Just 9 digits (Uganda mobile number)
      if (/^[7-9]/.test(cleaned) && cleaned.length === 9) {
        return '+256' + cleaned
      }
      
      // Other country codes (if user enters country code without +)
      // Pattern: 1-3 digit country code followed by 4-14 digits
      const countryCodePattern = /^([1-9]\d{0,2})(\d{4,14})$/
      const match = cleaned.match(countryCodePattern)
      if (match && cleaned.length >= 7 && cleaned.length <= 15) {
        const countryCode = match[1]
        const number = match[2]
        // Don't auto-format if it looks like it might be a local number
        // Only format if country code is clearly identifiable (1-3 digits, number is 4+ digits)
        if (countryCode.length <= 3 && number.length >= 4) {
          return '+' + cleaned
        }
      }
      
      return val
    }
  },
  {
    key: 'category',
    condition: (data) => data.identity === 'OTHERS',
    question: "What type of case is this? Please select the best match.",
    type: 'options',
    options: [
      { label: 'Abuse and Violence', val: 'CHILD_PROTECTION' },
      { label: 'Gender Based Violence', val: 'GBV' },
      { label: 'Migrant Worker Issues', val: 'MIGRANT' },
      { label: 'PSEA (Sexual Exploitation and Abuse)', val: 'OTHER' }
    ]
  },
  {
    key: 'incident_type',
    condition: (data) => data.identity === 'OTHERS',
    question: "Could you specify the nature of the incident?",
    type: 'options',
    options: [
      { label: 'Exploitation', val: 'EXPLOITATION' },
      { label: 'Neglect', val: 'NEGLECT' },
      { label: 'Economic Violence', val: 'ECONOMIC_VIOLENCE' },
      { label: 'Emotional & Psychological Abuse', val: 'EMOTIONAL_PSYCHOLOGICAL' },
      { label: 'Harmful Traditional Practices', val: 'HARMFUL_TRADITIONAL' },
      { label: 'Murder', val: 'MURDER' },
      { label: 'Online Sexual Abuse & Violence', val: 'ONLINE_SEXUAL' },
      { label: 'Physical Violence', val: 'PHYSICAL_VIOLENCE' },
      { label: 'Sexual Violence', val: 'SEXUAL_VIOLENCE' },
      { label: 'Threatening Violence', val: 'THREATENING_VIOLENCE' },
      { label: 'Trafficking in Persons', val: 'TRAFFICKING' }
    ]
  },
  {
    key: 'description',
    condition: (data) => data.identity === 'OTHERS',
    question: "Please describe what happened in detail.",
    type: 'input',
    inputType: 'textarea',
    placeholder: "Type your story here...",
    required: true
  },
  {
    key: 'incident_location',
    condition: (data) => data.identity === 'OTHERS',
    question: "Where did this happen? (District, Village, or Place)",
    type: 'input',
    placeholder: "e.g. Kampala, Nakawa, or place...",
    required: true
  },
  {
    key: 'has_alternative_contact',
    condition: (data) => data.identity === 'OTHERS',
    question: "Do you have an alternative contact that we can reach you or the victim on?",
    type: 'options',
    options: [
      { label: 'Yes', val: 'YES' },
      { label: 'No', val: 'NO' }
    ]
  },
  {
    key: 'alternative_contact',
    condition: (data) => data.identity === 'OTHERS' && data.has_alternative_contact === 'YES',
    question: "Please provide the alternative contact details (e.g., phone, email, address).",
    type: 'input',
    placeholder: "e.g., phone, email, address...",
    required: true
  },
  // FOR MYSELF FLOW
  {
    key: 'victim_name',
    condition: (data) => data.identity === 'SELF',
    question: "What is your full name? <span class='text-red-500'>[Required]</span>",
    type: 'input',
    placeholder: "Type full name...",
    required: true
  },
  {
    key: 'victim_age',
    condition: (data) => data.identity === 'SELF',
    question: "Age (in years)?",
    type: 'input',
    inputType: 'number',
    placeholder: "e.g. 24",
    required: true
  },
  {
    key: 'victim_demographics_sex',
    condition: (data) => data.identity === 'SELF',
    question: "What is your sex?",
    type: 'options',
    options: [
      { label: 'Male', val: 'MALE' },
      { label: 'Female', val: 'FEMALE' }
    ]
  },
  {
    key: 'victim_location',
    condition: (data) => data.identity === 'SELF',
    question: "Where are you located? (District, Village, or Place)",
    type: 'input',
    placeholder: "e.g. Kampala, Nakawa, or place...",
    required: true
  },
  {
    key: 'reporter_phone',
    condition: (data) => data.identity === 'SELF',
    question: "Please provide a phone number where we can reach you for follow-up. <span class='text-red-500'>[Required]</span>",
    type: 'input',
    inputType: 'tel',
    placeholder: "+256 7XX XXX XXX (or +[country code] [number])",
    required: true,
    validator: (val) => {
      if (!val || !val.trim()) {
        return "Phone number is required"
      }
      // Remove spaces, dashes, and parentheses for validation
      const cleaned = val.replace(/[\s\-\(\)]/g, '')
      
      // International phone number pattern (E.164 format)
      // Must start with + followed by country code (1-3 digits) and number (4-14 digits)
      // Total length: 7-15 digits after the +
      const internationalPattern = /^\+[1-9]\d{6,14}$/
      
      // Uganda-specific patterns (for backward compatibility and default)
      const ugandaPattern = /^(\+?256|0)?(7[0-9]|20|3[1-9])[0-9]{7}$/
      
      // Check if it's a valid international format
      if (internationalPattern.test(cleaned)) {
        return true
      }
      
      // Check if it's a valid Uganda format (will be formatted to +256)
      if (ugandaPattern.test(cleaned)) {
        return true
      }
      
      // Check if it's a local format that can be converted (9-10 digits starting with 0 or 7-9)
      const localPattern = /^(0[1-9]|[7-9])[0-9]{8,9}$/
      if (localPattern.test(cleaned) && cleaned.length >= 9 && cleaned.length <= 10) {
        return true
      }
      
      return "Please enter a valid phone number with country code (e.g., +256 7XX XXX XXX, +1 555 123 4567, or 077XXXXXXX for Uganda)"
    },
    formatValue: (val) => {
      if (!val || !val.trim()) return val
      // Remove spaces, dashes, and parentheses for formatting
      const cleaned = val.replace(/[\s\-\(\)]/g, '')
      
      // Already has international format with +
      if (cleaned.startsWith('+') && /^\+[1-9]\d{6,14}$/.test(cleaned)) {
        return cleaned
      }
      
      // Uganda-specific formatting (default)
      // Already has +256
      if (cleaned.startsWith('+256') && cleaned.length === 13) {
        return cleaned
      }
      // Has 256 without +
      if (cleaned.startsWith('256') && cleaned.length === 12) {
        return '+' + cleaned
      }
      // Starts with 0 (local Uganda format)
      if (cleaned.startsWith('0') && cleaned.length === 10) {
        return '+256' + cleaned.substring(1)
      }
      // Just 9 digits (Uganda mobile number)
      if (/^[7-9]/.test(cleaned) && cleaned.length === 9) {
        return '+256' + cleaned
      }
      
      // Other country codes (if user enters country code without +)
      // Pattern: 1-3 digit country code followed by 4-14 digits
      const countryCodePattern = /^([1-9]\d{0,2})(\d{4,14})$/
      const match = cleaned.match(countryCodePattern)
      if (match && cleaned.length >= 7 && cleaned.length <= 15) {
        const countryCode = match[1]
        const number = match[2]
        // Don't auto-format if it looks like it might be a local number
        // Only format if country code is clearly identifiable (1-3 digits, number is 4+ digits)
        if (countryCode.length <= 3 && number.length >= 4) {
          return '+' + cleaned
        }
      }
      
      return val
    }
  },
  {
    key: 'category',
    condition: (data) => data.identity === 'SELF',
    question: "What type of case is this? Please select the best match.",
    type: 'options',
    options: [
      { label: 'Abuse and Violence', val: 'CHILD_PROTECTION' },
      { label: 'Gender Based Violence', val: 'GBV' },
      { label: 'Migrant Worker Issues', val: 'MIGRANT' },
      { label: 'PSEA (Sexual Exploitation and Abuse)', val: 'OTHER' }
    ]
  },
  {
    key: 'incident_type',
    condition: (data) => data.identity === 'SELF',
    question: "Could you specify the nature of the incident?",
    type: 'options',
    options: [
      { label: 'Exploitation', val: 'EXPLOITATION' },
      { label: 'Neglect', val: 'NEGLECT' },
      { label: 'Economic Violence', val: 'ECONOMIC_VIOLENCE' },
      { label: 'Emotional & Psychological Abuse', val: 'EMOTIONAL_PSYCHOLOGICAL' },
      { label: 'Harmful Traditional Practices', val: 'HARMFUL_TRADITIONAL' },
      { label: 'Murder', val: 'MURDER' },
      { label: 'Online Sexual Abuse & Violence', val: 'ONLINE_SEXUAL' },
      { label: 'Physical Violence', val: 'PHYSICAL_VIOLENCE' },
      { label: 'Sexual Violence', val: 'SEXUAL_VIOLENCE' },
      { label: 'Threatening Violence', val: 'THREATENING_VIOLENCE' },
      { label: 'Trafficking in Persons', val: 'TRAFFICKING' }
    ]
  },
  {
    key: 'description',
    condition: (data) => data.identity === 'SELF',
    question: "Please describe what happened in detail.",
    type: 'input',
    inputType: 'textarea',
    placeholder: "Type your story here...",
    required: true
  },
  {
    key: 'incident_location',
    condition: (data) => data.identity === 'SELF',
    question: "Where did this happen? (District, Village, or Place)",
    type: 'input',
    placeholder: "e.g. Kampala, Nakawa, or place...",
    required: true
  },
  {
    key: 'has_alternative_contact',
    condition: (data) => data.identity === 'SELF',
    question: "Do you have an alternative contact that we can reach you on?",
    type: 'options',
    options: [
      { label: 'Yes', val: 'YES' },
      { label: 'No', val: 'NO' }
    ]
  },
  {
    key: 'alternative_contact',
    condition: (data) => data.identity === 'SELF' && data.has_alternative_contact === 'YES',
    question: "Please provide the alternative contact details (e.g., phone, email, address).",
    type: 'input',
    placeholder: "e.g., phone, email, address...",
    required: true
  },
  // SUMMARY (appears for both flows)
  {
    key: 'review',
    question: (data) => {
      // Helper function to get case type label
      const getCaseTypeLabel = (val) => {
        const caseTypeMap = {
          'CHILD_PROTECTION': 'Abuse and Violence',
          'GBV': 'Gender Based Violence',
          'MIGRANT': 'Migrant Worker Issues',
          'OTHER': 'PSEA (Sexual Exploitation and Abuse)'
        }
        return caseTypeMap[val] || val
      }
      
      // Helper function to get incident type label
      const getIncidentTypeLabel = (val) => {
        const incidentTypeMap = {
          'EXPLOITATION': 'Exploitation',
          'NEGLECT': 'Neglect',
          'ECONOMIC_VIOLENCE': 'Economic Violence',
          'EMOTIONAL_PSYCHOLOGICAL': 'Emotional & Psychological Abuse',
          'HARMFUL_TRADITIONAL': 'Harmful Traditional Practices',
          'MURDER': 'Murder',
          'ONLINE_SEXUAL': 'Online Sexual Abuse & Violence',
          'PHYSICAL_VIOLENCE': 'Physical Violence',
          'SEXUAL_VIOLENCE': 'Sexual Violence',
          'THREATENING_VIOLENCE': 'Threatening Violence',
          'TRAFFICKING': 'Trafficking in Persons'
        }
        return incidentTypeMap[val] || val
      }
      
      const identityText = data.identity === 'SELF' ? 'Yourself' : 'Someone Else'
      const victimInfo = data.identity === 'SELF' 
        ? `You: ${data.victim_name} (${data.victim_age} years, ${data.victim_sex})`
        : `Victim: ${data.victim_name} (${data.victim_age} years, ${data.victim_sex})`
      const reporterInfo = data.identity === 'SELF' 
        ? `Phone: ${data.reporter_phone}`
        : `Reporter: ${data.reporter_name || 'Anonymous'}, Phone: ${data.reporter_phone}`
      
      const caseTypeLabel = getCaseTypeLabel(data.category)
      const incidentTypeLabel = getIncidentTypeLabel(data.incident_type)
      const alternativeContactInfo = data.has_alternative_contact === 'YES' && data.alternative_contact
        ? `\nAlternative Contact: ${data.alternative_contact}`
        : ''
      
      return `<strong>Summary:</strong>\n\nReporting for: ${identityText}\n${victimInfo}\nLocation: ${data.victim_location}\nCase Type: ${caseTypeLabel}\nIncident: ${incidentTypeLabel}\n${reporterInfo}${alternativeContactInfo}\nIncident Location: ${data.incident_location}\n\nDescription: ${data.description}\n\nAre you ready to submit this secure report?`
    },
    type: 'options',
    options: [
      { label: 'Yes, Submit Securely', val: 'CONFIRM' },
      { label: 'No, Start Over', val: 'RESET' }
    ]
  }
]

// Logic
const init = () => {
  currentStep.value = -1
  processNextStep()
}

const processNextStep = async () => {
  currentStep.value++
  const step = FLOW[currentStep.value]
  
  if (!step) return

  if (step.condition && !step.condition(formData.value)) {
    processNextStep()
    return
  }

  isTyping.value = true
  await scrollToBottom()
  
  setTimeout(async () => {
    isTyping.value = false
    
    let qText = typeof step.question === 'function' ? step.question(formData.value) : step.question
    
    messages.value.push({
      sender: 'bot',
      text: qText,
      options: step.options,
      responded: false
    })

    if (step.type === 'options') {
      waitingForOption.value = true
      currentInputType.value = 'text'
      inputPlaceholder.value = 'Select an option above...'
    } else {
      waitingForOption.value = false
      currentInputType.value = step.inputType || 'text'
      inputPlaceholder.value = step.placeholder || 'Type here...'
      // Set default value for phone if formatValue exists
      if (step.key === 'reporter_phone' && step.formatValue) {
        userInput.value = '+256 ' // Default to Uganda, but user can change country code
      } else {
        userInput.value = ''
      }
      await nextTick()
      inputRef.value?.focus()
    }

    await scrollToBottom()
  }, 800)
}

const handleSubmit = () => {
  const step = FLOW[currentStep.value]
  let val = userInput.value.trim()

  validationError.value = ''

  if (step.required && !val) {
    validationError.value = "This field is required."
    return
  }

  // Format phone number if formatValue function exists
  if (step.formatValue && val) {
    val = step.formatValue(val)
  }

  if (step.validator) {
    const valid = step.validator(val)
    if (valid !== true) {
      validationError.value = valid
      return
    }
  }

  if (step.allowSkip && val.toLowerCase() === 'skip') {
    messages.value.push({ sender: 'user', text: 'Skipped' })
    handleDataCapture(step.key, null)
    processNextStep()
    return
  }

  messages.value.push({ sender: 'user', text: val })
  handleDataCapture(step.key, val)
  
  userInput.value = ''
  processNextStep()
}

const handleOption = (opt) => {
  const step = FLOW[currentStep.value]
  const lastMsg = messages.value[messages.value.length - 1]
  if (lastMsg) lastMsg.responded = true

  if (opt.val === 'RESET') {
    resetChat()
    return
  }

  if (opt.val === 'CONFIRM') {
    submitForm()
    return
  }

  messages.value.push({ sender: 'user', text: opt.label })
  waitingForOption.value = false
  handleDataCapture(step.key, opt.val)
  
  if (step.key === 'victim_demographics_sex') formData.value.victim_sex = opt.label

  processNextStep()
}

const handleDataCapture = (key, val) => {
  if (key === 'reporter_contact') formData.value.reporter_name = val
  else if (key === 'victim_demographics_sex') formData.value.victim_sex = val
  else if (key === 'has_alternative_contact' && val === 'NO') {
    // If No, clear alternative contact and set flag
    formData.value.has_alternative_contact = val
    formData.value.alternative_contact = ''
  } else {
    formData.value[key] = val
  }
}

const submitForm = async () => {
    isTyping.value = true
    try {
        const payload = {
            reporter: {
                name: formData.value.reporter_name,
                phone: formData.value.reporter_phone,
                alternative_contact: formData.value.alternative_contact || null,
                safe_to_contact: true
            },
            reporting_for: formData.value.identity,
            affected_persons: [{
                name: formData.value.victim_name,
                age: formData.value.victim_age,
                gender: formData.value.victim_sex
            }],
            intake_category: formData.value.category,
            description: `[Incident Type: ${formData.value.incident_type}] \n\n${formData.value.description}`,
            location: formData.value.incident_location || formData.value.victim_location,
            victim_location: formData.value.victim_location
        }

        const response = await api.reports.submit(payload)
        if (response.data && response.data.reference_number) {
            referenceNumber.value = response.data.reference_number
            isSuccess.value = true
            isFinished.value = true
        }
    } catch (e) {
        messages.value.push({ sender: 'bot', text: "I'm having trouble connecting to the server. Please call 116 for immediate help." })
    } finally {
        isTyping.value = false
    }
}

const resetChat = () => {
  messages.value = []
  userInput.value = ''
  formData.value = {
    identity: '',
    victim_name: '',
    category: '',
    incident_type: '',
    reporter_name: '',
    reporter_phone: '',
    has_alternative_contact: '',
    alternative_contact: '',
    victim_sex: '',
    victim_age: '',
    victim_location: '',
    incident_location: '',
    description: ''
  }
  isSuccess.value = false
  isFinished.value = false
  init()
}

const scrollToBottom = async () => {
  await nextTick()
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  }
}

onMounted(() => {
  init()
})
</script>

<style scoped>
.animate-fade-in-up {
  animation: fadeInUp 0.4s ease-out forwards;
  opacity: 0;
  transform: translateY(10px);
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
