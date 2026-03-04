import { ref, computed } from 'vue'

/**
 * Composable for managing filters and filtered data
 * @param {Array} items - The items to filter
 * @param {Object} initialFilters - Initial filter values
 * @returns {Object} Filter state and filtered items
 */
export function useFilters(items, initialFilters = {}) {
    const filters = ref({
        search: '',
        status: '',
        custom: '',
        ...initialFilters
    })

    const filteredItems = computed(() => {
        if (!items.value || !Array.isArray(items.value)) {
            return []
        }

        return items.value.filter(item => {
            // Search filter
            if (filters.value.search) {
                const searchLower = filters.value.search.toLowerCase()
                const searchableFields = [
                    item.name,
                    item.title,
                    item.description,
                    item.email,
                    item.label
                ].filter(Boolean)

                const matchesSearch = searchableFields.some(field =>
                    String(field).toLowerCase().includes(searchLower)
                )

                if (!matchesSearch) return false
            }

            // Status filter
            if (filters.value.status) {
                const status = filters.value.status

                // Handle different status field names
                if (item.status && item.status !== status) return false
                if (item.is_active !== undefined) {
                    if (status === 'active' && !item.is_active) return false
                    if (status === 'inactive' && item.is_active) return false
                }
                if (item.is_published !== undefined) {
                    if (status === 'published' && !item.is_published) return false
                    if (status === 'draft' && item.is_published) return false
                }
            }

            // Custom filter (can be category, type, etc.)
            if (filters.value.custom && item.category) {
                if (item.category !== filters.value.custom) return false
            }
            if (filters.value.custom && item.type) {
                if (item.type !== filters.value.custom) return false
            }

            return true
        })
    })

    const clearFilters = () => {
        filters.value = {
            search: '',
            status: '',
            custom: ''
        }
    }

    const hasActiveFilters = computed(() => {
        return Object.values(filters.value).some(value => value !== '' && value !== null)
    })

    return {
        filters,
        filteredItems,
        clearFilters,
        hasActiveFilters
    }
}
