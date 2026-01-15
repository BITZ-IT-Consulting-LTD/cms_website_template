# Frontend Debugging Documentation

**Date:** January 13, 2026  
**Issue:** Frontend applications (public website and admin dashboard) returning 500 errors when making API requests  
**Status:** ✅ Resolved

---

## Table of Contents

1. [Initial Problems](#initial-problems)
2. [Root Cause Analysis](#root-cause-analysis)
3. [Solutions Implemented](#solutions-implemented)
4. [Files Modified](#files-modified)
5. [Advantages and Disadvantages](#advantages-and-disadvantages)
6. [Lessons Learned](#lessons-learned)

---

## Initial Problems

### Problem 1: Public Frontend (Port 5173) - 500 Errors
- **Endpoints Affected:**
  - `GET /api/sitesettings/` → 500 Internal Server Error
  - `GET /api/v1/calls/stats/keypair/` → 500 Internal Server Error
- **Error Details:**
  - Requests were failing with 500 status codes
  - No specific error messages visible in browser console

### Problem 2: Admin Frontend (Port 5174) - 500 Errors
- **Endpoints Affected:**
  - `POST /api/auth/login/` → 500 Internal Server Error
- **Error Details:**
  - Login functionality completely broken
  - Similar 500 errors on API requests

---

## Root Cause Analysis

### Issue 1: Vite Proxy Configuration in Docker

**Root Cause:**
- Vite dev servers were configured to proxy API requests to `http://127.0.0.1:8000`
- In Docker containers, `127.0.0.1` refers to the container itself, not the host machine
- The backend service is in a separate container, so `127.0.0.1:8000` was unreachable
- This caused connection failures and 500 errors

**Evidence:**
```javascript
// Before fix - sauti-frontend/vite.config.js
proxy: {
  '/api': {
    target: 'http://127.0.0.1:8000',  // ❌ Doesn't work in Docker
    changeOrigin: true,
    secure: false,
  },
}
```

### Issue 2: Django ALLOWED_HOSTS Configuration

**Root Cause:**
- Django's `ALLOWED_HOSTS` setting was rejecting requests due to invalid Host headers
- When nginx proxies requests, it sends the Host header as the service name (e.g., "nginx", "backend")
- The `.env` file was overriding the default `ALLOWED_HOSTS` with only `localhost,127.0.0.1`
- Django rejected requests with Host headers like "nginx" or "backend" as invalid

**Error Messages:**
```
DisallowedHost: Invalid HTTP_HOST header: 'nginx'. You may need to add 'nginx' to ALLOWED_HOSTS.
DisallowedHost: Invalid HTTP_HOST header: 'backend'. You may need to add 'backend' to ALLOWED_HOSTS.
```

### Issue 3: Nginx Host Header Configuration

**Root Cause:**
- Nginx was forwarding the original Host header from the client
- When frontend containers made requests, the Host header was set to the service name
- This caused Django to reject requests even after adding hosts to ALLOWED_HOSTS

---

## Solutions Implemented

### Solution 1: Updated Vite Proxy to Use Docker Service Names

**Changes Made:**

1. **Public Frontend (`sauti-frontend/vite.config.js`):**
   ```javascript
   // After fix
   proxy: {
     '/api': {
       target: env.VITE_API_PROXY_TARGET || 'http://127.0.0.1:8000',
       changeOrigin: true,
       secure: false,
       // No rewrite needed when proxying through nginx
     },
   }
   ```

2. **Docker Compose (`docker/docker-compose.dev.yml`):**
   ```yaml
   frontend:
     environment:
       - VITE_API_PROXY_TARGET=http://nginx:80
   ```

**Why This Works:**
- Docker Compose creates a DNS network where services can resolve each other by service name
- `nginx:80` resolves to the nginx container on the internal Docker network
- Nginx then handles routing to the backend

### Solution 2: Fixed Django ALLOWED_HOSTS

**Changes Made:**

1. **Django Settings (`sauti_cms/cms/settings.py`):**
   ```python
   # Updated default to include Docker service names
   ALLOWED_HOSTS = config('ALLOWED_HOSTS', 
       default='localhost,127.0.0.1,0.0.0.0,backend,nginx,sauti_backend_dev,sauti.local,sauti.mglsd.go.ug', 
       cast=lambda v: [s.strip() for s in v.split(',')])
   ```

2. **Docker Compose Environment Variable:**
   ```yaml
   backend:
     environment:
       - ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0,backend,nginx,sauti_backend_dev,sauti.local,sauti.mglsd.go.ug
   ```

**Why This Works:**
- Environment variables in docker-compose override `.env` file values
- Ensures Django accepts requests from all Docker service names
- Maintains security by explicitly listing allowed hosts

### Solution 3: Configured Nginx Host Header

**Changes Made:**

1. **Nginx Config (`docker/nginx/dev.conf`):**
   ```nginx
   # Removed Host header from common proxy settings
   # Common proxy settings
   proxy_http_version 1.1;
   proxy_set_header Upgrade $http_upgrade;
   proxy_set_header Connection "upgrade";
   # proxy_set_header Host $host;  # ❌ Removed this
   proxy_set_header X-Real-IP $remote_addr;
   proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
   proxy_set_header X-Forwarded-Proto $scheme;

   # API location block
   location /api/ {
       proxy_pass http://sauti_backend_dev:8000/;
       proxy_set_header Host backend;  # ✅ Set explicitly
   }
   ```

**Why This Works:**
- Sets a consistent Host header that Django expects
- "backend" is in ALLOWED_HOSTS and is RFC-compliant
- Prevents Host header spoofing issues

### Solution 4: Added Error Handling in Django Views

**Changes Made:**

1. **Sitesettings Views (`sauti_cms/sitesettings/views.py`):**
   ```python
   def get(self, request, *args, **kwargs):
       try:
           settings, created = GlobalSettings.objects.get_or_create()
           serializer = GlobalSettingsSerializer(settings)
           return Response(serializer.data)
       except Exception as e:
           import logging
           logger = logging.getLogger(__name__)
           logger.error(f"Error in GlobalSettingsView.get: {e}", exc_info=True)
           return Response(
               {"detail": "An error occurred while fetching settings."},
               status=status.HTTP_500_INTERNAL_SERVER_ERROR
           )
   ```

2. **Reports Views (`sauti_cms/reports/views.py`):**
   - Similar error handling added to `NormalizedCallStatsView`

**Why This Works:**
- Provides better error logging for debugging
- Returns proper error responses instead of crashing
- Helps identify issues in production

### Solution 5: Admin Frontend Proxy Fix

**Changes Made:**

1. **Admin Vite Config (`sauti-admin/vite.config.js`):**
   ```javascript
   proxy: {
     '/api': {
       target: process.env.VITE_API_PROXY_TARGET || 'http://nginx:80',
       changeOrigin: true,
       secure: false,
       // No rewrite needed when proxying through nginx
     },
   }
   ```

2. **Docker Compose:**
   ```yaml
   admin:
     environment:
       - VITE_API_PROXY_TARGET=http://nginx:80
   ```

**Why This Works:**
- Consistent with public frontend approach
- Routes through nginx for unified request handling
- Removes complex Host header manipulation code

---

## Files Modified

### Configuration Files

1. **`sauti-frontend/vite.config.js`**
   - Updated proxy target to use environment variable
   - Removed path rewrite (handled by nginx)

2. **`sauti-admin/vite.config.js`**
   - Updated proxy target to use nginx
   - Simplified configuration

3. **`docker/docker-compose.dev.yml`**
   - Added `VITE_API_PROXY_TARGET` environment variable to frontend and admin services
   - Added `ALLOWED_HOSTS` environment variable to backend service

4. **`docker/nginx/dev.conf`**
   - Removed `proxy_set_header Host $host;` from common settings
   - Added `proxy_set_header Host backend;` to API location block

### Django Files

5. **`sauti_cms/cms/settings.py`**
   - Updated `ALLOWED_HOSTS` default to include Docker service names

6. **`sauti_cms/sitesettings/views.py`**
   - Added try/except error handling to `GlobalSettingsView.get()`

7. **`sauti_cms/reports/views.py`**
   - Added try/except error handling to `NormalizedCallStatsView.get()`

---

## Advantages and Disadvantages

### Approach: Proxying Through Nginx

#### Advantages ✅

1. **Centralized Request Handling**
   - All API requests go through a single point (nginx)
   - Easier to add middleware, logging, rate limiting
   - Consistent request routing

2. **Separation of Concerns**
   - Frontend containers don't need to know backend details
   - Backend doesn't need to handle CORS for multiple origins
   - Nginx handles all proxy logic

3. **Production-Ready**
   - Same architecture as production setup
   - Easier to transition from dev to prod
   - Nginx is battle-tested for reverse proxying

4. **Simplified Configuration**
   - Frontend configs are simpler (just point to nginx)
   - No need for complex Host header manipulation
   - Environment variables make it configurable

5. **Better Security**
   - Backend not directly exposed to frontend containers
   - Nginx can add security headers
   - Easier to implement rate limiting and DDoS protection

#### Disadvantages ❌

1. **Additional Service Dependency**
   - Requires nginx container to be running
   - Adds another point of failure
   - Slightly more complex architecture

2. **Slight Performance Overhead**
   - Extra hop through nginx
   - Minimal in practice, but technically slower than direct connection

3. **Configuration Complexity**
   - Need to maintain nginx config
   - Must understand nginx proxy settings
   - More moving parts to debug

### Alternative Approach: Direct Backend Connection

#### Advantages ✅

1. **Simpler Architecture**
   - Fewer services to manage
   - Direct connection, no intermediate proxy
   - Easier to understand for beginners

2. **Lower Latency**
   - One less network hop
   - Slightly faster response times

3. **Fewer Dependencies**
   - Don't need nginx for dev environment
   - Less to configure and maintain

#### Disadvantages ❌

1. **Host Header Issues**
   - Must manually set Host headers in Vite proxy
   - More complex proxy configuration
   - Harder to debug Host header problems

2. **CORS Complexity**
   - Backend must handle CORS for multiple origins
   - More complex CORS configuration
   - Potential security issues if misconfigured

3. **Inconsistent with Production**
   - Dev and prod architectures differ
   - Harder to catch production issues early
   - More surprises during deployment

4. **Less Flexible**
   - Harder to add middleware
   - Can't easily add request logging/rate limiting
   - Less control over request routing

### Why We Chose Nginx Approach

**Decision Rationale:**
- **Consistency:** Matches production architecture
- **Maintainability:** Centralized configuration is easier to maintain
- **Scalability:** Easy to add more services behind nginx
- **Security:** Better security posture with nginx handling requests
- **Debugging:** Easier to debug with centralized logging

---

## Lessons Learned

### 1. Docker Networking Considerations

**Lesson:** In Docker Compose, services communicate via service names, not `localhost` or `127.0.0.1`.

**Best Practice:**
- Always use Docker service names for inter-container communication
- Use environment variables to make proxy targets configurable
- Test both local and Docker environments

### 2. Django ALLOWED_HOSTS in Docker

**Lesson:** Environment variables can override settings.py defaults, and `.env` files can cause unexpected behavior.

**Best Practice:**
- Set `ALLOWED_HOSTS` explicitly in docker-compose environment
- Include all possible Host headers (service names, localhost, etc.)
- Document which hosts are needed and why

### 3. Nginx Proxy Headers

**Lesson:** Proxy headers must be carefully configured to avoid Host header issues.

**Best Practice:**
- Set Host header explicitly in nginx location blocks
- Use RFC-compliant hostnames (no underscores in service names)
- Test Host header validation in Django

### 4. Error Handling

**Lesson:** Proper error handling in Django views provides better debugging information.

**Best Practice:**
- Always wrap view logic in try/except blocks
- Log errors with full context
- Return proper HTTP error responses

### 5. Development vs Production Parity

**Lesson:** Keeping dev and prod architectures similar prevents deployment surprises.

**Best Practice:**
- Use same proxy setup in dev and prod
- Test in environments that mirror production
- Document architectural decisions

---

## Testing Checklist

After implementing fixes, verify:

- [x] Public frontend can fetch `/api/sitesettings/`
- [x] Public frontend can fetch `/api/v1/calls/stats/keypair/`
- [x] Admin frontend can login via `/api/auth/login/`
- [x] All API endpoints return 200 status codes
- [x] No DisallowedHost errors in backend logs
- [x] Images and static assets load correctly
- [x] CORS headers are properly set

---

## Future Improvements

### Potential Enhancements

1. **Health Checks**
   - Add health check endpoints
   - Monitor service availability
   - Automatic restart on failure

2. **Request Logging**
   - Add structured logging in nginx
   - Log all API requests for debugging
   - Track request/response times

3. **Rate Limiting**
   - Implement rate limiting in nginx
   - Protect backend from abuse
   - Configurable per endpoint

4. **SSL/TLS in Dev**
   - Add self-signed certificates for HTTPS
   - Test HTTPS in development
   - Match production security

5. **Service Discovery**
   - Use Docker Compose service discovery
   - Dynamic service registration
   - Better container orchestration

---

## Conclusion

The debugging process revealed several interconnected issues:
1. Docker networking configuration
2. Django security settings
3. Nginx proxy configuration
4. Error handling in views

By addressing each issue systematically and choosing the nginx proxy approach, we achieved:
- ✅ Working API connections
- ✅ Consistent architecture
- ✅ Better error handling
- ✅ Production-ready setup

The solution balances simplicity, maintainability, and production-readiness, making it a solid choice for the project's needs.

---

**Document Version:** 1.0  
**Last Updated:** January 13, 2026  
**Author:** AI Assistant (Claude)
