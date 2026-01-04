# Production Deployment Instructions - SAUTI 116

This document provides step-by-step instructions for deploying the SAUTI 116 platform to production on the host `sauti.mglsd.go.ug`.

## 1. URL Architecture
The platform is configured to run across two distinct subdirectory routes:
- **Public Website:** `https://sauti.mglsd.go.ug/sauti/`
- **Admin Dashboard:** `https://sauti.mglsd.go.ug/cms-admin/`
- **Backend API:** `https://sauti.mglsd.go.ug/sauti/api/`

## 2. Prerequisites
1. Docker and Docker Compose installed on the production server.
2. Nginx (or another reverse proxy) installed on the host machine to handle SSL/HTTPS.
3. Access to the environment variables for PostgreSQL and Django (found in `.env` files).

## 3. Container Deployment
From the root of the project directory, run the following command to build and start the production stack:

```bash
docker-compose -f docker/docker-compose.prod.yml up -d --build
```

This command:
- Builds the **Frontend** with base path `/sauti/`.
- Builds the **Admin** with base path `/cms-admin/`.
- Starts a **Gunicorn** server for the Django Backend.
- Starts a **PostgreSQL** database.
- Starts an internal **Nginx proxy** on port `8080`.

## 4. Host Nginx Configuration
Update your production server's Nginx configuration (usually in `/etc/nginx/sites-available/`) to route traffic to the containerized stack.

```nginx
server {
    listen 80;
    server_name sauti.mglsd.go.ug;

    # Redirect all HTTP traffic to HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name sauti.mglsd.go.ug;

    # SSL Certificates
    ssl_certificate /path/to/your/fullchain.pem;
    ssl_certificate_key /path/to/your/privkey.pem;

    # Increase upload limit for video content
    client_max_body_size 500M;

    # Route 1: Public Frontend & API
    location /sauti/ {
        proxy_pass http://127.0.0.1:8080/sauti/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Route 2: CMS Admin Application
    location /cms-admin/ {
        proxy_pass http://127.0.0.1:8080/cms-admin/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Route 3: Django Admin (if needed for staff)
    location /sauti/django-admin/ {
        proxy_pass http://127.0.0.1:8080/sauti/django-admin/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Root redirect (Convenience)
    location = / {
        return 301 /sauti/;
    }
}
```

## 5. Post-Deployment Steps
Once the containers are running:
1. **Migrations & Data:** The `entrypoint.sh` script automatically runs migrations and populates initial content.
2. **Superuser:** If an admin user is not created, you can create one manually:
   ```bash
   docker exec -it sauti_backend_prod python manage.py createsuperuser
   ```
3. **Verify Static Assets:** Check that CSS/JS files load correctly at `https://sauti.mglsd.go.ug/sauti/assets/...`.

## 6. Troubleshooting
- **Logs:** View container logs with `docker-compose -f docker/docker-compose.prod.yml logs -f`.
- **Base Path errors:** If you see white screens, ensure the `VITE_BASE_PATH` in `.env.production` files matches the Nginx location blocks exactly.
