# Sauti Frontend & Admin Synchronization Guide

## 🔄 Overview
This document outlines how the **Sauti Public Frontend** and **Sauti Admin Dashboard** are synchronized and work together.

---

## 🏗️ Architecture

```
┌─────────────────────┐
│  Sauti Frontend     │ ← Public Website (Port 3000)
│  (Vue 3 + Vite)     │
└──────────┬──────────┘
           │
           │ API Calls
           ↓
┌─────────────────────┐
│   Django Backend    │ ← REST API (Port 8000)
│   (Django + DRF)    │
└──────────┬──────────┘
           │
           │ API Calls
           ↑
┌─────────────────────┐
│   Sauti Admin       │ ← Admin Dashboard (Port 3002)
│  (Vue 3 + Vite)     │
└─────────────────────┘
```

---

## 📁 Project Structure Comparison

| Feature | Sauti Frontend | Sauti Admin |
|---------|----------------|-------------|
| **Port** | 3000 | 3002 |
| **Purpose** | Public-facing website | Content management dashboard |
| **Users** | General public, citizens | Admin staff, case workers |
| **Store Path** | `@/store/` | `@/stores/` |
| **Auth Keys** | `token`, `refreshToken`, `user` | `admin_token`, `admin_refresh_token`, `admin_user` |
| **Primary Color** | #CC5500 (Orange Accent) | #E65100 (Orange Primary) |
| **Dependencies** | Vue Router, Pinia, Chart.js, Carousel | Vue Router, Pinia, Toastification |

---

## 🔑 Authentication Flow

### Frontend (Public)
```javascript
// Login Flow
User → Login Form → Django API → JWT Token → Store in localStorage
                                            → Redirect to Home

// Storage Keys
localStorage.setItem('token', access)
localStorage.setItem('refreshToken', refresh)
localStorage.setItem('user', JSON.stringify(userData))
```

### Admin Dashboard
```javascript
// Login Flow  
Admin → Login Form → Django API → JWT Token → Store in localStorage
                                            → Redirect to Dashboard

// Storage Keys (Prefixed with 'admin_')
localStorage.setItem('admin_token', access)
localStorage.setItem('admin_refresh_token', refresh)
localStorage.setItem('admin_user', JSON.stringify(userData))
```

**Why Different Keys?**
- Prevents conflicts if admin and public site are used in same browser
- Allows separate session management
- Admin sessions can have different timeout policies

---

## 🎨 Design System Sync

### Color Palette

#### Sauti Frontend (Black/White + Orange)
```javascript
primary: #262626 (Neutral Dark)
secondary: #CC5500 (Accent Orange)
success: #10b981 (Green)
danger: #ef4444 (Red)
purple: #8b5cf6 (GBV)
teal: #14b8a6 (Resources)
```

#### Sauti Admin (Orange Theme)
```javascript
primary: #E65100 (Primary Orange)
gray: #71717a (Neutral Gray)
```

### Typography
Both use **Inter** font family for consistency.

---

## 🔗 API Integration

Both projects share the same API endpoints:

### Shared Axios Configuration
```javascript
baseURL: 'http://localhost:8000/api'
timeout: 15000
headers: { 'Content-Type': 'application/json' }
```

### Common API Endpoints

#### Authentication
- `POST /auth/login/` - User/Admin login
- `POST /auth/register/` - User registration (Frontend only)
- `POST /auth/token/refresh/` - Refresh JWT token
- `GET /auth/profile/` - Get user profile
- `PUT /auth/profile/` - Update user profile

#### Posts/Blog
- `GET /posts/` - List posts (public on Frontend, all on Admin)
- `GET /posts/:slug/` - Get single post
- `POST /posts/` - Create post (Admin only)
- `PUT /posts/:slug/` - Update post (Admin only)
- `DELETE /posts/:slug/` - Delete post (Admin only)

#### Videos
- `GET /videos/` - List videos
- `POST /videos/` - Upload video (Admin only)
- `PUT /videos/:id/` - Update video (Admin only)
- `DELETE /videos/:id/` - Delete video (Admin only)

#### Resources
- `GET /resources/` - List resources
- `POST /resources/` - Create resource (Admin only)

#### FAQs
- `GET /faqs/` - List FAQs
- `POST /faqs/` - Create FAQ (Admin only)

#### Partners
- `GET /partners/` - List partners
- `POST /partners/` - Create partner (Admin only)

#### Reports (Sensitive)
- `POST /reports/` - Submit report (Frontend only)
- `GET /reports/` - List reports (Admin only, encrypted)
- `GET /reports/:id/` - View report details (Admin only)

---

## 🔒 Security Differences

### Frontend (Public)
- ✅ Open registration for citizens
- ✅ Public content viewing (no auth required for most pages)
- ✅ Anonymous report submission
- ✅ Public resource access

### Admin Dashboard  
- 🔐 No registration (accounts created by superadmin)
- 🔐 All routes require authentication
- 🔐 Role-based access (ADMIN, EDITOR, AUTHOR, VIEWER)
- 🔐 Full CRUD on all content
- 🔐 Access to encrypted reports
- 🔐 User management interface

---

## 📦 Pinia Store Synchronization

### Shared Store Pattern
Both projects use Pinia with Composition API:

```javascript
// Pattern used in both
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(null)
  const user = ref(null)
  const isAuthenticated = computed(() => !!token.value)
  
  async function login(credentials) { /* ... */ }
  function logout() { /* ... */ }
  
  return { token, user, isAuthenticated, login, logout }
})
```

### Store Files Comparison

| Store | Frontend Path | Admin Path | Purpose |
|-------|---------------|------------|---------|
| Auth | `@/store/auth.js` | `@/stores/auth.js` | Authentication |
| Blog/Posts | `@/store/blog.js` | `@/stores/posts.js` | Blog content |
| Resources | `@/store/resources.js` | N/A | Public resources |
| FAQs | `@/store/faqs.js` | N/A | FAQs |
| Partners | `@/store/partners.js` | N/A | Partners |
| Dashboard | N/A | `@/stores/dashboard.js` | Admin stats |

---

## 🚀 Running Both Simultaneously

### Start All Services

```bash
# Terminal 1: Django Backend
cd sauti_cms
python manage.py runserver

# Terminal 2: Public Frontend
cd sauti-frontend
npm run dev
# Runs on http://localhost:3000

# Terminal 3: Admin Dashboard
cd sauti-admin
npm run dev -- --port 3002
# Runs on http://localhost:3002
```

### Port Configuration
- **Django Backend**: 8000
- **Public Frontend**: 3000
- **Admin Dashboard**: 3002

---

## 🔄 Data Flow Example

### Creating a Blog Post

1. **Admin creates post** (Admin Dashboard)
   ```
   Admin → PostEditView → Create Post → POST /api/posts/
   → Django saves to DB → Returns post data
   → Admin Dashboard updates local store
   ```

2. **Post appears on public site** (Frontend)
   ```
   User visits /blog → Frontend fetches posts → GET /api/posts/
   → Django returns published posts → Frontend displays in BlogList
   ```

3. **Admin updates post**
   ```
   Admin → PostEditView → Edit → PUT /api/posts/:slug/
   → Django updates DB → Returns updated data
   → Changes immediately available on Frontend
   ```

---

## 🎯 Key Synchronization Points

### 1. **API Endpoints**
Both projects call the same Django REST API endpoints. Changes to API structure must be reflected in both.

### 2. **Data Models**
Both expect the same data structure from API:
```javascript
// Post Structure (same for both)
{
  id: number,
  title: string,
  slug: string,
  content: string,
  excerpt: string,
  featured_image: string,
  author: { username, first_name, last_name },
  category: string,
  tags: string[],
  status: 'draft' | 'published',
  published_at: string,
  created_at: string,
  updated_at: string
}
```

### 3. **Authentication Tokens**
Both use JWT tokens from Django SimpleJWT:
- Access token expires in 60 minutes
- Refresh token expires in 24 hours
- Both handle token refresh automatically

### 4. **CORS Configuration**
Django backend must allow both origins:
```python
# sauti_cms/.env
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3002
```

---

## 🛠️ Development Workflow

### Adding a New Feature

1. **Backend First** (Django)
   - Create/update models in `sauti_cms/app/models.py`
   - Create serializers in `sauti_cms/app/serializers.py`
   - Create views in `sauti_cms/app/views.py`
   - Add URL routes in `sauti_cms/app/urls.py`
   - Run migrations: `python manage.py makemigrations && python manage.py migrate`

2. **Admin Dashboard** (Management Interface)
   - Create store in `sauti-admin/src/stores/`
   - Create view component in `sauti-admin/src/views/`
   - Add route in `sauti-admin/src/router/index.js`
   - Update API client in `sauti-admin/src/utils/api.js`

3. **Public Frontend** (Display Interface)
   - Create store in `sauti-frontend/src/store/`
   - Create view component in `sauti-frontend/src/views/`
   - Add route in `sauti-frontend/src/router/index.js`
   - Update API client in `sauti-frontend/src/utils/axios.js`

### Example: Adding "Events" Feature

```bash
# 1. Backend
cd sauti_cms
# Create events app
python manage.py startapp events
# Add models, serializers, views, urls
python manage.py makemigrations
python manage.py migrate

# 2. Admin Dashboard
cd ../sauti-admin
# Create store
touch src/stores/events.js
# Create views
touch src/views/EventsView.vue
touch src/views/EventEditView.vue
# Update router and API

# 3. Public Frontend
cd ../sauti-frontend
# Create store
touch src/store/events.js
# Create view
touch src/views/Events.vue
# Update router
```

---

## 🧪 Testing Sync

### Manual Testing Checklist

- [ ] Login on Admin → Create post → Verify appears on Frontend
- [ ] Login on Frontend → Check posts load correctly
- [ ] Admin: Edit post → Frontend: Verify changes reflected
- [ ] Admin: Delete post → Frontend: Verify post removed
- [ ] Admin: Upload video → Frontend: Verify video displays
- [ ] Frontend: Submit report → Admin: Verify report received
- [ ] Test authentication flow on both (login/logout)
- [ ] Test token refresh on both
- [ ] Test API error handling on both
- [ ] Test offline/network error scenarios

### API Testing
```bash
# Test endpoints with curl
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'

curl -X GET http://localhost:8000/api/posts/ \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## 🐛 Common Sync Issues

### Issue 1: "API endpoint not found"
**Cause**: Frontend/Admin calling endpoint that doesn't exist in Django
**Fix**: Check Django `urls.py` and ensure endpoint is registered

### Issue 2: "CORS error"
**Cause**: Frontend origin not in Django CORS_ALLOWED_ORIGINS
**Fix**: Add origin to `sauti_cms/.env`
```bash
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3002
```

### Issue 3: "Token expired"
**Cause**: JWT access token expired (60 min default)
**Fix**: Both apps auto-refresh tokens, but check refresh token not expired

### Issue 4: "Data structure mismatch"
**Cause**: Django API returning different structure than expected
**Fix**: Check serializer output matches frontend expectations

### Issue 5: "Store not updating"
**Cause**: Pinia store not reactive or not awaiting API calls
**Fix**: Ensure proper async/await and reactive refs

---

## 📝 Maintenance Notes

### When Updating Django Models
1. Update model in `sauti_cms/app/models.py`
2. Run migrations
3. Update serializer
4. Update both Frontend and Admin stores/API clients
5. Test API endpoints
6. Update both UIs to display new fields

### When Changing API Endpoints
1. Update Django view and URL
2. Update `sauti-admin/src/utils/api.js`
3. Update `sauti-frontend/src/utils/axios.js`
4. Update stores in both projects
5. Test all affected components

### When Adding New Roles/Permissions
1. Update Django User model
2. Update both auth stores
3. Update route guards in both routers
4. Test permission checks on both sides

---

## 🔮 Future Enhancements

### Planned Sync Improvements
- [ ] Shared TypeScript types for API responses
- [ ] Shared component library (buttons, forms, cards)
- [ ] Unified error handling utility
- [ ] Real-time sync with WebSockets
- [ ] Shared validation schemas (Yup/Zod)
- [ ] Shared constant values (status codes, roles, etc)
- [ ] Storybook for shared components
- [ ] E2E tests covering both frontends

### Recommended Structure
```
cms_website_template/
├── sauti-shared/          # NEW: Shared code
│   ├── types/            # TypeScript types
│   ├── constants/        # Shared constants
│   ├── utils/            # Shared utilities
│   └── components/       # Shared Vue components
├── sauti-frontend/
├── sauti-admin/
└── sauti_cms/
```

---

## 📚 Resources

- [Vue 3 Documentation](https://vuejs.org/)
- [Pinia Documentation](https://pinia.vuejs.org/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/)
- [Vite Documentation](https://vitejs.dev/)
- [TailwindCSS](https://tailwindcss.com/)

---

## 👥 Team Contacts

For questions about sync:
- **Frontend**: Frontend Team
- **Backend**: Backend Team  
- **DevOps**: DevOps Team

---

*Last Updated: October 24, 2025*
