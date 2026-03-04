# Sauti CMS Documentation

Complete documentation for the Sauti 116 helpline CMS platform.

---

## 🚀 Getting Started

### For First-Time Users
**Start here**: [`FIRST_TIME_SETUP.md`](./FIRST_TIME_SETUP.md)
- Docker setup instructions
- Default credentials
- Troubleshooting common issues

### For Developers
**Start here**: [`CLAUDE.md`](./CLAUDE.md)
- Project architecture overview
- Development commands  
- Code patterns and conventions

---

## 📚 Active Documentation

### Setup & Deployment
- [`FIRST_TIME_SETUP.md`](./FIRST_TIME_SETUP.md) - ⭐ **Start here for fresh clone**
- [`DOCKER_DEPLOYMENT.md`](./DOCKER_DEPLOYMENT.md) - Production deployment
- [`CLAUDE.md`](./CLAUDE.md) - Developer guide

### Recent Fixes
- [`DOCKER_MEDIA_FILES_FIX.md`](./DOCKER_MEDIA_FILES_FIX.md) - Images not displaying fix
- [`BLOG_POSTS_STATS_FIX.md`](./BLOG_POSTS_STATS_FIX.md) - Stats display fix
- [`ADMIN_UI_USER_FORM_FIX.md`](./ADMIN_UI_USER_FORM_FIX.md) - User form validation
- [`DJANGO_ADMIN_SETUP.md`](./DJANGO_ADMIN_SETUP.md) - Django admin configuration

### API & Backend
- [`CATEGORY_MANAGEMENT_ENDPOINTS.md`](./CATEGORY_MANAGEMENT_ENDPOINTS.md) - Category API
- [`TEST_RESULTS.md`](./TEST_RESULTS.md) - QA test results

---

## 🔑 Default Credentials

**Username**: `admin`  
**Password**: `admin123`

⚠️ Change these in production!

---

## 🐳 Docker Commands

```bash
# Start
docker compose --env-file .env.docker -f docker-compose-full.yml up -d

# Stop
docker compose --env-file .env.docker -f docker-compose-full.yml down

# Logs
docker compose --env-file .env.docker -f docker-compose-full.yml logs -f backend
```

---

## 🌐 Service URLs

- Admin Dashboard: http://localhost:3001
- Public Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api
- Django Admin: http://localhost:8000/admin

---

**Last Updated**: October 29, 2025
