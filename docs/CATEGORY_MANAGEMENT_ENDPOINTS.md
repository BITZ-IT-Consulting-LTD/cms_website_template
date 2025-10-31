# Category Management API Endpoints

**Date**: October 29, 2025
**Status**: ✅ Fully Implemented

---

## Overview

The backend provides complete CRUD endpoints for managing categories across all content types:
- **Blog Posts Categories** (`/api/posts/categories/`)
- **Video Categories** (`/api/videos/categories/`)
- **FAQ Categories** (`/api/faqs/categories/`)
- **Resource Categories** (`/api/resources/categories/`)

---

## Endpoints Summary

| Content Type | Endpoint | Methods | Permission |
|-------------|----------|---------|------------|
| **Blog Posts** | `/api/posts/categories/` | GET, POST | IsEditorOrReadOnly |
| **Blog Tags** | `/api/posts/tags/` | GET, POST | IsEditorOrReadOnly |
| **Videos** | `/api/videos/categories/` | GET only | AllowAny (Read-only) ⚠️ |
| **FAQs** | `/api/faqs/categories/` | GET, POST | IsEditorOrReadOnly |
| **Resources** | `/api/resources/categories/` | GET, POST | IsEditorOrReadOnly |

---

## 1. Blog Posts Categories

### Endpoint
```
GET  /api/posts/categories/  - List all categories
POST /api/posts/categories/  - Create new category (Editors/Admins only)
```

### Implementation
**File**: `sauti_cms/posts/views.py`
```python
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsEditorOrReadOnly]
```

### Request/Response Format

**GET Response**:
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "GBV",
      "slug": "gbv",
      "description": "Gender-Based Violence resources",
      "created_at": "2025-10-29T00:06:38.367773+03:00"
    }
  ]
}
```

**POST Request** (Editors/Admins only):
```json
{
  "name": "Child Protection",
  "description": "Resources for child protection and safety"
}
```

**POST Response**:
```json
{
  "id": 2,
  "name": "Child Protection",
  "slug": "child-protection",
  "description": "Resources for child protection and safety",
  "created_at": "2025-10-29T12:00:00.000000+03:00"
}
```

### Fields
- `name` (required): Category name
- `slug` (auto-generated): URL-friendly version of name
- `description` (optional): Category description
- `created_at` (auto): Timestamp

---

## 2. Blog Posts Tags

### Endpoint
```
GET  /api/posts/tags/  - List all tags
POST /api/posts/tags/  - Create new tag (Editors/Admins only)
```

### Implementation
**File**: `sauti_cms/posts/views.py`
```python
class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsEditorOrReadOnly]
```

### Request/Response Format

**POST Request**:
```json
{
  "name": "Mental Health"
}
```

**Response**:
```json
{
  "id": 5,
  "name": "Mental Health",
  "slug": "mental-health"
}
```

---

## 3. Video Categories

### Endpoint
```
GET /api/videos/categories/  - List all video categories (Read-only)
```

### Implementation
**File**: `sauti_cms/videos/views.py`
```python
class VideoCategoryListView(generics.ListAPIView):  # ⚠️ ListAPIView only!
    queryset = VideoCategory.objects.all()
    serializer_class = VideoCategorySerializer
    permission_classes = [permissions.AllowAny]
```

### ⚠️ Issue Identified
**Problem**: Video categories endpoint is **read-only** (`ListAPIView`) while others support creation (`ListCreateAPIView`).

**Current State**: Editors/Admins cannot create video categories via API

**Recommendation**: Change to `ListCreateAPIView` to match other category endpoints

### Response Format
```json
{
  "count": 0,
  "next": null,
  "previous": null,
  "results": []
}
```

---

## 4. FAQ Categories

### Endpoint
```
GET  /api/faqs/categories/  - List all FAQ categories
POST /api/faqs/categories/  - Create new category (Editors/Admins only)
```

### Implementation
**File**: `sauti_cms/faqs/views.py`
```python
class FAQCategoryListView(generics.ListCreateAPIView):
    queryset = FAQCategory.objects.all()
    serializer_class = FAQCategorySerializer
    permission_classes = [IsEditorOrReadOnly]
```

### Request/Response Format

**POST Request**:
```json
{
  "name": "Reporting Procedures",
  "description": "How to report cases to Sauti"
}
```

**Response**:
```json
{
  "id": 1,
  "name": "Reporting Procedures",
  "slug": "reporting-procedures",
  "description": "How to report cases to Sauti",
  "created_at": "2025-10-29T12:00:00.000000+03:00"
}
```

---

## 5. Resource Categories

### Endpoint
```
GET  /api/resources/categories/  - List all resource categories
POST /api/resources/categories/  - Create new category (Editors/Admins only)
```

### Implementation
**File**: `sauti_cms/resources/views.py`
```python
class ResourceCategoryListView(generics.ListCreateAPIView):
    queryset = ResourceCategory.objects.all()
    serializer_class = ResourceCategorySerializer
    permission_classes = [IsEditorOrReadOnly]
```

### Request/Response Format

**POST Request**:
```json
{
  "name": "Legal Documents",
  "description": "Legal forms and documentation"
}
```

**Response**:
```json
{
  "id": 1,
  "name": "Legal Documents",
  "slug": "legal-documents",
  "description": "Legal forms and documentation",
  "created_at": "2025-10-29T12:00:00.000000+03:00"
}
```

---

## Permission System

### IsEditorOrReadOnly
Custom permission class that allows:
- **Anyone** (unauthenticated): Can read (GET)
- **Editors**: Can create, update, delete
- **Admins**: Can create, update, delete
- **Authors**: Can only read
- **Viewers**: Can only read

**Location**: `sauti_cms/users/permissions.py`

---

## Authentication

All POST/PUT/DELETE requests require:
- **JWT Authentication**: Include `Authorization: Bearer <token>` header
- **Editor or Admin Role**: User must have `can_publish()` permission

### Getting a Token
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

Response:
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "user": {
    "id": 1,
    "username": "admin",
    "role": "ADMIN"
  }
}
```

---

## Testing Examples

### 1. List All Blog Categories
```bash
curl http://localhost:8000/api/posts/categories/
```

### 2. Create New Blog Category (Authenticated)
```bash
curl -X POST http://localhost:8000/api/posts/categories/ \
  -H "Authorization: Bearer <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Mental Health",
    "description": "Mental health resources and support"
  }'
```

### 3. List All Video Categories
```bash
curl http://localhost:8000/api/videos/categories/
```

### 4. Create New FAQ Category (Authenticated)
```bash
curl -X POST http://localhost:8000/api/faqs/categories/ \
  -H "Authorization: Bearer <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Safety Tips",
    "description": "Tips for staying safe"
  }'
```

### 5. Create New Resource Category (Authenticated)
```bash
curl -X POST http://localhost:8000/api/resources/categories/ \
  -H "Authorization: Bearer <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Educational Materials",
    "description": "Learning resources and guides"
  }'
```

---

## Admin UI Integration

The admin dashboard should use these endpoints for category management:

### Recommended UI Flow

1. **Category Management Page** (`/categories` or per content type)
   - List all categories with name, slug, description
   - "Add Category" button
   - Edit/Delete actions

2. **Create Category Modal/Form**
   - Name field (required)
   - Description field (optional)
   - Submit → POST to appropriate endpoint

3. **Content Creation Forms**
   - Dropdown populated from category endpoint
   - "Add New Category" option that opens modal

### Example Admin Implementation
```javascript
// In a Pinia store (e.g., postsStore.js)
const fetchCategories = async () => {
  const response = await api.get('/api/posts/categories/')
  categories.value = response.data.results
}

const createCategory = async (categoryData) => {
  const response = await api.post('/api/posts/categories/', categoryData)
  await fetchCategories() // Refresh list
  return response.data
}
```

---

## ⚠️ Action Required: Fix Video Categories Endpoint

### Current Issue
Video categories endpoint only supports GET (read-only), unlike other category endpoints.

### Recommended Fix

**File**: `sauti_cms/videos/views.py`

**Change From**:
```python
class VideoCategoryListView(generics.ListAPIView):
    """List all video categories"""
    queryset = VideoCategory.objects.all()
    serializer_class = VideoCategorySerializer
    permission_classes = [permissions.AllowAny]
```

**Change To**:
```python
class VideoCategoryListView(generics.ListCreateAPIView):
    """
    GET /api/videos/categories/ - List categories
    POST /api/videos/categories/ - Create category (Editors/Admins only)
    """
    queryset = VideoCategory.objects.all()
    serializer_class = VideoCategorySerializer
    permission_classes = [IsEditorOrReadOnly]
```

### Why This Fix Is Needed
1. **Consistency**: All other content types support category creation via API
2. **Admin UI**: Admin dashboard needs to create video categories without using Django admin
3. **User Experience**: Editors should be able to manage video categories inline while creating videos

---

## Related Files

### URL Configurations
- `sauti_cms/posts/urls.py` - Blog posts and categories
- `sauti_cms/videos/urls.py` - Videos and categories
- `sauti_cms/faqs/urls.py` - FAQs and categories
- `sauti_cms/resources/urls.py` - Resources and categories

### View Implementations
- `sauti_cms/posts/views.py` - CategoryListView, TagListView
- `sauti_cms/videos/views.py` - VideoCategoryListView ⚠️
- `sauti_cms/faqs/views.py` - FAQCategoryListView
- `sauti_cms/resources/views.py` - ResourceCategoryListView

### Serializers
- `sauti_cms/posts/serializers.py` - CategorySerializer, TagSerializer
- `sauti_cms/videos/serializers.py` - VideoCategorySerializer
- `sauti_cms/faqs/serializers.py` - FAQCategorySerializer
- `sauti_cms/resources/serializers.py` - ResourceCategorySerializer

### Permissions
- `sauti_cms/users/permissions.py` - IsEditorOrReadOnly

---

## Summary

### ✅ Working Endpoints (ListCreateAPIView)
- Blog Posts Categories: `/api/posts/categories/` (GET, POST)
- Blog Tags: `/api/posts/tags/` (GET, POST)
- FAQ Categories: `/api/faqs/categories/` (GET, POST)
- Resource Categories: `/api/resources/categories/` (GET, POST)

### ⚠️ Needs Fix (ListAPIView - Read-only)
- Video Categories: `/api/videos/categories/` (GET only)

### 🎯 Recommendation
Update `VideoCategoryListView` from `ListAPIView` to `ListCreateAPIView` and add `IsEditorOrReadOnly` permission to match other category endpoints.

---

**Status**: ✅ Category endpoints exist and work for Posts, FAQs, and Resources
**Action Required**: Fix Video Categories endpoint to support POST method
