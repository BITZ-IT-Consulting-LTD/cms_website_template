<template>
    <div class="stats-card">
        <div class="flex items-center justify-between">
            <div>
                <p class="text-sm font-medium text-gray-600">{{ label }}</p>
                <p class="text-3xl font-bold mt-2" :class="valueColor">{{ value }}</p>
                <p v-if="subtitle" class="text-xs text-gray-500 mt-1">{{ subtitle }}</p>
            </div>
            <div class="p-3 rounded-lg" :class="iconBgColor">
                <component :is="icon" class="h-8 w-8" :class="iconColor" />
            </div>
        </div>
    </div>
</template>

<script setup>
    import { computed } from 'vue'

    const props = defineProps({
        label: {
            type: String,
            required: true
        },
        value: {
            type: [String, Number],
            required: true
        },
        subtitle: {
            type: String,
            default: null
        },
        icon: {
            type: [Object, Function],
            required: true
        },
        color: {
            type: String,
            default: 'blue',
            validator: (value) => ['blue', 'green', 'orange', 'red', 'purple', 'gray', 'amber'].includes(value)
        }
    })

    const colorMap = {
        blue: {
            value: 'text-gray-900',
            iconBg: 'bg-blue-100',
            icon: 'text-blue-600'
        },
        green: {
            value: 'text-green-600',
            iconBg: 'bg-green-100',
            icon: 'text-green-600'
        },
        orange: {
            value: 'text-orange-600',
            iconBg: 'bg-orange-100',
            icon: 'text-orange-600'
        },
        amber: {
            value: 'text-amber-600',
            iconBg: 'bg-amber-100',
            icon: 'text-amber-600'
        },
        red: {
            value: 'text-red-600',
            iconBg: 'bg-red-100',
            icon: 'text-red-600'
        },
        purple: {
            value: 'text-purple-600',
            iconBg: 'bg-purple-100',
            icon: 'text-purple-600'
        },
        gray: {
            value: 'text-gray-900',
            iconBg: 'bg-gray-100',
            icon: 'text-gray-600'
        }
    }

    const valueColor = computed(() => colorMap[props.color]?.value || colorMap.blue.value)
    const iconBgColor = computed(() => colorMap[props.color]?.iconBg || colorMap.blue.iconBg)
    const iconColor = computed(() => colorMap[props.color]?.icon || colorMap.blue.icon)
</script>
