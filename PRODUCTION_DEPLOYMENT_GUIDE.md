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
3. Access to the environment variables for PostgreSQL and Django.
   > **Note:** The `docker-compose.prod.yml` currently uses hardcoded defaults for quick setup. For a secure production environment, create a `.env` file in `sauti_cms/` based on `.env.example` or update the `environment` section in the compose file.

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
The platform uses a modular Nginx configuration to separate the New CMS, Legacy Helpline, and WebSockets. This avoids server-name conflicts and improves maintainability.

### 4.1 Directory Setup
On the production server, create the following directory:
```bash
sudo mkdir -p /etc/nginx/sauticms/
```

### 4.2 Modular Files
The following files should be created in `/etc/nginx/sauticms/` (See **NGINX_INFRASTRUCTURE_CHANGES.md** for full content):

1.  **sauti_main.conf**: Handles domain names, SSL termination, and includes the logic files.
2.  **cms_logic.inc**: Contains the proxy rules for the Dockerized CMS.
3.  **helpline_logic.inc**: Contains the PHP-FPM and proxy rules for the legacy apps.
4.  **extra_ports.conf**: Handles SSL for WebSocket ports 8384/8394.

### 4.3 Clean Main Config
Ensure your `/etc/nginx/nginx.conf` is a clean loader that includes your new module folder:
```nginx
http {
    # ... global settings ...
    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sauticms/*.conf;
}
```

## 5. Post-Deployment Steps
Once the containers are running:
1. **Apply Changes Locally:** Commit and push the updated environment variables.
2. **Rebuild on Server:** 
   ```bash
   git pull
   docker compose -f docker/docker-compose.prod.yml down
   docker compose -f docker/docker-compose.prod.yml up -d --build --force-recreate
   ```
3. **Reload Host Nginx:**
   ```bash
   sudo nginx -t
   sudo systemctl reload nginx
   ```

## 6. Troubleshooting
- **502 Bad Gateway:** Usually means the Docker container (port 8080) is not accessible. Run `docker ps` to ensure the `nginx_prod` container is up.
- **Login Errors:** If you see "cms-api" in browser logs, it means the old JS bundle is cached or was built with old ENV vars. Run Step 5.2 again with `--no-cache`.
- **CORS Errors:** Ensure `CORS_ALLOWED_ORIGINS` in `docker-compose.prod.yml` includes `https://sauti.mglsd.go.ug`.
