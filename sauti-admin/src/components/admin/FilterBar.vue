<template>
    <div class="bg-white p-4 rounded-lg shadow-sm mb-6">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <!-- Search Input -->
            <div class="relative">
                <MagnifyingGlassIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
                <input :value="modelValue.search" @input="updateFilter('search', $event.target.value)" type="text"
                    :placeholder="searchPlaceholder"
                    class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500" />
            </div>

            <!-- Status Filter -->
            <select v-if="statusOptions" :value="modelValue.status"
                @change="updateFilter('status', $event.target.value)"
                class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500">
                <option value="">{{ statusLabel }}</option>
                <option v-for="option in statusOptions" :key="option.value" :value="option.value">
                    {{ option.label }}
                </option>
            </select>

            <!-- Custom Filter Slot -->
            <slot name="custom-filter">
                <select v-if="customOptions" :value="modelValue.custom"
                    @change="updateFilter('custom', $event.target.value)"
                    class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500">
                    <option value="">{{ customLabel }}</option>
                    <option v-for="option in customOptions" :key="option.value" :value="option.value">
                        {{ option.label }}
                    </option>
                </select>
            </slot>
        </div>

        <!-- Clear Filters -->
        <div v-if="hasActiveFilters" class="mt-3 flex justify-end">
            <button @click="clearFilters" class="text-sm text-primary-600 hover:text-primary-800 font-medium">
                Clear all filters
            </button>
        </div>
    </div>
</template>

<script setup>
    import { computed } from 'vue'
    import { MagnifyingGlassIcon } from '@heroicons/vue/24/outline'

    const props = defineProps({
        modelValue: {
            type: Object,
            required: true
        },
        searchPlaceholder: {
            type: String,
            default: 'Search...'
        },
        statusOptions: {
            type: Array,
            default: null
        },
        statusLabel: {
            type: String,
            default: 'All Status'
        },
        customOptions: {
            type: Array,
            default: null
        },
        customLabel: {
            type: String,
            default: 'All'
        }
    })

    const emit = defineEmits(['update:modelValue'])

    const hasActiveFilters = computed(() => {
        return Object.values(props.modelValue).some(value => value !== '' && value !== null)
    })

    const updateFilter = (key, value) => {
        emit('update:modelValue', {
            ...props.modelValue,
            [key]: value
        })
    }

    const clearFilters = () => {
        const clearedFilters = Object.keys(props.modelValue).reduce((acc, key) => {
            acc[key] = ''
            return acc
        }, {})
        emit('update:modelValue', clearedFilters)
    }
</script>
