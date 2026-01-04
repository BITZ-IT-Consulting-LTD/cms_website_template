<template>
  <div class="chat-container max-w-2xl mx-auto font-sans">
    <!-- Chat Messages Area -->
    <div ref="messagesContainer"
      class="chat-messages bg-sauti-white rounded-[1.5rem] shadow-xl border-2 border-sauti-blue p-6 mb-6 h-[700px] overflow-y-auto scroll-smooth relative">
      <div class="message-group mb-8">
        <div class="bot-message flex gap-4">
          <div class="avatar bg-sauti-blue w-12 h-12 rounded-xl flex items-center justify-center shadow-md">
            <svg class="w-6 h-6 text-sauti-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
            </svg>
          </div>
          <div
            class="message-bubble bot bg-sauti-white text-sauti-darkGreen p-5 rounded-2xl rounded-tl-none shadow-sm max-w-[85%] border-2 border-sauti-blue">
            <p class="font-bold text-sauti-blue mb-1 uppercase tracking-wider text-xs">Official Secure Intake</p>
            <p class="text-base leading-relaxed font-normal">I am here to help you report a case. Your safety is our
              priority.</p>
          </div>
        </div>
      </div>

      <div v-for="(message, index) in messages" :key="index" class="message-group mb-6">
        <!-- Bot Message -->
        <div v-if="message.type === 'bot'" class="bot-message flex gap-4 animate-fade-in-up">
          <div
            class="avatar bg-sauti-blue w-12 h-12 rounded-xl flex items-center justify-center shadow-md flex-shrink-0">
            <svg class="w-6 h-6 text-sauti-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
            </svg>
          </div>
          <div
            class="message-bubble bot bg-sauti-white text-sauti-darkGreen p-5 rounded-2xl rounded-tl-none shadow-sm max-w-[85%] border-2 border-sauti-blue">
            <p v-html="message.text" class="text-base leading-relaxed font-semibold"></p>
          </div>
        </div>

        <!-- User Message -->
        <div v-if="message.type === 'user'" class="user-message flex justify-end mb-4 animate-fade-in-up">
          <div
            class="message-bubble user bg-sauti-blue text-sauti-white p-5 rounded-2xl rounded-tr-none shadow-md max-w-[85%]">
            <p class="text-base leading-relaxed font-bold">{{ message.text }}</p>
          </div>
        </div>

        <!-- Options -->
        <div v-if="message.type === 'options'" class="bot-message flex gap-4 w-full animate-fade-in-up">
          <div
            class="avatar bg-sauti-blue w-12 h-12 rounded-xl flex items-center justify-center shadow-md flex-shrink-0">
            <svg class="w-6 h-6 text-sauti-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
          </div>
          <div class="message-bubble bot w-full max-w-[90%]">
            <p class="mb-6 font-bold text-sauti-darkGreen text-lg ml-1" v-html="message.question"></p>
            <div class="grid gap-3">
              <button v-for="option in message.options" :key="option.value"
                @click="selectOption(option.value, option.label)"
                class="option-button group relative overflow-hidden bg-sauti-white hover:bg-sauti-blue/5 border-2 border-sauti-neutral hover:border-sauti-blue p-5 rounded-xl transition-all duration-300 text-left flex items-center shadow-sm">
                <span
                  class="w-12 h-12 flex items-center justify-center mr-5 rounded-lg bg-sauti-white border-2 border-sauti-blue group-hover:bg-sauti-blue group-hover:text-sauti-white text-sauti-blue text-xl transition-all duration-300">
                  {{ option.icon || '•' }}
                </span>
                <div class="flex-1">
                  <span
                    class="font-bold text-sauti-darkGreen text-base group-hover:text-sauti-blue block transition-colors">{{
                      option.label }}</span>
                  <span v-if="option.description" class="text-xs text-sauti-darkGreen/80 mt-1 block font-bold">{{
                    option.description }}</span>
                </div>
                <svg
                  class="w-6 h-6 text-sauti-blue group-hover:text-sauti-darkGreen transform group-hover:translate-x-1 transition-all"
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
        <div class="avatar bg-sauti-blue w-10 h-10 rounded-full flex items-center justify-center shadow-md">
          <svg class="w-4 h-4 text-sauti-white" fill="currentColor" viewBox="0 0 20 20">
            <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
            <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
          </svg>
        </div>
        <div
          class="message-bubble bot bg-sauti-white border-2 border-sauti-blue p-4 rounded-2xl rounded-tl-none w-16 flex items-center justify-center">
          <div class="typing-indicator flex gap-1">
            <span class="bg-sauti-blue"></span><span class="bg-sauti-blue"></span><span class="bg-sauti-blue"></span>
          </div>
        </div>
      </div>

      <!-- Success Card -->
      <div v-if="submitted && referenceNumber" class="message-group animate-fade-in-up">
        <div class="bot-message flex gap-3">
          <div class="avatar bg-sauti-darkGreen w-10 h-10 rounded-full flex items-center justify-center shadow-md">
            <svg class="w-6 h-6 text-sauti-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <div
            class="message-bubble bot bg-sauti-white border-4 border-sauti-darkGreen w-full p-6 rounded-2xl rounded-tl-none shadow-sm">
            <h3 class="font-bold text-sauti-darkGreen text-xl mb-2">Report Securely Filed</h3>
            <div class="my-6 p-6 bg-sauti-white rounded-xl border-2 border-sauti-darkGreen shadow-inner text-center">
              <p class="text-[10px] text-sauti-darkGreen uppercase tracking-widest font-bold mb-2">Reference Number</p>
              <p class="text-3xl font-mono font-bold text-sauti-darkGreen tracking-widest">{{ referenceNumber }}</p>
            </div>
            <p class="text-sauti-darkGreen font-bold">Please save this number. Our protection team will review this case
              shortly.</p>
            <button @click="resetForm"
              class="mt-6 w-full py-4 bg-sauti-darkGreen text-sauti-white rounded-xl font-bold uppercase tracking-widest hover:brightness-95 transition shadow-lg">File
              Another Report</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Input Area -->
    <div v-if="!submitted && currentStepType === 'input'"
      class="chat-input bg-sauti-white rounded-3xl shadow-2xl p-6 border-4 border-sauti-blue transition-all duration-300">
      <form @submit.prevent="handleInputSubmit">
        <div class="flex gap-4">
          <input v-model="inputValue" :type="currentInputType" :placeholder="inputPlaceholder" :disabled="isTyping"
            class="flex-1 px-6 py-5 border-2 border-sauti-blue rounded-2xl focus:border-sauti-darkGreen outline-none transition text-sauti-darkGreen font-bold placeholder:text-sauti-blue text-lg"
            ref="inputRef" autofocus />
          <button type="submit" :disabled="!inputValue.trim() || isTyping"
            class="px-10 py-5 bg-sauti-blue text-sauti-white rounded-2xl font-bold text-lg hover:brightness-95 disabled:bg-sauti-neutral disabled:text-sauti-darkGreen/30 transition shadow-xl">
            SEND
          </button>
        </div>
        <p v-if="validationError" class="text-sauti-red text-sm mt-4 ml-2 flex items-center font-bold">
          <svg class="w-5 h-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          {{ validationError }}
        </p>
      </form>
    </div>

    <!-- Textarea for Narrative -->
    <div v-if="!submitted && currentStepType === 'textarea'"
      class="chat-input bg-sauti-white rounded-3xl shadow-2xl p-8 border-4 border-sauti-blue transition-all duration-300">
      <form @submit.prevent="handleInputSubmit">
        <label class="block text-lg font-bold text-sauti-darkGreen mb-4">{{ inputPlaceholder }}</label>
        <textarea v-model="inputValue" placeholder="Start typing here..." :disabled="isTyping"
          class="w-full px-6 py-5 border-2 border-sauti-blue rounded-2xl focus:border-sauti-darkGreen outline-none transition mb-6 resize-none h-48 text-sauti-darkGreen font-bold placeholder:text-sauti-blue text-lg"
          ref="inputRef"></textarea>
        <div class="flex justify-end">
          <button type="submit" :disabled="!inputValue.trim() || isTyping"
            class="px-12 py-5 bg-sauti-blue text-sauti-white rounded-2xl font-bold text-lg hover:bg-sauti-darkGreen shadow-xl transition-all">
            Submit Description
          </button>
        </div>
        <p v-if="validationError" class="text-sauti-red text-sm mt-4 font-bold">{{ validationError }}</p>
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
    intake_category: '',
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
    await promptStep(STEPS.REPORTER_NAME)
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
        // --- Reporter ---
        case STEPS.REPORTER_NAME:
          askInput('May we have your name? You can say "No" to remain anonymous.', 'Your Name (Optional)', 'input')
          break
        case STEPS.REPORTER_PHONE:
          askInput('Please provide a phone number where we can reach you.', 'Phone Number (Required)', 'input')
          break
        case STEPS.SAFE_TO_CONTACT:
          askOptions('Is it safe for us to contact you on this number?', [
            { value: 'yes', label: 'Yes, it is safe', icon: '✅' },
            { value: 'no', label: 'No, do not contact me', icon: '🚫' }
          ])
          break

        // --- Reporting For ---
        case STEPS.REPORTING_FOR:
          askOptions('Who is affected by the incident you are reporting?', [
            { value: 'SELF', label: 'Myself', icon: '👤' },
            { value: 'ADULT_OTHER', label: 'Another Person (Adult)', icon: '🧑' },
            { value: 'CHILD', label: 'A Child (Under 18)', icon: '👶' },
            { value: 'MULTIPLE', label: 'Multiple People', icon: '👥' },
            { value: 'UNSPECIFIED', label: 'Prefer not to say', icon: '🤐' }
          ])
          break

        // --- Self ---
        case STEPS.AFFECTED_SELF_AGE:
          askInput('What is your approximate age?', 'Age e.g. 25', 'input')
          break
        case STEPS.AFFECTED_SELF_GENDER:
          askOptions('How do you identify?', [
            { value: 'MALE', label: 'Male' }, { value: 'FEMALE', label: 'Female' }, { value: 'OTHER', label: 'Other' }, { value: 'UNKNOWN', label: 'Prefer not to say' }
          ])
          break

        // --- Other (Single) ---
        case STEPS.AFFECTED_OTHER_NAME:
          askInput('What is the name of the person affected?', 'Their Name (Optional)', 'input')
          break
        case STEPS.AFFECTED_OTHER_AGE:
          askInput('What is their approximate age?', 'Age e.g. 30', 'input')
          break
        case STEPS.AFFECTED_OTHER_GENDER:
          askOptions('Gender of the affected person?', [
            { value: 'MALE', label: 'Male' }, { value: 'FEMALE', label: 'Female' }, { value: 'OTHER', label: 'Other' }, { value: 'UNKNOWN', label: 'Prefer not to say' }
          ])
          break
        case STEPS.AFFECTED_OTHER_RELATION:
          askInput('What is your relationship to them?', 'e.g. Neighbor, Friend', 'input')
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
          askInput('Approximate age?', 'Age', 'input')
          break
        case STEPS.MULTIPLE_GENDER:
          askOptions('Gender?', [{ value: 'MALE', label: 'Male' }, { value: 'FEMALE', label: 'Female' }, { value: 'OTHER', label: 'Other' }])
          break
        case STEPS.MULTIPLE_IS_CHILD:
          askOptions('Is this person under 18?', [{ value: 'yes', label: 'Yes (Child)' }, { value: 'no', label: 'No (Adult)' }])
          break
        case STEPS.MULTIPLE_ADD_MORE:
          askOptions('Would you like to add another person?', [{ value: 'yes', label: 'Yes, add another' }, { value: 'no', label: 'No, continue' }])
          break

        // --- Common ---
        case STEPS.INTAKE_CATEGORY:
          askOptions('What best describes the issue you are reporting?', [
            { value: 'CHILD_PROTECTION', label: 'Harm or abuse involving a child', icon: '🚸' },
            { value: 'GBV', label: 'Violence or abuse related to gender/relationships', icon: '💔' },
            { value: 'PSEA', label: 'Sexual violence or exploitation', icon: '⚠️' },
            { value: 'MIGRANT', label: 'Migration or displacement-related issue', icon: '🚶' },
            { value: 'OTHER', label: 'Something else / Not sure', icon: '❓' }
          ])
          break

        case STEPS.NARRATIVE:
          askInput('Please describe what happened, in your own words. Include when and where. Do not include names inside the story if unsafe.', 'Please describe the incident...', 'textarea')
          break

        case STEPS.LOCATION_DISTRICT:
          askInput('Location: Please provide the District and Town/Village', 'e.g. Kampala, Nakawa', 'input')
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
    if (!val) return

    if (currentStepId.value === STEPS.REPORTER_PHONE && val.length < 5) {
      validationError.value = 'Please enter a valid phone number.'
      return
    }

    saveData(currentStepId.value, val)
    addUserMessage(val)
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
        if (value.toLowerCase() === 'no' || value.toLowerCase() === 'anonymous') formData.value.reporter.name = null
        else formData.value.reporter.name = value
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
        else if (value === 'MULTIPLE') formData.value.affected_persons = [] // Reset
        break

      // Single 
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

      // Multiple Loop Data
      case STEPS.MULTIPLE_NAME:
        // New person start
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
        formData.value.description = value
        break
      case STEPS.LOCATION_DISTRICT:
        formData.value.location = value
        break
    }
  }

  const getLastPerson = () => formData.value.affected_persons[formData.value.affected_persons.length - 1]

  const nextStep = () => {
    const current = currentStepId.value

    if (current === STEPS.REPORTER_NAME) return promptStep(STEPS.REPORTER_PHONE)
    if (current === STEPS.REPORTER_PHONE) return promptStep(STEPS.SAFE_TO_CONTACT)
    if (current === STEPS.SAFE_TO_CONTACT) return promptStep(STEPS.REPORTING_FOR)

    if (current === STEPS.REPORTING_FOR) {
      const type = formData.value.reporting_for
      if (type === 'SELF') return promptStep(STEPS.AFFECTED_SELF_AGE)
      if (type === 'ADULT_OTHER') return promptStep(STEPS.AFFECTED_OTHER_NAME)
      if (type === 'CHILD') return promptStep(STEPS.AFFECTED_OTHER_NAME)
      if (type === 'MULTIPLE') return promptStep(STEPS.MULTIPLE_INTRO)
      if (type === 'UNSPECIFIED') return promptStep(STEPS.INTAKE_CATEGORY)
    }

    // Single Flow
    if (current === STEPS.AFFECTED_SELF_AGE) return promptStep(STEPS.AFFECTED_SELF_GENDER)
    if (current === STEPS.AFFECTED_SELF_GENDER) return promptStep(STEPS.INTAKE_CATEGORY)

    if (current === STEPS.AFFECTED_OTHER_NAME) return promptStep(STEPS.AFFECTED_OTHER_AGE)
    if (current === STEPS.AFFECTED_OTHER_AGE) return promptStep(STEPS.AFFECTED_OTHER_GENDER)
    if (current === STEPS.AFFECTED_OTHER_GENDER) return promptStep(STEPS.AFFECTED_OTHER_RELATION)
    if (current === STEPS.AFFECTED_OTHER_RELATION) return promptStep(STEPS.INTAKE_CATEGORY)

    // Multiple Loop
    if (current === STEPS.MULTIPLE_NAME) return promptStep(STEPS.MULTIPLE_AGE)
    if (current === STEPS.MULTIPLE_AGE) return promptStep(STEPS.MULTIPLE_GENDER)
    if (current === STEPS.MULTIPLE_GENDER) return promptStep(STEPS.MULTIPLE_IS_CHILD)
    if (current === STEPS.MULTIPLE_IS_CHILD) return promptStep(STEPS.MULTIPLE_ADD_MORE)
    if (current === STEPS.MULTIPLE_ADD_MORE) {
      if (lastSubmittedValue.value === 'yes') return promptStep(STEPS.MULTIPLE_NAME)
      else return promptStep(STEPS.INTAKE_CATEGORY)
    }

    if (current === STEPS.INTAKE_CATEGORY) return promptStep(STEPS.NARRATIVE)
    if (current === STEPS.NARRATIVE) return promptStep(STEPS.LOCATION_DISTRICT)
    if (current === STEPS.LOCATION_DISTRICT) return promptStep(STEPS.REVIEW)
  }

  const showReview = () => {
    const personCount = formData.value.affected_persons.length
    const html = `
      <div class="border-l-4 border-blue-500 pl-4 py-2 bg-gray-50 rounded-r-lg">
        <h4 class="font-bold text-gray-800 mb-2">Review Details</h4>
        <p class="text-sm"><strong>Reporter:</strong> ${formData.value.reporter.name || 'Anonymous'}</p>
        <p class="text-sm"><strong>Safe to Contact:</strong> ${formData.value.reporter.safe_to_contact ? 'Yes' : 'No'}</p>
        <p class="text-sm"><strong>Reporting For:</strong> ${formData.value.reporting_for}</p>
        <p class="text-sm"><strong>Affected Persons:</strong> ${personCount > 0 ? personCount + ' person(s) listed' : 'As described'}</p>
        <p class="text-sm text-gray-500 italic mt-2">Category selected is provisional.</p>
        <p class="text-sm mt-1"><strong>Category:</strong> ${formData.value.intake_category}</p>
      </div>
    `
    addBotMessage(html)
    setTimeout(() => {
      askOptions('Is this correct? Submitting will securely save this report.', [
        { value: 'submit', label: 'Yes, Submit Report', icon: '✅' },
        { value: 'edit', label: 'No, Start Over', icon: '🔄' }
      ])
    }, 1000)
  }

  const submitReport = async () => {
    try {
      isTyping.value = true
      formData.value.description = formData.value.description || "No description provided." // Safety

      console.log('Submitting Payload:', JSON.stringify(formData.value, null, 2))

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
      } else {
        throw new Error('Reference number missing')
      }
    } catch (err) {
      let msg = 'Submission failed. Network or Server Error.'
      if (err.response?.data?.detail) msg = err.response.data.detail
      errorMessage(msg)
    } finally {
      isTyping.value = false
    }
  }

  const errorMessage = (msg) => {
    addBotMessage(`<span class="text-red-600 font-bold">❌ Error:</span> ${msg}`)
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
