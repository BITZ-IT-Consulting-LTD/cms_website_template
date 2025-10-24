# Sauti Child Helpline - Vue 3 Frontend

A modern, responsive, and accessible Vue 3 frontend application for the Sauti Child Helpline website. Built to empower children, GBV survivors, and migrant workers in Uganda with easy access to support services.

## Features

- **Modern Stack**: Vue 3 Composition API + Vite for fast development
- **State Management**: Pinia for reactive state management
- **Routing**: Vue Router with route guards and lazy loading
- **Styling**: TailwindCSS for beautiful, responsive design
- **API Integration**: Axios with interceptors for seamless backend communication
- **Multilingual**: Support for English, Luganda, and Swahili
- **Accessibility**: WCAG compliant with ARIA labels and keyboard navigation
- **Mobile-First**: Optimized for mobile devices
- **Anonymous Reporting**: Secure, multi-step report submission form

## Tech Stack

- Vue 3.4.21 (Composition API)
- Vite 5.2.0
- Pinia 2.1.7 (State Management)
- Vue Router 4.3.0
- Axios 1.6.8
- TailwindCSS 3.4.3
- HeroIcons for icons

## Quick Start

### Prerequisites

- Node.js 18+ and npm/yarn
- Running Django backend API (see backend README)

### Installation

```bash
# Clone or navigate to the project
cd sauti-frontend

# Install dependencies
npm install

# Create environment file
cp .env.example .env

# Edit .env with your API URL
# VITE_API_URL=http://localhost:8000/api

# Start development server
npm run dev
```

The app will be available at `http://localhost:3000`

## Project Structure

```
sauti-frontend/
├── src/
│   ├── assets/
│   │   └── styles/
│   │       └── main.css          # Centralized Tailwind styles
│   ├── components/
│   │   ├── layout/
│   │   │   ├── Header.vue        # Main navigation
│   │   │   └── Footer.vue        # Footer with contact info
│   │   ├── blog/
│   │   │   ├── BlogCard.vue      # Blog post card
│   │   │   └── BlogList.vue      # Blog listing (placeholder)
│   │   ├── resources/
│   │   │   └── ResourceCard.vue  # Resource card (placeholder)
│   │   ├── faqs/
│   │   │   └── FaqList.vue       # FAQ accordion (placeholder)
│   │   ├── partners/
│   │   │   └── PartnerCarousel.vue  # Partners carousel (placeholder)
│   │   ├── reports/
│   │   │   └── ReportForm.vue    # ⭐ Multi-step report form
│   │   └── common/
│   │       ├── LanguageSwitcher.vue  # Language selector
│   │       ├── GetHelpButton.vue     # Emergency help modal
│   │       └── Loader.vue            # Loading spinner
│   ├── views/
│   │   ├── Home.vue              # Landing page
│   │   ├── About.vue             # About Sauti
│   │   ├── Blog.vue              # Blog listing
│   │   ├── BlogDetail.vue        # Single blog post
│   │   ├── Resources.vue         # Resources library
│   │   ├── Faqs.vue              # FAQ page
│   │   ├── Partners.vue          # Partners page
│   │   ├── Report.vue            # ⭐ Report submission page
│   │   ├── Contact.vue           # Contact page
│   │   ├── Login.vue             # Staff login
│   │   └── NotFound.vue          # 404 page
│   ├── router/
│   │   └── index.js              # Route configuration
│   ├── store/
│   │   ├── auth.js               # Authentication state
│   │   ├── blog.js               # Blog/posts state
│   │   ├── resources.js          # Resources state
│   │   ├── faqs.js               # FAQs state
│   │   └── partners.js           # Partners state
│   ├── utils/
│   │   └── axios.js              # ⭐ Axios instance with interceptors
│   ├── App.vue                   # Root component
│   └── main.js                   # Application entry point
├── public/                        # Static assets
├── index.html                     # HTML template
├── vite.config.js                # Vite configuration
├── tailwind.config.js            # Tailwind configuration
├── postcss.config.js             # PostCSS configuration
├── package.json                  # Dependencies
├── .env.example                  # Environment variables template
└── README.md                     # This file
```

## Key Components

### 1. ReportForm (Most Important!)
Location: `src/components/reports/ReportForm.vue`

Multi-step form for anonymous case reporting:
- **Step 1**: Category selection (Child Protection, GBV, Migrants, PSEA)
- **Step 2**: Report details (description, location, file upload)
- **Step 3**: Contact information (optional for anonymous reporting)
- **Step 4**: Review and submit

Features:
- Form validation at each step
- File upload support
- Anonymous submission option
- Success modal with reference number
- Mobile-optimized

### 2. GetHelpButton
Location: `src/components/common/GetHelpButton.vue`

Emergency access button that shows a modal with all help channels:
- 116 hotline (tap-to-call)
- WhatsApp
- U-Report
- Online form
- Email
- Safety notice

### 3. Axios Interceptors
Location: `src/utils/axios.js`

Centralized API client with:
- Automatic JWT token injection
- 401 error handling (auto-logout and redirect)
- Request/response logging
- Error handling for all status codes
- Convenient API methods for all endpoints

## Styling

### TailwindCSS Configuration
Custom color palette matching Sauti brand:
- **Primary**: Blue (`#3b82f6`) - Trust, professionalism
- **Secondary**: Orange (`#f97316`) - Emergencies, alerts
- **Success**: Green (`#10b981`) - Positive actions
- **Purple**: (`#8b5cf6`) - GBV services
- **Teal**: (`#14b8a6`) - Resources
- **Danger**: Red (`#ef4444`) - Critical alerts

### Custom CSS Classes
All custom styles centralized in `src/assets/styles/main.css`:
- Button styles (`.btn-primary`, `.btn-secondary`, `.btn-emergency`)
- Card styles (`.card`, `.service-card`)
- Form styles (`.form-input`, `.form-label`, `.form-error`)
- Utility classes for accessibility

## 🔌 API Integration

### Environment Variables
```env
VITE_API_URL=http://localhost:8000/api  # Backend API URL
```

### Available Stores

#### Auth Store (`useAuthStore`)
```javascript
import { useAuthStore } from '@/store/auth'

const authStore = useAuthStore()
await authStore.login({ username, password })
await authStore.logout()
const isAuthenticated = authStore.isAuthenticated
```

#### Blog Store (`useBlogStore`)
```javascript
import { useBlogStore } from '@/store/blog'

const blogStore = useBlogStore()
await blogStore.fetchPosts({ category: 'news', language: 'en' })
await blogStore.fetchPost('post-slug')
```

#### Resources Store (`useResourcesStore`)
```javascript
import { useResourcesStore } from '@/store/resources'

const resourcesStore = useResourcesStore()
await resourcesStore.fetchResources({ category: 'guides' })
```

## 🛣️ Routes

| Path | Component | Description |
|------|-----------|-------------|
| `/` | Home | Landing page with hero and services |
| `/about` | About | About Sauti information |
| `/blog` | Blog | Blog listing with filters |
| `/blog/:slug` | BlogDetail | Single blog post |
| `/resources` | Resources | Downloadable resources |
| `/faqs` | Faqs | FAQ accordion |
| `/partners` | Partners | Partner organizations |
| `/report` | Report | ⭐ Anonymous case reporting |
| `/contact` | Contact | Contact information and form |
| `/login` | Login | Staff login (admin access) |
| `*` | NotFound | 404 page |

## 🌍 Multilingual Support

Three languages supported:
- **English** (en) - Default
- **Luganda** (lg) - Primary local language
- **Swahili** (sw) - Regional language

Language switcher in header allows users to change language. Language preference stored in localStorage.

To add more languages, update `LanguageSwitcher.vue` component.

## 📱 Responsive Design

Mobile-first approach:
- **Mobile**: 320px+
- **Tablet**: 768px+
- **Desktop**: 1024px+
- **Large**: 1280px+

All components optimized for touch interactions on mobile devices.

## ♿ Accessibility

WCAG 2.1 AA compliant:
- Semantic HTML
- ARIA labels on all interactive elements
- Keyboard navigation support
- Focus visible indicators
- Alt text for images
- Color contrast ratios meet standards
- Screen reader compatible

## 🔒 Security Features

1. **JWT Authentication**
   - Tokens stored in localStorage
   - Automatic token injection in API requests
   - Auto-logout on 401 errors

2. **Anonymous Reporting**
   - No authentication required
   - Optional contact information
   - Secure file uploads
   - Client-side form validation

3. **CORS Configuration**
   - Configured to work with Django backend
   - Credentials included in requests

## 🧪 Development

### Available Scripts

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint

# Format code
npm run format
```

### Code Style
- ESLint for code quality
- Prettier for code formatting
- Vue 3 Composition API with `<script setup>`
- Reactive state with `ref` and `reactive`

### Component Structure
All components follow this pattern:
```vue
<template>
  <!-- Template -->
</template>

<script setup>
import { ref } from 'vue'
// Component logic
</script>

<style scoped>
/* Component-specific styles */
</style>
```

## 🏗️ Build for Production

```bash
# Build optimized production bundle
npm run build

# Output will be in /dist directory
# Serve with any static file server
```

### Production Checklist
- [ ] Set `VITE_API_URL` to production backend
- [ ] Update contact information (phone, email, WhatsApp)
- [ ] Add real partner logos
- [ ] Configure analytics (if using)
- [ ] Test all forms and API integrations
- [ ] Verify mobile responsiveness
- [ ] Run accessibility audit
- [ ] Test on multiple browsers

## 🚀 Deployment

### Option 1: Netlify/Vercel
```bash
npm run build
# Upload /dist folder or connect Git repo
```

### Option 2: Nginx
```bash
npm run build

# Copy dist/ to web server
sudo cp -r dist/* /var/www/sauti/

# Nginx config
server {
    listen 80;
    server_name yourdomain.com;
    root /var/www/sauti;
    index index.html;
    
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

### Option 3: Docker
```dockerfile
FROM node:18-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

## 🐛 Troubleshooting

### API Connection Issues
```bash
# Check if backend is running
curl http://localhost:8000/api/posts/

# Verify VITE_API_URL in .env
echo $VITE_API_URL

# Check browser console for CORS errors
```

### Build Errors
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install

# Clear Vite cache
rm -rf node_modules/.vite
```

### Hot Reload Not Working
```bash
# Restart dev server
npm run dev

# Check for file watcher limits (Linux)
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

## 📚 Additional Resources

- [Vue 3 Documentation](https://vuejs.org/)
- [Pinia Documentation](https://pinia.vuejs.org/)
- [TailwindCSS Documentation](https://tailwindcss.com/)
- [Vite Documentation](https://vitejs.dev/)
- [Backend API Documentation](../sauti_cms/API_DOCUMENTATION.md)

## 🤝 Contributing

This is a government project. External contributions require approval from MGLSD.

## 📄 License

Proprietary - Ministry of Gender, Labour and Social Development (MGLSD), Uganda

## 📞 Support

For issues or questions:
- Email: support@sauti.mglsd.go.ug
- Hotline: 116 (within Uganda)

---

**Built with ❤️ for Sauti Child Helpline by Sales Push Limited / Bitz ITC**
