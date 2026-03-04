import { ref } from 'vue'

/**
 * Composable for managing modal state
 * @returns {Object} Modal state and control functions
 */
export function useModal() {
    const isOpen = ref(false)
    const data = ref(null)

    const open = (initialData = null) => {
        data.value = initialData
        isOpen.value = true
    }

    const close = () => {
        isOpen.value = false
        // Clear data after animation completes
        setTimeout(() => {
            data.value = null
        }, 300)
    }

    const toggle = () => {
        if (isOpen.value) {
            close()
        } else {
            open()
        }
    }

    return {
        isOpen,
        data,
        open,
        close,
        toggle
    }
}
