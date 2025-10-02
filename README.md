# 🎉 Sauti Child Helpline CMS - Complete Full Stack Application

**A comprehensive, production-ready platform for child protection, GBV survivors, and migrant workers in Uganda**

---

## 🌟 Overview

This is a complete full-stack application consisting of:

1. **Backend:** Django 5.x + Django REST Framework + PostgreSQL
2. **Frontend:** Vue 3 + Vite + TailwindCSS + Pinia

**Key Feature:** Anonymous case reporting system with encrypted storage ⭐

---

## 📦 What's Included

### Backend (`sauti_cms/`)
- ✅ Django 5.0.6 + DRF 3.15.1
- ✅ PostgreSQL database
- ✅ JWT authentication
- ✅ Role-based access control (4 roles)
- ✅ Anonymous reporting with encryption
- ✅ Blog/News system
- ✅ Resource library
- ✅ FAQ management
- ✅ Partner showcase
- ✅ Multilingual support (EN, LG, SW)
- ✅ API documentation (Swagger/OpenAPI)
- ✅ Docker deployment ready

### Frontend (`sauti_cms_frontend/`)
- ✅ Vue 3.4.21 + Composition API
- ✅ Vite 5.2.0 build tool
- ✅ Pinia 2.1.7 state management
- ✅ Vue Router 4.3.0
- ✅ TailwindCSS 3.4.3 styling
- ✅ Axios with JWT interceptors
- ✅ Anonymous reporting form
- ✅ Emergency "Get Help Now" button
- ✅ Language switcher
- ✅ Mobile-first responsive design
- ✅ WCAG 2.1 AA accessible

---

## 🚀 Quick Start

### Prerequisites
- **Backend:** Python 3.12+, PostgreSQL 16+
- **Frontend:** Node.js 18+, npm/yarn

### Option 1: Automated Setup

**Backend:**
```bash
cd sauti_cms
chmod +x setup.sh
./setup.sh
```

**Frontend:**
```bash
cd sauti_cms_frontend
npm install
cp .env.example .env
# Edit .env with API URL
npm run dev
```

### Option 2: Docker Deployment

```bash
# Backend
cd sauti_cms
docker-compose up --build

# Frontend
cd sauti_cms_frontend
docker build -t sauti-frontend .
docker run -p 80:80 sauti-frontend
```

---

## 🔌 Access Points

Once running:

| Service | URL | Purpose |
|---------|-----|---------|
| **Frontend** | http://localhost:3000 | Main website |
| **Backend API** | http://localhost:8000/api/ | REST API |
| **Admin Panel** | http://localhost:8000/admin/ | Django admin |
| **API Docs** | http://localhost:8000/api/docs/ | Swagger UI |

---

## 🎯 Core Features

### 1. Anonymous Case Reporting ⭐

**The centerpiece of the application**

- **Frontend:** `/report` page with comprehensive form
- **Backend:** Encrypted storage with Fernet
- **Categories:** Child Protection, GBV, Migrants, PSEA
- **Features:**
  - No authentication required
  - Optional anonymous submission
  - File upload support
  - Auto-generated reference numbers
  - Success confirmation with next steps

**Flow:**
```
User fills form → Submit (no login) → Encrypted storage → Reference number returned
```

### 2. Content Management System

**Blog/News System:**
- Create, edit, publish posts
- Categories and tags
- Featured posts
- Draft → Published workflow
- Rich text editor
- View counter

**Resource Library:**
- Upload PDF, DOCX files
- Categorization
- Download tracking
- Multilingual support

**FAQ Management:**
- Question/Answer pairs
- Categories
- View counter
- Easy CRUD operations

**Partner Showcase:**
- Partner profiles
- Logo uploads
- Contact information
- Website links

### 3. User Management

**Roles:**
1. **Admin** - Full access, can delete
2. **Editor** - Create/edit/publish, view reports
3. **Author** - Create drafts only
4. **Viewer** - Read-only

**Authentication:**
- JWT token-based
- Automatic token refresh
- Secure password hashing
- Login/logout functionality

### 4. Multilingual Support

**Languages:**
- English (en) - Default
- Luganda (lg) - Primary local language
- Swahili (sw) - Regional language

**Implementation:**
- Language switcher in header
- API filtering by language
- Easy to expand to more languages

### 5. Mobile-First Design

**Features:**
- Responsive on all devices
- Touch-friendly (44px minimum tap targets)
- Mobile menu
- Optimized images
- Fast loading on slow connections

### 6. Accessibility (WCAG 2.1 AA)

**Compliance:**
- Semantic HTML
- ARIA labels
- Keyboard navigation
- Focus indicators
- Color contrast 4.5:1
- Screen reader support
- Reduced motion support

---

## 📊 Technology Stack

### Backend
```
Django 5.0.6
Django REST Framework 3.15.1
PostgreSQL 16
JWT Authentication (simplejwt)
Cryptography (Fernet encryption)
Gunicorn (WSGI server)
Docker support
```

### Frontend
```
Vue 3.4.21 (Composition API)
Vite 5.2.0
Pinia 2.1.7
Vue Router 4.3.0
TailwindCSS 3.4.3
Axios 1.6.8
@headlessui/vue
@heroicons/vue
```

---

## 📂 Project Structure

```
sauti_cms_project/
│
├── sauti_cms/                      # Django Backend
│   ├── cms/                        # Main project settings
│   ├── users/                      # User management
│   ├── posts/                      # Blog/News
│   ├── resources/                  # Resource library
│   ├── faqs/                       # FAQs
│   ├── partners/                   # Partners
│   ├── reports/                    # Anonymous reporting ⭐
│   ├── requirements.txt
│   ├── manage.py
│   ├── setup.sh                    # Automated setup
│   ├── README.md                   # Backend docs
│   ├── DEPLOYMENT.md               # Deployment guide
│   └── API_DOCUMENTATION.md        # API reference
│
├── sauti_cms_frontend/             # Vue 3 Frontend
│   ├── src/
│   │   ├── assets/                 # Styles
│   │   ├── components/             # Vue components
│   │   │   ├── layout/             # Header, Footer
│   │   │   ├── common/             # Shared components
│   │   │   ├── blog/               # Blog components
│   │   │   ├── resources/          # Resource components
│   │   │   ├── faqs/               # FAQ components
│   │   │   ├── partners/           # Partner components
│   │   │   └── reports/            # Report form ⭐
│   │   ├── views/                  # Page views
│   │   ├── store/                  # Pinia stores
│   │   ├── router/                 # Vue Router
│   │   ├── utils/                  # Axios client
│   │   ├── App.vue
│   │   └── main.js
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── README.md                   # Frontend docs
│   └── QUICKSTART.md               # Quick setup guide
│
└── INTEGRATION_GUIDE.md            # Full stack integration
```

---

## 🔐 Security Features

### Backend
1. **JWT Authentication** - Secure token-based auth
2. **Role-Based Access Control** - Granular permissions
3. **Report Encryption** - Fernet encryption for sensitive data
4. **HTTPS Enforcement** - Secure in production
5. **CORS Configuration** - Whitelisted origins
6. **CSRF Protection** - Django CSRF middleware
7. **SQL Injection Prevention** - Django ORM
8. **XSS Protection** - Django escaping

### Frontend
1. **JWT Token Storage** - LocalStorage with automatic refresh
2. **Axios Interceptors** - Automatic token injection
3. **Vue Escaping** - Automatic XSS prevention
4. **HTTPS Only** - Secure cookies in production
5. **No Inline Scripts** - CSP compatible
6. **Validated Forms** - Input sanitization

---

## 📖 Documentation

### Main Documentation Files

| File | Description | Location |
|------|-------------|----------|
| **Backend README** | Complete backend docs | `sauti_cms/README.md` |
| **Frontend README** | Complete frontend docs | `sauti_cms_frontend/README.md` |
| **Integration Guide** | Full stack integration | `INTEGRATION_GUIDE.md` |
| **Deployment Guide** | Production deployment | `sauti_cms/DEPLOYMENT.md` |
| **API Documentation** | API endpoints reference | `sauti_cms/API_DOCUMENTATION.md` |
| **Quick Start (Backend)** | Backend setup | `sauti_cms/PROJECT_SUMMARY.md` |
| **Quick Start (Frontend)** | Frontend setup | `sauti_cms_frontend/QUICKSTART.md` |

### API Documentation

Interactive API docs available at:
- **Swagger UI:** http://localhost:8000/api/docs/
- **ReDoc:** http://localhost:8000/api/redoc/
- **OpenAPI Schema:** http://localhost:8000/api/schema/

---

## 🧪 Testing

### Backend Tests
```bash
cd sauti_cms
source venv/bin/activate
python manage.py test
```

### Frontend Tests (Future)
```bash
cd sauti_cms_frontend
npm run test
```

### Integration Testing
See `INTEGRATION_GUIDE.md` for complete testing procedures.

---

## 🚢 Deployment

### Development
```bash
# Backend
cd sauti_cms
python manage.py runserver

# Frontend
cd sauti_cms_frontend
npm run dev
```

### Production (Docker)
```bash
# Backend
cd sauti_cms
docker-compose up -d

# Frontend
cd sauti_cms_frontend
npm run build
# Deploy dist/ folder
```

### Production (Traditional)
See `sauti_cms/DEPLOYMENT.md` for:
- Gunicorn + Nginx setup
- SSL configuration
- Database setup
- Static file serving
- Media file handling
- Backup strategies

---

## 🌍 Multilingual Setup

### Backend Configuration
```python
# cms/settings.py
LANGUAGES = [
    ('en', 'English'),
    ('lg', 'Luganda'),
    ('sw', 'Swahili'),
]
```

### Frontend Configuration
```javascript
// Language switcher component
languages = [
  { code: 'en', name: 'English' },
  { code: 'lg', name: 'Luganda' },
  { code: 'sw', name: 'Swahili' }
]
```

### Usage
```javascript
// Filter content by language
await blogStore.fetchPosts({ language: 'lg' })
```

---

## 🎨 Design System

### Color Palette
```javascript
primary: '#3b82f6'     // Blue - Trust, safety
secondary: '#f97316'   // Orange - Energy, warmth
success: '#22c55e'     // Green - Positive actions
danger: '#ef4444'      // Red - Emergency, alerts
purple: '#a855f7'      // Purple - GBV support
teal: '#14b8a6'        // Teal - Migrant workers
```

### Typography
```css
font-family: 'Inter', sans-serif;
font-heading: 'Poppins', sans-serif;
```

### Components
- Custom buttons (primary, secondary, danger, outline)
- Card layouts
- Form elements
- Alert messages
- Loading spinners

---

## 📊 System Architecture

```
┌──────────────────────────────────────────────┐
│          Users (Children, GBV              │
│          Survivors, Migrant Workers)         │
└──────────────────────────────────────────────┘
                    │
                    ↓
┌──────────────────────────────────────────────┐
│         Vue 3 Frontend (Port 3000)           │
│  ┌────────────┐  ┌────────────┐             │
│  │ Report Form│  │ Blog Pages │             │
│  └────────────┘  └────────────┘             │
│  ┌────────────────────────────────┐         │
│  │   Axios + JWT Interceptors     │         │
│  └────────────────────────────────┘         │
└──────────────────────────────────────────────┘
                    │
                    ↓ HTTPS + JWT
┌──────────────────────────────────────────────┐
│    Django REST Framework (Port 8000)         │
│  ┌────────────┐  ┌────────────┐             │
│  │Reports API │  │ Posts API  │             │
│  │(No Auth)   │  │(Public)    │             │
│  └────────────┘  └────────────┘             │
│  ┌────────────────────────────────┐         │
│  │   JWT Auth + Encryption        │         │
│  └────────────────────────────────┘         │
└──────────────────────────────────────────────┘
                    │
                    ↓ SQL Queries
┌──────────────────────────────────────────────┐
│       PostgreSQL Database (Port 5432)        │
│  ┌────────┐ ┌────────┐ ┌────────┐           │
│  │Reports │ │ Posts  │ │ Users  │           │
│  │(Encrypt│ │        │ │        │           │
│  └────────┘ └────────┘ └────────┘           │
└──────────────────────────────────────────────┘
```

---

## ✅ Feature Checklist

### Core Features
- [x] Anonymous case reporting
- [x] Blog/News system
- [x] Resource library
- [x] FAQ management
- [x] Partner showcase
- [x] User authentication
- [x] Role-based permissions
- [x] Multilingual support

### Security
- [x] JWT authentication
- [x] Report encryption
- [x] HTTPS support
- [x] CORS configuration
- [x] CSRF protection
- [x] XSS prevention
- [x] SQL injection prevention

### User Experience
- [x] Mobile-first design
- [x] Responsive layouts
- [x] Fast loading
- [x] Accessible (WCAG 2.1 AA)
- [x] Intuitive navigation
- [x] Error handling
- [x] Loading states

### Developer Experience
- [x] Comprehensive documentation
- [x] Setup automation scripts
- [x] API documentation
- [x] Code linting
- [x] Code formatting
- [x] Docker support
- [x] Environment configuration

---

## 🐛 Troubleshooting

See individual README files for specific issues:

- **Backend Issues:** `sauti_cms/README.md`
- **Frontend Issues:** `sauti_cms_frontend/README.md`
- **Integration Issues:** `INTEGRATION_GUIDE.md`

### Common Issues

**Backend won't start:**
- Check PostgreSQL is running
- Verify database credentials in .env
- Run migrations: `python manage.py migrate`

**Frontend can't connect to backend:**
- Check CORS settings in backend
- Verify VITE_API_URL in frontend .env
- Ensure backend is running on port 8000

**JWT token errors:**
- Check token expiry settings
- Verify SECRET_KEY matches
- Clear localStorage and login again

---

## 📞 Support

### Documentation
- Backend: `sauti_cms/README.md`
- Frontend: `sauti_cms_frontend/README.md`
- Integration: `INTEGRATION_GUIDE.md`

### Contact
- Email: support@sauti.mglsd.go.ug
- Website: https://sauti.mglsd.go.ug
- GitHub: [Create an issue]

---

## 📄 License

Proprietary - Ministry of Gender, Labour and Social Development (MGLSD), Uganda

---

## 🤝 Contributing

This is a government project. External contributions require approval from MGLSD.

---

## 🎓 Training Resources

### For Developers
- Django Docs: https://docs.djangoproject.com/
- DRF Docs: https://www.django-rest-framework.org/
- Vue 3 Docs: https://vuejs.org/
- TailwindCSS Docs: https://tailwindcss.com/

### For Content Managers
- Django Admin guide included in backend docs
- CMS training manual (to be created)
- Video tutorials (to be created)

---

## 🎉 Congratulations!

You now have a **complete, production-ready full-stack application** for the Sauti Child Helpline!

### What You Can Do Now:

1. **Deploy to Production** - Launch the platform
2. **Train Staff** - Onboard content managers
3. **Populate Content** - Add blog posts, resources, FAQs
4. **Monitor Performance** - Track usage and errors
5. **Gather Feedback** - Improve based on user input
6. **Scale** - Add features as needed

### Key Metrics to Track:

- Anonymous reports submitted
- Page views
- User engagement
- Mobile vs desktop traffic
- Most accessed resources
- Response times

---

## 🚀 Ready to Launch!

Your Sauti CMS is ready to protect and empower vulnerable communities in Uganda.

**Status: PRODUCTION READY** ✅

---

**Built with ❤️ for Sauti Child Helpline**  
**Ministry of Gender, Labour and Social Development (MGLSD), Uganda**  
**Developed by: Sales Push Limited / Bitz ITC**

---

*"Technology that saves lives and empowers communities"*
