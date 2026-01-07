<template>
  <div>
    <button @click="showModal = true" class="btn-emergency" aria-label="Get help now">
      <svg class="w-5 h-5 inline mr-2" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd"
          d="M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11.707 4.707a1 1 0 00-1.414-1.414L10 9.586 8.707 8.293a1 1 0 00-1.414 0l-2 2a1 1 0 101.414 1.414L8 10.414l1.293 1.293a1 1 0 001.414 0l4-4z"
          clip-rule="evenodd" />
      </svg>
      Get Help Now
    </button>

    <!-- Help Modal -->
    <Teleport to="body">
      <Transition name="modal">
        <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black bg-opacity-50"
          @click.self="showModal = false">
          <div class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto" role="dialog"
            aria-labelledby="help-modal-title" aria-modal="true">
            <!-- Header -->
            <div class="bg-emergency text-neutral-white p-6 rounded-t-2xl relative">
              <button @click="showModal = false"
                class="absolute top-4 right-4 text-neutral-white hover:bg-secondary rounded-lg p-2 transition-colors focus:ring-2 focus:ring-neutral-white focus:outline-none"
                aria-label="Close" ref="closeButton">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
              <h2 id="help-modal-title" class="text-2xl font-bold mb-2">Get Help Now</h2>
              <p class="text-neutral-white/90">We're here to help you. All services are confidential and free.</p>
            </div>

            <!-- Content -->
            <div class="p-6 space-y-6">
              <!-- Emergency Hotline -->
              <div class="bg-neutral-white rounded-xl p-6 text-center border border-neutral-offwhite shadow-sm">
                <h3 class="text-lg font-bold text-secondary mb-2">Emergency Hotline</h3>
                <a href="tel:116" class="hotline-btn">
                  116
                </a>
                <p class="text-sm font-bold text-secondary">Reporting any form of violence. Call 116. Toll-free ·
                  Available 24/7</p>
              </div>

              <!-- Other Channels -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <!-- WhatsApp -->
                <a href="https://wa.me/256743889999" target="_blank"
                  class="card p-4 flex items-center space-x-3 focus:ring-2 focus:ring-primary focus:outline-none">
                  <div class="bg-neutral-offwhite p-3 rounded-lg">
                    <svg class="w-6 h-6 text-primary" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                      <path
                        d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" />
                    </svg>
                  </div>
                  <div class="flex-1">
                    <p class="font-bold text-secondary">WhatsApp</p>
                    <p class="text-xs text-secondary">Chat with us</p>
                  </div>
                </a>

                <!-- U-Report -->
                <a href="https://ureport.in" target="_blank"
                  class="card p-4 flex items-center space-x-3 focus:ring-2 focus:ring-primary focus:outline-none">
                  <div class="bg-neutral-offwhite p-3 rounded-lg">
                    <svg class="w-6 h-6 text-primary" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                      <path d="M2 5a2 2 0 012-2h7a2 2 0 012 2v4a2 2 0 01-2 2H9l-3 3v-3H4a2 2 0 01-2-2V5z" />
                      <path
                        d="M15 7v2a4 4 0 01-4 4H9.828l-1.766 1.767c.28.149.599.233.938.233h2l3 3v-3h2a2 2 0 002-2V9a2 2 0 00-2-2h-1z" />
                    </svg>
                  </div>
                  <div class="flex-1">
                    <p class="font-bold text-secondary">U-Report</p>
                    <p class="text-xs text-secondary">SMS reporting</p>
                  </div>
                </a>

                <!-- Online Report -->
                <router-link to="/report" @click="showModal = false"
                  class="card p-4 flex items-center space-x-3 focus:ring-2 focus:ring-primary focus:outline-none">
                  <div class="bg-neutral-offwhite p-3 rounded-lg">
                    <svg class="w-6 h-6 text-primary" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                      <path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z" />
                      <path fill-rule="evenodd"
                        d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z"
                        clip-rule="evenodd" />
                    </svg>
                  </div>
                  <div class="flex-1">
                    <p class="font-bold text-secondary">Online Form</p>
                    <p class="text-xs text-secondary">Submit report</p>
                  </div>
                </router-link>

                <!-- Email -->
                <a href="mailto:info@sauti.mglsd.go.ug"
                  class="card p-4 flex items-center space-x-3 focus:ring-2 focus:ring-primary focus:outline-none">
                  <div class="bg-neutral-offwhite p-3 rounded-lg">
                    <svg class="w-6 h-6 text-primary" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                      <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
                      <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
                    </svg>
                  </div>
                  <div class="flex-1">
                    <p class="font-bold text-secondary">Email</p>
                    <p class="text-xs text-secondary">Send us message</p>
                  </div>
                </a>
              </div>

              <!-- Safety Notice -->
              <div class="bg-accent-yellow/20 border-l-4 border-accent-yellow p-4 rounded">
                <div class="flex">
                  <svg class="w-5 h-5 text-secondary mt-0.5" fill="currentColor" viewBox="0 0 20 20"
                    aria-hidden="true">
                    <path fill-rule="evenodd"
                      d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z"
                      clip-rule="evenodd" />
                  </svg>
                  <div class="ml-3">
                    <p class="text-sm font-bold text-secondary">
                      Your safety is our priority. If you're in immediate danger, call 116 or the police. All our
                      services are confidential, compassionate, and free.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
  import { ref, watch, nextTick } from 'vue'

  const showModal = ref(false)
  const closeButton = ref(null)

  watch(showModal, async (isOpen) => {
    if (isOpen) {
      await nextTick()
      closeButton.value?.focus()
    }
  })
</script>

<style scoped>

  .modal-enter-active,
  .modal-leave-active {
    transition: opacity 0.3s ease;
  }

  .modal-enter-from,
  .modal-leave-to {
    opacity: 0;
  }

  .modal-enter-active>div,
  .modal-leave-active>div {
    transition: transform 0.3s ease;
  }

  .modal-enter-from>div,
  .modal-leave-to>div {
    transform: scale(0.9);
  }
</style>
