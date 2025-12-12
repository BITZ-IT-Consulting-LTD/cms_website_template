# Sauti CMS Backend - Project Summary

## 📋 Overview

**Project Name:** Sauti 116 helpline CMS Backend  
**Tech Stack:** Django 5.0.6 + Django REST Framework  
**Database:** PostgreSQL  
**Authentication:** JWT (djangorestframework-simplejwt)  
**Status:** ✅ Production Ready

This is a complete, modular, and secure CMS backend for the Sauti 116 helpline website, designed to empower children, GBV survivors, and migrant workers in Uganda with safe reporting channels and comprehensive information access.

---

## 🎯 Project Goals Achieved

### ✅ Core Requirements Implemented

1. **User Management System**
   - Custom User model extending AbstractUser
   - Role-based access control (Admin, Editor, Author, Viewer)
   - JWT authentication with token refresh
   - User registration (Admin only)
   - Profile management

2. **Blog/News System (Posts)**
   - Full CRUD operations
   - Draft → Published workflow
   - Category and tag support
   - Multilingual content (English, Luganda, Swahili)
   - Featured posts
   - View counter
   - Rich text content support
   - Auto-slug generation

3. **Resource Library**
   - File upload support (PDF, DOCX, etc.)
   - Categorization
   - Multilingual support
   - Download counter
   - File metadata (size, type)
   - Thumbnail support

4. **FAQ System**
   - Question/Answer pairs
   - Category organization
   - Multilingual support
   - View counter
   - Custom ordering

5. **Partner Management**
   - Partner organization profiles
   - Logo uploads
   - Contact information
   - Website links
   - Partner types

6. **Anonymous Reporting System** ⭐
   - **Secure case reporting** (Child Protection, GBV, Migrants, PSEA)
   - **Anonymous submission** (no authentication required)
   - **Encrypted storage** using Fernet
   - Auto-generated reference numbers
   - Status tracking workflow
   - File attachment support
   - Follow-up system
   - Admin/Editor access only

---

## 🏗️ Project Structure

```
sauti_cms/
├── cms/                        # Main project configuration
│   ├── __init__.py
│   ├── settings.py            # Production-ready settings
│   ├── urls.py                # Main URL routing
│   ├── wsgi.py                # WSGI entry point
│   └── asgi.py                # ASGI entry point
│
├── users/                      # User management app
│   ├── models.py              # Custom User model with roles
│   ├── serializers.py         # User, registration, profile serializers
│   ├── views.py               # Login, register, profile views
│   ├── admin.py               # User admin customization
│   ├── urls.py                # Auth endpoints
│   └── migrations/
│
├── posts/                      # Blog/News system
│   ├── models.py              # Post, Category, Tag models
│   ├── serializers.py         # Post serializers (list, detail, create)
│   ├── views.py               # Post CRUD views with permissions
│   ├── admin.py               # Post admin with filters
│   ├── urls.py                # Post endpoints
│   └── migrations/
│
├── resources/                  # Resource library
│   ├── models.py              # Resource, ResourceCategory models
│   ├── serializers.py         # Resource serializers
│   ├── views.py               # Resource CRUD views
│   ├── admin.py               # Resource admin
│   ├── urls.py                # Resource endpoints
│   └── migrations/
│
├── faqs/                       # FAQ system
│   ├── models.py              # FAQ, FAQCategory models
│   ├── serializers.py         # FAQ serializers
│   ├── views.py               # FAQ views
│   ├── admin.py               # FAQ admin
│   ├── urls.py                # FAQ endpoints
│   └── migrations/
│
├── partners/                   # Partner management
│   ├── models.py              # Partner model
│   ├── serializers.py         # Partner serializers
│   ├── views.py               # Partner views
│   ├── admin.py               # Partner admin
│   ├── urls.py                # Partner endpoints
│   └── migrations/
│
├── reports/                    # Anonymous reporting system
│   ├── models.py              # Report, ReportFollowUp models
│   ├── serializers.py         # Report serializers with encryption
│   ├── views.py               # Report submission and management
│   ├── admin.py               # Report admin (color-coded statuses)
│   ├── urls.py                # Report endpoints
│   └── migrations/
│
├── media/                      # User-uploaded files
│   ├── posts/images/
│   ├── resources/files/
│   ├── partners/logos/
│   └── reports/attachments/
│
├── staticfiles/                # Collected static files
│
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variables template
├── Dockerfile                  # Docker container configuration
├── docker-compose.yml          # Docker Compose setup
├── manage.py                   # Django management script
├── setup.sh                    # Quick setup script
├── verify_setup.sh             # System verification script
├── README.md                   # Comprehensive documentation
├── DEPLOYMENT.md               # Production deployment guide
└── API_DOCUMENTATION.md        # API endpoint documentation
```

---

## 🔐 Security Features Implemented

### 1. **Report Encryption**
- Sensitive report descriptions encrypted using Fernet (symmetric encryption)
- Automatic encryption on save
- Decryption method for authorized users only
- Configurable encryption key via environment variable

### 2. **Role-Based Access Control (RBAC)**
- **Admin**: Full CRUD, user management, report access
- **Editor**: Create/edit/publish, report access, no delete
- **Author**: Create drafts only, no publish/delete
- **Viewer**: Read-only access

### 3. **Production Security Settings**
When `DEBUG=False`:
- SSL redirect enabled
- Secure cookies (HTTPS only)
- HSTS headers (HTTP Strict Transport Security)
- XSS protection
- Content-type sniffing protection
- CSRF protection
- Frame-deny (clickjacking protection)

### 4. **Anonymous Reporting**
- No authentication required for submission
- Optional contact information
- IP address and user agent logging (for forensics)
- Reference number generation for tracking

### 5. **JWT Authentication**
- Short-lived access tokens (60 min default)
- Long-lived refresh tokens (24 hrs default)
- Token rotation on refresh
- Blacklist after rotation

---

## 📡 API Endpoints Summary

### Authentication (`/api/auth/`)
```
POST   /api/auth/login/           - JWT login
POST   /api/auth/token/refresh/   - Refresh token
POST   /api/auth/register/        - Register user (Admin only)
GET    /api/auth/profile/         - Get profile
PUT    /api/auth/profile/         - Update profile
```

### Posts (`/api/posts/`)
```
GET    /api/posts/                - List posts
POST   /api/posts/                - Create post (Editor+)
GET    /api/posts/<slug>/         - Get post detail
PUT    /api/posts/<slug>/         - Update post (Editor+)
DELETE /api/posts/<slug>/         - Delete post (Admin only)
GET    /api/posts/categories/     - List categories
GET    /api/posts/tags/           - List tags
```

### Resources (`/api/resources/`)
```
GET    /api/resources/            - List resources
POST   /api/resources/            - Create resource (Editor+)
GET    /api/resources/<slug>/     - Get resource detail
PUT    /api/resources/<slug>/     - Update resource
DELETE /api/resources/<slug>/     - Delete resource (Admin)
GET    /api/resources/categories/ - List categories
```

### FAQs (`/api/faqs/`)
```
GET    /api/faqs/                 - List FAQs
POST   /api/faqs/                 - Create FAQ (Editor+)
GET    /api/faqs/<id>/            - Get FAQ detail
PUT    /api/faqs/<id>/            - Update FAQ
DELETE /api/faqs/<id>/            - Delete FAQ (Admin)
GET    /api/faqs/categories/      - List categories
```

### Partners (`/api/partners/`)
```
GET    /api/partners/             - List partners
POST   /api/partners/             - Create partner (Editor+)
GET    /api/partners/<slug>/      - Get partner detail
PUT    /api/partners/<slug>/      - Update partner
DELETE /api/partners/<slug>/      - Delete partner (Admin)
```

### Reports (`/api/reports/`)
```
POST   /api/reports/              - Submit report (NO AUTH REQUIRED) ⭐
GET    /api/reports/list/         - List reports (Editor+)
GET    /api/reports/<id>/         - Get report detail (Editor+)
PUT    /api/reports/<id>/         - Update report status (Editor+)
POST   /api/reports/<id>/followup/ - Add follow-up (Editor+)
```

**Query Parameters:**
- `?search=keyword` - Search in relevant fields
- `?category=slug` - Filter by category
- `?language=en|lg|sw` - Filter by language
- `?featured=true` - Only featured items
- `?status=PENDING` - Filter by status (reports)
- `?ordering=-created_at` - Custom ordering

---

## 🌍 Multilingual Support

### Supported Languages
- **English** (`en`) - Default
- **Luganda** (`lg`) - Primary local language
- **Swahili** (`sw`) - Regional language

### Implementation
- Language field in all content models
- Filter content by `?language=en` parameter
- Easy to expand to additional languages (Acholi, Runyankore, Arabic, Somali)

---

## 🎨 Admin Panel Features

Access at: `http://localhost:8000/admin/`

### Customizations
- **Posts**: List display with status, author, category, views
- **Reports**: Color-coded status badges (Pending=yellow, In Progress=blue, Resolved=green)
- **Resources**: File type icons, download counter
- **Users**: Role badges, last login info
- **All Models**: Search, filters, bulk actions
- **Inline Editing**: Follow-ups inline with reports

---

## 📦 Dependencies Installed

### Core Framework
- Django 5.0.6
- djangorestframework 3.15.1
- psycopg2-binary 2.9.9 (PostgreSQL driver)

### Authentication & Security
- djangorestframework-simplejwt 5.3.1 (JWT)
- cryptography 42.0.7 (Encryption)
- django-ratelimit 4.1.0 (Rate limiting)

### Features
- django-cors-headers 4.3.1 (CORS)
- Pillow 10.3.0 (Image processing)
- django-modeltranslation 0.18.12 (i18n)
- django-ckeditor 6.7.1 (Rich text)

### API Documentation
- drf-spectacular 0.27.2 (OpenAPI/Swagger)

### Admin Enhancements
- django-grappelli 3.0.8 (Admin UI)

### Deployment
- gunicorn 22.0.0 (WSGI server)
- whitenoise 6.6.0 (Static files)

### Development
- pytest 8.2.1
- pytest-django 4.8.0
- factory-boy 3.3.0 (Test factories)
- flake8 7.0.0 (Linting)
- black 24.4.2 (Code formatting)

---

## 🚀 Quick Start Guide

### Option 1: Automated Setup (Recommended)

```bash
cd sauti_cms

# Run setup script
chmod +x setup.sh
./setup.sh

# Activate virtual environment
source venv/bin/activate

# Start development server
python manage.py runserver
```

### Option 2: Manual Setup

```bash
cd sauti_cms

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with your settings

# Create database
createdb sauti_cms

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

### Verification

```bash
# Run verification script
chmod +x verify_setup.sh
./verify_setup.sh
```

---

## 🐳 Docker Deployment

### Quick Start
```bash
# Build and run
docker-compose up --build

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Access at http://localhost:8000
```

### Docker Configuration
- **Web Service**: Django + Gunicorn
- **DB Service**: PostgreSQL 16
- **Volumes**: Database persistence, media files
- **Networks**: Isolated backend network

---

## 📊 Database Schema Summary

### User Model
```python
- username, email, password (from AbstractUser)
- role: ADMIN | EDITOR | AUTHOR | VIEWER
- phone_number
- organization
- created_at, updated_at
```

### Post Model
```python
- title, slug, content, excerpt
- author (FK to User)
- category (FK to Category)
- tags (M2M to Tag)
- featured_image
- status: DRAFT | PUBLISHED
- language: en | lg | sw
- views_count
- is_featured
- published_at, created_at, updated_at
```

### Report Model ⭐
```python
- reference_number (auto-generated)
- category: CHILD_PROTECTION | GBV | MIGRANT | PSEA
- description (encrypted)
- is_anonymous
- contact_name, contact_phone, contact_email (optional)
- location
- attachment (file)
- status: PENDING | IN_PROGRESS | RESOLVED | CLOSED
- assigned_to (FK to User)
- notes (internal)
- ip_address, user_agent
- created_at, updated_at, resolved_at
```

---

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run tests with coverage
coverage run --source='.' manage.py test
coverage report

# Run specific app tests
python manage.py test users
python manage.py test reports
```

---

## 📈 Performance Optimizations

### Implemented
1. **Database Indexing**
   - Indexes on frequently queried fields
   - Composite indexes for common filters
   - Optimal query structure

2. **Query Optimization**
   - `select_related()` for foreign keys
   - `prefetch_related()` for M2M relationships
   - Pagination on all list views

3. **Static File Handling**
   - WhiteNoise for static file serving
   - Media file organization by date
   - Configurable for S3/MinIO

4. **Security Headers**
   - HSTS, XSS protection
   - Content-type sniffing protection
   - Frame-deny for clickjacking

---

## 🔧 Configuration Management

### Environment Variables (.env)
```env
DEBUG=True|False
SECRET_KEY=<django-secret-key>
ALLOWED_HOSTS=localhost,yourdomain.com
DB_NAME=sauti_cms
DB_USER=postgres
DB_PASSWORD=<password>
JWT_ACCESS_TOKEN_LIFETIME=60
CORS_ALLOWED_ORIGINS=http://localhost:3000
ENCRYPTION_KEY=<fernet-key>
EMAIL_HOST_USER=<email>
EMAIL_HOST_PASSWORD=<password>
```

### Generate Secure Keys
```bash
# Django SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Fernet ENCRYPTION_KEY
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

---

## 📝 API Documentation

### Auto-Generated Docs
- **Swagger UI**: `http://localhost:8000/api/docs/`
- **ReDoc**: `http://localhost:8000/api/redoc/`
- **OpenAPI Schema**: `http://localhost:8000/api/schema/`

### Features
- Interactive API testing
- Request/response examples
- Authentication flows
- Model schemas

---

## 🎯 Next Steps & Future Enhancements

### Recommended Additions
1. **Real-time Notifications**
   - WebSocket integration for report updates
   - Email notifications for status changes

2. **Analytics Dashboard**
   - Report statistics
   - Content performance metrics
   - User activity tracking

3. **Advanced Search**
   - Elasticsearch integration
   - Full-text search optimization

4. **File Storage**
   - AWS S3 or MinIO integration
   - CDN for static files

5. **API Rate Limiting**
   - Throttling per user/IP
   - DDoS protection

6. **Audit Logging**
   - Track all admin actions
   - Report viewing logs

---

## 🆘 Support & Maintenance

### Logs
- **Application**: `/var/log/sauti/`
- **Nginx**: `/var/log/nginx/`
- **Docker**: `docker-compose logs -f`

### Health Checks
```bash
# API health
curl http://localhost:8000/api/docs/

# Database
python manage.py dbshell

# Service status (production)
sudo systemctl status sauti-cms
```

### Common Issues
See `DEPLOYMENT.md` - Troubleshooting section

---

## 📄 License & Credits

**Copyright:** Ministry of Gender, Labour and Social Development (MGLSD), Uganda  
**Built by:** Sales Push Limited / Bitz ITC  
**License:** Proprietary

---

## ✅ Deliverables Checklist

- [x] Django 5.x project setup
- [x] 6 Django apps (users, posts, resources, faqs, partners, reports)
- [x] Custom User model with roles
- [x] JWT authentication
- [x] Role-based permissions
- [x] Anonymous reporting with encryption
- [x] Multilingual support (3 languages)
- [x] Django Admin customization
- [x] DRF API with Swagger docs
- [x] PostgreSQL integration
- [x] CORS configuration
- [x] Docker setup
- [x] Production-ready settings
- [x] Comprehensive documentation
- [x] Deployment guide
- [x] Setup scripts

---

## 🎉 Conclusion

This Sauti CMS backend is **production-ready** and includes:
- ✅ All requested features
- ✅ Security best practices
- ✅ Comprehensive documentation
- ✅ Docker deployment option
- ✅ Admin panel customization
- ✅ API documentation
- ✅ Role-based access control
- ✅ Anonymous reporting system
- ✅ Encryption for sensitive data
- ✅ Multilingual support

**Status: Ready for deployment and integration with Vue 3 frontend**

---

**Contact:** support@sauti.mglsd.go.ug
