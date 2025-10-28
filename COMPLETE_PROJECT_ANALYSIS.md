# Complete Project Analysis: Sauti Child Helpline CMS

## 🏗️ Project Structure

This is a **full-stack web application** consisting of three main components:

```
sauti_cms/          → Backend (Django REST Framework API)
sauti-admin/        → Admin Dashboard (Vue 3 - Content Management)
sauti-frontend/     → Public Website (Vue 3 - User-Facing)
```

---

## 📊 Component Architecture

### **1. Backend - Django CMS (sauti_cms/)**

#### **Technology Stack:**
- **Framework**: Django 5.0.6
- **API**: Django REST Framework 3.15.1
- **Database**: SQLite (dev) / PostgreSQL (production)
- **Authentication**: JWT (rest_framework_simplejwt)
- **Documentation**: drf-spectacular (OpenAPI/Swagger)
- **CORS**: django-cors-headers

#### **Django Apps:**
1. **users** - Custom user model with role-based access control
2. **posts** - Blog posts/news management
3. **videos** - Video content management
4. **resources** - Downloadable resources
5. **faqs** - FAQ management
6. **partners** - Partner organization management
7. **reports** - Anonymous case reporting with encryption
8. **dashboard** - Analytics and statistics

#### **URL Routing Structure:**
```python
URL: http://localhost:8000

/api/auth/          → Authentication endpoints
  - login/           → POST: Login with username/password
  - token/refresh/   → POST: Refresh JWT token
  - profile/         → GET: Get user profile
  
/api/posts/         → Blog posts endpoints
  - /               → GET: List posts, POST: Create post
  - categories/     → GET: List categories
  - tags/           → GET: List tags
  - <slug>/         → GET/PUT/DELETE: Post detail operations
  
/api/videos/        → Video endpoints
  - /               → GET: List videos, POST: Create video
  - categories/     → GET: List video categories
  - <slug>/         → GET/PUT/DELETE: Video detail operations
  
/api/resources/     → Resource endpoints
  - /               → GET: List resources, POST: Create resource
  - categories/     → GET: List resource categories
  - <slug>/         → GET/PUT/DELETE: Resource detail operations
  
/api/faqs/          → FAQ endpoints
  - /               → GET: List FAQs, POST: Create FAQ
  - categories/     → GET: List FAQ categories
  - <id>/           → GET/PUT/DELETE: FAQ detail operations
  
/api/partners/      → Partner endpoints
  - /               → GET: List partners, POST: Create partner
  - <slug>/         → GET/PUT/DELETE: Partner detail operations
  
/api/reports/       → Report endpoints
  - /               → POST: Create report (anonymous)
  
/api/dashboard/     → Dashboard endpoints
  - stats/          → GET: Dashboard statistics
  - top-content/    → GET: Top performing content
  
/api/docs/          → Swagger UI documentation
/api/redoc/         → ReDoc documentation
```

#### **Permission System:**
```python
Role Hierarchy:
1. ADMIN    → Full access to everything
2. EDITOR   → Can create/edit content, cannot delete
3. AUTHOR   → Can create content (drafts only)
4. VIEWER   → Read-only access

Permission Classes:
- IsEditorOrReadOnly  → Editors/Admins can write, others read-only
- IsAdminOrReadOnly   → Only Admins can delete
- IsAuthenticated     → Requires authentication
- AllowAny            → Public access
```

---

### **2. Admin Dashboard - Vue 3 (sauti-admin/)**

#### **Technology Stack:**
- **Framework**: Vue 3.4.21 (Composition API)
- **Build Tool**: Vite 5.2.0
- **State Management**: Pinia 2.1.7
- **Routing**: Vue Router 4.3.0
- **Styling**: TailwindCSS 3.4.3
- **HTTP Client**: Axios 1.6.8
- **Icons**: Heroicons 2.1.3
- **Notifications**: vue-toastification

#### **Project Structure:**
```
sauti-admin/
├── src/
│   ├── App.vue                    → Root component
│   ├── main.js                    → Application entry point
│   ├── router/
│   │   └── index.js               → Route definitions
│   ├── stores/                    → Pinia state management
│   │   ├── auth.js               → Authentication store
│   │   ├── posts.js              → Blog posts store
│   │   ├── videos.js             → Videos store
│   │   ├── resources.js           → Resources store
│   │   ├── faqs.js               → FAQs store
│   │   ├── partners.js            → Partners store
│   │   └── dashboard.js          → Dashboard statistics
│   ├── utils/
│   │   └── api.js                → Axios configuration & API methods
│   ├── components/
│   │   └── DashboardLayout.vue   → Main layout wrapper
│   └── views/                     → Page components
│       ├── LoginView.vue         → Admin login
│       ├── DashboardView.vue    → Main dashboard
│       ├── PostsView.vue         → Post list
│       ├── PostEditView.vue      → Create/Edit posts
│       ├── VideosView.vue        → Video list
│       ├── VideoEditView.vue     → Create/Edit videos
│       ├── ResourcesView.vue     → Resource management
│       ├── FaqsView.vue          → FAQ management
│       ├── PartnersView.vue      → Partner management
│       ├── ReportsView.vue       → Report management
│       └── SettingsView.vue     → Settings
```

#### **Key Files:**
- **`src/utils/api.js`** - Axios instance with:
  - JWT token injection via interceptors
  - Request/response logging
  - Automatic error handling
  - 401 redirects to login
  - All API endpoint definitions

- **`src/stores/*.js`** - Pinia stores for:
  - State management (refs, computed)
  - API integration
  - CRUD operations
  - Loading/error states

#### **Port Configuration:**
- **URL**: http://localhost:3001
- **Proxy**: Proxies `/api/*` → `http://localhost:8000/api/*`

---

### **3. Public Frontend - Vue 3 (sauti-frontend/)**

#### **Technology Stack:**
- **Framework**: Vue 3.4.21 (Composition API)
- **Build Tool**: Vite 5.2.0
- **State Management**: Pinia 2.1.7
- **Routing**: Vue Router 4.3.0
- **Styling**: TailwindCSS 3.4.3
- **HTTP Client**: Axios 1.6.8
- **Components**: vue3-carousel

#### **Project Structure:**
```
sauti-frontend/
├── src/
│   ├── App.vue                    → Root component
│   ├── main.js                    → Application entry point
│   ├── router/
│   │   └── index.js               → Route definitions
│   ├── store/                     → Pinia stores
│   │   ├── auth.js               → Authentication
│   │   ├── blog.js               → Blog posts
│   │   ├── faqs.js               → FAQs
│   │   ├── partners.js           → Partners
│   │   └── resources.js           → Resources
│   ├── stores/
│   │   └── videos.js             → Videos
│   ├── utils/
│   │   └── axios.js              → Axios configuration
│   ├── components/               → Reusable components
│   │   ├── layout/              → Header, Footer
│   │   ├── blog/                → Blog-specific components
│   │   ├── common/              → Common UI elements
│   │   ├── faqs/                → FAQ components
│   │   ├── partners/            → Partner components
│   │   ├── resources/           → Resource components
│   │   └── reports/             → Report form
│   └── views/                     → Page components
│       ├── Home.vue             → Homepage
│       ├── Blog.vue              → Blog listing
│       ├── BlogDetail.vue       → Blog post detail
│       ├── Videos.vue           → Video listings
│       ├── Resources.vue         → Resource library
│       ├── Faqs.vue             → FAQ page
│       ├── Partners.vue         → Partners page
│       ├── Report.vue           → Report a case
│       ├── About.vue            → About page
│       ├── Operations.vue       → Operations page
│       ├── Contact.vue          → Contact page
│       ├── Privacy.vue         → Privacy policy
│       ├── Terms.vue            → Terms of service
│       └── Accessibility.vue   → Accessibility statement
```

#### **Port Configuration:**
- **URL**: http://localhost:3000
- **Proxy**: Proxies `/api/*` → `http://localhost:8000/api/*`

---

## 🔄 Data Flow Architecture

### **Authentication Flow:**

```
1. User Login (Admin):
   POST /api/auth/login/
   → Username: "admin"
   → Password: "admin123"
   
2. Backend Response:
   {
     "access": "eyJhbGci...",  // JWT access token
     "refresh": "eyJhbGci...", // Refresh token
     "user": {...}            // User object
   }

3. Frontend Stores Token:
   localStorage.setItem('admin_token', access)
   localStorage.setItem('admin_user', JSON.stringify(user))

4. Subsequent Requests:
   Authorization: Bearer eyJhbGci...

5. Token Refresh (if expired):
   POST /api/auth/token/refresh/
   → Returns new access token
```

### **Content Management Flow (Admin → Backend → Frontend):**

```
ADMIN CREATES POST
==================

1. Admin fills form in PostEditView.vue
   - Title, content, categories, tags, featured image

2. Form submission triggers:
   postsStore.createPost(postData)

3. Store calls API:
   api.posts.create(postData)
   → Method: POST
   → URL: /api/posts/
   → Body: FormData with file upload

4. Vite Proxy forwards:
   /api/posts/ → http://localhost:8000/api/posts/

5. Django REST Framework:
   - Validates data with PostCreateUpdateSerializer
   - Checks permissions (IsEditorOrReadOnly)
   - Creates Post object in database
   - Returns serialized Post object

6. Response sent back:
   {
     "id": 1,
     "title": "Example Post",
     "slug": "example-post",
     ...
   }

7. Store updates local state:
   posts.value.unshift(newPost)

8. Redirect to PostsView.vue


FRONTEND DISPLAYS POST
=======================

1. Public user visits Blog page
   → Blog.vue component mounts

2. Component calls:
   blogStore.fetchPosts({ status: 'PUBLISHED' })

3. Store calls API:
   api.posts.list({ status: 'PUBLISHED' })
   → Method: GET
   → URL: /api/posts/?status=PUBLISHED

4. Vite Proxy forwards:
   /api/posts/?status=PUBLISHED → http://localhost:8000/api/posts/?status=PUBLISHED

5. Django REST Framework:
   - Filters posts by status=PUBLISHED
   - Uses PostListSerializer
   - Returns paginated results

6. Store updates state:
   posts.value = response.data.results

7. Component displays:
   <BlogCard> for each post in posts array


SAME FLOW FOR:
- Videos
- Resources
- FAQs
- Partners
```

---

## 🔌 API Integration Details

### **Admin Dashboard API Integration:**

#### **`sauti-admin/src/utils/api.js`**

```javascript
// Axios Configuration
const apiClient = axios.create({
  baseURL: '/api',           // Relative path (proxied)
  timeout: 15000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request Interceptor: Inject JWT Token
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('admin_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Response Interceptor: Handle Errors
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Redirect to login
      localStorage.removeItem('admin_token')
      router.push('/login')
    }
    return Promise.reject(error)
  }
)

// API Methods
export const api = {
  auth: {
    login: (credentials) => apiClient.post('/auth/login/', credentials),
    profile: () => apiClient.get('/auth/profile/'),
  },
  
  posts: {
    list: (params) => apiClient.get('/posts/', { params }),
    get: (slug) => apiClient.get(`/posts/${slug}/`),
    create: (data) => {
      const formData = new FormData()
      // Convert data to FormData for file uploads
      return apiClient.post('/posts/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
    },
    update: (slug, data) => apiClient.put(`/posts/${slug}/`, formData),
    delete: (slug) => apiClient.delete(`/posts/${slug}/`),
    categories: () => apiClient.get('/posts/categories/'),
    tags: () => apiClient.get('/posts/tags/'),
  },
  
  videos: { /* Similar structure */ },
  resources: { /* Similar structure */ },
  faqs: { /* Similar structure */ },
  partners: { /* Similar structure */ },
  dashboard: { /* Dashboard endpoints */ }
}
```

### **Pinia Store Pattern:**

#### **`sauti-admin/src/stores/posts.js`**

```javascript
export const usePostsStore = defineStore('posts', () => {
  // State
  const posts = ref([])
  const currentPost = ref(null)
  const categories = ref([])
  const tags = ref([])
  const loading = ref(false)
  const error = ref(null)
  
  // Actions (API calls)
  async function fetchPosts(params = {}) {
    loading.value = true
    try {
      const response = await api.posts.list(params)
      posts.value = response.data.results || response.data
      return posts.value
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function createPost(postData) {
    loading.value = true
    try {
      const response = await api.posts.create(postData)
      posts.value.unshift(response.data)
      return response.data
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function updatePost(slug, postData) {
    loading.value = true
    try {
      const response = await api.posts.update(slug, postData)
      const index = posts.value.findIndex(p => p.slug === slug)
      if (index !== -1) {
        posts.value[index] = response.data
      }
      return response.data
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      loading.value = false
    }
  }
  
  async function deletePost(slug) {
    loading.value = true
    try {
      await api.posts.delete(slug)
      posts.value = posts.value.filter(p => p.slug !== slug)
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      loading.value = false
    }
  }
  
  return {
    // State
    posts, currentPost, categories, tags, loading, error,
    // Actions
    fetchPosts, createPost, updatePost, deletePost
  }
})
```

---

## 🎯 Complete Interaction Examples

### **Example 1: Creating a Blog Post (Admin)**

```javascript
// 1. User fills form in PostEditView.vue
const form = ref({
  title: 'New Post',
  content: 'Content here...',
  categories: [1, 2],
  tags: [3, 5],
  featuredImage: fileObject,
  status: 'published'
})

// 2. User clicks "Publish"
savePost('published')

// 3. Store method called
async function createPost(postData) {
  const response = await api.posts.create(postData)
  // Converts to FormData automatically
  // Appends JWT token
  // Sends multipart/form-data
}

// 4. Request sent to Django
POST http://localhost:8000/api/posts/
Authorization: Bearer eyJhbGci...
Content-Type: multipart/form-data

FormData:
  title: "New Post"
  content: "Content here..."
  categories: [1, 2]
  tags: [3, 5]
  featuredImage: <File>
  status: "published"

// 5. Django validates & creates
serializer.save(author=request.user)

// 6. Response returned
{
  "id": 10,
  "title": "New Post",
  "slug": "new-post",
  "author_name": "admin",
  ...
}

// 7. Store updates state
posts.value.unshift(response.data)

// 8. Success toast shown
toast.success('Post created successfully')
```

### **Example 2: Displaying Blog Posts (Frontend)**

```javascript
// 1. User visits /blog
// 2. Blog.vue component mounts

// 3. Component calls store
onMounted(async () => {
  await blogStore.fetchPosts({ status: 'PUBLISHED', limit: 10 })
})

// 4. Store makes API call
async function fetchPosts(params) {
  const response = await api.posts.list(params)
  posts.value = response.data.results
}

// 5. Request sent to Django
GET http://localhost:8000/api/posts/?status=PUBLISHED&limit=10

// 6. Django filters and returns
queryset.filter(status='PUBLISHED')[:10]

// 7. Response
{
  "count": 25,
  "results": [
    {
      "id": 10,
      "title": "New Post",
      "slug": "new-post",
      "author_name": "admin",
      "category_name": "News",
      "featured_image": "http://localhost:8000/media/posts/image.jpg",
      "published_at": "2024-01-15T10:00:00Z",
      ...
    },
    ...
  ]
}

// 8. Store updates
posts.value = response.data.results

// 9. Component displays
<div v-for="post in posts" :key="post.id">
  <BlogCard :post="post" />
</div>
```

---

## 🔒 Security Architecture

### **JWT Token Flow:**

```
1. Login → POST /api/auth/login/
   ↓
2. Receive tokens (access + refresh)
   ↓
3. Store in localStorage
   ↓
4. Include in all subsequent requests
   ↓
5. Token expires → Get 401
   ↓
6. Automatically refresh using refresh_token
   ↓
7. Retry original request with new access_token
```

### **CORS Configuration:**

```python
# Django settings.py
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # Frontend
    'http://localhost:3001',  # Admin
    'http://localhost:3002',
    'http://localhost:3003',
    'http://localhost:3004',
    'http://localhost:3005',
]
CORS_ALLOW_CREDENTIALS = True
```

### **Permission Classes:**

```python
# posts/views.py
class IsEditorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True  # Everyone can read
        return request.user.is_authenticated and request.user.is_editor
```

---

## 📦 File Upload Flow

```
1. User selects image in PostEditView
   handleImageUpload(event)
   ↓
2. File validated (type, size)
   ↓
3. File stored in form.value.featuredImage
   ↓
4. Form submitted with FormData
   const formData = new FormData()
   formData.append('featuredImage', file)
   ↓
5. Sent to Django with multipart/form-data
   ↓
6. Django saves to MEDIA_ROOT/posts/images/
   ↓
7. URL returned in response
   "featured_image": "/media/posts/images/abc123.jpg"
   ↓
8. Frontend displays image using full URL
   http://localhost:8000/media/posts/images/abc123.jpg
```

---

## 🚀 Development Setup

### **Start Backend:**
```bash
cd sauti_cms
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

### **Start Admin:**
```bash
cd sauti-admin
npm run dev
# Runs on http://localhost:3001
```

### **Start Frontend:**
```bash
cd sauti-frontend
npm run dev
# Runs on http://localhost:3000
```

---

## 📊 Data Synchronization

### **Admin Creates → Backend Stores → Frontend Displays**

```
ADMIN DASHBOARD              BACKEND API              PUBLIC FRONTEND
==================           ============             ===============
1. Create post               3. Validate & save        5. Fetch posts
   ↓                             ↓                        ↓
2. POST /api/posts/    →     4. Return data       →    6. Display posts
                                (JSON)                    (UI)
```

### **Real-time Updates:**
- Changes in admin immediately visible in frontend
- No need to refresh manually
- Pinia store auto-updates on create/edit/delete

---

## 🎯 Summary

### **Three-Layer Architecture:**

1. **Backend (Django)** → Provides REST API with:
   - Database operations
   - Authentication & authorization
   - File storage
   - Business logic

2. **Admin (Vue 3)** → Content management with:
   - CRUD operations
   - File uploads
   - Rich text editing
   - User authentication

3. **Frontend (Vue 3)** → Public-facing with:
   - Content display
   - User engagement
   - Report submission
   - Multi-language support

### **Communication:**
- **Admin → Backend**: REST API with JWT auth
- **Frontend → Backend**: REST API (public endpoints)
- **Vite Proxy**: Handles `/api/*` forwarding
- **CORS**: Configured for all origins
- **Serializers**: Handle data validation & transformation

### **Key Features:**
- ✅ JWT Authentication
- ✅ Role-Based Access Control
- ✅ File Upload Support
- ✅ Real-time Data Sync
- ✅ Error Handling
- ✅ API Documentation
- ✅ Mobile-Responsive
- ✅ Multi-language Support

---

**This architecture provides a complete, production-ready CMS with separation of concerns, security, and scalability!** 🚀
