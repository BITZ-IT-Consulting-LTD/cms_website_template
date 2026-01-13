<template>
    <!-- 
    SAUTI 116 BRAND COMPLIANCE: PART 6 — LOGO USAGE RULES
    - No stretching (object-fit: contain)
    - No recolouring (pristine assets)
    - No shadows or effects (filter: none)
    - Required exclusion space (standardized padding)
    - Minimum readable size (enforced via size classes)
  -->
    <div class="logo-container" :class="[variant, sizeClass]" :style="containerStyle">
        <img v-if="logoSrc" :src="logoSrc" :alt="alt" class="logo-img" @error="handleError" />
        <span v-else class="logo-fallback">{{ fallbackInitial }}</span>
    </div>
</template>

<script setup>
    import { computed } from 'vue'
    import { useSettingsStore } from '@/store/settings'

    const props = defineProps({
        variant: {
            type: String,
            default: 'default', // 'default', 'white', 'partner'
        },
        size: {
            type: String,
            default: 'md', // 'sm', 'md', 'lg', 'auto'
        },
        alt: {
            type: String,
            default: 'Sauti Logo',
        },
        customSrc: {
            type: String,
            default: null,
        }
    })

    const settingsStore = useSettingsStore()
    const settings = computed(() => settingsStore.settings)
    const orgProfile = computed(() => settingsStore.orgProfile)

    const logoSrc = computed(() => {
        if (props.customSrc) return props.customSrc

        if (props.variant === 'white' && settings.value.logo_white) {
            return settings.value.logo_white
        }

        // Priority 1: Organization Profile Logo (from Master Data)
        if (orgProfile.value && orgProfile.value.logo) {
            return orgProfile.value.logo
        }

        // Priority 2: Legacy Site Settings Logo
        return settings.value.logo
    })

    const fallbackInitial = computed(() => {
        return props.alt.charAt(0).toUpperCase()
    })

    const sizeClass = computed(() => `logo-${props.size}`)

    const containerStyle = computed(() => {
        // Enforce required exclusion (clear) space
        // Standard brand exclusion space is often 1/4 of logo height or a fixed minimum
        return {
            padding: props.size === 'sm' ? '0.25rem' : '0.5rem',
        }
    })

    const handleError = (e) => {
        console.error('Logo failed to load:', e.target.src)
        // Optionally set a fallback or hide
    }
</script>

<style scoped>
    .logo-container {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        /* Brand Rule: No stretched logos */
        aspect-ratio: auto;
    }

    .logo-img {
        width: 100%;
        height: 100%;
        /* Brand Rule: No stretching */
        object-fit: contain;
        /* Brand Rule: No shadows or effects on the logo itself */
        filter: none !important;
        box-shadow: none !important;
        display: block;
    }

    /* Minimum readable sizes */
    .logo-sm {
        height: 32px;
        /* Minimum for mobile/small spots */
        min-width: 32px;
    }

    .logo-md {
        height: 56px;
        min-width: 56px;
    }

    .logo-lg {
        height: 80px;
        min-width: 80px;
    }

    .logo-auto {
        height: 100%;
        width: 100%;
    }

    .logo-fallback {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        color: theme('colors.primary');
    }

    /* Variant-specific adjustments if needed */
    .white .logo-fallback {
        color: theme('colors.neutral-white');
    }
</style>
