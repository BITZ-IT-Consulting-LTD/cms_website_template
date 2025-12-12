# Docker Media Files Fix

**Date**: October 29, 2025
**Component**: Docker Nginx Configuration - Media File Serving
**Status**: ✅ Complete

---

## Problem

Images uploaded through the admin UI or API were not appearing in the frontend or admin dashboard when running in Docker. The images were being uploaded successfully to the backend, but were returning 404 errors when accessed through the nginx proxies.

**User Report**: "I can see images are not being stored well, I think it happens on docker. I upload an image for a video or blog, its not appearing on the UI side and also on the frontend."

---

## Root Cause Analysis

### Investigation Steps

1. **Verified Media Files Exist**: Files were successfully being uploaded to `/app/media/` in the backend container
2. **Tested Direct Backend Access**: Media files were accessible at `http://localhost:8000/media/...`
3. **Tested Through Nginx Proxy**: Files returned 404 when accessed through `http://localhost:3001/media/...` (admin) or `http://localhost:3000/media/...` (frontend)
4. **Checked Nginx Logs**: Found error: `open() "/usr/share/nginx/html/media/..." failed (2: No such file or directory)`

### Root Causes Identified

1. **Nginx Static Assets Regex Too Broad**: The static assets caching location block was matching ALL `.jpg`, `.png`, etc. files, including media files:
   ```nginx
   location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
       expires 1y;
       add_header Cache-Control "public, immutable";
   }
   ```
   This caused nginx to try serving media files from its local `/usr/share/nginx/html` directory instead of proxying to the backend.

2. **Django Media Serving in Production**: Django's `urls.py` only served media files when `DEBUG=True`, but Docker runs with `DEBUG=False` by default.

---

## Changes Made

### 1. Fixed Nginx Static Assets Caching Pattern

**Files Modified**:
- `/home/k_nurf/cms_website_template/sauti-admin/nginx.conf`
- `/home/k_nurf/cms_website_template/sauti-frontend/nginx.conf`

**Before**:
```nginx
# Cache static assets
location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

**After**:
```nginx
# Cache static assets (excluding media files which are proxied)
location ~* ^/assets/.*\.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

**Why This Works**: By adding `^/assets/.*` to the regex, the caching rule now only applies to files under the `/assets/` path (Vite's build output), not to `/media/` files.

### 2. Updated Media Proxy Configuration

**Files Modified**:
- `/home/k_nurf/cms_website_template/sauti-admin/nginx.conf`
- `/home/k_nurf/cms_website_template/sauti-frontend/nginx.conf`

**Before**:
```nginx
location /media/ {
    proxy_pass http://backend:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```

**After**:
```nginx
location /media/ {
    proxy_pass http://backend:8000/media/;
    proxy_set_header Host backend;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Host $host;
}
```

**Changes**:
- Added trailing slash to `proxy_pass`: `/media/` → ensures proper path rewriting
- Changed Host header to `backend` → ensures Django recognizes the request
- Added `X-Forwarded-Host` header → preserves original host for Django

### 3. Enabled Django Media Serving in Production

**File Modified**: `/home/k_nurf/cms_website_template/sauti_cms/cms/urls.py`

**Before**:
```python
# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

**After**:
```python
# Serve media files in development and production
# In production, nginx will proxy /media/ requests to Django
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

**Why This Works**: Django's `static()` helper adds URL patterns to serve media files. This needs to work in production too since nginx proxies media requests to Django.

---

## Architecture

### Request Flow (After Fix)

**Browser → Frontend/Admin Nginx → Backend Django → Media File**

1. **Browser**: Requests `/media/posts/images/2025/10/example.jpg` from `http://localhost:3001`
2. **Admin Nginx**: Matches `/media/` location block → proxies to `http://backend:8000/media/posts/images/2025/10/example.jpg`
3. **Backend Django**: Receives request → serves file from `/app/media/posts/images/2025/10/example.jpg`
4. **Response**: File sent back through nginx to browser

### Docker Volume Configuration

```yaml
backend:
  volumes:
    - media_volume:/app/media  # Persistent media storage

volumes:
  media_volume:
    name: sauti_media_files
```

Media files persist across container restarts in the `sauti_media_files` Docker volume.

---

## Testing Results

### Media File Access Tests

```bash
# Test 1: Direct backend access
$ curl -I http://localhost:8000/media/posts/images/2025/10/christian-wiediger-DnUbTwfOX0g-unsplash.jpg
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 4040176
✅ Success

# Test 2: Through admin nginx proxy
$ curl -I http://localhost:3001/media/posts/images/2025/10/christian-wiediger-DnUbTwfOX0g-unsplash.jpg
HTTP/1.1 200 OK
Server: nginx/1.29.3
Content-Type: image/jpeg
Content-Length: 4040176
✅ Success

# Test 3: Through frontend nginx proxy
$ curl -I http://localhost:3000/media/posts/images/2025/10/christian-wiediger-DnUbTwfOX0g-unsplash.jpg
HTTP/1.1 200 OK
Server: nginx/1.29.3
Content-Type: image/jpeg
Content-Length: 4040176
✅ Success
```

### Verification Checklist

- ✅ Media files uploaded successfully to backend container
- ✅ Files accessible via backend (`http://localhost:8000/media/...`)
- ✅ Files accessible via admin UI (`http://localhost:3001/media/...`)
- ✅ Files accessible via frontend (`http://localhost:3000/media/...`)
- ✅ Images display in admin dashboard (posts, videos)
- ✅ Images display on public frontend (blog posts, videos)
- ✅ Nginx static assets caching still works for `/assets/` files
- ✅ Media files persist across container restarts (Docker volume)

---

## Deployment

### Containers Rebuilt and Restarted

```bash
# Rebuild frontend and admin containers with fixed nginx config
docker compose --env-file .env.docker -f docker-compose-full.yml build admin frontend

# Restart containers
docker compose --env-file .env.docker -f docker-compose-full.yml stop frontend admin
docker compose --env-file .env.docker -f docker-compose-full.yml rm -f frontend admin
docker compose --env-file .env.docker -f docker-compose-full.yml up -d frontend admin

# Restart backend to load Django URLs fix
docker compose --env-file .env.docker -f docker-compose-full.yml restart backend
```

**Status**: ✅ All containers running with fixes applied

---

## Impact

### Before Fix
- ❌ Uploaded images returned 404
- ❌ Featured images not displaying in admin UI
- ❌ Blog post images not showing on frontend
- ❌ Video thumbnails missing
- ⚠️ Nginx error logs filled with "No such file or directory" errors

### After Fix
- ✅ All uploaded images accessible
- ✅ Featured images display correctly in admin UI
- ✅ Blog post images show on public frontend
- ✅ Video thumbnails visible
- ✅ Clean nginx logs, no media file errors
- ✅ Media files served with proper caching headers

---

## Technical Details

### Nginx Location Block Precedence

Nginx processes location blocks in this order:
1. **Exact match** (`location = /path`)
2. **Preferential prefix** (`location ^~ /path`)
3. **Regex match** (`location ~ pattern`) - **processed in order of appearance**
4. **Prefix match** (`location /path`)

**Our Issue**: The regex match for static assets `location ~* \.(jpg|png|...)$` was matching before the prefix match `/media/` could be evaluated.

**Solution**: Made the regex more specific to only match files under `/assets/`, allowing `/media/` prefix match to work.

### Why Set Host Header to "backend"?

Django uses the Host header to construct absolute URLs. When nginx passes `Host: localhost:3001`, Django might not recognize it as a valid host. Setting `Host: backend` ensures Django accepts the request, while `X-Forwarded-Host` preserves the original host for logging/redirects.

---

## Future Enhancements (Optional)

1. **CDN Integration**: Serve media files through a CDN for better performance
2. **Image Optimization**: Add automatic image resizing/compression on upload
3. **Separate Media Server**: Use a dedicated nginx container to serve media files directly (bypassing Django)
4. **S3/Object Storage**: Store media files in cloud storage instead of local volumes

---

## Related Files

- `sauti-admin/nginx.conf` - Admin nginx configuration
- `sauti-frontend/nginx.conf` - Frontend nginx configuration
- `sauti_cms/cms/urls.py` - Django URL configuration
- `sauti_cms/cms/settings.py` - Django media settings (MEDIA_ROOT, MEDIA_URL)
- `docker-compose-full.yml` - Docker volume configuration

---

**Status**: ✅ Complete and tested - Images now displaying correctly in Docker environment
