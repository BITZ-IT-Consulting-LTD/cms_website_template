# Docker Deployment Guide - Sauti CMS

This guide provides complete instructions for deploying the Sauti 116 helpline CMS using Docker and Docker Compose.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Start](#quick-start)
3. [Configuration](#configuration)
4. [Building and Running](#building-and-running)
5. [Service Management](#service-management)
6. [Database Management](#database-management)
7. [Troubleshooting](#troubleshooting)
8. [Production Deployment](#production-deployment)
9. [Backup and Restore](#backup-and-restore)

---

## Prerequisites

### Required Software

- **Docker**: Version 20.10 or higher
- **Docker Compose**: Version 2.0 or higher

### Installation

**Ubuntu/Debian:**
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo apt-get update
sudo apt-get install docker-compose-plugin

# Add user to docker group
sudo usermod -aG docker $USER
```

**macOS:**
```bash
# Install Docker Desktop
brew install --cask docker
```

**Windows:**
Download and install [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)

### Verify Installation

```bash
docker --version
docker compose version
```

---

## Quick Start

### 1. Clone or Navigate to Project

```bash
cd /path/to/cms_website_template
```

### 2. Create Environment File

```bash
# Copy the example file
cp .env.docker.example .env.docker

# Edit with your values
nano .env.docker
```

### 3. Build and Start Services

```bash
# Build all services
docker compose -f docker-compose-full.yml build

# Start all services
docker compose -f docker-compose-full.yml up -d
```

### 4. Access the Application

- **Public Frontend**: http://localhost:3000 or http://localhost
- **Admin Dashboard**: http://localhost:3001
- **Backend API**: http://localhost:8000
- **Django Admin**: http://localhost:8000/admin

**Default Admin Credentials:**
- Username: `admin`
- Password: `admin123`

---

## Configuration

### Environment Variables

The system uses `.env.docker` file for configuration. Key variables:

#### Django Backend

```bash
DEBUG=False                    # Set to False for production
SECRET_KEY=<random-key>        # 50+ character random string
ALLOWED_HOSTS=localhost,your-domain.com
DB_NAME=sauti_cms
DB_USER=postgres
DB_PASSWORD=<secure-password>
ENCRYPTION_KEY=<32-byte-key>   # For report encryption
```

#### CORS Settings

```bash
CORS_ALLOWED_ORIGINS=http://localhost,https://your-domain.com
```

#### Frontend Settings

```bash
VITE_API_URL=http://localhost:8000
VITE_APP_NAME=Sauti 116 helpline
VITE_HOTLINE=116
VITE_WHATSAPP=+256123456789
VITE_EMAIL=info@sauti.mglsd.go.ug
```

### Generating Secure Keys

**SECRET_KEY:**
```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**ENCRYPTION_KEY:**
```bash
python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

---

## Building and Running

### Build Services

```bash
# Build all services
docker compose -f docker-compose-full.yml build

# Build specific service
docker compose -f docker-compose-full.yml build backend
docker compose -f docker-compose-full.yml build frontend
docker compose -f docker-compose-full.yml build admin
```

### Start Services

```bash
# Start all services in detached mode
docker compose -f docker-compose-full.yml up -d

# Start with logs visible
docker compose -f docker-compose-full.yml up

# Start specific service
docker compose -f docker-compose-full.yml up -d backend
```

### Stop Services

```bash
# Stop all services
docker compose -f docker-compose-full.yml down

# Stop and remove volumes (CAUTION: deletes data!)
docker compose -f docker-compose-full.yml down -v
```

### Restart Services

```bash
# Restart all services
docker compose -f docker-compose-full.yml restart

# Restart specific service
docker compose -f docker-compose-full.yml restart backend
```

---

## Service Management

### View Logs

```bash
# View all logs
docker compose -f docker-compose-full.yml logs

# Follow logs in real-time
docker compose -f docker-compose-full.yml logs -f

# View specific service logs
docker compose -f docker-compose-full.yml logs -f backend
docker compose -f docker-compose-full.yml logs -f frontend
docker compose -f docker-compose-full.yml logs -f admin
docker compose -f docker-compose-full.yml logs -f db
```

### Check Service Status

```bash
# List running services
docker compose -f docker-compose-full.yml ps

# Check health status
docker compose -f docker-compose-full.yml ps --format json | jq
```

### Execute Commands in Containers

```bash
# Access backend shell
docker compose -f docker-compose-full.yml exec backend sh

# Access Django shell
docker compose -f docker-compose-full.yml exec backend python manage.py shell

# Access database
docker compose -f docker-compose-full.yml exec db psql -U postgres -d sauti_cms
```

---

## Database Management

### Run Migrations

```bash
docker compose -f docker-compose-full.yml exec backend python manage.py migrate
```

### Create Superuser

```bash
# Using the script (creates admin/admin123)
docker compose -f docker-compose-full.yml exec backend python create_admin.py

# Or create custom superuser
docker compose -f docker-compose-full.yml exec backend python manage.py createsuperuser
```

### Create Sample Data

```bash
docker compose -f docker-compose-full.yml exec backend python create_sample_posts.py
docker compose -f docker-compose-full.yml exec backend python create_sample_videos.py
```

### Database Backup

```bash
# Backup database
docker compose -f docker-compose-full.yml exec db pg_dump -U postgres sauti_cms > backup_$(date +%Y%m%d_%H%M%S).sql

# Or use docker volume backup
docker run --rm \
  --volumes-from sauti_postgres \
  -v $(pwd):/backup \
  ubuntu tar czf /backup/postgres_backup_$(date +%Y%m%d).tar.gz /var/lib/postgresql/data
```

### Database Restore

```bash
# Restore from SQL dump
docker compose -f docker-compose-full.yml exec -T db psql -U postgres sauti_cms < backup.sql

# Or restore from volume backup
docker run --rm \
  --volumes-from sauti_postgres \
  -v $(pwd):/backup \
  ubuntu tar xzf /backup/postgres_backup.tar.gz -C /
```

---

## Troubleshooting

### Services Won't Start

**Check logs:**
```bash
docker compose -f docker-compose-full.yml logs
```

**Common issues:**
- Port already in use: Stop other services using ports 80, 3000, 3001, 8000, 5432
- Permission denied: Ensure Docker daemon is running and user is in docker group
- Out of disk space: Clean up Docker resources

### Clear Docker Resources

```bash
# Remove stopped containers
docker container prune

# Remove unused images
docker image prune -a

# Remove unused volumes
docker volume prune

# Remove everything (CAUTION!)
docker system prune -a --volumes
```

### Database Connection Issues

```bash
# Check if database is healthy
docker compose -f docker-compose-full.yml ps db

# View database logs
docker compose -f docker-compose-full.yml logs db

# Test database connection
docker compose -f docker-compose-full.yml exec db pg_isready -U postgres
```

### Frontend Not Loading

```bash
# Check if backend is running
curl http://localhost:8000/admin/login/

# Rebuild frontend
docker compose -f docker-compose-full.yml build frontend
docker compose -f docker-compose-full.yml up -d frontend

# Clear browser cache and try again
```

### File Upload Issues

```bash
# Check media volume
docker volume inspect sauti_media_files

# Verify permissions in container
docker compose -f docker-compose-full.yml exec backend ls -la /app/media

# Create directories if missing
docker compose -f docker-compose-full.yml exec backend mkdir -p /app/media/{posts/images,resources/files,partners/logos}
```

---

## Production Deployment

### 1. Server Setup

**Requirements:**
- Ubuntu 20.04 LTS or higher
- Minimum 2GB RAM, 2 CPU cores
- 20GB disk space
- Domain name pointed to server IP

### 2. Install Prerequisites

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo apt-get install docker-compose-plugin

# Install nginx (for reverse proxy)
sudo apt install nginx -y
```

### 3. Configure Environment

```bash
# Copy project to server
scp -r cms_website_template user@your-server:/opt/

# Create production env file
cd /opt/cms_website_template
cp .env.docker.example .env.docker
nano .env.docker  # Edit with production values
```

**Important production settings:**
```bash
DEBUG=False
SECRET_KEY=<generate-new-secure-key>
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
CORS_ALLOWED_ORIGINS=https://your-domain.com,https://www.your-domain.com
DB_PASSWORD=<strong-database-password>
ENCRYPTION_KEY=<generate-new-key>
```

### 4. SSL Certificate (Let's Encrypt)

```bash
# Install certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtain certificate
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

### 5. Configure Nginx Reverse Proxy

Create `/etc/nginx/sites-available/sauti`:

```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com www.your-domain.com;

    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;

    # Frontend
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Admin
    location /admin-dashboard {
        proxy_pass http://localhost:3001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # API
    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        client_max_body_size 20M;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/sauti /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 6. Deploy Application

```bash
# Build and start
docker compose -f docker-compose-full.yml build
docker compose -f docker-compose-full.yml up -d

# Check status
docker compose -f docker-compose-full.yml ps

# View logs
docker compose -f docker-compose-full.yml logs -f
```

### 7. Configure Auto-Start

```bash
# Create systemd service
sudo nano /etc/systemd/system/sauti-cms.service
```

```ini
[Unit]
Description=Sauti CMS Docker Compose
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/opt/cms_website_template
ExecStart=/usr/bin/docker compose -f docker-compose-full.yml up -d
ExecStop=/usr/bin/docker compose -f docker-compose-full.yml down
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
```

Enable service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable sauti-cms.service
sudo systemctl start sauti-cms.service
```

---

## Backup and Restore

### Automated Backups

Create backup script `/opt/cms_website_template/backup.sh`:

```bash
#!/bin/bash
BACKUP_DIR="/opt/backups/sauti"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR

# Backup database
docker compose -f docker-compose-full.yml exec -T db pg_dump -U postgres sauti_cms > "$BACKUP_DIR/db_$DATE.sql"

# Backup media files
docker run --rm \
  --volumes-from sauti_backend \
  -v $BACKUP_DIR:/backup \
  ubuntu tar czf /backup/media_$DATE.tar.gz /app/media

# Keep only last 7 days
find $BACKUP_DIR -mtime +7 -delete

echo "Backup completed: $DATE"
```

Add to crontab:
```bash
sudo chmod +x /opt/cms_website_template/backup.sh
crontab -e
# Add: 0 2 * * * /opt/cms_website_template/backup.sh
```

### Manual Backup

```bash
# Full system backup
./backup.sh

# Database only
docker compose -f docker-compose-full.yml exec db pg_dump -U postgres sauti_cms > backup.sql

# Media files only
docker cp sauti_backend:/app/media ./media_backup
```

### Restore

```bash
# Restore database
docker compose -f docker-compose-full.yml exec -T db psql -U postgres sauti_cms < backup.sql

# Restore media files
docker cp ./media_backup sauti_backend:/app/media
```

---

## Monitoring

### Container Health

```bash
# Check container health
docker compose -f docker-compose-full.yml ps

# Monitor resource usage
docker stats
```

### Logs

```bash
# Export logs
docker compose -f docker-compose-full.yml logs > application.log

# Tail specific service
docker compose -f docker-compose-full.yml logs -f --tail=100 backend
```

### Performance Monitoring

Consider installing:
- **Portainer**: Docker management UI
- **Grafana + Prometheus**: Metrics and monitoring
- **ELK Stack**: Log aggregation

---

## Security Checklist

- [ ] Change all default passwords
- [ ] Use strong SECRET_KEY and ENCRYPTION_KEY
- [ ] Enable HTTPS with valid SSL certificate
- [ ] Set DEBUG=False in production
- [ ] Configure firewall (UFW)
- [ ] Enable automatic security updates
- [ ] Regular backups configured
- [ ] Monitor logs for suspicious activity
- [ ] Keep Docker and system updated
- [ ] Restrict database access to containers only

---

## Support

For issues and questions:
- GitHub Issues: [Create an issue]
- Email: support@sauti.mglsd.go.ug
- Documentation: See CLAUDE.md and README.md

---

## Quick Reference

```bash
# Start everything
docker compose -f docker-compose-full.yml up -d

# Stop everything
docker compose -f docker-compose-full.yml down

# View logs
docker compose -f docker-compose-full.yml logs -f

# Restart a service
docker compose -f docker-compose-full.yml restart backend

# Rebuild and restart
docker compose -f docker-compose-full.yml up -d --build

# Access Django shell
docker compose -f docker-compose-full.yml exec backend python manage.py shell

# Create superuser
docker compose -f docker-compose-full.yml exec backend python create_admin.py

# Backup database
docker compose -f docker-compose-full.yml exec db pg_dump -U postgres sauti_cms > backup.sql
```

---

**Version**: 1.0.0
**Last Updated**: October 28, 2025
**Maintained by**: Sauti Development Team
