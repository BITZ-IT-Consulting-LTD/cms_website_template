# 🔄 Sauti Platform - Frontend & Admin Synchronization

This document explains how the **Sauti Public Frontend** and **Sauti Admin Dashboard** are synchronized and work together as a unified platform.

## 🎯 Quick Start

### Start Both Frontends at Once
```bash
./start-frontends.sh
```

This will start:
- 🌐 **Public Frontend** on http://localhost:3000
- 👑 **Admin Dashboard** on http://localhost:3002

### Or Start Individually

**Public Frontend:**
```bash
cd sauti-frontend
npm run dev
```

**Admin Dashboard:**
```bash
cd sauti-admin
npm run dev -- --port 3002
```

## 🏗️ Architecture Overview

```
┌──────────────────────┐
│   Public Website     │ ← Citizens, General Public
│   Port: 3000         │   (Report issues, view resources)
└──────────┬───────────┘
           │
           ↓ HTTP/REST
┌──────────────────────┐
│   Django Backend     │ ← Central API Server
│   Port: 8000         │   (JWT Auth, Data Storage)
└──────────┬───────────┘
           ↑ HTTP/REST
           │
┌──────────────────────┐
│  Admin Dashboard     │ ← Staff, Case Workers
│   Port: 3002         │   (Manage content, view cases)
└──────────────────────┘
```

## 🔑 Key Synchronization Points

### 1. **Shared Backend API**
Both frontends connect to the same Django REST API at `http://localhost:8000/api`

| Feature | Endpoint | Frontend Access | Admin Access |
|---------|----------|-----------------|--------------|
| Authentication | `/auth/login/` | ✅ Public login | ✅ Admin login |
| Blog Posts | `/posts/` | ✅ Read only | ✅ Full CRUD |
| Videos | `/videos/` | ✅ Read only | ✅ Full CRUD |
| Resources | `/resources/` | ✅ Read only | ✅ Full CRUD |
| FAQs | `/faqs/` | ✅ Read only | ✅ Full CRUD |
| Reports | `/reports/` | ✅ Submit only | ✅ View all (encrypted) |
| Partners | `/partners/` | ✅ Read only | ✅ Full CRUD |

### 2. **Unified Design System**

Both projects now share the same color palette:

```javascript
// Sauti Brand Colors
Primary Orange:  #CC5500
Text Dark:       #262626
Success Green:   #10b981
Danger Red:      #ef4444
GBV Purple:      #8b5cf6
Resources Teal:  #14b8a6
```

**Typography:** Both use `Inter` font family

### 3. **Authentication Strategy**

Both use JWT tokens from Django, but with separate storage keys:

**Frontend (Public):**
- `localStorage.getItem('token')`
- `localStorage.getItem('refreshToken')`
- `localStorage.getItem('user')`

**Admin:**
- `localStorage.getItem('admin_token')`
- `localStorage.getItem('admin_refresh_token')`
- `localStorage.getItem('admin_user')`

**Why Different?** This prevents conflicts and allows:
- Separate session management
- Different timeout policies
- Admin can be logged into both simultaneously

### 4. **Data Flow Example**

**Creating a Blog Post:**

1. Admin creates post in Admin Dashboard
2. POST request sent to Django API: `/api/posts/`
3. Django saves to database
4. Post immediately available on Public Frontend
5. When user visits `/blog`, Frontend fetches from same API

```
Admin Dashboard → Django API → Database
                       ↓
                  Public Frontend
```

### 5. **Pinia Store Structure**

Both projects use Pinia for state management with identical patterns:

**Frontend Stores:**
- `@/store/auth.js` - Authentication
- `@/store/blog.js` - Blog posts
- `@/store/resources.js` - Resources
- `@/store/faqs.js` - FAQs
- `@/store/partners.js` - Partners

**Admin Stores:**
- `@/stores/auth.js` - Authentication
- `@/stores/posts.js` - Blog posts management
- `@/stores/dashboard.js` - Dashboard stats

## 🔧 Configuration Files

### Environment Variables

**Frontend (`.env`):**
```bash
VITE_API_URL=http://localhost:8000/api
VITE_APP_NAME=Sauti Child Helpline
VITE_HOTLINE=116
```

**Admin (`.env`):**
```bash
VITE_API_URL=http://localhost:8000/api
```

**Backend (`.env`):**
```bash
DEBUG=True
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3002
```

### Axios/API Configuration

Both projects have identical axios setup:

```javascript
// Base URL
baseURL: 'http://localhost:8000/api'

// Request Interceptor
config.headers.Authorization = `Bearer ${token}`

// Response Interceptor
- Handle 401: Logout and redirect to login
- Handle 403: Show permission error
- Handle 500: Show server error
```

## 📦 Shared Dependencies

Both projects use:
- **Vue 3** with Composition API
- **Vite** for build tooling
- **TailwindCSS** for styling
- **Pinia** for state management
- **Vue Router** for routing
- **Axios** for API calls

## 🚀 Development Workflow

### When Adding a New Feature

1. **Backend First (Django)**
   ```bash
   cd sauti_cms
   # Create model, serializer, view, URL
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Admin Dashboard (Management)**
   ```bash
   cd sauti-admin
   # Create store, views, routes
   # Add CRUD interface
   ```

3. **Public Frontend (Display)**
   ```bash
   cd sauti-frontend
   # Create store, views, routes
   # Add read-only display
   ```

### Example: Adding "Events" Feature

```bash
# 1. Backend
cd sauti_cms
python manage.py startapp events
# Add models, serializers, views, urls

# 2. Admin
cd ../sauti-admin
touch src/stores/events.js
touch src/views/EventsView.vue

# 3. Frontend
cd ../sauti-frontend
touch src/store/events.js
touch src/views/Events.vue
```

## 🔒 Security Sync

### Public Frontend
- ✅ Open user registration
- ✅ Anonymous report submission
- ✅ Public content access
- 🔒 Authentication for user profile

### Admin Dashboard
- 🔐 No public registration
- 🔐 All routes require authentication
- 🔐 Role-based access control
- 🔐 Full CRUD on all resources

### Shared Security Features
- JWT token authentication
- Automatic token refresh
- 401 handling (auto-logout)
- HTTPS in production
- CSRF protection

## 🧪 Testing Synchronization

### Manual Test Checklist

```bash
# Start all services
./start-frontends.sh

# In another terminal, start Django
cd sauti_cms
python manage.py runserver
```

**Then test:**

- [ ] **Admin Login** → http://localhost:3002/login (admin/admin123)
- [ ] **Create Blog Post** in Admin Dashboard
- [ ] **Verify Post Appears** on Public Frontend at http://localhost:3000/blog
- [ ] **Edit Post** in Admin Dashboard
- [ ] **Refresh Public Frontend** → Changes should appear
- [ ] **Delete Post** in Admin
- [ ] **Verify Removed** from Public Frontend
- [ ] **Upload Video** in Admin
- [ ] **Check Video** displays on Public Frontend
- [ ] **Submit Report** from Public Frontend
- [ ] **View Report** in Admin Dashboard (as staff)

### API Testing

```bash
# Test shared endpoints
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'

# Should work from both frontends
curl -X GET http://localhost:8000/api/posts/ \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## 🐛 Common Sync Issues

### Issue: "CORS Error"
**Symptom:** Browser console shows CORS policy error  
**Fix:** Check `sauti_cms/.env` includes both origins:
```bash
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3002
```

### Issue: "API Not Found (404)"
**Symptom:** API endpoint returns 404  
**Fix:** Verify endpoint exists in Django `urls.py` and Django server is running

### Issue: "Unauthorized (401)"
**Symptom:** API calls fail with 401  
**Fix:** 
- Check token is stored correctly
- Verify token not expired (60 min default)
- Check authorization header format: `Bearer <token>`

### Issue: "Data Not Syncing"
**Symptom:** Changes in Admin don't appear on Frontend  
**Fix:**
- Refresh Frontend page (data is fetched on mount)
- Check both apps calling same API URL
- Verify Django backend is running
- Check browser network tab for failed requests

### Issue: "Different Port Issues"
**Symptom:** Services won't start on expected ports  
**Fix:**
- Kill processes using those ports:
  ```bash
  lsof -ti:3000 | xargs kill -9  # Frontend
  lsof -ti:3002 | xargs kill -9  # Admin
  lsof -ti:8000 | xargs kill -9  # Django
  ```

## 📊 Data Model Synchronization

Both frontends expect the same data structures from Django:

### Post/Blog
```javascript
{
  id: number
  title: string
  slug: string
  content: string
  excerpt: string
  featured_image: string
  author: {
    username: string
    first_name: string
    last_name: string
  }
  category: string
  tags: string[]
  status: 'draft' | 'published'
  published_at: string (ISO 8601)
  created_at: string
  updated_at: string
}
```

### User
```javascript
{
  id: number
  username: string
  email: string
  first_name: string
  last_name: string
  role: 'ADMIN' | 'EDITOR' | 'AUTHOR' | 'VIEWER'
  is_active: boolean
}
```

### Report (Encrypted)
```javascript
{
  id: number
  reporter_name: string (encrypted)
  reporter_contact: string (encrypted)
  incident_type: string
  description: string (encrypted)
  location: string (encrypted)
  status: 'pending' | 'in_progress' | 'resolved'
  priority: 'low' | 'medium' | 'high' | 'critical'
  created_at: string
  updated_at: string
}
```

## 🎨 Design Sync

Both projects now use the **same Tailwind colors**:

```javascript
// Primary Orange (Sauti Brand)
bg-primary-500  // #CC5500

// Text Colors
text-gray-900   // Dark text
text-gray-600   // Light text

// Status Colors
bg-success-500  // Green - success states
bg-danger-500   // Red - errors, critical
bg-purple-500   // Purple - GBV cases
bg-teal-500     // Teal - resources
```

## 📝 File Structure Comparison

```
sauti-frontend/                  sauti-admin/
├── src/                        ├── src/
│   ├── store/                  │   ├── stores/
│   │   ├── auth.js             │   │   ├── auth.js
│   │   ├── blog.js             │   │   ├── posts.js
│   │   ├── resources.js        │   │   └── dashboard.js
│   │   ├── faqs.js             │   ├── views/
│   │   └── partners.js         │   │   ├── DashboardView.vue
│   ├── views/                  │   │   ├── PostsView.vue
│   │   ├── Home.vue            │   │   ├── PostEditView.vue
│   │   ├── Blog.vue            │   │   ├── VideosView.vue
│   │   ├── Resources.vue       │   │   └── SettingsView.vue
│   │   ├── Report.vue          │   ├── components/
│   │   └── Login.vue           │   │   └── DashboardLayout.vue
│   ├── utils/                  │   └── utils/
│   │   └── axios.js            │       └── api.js
│   └── router/                 └── router/
│       └── index.js                    └── index.js
├── .env                        ├── .env
└── package.json                └── package.json
```

## 🔄 Real-Time Sync (Future)

Currently, changes require page refresh. Future enhancement:

```javascript
// WebSocket connection (planned)
const ws = new WebSocket('ws://localhost:8000/ws/')

ws.onmessage = (event) => {
  const data = JSON.parse(event.data)
  if (data.type === 'post_updated') {
    // Refresh posts in both apps
    postsStore.fetchPosts()
  }
}
```

## 📚 Documentation Links

- **[SYNC_GUIDE.md](./SYNC_GUIDE.md)** - Full synchronization guide
- **[sauti_cms/README.md](./sauti_cms/README.md)** - Backend documentation
- **[sauti-frontend/README.md](./sauti-frontend/README.md)** - Frontend docs
- **[sauti-admin/README.md](./sauti-admin/README.md)** - Admin docs

## 🤝 Contributing

When making changes that affect both frontends:

1. Update Django API first
2. Test API endpoints with Postman/curl
3. Update Admin Dashboard
4. Update Public Frontend
5. Test synchronization manually
6. Update this documentation

## 📞 Support

For sync issues:
- Check console logs in browser DevTools
- Check Django terminal for API errors
- Check network tab for failed requests
- Review [SYNC_GUIDE.md](./SYNC_GUIDE.md)

---

**Last Updated:** October 24, 2025  
**Version:** 1.0.0
