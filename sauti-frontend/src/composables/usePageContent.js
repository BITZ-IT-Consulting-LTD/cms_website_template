import { ref } from 'vue'
import { api } from '@/utils/axios'

/**
 * Composable for fetching and managing page-specific content from CMS.
 * Provides dynamic images and fallback to local assets if CMS fails.
 * 
 * @param {string} pageName - The page identifier (e.g., 'home', 'about')
 */
export function usePageContent(pageName) {
    const images = ref({})
    const loading = ref(false)
    const error = ref(null)
    const loaded = ref(false)

    /**
     * Fetch page images from the CMS API
     */
    async function fetchPageImages() {
        if (loaded.value) return // Don't refetch if already loaded

        loading.value = true
        error.value = null

        try {
            const response = await api.get('/content/page-images/', {
                params: { page: pageName }
            })

            const data = response.data
            const imageMap = {}

            // Handle both array and paginated responses
            const items = Array.isArray(data) ? data : (data.results || [])

            items.forEach(item => {
                if (item.is_active !== false) {
                    imageMap[item.key] = {
                        url: item.image_url || item.image,
                        alt: item.alt_text || item.label,
                        fallback: item.fallback_path
                    }
                }
            })

            images.value = imageMap
            loaded.value = true
            console.log(`[PageContent] Loaded ${Object.keys(imageMap).length} images for "${pageName}"`)
        } catch (err) {
            console.warn(`[PageContent] Failed to load images for "${pageName}":`, err.message)
            error.value = err.message
            // Don't fail - components will use fallback images
        } finally {
            loading.value = false
        }
    }

    /**
     * Get image URL with fallback support.
     * @param {string} key - The image key (e.g., 'hero_main_image')
     * @param {string} fallbackPath - Local asset path to use as fallback
     * @returns {string} The image URL (CMS or fallback)
     */
    function getImage(key, fallbackPath = '') {
        const img = images.value[key]
        if (img && img.url) {
            return img.url
        }
        // Return CMS-stored fallback or provided fallback
        return img?.fallback || fallbackPath
    }

    /**
     * Get image alt text.
     * @param {string} key - The image key
     * @param {string} defaultAlt - Default alt text
     * @returns {string} Alt text for the image
     */
    function getAlt(key, defaultAlt = '') {
        const img = images.value[key]
        return img?.alt || defaultAlt
    }

    /**
     * Check if a specific image exists in CMS
     * @param {string} key - The image key
     * @returns {boolean}
     */
    function hasImage(key) {
        return !!images.value[key]?.url
    }

    return {
        images,
        loading,
        error,
        loaded,
        fetchPageImages,
        getImage,
        getAlt,
        hasImage
    }
}
