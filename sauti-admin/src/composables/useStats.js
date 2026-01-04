import { computed } from 'vue'

/**
 * Composable for computing statistics from a list of items
 * @param {Ref<Array>} items - Reactive array of items
 * @param {Object} config - Configuration for stat calculations
 * @returns {Object} Computed statistics
 */
export function useStats(items, config = {}) {
    const total = computed(() => {
        return items.value?.length || 0
    })

    const active = computed(() => {
        if (!items.value) return 0
        return items.value.filter(item =>
            item.is_active === true || item.status === 'active'
        ).length
    })

    const inactive = computed(() => {
        if (!items.value) return 0
        return items.value.filter(item =>
            item.is_active === false || item.status === 'inactive'
        ).length
    })

    const published = computed(() => {
        if (!items.value) return 0
        return items.value.filter(item =>
            item.is_published === true || item.status === 'published'
        ).length
    })

    const draft = computed(() => {
        if (!items.value) return 0
        return items.value.filter(item =>
            item.is_published === false || item.status === 'draft'
        ).length
    })

    const archived = computed(() => {
        if (!items.value) return 0
        return items.value.filter(item =>
            item.is_archived === true || item.status === 'archived'
        ).length
    })

    const featured = computed(() => {
        if (!items.value) return 0
        return items.value.filter(item => item.is_featured === true).length
    })

    const urgent = computed(() => {
        if (!items.value) return 0
        return items.value.filter(item =>
            item.is_urgent === true || item.priority === 'urgent' || item.priority === 'high'
        ).length
    })

    // Custom stat calculator
    const custom = (filterFn) => {
        return computed(() => {
            if (!items.value) return 0
            return items.value.filter(filterFn).length
        })
    }

    return {
        total,
        active,
        inactive,
        published,
        draft,
        archived,
        featured,
        urgent,
        custom
    }
}
