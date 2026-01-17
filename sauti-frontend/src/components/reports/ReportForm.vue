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
          :type="currentInputType === 'number' ? 'tel' : 'text'"
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
  victim_sex: '',
  victim_age: '',
  location: '',
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
  {
    key: 'victim_name',
    question: (data) => data.identity === 'SELF' ? "What is your full name? <span class='text-red-500'>[Required]</span>" : "What is the name of the person you are reporting for? <span class='text-red-500'>[Required]</span>",
    type: 'input',
    placeholder: "Type full name...",
    required: true
  },
  {
    key: 'category',
    question: "What type of case is this? Please select the best match.",
    type: 'options',
    options: [
      { label: 'Child Protection', val: 'CHILD_PROTECTION' },
      { label: 'Gender Based Violence', val: 'GBV' },
      { label: 'Trafficking / Migrant', val: 'MIGRANT' },
      { label: 'Other', val: 'OTHER' }
    ]
  },
  {
    key: 'incident_type',
    question: "Could you specify the nature of the incident?",
    type: 'options',
    options: [
      { label: 'Physical Abuse', val: 'PHYSICAL' },
      { label: 'Sexual Violence', val: 'SEXUAL' },
      { label: 'Emotional Abuse', val: 'EMOTIONAL' },
      { label: 'Neglect', val: 'NEGLECT' },
      { label: 'Economic', val: 'ECONOMIC' }
    ]
  },
  {
    key: 'reporter_contact',
    condition: (data) => data.identity !== 'SELF',
    question: "As the reporter, may we have your name? \n(You can type 'Skip' to remain anonymous)",
    type: 'input',
    placeholder: "Your Name",
    allowSkip: true
  },
  {
    key: 'reporter_phone',
    question: "Please provide a phone number where we can reach you for follow-up. <span class='text-red-500'>[Required]</span>",
    type: 'input',
    inputType: 'number',
    placeholder: "e.g., 077...",
    required: true,
    validator: (val) => /\d{9,}/.test(val) ? true : "Please enter a valid phone number (at least 9 digits)"
  },
  {
    key: 'victim_demographics_sex',
    question: (data) => data.identity === 'SELF' ? "What is your sex?" : "What is the victim's sex?",
    type: 'options',
    options: [
      { label: 'Male', val: 'MALE' },
      { label: 'Female', val: 'FEMALE' }
    ]
  },
  {
    key: 'victim_age',
    question: "Age (in years)?",
    type: 'input',
    inputType: 'number',
    placeholder: "e.g. 24",
    required: true
  },
  {
    key: 'location',
    question: "Where did this happen? (District, Village, or Landmark)",
    type: 'input',
    placeholder: "e.g. Kampala, Nakawa...",
    required: true
  },
  {
    key: 'description',
    question: "Please describe what happened in detail.",
    type: 'input',
    inputType: 'textarea',
    placeholder: "Type your story here...",
    required: true
  },
  {
    key: 'review',
    question: (data) => `<strong>Summary:</strong>\nType: ${data.category} - ${data.incident_type}\nVictim: ${data.victim_name} (${data.victim_age}, ${data.victim_sex})\nLocation: ${data.location}\n\nAre you ready to submit this secure report?`,
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
      userInput.value = ''
      await nextTick()
      inputRef.value?.focus()
    }

    await scrollToBottom()
  }, 800)
}

const handleSubmit = () => {
  const step = FLOW[currentStep.value]
  const val = userInput.value.trim()

  validationError.value = ''

  if (step.required && !val) {
    validationError.value = "This field is required."
    return
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
  else formData.value[key] = val
}

const submitForm = async () => {
    isTyping.value = true
    try {
        const payload = {
            reporter: {
                name: formData.value.reporter_name,
                phone: formData.value.reporter_phone,
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
            location: formData.value.location
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
    victim_sex: '',
    victim_age: '',
    location: '',
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
