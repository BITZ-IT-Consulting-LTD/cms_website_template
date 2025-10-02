<template>
  <div class="max-w-3xl mx-auto">
    <!-- Progress Steps -->
    <div class="mb-8">
      <div class="flex items-center justify-between">
        <div
          v-for="(step, index) in steps"
          :key="index"
          class="flex-1 flex items-center"
        >
          <div
            class="flex items-center justify-center w-10 h-10 rounded-full border-2 transition-colors"
            :class="[
              currentStep > index
                ? 'bg-success-500 border-success-500 text-white'
                : currentStep === index
                ? 'bg-primary-500 border-primary-500 text-white'
                : 'bg-white border-gray-300 text-gray-500',
            ]"
          >
            <svg v-if="currentStep > index" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
            </svg>
            <span v-else>{{ index + 1 }}</span>
          </div>
          <div
            v-if="index < steps.length - 1"
            class="flex-1 h-1 mx-2 transition-colors"
            :class="currentStep > index ? 'bg-success-500' : 'bg-gray-300'"
          ></div>
        </div>
      </div>
      <div class="flex justify-between mt-2">
        <span
          v-for="(step, index) in steps"
          :key="index"
          class="text-sm font-medium"
          :class="currentStep >= index ? 'text-gray-900' : 'text-gray-500'"
        >
          {{ step }}
        </span>
      </div>
    </div>

    <!-- Form -->
    <form @submit.prevent="handleSubmit" class="card card-body">
      <!-- Step 1: Category Selection -->
      <div v-show="currentStep === 0" class="space-y-6">
        <h2 class="text-2xl font-bold text-gray-900 mb-4">Select Report Category</h2>
        
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
            <div class="card p-6 peer-checked:ring-2 peer-checked:ring-primary-500 peer-checked:bg-primary-50 transition-all">
              <div class="flex items-start space-x-4">
                <div :class="category.iconClass" class="p-3 rounded-lg">
                  <component :is="category.icon" class="w-6 h-6" />
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

      <!-- Step 2: Report Details -->
      <div v-show="currentStep === 1" class="space-y-6">
        <h2 class="text-2xl font-bold text-gray-900 mb-4">Describe What Happened</h2>
        
        <div>
          <label class="form-label">
            Description <span class="text-danger-500">*</span>
          </label>
          <textarea
            v-model="form.description"
            rows="8"
            class="form-textarea"
            placeholder="Please describe what happened in as much detail as you can..."
            required
          ></textarea>
          <p class="text-sm text-gray-500 mt-1">Be as detailed as possible. This helps us assist you better.</p>
        </div>

        <div>
          <label class="form-label">Location (District/Area)</label>
          <input
            type="text"
            v-model="form.location"
            class="form-input"
            placeholder="e.g., Kampala, Wakiso..."
          />
        </div>

        <div>
          <label class="form-label">Attachment (Optional)</label>
          <input
            type="file"
            @change="handleFileUpload"
            accept="image/*,.pdf,.doc,.docx"
            class="form-input"
          />
          <p class="text-sm text-gray-500 mt-1">You can attach photos, documents, or other evidence (max 5MB)</p>
        </div>
      </div>

      <!-- Step 3: Contact Information -->
      <div v-show="currentStep === 2" class="space-y-6">
        <h2 class="text-2xl font-bold text-gray-900 mb-4">Contact Information</h2>
        
        <div class="bg-blue-50 border-l-4 border-blue-400 p-4 rounded mb-6">
          <p class="text-sm text-blue-700">
            You can choose to submit this report anonymously or provide your contact information so we can follow up with you.
          </p>
        </div>

        <label class="flex items-start space-x-3 cursor-pointer">
          <input
            type="checkbox"
            v-model="form.is_anonymous"
            class="mt-1 w-5 h-5 text-primary-600 border-gray-300 rounded focus:ring-primary-500"
          />
          <div>
            <span class="font-medium text-gray-900">Submit Anonymously</span>
            <p class="text-sm text-gray-600">Your identity will not be recorded</p>
          </div>
        </label>

        <div v-if="!form.is_anonymous" class="space-y-4 pt-4">
          <div>
            <label class="form-label">Your Name</label>
            <input
              type="text"
              v-model="form.contact_name"
              class="form-input"
              placeholder="Full name"
            />
          </div>

          <div>
            <label class="form-label">Phone Number</label>
            <input
              type="tel"
              v-model="form.contact_phone"
              class="form-input"
              placeholder="+256..."
            />
          </div>

          <div>
            <label class="form-label">Email Address</label>
            <input
              type="email"
              v-model="form.contact_email"
              class="form-input"
              placeholder="your@email.com"
            />
          </div>
        </div>
      </div>

      <!-- Step 4: Confirmation -->
      <div v-show="currentStep === 3" class="space-y-6">
        <h2 class="text-2xl font-bold text-gray-900 mb-4">Review & Submit</h2>
        
        <div class="space-y-4">
          <div class="bg-gray-50 p-4 rounded-lg">
            <h3 class="font-semibold text-gray-900 mb-2">Category</h3>
            <p class="text-gray-700">{{ getCategoryLabel(form.category) }}</p>
          </div>

          <div class="bg-gray-50 p-4 rounded-lg">
            <h3 class="font-semibold text-gray-900 mb-2">Description</h3>
            <p class="text-gray-700 whitespace-pre-wrap">{{ form.description }}</p>
          </div>

          <div v-if="form.location" class="bg-gray-50 p-4 rounded-lg">
            <h3 class="font-semibold text-gray-900 mb-2">Location</h3>
            <p class="text-gray-700">{{ form.location }}</p>
          </div>

          <div class="bg-gray-50 p-4 rounded-lg">
            <h3 class="font-semibold text-gray-900 mb-2">Contact Information</h3>
            <p v-if="form.is_anonymous" class="text-gray-700">Submitted anonymously</p>
            <div v-else class="space-y-1 text-gray-700">
              <p v-if="form.contact_name">Name: {{ form.contact_name }}</p>
              <p v-if="form.contact_phone">Phone: {{ form.contact_phone }}</p>
              <p v-if="form.contact_email">Email: {{ form.contact_email }}</p>
            </div>
          </div>
        </div>

        <div class="bg-yellow-50 border-l-4 border-yellow-400 p-4 rounded">
          <p class="text-sm text-yellow-700">
            <strong>Important:</strong> By submitting this report, you confirm that the information provided is accurate to the best of your knowledge. Your report will be handled confidentially by our team.
          </p>
        </div>
      </div>

      <!-- Error Message -->
      <div v-if="error" class="bg-danger-50 border-l-4 border-danger-400 p-4 rounded">
        <p class="text-sm text-danger-700">{{ error }}</p>
      </div>

      <!-- Navigation Buttons -->
      <div class="flex justify-between pt-6 border-t">
        <button
          v-if="currentStep > 0"
          type="button"
          @click="previousStep"
          class="btn-outline"
          :disabled="submitting"
        >
          ← Previous
        </button>
        <div v-else></div>

        <button
          v-if="currentStep < steps.length - 1"
          type="button"
          @click="nextStep"
          class="btn-primary"
        >
          Next →
        </button>
        <button
          v-else
          type="submit"
          class="btn-primary"
          :disabled="submitting"
        >
          <span v-if="!submitting">Submit Report</span>
          <span v-else class="flex items-center">
            <span class="spinner w-5 h-5 mr-2"></span>
            Submitting...
          </span>
        </button>
      </div>
    </form>

    <!-- Success Modal -->
    <Teleport to="body">
      <Transition name="modal">
        <div
          v-if="showSuccess"
          class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black bg-opacity-50"
        >
          <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full p-8 text-center">
            <div class="bg-success-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-10 h-10 text-success-600" fill="currentColor" viewBox="0 0 20 20">
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

            <p class="text-sm text-gray-600 mb-6">
              We will review your report and take appropriate action. If you provided contact information, we may reach out to you for follow-up.
            </p>

            <button
              @click="resetForm"
              class="btn-primary w-full"
            >
              Submit Another Report
            </button>

            <router-link
              to="/"
              class="block mt-3 text-primary-600 hover:text-primary-700 text-sm font-medium"
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
import { ref, reactive } from 'vue'
import { api } from '@/utils/axios'

const steps = ['Category', 'Details', 'Contact', 'Review']
const currentStep = ref(0)
const submitting = ref(false)
const error = ref(null)
const showSuccess = ref(false)
const referenceNumber = ref('')

const categories = [
  {
    value: 'CHILD_PROTECTION',
    label: 'Child Protection',
    description: 'Abuse, neglect, or exploitation of children',
    iconClass: 'bg-blue-100 text-blue-600',
    icon: 'shield-icon',
  },
  {
    value: 'GBV',
    label: 'Gender-Based Violence',
    description: 'Domestic violence, sexual violence, or harassment',
    iconClass: 'bg-purple-100 text-purple-600',
    icon: 'heart-icon',
  },
  {
    value: 'MIGRANT',
    label: 'Migrant Worker',
    description: 'Exploitation, trafficking, or unsafe migration',
    iconClass: 'bg-teal-100 text-teal-600',
    icon: 'globe-icon',
  },
  {
    value: 'PSEA',
    label: 'PSEA',
    description: 'Sexual exploitation by aid workers or officials',
    iconClass: 'bg-orange-100 text-orange-600',
    icon: 'alert-icon',
  },
]

const form = reactive({
  category: '',
  description: '',
  location: '',
  is_anonymous: false,
  contact_name: '',
  contact_phone: '',
  contact_email: '',
  attachment: null,
})

function nextStep() {
  if (validateCurrentStep()) {
    currentStep.value++
  }
}

function previousStep() {
  currentStep.value--
  error.value = null
}

function validateCurrentStep() {
  error.value = null

  if (currentStep.value === 0 && !form.category) {
    error.value = 'Please select a category'
    return false
  }

  if (currentStep.value === 1) {
    if (!form.description || form.description.trim().length < 20) {
      error.value = 'Please provide a detailed description (at least 20 characters)'
      return false
    }
  }

  return true
}

function handleFileUpload(event) {
  const file = event.target.files[0]
  if (file) {
    if (file.size > 5 * 1024 * 1024) {
      error.value = 'File size must be less than 5MB'
      event.target.value = ''
      return
    }
    form.attachment = file
  }
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
    if (key === 'is_anonymous') {
      form[key] = false
    } else {
      form[key] = ''
    }
  })
  form.attachment = null
  currentStep.value = 0
  showSuccess.value = false
  referenceNumber.value = ''
  error.value = null
}

function getCategoryLabel(value) {
  return categories.find(c => c.value === value)?.label || value
}
</script>
