<template>
  <div class="max-w-3xl mx-auto" :key="currentStep">
    <!-- Progress Steps -->
    <div class="mb-8">
      <div class="flex items-center justify-between mb-4">
        <span class="text-sm text-primary-600 font-medium">Step {{ currentStep + 1 }} of {{ steps.length }}</span>
      </div>
      <!-- Progress bar -->
      <div class="h-2 bg-gray-200 rounded-full overflow-hidden">
        <div class="h-full bg-primary-500 transition-all duration-300" :style="{ width: progressPercent + '%' }"></div>
      </div>
    </div>

    <!-- Form Card -->
    <div class="bg-white rounded-2xl shadow-lg p-8">
      <!-- Step 1: Category Selection -->
      <div v-show="currentStep === 0" class="space-y-6">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Select Report Category</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <label
            v-for="category in categories"
            :key="category.value"
            class="relative cursor-pointer"
          >
            <input
              type="radio"
              v-model="form.category"
              :value="category.value"
              class="sr-only peer"
              required
            />
            <div class="border-2 border-gray-200 rounded-xl p-6 hover:border-primary-300 peer-checked:border-primary-500 peer-checked:bg-primary-50 transition-all">
              <div class="flex items-start space-x-4">
                <div :class="category.iconClass" class="p-3 rounded-lg">
                  <div class="w-6 h-6 rounded-full" :class="category.dotColor"></div>
                </div>
                <div class="flex-1">
                  <h3 class="font-semibold text-gray-900 mb-1">{{ category.label }}</h3>
                  <p class="text-sm text-gray-600">{{ category.description }}</p>
                </div>
              </div>
            </div>
          </label>
        </div>
      </div>

      <!-- Step 2: Your Information & Incident Details -->
      <div v-show="currentStep === 1" class="space-y-8">
        <!-- Your Information Section -->
        <div>
          <h3 class="text-lg font-bold text-gray-900 mb-4">Your Information (Optional)</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Name</label>
              <input
                type="text"
                v-model="form.contact_name"
                class="w-full px-4 py-3 border border-gray-200 rounded-lg bg-gray-50 focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                placeholder="E.g., Jane Doe"
              />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Phone Number</label>
              <input
                type="tel"
                v-model="form.contact_phone"
                class="w-full px-4 py-3 border border-gray-200 rounded-lg bg-gray-50 focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                placeholder="E.g., 0771234567"
              />
            </div>
          </div>
          <p class="text-sm text-gray-600 mt-3">You can remain anonymous. Providing contact information helps us to follow up if needed.</p>
        </div>

        <!-- Incident Details Section -->
        <div>
          <h3 class="text-lg font-bold text-gray-900 mb-4">Incident Details</h3>
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Type of Incident</label>
              <select
                v-model="form.incident_type"
                class="w-full px-4 py-3 border border-gray-200 rounded-lg bg-gray-50 focus:ring-2 focus:ring-primary-500 focus:border-primary-500 appearance-none"
                required
              >
                <option value="">Select the type of abuse</option>
                <option value="physical">Physical Abuse</option>
                <option value="sexual">Sexual Abuse</option>
                <option value="emotional">Emotional Abuse</option>
                <option value="neglect">Neglect</option>
                <option value="exploitation">Exploitation</option>
                <option value="other">Other</option>
              </select>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Describe what happened</label>
              <textarea
                v-model="form.description"
                rows="6"
                class="w-full px-4 py-3 border border-gray-200 rounded-lg bg-gray-50 focus:ring-2 focus:ring-primary-500 focus:border-primary-500 resize-none"
                placeholder="Please provide as much detail as possible. Who was involved? Where and when did it happen?"
                required
              ></textarea>
            </div>
          </div>
        </div>
      </div>

      <!-- Step 3: Review -->
      <div v-show="currentStep === 2" class="space-y-6">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Review Your Report</h2>
        
        <div class="space-y-4">
          <div class="bg-gray-50 p-4 rounded-lg">
            <h3 class="font-semibold text-gray-900 mb-2">Category</h3>
            <p class="text-gray-700">{{ getCategoryLabel(form.category) }}</p>
          </div>

          <div v-if="form.contact_name || form.contact_phone" class="bg-gray-50 p-4 rounded-lg">
            <h3 class="font-semibold text-gray-900 mb-2">Contact Information</h3>
            <div class="space-y-1 text-gray-700">
              <p v-if="form.contact_name">Name: {{ form.contact_name }}</p>
              <p v-if="form.contact_phone">Phone: {{ form.contact_phone }}</p>
            </div>
          </div>

          <div class="bg-gray-50 p-4 rounded-lg">
            <h3 class="font-semibold text-gray-900 mb-2">Incident Type</h3>
            <p class="text-gray-700">{{ getIncidentTypeLabel(form.incident_type) }}</p>
          </div>

          <div class="bg-gray-50 p-4 rounded-lg">
            <h3 class="font-semibold text-gray-900 mb-2">Description</h3>
            <p class="text-gray-700 whitespace-pre-wrap">{{ form.description }}</p>
          </div>
        </div>

        <div class="bg-yellow-50 border-l-4 border-yellow-400 p-4 rounded">
          <p class="text-sm text-yellow-700">
            <strong>Important:</strong> By submitting this report, you confirm that the information provided is accurate to the best of your knowledge. Your report will be handled confidentially by our team.
          </p>
        </div>
      </div>

      <!-- Error Message -->
      <div v-if="error" class="bg-red-50 border-l-4 border-red-400 p-4 rounded mb-4">
        <p class="text-sm text-red-700">{{ error }}</p>
      </div>

      <!-- Navigation Buttons -->
      <div class="flex justify-end pt-6 border-t">
        <button
          v-if="currentStep < steps.length - 1"
          type="button"
          @click="nextStep"
          class="px-6 py-3 bg-primary-500 text-white rounded-lg hover:bg-primary-600 transition-colors flex items-center"
        >
          Next Step
          <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
          </svg>
        </button>
        <button
          v-else
          type="button"
          @click="handleSubmit"
          class="px-6 py-3 bg-primary-500 text-white rounded-lg hover:bg-primary-600 transition-colors flex items-center"
          :disabled="submitting"
        >
          <span v-if="!submitting">Submit Report</span>
          <span v-else class="flex items-center">
            <span class="spinner w-5 h-5 mr-2"></span>
            Submitting...
          </span>
        </button>
      </div>
    </div>

    <!-- Success Modal -->
    <Teleport to="body">
      <Transition name="modal">
        <div
          v-if="showSuccess"
          class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black bg-opacity-50"
        >
          <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full p-8 text-center">
            <div class="bg-green-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-10 h-10 text-green-600" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
              </svg>
            </div>

            <h2 class="text-2xl font-bold text-gray-900 mb-2">Report Submitted Successfully</h2>
            
            <p class="text-gray-600 mb-4">
              Your report has been received and will be reviewed by our team.
            </p>

            <div v-if="referenceNumber" class="bg-primary-50 p-4 rounded-lg mb-6">
              <p class="text-sm text-gray-600 mb-1">Reference Number:</p>
              <p class="text-xl font-bold text-primary-600">{{ referenceNumber }}</p>
              <p class="text-xs text-gray-500 mt-2">Save this number to track your report</p>
            </div>

            <button
              @click="resetForm"
              class="w-full px-6 py-3 bg-primary-500 text-white rounded-lg hover:bg-primary-600 transition-colors mb-3"
            >
              Submit Another Report
            </button>

            <router-link
              to="/"
              class="block text-primary-600 hover:text-primary-700 text-sm font-medium"
            >
              Return to Home
            </router-link>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import { api } from '@/utils/axios'

const steps = ['Category', 'Details', 'Review']
const currentStep = ref(0)
const submitting = ref(false)
const error = ref(null)
const showSuccess = ref(false)
const referenceNumber = ref('')

const progressPercent = computed(() => ((currentStep.value + 1) / steps.length) * 100)

const categories = [
  {
    value: 'CHILD_PROTECTION',
    label: 'Child Protection',
    description: 'Abuse, neglect, or exploitation of children',
    iconClass: 'bg-blue-100',
    dotColor: 'bg-blue-400',
  },
  {
    value: 'GBV',
    label: 'Gender-Based Violence',
    description: 'Domestic violence, sexual violence, or harassment',
    iconClass: 'bg-purple-100',
    dotColor: 'bg-purple-400',
  },
  {
    value: 'MIGRANT',
    label: 'Migrant Worker',
    description: 'Exploitation, trafficking, or unsafe migration',
    iconClass: 'bg-teal-100',
    dotColor: 'bg-teal-400',
  },
  {
    value: 'PSEA',
    label: 'PSEA',
    description: 'Sexual exploitation by aid workers or officials',
    iconClass: 'bg-orange-100',
    dotColor: 'bg-orange-400',
  },
]

const form = reactive({
  category: '',
  contact_name: '',
  contact_phone: '',
  incident_type: '',
  description: '',
})

function nextStep() {
  if (validateCurrentStep()) {
    currentStep.value++
  }
}

function validateCurrentStep() {
  error.value = null

  if (currentStep.value === 0 && !form.category) {
    error.value = 'Please select a category'
    return false
  }

  if (currentStep.value === 1) {
    if (!form.incident_type) {
      error.value = 'Please select the type of incident'
      return false
    }
    if (!form.description || form.description.trim().length < 20) {
      error.value = 'Please provide a detailed description (at least 20 characters)'
      return false
    }
  }

  return true
}

async function handleSubmit() {
  if (!validateCurrentStep()) return

  submitting.value = true
  error.value = null

  try {
    const response = await api.reports.submit(form)
    referenceNumber.value = response.data.reference_number
    showSuccess.value = true
  } catch (err) {
    error.value = err.response?.data?.detail || 'Failed to submit report. Please try again.'
    console.error('Report submission error:', err)
  } finally {
    submitting.value = false
  }
}

function resetForm() {
  Object.keys(form).forEach(key => {
    form[key] = ''
  })
  currentStep.value = 0
  showSuccess.value = false
  referenceNumber.value = ''
  error.value = null
}

function getCategoryLabel(value) {
  return categories.find(c => c.value === value)?.label || value
}

function getIncidentTypeLabel(value) {
  const types = {
    physical: 'Physical Abuse',
    sexual: 'Sexual Abuse',
    emotional: 'Emotional Abuse',
    neglect: 'Neglect',
    exploitation: 'Exploitation',
    other: 'Other'
  }
  return types[value] || value
}
</script>
