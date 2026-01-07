<template>
  <div class="chat-container max-w-2xl mx-auto font-sans">
    <!-- 4-Stage Progress Indicator (Trauma-Informed Step Tracking) -->
    <div class="mb-6 flex gap-2 h-1.5 px-2">
      <div v-for="step in 4" :key="step" :class="[
        'flex-1 rounded-full transition-all duration-500',
        currentProgress >= step ? 'bg-primary shadow-sm' : 'bg-neutral-offwhite border border-primary/10'
      ]">
      </div>
    </div>

    <!-- Chat Messages Area (Accessible Live Region) -->
    <div ref="messagesContainer" role="log" aria-live="polite" aria-label="Incident Report Chat History"
      class="chat-messages bg-neutral-white rounded-[1.5rem] shadow-xl border-2 border-primary p-6 mb-6 h-[calc(100vh-280px)] max-h-[700px] min-h-[450px] overflow-y-auto scroll-smooth relative transition-all duration-300">
      <div class="message-group mb-8">
        <div class="bot-message flex gap-4">
          <div
            class="avatar bg-primary w-12 h-12 rounded-xl flex items-center justify-center shadow-md text-neutral-white">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
            </svg>
          </div>
          <div
            class="message-bubble bot bg-neutral-white text-secondary p-6 rounded-2xl rounded-tl-none shadow-sm max-w-[85%] border-2 border-primary">
            <p class="font-bold text-primary mb-1 uppercase tracking-wider text-xs">Always Safe & Confidential</p>
            <p class="text-base leading-relaxed font-normal">We are here to listen and help. Everything you share here
              is protected by secure encryption and kept strictly private. You can stop at any time.</p>
          </div>
        </div>
      </div>

      <div v-for="(message, index) in messages" :key="index" class="message-group mb-6">
        <!-- Bot Message -->
        <div v-if="message.type === 'bot'" class="bot-message flex gap-4 animate-fade-in-up">
          <div
            class="avatar bg-primary w-12 h-12 rounded-xl flex items-center justify-center shadow-md flex-shrink-0 text-neutral-white">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
            </svg>
          </div>
          <div
            class="message-bubble bot bg-neutral-white text-secondary p-6 rounded-2xl rounded-tl-none shadow-sm max-w-[85%] border-2 border-primary">
            <p v-html="message.text" class="text-base leading-relaxed font-semibold"></p>
          </div>
        </div>

        <!-- User Message -->
        <div v-if="message.type === 'user'" class="user-message flex justify-end mb-4 animate-fade-in-up">
          <div
            class="message-bubble user bg-primary text-neutral-white p-6 rounded-2xl rounded-tr-none shadow-md max-w-[85%]">
            <p class="text-base leading-relaxed font-bold">{{ message.text }}</p>
          </div>
        </div>

        <!-- Options -->
        <div v-if="message.type === 'options'" class="bot-message flex gap-4 w-full animate-fade-in-up">
          <div
            class="avatar bg-primary w-12 h-12 rounded-xl flex items-center justify-center shadow-md flex-shrink-0 text-neutral-white">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
          </div>
          <div class="message-bubble bot w-full max-w-[90%]">
            <p class="mb-6 font-bold text-black text-lg ml-1" v-html="message.question"></p>
            <div class="grid gap-3">
              <button v-for="option in message.options" :key="option.value"
                @click="selectOption(option.value, option.label)"
                class="option-button group relative overflow-hidden bg-neutral-white hover:bg-primary/5 border-2 border-neutral-offwhite hover:border-primary p-6 rounded-xl transition-all duration-300 text-left flex items-center shadow-sm">
                <span
                  class="w-12 h-12 flex items-center justify-center mr-5 rounded-lg bg-neutral-white border-2 border-primary group-hover:bg-primary group-hover:text-neutral-white text-primary text-xl transition-all duration-300">
                  {{ option.icon || '•' }}
                </span>
                <div class="flex-1">
                  <span class="font-bold text-black text-base group-hover:text-primary block transition-colors">{{
                    option.label }}</span>
                  <span v-if="option.description" class="text-xs text-black/80 mt-1 block font-bold">{{
                    option.description }}</span>
                </div>
                <svg
                  class="w-6 h-6 text-primary group-hover:text-secondary transform group-hover:translate-x-1 transition-all"
                  fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Typing Indicator -->
      <div v-if="isTyping" class="bot-message flex gap-3">
        <div
          class="avatar bg-primary w-10 h-10 rounded-full flex items-center justify-center shadow-md text-neutral-white">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
            <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
          </svg>
        </div>
        <div
          class="message-bubble bot bg-neutral-white border-2 border-primary p-4 rounded-2xl rounded-tl-none w-16 flex items-center justify-center">
          <div class="typing-indicator flex gap-1">
            <span class="bg-primary"></span><span class="bg-primary"></span><span class="bg-primary"></span>
          </div>
        </div>
      </div>

      <!-- Success Card -->
      <div v-if="submitted && referenceNumber" class="message-group animate-fade-in-up">
        <div class="bot-message flex gap-3">
          <div
            class="avatar bg-secondary w-10 h-10 rounded-full flex items-center justify-center shadow-md text-neutral-white">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <div
            class="message-bubble bot bg-neutral-white border-4 border-secondary w-full p-6 rounded-2xl rounded-tl-none shadow-sm">
            <h3 class="font-bold text-secondary text-xl mb-2">Report Securely Filed</h3>
            <div class="my-6 p-6 bg-neutral-white rounded-xl border-2 border-secondary shadow-inner text-center">
              <p class="text-[10px] text-black uppercase tracking-widest font-bold mb-2">Reference Number</p>
              <p class="text-3xl font-mono font-bold text-black tracking-widest">{{ referenceNumber }}</p>
            </div>
            <p class="text-black font-bold">Please save this number. Our protection team will review this case
              shortly.</p>

            <!-- What Happens Next Roadmap (Trauma-Informed Closure) -->
            <div class="mt-8 pt-8 border-t-2 border-neutral-offwhite">
              <h4 class="text-xs font-black text-primary uppercase tracking-[0.2em] mb-6">What Happens Next</h4>
              <div class="space-y-4">
                <div v-for="(step, idx) in [
                  { title: 'Secure Review', desc: 'Case workers at MGLSD verify the details.' },
                  { title: 'Action Plan', desc: 'We coordinate with local district protection officers.' },
                  { title: 'Safety Referral', desc: 'Direct support or intervention is launched.' }
                ]" :key="idx" class="flex gap-4 items-start text-left">
                  <div class="w-6 h-6 rounded-full bg-secondary/10 flex items-center justify-center shrink-0">
                    <span class="text-[10px] font-bold text-black">{{ idx + 1 }}</span>
                  </div>
                  <div>
                    <p class="text-[11px] font-bold text-black uppercase leading-none mb-1">{{ step.title }}</p>
                    <p class="text-[10px] text-black/60 leading-relaxed font-bold">{{ step.desc }}</p>
                  </div>
                </div>
              </div>
            </div>

            <button @click="resetForm"
              class="mt-8 w-full py-4 bg-secondary text-neutral-white rounded-xl font-bold uppercase tracking-widest hover:brightness-95 transition shadow-lg">File
              Another Report</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Input Area -->
    <div v-if="!submitted && currentStepType === 'input'"
      class="chat-input bg-neutral-white rounded-3xl shadow-2xl p-6 border-4 border-primary transition-all duration-300">
      <form @submit.prevent="handleInputSubmit">
        <div class="flex gap-4">
          <input v-model="inputValue" :type="currentInputType" :placeholder="inputPlaceholder" :disabled="isTyping"
            class="flex-1 px-6 py-6 border-2 border-primary rounded-2xl focus:border-secondary outline-none transition text-black font-bold placeholder:text-primary text-lg"
            ref="inputRef" autofocus :aria-label="inputPlaceholder" aria-describedby="validation-msg"
            id="chat-input-field" />
          <button type="submit"
            class="px-8 py-6 bg-primary text-neutral-white rounded-2xl font-bold text-lg hover:brightness-95 disabled:bg-neutral-offwhite disabled:text-black/30 transition shadow-xl"
            :aria-label="inputValue.trim() ? 'Send message' : 'Skip this part'">
            {{ inputValue.trim() ? 'SEND' : 'SKIP' }}
          </button>
        </div>
        <p v-if="validationError" id="validation-msg"
          class="text-emergency text-sm mt-4 ml-2 flex items-center font-bold" aria-live="assertive">
          <svg class="w-5 h-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          {{ validationError }}
        </p>
      </form>
    </div>

    <!-- Textarea for Narrative -->
    <div v-if="!submitted && currentStepType === 'textarea'"
      class="chat-input bg-neutral-white rounded-3xl shadow-2xl p-8 border-4 border-primary transition-all duration-300">
      <form @submit.prevent="handleInputSubmit">
        <label class="block text-lg font-bold text-black mb-4">{{ inputPlaceholder }}</label>
        <textarea v-model="inputValue" placeholder="Start typing here..." :disabled="isTyping"
          class="w-full px-6 py-6 border-2 border-primary rounded-2xl focus:border-secondary outline-none transition mb-6 resize-none h-48 text-black font-bold placeholder:text-primary text-lg"
          ref="inputRef"></textarea>
        <div class="flex justify-end">
          <button type="submit"
            class="px-12 py-6 bg-primary text-neutral-white rounded-2xl font-bold text-lg hover:bg-secondary shadow-xl transition-all">
            {{ inputValue.trim() ? 'Next Step' : 'Skip this part' }}
          </button>
        </div>
        <p v-if="validationError" class="text-emergency text-sm mt-4 font-bold">{{ validationError }}</p>
      </form>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed, nextTick, onMounted } from 'vue'
  import { api } from '@/utils/axios'

  // --- State ---
  const messagesContainer = ref(null)
  const inputRef = ref(null)
  const isTyping = ref(false)
  const inputValue = ref('')
  const inputPlaceholder = ref('')
  const validationError = ref('')
  const messages = ref([])
  const submitted = ref(false)
  const referenceNumber = ref('')

  const currentStepId = ref(null)
  const currentInputType = ref('text')
  const currentStepType = ref('none')
  const lastSubmittedValue = ref(null) // Track decision

  // Form Data Model
  const formData = ref({
    reporter: { name: null, phone: '', safe_to_contact: true },
    reporting_for: '',
    affected_persons: [],
    intake_category: 'OTHER',
    description: '',
    location: ''
  })

  // --- Flow Logic ---
  const STEPS = {
    REPORTER_NAME: 'reporter_name',
    REPORTER_PHONE: 'reporter_phone',
    SAFE_TO_CONTACT: 'safe_to_contact',
    REPORTING_FOR: 'reporting_for',

    // Single Person
    AFFECTED_SELF_AGE: 'affected_self_age',
    AFFECTED_SELF_GENDER: 'affected_self_gender',
    AFFECTED_OTHER_NAME: 'affected_other_name',
    AFFECTED_OTHER_AGE: 'affected_other_age',
    AFFECTED_OTHER_GENDER: 'affected_other_gender',
    AFFECTED_OTHER_RELATION: 'affected_other_relation',

    // Multiple Loop
    MULTIPLE_INTRO: 'multiple_intro',
    MULTIPLE_NAME: 'multiple_name',
    MULTIPLE_AGE: 'multiple_age',
    MULTIPLE_GENDER: 'multiple_gender',
    MULTIPLE_IS_CHILD: 'multiple_is_child',
    MULTIPLE_ADD_MORE: 'multiple_add_more',

    INTAKE_CATEGORY: 'intake_category',
    NARRATIVE: 'description',
    LOCATION_DISTRICT: 'location_district',
    REVIEW: 'review',
  }

  const startConversation = async () => {
    await promptStep(STEPS.NARRATIVE)
  }

  const promptStep = async (stepId) => {
    currentStepId.value = stepId
    isTyping.value = true
    await scrollToBottom()

    setTimeout(async () => {
      isTyping.value = false
      inputValue.value = ''
      validationError.value = ''

      switch (stepId) {
        // --- Narrative Flow (Stage 1: The Story) ---
        case STEPS.NARRATIVE:
          askInput('In your own words, can you share what is happening? Take your time—whatever you feel comfortable sharing is enough.', 'Start typing here...', 'textarea')
          break

        case STEPS.INTAKE_CATEGORY:
          askOptions('To help us get you the right kind of support, which of these best describes your situation?', [
            {
              value: 'CHILD_PROTECTION',
              label: 'Violence Against Children',
              icon: '🚸',
              description: 'Report abuse, neglect, or violence against anyone under 18.'
            },
            {
              value: 'GBV',
              label: 'Gender Based Violence',
              icon: '🛡️',
              description: 'Report domestic violence, sexual assault, or gender-based harm.'
            },
            {
              value: 'PSEA',
              label: 'Prevention of Sexual Exploitation',
              icon: '⚠️',
              description: 'Report sexual exploitation or abuse by aid workers or officials.'
            },
            {
              value: 'MIGRANT',
              label: 'Migrant Workers',
              icon: '🚶',
              description: 'Report labor issues, trafficking, or safety concerns abroad.'
            }
          ])
          break

        // --- Context (Stage 2: People Involved) ---
        case STEPS.REPORTING_FOR:
          askOptions('Are you sharing this story for yourself, or someone else?', [
            { value: 'SELF', label: 'Myself', icon: '👤' },
            { value: 'CHILD', label: 'A Child', icon: '👶' },
            { value: 'ADULT_OTHER', label: 'Another Adult', icon: '🧑' },
            { value: 'MULTIPLE', label: 'More than one person', icon: '👥' }
          ])
          break

        case STEPS.LOCATION_DISTRICT:
          askInput('Where did this happen? Knowing the location helps us coordinate with local teams. You can keep this general (e.g., Kampala).', 'e.g. Kampala, Nakawa', 'input')
          break

        // --- Reporter (Contextual Follow up) ---
        case STEPS.REPORTER_NAME:
          askInput('To follow up later, may we have your name? Leaving this blank means your report is anonymous.', 'Your Name (Optional)', 'input')
          break
        case STEPS.REPORTER_PHONE:
          askInput('What is the best phone number to reach you? We only ask so our counselors can offer direct assistance.', 'Phone Number', 'input')
          break
        case STEPS.SAFE_TO_CONTACT:
          askOptions('Is it safe for us to call or text you on this number?', [
            { value: 'yes', label: 'Yes, it is safe', icon: '✅' },
            { value: 'no', label: 'No, please do not contact me here', icon: '🚫' }
          ])
          break

        // --- Self ---
        case STEPS.AFFECTED_SELF_AGE:
          askInput('What is your age? This helps us choose the best counselor for you.', 'Your age', 'input')
          break
        case STEPS.AFFECTED_SELF_GENDER:
          askOptions('What is your sex?', [
            { value: 'MALE', label: 'Male' }, { value: 'FEMALE', label: 'Female' }
          ])
          break

        // --- Other (Single) ---
        case STEPS.AFFECTED_OTHER_NAME:
          askInput('What is the name of the person who needs help?', 'Their name', 'input')
          break
        case STEPS.AFFECTED_OTHER_AGE:
          askInput('What is their age?', 'Their age', 'input')
          break
        case STEPS.AFFECTED_OTHER_GENDER:
          askOptions('What is their sex?', [
            { value: 'MALE', label: 'Male' }, { value: 'FEMALE', label: 'Female' }
          ])
          break
        case STEPS.AFFECTED_OTHER_RELATION:
          askInput('What is your relationship to this person?', 'e.g. Neighbor, Friend, etc.', 'input')
          break

        // --- Multiple Loop ---
        case STEPS.MULTIPLE_INTRO:
          addBotMessage("Please tell us about the people affected one by one.")
          setTimeout(() => promptStep(STEPS.MULTIPLE_NAME), 800)
          break
        case STEPS.MULTIPLE_NAME:
          askInput(`Person ${formData.value.affected_persons.length + 1}: Name?`, 'Name (Optional)', 'input')
          break
        case STEPS.MULTIPLE_AGE:
          askInput('What is their age?', 'Age', 'input')
          break
        case STEPS.MULTIPLE_GENDER:
          askOptions('What is their sex?', [{ value: 'MALE', label: 'Male' }, { value: 'FEMALE', label: 'Female' }])
          break
        case STEPS.MULTIPLE_IS_CHILD:
          askOptions('Is this person under 18?', [{ value: 'yes', label: 'Yes (Child)' }, { value: 'no', label: 'No (Adult)' }])
          break
        case STEPS.MULTIPLE_ADD_MORE:
          askOptions('Would you like to add another person?', [{ value: 'yes', label: 'Yes, add another' }, { value: 'no', label: 'No, continue' }])
          break

        case STEPS.REVIEW:
          showReview()
          break
      }
    }, 500)
  }

  // Helpers
  const askInput = (text, placeholder, type, inputType = 'text') => {
    addBotMessage(text)
    inputPlaceholder.value = placeholder
    currentStepType.value = type
    currentInputType.value = inputType
    nextTick(() => inputRef.value?.focus())
  }

  const askOptions = (question, options) => {
    messages.value.push({ type: 'options', question, options })
    currentStepType.value = 'options'
    scrollToBottom()
  }

  const addBotMessage = (text) => {
    messages.value.push({ type: 'bot', text })
    scrollToBottom()
  }

  const addUserMessage = (text) => {
    messages.value.push({ type: 'user', text })
    scrollToBottom()
  }

  // Input Handling
  const handleInputSubmit = async () => {
    const val = inputValue.value.trim()

    // Trauma-informed: Allow skip on non-critical fields
    if (!val) {
      if ([STEPS.REPORTER_NAME, STEPS.AFFECTED_OTHER_NAME, STEPS.MULTIPLE_NAME].includes(currentStepId.value)) {
        addUserMessage('Skipped for now')
        saveData(currentStepId.value, null)
        currentStepType.value = 'none'
        nextStep()
        return
      }
      if (currentStepId.value === STEPS.NARRATIVE && !messages.some(m => m.type === 'user')) {
        // Must provide some info if it's the very first step
        validationError.value = 'Would you like to share a few words first?'
        return
      }
    }

    if (currentStepId.value === STEPS.REPORTER_PHONE && val && val.length < 5) {
      validationError.value = 'This helps us stay in touch. If it’s not safe, you can skip.'
      return
    }

    saveData(currentStepId.value, val)
    addUserMessage(val || 'No details provided')
    lastSubmittedValue.value = val
    currentStepType.value = 'none'
    nextStep()
  }

  const selectOption = async (value, label) => {
    if (currentStepType.value !== 'options') return

    if (currentStepId.value === STEPS.REVIEW) {
      if (value === 'submit') {
        addUserMessage(label)
        submitReport()
      } else {
        window.location.reload()
      }
      return
    }

    saveData(currentStepId.value, value)
    addUserMessage(label)
    lastSubmittedValue.value = value
    currentStepType.value = 'none'
    nextStep()
  }

  const saveData = (step, value) => {
    switch (step) {
      case STEPS.REPORTER_NAME:
        formData.value.reporter.name = value
        break
      case STEPS.REPORTER_PHONE:
        formData.value.reporter.phone = value
        break
      case STEPS.SAFE_TO_CONTACT:
        formData.value.reporter.safe_to_contact = (value === 'yes')
        break
      case STEPS.REPORTING_FOR:
        formData.value.reporting_for = value
        if (['SELF', 'ADULT_OTHER', 'CHILD'].includes(value)) formData.value.affected_persons = [{}]
        else if (value === 'MULTIPLE') formData.value.affected_persons = []
        break
      case STEPS.AFFECTED_SELF_AGE:
      case STEPS.AFFECTED_OTHER_AGE:
        if (formData.value.affected_persons[0]) formData.value.affected_persons[0].age = value
        break
      case STEPS.AFFECTED_SELF_GENDER:
      case STEPS.AFFECTED_OTHER_GENDER:
        if (formData.value.affected_persons[0]) formData.value.affected_persons[0].gender = value
        break
      case STEPS.AFFECTED_OTHER_NAME:
        if (formData.value.affected_persons[0]) formData.value.affected_persons[0].name = value
        break
      case STEPS.MULTIPLE_NAME:
        formData.value.affected_persons.push({ name: value })
        break
      case STEPS.MULTIPLE_AGE:
        getLastPerson().age = value
        break
      case STEPS.MULTIPLE_GENDER:
        getLastPerson().gender = value
        break
      case STEPS.MULTIPLE_IS_CHILD:
        getLastPerson().is_child = (value === 'yes')
        break
      case STEPS.INTAKE_CATEGORY:
        formData.value.intake_category = value
        break
      case STEPS.NARRATIVE:
        formData.value.description = value || "Story shared in confidence."
        break
      case STEPS.LOCATION_DISTRICT:
        formData.value.location = value
        break
    }
  }

  const getLastPerson = () => formData.value.affected_persons[formData.value.affected_persons.length - 1]

  const nextStep = () => {
    const current = currentStepId.value

    if (current === STEPS.NARRATIVE) return promptStep(STEPS.INTAKE_CATEGORY)
    if (current === STEPS.INTAKE_CATEGORY) return promptStep(STEPS.LOCATION_DISTRICT)
    if (current === STEPS.LOCATION_DISTRICT) return promptStep(STEPS.REPORTING_FOR)

    if (current === STEPS.REPORTING_FOR) {
      const type = formData.value.reporting_for
      if (type === 'SELF') return promptStep(STEPS.AFFECTED_SELF_AGE)
      if (type === 'ADULT_OTHER') return promptStep(STEPS.AFFECTED_OTHER_NAME)
      if (type === 'CHILD') return promptStep(STEPS.AFFECTED_OTHER_NAME)
      if (type === 'MULTIPLE') return promptStep(STEPS.MULTIPLE_INTRO)
    }

    if (current === STEPS.AFFECTED_SELF_GENDER ||
      current === STEPS.AFFECTED_OTHER_RELATION ||
      (current === STEPS.MULTIPLE_ADD_MORE && lastSubmittedValue.value === 'no')) {
      return promptStep(STEPS.REPORTER_NAME)
    }

    if (current === STEPS.REPORTER_NAME) return promptStep(STEPS.REPORTER_PHONE)
    if (current === STEPS.REPORTER_PHONE) return promptStep(STEPS.SAFE_TO_CONTACT)
    if (current === STEPS.SAFE_TO_CONTACT) return promptStep(STEPS.REVIEW)

    if (current === STEPS.AFFECTED_SELF_AGE) return promptStep(STEPS.AFFECTED_SELF_GENDER)
    if (current === STEPS.AFFECTED_OTHER_NAME) return promptStep(STEPS.AFFECTED_OTHER_AGE)
    if (current === STEPS.AFFECTED_OTHER_AGE) return promptStep(STEPS.AFFECTED_OTHER_GENDER)
    if (current === STEPS.AFFECTED_OTHER_GENDER) return promptStep(STEPS.AFFECTED_OTHER_RELATION)

    if (current === STEPS.MULTIPLE_NAME) return promptStep(STEPS.MULTIPLE_AGE)
    if (current === STEPS.MULTIPLE_AGE) return promptStep(STEPS.MULTIPLE_GENDER)
    if (current === STEPS.MULTIPLE_GENDER) return promptStep(STEPS.MULTIPLE_IS_CHILD)
    if (current === STEPS.MULTIPLE_IS_CHILD) return promptStep(STEPS.MULTIPLE_ADD_MORE)
    if (current === STEPS.MULTIPLE_ADD_MORE && lastSubmittedValue.value === 'yes') return promptStep(STEPS.MULTIPLE_NAME)
  }

  const currentProgress = computed(() => {
    if (!currentStepId.value) return 1
    const s = currentStepId.value
    if ([STEPS.NARRATIVE, STEPS.INTAKE_CATEGORY].includes(s)) return 1
    if ([STEPS.LOCATION_DISTRICT, STEPS.REPORTING_FOR].includes(s)) return 2
    if (s.startsWith('AFFECTED_') || s.startsWith('MULTIPLE_')) return 3
    if ([STEPS.REPORTER_NAME, STEPS.REPORTER_PHONE, STEPS.SAFE_TO_CONTACT, STEPS.REVIEW].includes(s)) return 4
    return 1
  })

  const showReview = () => {
    const personCount = formData.value.affected_persons.length
    const html = `
      <div class="border-l-4 border-primary pl-4 py-2 bg-neutral-offwhite rounded-r-lg">
        <h4 class="font-bold text-secondary mb-2">Review Your Information</h4>
        <p class="text-sm"><strong>Reporter:</strong> ${formData.value.reporter.name || 'Anonymous'}</p>
        <p class="text-sm"><strong>People Concerned:</strong> ${personCount > 0 ? personCount + ' person(s) listed' : 'As described'}</p>
        <p class="text-sm"><strong>Location:</strong> ${formData.value.location || 'General'}</p>
        <p class="text-sm text-black/60 italic mt-2">Your information is sent through a secure server.</p>
      </div>
    `
    addBotMessage(html)
    setTimeout(() => {
      askOptions('Are you ready to send this to our protection team?', [
        { value: 'submit', label: 'Yes, Submit Securely', icon: '✅' },
        { value: 'edit', label: 'No, let me start over', icon: '🔄' }
      ])
    }, 1000)
  }

  const submitReport = async () => {
    try {
      isTyping.value = true
      const payload = {
        reporter: formData.value.reporter,
        reporting_for: formData.value.reporting_for,
        affected_persons: formData.value.affected_persons,
        intake_category: formData.value.intake_category,
        description: formData.value.description,
        location: formData.value.location
      }
      const response = await api.reports.submit(payload)
      if (response.data && response.data.reference_number) {
        referenceNumber.value = response.data.reference_number
        submitted.value = true
      }
    } catch (err) {
      errorMessage('We encountered a temporary issue. Please try again or call 116 for immediate support.')
    } finally {
      isTyping.value = false
    }
  }

  const errorMessage = (msg) => {
    addBotMessage(`
      <div class="p-6 bg-emergency/5 border-2 border-emergency/20 rounded-[1.5rem] shadow-sm">
        <p class="text-emergency font-black uppercase tracking-[0.1em] text-[10px] mb-3 flex items-center gap-2">
          <span class="w-2 h-2 bg-emergency rounded-full animate-pulse"></span>
          System Connection Note
        </p>
        <p class="text-black font-bold text-base leading-relaxed mb-4">
          Our server is taking a deep breath. Your story is important and your data is safe.
        </p>
        <p class="text-sm text-black/70 font-bold">
          Please wait a moment and try again, or call <span class="text-emergency">116</span> directly for immediate support.
        </p>
      </div>
    `)
  }

  const resetForm = () => window.location.reload()

  const scrollToBottom = async () => {
    await nextTick()
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  }
  onMounted(() => startConversation())
</script>

<style scoped>
  .chat-messages::-webkit-scrollbar {
    width: 6px;
  }

  .chat-messages::-webkit-scrollbar-thumb {
    background: #cbd5e0;
    border-radius: 10px;
  }

  .typing-indicator span {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    animation: type 1.4s infinite;
  }

  .typing-indicator span:nth-child(2) {
    animation-delay: 0.2s;
  }

  .typing-indicator span:nth-child(3) {
    animation-delay: 0.4s;
  }

  @keyframes type {

    0%,
    100% {
      transform: translateY(0);
    }

    50% {
      transform: translateY(-4px);
    }
  }

  .animate-fade-in-up {
    animation: fadeInUp 0.3s ease-out;
  }

  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(10px);
    }

    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
</style>
