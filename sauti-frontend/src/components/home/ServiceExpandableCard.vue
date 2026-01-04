<template>
    <div class="bg-sauti-white rounded-3xl border transition-all duration-500 overflow-hidden group" :class="[
        isOpen ? 'border-sauti-blue shadow-xl ring-1 ring-sauti-blue' : 'border-sauti-neutral shadow-sm hover:shadow-lg'
    ]">
        <!-- Header (Always Visible) -->
        <button type="button"
            class="w-full text-left p-6 md:p-8 flex flex-col md:flex-row gap-6 md:items-center focus:outline-none focus:ring-2 focus:ring-inset focus:ring-sauti-blue transition-colors"
            :aria-expanded="isOpen" :aria-controls="`service-content-${service.id}`" @click="$emit('toggle')">
            <!-- Icon -->
            <div class="w-16 h-16 rounded-2xl flex items-center justify-center transition-colors duration-300 shrink-0"
                :class="isOpen ? 'bg-sauti-blue text-sauti-white' : 'bg-sauti-neutral text-sauti-blue group-hover:bg-sauti-blue group-hover:text-sauti-white'">
                <component :is="iconComponent" class="w-8 h-8" />
            </div>

            <!-- content -->
            <div class="flex-grow">
                <h3 :id="`service-title-text-${service.id}`"
                    class="text-xl font-bold text-sauti-darkGreen mb-2 transition-colors"
                    :class="{ 'text-sauti-blue': isOpen }">
                    {{ service.title }}
                </h3>
                <p v-show="!isOpen"
                    class="text-sauti-darkGreen line-clamp-2 md:line-clamp-none transition-opacity duration-300">
                    {{ service.summary }}
                </p>
            </div>

            <!-- Chevron -->
            <div class="shrink-0 flex items-center justify-center w-10 h-10 rounded-full bg-sauti-neutral text-sauti-darkGreen group-hover:bg-sauti-blue group-hover:text-sauti-white transition-all"
                :class="{ 'bg-sauti-blue text-sauti-white': isOpen }">
                <ChevronDownIcon class="w-6 h-6 transform transition-transform duration-300"
                    :class="{ 'rotate-180': isOpen }" />
            </div>
        </button>

        <!-- Expanded Content -->
        <div v-if="isOpen" :id="`service-content-${service.id}`" role="region"
            :aria-labelledby="`service-title-text-${service.id}`"
            class="border-t border-sauti-neutral bg-sauti-neutral/30 animate-fade-in">
            <div class="p-6 md:p-8 space-y-8">
                <!-- Intro & Scope -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div>
                        <h4 class="font-bold text-sauti-darkGreen mb-4 flex items-center gap-2">
                            <InformationCircleIcon class="w-5 h-5 text-sauti-blue" />
                            About this service
                        </h4>
                        <p class="text-sauti-darkGreen leading-relaxed">{{ service.intro_text }}</p>
                    </div>

                    <div v-if="service.scope_items && service.scope_items.length">
                        <h4 class="font-bold text-sauti-darkGreen mb-4 flex items-center gap-2">
                            <CheckCircleIcon class="w-5 h-5 text-sauti-lightGreen" />
                            What is included
                        </h4>
                        <ul class="space-y-2">
                            <li v-for="(item, idx) in service.scope_items" :key="idx"
                                class="flex items-start gap-2 text-sm text-sauti-darkGreen font-normal">
                                <CheckCircleIcon class="w-4 h-4 text-sauti-lightGreen mt-1 shrink-0" />
                                <span>{{ item }}</span>
                            </li>
                        </ul>
                    </div>
                </div>

                <!-- Steps -->
                <div v-if="service.steps && service.steps.length">
                    <h4 class="font-bold text-sauti-darkGreen mb-6 border-b border-sauti-neutral pb-2">How we help</h4>
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                        <div v-for="(step, idx) in service.steps" :key="step.id"
                            class="bg-sauti-white p-4 rounded-xl border border-sauti-neutral shadow-sm relative overflow-hidden">
                            <div
                                class="absolute -right-4 -top-4 w-16 h-16 bg-sauti-neutral rounded-full flex items-center justify-center text-4xl font-bold text-sauti-blue/10">
                                {{ idx + 1 }}
                            </div>
                            <h5 class="font-bold text-sauti-darkGreen mb-2 relative z-10">{{ step.title }}</h5>
                            <p class="text-sm text-sauti-darkGreen relative z-10 font-normal">{{ step.description }}</p>
                        </div>
                    </div>
                </div>

                <!-- CTA -->
                <div class="flex flex-wrap gap-4 pt-4 border-t border-sauti-neutral mt-4 justify-end">
                    <BaseCTA variant="emergency" :href="`tel:${hotlineNumber}`" external
                        class="w-full sm:w-auto justify-center font-bold">
                        CALL {{ hotlineNumber }} FOR HELP
                    </BaseCTA>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { computed } from 'vue'
    import BaseCTA from '@/components/common/BaseCTA.vue'
    import {
        ChevronDownIcon,
        InformationCircleIcon,
        CheckCircleIcon,
        UserGroupIcon,
        ShieldCheckIcon,
        GlobeAltIcon,
        ScaleIcon
    } from '@heroicons/vue/24/outline'

    const props = defineProps({
        service: {
            type: Object,
            required: true
        },
        isOpen: {
            type: Boolean,
            default: false
        },
        hotlineNumber: {
            type: String,
            default: '116'
        }
    })

    const emit = defineEmits(['toggle'])



    // Map string icon names to components
    const icons = {
        UserGroupIcon,
        ShieldCheckIcon,
        GlobeAltIcon,
        ScaleIcon
    }

    const iconComponent = computed(() => {
        return icons[props.service.icon_name] || ShieldCheckIcon
    })
</script>

<style scoped>
    .animate-fade-in {
        animation: fadeIn 0.3s ease-out;
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .line-clamp-2 {
        display: -webkit-box;
        -webkit-line-clamp: 2;
        line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
</style>
