# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a full-stack CMS platform for Sauti Child Helpline, built to handle child protection cases, GBV reports, and migrant worker issues in Uganda. The system consists of:

- **Backend**: Django 4.2 + Django REST Framework + PostgreSQL
- **Public Frontend**: Vue 3 + Vite (port 3000) - Public-facing website
- **Admin Dashboard**: Vue 3 + Vite (port 3001/3002) - Content management

**Critical Feature**: Anonymous case reporting with Fernet encryption for sensitive data.

## Development Commands

### Running the Full Stack

```bash
# Start all services at once (recommended)
./start-all.sh

# Or start individually:
# Backend (Django)
cd sauti_cms && python manage.py runserver

# Public Frontend
cd sauti-frontend && npm run dev

# Admin Dashboard
cd sauti-admin && npm run dev -- --port 3002
```

### Backend Commands

```bash
cd sauti_cms

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Run tests for a specific app
python manage.py test posts
python manage.py test reports

# Shell access
python manage.py shell

# Collect static files
python manage.py collectstatic
```

### Frontend Commands

```bash
# Public Frontend (sauti-frontend)
cd sauti-frontend
npm install
npm run dev          # Development server (port 3000)
npm run build        # Production build
npm run preview      # Preview production build
npm run lint         # Lint code
npm run format       # Format with Prettier

# Admin Dashboard (sauti-admin)
cd sauti-admin
npm install
npm run dev          # Development server (port 3001)
npm run build
npm run preview
npm run lint
npm run format
```

### Docker Commands

```bash
# Build and start all services
docker-compose up --build

# Start in detached mode
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Access backend shell
docker-compose exec backend python manage.py shell
```

## Project Architecture

### Backend Structure (sauti_cms/)

The Django backend follows a modular app-based architecture:

- **users/** - Custom user model with role-based access (ADMIN, EDITOR, AUTHOR, VIEWER)
- **posts/** - Blog/news system with categories, tags, multilingual support
- **videos/** - Video management (YouTube URLs or file uploads)
- **resources/** - Downloadable resources (PDFs, documents)
- **faqs/** - FAQ management with categories
- **partners/** - Partner/organization profiles
- **reports/** - Anonymous case reporting with encryption (CRITICAL)
- **dashboard/** - Admin dashboard API endpoints
- **cms/** - Main Django settings and configuration

### Frontend Structure

**Public Frontend (sauti-frontend/src/)**
- `views/` - Page components (Home, About, Blog, Report, etc.)
- `components/` - Reusable UI components organized by feature
- `store/` - Pinia state management stores
- `router/` - Vue Router configuration
- `utils/axios.js` - Axios instance with JWT interceptors

**Admin Dashboard (sauti-admin/src/)**
- `views/` - Admin pages (Dashboard, Posts, Videos, Reports, Users, etc.)
- `stores/` - Pinia stores for each content type
- `components/DashboardLayout.vue` - Main admin layout with sidebar
- `utils/api.js` - Centralized API client with helper methods

### Data Flow

1. **Authentication**: JWT tokens stored in localStorage, auto-refreshed via axios interceptors
2. **Content Creation**: Admin creates content → Django saves to PostgreSQL → Public frontend fetches via API
3. **Anonymous Reporting**: Public form → Django encrypts with Fernet → Stored encrypted in database → Admin can decrypt and view
4. **Role-Based Access**: User roles checked in Django views and serializers

### Key Models

**User Model (users/models.py)**
- Custom user with `role` field (ADMIN, EDITOR, AUTHOR, VIEWER)
- Methods: `can_publish()`, `can_delete()`, `is_admin`, `is_editor`, `is_author`

**Post Model (posts/models.py)**
- Status: DRAFT or PUBLISHED
- Language: en, lg, sw
- Auto-generates slug from title
- Auto-sets `published_at` when status changes to PUBLISHED

**Report Model (reports/models.py)**
- Categories: CHILD_PROTECTION, GBV, MIGRANT, PSEA
- `encrypted_description` field - uses Fernet encryption
- Auto-generates reference number format: `SAUTI-{category_code}-{timestamp}`
- Method: `decrypt_description()` to decrypt stored data

**Video Model (videos/models.py)**
- VideoType: YOUTUBE or UPLOAD
- For YouTube: stores URL, extracts video ID
- Properties: `youtube_id`, `youtube_embed_url`, `youtube_thumbnail_url`

## Critical Implementation Details

### Encryption System

Reports use Fernet symmetric encryption for sensitive data:
- Encryption key set in `.env` as `ENCRYPTION_KEY`
- Automatic encryption on save in `reports/models.py:104-111`
- Decrypt using `report.decrypt_description()` method
- Only admins and editors should have decrypt access

### User Permissions

The system uses a custom role hierarchy:
- **ADMIN**: Full access, can delete
- **EDITOR**: Create, edit, publish content, view reports
- **AUTHOR**: Create drafts only (cannot publish)
- **VIEWER**: Read-only access

Check permissions in views using:
```python
if request.user.can_publish():
    # Allow publishing
if request.user.can_delete():
    # Allow deletion
```

### API Endpoints Pattern

All API endpoints follow this structure:
- Public endpoints: `/api/{resource}/` (no auth required for GET)
- Admin endpoints: `/api/{resource}/` (auth required for POST/PUT/DELETE)
- Authentication: JWT token in `Authorization: Bearer {token}` header

### State Management Pattern

Both frontends use Pinia stores with this pattern:
```javascript
// Stores have these common methods:
- fetchItems()      // GET list
- fetchItem(id)     // GET single item
- createItem(data)  // POST
- updateItem(id, data) // PUT/PATCH
- deleteItem(id)    // DELETE
```

### Multilingual Support

Content supports three languages (en, lg, sw):
- Filter API responses: `/api/posts/?language=lg`
- Language stored in `language` field on models
- Frontend language switcher in Header component

## Database Configuration

The system supports both PostgreSQL (production) and SQLite (development):
- Set `DB_ENGINE=sqlite` in `.env` for SQLite (easier local development)
- Set `DB_ENGINE=postgresql` for PostgreSQL (production)
- Database credentials configured via environment variables

## Testing

When writing tests:
- Use Django's `TestCase` for model and API tests
- Create test fixtures for users with different roles
- Test encryption/decryption in reports tests
- Test role-based permissions thoroughly
- Mock external services (YouTube API calls)

## Environment Variables

Required environment variables (see `.env.example`):
- `SECRET_KEY` - Django secret key (generate new for production)
- `DEBUG` - Set to False in production
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` - Database config
- `ENCRYPTION_KEY` - 32-byte Fernet key for report encryption
- `CORS_ALLOWED_ORIGINS` - Frontend URLs for CORS
- `VITE_API_URL` - Backend API URL for frontends

## Common Development Patterns

### Adding a New Content Type

1. Create Django app: `python manage.py startapp newapp`
2. Add models in `newapp/models.py`
3. Create serializers in `newapp/serializers.py`
4. Create views (ViewSet) in `newapp/views.py`
5. Register URLs in `newapp/urls.py` and `cms/urls.py`
6. Add to `INSTALLED_APPS` in settings
7. Run migrations
8. Create Pinia store in frontend
9. Create Vue components and views
10. Add to router

### Working with Reports

Reports are sensitive - always:
- Ensure encryption is enabled (check `ENCRYPTION_KEY` exists)
- Use `decrypt_description()` method, never access `encrypted_description` directly
- Check user has ADMIN or EDITOR role before displaying decrypted data
- Log access to report details for audit trail

### Debugging

- Backend errors: Check Django console output and `/sauti_cms/logs/` (if logging configured)
- Frontend errors: Check browser console and network tab
- Database issues: Connect directly with `python manage.py dbshell`
- JWT issues: Check token expiry, refresh token mechanism in axios interceptors

## Service Ports

- Backend API: `http://localhost:8000/api/`
- Django Admin: `http://localhost:8000/admin/`
- API Docs (Swagger): `http://localhost:8000/api/docs/`
- Public Frontend: `http://localhost:3000`
- Admin Dashboard: `http://localhost:3001` or `http://localhost:3002`
- PostgreSQL: `localhost:5432`

## Code Style

- Backend: Follow Django conventions, use `black` for formatting
- Frontend: Use ESLint + Prettier (configs in package.json)
- Components: Vue 3 Composition API with `<script setup>` syntax
- CSS: TailwindCSS utility classes (avoid custom CSS)

## Important Bug Fixes & Lessons Learned (newtvn branch)

The `newtvn` development branch contains critical fixes that addressed several production issues. When working with this codebase, be aware of these patterns:

### Field Name Consistency (CRITICAL)

**Problem**: Django backend expects snake_case field names, but frontend was sending camelCase.

**Solution**: Always match backend serializer field names exactly:
- Use `category` (singular) not `categories` - it's a ForeignKey
- Use `featured_image` not `featuredImage`
- Use `video_type` not `videoType`
- Status values must be UPPERCASE: `DRAFT`, `PUBLISHED` (not `draft`, `published`)

**Location**: Check serializers in `sauti_cms/{app}/serializers.py` for exact field names.

### API Client Architecture (sauti-admin/src/utils/api.js)

The admin API client has been refactored to use a centralized helper pattern:

```javascript
// New pattern - use helper methods
api.posts.create(postData)
api.posts.update(slug, postData)
api.videos.list({ status: 'DRAFT' })

// Automatically handles:
- FormData creation for file uploads
- JWT token injection
- Error handling and 401 redirects
```

**Key point**: Don't create FormData manually in stores - let the API client handle it.

### Draft/Published Workflow

**Critical**: The system distinguishes between drafts and published content:
- Dashboard counters filter by `status: 'PUBLISHED'` or `status: 'DRAFT'`
- Backend serializers auto-set `published_at` timestamp when status changes to PUBLISHED
- Drafts page must explicitly filter with `?status=DRAFT` query parameter
- Preview functionality works for both drafts and published content

### Sidebar Draft Counters

The admin sidebar shows real-time draft counts synced from the backend:
- Located in `sauti-admin/src/components/DashboardLayout.vue`
- Fetches from `/api/posts/?status=DRAFT`, `/api/videos/?status=DRAFT`
- Updates when content is created/published
- Uses dashboard store for centralized stats

### Video Upload Fix

Videos had field name mismatches causing 400 errors:
- Backend expects `video_type` (not `videoType`)
- Backend expects `youtube_url` (not `youtubeUrl`)
- After successful upload, must refresh list to prevent blank pages
- File uploads use `video_file` field

### User Management

A full user management interface was added in `newtvn`:
- Location: `sauti-admin/src/views/UsersView.vue`
- Shows user statistics (total, admins, editors, active)
- Filter by role and status
- Search functionality
- CRUD operations for team members

### Array Safety Pattern

Always check if data is an array before using array methods:

```javascript
// Bad
const validTags = tagList.filter(tag => tag)

// Good
const validTags = Array.isArray(tagList) ? tagList.filter(tag => tag) : []
```

This prevents `filter is not a function` errors when API returns null/undefined.

### Preview Implementation

Posts and videos can be previewed in the public frontend:
- Opens in new window: `window.open('http://localhost:3000/blog/{slug}', '_blank')`
- Works for both drafts and published content
- Shows appropriate messages for unsaved content
- Location: PostEditView, VideoEditView

### API Base URL Configuration

The admin uses Vite proxy configuration:
- `baseURL: '/api'` (relative path, proxied by Vite)
- Not `http://localhost:8000/api` (absolute URL)
- This allows seamless dev/production switching
- Check `vite.config.js` for proxy settings

### Status Comparison Fix

When filtering by status, always use uppercase:

```javascript
// Backend returns uppercase
items.filter(item => item.status === 'PUBLISHED') // Correct
items.filter(item => item.status === 'published')  // Wrong - no match
```

### Mock Data Removal

All mock data has been removed from stores:
- Previously used fallback mock data for categories, tags
- Now returns empty arrays if API fails
- Ensures frontend always reflects real database state
- Forces proper error handling

## Debugging Common Issues

### HTTP 400 Bad Request
- Check field names match backend serializer exactly (snake_case)
- Verify status values are uppercase (`DRAFT`, `PUBLISHED`)
- Check if ForeignKey fields are sending IDs not objects
- Look for array fields being sent as strings

### Blank Page After Upload
- Ensure list refresh after create/update operations
- Check if response data structure changed
- Verify router navigation happens after data loads

### Dashboard Counters Wrong
- Verify stats computed property accesses nested structure correctly
- Check status filtering uses uppercase values
- Ensure API response structure matches expected format

### Preview Not Working
- Verify public frontend is running on correct port
- Check slug is saved before attempting preview
- Ensure preview URL format matches router paths
