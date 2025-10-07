<template>
  <div class="section-padding">
    <div class="container-custom max-w-6xl">
      <h1 class="text-center mb-12">Contact Us</h1>
      
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
        <!-- Contact Information -->
        <div>
          <h2 class="text-2xl font-bold mb-6">Get in Touch</h2>
          
          <div class="space-y-6">
            <div class="flex items-start space-x-4">
              <div class="bg-gray-100 p-3 rounded-lg">
                <svg class="w-6 h-6 text-gray-800" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"/>
                </svg>
              </div>
              <div>
                <h3 class="font-semibold text-gray-900 mb-1">Hotline</h3>
                <a href="tel:116" class="text-2xl font-bold text-secondary-500 hover:text-secondary-600">116</a>
                <p class="text-sm text-gray-600">Toll-free · 24/7</p>
              </div>
            </div>

            <div class="flex items-start space-x-4">
              <div class="bg-gray-100 p-3 rounded-lg">
                <svg class="w-6 h-6 text-gray-800" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/>
                </svg>
              </div>
              <div>
                <h3 class="font-semibold text-gray-900 mb-1">WhatsApp</h3>
                <a href="https://wa.me/256123456789" target="_blank" class="text-secondary-500 hover:text-secondary-600">+256 123 456 789</a>
              </div>
            </div>

            <div class="flex items-start space-x-4">
              <div class="bg-gray-100 p-3 rounded-lg">
                <svg class="w-6 h-6 text-gray-800" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"/>
                  <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"/>
                </svg>
              </div>
              <div>
                <h3 class="font-semibold text-gray-900 mb-1">Email</h3>
                <a href="mailto:info@sauti.mglsd.go.ug" class="text-secondary-500 hover:text-secondary-600">info@sauti.mglsd.go.ug</a>
              </div>
            </div>

            <div class="flex items-start space-x-4">
              <div class="bg-gray-100 p-3 rounded-lg">
                <svg class="w-6 h-6 text-gray-800" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/>
                </svg>
              </div>
              <div>
                <h3 class="font-semibold text-gray-900 mb-1">Office</h3>
                <p class="text-gray-700">Ministry of Gender, Labour & Social Development<br/>Kampala, Uganda</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Contact Form -->
        <div class="card card-body">
          <h2 class="text-2xl font-bold mb-6">Send Us a Message</h2>
          <form @submit.prevent="submitForm" class="space-y-4">
            <div>
              <label class="form-label">Name</label>
              <input v-model="form.name" type="text" class="form-input" required />
            </div>
            <div>
              <label class="form-label">Email</label>
              <input v-model="form.email" type="email" class="form-input" required />
            </div>
            <div>
              <label class="form-label">Subject</label>
              <input v-model="form.subject" type="text" class="form-input" required />
            </div>
            <div>
              <label class="form-label">Message</label>
              <textarea v-model="form.message" rows="5" class="form-textarea" required></textarea>
            </div>
            <button type="submit" class="btn-primary w-full bg-secondary-500 hover:bg-secondary-600 focus:ring-secondary-400">Send Message</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue'

const form = reactive({ name: '', email: '', subject: '', message: '' })

function submitForm() {
  alert('Contact form submitted! (Integration pending)')
}
</script>
