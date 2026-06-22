# Nginx Reverse Proxy Configuration

This folder contains Nginx configuration files for routing requests to backend and frontend services in both development and production environments.

## Overview

Nginx acts as the central reverse proxy for the Sauti 116 CMS platform, handling:
- Request routing to appropriate services
- SSL/TLS termination (production)
- Static file serving
- HTTP header management
- CORS and security headers

## Folder Structure

### Root Level
- `dev.conf` - Development environment configuration
- `prod.conf` - Production environment configuration
- `template.conf` - Configuration template

### `/host`
Production hosting-specific configurations

### `/host/sauticms`
Sauti CMS-specific Nginx includes and routing rules:
- `cms_logic.inc` - CMS routing rules and endpoints
- `helpline_logic.inc` - Helpline-specific routing logic
- `sauti_main.conf` - Main Sauti platform configuration

## Configuration Files Explained

### `dev.conf` - Development Configuration

**Purpose:** Local development environment routing

**Key Features:**
- Simple HTTP-based routing (no HTTPS)
- Verbose error logging
- Static file caching disabled (for development)
- CORS headers for development

**Routes Configured:**
```
/api/*          → Django backend (http://sauti_cms:8000)
/admin/*        → Admin dashboard (http://sauti-admin:3001)
/static/*       → Django static files
/media/*        → Django media files
/                → Frontend (http://sauti-frontend:3000)
```

### `prod.conf` - Production Configuration

**Purpose:** Production environment with security hardening

**Key Features:**
- HTTPS/SSL enforcement
- Security headers (HSTS, X-Content-Type-Options, etc.)
- Gzip compression enabled
- Request rate limiting
- Security practices:
  - Server signature hidden
  - Version information masked
  - Strict Content Security Policy

**Routes Configured:**
- Same as development but with production settings
- SSL certificate paths configured
- Production domain names

### `template.conf` - Template Configuration

**Purpose:** Base template for custom configurations

**Used for:**
- Creating environment-specific configurations
- Documentation of available directives

## Host-Specific Configurations

### `/host/sauticms/cms_logic.inc`
CMS-specific routing and logic:
- Content management endpoints
- Admin panel routing
- API endpoint prefixes
- Database access control

### `/host/sauticms/helpline_logic.inc`
Helpline platform features:
- Voice capture routes
- Chat interface endpoints
- Contact management APIs
- Emergency protocols

### `/host/sauticms/sauti_main.conf`
Main platform configuration combining all logic.

## Key Nginx Directives

### Upstream Services
Defines backend service addresses:
```nginx
upstream sauti_cms {
    server sauti_cms:8000;
}

upstream sauti_frontend {
    server sauti-frontend:3000;
}

upstream sauti_admin {
    server sauti-admin:3001;
}
```

### Server Block
Main server configuration for request handling.

### Location Blocks
Path-specific routing rules:
```nginx
location /api/ {
    proxy_pass http://sauti_cms;
    # Additional proxy headers
}

location /admin {
    proxy_pass http://sauti-admin;
}

location / {
    proxy_pass http://sauti-frontend;
}
```

### Proxy Headers
Critical headers for proxying requests:
- `X-Real-IP` - Client's actual IP
- `X-Forwarded-For` - IP chain
- `X-Forwarded-Proto` - Original protocol (http/https)
- `X-Forwarded-Host` - Original host header
- `X-Forwarded-Port` - Original port

## Development vs Production

### Development (`dev.conf`)
```
Optimized for:
- Rapid development iteration
- Easy debugging
- Hot reload support
- Verbose logging
```

### Production (`prod.conf`)
```
Optimized for:
- Security hardening
- Performance
- SSL/TLS encryption
- Minimal logging (reduced I/O)
```

## SSL/TLS Configuration (Production)

Production configuration includes:
- SSL certificate and key paths
- SSL protocols version configuration
- Cipher suite specification
- HSTS header for HTTPS enforcement
- Certificate auto-renewal support

## Static and Media Files

### Static Files
- Path: `/static/`
- Source: Django-collected static files
- Caching: Long-term caching (production), no-cache (development)
- Served directly by Nginx (not proxied to Django)

### Media Files
- Path: `/media/`
- Source: User-uploaded files
- Caching: Dynamic caching based on file type
- Access control: User authentication required (for sensitive files)

## Compression

Gzip compression configured for:
- HTML
- CSS
- JavaScript
- JSON responses
- SVG files

Disabled for:
- Images (already compressed)
- Compressed files

## Security Headers (Production)

```
Strict-Transport-Security: Enforces HTTPS
X-Content-Type-Options: Prevents MIME type sniffing
X-Frame-Options: Clickjacking protection
Content-Security-Policy: Restricts resource loading
X-XSS-Protection: XSS attack prevention
```

## Logging

### Access Logs
- Development: Verbose with request details
- Production: Standard format with essential info only

### Error Logs
- Development: Debug level (full details)
- Production: Warn level (errors and warnings only)

## Testing Configuration

### Validate Configuration
```bash
docker-compose exec nginx-dev nginx -t
```

### View Logs
```bash
docker-compose logs nginx-dev
```

### Check Active Connections
```bash
docker-compose exec nginx-dev netstat -an | grep ESTABLISHED
```

## Common Issues and Solutions

### 502 Bad Gateway
**Problem:** Upstream service unavailable
**Solution:**
1. Check if backend services are running: `docker-compose ps`
2. Check service connectivity: `docker-compose exec nginx-dev ping sauti_cms`
3. View Nginx error logs: `docker-compose logs nginx-dev`

### Static Files Not Loading
**Problem:** 404 for /static/ paths
**Solution:**
1. Ensure Django static files collected: `docker-compose exec sauti_cms python manage.py collectstatic --noinput`
2. Check file permissions on mounted volume
3. Verify path in Nginx config matches Django settings

### CORS Errors
**Problem:** Frontend can't access API
**Solution:**
1. Check CORS headers in Nginx config
2. Verify ALLOWED_HOSTS in Django settings
3. Check browser console for specific CORS error details

### SSL Certificate Errors (Production)
**Problem:** HTTPS connection failures
**Solution:**
1. Verify certificate files exist
2. Check certificate expiration: `openssl x509 -in cert.pem -text -noout`
3. Check certificate permissions

## Performance Optimization

### Connection Timeouts
```nginx
# Connection establishment timeout
proxy_connect_timeout 60s;

# Read timeout (waiting for response)
proxy_read_timeout 60s;

# Write timeout (sending request)
proxy_send_timeout 60s;
```

### Buffering
```nginx
# Buffer large responses in memory before sending
proxy_buffering on;
proxy_buffer_size 4k;
proxy_buffers 8 4k;
```

### Keepalive
```nginx
# Reuse backend connections
proxy_http_version 1.1;
proxy_set_header Connection "";
```

## Maintenance

### Reload Configuration Without Downtime
```bash
docker-compose kill -s SIGHUP nginx-dev
# or
docker-compose exec nginx-dev nginx -s reload
```

### Monitor Nginx Performance
```bash
docker stats nginx-dev
```

## Related Documentation

- [Docker Configuration](../README.md)
- [Nginx Local Setup](../../docs/NGINX_LOCAL_SETUP.md)
- [Nginx Infrastructure Changes](../../NGINX_INFRASTRUCTURE_CHANGES.md)
- [Production Deployment Guide](../../PRODUCTION_DEPLOYMENT_GUIDE.md)

## Nginx Resources

- [Official Nginx Documentation](http://nginx.org/en/docs/)
- [Nginx Reverse Proxy Guide](http://nginx.org/en/docs/http/ngx_http_proxy_module.html)
- [Nginx Security Best Practices](https://nginx.org/en/docs/http/configuring_https_servers.html)
