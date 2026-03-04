# Quick CMS Integration for All Pages

## Step 1: Run Populate Script

```powershell
docker exec sauti_backend_dev python /app/populate_comprehensive_content.py
```

## Step 2: Update Each Vue Component

### Blog Page (`BlogPage.vue`)
Add to `<script setup>`:
```javascript
import { useSiteContent } from '@/composables/useSiteContent'
const siteContent = useSiteContent('blog')
```

Update `onMounted`:
```javascript
onMounted(async () => {
  await siteContent.fetchContent()
  await settingsStore.fetchGlobalSettings()
  await Promise.all([fetchCategories(), fetchFilteredPosts()])
})
```

Update template line 7:
```vue
<h1 class="page-header-title">
  {{ siteContent.getContent('blog_page_title', 'Updates') }} <span class="text-primary">{{ siteContent.getContent('blog_page_title_highlight', 'and blogs') }}</span>
</h1>
```

Update line 19 (search placeholder):
```vue
:placeholder="siteContent.getContent('blog_search_placeholder', blogSearchPlaceholder)"
```

Update line 26 (categories dropdown):
```vue
<option value="">{{ siteContent.getContent('blog_categories_dropdown', blogCategoriesDropdown) }}</option>
```

Update line 41 (filter buttons):
```vue
{{ type === 'All' ? siteContent.getContent('blog_all_button', blogAllButton) : siteContent.getContent('blog_articles_button', blogArticlesButton) }}
```

Update line 47 (loading):
```vue
<AppLoader v-if="loading" :message="siteContent.getContent('blog_loading', blogLoading)" />
```

---

### News Page (`NewsPage.vue`)
Add to `<script setup>`:
```javascript
import { useSiteContent } from '@/composables/useSiteContent'
const siteContent = useSiteContent('news')

onMounted(async () => {
  await siteContent.fetchContent()
  // ... rest of code
})
```

Update template header:
```vue
<h1 class="page-header-title">
  {{ siteContent.getContent('news_page_title', 'Latest') }} <span class="text-primary">{{ siteContent.getContent('news_page_title_highlight', 'News & Updates') }}</span>
</h1>
```

---

### Resources Page (`ResourcesPage.vue`)
Add to `<script setup>`:
```javascript
import { useSiteContent } from '@/composables/useSiteContent'
const siteContent = useSiteContent('resources')

onMounted(async () => {
  await siteContent.fetchContent()
  // ... rest
})
```

Update template:
```vue
<h1 class="page-header-title">
  {{ siteContent.getContent('resources_page_title', 'Resources') }} <span class="text-primary">{{ siteContent.getContent('resources_page_title_highlight', '& Downloads') }}</span>
</h1>
```

Update search placeholder:
```vue
:placeholder="siteContent.getContent('resources_search_placeholder', 'Search resources...')"
```

Update filter dropdown:
```vue
<option value="">{{ siteContent.getContent('resources_filter_all_categories', 'All Categories') }}</option>
```

---

### FAQs Page (`FaqsPage.vue`)
Add to `<script setup>`:
```javascript
import { useSiteContent } from '@/composables/useSiteContent'
const siteContent = useSiteContent('faqs')

onMounted(async () => {
  await siteContent.fetchContent()
  // ... rest
})
```

Update template:
```vue
<h1 class="page-header-title">
  {{ siteContent.getContent('faqs_page_title', 'Frequently Asked') }} <span class="text-primary">{{ siteContent.getContent('faqs_page_title_highlight', 'Questions') }}</span>
</h1>
```

Update search:
```vue
:placeholder="siteContent.getContent('faqs_search_placeholder', 'Search questions...')"
```

---

### Contact Page (`ContactPage.vue`)
Add to `<script setup>`:
```javascript
import { useSiteContent } from '@/composables/useSiteContent'
const siteContent = useSiteContent('contact')

onMounted(async () => {
  await siteContent.fetchContent()
  // ... rest
})
```

Update template:
```vue
<h1 class="page-header-title">
  {{ siteContent.getContent('contact_page_title', 'Get in') }} <span class="text-primary">{{ siteContent.getContent('contact_page_title_highlight', 'Touch') }}</span>
</h1>
<p class="page-header-subtitle">
  {{ siteContent.getContent('contact_page_description', 'We\'re here 24/7 to listen, support, and help. Reach out anytime.') }}
</p>
```

---

## ✅ ALL DONE!

After these updates:
1. ✅ Videos Page - CMS controlled
2. ✅ Blog Page - CMS controlled
3. ✅ News Page - CMS controlled
4. ✅ Resources Page - CMS controlled
5. ✅ FAQs Page - CMS controlled
6. ✅ Contact Page - CMS controlled
7. ✅ Home Page - Already done
8. ✅ About Page - Already done
9. ✅ Footer - Already done

**All content is now editable in the CMS Dashboard!**
