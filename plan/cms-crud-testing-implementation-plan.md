# SAUTI CMS Backend CRUD Operations & Image Upload Testing Implementation Plan

## Status: PLANNING — Production-Ready Quality Assurance

---

## Executive Summary

This plan ensures **all CRUD operations** and **image/file upload functionality** work correctly in the **Django backend (sauti_cms)** before production deployment. Every API endpoint and Django admin interface will be tested systematically to prevent issues like the team member image display problem.

**Focus**: The Django backend at `sauti_cms/` is the core that manages all content and serves APIs to the frontend.

**Target**: Zero production issues, 100% functional CRUD operations, reliable image/file uploads/display across all modules.

---

## Critical Understanding: Architecture Overview

### Backend (sauti_cms/) - **PRIMARY FOCUS**
- **Django REST Framework** backend
- **Admin Interface**: Django admin at `/sauti/admin/`
- **API Endpoints**: RESTful APIs at `/api/`
- **File Management**: Handles all image/file uploads to `/media/`
- **Database**: PostgreSQL (production) or SQLite (dev)

### Frontend Applications
- **sauti-admin**: Vue.js admin dashboard (uses Django APIs)
- **sauti-frontend**: Public-facing Vue.js website (uses Django APIs)

**Key Insight**: Testing the Django backend (`sauti_cms/`) is critical because:
1. It's the single source of truth for all data
2. It serves both admin and public frontends via APIs
3. It handles all file uploads and storage
4. Issues here affect both frontends

---

## Django Apps to Test

Based on codebase analysis, these Django apps have image/file fields:

1. **posts** - Blog posts and news with featured images
2. **videos** - Videos with thumbnails and video files
3. **content** - Team members with profile images
4. **partners** - Partner logos
5. **resources** - Downloadable files with thumbnails
6. **sitesettings** - Organization logo, favicon, team photo
7. **faqs** - No images, but test CRUD
8. **services** - No images currently
9. **timeline** - No images currently
10. **social_media** - Social media links (no files)

---

## Issues Identified

### Issue 1: Team Member Image Upload & Display ⚠️ **CRITICAL**
- **Symptom**: Images uploaded for team members don't appear on frontend
- **Location**: `sauti_cms/content/` app
- **Model**: `TeamMember` ([content/models.py:229-266](sauti_cms/content/models.py#L229-L266))
- **Serializer**: `TeamMemberSerializer` has `get_image_url()` method ([content/serializers.py:32-59](sauti_cms/content/serializers.py#L32-L59))
- **Potential Causes**:
  - Image file not saved to disk at `/media/team_members/`
  - API response not including `image_url` field
  - Frontend component not rendering the URL correctly
  - Path/permission issues in media directory
  - Docker proxy URL resolution issue

### Issue 2: Inconsistent Image URL Serialization Patterns
- **Symptom**: Different serializers use different patterns for building absolute URLs
- **Observation**:
  - ✅ **posts**: Has proper `get_featured_image()` with Docker-aware URL building
  - ✅ **videos**: Has proper `get_thumbnail()` with Docker-aware URL building
  - ✅ **partners**: Has proper `get_logo_url()` with Docker-aware URL building
  - ✅ **content**: Has proper `get_image_url()` with Docker-aware URL building
  - ✅ **resources**: Has `_build_absolute_url()` helper method
  - ❌ **sitesettings**: `OrganizationProfileSerializer` uses `fields = '__all__'` - **NO custom image URL methods!**

### Issue 3: OrganizationProfile Serializer Missing Image URL Methods ⚠️ **HIGH PRIORITY**
- **File**: [sauti_cms/sitesettings/serializers.py:17-21](sauti_cms/sitesettings/serializers.py#L17-L21)
- **Problem**: Uses `fields = '__all__'` which returns relative paths, not absolute URLs
- **Image Fields**:
  - `logo` → needs `logo_url` SerializerMethodField
  - `favicon` → needs `favicon_url` SerializerMethodField
  - `team_photo` → needs `team_photo_url` SerializerMethodField
- **Impact**: Frontend cannot display organization logo, favicon, or team photo

### Issue 4: Incomplete CRUD Testing
- **Symptom**: Some pages work, others don't - inconsistent behavior
- **Root Cause**: No systematic testing of Create, Read, Update, Delete operations
- **Impact**: Risk of production failures

### Issue 5: Report Management - Case Status Update Not Working ⚠️ **CRITICAL - FRONTEND BUG**
- **Symptom**: When trying to change status of a case (e.g., from "Pending" to "Resolved") under Report Management, the update doesn't work
- **Location**: ⚠️ **FRONTEND**: `sauti-admin/` Vue application (NOT backend)
- **Operation**: UPDATE operation - frontend not calling API correctly
- **Testing Results**: ✅ **Backend API is WORKING correctly**
  - ✅ API endpoint `/api/reports/<id>/` supports PATCH method
  - ✅ `ReportUpdateSerializer` includes `status` field
  - ✅ Status updates persist in database
  - ✅ Tested: PENDING → IN_PROGRESS → RESOLVED (all working)
  - ✅ JWT authentication working
  - ✅ Permissions working (requires Editor/Admin role)
- **Root Cause**: Frontend bug - likely causes:
  1. Frontend not sending PATCH/PUT request (may be using POST or GET)
  2. Frontend not including JWT token in Authorization header
  3. Frontend sending wrong status value (e.g., "Resolved" instead of "RESOLVED")
  4. Frontend not handling API response correctly
  5. Missing CSRF token in request
  6. Calling wrong endpoint URL
- **Impact**:
  - Reports cannot be managed/tracked properly through UI
  - Case workflow broken in admin dashboard
  - Backend working but frontend not utilizing it
- **Testing Priority**: HIGH - Frontend fix required
- **Next Steps**:
  - Locate Vue component handling status updates in `sauti-admin/src/views/` or `sauti-admin/src/components/`
  - Check axios API call configuration
  - Verify HTTP method (should be PATCH or PUT, not POST)
  - Confirm Authorization header with Bearer token
  - Check status value format (should be enum: PENDING, IN_PROGRESS, RESOLVED, etc.)

---

## Phase 1: Fix Critical Serializer Issues

### 1.1 Fix OrganizationProfileSerializer ⚠️ **DO THIS FIRST**

**Problem**: `OrganizationProfileSerializer` doesn't build absolute URLs for images.

**Solution**: Add SerializerMethodFields for all image fields.

**File**: `sauti_cms/sitesettings/serializers.py`

**Required Changes**:
```python
class OrganizationProfileSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    favicon_url = serializers.SerializerMethodField()
    team_photo_url = serializers.SerializerMethodField()

    class Meta:
        model = OrganizationProfile
        fields = '__all__'
        read_only_fields = ('last_updated', 'logo_url', 'favicon_url', 'team_photo_url')

    def _build_absolute_url(self, image_field):
        """Helper to build absolute URL for image fields"""
        if not image_field:
            return None

        try:
            image_url = image_field.url
        except (ValueError, AttributeError):
            return None

        request = self.context.get('request')
        if request:
            host = request.META.get('HTTP_X_FORWARDED_HOST', request.get_host())
            scheme = request.META.get('HTTP_X_FORWARDED_PROTO', request.scheme)
            if host == 'backend':
                host = 'localhost:8080'
                scheme = 'http'
            return f"{scheme}://{host}{image_url}"

        return f"http://localhost:8080{image_url}" if image_url else None

    def get_logo_url(self, obj):
        return self._build_absolute_url(obj.logo)

    def get_favicon_url(self, obj):
        return self._build_absolute_url(obj.favicon)

    def get_team_photo_url(self, obj):
        return self._build_absolute_url(obj.team_photo)
```

---

## Phase 2: Systematic Testing Plan

### Test Environment Setup

**Prerequisites**:
- [ ] Docker containers running (`docker-compose up -d`)
- [ ] Django backend accessible at `http://localhost:8080/sauti/admin/`
- [ ] API accessible at `http://localhost:8080/api/`
- [ ] Test images prepared (JPEG/PNG, various sizes)
- [ ] Browser DevTools ready for network inspection

**Test Image Set**:
- Small: 100x100px, ~10KB
- Medium: 800x600px, ~200KB
- Large: 2000x1500px, ~2MB
- Formats: JPEG, PNG, WebP (for partners), SVG (for logos)

---

### 2.1 Django Admin CRUD Testing Matrix

For each app, test CRUD operations through Django admin interface.

#### **App: posts (Blog/News)**

**Model**: `Post`
**Admin URL**: `/sauti/admin/posts/post/`
**Image Field**: `featured_image` → upload path: `posts/images/%Y/%m/`

| Operation | Test Steps | Expected Result | Status |
|-----------|-----------|-----------------|--------|
| **CREATE** | 1. Navigate to Posts > Add Post<br>2. Fill: title, slug, content, category<br>3. Upload featured_image (JPEG)<br>4. Set status=DRAFT, Save | - Post created<br>- Image saved to `/media/posts/images/2026/02/`<br>- Admin shows image preview | 🔄 |
| **READ** | 1. Open created post in admin<br>2. Verify all fields display<br>3. Check image preview | - All fields visible<br>- Image displays | 🔄 |
| **UPDATE** | 1. Edit post, change title and image<br>2. Upload new featured_image<br>3. Save | - Title updated<br>- New image saved<br>- Old image handled (kept or deleted) | 🔄 |
| **DELETE** | 1. Select post, Delete<br>2. Confirm deletion<br>3. Check filesystem | - Post removed from DB<br>- Image file deleted from disk | 🔄 |

**API Testing**:
- [ ] `GET /api/posts/` → Returns list with `featured_image` URLs (absolute)
- [ ] `GET /api/posts/<slug>/` → Returns detail with `featured_image` URL
- [ ] `POST /api/posts/` → Create post with image upload
- [ ] `PUT /api/posts/<slug>/` → Update post with new image
- [ ] `DELETE /api/posts/<slug>/` → Delete post

---

#### **App: videos**

**Model**: `Video`
**Admin URL**: `/sauti/admin/videos/video/`
**Image Field**: `thumbnail` → upload path: `videos/thumbnails/%Y/%m/`
**File Field**: `video_file` → upload path: `videos/files/%Y/%m/`

| Operation | Test Case | Test Steps | Expected Result | Status |
|-----------|-----------|-----------|-----------------|--------|
| **CREATE** | YouTube Video | 1. Add Video<br>2. Set video_type=YOUTUBE<br>3. Paste YouTube URL<br>4. Save | - `youtube_id` extracted<br>- `youtube_thumbnail_url` auto-generated<br>- Video playable on frontend | 🔄 |
| **CREATE** | Uploaded Video | 1. Add Video<br>2. Set video_type=UPLOADED<br>3. Upload video_file (MP4)<br>4. Upload thumbnail<br>5. Save | - video_file saved to `/media/videos/files/`<br>- thumbnail saved to `/media/videos/thumbnails/`<br>- API returns both URLs | 🔄 |
| **READ** | Admin List | 1. Open Videos list in admin | - All videos display<br>- Thumbnails show | 🔄 |
| **UPDATE** | Change Thumbnail | 1. Edit video<br>2. Upload new thumbnail<br>3. Save | - New thumbnail saved<br>- Old thumbnail handled | 🔄 |
| **DELETE** | Delete Video | 1. Delete video<br>2. Check filesystem | - Video removed from DB<br>- Files deleted from disk | 🔄 |

**API Testing**:
- [ ] `GET /api/videos/` → Returns list with `thumbnail` URLs
- [ ] `GET /api/videos/<slug>/` → Returns detail with `youtube_thumbnail_url` or custom `thumbnail`
- [ ] Check both YouTube and uploaded video types work correctly

---

#### **App: content (Team Members)** ⚠️ **PRIORITY - Known Issue**

**Model**: `TeamMember`
**Admin URL**: `/sauti/admin/content/teammember/`
**Image Field**: `image` → upload path: `team_members/`

| Operation | Test Steps | Expected Result | Actual Result | Status |
|-----------|-----------|-----------------|---------------|--------|
| **CREATE** | 1. Navigate to Content > Team Members > Add<br>2. Fill: name="Test Member", role="Tester"<br>3. Upload image (200x200px JPEG)<br>4. Set order=1, is_active=True<br>5. Save | ✅ Member created<br>✅ Image saved to `/media/team_members/filename.jpg`<br>✅ Admin shows image preview | ❌ **TO TEST** | 🔄 |
| **READ (Admin)** | 1. Open team member in admin<br>2. Check image field | ✅ Image displays in admin | ❌ **TO TEST** | 🔄 |
| **READ (API)** | 1. `GET /api/content/team-members/`<br>2. Inspect response JSON | ✅ Returns:<br>```json<br>{<br>  "image": "team_members/filename.jpg",<br>  "image_url": "http://localhost:8080/sauti/media/team_members/filename.jpg"<br>}<br>``` | ❌ **TO TEST** | 🔄 |
| **READ (Frontend)** | 1. Open `/about` page<br>2. Check "Our Team" section | ✅ Team member displays with image | ❌ **CURRENTLY BROKEN** | ❌ |
| **UPDATE** | 1. Edit team member<br>2. Upload new image<br>3. Save | ✅ New image saved<br>✅ Old image replaced | ❌ **TO TEST** | 🔄 |
| **DELETE** | 1. Delete team member<br>2. Check filesystem | ✅ Member removed<br>✅ Image file deleted | ❌ **TO TEST** | 🔄 |

**Debugging Steps if Image Doesn't Display**:
1. [ ] Check Django logs: `docker logs sauti_backend_dev`
2. [ ] Verify file exists: `ls media/team_members/`
3. [ ] Check database: `SELECT id, name, image FROM content_teammember;`
4. [ ] Test API directly: `curl http://localhost:8080/api/content/team-members/`
5. [ ] Check browser Network tab: Look for 404 on image URL
6. [ ] Verify serializer returns `image_url`: Inspect JSON response
7. [ ] Check frontend component: `sauti-frontend/src/views/AboutPage.vue`

---

#### **App: partners**

**Model**: `Partner`
**Admin URL**: `/sauti/admin/partners/partner/`
**Image Field**: `logo` → upload path: custom function with timestamp

| Operation | Test Steps | Expected Result | Status |
|-----------|-----------|-----------------|--------|
| **CREATE** | 1. Add Partner<br>2. Fill name, partner_type<br>3. Upload logo (PNG with transparency)<br>4. Save | - Partner created<br>- Logo saved with unique filename<br>- `logo_url` includes timestamp/UUID | 🔄 |
| **READ** | Admin & API | - Logo displays in admin<br>- API returns `logo_url` with absolute path | 🔄 |
| **UPDATE** | Change logo | - New logo saved<br>- Old logo handled (cache-busting works) | 🔄 |
| **DELETE** | Delete partner | - Partner removed<br>- Logo file deleted | 🔄 |

**API Testing**:
- [ ] `GET /api/partners/` → Returns `logo_url` for each partner
- [ ] Verify logo URLs are accessible (no 404)

---

#### **App: resources**

**Model**: `Resource`
**Admin URL**: `/sauti/admin/resources/resource/`
**File Field**: `file` → upload path: `resources/files/%Y/%m/`
**Image Field**: `thumbnail` → upload path: `resources/thumbnails/`

| Operation | Test Steps | Expected Result | Status |
|-----------|-----------|-----------------|--------|
| **CREATE** | 1. Add Resource<br>2. Fill title, category<br>3. Upload file (PDF, DOCX, or other)<br>4. Upload thumbnail image<br>5. Save | - Resource created<br>- File saved to `/media/resources/files/`<br>- Thumbnail saved to `/media/resources/thumbnails/`<br>- `file_size` and `file_type` auto-detected | 🔄 |
| **READ** | API | - `GET /api/resources/` returns `file` and `thumbnail` URLs | 🔄 |
| **UPDATE** | Replace file | - New file uploaded<br>- Old file handled | 🔄 |
| **DELETE** | Delete resource | - Resource removed<br>- File and thumbnail deleted | 🔄 |

**API Testing**:
- [ ] Download link works: Click file URL → File downloads
- [ ] Thumbnail displays on frontend

---

#### **App: sitesettings (Organization Profile)** ⚠️ **HIGH PRIORITY**

**Model**: `OrganizationProfile` (singleton)
**Admin URL**: `/sauti/admin/sitesettings/organizationprofile/`
**Image Fields**:
- `logo` → upload path: `org/identity/`
- `favicon` → upload path: `org/identity/`
- `team_photo` → upload path: `org/identity/`

| Operation | Test Steps | Expected Result | Status |
|-----------|-----------|-----------------|--------|
| **CREATE** | N/A - Singleton (only one instance allowed) | - | N/A |
| **READ (Admin)** | 1. Open Organization Profile in admin | - All fields display<br>- Images show previews | 🔄 |
| **UPDATE** | 1. Edit Organization Profile<br>2. Upload logo (PNG/SVG)<br>3. Upload favicon (ICO/PNG)<br>4. Upload team_photo (JPEG)<br>5. Save | - All images saved to `/media/org/identity/`<br>- Admin shows image previews | 🔄 |
| **READ (API)** | 1. `GET /api/sitesettings/organization-profile/` | ✅ **AFTER FIX**:<br>```json<br>{<br>  "logo": "org/identity/logo.png",<br>  "logo_url": "http://localhost:8080/sauti/media/org/identity/logo.png",<br>  "favicon": "org/identity/favicon.ico",<br>  "favicon_url": "http://localhost:8080/sauti/media/org/identity/favicon.ico",<br>  "team_photo": "org/identity/team.jpg",<br>  "team_photo_url": "http://localhost:8080/sauti/media/org/identity/team.jpg"<br>}<br>```<br><br>❌ **BEFORE FIX**:<br>Only relative paths returned | 🔄 |
| **READ (Frontend)** | 1. Check header for logo<br>2. Check browser tab for favicon<br>3. Check About page for team photo | - Logo displays in header<br>- Favicon shows in browser tab<br>- Team photo displays on About page | 🔄 |

**Critical Test**: Verify frontend receives absolute URLs after serializer fix.

---

#### **App: faqs (No Images)**

**Model**: `FAQ`
**Admin URL**: `/sauti/admin/faqs/faq/`
**Fields**: question, answer, language, category

| Operation | Test Steps | Expected Result | Status |
|-----------|-----------|-----------------|--------|
| **CREATE** | 1. Add FAQ<br>2. Fill question, answer<br>3. Set language=EN or LG<br>4. Save | - FAQ created | 🔄 |
| **READ** | Admin & API | - FAQ displays correctly<br>- Language filtering works | 🔄 |
| **UPDATE** | Edit FAQ | - Changes saved | 🔄 |
| **DELETE** | Delete FAQ | - FAQ removed | 🔄 |

**API Testing**:
- [ ] `GET /api/faqs/` → Returns all FAQs
- [ ] `GET /api/faqs/?language=EN` → Filters by language

---

### 2.2 Image Format Support Testing

Test each image format on each module with image fields:

| Module | Field | PNG | JPEG | WebP | SVG | GIF | Notes |
|--------|-------|-----|------|------|-----|-----|-------|
| posts | featured_image | ✅ | ✅ | ? | ❌ | ? | |
| videos | thumbnail | ✅ | ✅ | ? | ❌ | ? | |
| content | TeamMember.image | ✅ | ✅ | ? | ❌ | ? | |
| partners | logo | ✅ | ✅ | ✅ | ✅ | ? | Logos often need transparency |
| resources | thumbnail | ✅ | ✅ | ? | ❌ | ? | |
| sitesettings | logo | ✅ | ✅ | ✅ | ✅ | ❌ | SVG for scalability |
| sitesettings | favicon | ✅ | ✅ | ❌ | ❌ | ❌ | ICO preferred for favicons |
| sitesettings | team_photo | ✅ | ✅ | ? | ❌ | ? | |

**Test Procedure**:
1. Attempt to upload each format
2. Verify upload succeeds/fails
3. Check file is saved to disk
4. Verify API returns correct URL
5. Check frontend displays image
6. Note any format conversions

---

### 2.3 Image Size & Validation Testing

**Test Boundary Cases**:

| Test Case | Size | Expected Behavior | Status |
|-----------|------|-------------------|--------|
| Very Small | 10x10px, 1KB | ✅ Upload and display | 🔄 |
| Small | 100x100px, 10KB | ✅ Upload and display | 🔄 |
| Medium | 800x600px, 200KB | ✅ Upload and display | 🔄 |
| Large | 2000x1500px, 2MB | ✅ Upload and display | 🔄 |
| Very Large | 5000x5000px, 10MB | ⚠️ May be slow, but should work | 🔄 |
| Too Large | File > 500MB | ❌ Reject with error | 🔄 |
| Invalid File | .exe renamed to .jpg | ❌ Reject with error | 🔄 |
| Corrupted | Truncated JPEG | ❌ Reject or handle gracefully | 🔄 |

**Settings to Check**:
```python
# sauti_cms/cms/settings.py
MEDIA_URL = '/sauti/media/'
MEDIA_ROOT = BASE_DIR / 'media'
DATA_UPLOAD_MAX_MEMORY_SIZE = 500 * 1024 * 1024  # 500MB for videos
FILE_UPLOAD_MAX_MEMORY_SIZE = 500 * 1024 * 1024  # 500MB
```

---

### 2.4 Image URL Resolution Testing

Test URL building in different environments:

#### **Local Development** (direct Django access)
```bash
# Access Django directly
http://localhost:8000/sauti/admin/

# Expected image URLs
http://localhost:8000/sauti/media/team_members/photo.jpg
```

#### **Docker Development** (via nginx proxy)
```bash
# Access via nginx
http://localhost:8080/sauti/admin/

# Expected image URLs (Docker-aware)
http://localhost:8080/sauti/media/team_members/photo.jpg
```

**Test Cases**:
1. [ ] Upload image via Django admin
2. [ ] Check API response includes correct URL
3. [ ] Test URL is accessible in browser (200 OK)
4. [ ] Verify frontend displays image
5. [ ] Check no mixed content warnings (HTTP/HTTPS)

**Docker-Specific Checks**:
- [ ] When `request.META['HTTP_X_FORWARDED_HOST'] == 'backend'`
  - Serializer replaces with `localhost:8080`
  - Scheme changes to `http`
- [ ] When accessed via nginx proxy
  - URLs use `HTTP_X_FORWARDED_HOST` header
  - URLs use `HTTP_X_FORWARDED_PROTO` header

---

## Phase 3: Bug Documentation & Resolution

### 3.1 Bug Report Template

Use this template for any test failures:

```markdown
**Bug ID**: [CRUD-XXX]
**Module**: [e.g., content/TeamMember]
**Operation**: [CREATE/READ/UPDATE/DELETE]
**Severity**: [CRITICAL/HIGH/MEDIUM/LOW]

**Description**:
[What is broken]

**Steps to Reproduce**:
1. Step 1
2. Step 2
3. Step 3

**Expected Behavior**:
[What should happen]

**Actual Behavior**:
[What actually happens]

**Environment**:
- Django: [version]
- DRF: [version]
- Docker: [yes/no]
- Browser: [name + version]

**Logs/Screenshots**:
[Attach Django logs, API responses, screenshots]

**Affected Files**:
- [File 1]
- [File 2]

**Root Cause**:
[Analysis of why it's broken]

**Fix**:
[Solution/code changes]
```

---

## Phase 4: Implementation Roadmap

### **Week 1: Critical Fixes & Setup**
- [ ] **Day 1-2**: Fix `OrganizationProfileSerializer` (add image URL methods)
- [ ] **Day 3**: Test Team Member CRUD (resolve known issue)
- [ ] **Day 4**: Test Organization Profile CRUD
- [ ] **Day 5**: Document findings from critical tests

### **Week 2: Systematic CRUD Testing**
- [ ] **Day 1**: Posts (blogs/news) CRUD + image upload
- [ ] **Day 2**: Videos CRUD + YouTube vs uploaded
- [ ] **Day 3**: Partners CRUD + logo upload
- [ ] **Day 4**: Resources CRUD + file + thumbnail upload
- [ ] **Day 5**: FAQs CRUD (no images)

### **Week 3: Image Format & Size Testing**
- [ ] Test all image formats on each module
- [ ] Test boundary cases (very small, very large files)
- [ ] Test validation (invalid files, corrupted images)
- [ ] Document format support matrix

### **Week 4: Regression Testing & Production Prep**
- [ ] Re-test all modules end-to-end
- [ ] Verify all bugs fixed
- [ ] Load testing (multiple uploads)
- [ ] Final production readiness checklist

---

## Phase 5: Production Readiness Checklist

### **Backend (sauti_cms/)**
- [ ] All CRUD operations tested and passing
- [ ] All image/file uploads work
- [ ] All serializers return absolute image URLs
- [ ] API responses include all required fields
- [ ] No Django errors in logs
- [ ] File permissions correct on `/media/` directory
- [ ] Database clean (no orphaned records)
- [ ] Settings configured correctly (MEDIA_URL, MEDIA_ROOT)

### **Frontend (sauti-frontend & sauti-admin)**
- [ ] All images display correctly
- [ ] Fallback images work when image missing
- [ ] No console errors
- [ ] No 404 errors on image URLs
- [ ] Responsive design works

### **Integration**
- [ ] End-to-end: Django admin upload → API → Frontend display
- [ ] Admin pages functional
- [ ] Public pages functional
- [ ] Docker environment works
- [ ] Local development works

---

## Quick Reference

### API Endpoints
```bash
# Posts (Blogs/News)
GET    /api/posts/              # List all posts
GET    /api/posts/<slug>/       # Get post detail
POST   /api/posts/              # Create post
PUT    /api/posts/<slug>/       # Update post
DELETE /api/posts/<slug>/       # Delete post

# Videos
GET    /api/videos/             # List all videos
GET    /api/videos/<slug>/      # Get video detail
POST   /api/videos/             # Create video
PUT    /api/videos/<slug>/      # Update video
DELETE /api/videos/<slug>/      # Delete video

# Team Members
GET    /api/content/team-members/     # List all team members
GET    /api/content/team-members/<id>/ # Get team member detail
POST   /api/content/team-members/     # Create team member
PUT    /api/content/team-members/<id>/ # Update team member
DELETE /api/content/team-members/<id>/ # Delete team member

# Partners
GET    /api/partners/           # List all partners
GET    /api/partners/<id>/      # Get partner detail
POST   /api/partners/           # Create partner
PUT    /api/partners/<id>/      # Update partner
DELETE /api/partners/<id>/      # Delete partner

# Resources
GET    /api/resources/          # List all resources
GET    /api/resources/<slug>/   # Get resource detail
POST   /api/resources/          # Create resource
PUT    /api/resources/<slug>/   # Update resource
DELETE /api/resources/<slug>/   # Delete resource

# FAQs
GET    /api/faqs/               # List all FAQs
GET    /api/faqs/<id>/          # Get FAQ detail
POST   /api/faqs/               # Create FAQ
PUT    /api/faqs/<id>/          # Update FAQ
DELETE /api/faqs/<id>/          # Delete FAQ

# Organization Profile (singleton)
GET    /api/sitesettings/organization-profile/ # Get org profile
PUT    /api/sitesettings/organization-profile/ # Update org profile
```

### Django Admin URLs
```bash
/sauti/admin/posts/post/                     # Posts (blogs/news)
/sauti/admin/videos/video/                   # Videos
/sauti/admin/content/teammember/             # Team Members
/sauti/admin/partners/partner/               # Partners
/sauti/admin/resources/resource/             # Resources
/sauti/admin/faqs/faq/                       # FAQs
/sauti/admin/sitesettings/organizationprofile/ # Organization Profile
```

### Media Directories
```bash
media/posts/images/%Y/%m/           # Blog/News featured images
media/videos/thumbnails/%Y/%m/      # Video thumbnails
media/videos/files/%Y/%m/           # Uploaded video files
media/resources/files/%Y/%m/        # Resource files
media/resources/thumbnails/         # Resource thumbnails
media/team_members/                 # Team member images
media/partners/logos/               # Partner logos (with timestamp)
media/org/identity/                 # Organization logo, favicon, team photo
```

### Useful Commands
```bash
# Django shell
docker exec -it sauti_backend_dev python manage.py shell

# Check database
docker exec -it sauti_backend_dev python manage.py dbshell

# View logs
docker logs -f sauti_backend_dev

# List media files
docker exec -it sauti_backend_dev ls -la media/

# Test API
curl http://localhost:8080/api/content/team-members/
curl http://localhost:8080/api/sitesettings/organization-profile/
```

---

## Success Criteria

✅ **All Django apps tested**:
- Posts ✅
- Videos ✅
- Content (Team Members) ✅
- Partners ✅
- Resources ✅
- FAQs ✅
- SiteSettings (OrganizationProfile) ✅

✅ **All CRUD operations work**:
- Create with image/file upload ✅
- Read with absolute image URLs ✅
- Update with new image/file ✅
- Delete with file cleanup ✅

✅ **All serializers fixed**:
- OrganizationProfileSerializer has image URL methods ✅
- All image URLs are absolute ✅
- Docker proxy detection works ✅

✅ **Production ready**:
- No errors in Django logs ✅
- All images display on frontend ✅
- Zero known bugs ✅

---

## Notes

- **Focus on Backend First**: Django backend (`sauti_cms/`) is the foundation
- **Fix Serializers Early**: Fix `OrganizationProfileSerializer` before other tests
- **Test Through Admin**: Django admin is the primary content management interface
- **Verify APIs**: Always check API responses match expected format
- **Check Frontend**: After backend tests pass, verify frontend displays correctly
- **Document Everything**: Record all test results for future reference
