<template>
    <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-12 text-center">
        <component :is="icon" class="mx-auto h-12 w-12 text-gray-400 mb-4" />
        <h3 class="text-lg font-medium text-gray-900 mb-2">{{ title }}</h3>
        <p class="text-gray-600 mb-6 max-w-md mx-auto">{{ message }}</p>
        <slot name="action">
            <button v-if="actionLabel" @click="handleAction" class="btn-primary inline-flex items-center">
                <component v-if="actionIcon" :is="actionIcon" class="h-5 w-5 mr-2" />
                {{ actionLabel }}
            </button>
        </slot>
    </div>
</template>

<script setup>
    const props = defineProps({
        icon: {
            type: Object,
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
        actionLabel: {
            type: String,
            default: null
        },
        actionIcon: {
            type: Object,
            default: null
        }
    })

    const emit = defineEmits(['action'])

    const handleAction = () => {
        emit('action')
    }
</script>
