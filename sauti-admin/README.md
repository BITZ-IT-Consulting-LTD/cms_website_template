# Sauti Admin Dashboard

A modern Vue 3 admin dashboard for the Sauti Child Helpline CMS system.

## Features

- 🎨 **Modern Design** - Clean, professional interface matching provided designs
- 🔐 **JWT Authentication** - Secure login with role-based access control
- 📊 **Dashboard Analytics** - Real-time stats and performance metrics
- ✍️ **Rich Text Editor** - Full-featured blog post editor
- 🎥 **Video Management** - Upload and manage video content
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- 🚀 **Fast Performance** - Built with Vue 3 and Vite

## Tech Stack

- **Frontend Framework**: Vue 3 with Composition API
- **Build Tool**: Vite
- **Styling**: TailwindCSS
- **State Management**: Pinia
- **Routing**: Vue Router 4
- **HTTP Client**: Axios
- **Icons**: Heroicons
- **Notifications**: Vue Toastification

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn
- Running Sauti CMS backend (Django)

### Installation

1. **Install dependencies**
   ```bash
   npm install
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   ```
   
   Update `.env` with your backend API URL:
   ```env
   VITE_API_URL=http://localhost:8000/api
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

   The admin dashboard will be available at `http://localhost:3001`

### Default Login

Use your Django admin credentials to log in:
- Username: Your Django admin username
- Password: Your Django admin password

## Project Structure

```
src/
├── assets/          # Static assets and global styles
├── components/      # Reusable Vue components
│   └── DashboardLayout.vue  # Main layout with sidebar
├── stores/          # Pinia stores for state management
│   ├── auth.js      # Authentication store
│   ├── dashboard.js # Dashboard data store
│   └── posts.js     # Blog posts store
├── utils/           # Utility functions
│   └── api.js       # Axios configuration and API methods
├── views/           # Page components
│   ├── LoginView.vue        # Login page
│   ├── DashboardView.vue    # Main dashboard
│   ├── PostEditView.vue     # Blog post editor
│   ├── VideoEditView.vue    # Video editor
│   └── ...
├── router/          # Vue Router configuration
├── App.vue          # Root component
└── main.js          # App initialization
```

## Key Features

### Dashboard Overview
- Stats cards showing content metrics
- Content management table with filters
- Analytics charts (Chart.js integration ready)
- Top performing content list

### Blog Post Editor
- Rich text WYSIWYG editor
- Image upload for featured images
- Category and tag management
- Draft/publish workflow
- SEO metadata fields

### Video Management
- Video file upload
- Thumbnail management
- Video metadata editing
- Privacy settings

### Authentication
- JWT token-based authentication
- Automatic token refresh
- Role-based access control
- Secure logout

## API Integration

The dashboard communicates with the Django backend via REST API:

- **Authentication**: `/api/auth/login/`, `/api/auth/token/refresh/`
- **Posts**: `/api/posts/` (CRUD operations)
- **Categories**: `/api/posts/categories/`
- **Tags**: `/api/posts/tags/`
- **Dashboard**: Custom endpoints for analytics data

## Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint
- `npm run format` - Format code with Prettier

### Environment Variables

- `VITE_API_URL` - Backend API base URL
- `VITE_APP_TITLE` - Application title
- `VITE_APP_VERSION` - Application version

## Deployment

1. **Build the application**
   ```bash
   npm run build
   ```

2. **Deploy the `dist` folder** to your web server

3. **Configure web server** to serve the SPA properly (redirect all routes to `index.html`)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

This project is part of the Sauti Child Helpline CMS system.
