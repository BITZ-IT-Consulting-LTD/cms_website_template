# Docker Configuration

This folder contains all Docker and container orchestration configurations for the Sauti 116 CMS platform.

## Overview

The Docker setup enables containerization of the entire application stack including the Django backend, PostgreSQL database, Nginx reverse proxy, and Vue.js frontend and admin applications.

## Folder Structure

### `/nginx`
Nginx reverse proxy configuration for routing requests to different services.

**Key Files:**
- `dev.conf` - Development environment Nginx configuration
- `prod.conf` - Production environment Nginx configuration
- `template.conf` - Template configuration file

**Subdirectories:**
- `host/` - Production hosting configurations
  - `sauticms/` - Sauti CMS-specific Nginx includes:
    - `cms_logic.inc` - CMS routing rules
    - `helpline_logic.inc` - Helpline-specific routing
    - `sauti_main.conf` - Main Sauti configuration

### `/docs`
Docker-specific documentation and root configuration file templates.

**Key Files:**
- Contains documentation about Docker setup and configuration

## Docker Compose Files

Located at project root:

### `docker-compose.dev.yml`
**Purpose:** Development environment configuration
**Services:**
- `sauti_postgres` - PostgreSQL database
- `sauti_cms` - Django backend API
- `sauti-frontend` - Vue.js public website
- `sauti-admin` - Vue.js admin dashboard
- `nginx-dev` - Nginx development reverse proxy

**Usage:**
```bash
docker-compose -f docker-compose.dev.yml up
```

### `docker-compose.prod.yml`
**Purpose:** Production environment configuration
**Services:**
- Same as dev but optimized for production
- Different environment variables and resource limits
- SSL/TLS configuration for production

**Usage:**
```bash
docker-compose -f docker-compose.prod.yml up -d
```

## Key Files in Docker Folder

### Dockerfiles
- `Dockerfile` (in sauti_cms/) - Backend Django application container
- `Dockerfile.dev` & `Dockerfile.prod` (in sauti-admin/) - Admin application containers
- Similar dockerfiles in sauti-frontend/ for frontend application

### Container Entry Points
- `entrypoint.sh` - Backend service initialization script
- Handles database migrations, static file collection, and service startup

### Environment Configuration
- `.env` - Environment variables (create from `.env.example`)
- `.env.example` - Template for environment variables

## Development Workflow

1. **Build Images:**
   ```bash
   docker-compose -f docker-compose.dev.yml build
   ```

2. **Start Services:**
   ```bash
   docker-compose -f docker-compose.dev.yml up
   ```

3. **Access Services:**
   - Frontend: http://localhost:3000
   - Admin: http://localhost:3001
   - API: http://localhost:8000/api
   - Nginx: http://localhost:80

4. **Database Migrations:**
   ```bash
   docker-compose -f docker-compose.dev.yml exec sauti_cms python manage.py migrate
   ```

5. **Populate Initial Content:**
   ```bash
   docker-compose -f docker-compose.dev.yml exec sauti_cms python populate_initial_content.py
   ```

## Production Deployment

For production deployment instructions, see:
- `/docs/DOCKER_DEPLOYMENT.md` - Complete Docker deployment guide
- `/PRODUCTION_DEPLOYMENT_GUIDE.md` - Production-specific guidelines

## Network Configuration

### Port Mappings (Development)
- **80** - Nginx (reverse proxy)
- **3000** - Frontend application
- **3001** - Admin dashboard
- **8000** - Django API
- **5432** - PostgreSQL database

### Environment Variables

Key environment variables configured in docker-compose files:
- `DEBUG` - Django debug mode
- `SECRET_KEY` - Django secret key
- `DATABASE_URL` - PostgreSQL connection string
- `ALLOWED_HOSTS` - Allowed domain names
- `VITE_API_URL` - Frontend API endpoint

See `.env.example` for complete list.

## Troubleshooting

**Port Already in Use:**
```bash
# Change port in docker-compose.yml
# Or stop services using the port
lsof -i :3000
kill -9 <PID>
```

**Database Connection Issues:**
```bash
# Check PostgreSQL is running
docker-compose ps

# View container logs
docker-compose logs sauti_postgres
```

**Frontend Not Loading:**
```bash
# Check Nginx configuration
docker-compose exec nginx-dev nginx -t

# View Nginx logs
docker-compose logs nginx-dev
```

## Nginx Configuration

Nginx acts as the reverse proxy, routing requests to appropriate services:

- `/api/*` → Django backend (port 8000)
- `/admin/*` → Admin dashboard (port 3001)
- `/` → Frontend (port 3000)

For detailed Nginx configuration, see `/docker/nginx/README.md`

## Related Documentation

- [Docker Deployment Guide](../docs/DOCKER_DEPLOYMENT.md)
- [First Time Setup](../docs/FIRST_TIME_SETUP.md)
- [Production Deployment Guide](../PRODUCTION_DEPLOYMENT_GUIDE.md)
- [Nginx Configuration](./nginx/README.md)
