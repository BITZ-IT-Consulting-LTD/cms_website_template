# Deployment Guide - Sauti CMS

Complete guide for deploying the Sauti CMS to production.

## Pre-Deployment Checklist

- [ ] PostgreSQL database created
- [ ] Domain name configured
- [ ] SSL certificate obtained
- [ ] Environment variables configured
- [ ] Media/static file storage configured
- [ ] Backup strategy implemented
- [ ] Monitoring tools set up

## Option 1: Docker Deployment (Recommended)

### Step 1: Server Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo apt install docker-compose -y

# Create application directory
sudo mkdir -p /var/www/sauti_cms
cd /var/www/sauti_cms
```

### Step 2: Deploy Application

```bash
# Clone repository or copy files
git clone <repository-url> .

# Create production .env file
cp .env.example .env
nano .env  # Edit with production values

# Build and start containers
docker-compose up -d --build

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Collect static files
docker-compose exec web python manage.py collectstatic --noinput
```

### Step 3: Configure Nginx Reverse Proxy

```bash
# Install Nginx
sudo apt install nginx -y

# Create Nginx config
sudo nano /etc/nginx/sites-available/sauti
```

Add the following configuration:

```nginx
upstream sauti_backend {
    server localhost:8000;
}

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    client_max_body_size 20M;

    location /static/ {
        alias /var/www/sauti_cms/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /media/ {
        alias /var/www/sauti_cms/media/;
        expires 7d;
        add_header Cache-Control "public";
    }

    location / {
        proxy_pass http://sauti_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable site and restart Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/sauti /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Step 4: Configure SSL with Let's Encrypt

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtain SSL certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renewal (already configured by certbot)
sudo systemctl status certbot.timer
```

## Option 2: Traditional Server Deployment

### Step 1: System Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install python3-pip python3-venv nginx postgresql postgresql-contrib -y

# Create application directory
sudo mkdir -p /var/www/sauti_cms
cd /var/www/sauti_cms
```

### Step 2: Database Setup

```bash
# Access PostgreSQL
sudo -u postgres psql

# Create database and user
CREATE DATABASE sauti_cms;
CREATE USER sauti_user WITH PASSWORD 'secure_password';
ALTER ROLE sauti_user SET client_encoding TO 'utf8';
ALTER ROLE sauti_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE sauti_user SET timezone TO 'Africa/Kampala';
GRANT ALL PRIVILEGES ON DATABASE sauti_cms TO sauti_user;
\q
```

### Step 3: Application Setup

```bash
# Clone or copy application files
git clone <repository-url> .

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
nano .env  # Edit with production values

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Set permissions
sudo chown -R www-data:www-data /var/www/sauti_cms
sudo chmod -R 755 /var/www/sauti_cms
```

### Step 4: Configure Gunicorn Service

Create systemd service file:

```bash
sudo nano /etc/systemd/system/sauti-cms.service
```

Add configuration:

```ini
[Unit]
Description=Sauti CMS Gunicorn daemon
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/sauti_cms
Environment="PATH=/var/www/sauti_cms/venv/bin"
ExecStart=/var/www/sauti_cms/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/var/www/sauti_cms/sauti.sock \
          --access-logfile /var/log/sauti/access.log \
          --error-logfile /var/log/sauti/error.log \
          cms.wsgi:application

[Install]
WantedBy=multi-user.target
```

Create log directory and start service:

```bash
sudo mkdir -p /var/log/sauti
sudo chown www-data:www-data /var/log/sauti

sudo systemctl start sauti-cms
sudo systemctl enable sauti-cms
sudo systemctl status sauti-cms
```

### Step 5: Configure Nginx

```bash
sudo nano /etc/nginx/sites-available/sauti
```

Add configuration:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    client_max_body_size 20M;

    location /static/ {
        alias /var/www/sauti_cms/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /media/ {
        alias /var/www/sauti_cms/media/;
        expires 7d;
        add_header Cache-Control "public";
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/sauti_cms/sauti.sock;
    }
}
```

Enable and restart:

```bash
sudo ln -s /etc/nginx/sites-available/sauti /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## Production Environment Variables

Create a production `.env` file:

```env
# Security
DEBUG=False
SECRET_KEY=<generate-strong-key>
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database
DB_NAME=sauti_cms
DB_USER=sauti_user
DB_PASSWORD=<strong-password>
DB_HOST=localhost
DB_PORT=5432

# JWT Settings
JWT_ACCESS_TOKEN_LIFETIME=60
JWT_REFRESH_TOKEN_LIFETIME=1440

# CORS
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# Email (Gmail example)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=notifications@yourdomain.com
EMAIL_HOST_PASSWORD=<app-password>

# Report Encryption
ENCRYPTION_KEY=<generate-with-fernet>
```

Generate secure values:

```bash
# SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# ENCRYPTION_KEY
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

## Database Backup Strategy

### Automated Daily Backups

Create backup script:

```bash
sudo nano /usr/local/bin/backup-sauti-db.sh
```

Add:

```bash
#!/bin/bash
BACKUP_DIR="/var/backups/sauti"
DATE=$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR

# PostgreSQL backup
pg_dump -U sauti_user sauti_cms | gzip > $BACKUP_DIR/sauti_cms_$DATE.sql.gz

# Media files backup
tar -czf $BACKUP_DIR/media_$DATE.tar.gz /var/www/sauti_cms/media/

# Keep only last 30 days
find $BACKUP_DIR -name "*.gz" -mtime +30 -delete

echo "Backup completed: $DATE"
```

Make executable and schedule:

```bash
sudo chmod +x /usr/local/bin/backup-sauti-db.sh

# Add to crontab
sudo crontab -e

# Daily backup at 2 AM
0 2 * * * /usr/local/bin/backup-sauti-db.sh >> /var/log/sauti/backup.log 2>&1
```

## Monitoring & Logging

### Application Logs

```bash
# Gunicorn logs
sudo tail -f /var/log/sauti/error.log
sudo tail -f /var/log/sauti/access.log

# Nginx logs
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/access.log

# Docker logs (if using Docker)
docker-compose logs -f web
```

### Health Check Script

Create monitoring script:

```bash
sudo nano /usr/local/bin/sauti-healthcheck.sh
```

Add:

```bash
#!/bin/bash
URL="https://yourdomain.com/api/docs/"
STATUS=$(curl -s -o /dev/null -w "%{http_code}" $URL)

if [ $STATUS -eq 200 ]; then
    echo "OK: Sauti CMS is running"
    exit 0
else
    echo "ERROR: Sauti CMS returned status $STATUS"
    # Restart service
    sudo systemctl restart sauti-cms
    exit 1
fi
```

Schedule health checks:

```bash
sudo chmod +x /usr/local/bin/sauti-healthcheck.sh

# Check every 5 minutes
*/5 * * * * /usr/local/bin/sauti-healthcheck.sh >> /var/log/sauti/healthcheck.log 2>&1
```

## Updating Application

### Docker Deployment

```bash
cd /var/www/sauti_cms

# Pull latest changes
git pull origin main

# Rebuild containers
docker-compose down
docker-compose up -d --build

# Run migrations
docker-compose exec web python manage.py migrate

# Collect static files
docker-compose exec web python manage.py collectstatic --noinput
```

### Traditional Deployment

```bash
cd /var/www/sauti_cms
source venv/bin/activate

# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Restart service
sudo systemctl restart sauti-cms
```

## Troubleshooting

### Common Issues

**Issue**: Service won't start
```bash
# Check service status
sudo systemctl status sauti-cms

# View logs
sudo journalctl -u sauti-cms -n 50
```

**Issue**: Static files not loading
```bash
# Verify static files collected
python manage.py collectstatic --noinput

# Check Nginx permissions
ls -la /var/www/sauti_cms/staticfiles/
```

**Issue**: Database connection error
```bash
# Test database connection
psql -U sauti_user -d sauti_cms -h localhost

# Check .env settings
cat .env | grep DB_
```

**Issue**: 502 Bad Gateway
```bash
# Check if Gunicorn is running
sudo systemctl status sauti-cms

# Check socket permissions
ls -la /var/www/sauti_cms/sauti.sock
```

## Security Hardening

### Firewall Configuration

```bash
# Install UFW
sudo apt install ufw -y

# Allow SSH, HTTP, HTTPS
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Enable firewall
sudo ufw enable
```

### Fail2Ban Setup

```bash
# Install Fail2Ban
sudo apt install fail2ban -y

# Configure for Nginx
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo nano /etc/fail2ban/jail.local

# Add Nginx protection
[nginx-http-auth]
enabled = true
[nginx-noscript]
enabled = true

sudo systemctl restart fail2ban
```

## Performance Optimization

### Enable Gzip Compression

Add to Nginx config:

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css text/xml text/javascript application/x-javascript application/xml+rss application/json;
```

### Database Optimization

```bash
# PostgreSQL tuning
sudo nano /etc/postgresql/*/main/postgresql.conf

# Adjust based on server resources
shared_buffers = 256MB
effective_cache_size = 1GB
maintenance_work_mem = 64MB
checkpoint_completion_target = 0.9
wal_buffers = 16MB
default_statistics_target = 100
random_page_cost = 1.1
effective_io_concurrency = 200
work_mem = 5242kB
min_wal_size = 1GB
max_wal_size = 4GB

sudo systemctl restart postgresql
```

## Maintenance Tasks

### Weekly Tasks

- [ ] Review error logs
- [ ] Check disk space
- [ ] Verify backups are working
- [ ] Review user activity

### Monthly Tasks

- [ ] Update system packages
- [ ] Review and optimize database
- [ ] Update dependencies
- [ ] Security audit

---

For support: support@sauti.mglsd.go.ug
