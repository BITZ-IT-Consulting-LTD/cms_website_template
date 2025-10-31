# Sauti Child Helpline CMS

Full-stack Content Management System for Sauti Child Helpline - Ministry of Gender, Labour and Social Development (MGLSD), Uganda.

## 🚀 Quick Start

```bash
# Clone and start
git clone <repository-url>
cd cms_website_template
docker compose --env-file .env.docker -f docker-compose-full.yml up -d --build
```

**Wait 1-2 minutes for services to initialize**, then:
- Admin Dashboard: http://localhost:3001
- Public Website: http://localhost:3000
- Login: `admin` / `admin123`

📖 **Full setup guide**: [`docs/FIRST_TIME_SETUP.md`](./docs/FIRST_TIME_SETUP.md)

---

## 📚 Documentation

All documentation is in the [`docs/`](./docs/) folder:

- **First-Time Setup**: [`docs/FIRST_TIME_SETUP.md`](./docs/FIRST_TIME_SETUP.md) ⭐
- **Developer Guide**: [`docs/CLAUDE.md`](./docs/CLAUDE.md)
- **API Documentation**: [`docs/CATEGORY_MANAGEMENT_ENDPOINTS.md`](./docs/CATEGORY_MANAGEMENT_ENDPOINTS.md)
- **Complete Index**: [`docs/README.md`](./docs/README.md)

---

## 🏗️ Stack

- **Backend**: Django 4.2 + Django REST Framework + PostgreSQL
- **Admin UI**: Vue 3 + Vite + TailwindCSS (Port 3001)
- **Public Frontend**: Vue 3 + Vite + TailwindCSS (Port 3000)
- **Deployment**: Docker + Docker Compose

---

## ✨ Key Features

- 🔐 Anonymous case reporting with encryption
- 📝 Blog posts & news management
- 🎥 Video management (YouTube & uploads)
- 📚 Resource library
- ❓ FAQ management
- 🤝 Partner management
- 👥 Role-based access control (ADMIN, EDITOR, AUTHOR, VIEWER)
- 🌍 Multilingual support (EN, LG, SW)

---

## 🔑 Default Credentials

**Username**: `admin`  
**Password**: `admin123`

⚠️ **Change these immediately after first login!**

---

## 🐳 Docker Commands

```bash
# Start all services
docker compose --env-file .env.docker -f docker-compose-full.yml up -d

# Stop all services
docker compose --env-file .env.docker -f docker-compose-full.yml down

# View logs
docker compose --env-file .env.docker -f docker-compose-full.yml logs -f

# Restart a service
docker compose --env-file .env.docker -f docker-compose-full.yml restart backend
```

---

## 🆘 Troubleshooting

**Login not working?**
```bash
# Check if admin user was created
docker compose --env-file .env.docker -f docker-compose-full.yml logs backend | grep "Admin user"

# Manually create admin
docker compose --env-file .env.docker -f docker-compose-full.yml exec backend python create_admin.py
```

**Images not displaying?**  
See [`docs/DOCKER_MEDIA_FILES_FIX.md`](./docs/DOCKER_MEDIA_FILES_FIX.md)

**More help**: [`docs/FIRST_TIME_SETUP.md`](./docs/FIRST_TIME_SETUP.md)

---

## 📞 Support

- **Hotline**: 116
- **Email**: info@sauti.mglsd.go.ug

---

**Built with ❤️ for Sauti Child Helpline**  
**Ministry of Gender, Labour and Social Development (MGLSD), Uganda**
