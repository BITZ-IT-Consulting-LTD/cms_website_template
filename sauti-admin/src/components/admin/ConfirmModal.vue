<template>
    <Teleport to="body">
        <Transition name="modal">
            <div v-if="isOpen"
                class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm"
                @click.self="handleClose">
                <div class="relative w-full max-w-md bg-white rounded-xl shadow-2xl overflow-hidden" @click.stop>
                    <!-- Icon -->
                    <div class="p-6 text-center">
                        <div class="mx-auto flex items-center justify-center h-12 w-12 rounded-full"
                            :class="iconBgClass">
                            <component :is="iconComponent" class="h-6 w-6" :class="iconClass" />
                        </div>

                        <!-- Title -->
                        <h3 class="mt-4 text-lg font-semibold text-gray-900">{{ title }}</h3>

                        <!-- Message -->
                        <p class="mt-2 text-sm text-gray-600">{{ message }}</p>
                    </div>

                    <!-- Actions -->
                    <div class="flex gap-3 p-6 bg-gray-50 border-t border-gray-200">
                        <button @click="handleClose"
                            class="flex-1 px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 font-medium"
                            :disabled="loading">
                            {{ cancelLabel }}
                        </button>
                        <button @click="handleConfirm"
                            class="flex-1 px-4 py-2 rounded-lg font-medium disabled:opacity-50 disabled:cursor-not-allowed"
                            :class="confirmButtonClass" :disabled="loading">
                            <span v-if="loading" class="flex items-center justify-center">
                                <svg class="animate-spin -ml-1 mr-2 h-4 w-4" fill="none" viewBox="0 0 24 24">
                                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor"
                                        stroke-width="4"></circle>
                                    <path class="opacity-75" fill="currentColor"
                                        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                                    </path>
                                </svg>
                                {{ loadingLabel }}
                            </span>
                            <span v-else>{{ confirmLabel }}</span>
                        </button>
                    </div>
                </div>
            </div>
        </Transition>
    </Teleport>
</template>

<script setup>
    import { computed, onMounted, onUnmounted } from 'vue'
    import { ExclamationTriangleIcon, InformationCircleIcon, CheckCircleIcon } from '@heroicons/vue/24/outline'

    const props = defineProps({
        isOpen: {
            type: Boolean,
            required: true
        },
        title: {
            type: String,
            required: true
        },
        message: {
            type: String,
            required: true
        },
        confirmLabel: {
            type: String,
            default: 'Confirm'
        },
        cancelLabel: {
            type: String,
            default: 'Cancel'
        },
        loadingLabel: {
            type: String,
            default: 'Processing...'
        },
        loading: {
            type: Boolean,
            default: false
        },
        variant: {
            type: String,
            default: 'danger',
            validator: (value) => ['danger', 'warning', 'info', 'success'].includes(value)
        }
    })

    const emit = defineEmits(['close', 'confirm'])

    const variantConfig = {
        danger: {
            icon: ExclamationTriangleIcon,
            iconBg: 'bg-red-100',
            iconColor: 'text-red-600',
            buttonClass: 'bg-red-600 text-white hover:bg-red-700'
        },
        warning: {
            icon: ExclamationTriangleIcon,
            iconBg: 'bg-orange-100',
            iconColor: 'text-orange-600',
            buttonClass: 'bg-orange-600 text-white hover:bg-orange-700'
        },
        info: {
            icon: InformationCircleIcon,
            iconBg: 'bg-blue-100',
            iconColor: 'text-blue-600',
            buttonClass: 'bg-blue-600 text-white hover:bg-blue-700'
        },
        success: {
            icon: CheckCircleIcon,
            iconBg: 'bg-green-100',
            iconColor: 'text-green-600',
            buttonClass: 'bg-green-600 text-white hover:bg-green-700'
        }
    }

    const iconComponent = computed(() => variantConfig[props.variant].icon)
    const iconBgClass = computed(() => variantConfig[props.variant].iconBg)
    const iconClass = computed(() => variantConfig[props.variant].iconColor)
    const confirmButtonClass = computed(() => variantConfig[props.variant].buttonClass)

    const handleClose = () => {
        if (!props.loading) {
            emit('close')
        }
    }

    const handleConfirm = () => {
        emit('confirm')
    }

    const handleEscape = (e) => {
        if (e.key === 'Escape' && props.isOpen && !props.loading) {
            handleClose()
        }
    }

    onMounted(() => {
        document.addEventListener('keydown', handleEscape)
    })

    onUnmounted(() => {
        document.removeEventListener('keydown', handleEscape)
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
