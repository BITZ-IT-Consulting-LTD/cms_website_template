# Sauti 116 helpline CMS Backend

A comprehensive Django REST Framework backend for the Sauti 116 helpline website, empowering children, GBV survivors, and migrant workers in Uganda.

## Features

- **User Management**: Role-based access control (Admin, Editor, Author, Viewer)
- **Blog/News System**: Full CMS with draft/publish workflow
- **Resource Library**: Downloadable resources (PDFs, docs) with categorization
- **FAQ Management**: Multilingual FAQ system
- **Partner Management**: Display partner organizations
- **Anonymous Reporting**: Secure case reporting with encryption
- **Multilingual Support**: English, Luganda, Swahili
- **JWT Authentication**: Secure API authentication
- **API Documentation**: Auto-generated OpenAPI/Swagger docs
- **Production Ready**: Docker support, PostgreSQL, Gunicorn

## Quick Start

### Prerequisites

- Python 3.12+
- PostgreSQL 16+
- Docker & Docker Compose (optional)

### Option 1: Local Development

1. **Clone and setup**:
   ```bash
   cd sauti_cms
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Environment Configuration**:
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

3. **Database Setup**:
   ```bash
   createdb sauti_cms  # Create PostgreSQL database
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser**:
   ```bash
   python manage.py createsuperuser
   # Username: admin
   # Role will be set to ADMIN automatically
   ```

5. **Run Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access**:
   - API: http://localhost:8000/api/
   - Admin: http://localhost:8000/admin/
   - Swagger Docs: http://localhost:8000/api/docs/
   - ReDoc: http://localhost:8000/api/redoc/

### Option 2: Docker Deployment

1. **Build and run**:
   ```bash
   docker-compose up --build
   ```

2. **Run migrations**:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

3. **Create superuser**:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

4. **Access**: http://localhost:8000

## API Endpoints

### Authentication
- `POST /api/auth/login/` - JWT login
- `POST /api/auth/token/refresh/` - Refresh JWT token
- `POST /api/auth/register/` - Register user (Admin only)
- `GET /api/auth/profile/` - Get current user profile
- `PUT /api/auth/profile/` - Update profile

### Posts (Blog/News)
- `GET /api/posts/` - List posts (public: published only)
- `POST /api/posts/` - Create post (Editors/Admins)
- `GET /api/posts/<slug>/` - Get post detail
- `PUT /api/posts/<slug>/` - Update post (Editors/Admins)
- `DELETE /api/posts/<slug>/` - Delete post (Admins only)
- `GET /api/posts/categories/` - List categories
- `GET /api/posts/tags/` - List tags

### Resources
- `GET /api/resources/` - List resources
- `POST /api/resources/` - Create resource (Editors/Admins)
- `GET /api/resources/<slug>/` - Get resource detail
- `PUT /api/resources/<slug>/` - Update resource
- `DELETE /api/resources/<slug>/` - Delete resource (Admins)
- `GET /api/resources/categories/` - List categories

### FAQs
- `GET /api/faqs/` - List FAQs
- `POST /api/faqs/` - Create FAQ (Editors/Admins)
- `GET /api/faqs/<id>/` - Get FAQ detail
- `PUT /api/faqs/<id>/` - Update FAQ
- `DELETE /api/faqs/<id>/` - Delete FAQ (Admins)
- `GET /api/faqs/categories/` - List categories

### Partners
- `GET /api/partners/` - List partners
- `POST /api/partners/` - Create partner (Editors/Admins)
- `GET /api/partners/<slug>/` - Get partner detail
- `PUT /api/partners/<slug>/` - Update partner
- `DELETE /api/partners/<slug>/` - Delete partner (Admins)

### Reports (Anonymous Submission)
- `POST /api/reports/` - Submit report (NO AUTH REQUIRED)
- `GET /api/reports/list/` - List reports (Editors/Admins only)
- `GET /api/reports/<id>/` - Get report detail (Editors/Admins)
- `PUT /api/reports/<id>/` - Update report status
- `POST /api/reports/<report_id>/followup/` - Add follow-up

## 🔐 Role-Based Access Control

### Roles

1. **Admin** (Full Access)
   - All CRUD operations
   - User management
   - Delete any content
   - View and manage reports

2. **Editor** (Content Management)
   - Create, edit, publish content
   - Cannot delete
   - View and manage reports

3. **Author** (Content Creation)
   - Create drafts
   - Cannot publish without approval
   - Cannot access reports

4. **Viewer** (Read-Only)
   - View backend content
   - No creation/editing

## 📝 Filtering & Search

### Query Parameters

**Posts**:
- `?search=keyword` - Search in title/content
- `?category=slug` - Filter by category
- `?language=en` - Filter by language (en, lg, sw)
- `?featured=true` - Only featured posts
- `?ordering=-published_at` - Order by field

**Resources**:
- `?search=keyword` - Search in title/description
- `?category=slug` - Filter by category
- `?language=en` - Filter by language
- `?featured=true` - Only featured resources

**FAQs**:
- `?search=keyword` - Search in question/answer
- `?category=slug` - Filter by category
- `?language=en` - Filter by language

**Reports** (Admin/Editor only):
- `?status=PENDING` - Filter by status
- `?category=CHILD_PROTECTION` - Filter by category
- `?assigned_to_me=true` - Show only assigned to me

## 🔒 Security Features

### Report Encryption
Sensitive report data is encrypted using Fernet (symmetric encryption):

1. **Generate encryption key**:
   ```bash
   python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
   ```

2. **Add to .env**:
   ```
   ENCRYPTION_KEY=your-generated-key
   ```

3. **Usage**: Reports are automatically encrypted on save

### Production Security Settings
When `DEBUG=False`:
- SSL redirect enabled
- Secure cookies
- HSTS headers
- XSS protection
- Content-type sniffing protection

## 🌍 Multilingual Support

The CMS supports three languages:
- English (`en`)
- Luganda (`lg`)
- Swahili (`sw`)

Filter content by language using `?language=en` query parameter.

## 📊 Admin Panel Customization

Access Django Admin at `/admin/`:

**Features**:
- Custom list displays with filters
- Search functionality
- Inline editing
- Color-coded status badges (Reports)
- Bulk actions
- Role-based permissions

## 🧪 Testing

```bash
# Run tests
python manage.py test

# Run tests with coverage
coverage run --source='.' manage.py test
coverage report
```

## 📦 Project Structure

```
sauti_cms/
├── cms/                    # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/                  # User management
│   ├── models.py          # Custom User model
│   ├── serializers.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
├── posts/                  # Blog/News system
│   ├── models.py          # Post, Category, Tag
│   ├── serializers.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
├── resources/              # Resource library
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── faqs/                   # FAQ system
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── partners/               # Partner organizations
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── reports/                # Case reporting
│   ├── models.py          # Report, ReportFollowUp
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── media/                  # Uploaded files
├── staticfiles/            # Static files
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 🔧 Configuration

### Environment Variables (.env)

```env
# Django
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Database
DB_NAME=sauti_cms
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

# JWT
JWT_ACCESS_TOKEN_LIFETIME=60
JWT_REFRESH_TOKEN_LIFETIME=1440

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-password

# Encryption
ENCRYPTION_KEY=your-fernet-key
```

## 📋 Database Models

### User
- Username, email, password
- Role (Admin, Editor, Author, Viewer)
- Organization, phone_number

### Post
- Title, slug, content, excerpt
- Author, category, tags
- Status (Draft, Published)
- Language, featured_image
- Views count, published_at

### Resource
- Title, slug, description
- Category, file, thumbnail
- Language, file_size, file_type
- Download count

### FAQ
- Question, answer
- Category, language
- Order, views_count

### Partner
- Name, slug, description
- Partner type, logo
- Website, email, phone

### Report
- Reference number, category
- Description (encrypted)
- Anonymous flag, contact info
- Status, assigned_to
- IP address, user_agent

## 🚀 Deployment to Production

### Using Gunicorn + Nginx

1. **Install Nginx**:
   ```bash
   sudo apt install nginx
   ```

2. **Gunicorn config** (`/etc/systemd/system/sauti-cms.service`):
   ```ini
   [Unit]
   Description=Sauti CMS Gunicorn
   After=network.target

   [Service]
   User=www-data
   Group=www-data
   WorkingDirectory=/var/www/sauti_cms
   Environment="PATH=/var/www/sauti_cms/venv/bin"
   ExecStart=/var/www/sauti_cms/venv/bin/gunicorn \
             --workers 3 \
             --bind unix:/var/www/sauti_cms/sauti.sock \
             cms.wsgi:application

   [Install]
   WantedBy=multi-user.target
   ```

3. **Nginx config** (`/etc/nginx/sites-available/sauti`):
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;

       client_max_body_size 20M;

       location /static/ {
           alias /var/www/sauti_cms/staticfiles/;
       }

       location /media/ {
           alias /var/www/sauti_cms/media/;
       }

       location / {
           proxy_pass http://unix:/var/www/sauti_cms/sauti.sock;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

4. **Enable and start**:
   ```bash
   sudo systemctl enable sauti-cms
   sudo systemctl start sauti-cms
   sudo systemctl enable nginx
   sudo systemctl restart nginx
   ```

## 📞 Support

For issues or questions:
- Email: support@sauti.mglsd.go.ug
- GitHub Issues: [Create an issue]

## 📄 License

Proprietary - Ministry of Gender, Labour and Social Development (MGLSD), Uganda

## 🤝 Contributing

This is a government project. External contributions require approval from MGLSD.

---

**Built with ❤️ for Sauti 116 helpline by Sales Push Limited / Bitz ITC**
