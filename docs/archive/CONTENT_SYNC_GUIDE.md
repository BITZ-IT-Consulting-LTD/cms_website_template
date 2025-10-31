# Content Sync & Upload Integration Guide

## Overview
This guide ensures content created in the admin dashboard appears correctly on the frontend, and that file uploads (images, documents) work seamlessly.

---

## 🔄 Content Flow

```
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│  Sauti Admin    │      │  Django Backend │      │ Sauti Frontend  │
│  (Port 3002)    │─────▶│  (Port 8000)    │─────▶│  (Port 3000)    │
│                 │      │                 │      │                 │
│ Create/Edit     │      │ Store in DB     │      │ Display to      │
│ Content + Upload│      │ + Save Files    │      │ Public Users    │
└─────────────────┘      └─────────────────┘      └─────────────────┘
```

---

## ✅ Completed Integration

### 1. **Pinia Stores Created** (Admin Side)

#### `/sauti-admin/src/stores/resources.js`
- Manages educational resources (PDFs, docs, images)
- **File Upload:** FormData with multipart/form-data
- **Actions:** fetchResources, createResource, updateResource, deleteResource
- **Categories:** Fetch resource categories from backend

#### `/sauti-admin/src/stores/faqs.js`
- Manages FAQ questions and answers
- **Actions:** fetchFaqs, createFaq, updateFaq, deleteFaq, togglePublished
- **Categories:** Fetch FAQ categories from backend

#### `/sauti-admin/src/stores/partners.js`
- Manages partner organizations
- **File Upload:** Logo images with FormData
- **Actions:** fetchPartners, createPartner, updatePartner, deletePartner, toggleActive

#### Existing Stores
- `/sauti-admin/src/stores/posts.js` - Already handles featured images
- `/sauti-admin/src/stores/auth.js` - Authentication with JWT

---

### 2. **API Endpoints Updated**

#### `/sauti-admin/src/utils/api.js`
Enhanced with CRUD operations for all content types:

```javascript
// Resources with file upload
resources: {
  create: (data) => FormData + multipart/form-data
  update: (slug, data) => FormData + multipart/form-data
  delete: (slug)
}

// FAQs
faqs: {
  create, update, delete + categories
}

// Partners with logo upload
partners: {
  create: (data) => FormData + multipart/form-data
  update: (slug, data) => FormData + multipart/form-data
  delete: (slug)
}
```

---

### 3. **Frontend Stores Already Setup**

The Sauti Frontend already has working stores:

- `/sauti-frontend/src/store/blog.js` - Fetches posts
- `/sauti-frontend/src/store/resources.js` - Fetches resources
- `/sauti-frontend/src/store/faqs.js` - Fetches FAQs
- `/sauti-frontend/src/store/partners.js` - Fetches partners

These automatically pull content from the same Django backend!

---

## 📁 File Upload Configuration

### Django Backend (Already Configured ✅)

**Settings** (`sauti_cms/cms/settings.py`):
```python
# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

**URLs** (`sauti_cms/cms/urls.py`):
```python
# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**Models Support Uploads:**
- `Post.featured_image` → uploads to `posts/images/%Y/%m/`
- `Resource.file` → uploads to `resources/files/%Y/%m/`
- `Partner.logo` → uploads to `partners/logos/`

---

## 🔧 How to Use File Uploads

### Example: Creating a Resource with File

**Admin Side** (`sauti-admin`):
```javascript
import { useResourcesStore } from '@/stores/resources'

const resourcesStore = useResourcesStore()

async function createResourceWithFile() {
  const fileInput = document.querySelector('input[type="file"]')
  const file = fileInput.files[0]
  
  const resourceData = {
    title: 'Child Safeguarding Guide',
    description: 'Complete guide for child protection',
    category: 'guides',
    file: file,  // The actual file
    language: 'en',
    is_published: true
  }
  
  try {
    const newResource = await resourcesStore.createResource(resourceData)
    console.log('Resource created:', newResource)
    // File URL will be: newResource.file (e.g., /media/resources/files/2024/10/guide.pdf)
  } catch (error) {
    console.error('Failed:', error)
  }
}
```

### Example: Creating a Partner with Logo

```javascript
import { usePartnersStore } from '@/stores/partners'

const partnersStore = usePartnersStore()

async function createPartnerWithLogo() {
  const logoInput = document.querySelector('input[type="file"]')
  const logo = logoInput.files[0]
  
  const partnerData = {
    name: 'UNICEF Uganda',
    description: 'UN Children\'s Fund',
    partner_type: 'UN_AGENCY',
    logo: logo,  // The actual logo file
    website_url: 'https://www.unicef.org/uganda',
    email: 'kampala@unicef.org',
    is_active: true
  }
  
  try {
    const newPartner = await partnersStore.createPartner(partnerData)
    console.log('Partner created:', newPartner)
    // Logo URL will be: newPartner.logo (e.g., /media/partners/logos/unicef.png)
  } catch (error) {
    console.error('Failed:', error)
  }
}
```

---

## 🖼️ Displaying Uploaded Files

### Frontend Side (`sauti-frontend`)

**Images** (Posts, Partners):
```vue
<template>
  <div v-for="post in posts" :key="post.id">
    <img 
      :src="`http://localhost:8000${post.featured_image}`" 
      :alt="post.title"
      class="w-full h-64 object-cover"
    />
  </div>
</template>

<script setup>
import { useBlogStore } from '@/store/blog'
const blogStore = useBlogStore()

onMounted(async () => {
  await blogStore.fetchPosts()
})
</script>
```

**Downloadable Files** (Resources):
```vue
<template>
  <div v-for="resource in resources" :key="resource.id">
    <a 
      :href="`http://localhost:8000${resource.file}`"
      :download="resource.title"
      class="btn btn-download"
    >
      📥 Download {{ resource.title }}
    </a>
  </div>
</template>
```

---

## 🔄 Content Synchronization

### How It Works

1. **Create in Admin** (Port 3002)
   - User fills out form
   - Uploads image/file
   - Clicks "Save"
   - Pinia store sends to Django API

2. **Store in Backend** (Port 8000)
   - Django receives POST/PUT request
   - Validates data
   - Saves file to `MEDIA_ROOT`
   - Stores database record
   - Returns data with file URL

3. **Display on Frontend** (Port 3000)
   - Frontend fetches data on page load
   - Gets file URL from API
   - Displays image or download link
   - Users can view/download

### Real-Time Updates

**Admin Changes Are Immediate:**
- Create a post in admin → Refresh frontend → Post appears
- Upload a resource → Frontend can download it
- Add a partner logo → Logo displays on frontend

No caching issues because:
- Frontend fetches fresh data on each page load
- Django serves files directly from filesystem
- Images/files have unique URLs

---

## 🧪 Testing Content Sync

### Test Workflow

#### 1. Test Posts (Already Working)
```bash
# Admin (3002): Create a blog post with featured image
# Frontend (3000): Visit /blog → See new post with image
```

#### 2. Test Resources
```bash
# Admin (3002): Upload a PDF resource
# Frontend (3000): Visit /resources → See + download PDF
```

#### 3. Test Partners
```bash
# Admin (3002): Add partner with logo
# Frontend (3000): Visit /partners → See partner logo
```

#### 4. Test FAQs
```bash
# Admin (3002): Create FAQ
# Frontend (3000): Visit /faqs → See new FAQ
```

---

## 📝 Next Steps to Complete Integration

### Phase 1: Connect Admin Views to Stores

Update these admin views to use real stores instead of mock data:

#### 1. **PostsView.vue** (Already uses store ✅)
```javascript
import { usePostsStore } from '@/stores/posts'
const postsStore = usePostsStore()
onMounted(() => postsStore.fetchPosts())
```

#### 2. **ResourcesView.vue** (Update needed)
```javascript
// Replace mock data with:
import { useResourcesStore } from '@/stores/resources'
const resourcesStore = useResourcesStore()

onMounted(async () => {
  await resourcesStore.fetchResources()
  await resourcesStore.fetchCategories()
})

const filteredResources = computed(() => resourcesStore.resources)
```

#### 3. **FaqsView.vue** (Update needed)
```javascript
// Replace mock data with:
import { useFaqsStore } from '@/stores/faqs'
const faqsStore = useFaqsStore()

onMounted(async () => {
  await faqsStore.fetchFaqs()
  await faqsStore.fetchCategories()
})

const filteredFaqs = computed(() => faqsStore.faqs)
```

#### 4. **PartnersView.vue** (Update needed)
```javascript
// Replace mock data with:
import { usePartnersStore } from '@/stores/partners'
const partnersStore = usePartnersStore()

onMounted(async () => {
  await partnersStore.fetchPartners()
})

const filteredPartners = computed(() => partnersStore.partners)
```

---

### Phase 2: Create Form Components

Build modal/page forms for creating/editing:

1. **ResourceForm.vue**
   - Title, description, category
   - File upload input (`<input type="file">`)
   - Language selector
   - Published toggle

2. **FaqForm.vue**
   - Question, answer
   - Category selector
   - Order field
   - Published toggle

3. **PartnerForm.vue**
   - Name, description, type
   - Logo upload (`<input type="file" accept="image/*">`)
   - Contact info (website, email, phone)
   - Active/Featured toggles

---

## 🔒 File Upload Security

### Already Configured in Django

1. **File Size Limits** (Django default: 2.5MB)
   - Can increase in settings with `DATA_UPLOAD_MAX_MEMORY_SIZE`

2. **File Type Validation**
   - Models specify upload paths
   - Can add validators to model fields

3. **Authentication Required**
   - All upload endpoints require JWT token
   - Only authenticated admin users can upload

4. **Virus Scanning** (Recommended for production)
   - Add `django-clamav` or similar

---

## 📊 File Storage Structure

```
sauti_cms/
├── media/
│   ├── posts/
│   │   └── images/
│   │       └── 2024/
│   │           └── 10/
│   │               ├── article-1.jpg
│   │               └── article-2.png
│   ├── resources/
│   │   └── files/
│   │       └── 2024/
│   │           └── 10/
│   │               ├── guide.pdf
│   │               └── poster.png
│   └── partners/
│       └── logos/
│           ├── unicef.png
│           ├── save-children.jpg
│           └── mglsd.png
```

---

## 🚀 Quick Start Commands

### 1. Start All Services
```bash
cd /Users/newtonbrian/Documents/Bitz/cms_website_template
./start-all.sh
```

### 2. Test Content Creation
```bash
# Login to admin
open http://localhost:3002

# Login credentials
Username: admin
Password: admin123

# Create content and upload files
# Then check frontend
open http://localhost:3000
```

### 3. Verify Media Files
```bash
# Check uploaded files
ls -la sauti_cms/media/posts/images/
ls -la sauti_cms/media/resources/files/
ls -la sauti_cms/media/partners/logos/

# Access via browser
open http://localhost:8000/media/posts/images/2024/10/filename.jpg
```

---

## ✅ Content Matching Checklist

- [x] **Posts:** Admin creates → Frontend displays ✅
- [x] **Featured Images:** Upload in admin → Show on frontend ✅
- [ ] **Resources:** Admin uploads → Frontend can download (needs view update)
- [ ] **Resource Files:** PDF/DOC uploads work (needs form)
- [ ] **FAQs:** Admin creates → Frontend displays (needs view update)
- [ ] **Partners:** Admin adds → Frontend shows (needs view update)
- [ ] **Partner Logos:** Upload logos → Display on frontend (needs form)

---

## 🎯 Summary

### What's Working Now ✅
1. Django backend configured for uploads
2. Admin stores created with FormData support
3. Frontend stores ready to fetch content
4. Posts with images fully working
5. JWT authentication working
6. CORS configured properly

### What Needs Completion 🔧
1. Update admin views to use real stores (remove mock data)
2. Create form components for file uploads
3. Test end-to-end content creation
4. Verify files display correctly on frontend

### Expected Behavior 🎉
Once complete:
- Create post in admin → Appears on frontend blog
- Upload resource in admin → Downloadable on frontend
- Add partner with logo → Logo shows on frontend partners page
- Create FAQ in admin → Visible in frontend FAQ section

**All content will sync automatically via shared Django API!**

---

*Last Updated: October 2025*
