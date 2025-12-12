# First Time Setup Guide

## Quick Start (For Fresh Clone)

### 1. Prerequisites
- Docker and Docker Compose installed
- Git (to clone the repository)

### 2. Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd cms_website_template

# Copy environment file
cp .env.example .env.docker  # If .env.docker doesn't exist

# Start all services
docker compose --env-file .env.docker -f docker-compose-full.yml up -d --build
```

### 3. Wait for Services to Start

The first run will:
1. Build Docker images (takes 2-5 minutes)
2. Create database schema (migrations)
3. **Automatically create admin user** with credentials:
   - **Username**: `admin`
   - **Password**: `admin123`
   - **Email**: `admin@sauti.org`

**Wait 1-2 minutes** after containers start for the backend to complete initialization.

### 4. Verify Setup

```bash
# Check all containers are running
docker compose --env-file .env.docker -f docker-compose-full.yml ps

# You should see:
# - sauti_postgres (healthy)
# - sauti_backend (healthy)
# - sauti_frontend (healthy)
# - sauti_admin (healthy)
```

### 5. Check Backend Logs

If login fails, check if admin user was created:

```bash
docker compose --env-file .env.docker -f docker-compose-full.yml logs backend | grep -A 5 "Admin user"
```

You should see:
```
✅ Admin user created successfully!
Username: admin
Password: admin123
Email: admin@sauti.org
Role: ADMIN
```

### 6. Access the Application

- **Admin Dashboard**: http://localhost:3001
- **Public Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000/api
- **Django Admin**: http://localhost:8000/admin

**Default Admin Credentials**:
- Username: `admin`
- Password: `admin123`

---

## Troubleshooting

### Problem: "Invalid credentials" when logging in

**Solution 1: Check if admin user was created**
```bash
# View backend logs
docker compose --env-file .env.docker -f docker-compose-full.yml logs backend | tail -50

# Look for "Admin user created" message
```

**Solution 2: Manually create admin user**
```bash
# Access backend container
docker compose --env-file .env.docker -f docker-compose-full.yml exec backend bash

# Inside container, run:
python create_admin.py

# Exit container
exit
```

**Solution 3: Create admin via Django shell**
```bash
# Access backend container
docker compose --env-file .env.docker -f docker-compose-full.yml exec backend python manage.py shell

# In Django shell:
from django.contrib.auth import get_user_model
User = get_user_model()

# Create admin user
admin = User.objects.create_superuser(
    username='admin',
    email='admin@sauti.org',
    password='admin123'
)
admin.role = 'ADMIN'
admin.save()
print("Admin created!")

# Exit shell (Ctrl+D or type: exit())
```

### Problem: Containers not starting

**Check Docker volumes (might have old data)**:
```bash
# Stop containers
docker compose --env-file .env.docker -f docker-compose-full.yml down

# Remove volumes to start fresh (WARNING: deletes all data!)
docker compose --env-file .env.docker -f docker-compose-full.yml down -v

# Start again
docker compose --env-file .env.docker -f docker-compose-full.yml up -d --build
```

### Problem: Backend container keeps restarting

**Check environment variables**:
```bash
# Make sure .env.docker exists and has required values
cat .env.docker

# Required variables:
# - SECRET_KEY
# - ENCRYPTION_KEY
# - DB_NAME, DB_USER, DB_PASSWORD
```

**View detailed error logs**:
```bash
docker compose --env-file .env.docker -f docker-compose-full.yml logs backend --follow
```

### Problem: Port already in use

If you see "port is already allocated":
```bash
# Check what's using the port
sudo lsof -i :8000  # Backend
sudo lsof -i :3000  # Frontend
sudo lsof -i :3001  # Admin
sudo lsof -i :5432  # PostgreSQL

# Stop the conflicting service or change ports in docker-compose-full.yml
```

---

## Verifying Admin User Exists

### Option 1: Via API
```bash
# Login via API
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'

# Success response will include:
# - "access": "eyJ..." (JWT token)
# - "user": {"username": "admin", "role": "ADMIN", ...}
```

### Option 2: Via Django Admin
1. Go to http://localhost:8000/admin/
2. Login with `admin` / `admin123`
3. Navigate to Users section
4. You should see the admin user listed

### Option 3: Via Database
```bash
# Access PostgreSQL
docker compose --env-file .env.docker -f docker-compose-full.yml exec db psql -U postgres -d sauti_cms

# Check users
SELECT username, email, role, is_superuser FROM users_user;

# Exit PostgreSQL
\q
```

---

## What Gets Created Automatically

When you first start the containers:

1. ✅ **Database Schema**: All tables created via migrations
2. ✅ **Admin User**:
   - Username: `admin`
   - Password: `admin123`
   - Role: `ADMIN`
   - Superuser: Yes
3. ✅ **Static Files**: Collected to `/app/staticfiles`
4. ✅ **Docker Volumes**:
   - `sauti_postgres_data` (database)
   - `sauti_media_files` (uploaded files)
   - `sauti_static_files` (CSS/JS)

---

## Recommended Next Steps

After successful login:

1. **Change admin password**:
   - Go to Admin Dashboard → Settings → Profile
   - Update password from default `admin123`

2. **Create additional users**:
   - Admin Dashboard → Team Members → Add New User
   - Assign appropriate roles (EDITOR, AUTHOR, VIEWER)

3. **Configure site settings**:
   - Update site name, contact info
   - Set up email configuration (if needed)

4. **Add content**:
   - Create categories for Posts, Videos, FAQs, Resources
   - Start creating content

---

## Quick Reference Commands

```bash
# Start services
docker compose --env-file .env.docker -f docker-compose-full.yml up -d

# Stop services
docker compose --env-file .env.docker -f docker-compose-full.yml down

# View logs
docker compose --env-file .env.docker -f docker-compose-full.yml logs -f

# Restart a service
docker compose --env-file .env.docker -f docker-compose-full.yml restart backend

# Access backend shell
docker compose --env-file .env.docker -f docker-compose-full.yml exec backend bash

# Run Django management command
docker compose --env-file .env.docker -f docker-compose-full.yml exec backend python manage.py <command>

# Rebuild containers (after code changes)
docker compose --env-file .env.docker -f docker-compose-full.yml up -d --build
```

---

## Support

If issues persist:
1. Check logs: `docker compose --env-file .env.docker -f docker-compose-full.yml logs backend`
2. Verify environment variables in `.env.docker`
3. Ensure Docker has enough resources (4GB+ RAM recommended)
4. Try fresh start: `docker compose down -v && docker compose up -d --build`

**Default Credentials (DO NOT USE IN PRODUCTION)**:
- Username: `admin`
- Password: `admin123`
- Change immediately after first login!
