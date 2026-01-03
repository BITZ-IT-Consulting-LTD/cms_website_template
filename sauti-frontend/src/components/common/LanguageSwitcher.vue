<template>
  <div class="relative">
    <button
      @click="isOpen = !isOpen"
      class="flex items-center space-x-2 px-3 py-2 rounded-lg hover:bg-gray-100 transition-colors focus:ring-2 focus:ring-blue-500 focus:outline-none"
      aria-label="Change language"
      :aria-expanded="isOpen"
      aria-haspopup="true"
    >
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129"/>
      </svg>
      <span class="font-medium">{{ currentLanguage.name }}</span>
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
      </svg>
    </button>

    <!-- Dropdown -->
    <Transition name="fade">
      <div
        v-if="isOpen"
        v-click-outside="closeDropdown"
        class="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg py-2 z-50"
      >
        <button
          v-for="lang in languages"
          :key="lang.code"
          @click="changeLanguage(lang.code)"
          class="w-full text-left px-4 py-2 hover:bg-gray-100 transition-colors"
          :class="{ 'bg-primary-50 text-primary-600': currentLanguageCode === lang.code }"
        >
          <div class="flex items-center justify-between">
            <span>{{ lang.name }}</span>
            <span class="text-xs text-gray-500">{{ lang.nativeName }}</span>
          </div>
        </button>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const isOpen = ref(false)
const currentLanguageCode = ref(localStorage.getItem('language') || 'en')

const languages = [
  { code: 'en', name: 'English', nativeName: 'English' },
  { code: 'lg', name: 'Luganda', nativeName: 'Luganda' },
  { code: 'sw', name: 'Swahili', nativeName: 'Kiswahili' },
]

const currentLanguage = computed(() => {
  return languages.find(lang => lang.code === currentLanguageCode.value) || languages[0]
})

function changeLanguage(code) {
  currentLanguageCode.value = code
  localStorage.setItem('language', code)
  isOpen.value = false
  
  // Emit event for other components to react
  window.dispatchEvent(new CustomEvent('language-changed', { detail: code }))
  
  // Reload page to apply language change
  // In production, you'd use a proper i18n solution
  window.location.reload()
}

function closeDropdown() {
  isOpen.value = false
}

// Click outside directive
const vClickOutside = {
  mounted(el, binding) {
    el.clickOutsideEvent = (event) => {
      if (!(el === event.target || el.contains(event.target))) {
        binding.value()
      }
    }
    document.addEventListener('click', el.clickOutsideEvent)
  },
  unmounted(el) {
    document.removeEventListener('click', el.clickOutsideEvent)
  },
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
