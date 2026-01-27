import { ref, computed } from 'vue'
import { api } from '@/utils/axios'

/**
 * Composable for fetching and managing site content from CMS.
 * Provides dynamic content (text, headings, buttons) with fallback to defaults.
 * 
 * @param {string} pageName - The page identifier (e.g., 'home', 'about')
 */
export function useSiteContent(pageName = 'home') {
    const content = ref({})
    const loading = ref(false)
    const error = ref(null)
    const loaded = ref(false)

    /**
     * Fetch site content from the CMS API
     * @param {boolean} forceRefresh - Force refresh even if already loaded
     */
    async function fetchContent(forceRefresh = false) {
        if (loaded.value && !forceRefresh) return // Don't refetch if already loaded unless forced

        loading.value = true
        error.value = null

        try {
            const response = await api.get('/content/site-content/', {
                params: { page: pageName }
            })

            const data = response.data
            const contentMap = {}

            // Handle both array and paginated responses
            const items = Array.isArray(data) ? data : (data.results || data)

            if (Array.isArray(items)) {
                items.forEach(item => {
                    if (item.is_published !== false) {
                        contentMap[item.key] = {
                            value: item.value,
                            type: item.type,
                            label: item.label,
                            page: item.page
                        }
                    }
                })
            } else if (typeof items === 'object') {
                // Handle object format (key-value pairs)
                Object.keys(items).forEach(key => {
                    const item = items[key]
                    if (typeof item === 'object') {
                        contentMap[key] = {
                            value: item.value,
                            type: item.type || 'text',
                            label: item.label || key,
                            page: item.page || pageName
                        }
                    } else {
                        // Simple string value
                        contentMap[key] = {
                            value: item,
                            type: 'text',
                            label: key,
                            page: pageName
                        }
                    }
                })
            }

            content.value = contentMap
            loaded.value = true
            console.log(`[SiteContent] Loaded ${Object.keys(contentMap).length} content items for "${pageName}"`)
        } catch (err) {
            console.warn(`[SiteContent] Failed to load content for "${pageName}":`, err.message)
            error.value = err.message
            // Don't fail - components will use fallback content
        } finally {
            loading.value = false
        }
    }

    /**
     * Get content value by key with fallback support.
     * @param {string} key - The content key (e.g., 'home_hero_headline')
     * @param {string} defaultValue - Default value to use if key not found
     * @returns {string} The content value (CMS or default)
     */
    function getContent(key, defaultValue = '') {
        const item = content.value[key]
        if (item && item.value !== undefined && item.value !== null) {
            return item.value
        }
        return defaultValue
    }

    /**
     * Get content and replace placeholders with dynamic values.
     * Example: getContent('home_hero_cta_text', 'Call {hotline}', { hotline: '116' })
     * @param {string} key - The content key
     * @param {string} defaultValue - Default value to use if key not found
     * @param {Object} replacements - Key-value pairs for replacements
     * @returns {string} The content value with replacements applied
     */
    function getContentWithReplacements(key, defaultValue = '', replacements = {}) {
        let value = getContent(key, defaultValue)
        
        Object.keys(replacements).forEach(placeholder => {
            const regex = new RegExp(`\\{${placeholder}\\}`, 'g')
            value = value.replace(regex, replacements[placeholder])
        })
        
        return value
    }

    /**
     * Check if a specific content key exists in CMS
     * @param {string} key - The content key
     * @returns {boolean}
     */
    function hasContent(key) {
        const item = content.value[key]
        return !!(item && item.value)
    }

    /**
     * Get content type (text, heading, button, etc.)
     * @param {string} key - The content key
     * @returns {string} The content type
     */
    function getContentType(key) {
        const item = content.value[key]
        return item?.type || 'text'
    }

    /**
     * Get all content for the current page as an object
     * Useful for bulk operations or debugging
     * @returns {Object} All content items
     */
    const allContent = computed(() => content.value)

    /**
     * Check if any content is available
     * @returns {boolean}
     */
    const hasAnyContent = computed(() => Object.keys(content.value).length > 0)

    return {
        content,
        loading,
        error,
        loaded,
        fetchContent,
        getContent,
        getContentWithReplacements,
        hasContent,
        getContentType,
        allContent,
        hasAnyContent
    }
}
