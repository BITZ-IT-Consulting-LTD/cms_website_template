<template>
    <Teleport to="body">
        <Transition name="modal">
            <div v-if="isOpen"
                class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm"
                @click.self="handleClose">
                <div :class="[
                    'relative w-full bg-white rounded-xl shadow-2xl overflow-hidden max-h-[90vh] flex flex-col',
                    sizeClass
                ]" @click.stop>
                    <!-- Header -->
                    <div
                        class="flex items-center justify-between p-6 border-b border-gray-200 bg-gray-50 flex-shrink-0">
                        <h3 class="text-lg font-semibold text-gray-900">{{ title }}</h3>
                        <button @click="handleClose"
                            class="p-2 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-full transition-colors"
                            aria-label="Close modal">
                            <XMarkIcon class="h-5 w-5" />
                        </button>
                    </div>

                    <!-- Content -->
                    <div class="flex-1 overflow-y-auto p-6">
                        <slot />
                    </div>

                    <!-- Footer -->
                    <div
                        class="flex justify-between items-center p-6 border-t border-gray-200 bg-gray-50 flex-shrink-0">
                        <div>
                            <slot name="footer-left" />
                        </div>
                        <div class="flex gap-3">
                            <button @click="handleClose"
                                class="px-6 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 font-medium"
                                :disabled="loading">
                                {{ cancelLabel }}
                            </button>
                            <button @click="handleSubmit"
                                class="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium disabled:opacity-50 disabled:cursor-not-allowed"
                                :disabled="loading || submitDisabled">
                                <span v-if="loading" class="flex items-center">
                                    <svg class="animate-spin -ml-1 mr-3 h-4 w-4 text-white" fill="none"
                                        viewBox="0 0 24 24">
                                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor"
                                            stroke-width="4"></circle>
                                        <path class="opacity-75" fill="currentColor"
                                            d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                                        </path>
                                    </svg>
                                    {{ loadingLabel }}
                                </span>
                                <span v-else>{{ submitLabel }}</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </Transition>
    </Teleport>
</template>

<script setup>
    import { onMounted, onUnmounted, watch } from 'vue'
    import { XMarkIcon } from '@heroicons/vue/24/outline'

    const props = defineProps({
        isOpen: {
            type: Boolean,
            required: true
        },
        title: {
            type: String,
            required: true
        },
        submitLabel: {
            type: String,
            default: 'Save'
        },
        cancelLabel: {
            type: String,
            default: 'Cancel'
        },
        loadingLabel: {
            type: String,
            default: 'Saving...'
        },
        loading: {
            type: Boolean,
            default: false
        },
        submitDisabled: {
            type: Boolean,
            default: false
        },
        size: {
            type: String,
            default: 'large',
            validator: (value) => ['small', 'medium', 'large'].includes(value)
        }
    })

    const emit = defineEmits(['close', 'submit'])

    const sizeClass = {
        small: 'max-w-lg',
        medium: 'max-w-2xl',
        large: 'max-w-3xl'
    }[props.size]

    const handleClose = () => {
        if (!props.loading) {
            emit('close')
        }
    }

    const handleSubmit = () => {
        emit('submit')
    }

    const handleEscape = (e) => {
        if (e.key === 'Escape' && props.isOpen && !props.loading) {
            handleClose()
        }
    }

    watch(() => props.isOpen, (newValue) => {
        if (newValue) {
            document.body.style.overflow = 'hidden'
        } else {
            document.body.style.overflow = ''
        }
    })

    onMounted(() => {
        document.addEventListener('keydown', handleEscape)
    })

    onUnmounted(() => {
        document.removeEventListener('keydown', handleEscape)
        document.body.style.overflow = ''
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

    .modal-enter-active .relative,
    .modal-leave-active .relative {
        transition: transform 0.3s ease, opacity 0.3s ease;
    }

    .modal-enter-from .relative,
    .modal-leave-to .relative {
        transform: scale(0.9);
        opacity: 0;
    }
</style>
