# Sauti Admin - Source Code

Vue 3 + Vite-based administrative dashboard for the Sauti 116 CMS platform.

## Overview

This folder contains all source code for the admin dashboard, including Vue components, state management, routing, and utilities.

## Folder Structure

```
src/
├── components/          # Reusable Vue components
│   ├── admin/          # Admin-specific UI components
│   ├── common/         # Shared components
│   ├── contacts/       # Contact management components
│   ├── content/        # Content editor components
│   └── previews/       # Content preview modals
├── stores/             # Pinia state management
├── views/              # Page-level components
├── router/             # Vue Router configuration
├── composables/        # Reusable composition functions
├── utils/              # Helper functions
├── assets/             # Images and styling
├── App.vue             # Root component
├── main.js             # Entry point
└── README.md           # This file
```

## Key Directories

### `/components`
**Purpose**: Reusable UI components organized by feature

- **`admin/`**: Core admin UI components
  - `ConfirmModal.vue` - Confirmation dialogs
  - `FormModal.vue` - Generic form modals
  - `FilterBar.vue` - Filtering controls
  - `PageHeader.vue` - Page title and actions
  - `StatCard.vue` - Statistics display
  - `StatsGrid.vue` - Grid of statistics
  - `LoadingState.vue` - Loading indicators
  - `EmptyState.vue` - No data messages

- **`common/`**: Shared across admin and frontend
  - `AuditHistory.vue` - Content revision history

- **`contacts/`**: Contact management
  - `ContactItemList.vue` - Contact list display

- **`content/`**: Content editing
  - `HubCard.vue` - Content hub cards

- **`previews/`**: Content preview modals
  - `BlogPreviewModal.vue` - Blog post preview
  - `ResourcePreviewModal.vue` - Resource preview

### `/stores`
**Purpose**: Pinia state management for reactive data

**Available Stores**:
- `auth.js` - User authentication state
- `dashboard.js` - Dashboard statistics
- `partners.js` - Partner management state
- `posts.js` - Blog posts state
- `resources.js` - Resources state
- `socialMedia.js` - Social media posts state
- `uploads.js` - File uploads state
- `videos.js` - Video management state

### `/views`
**Purpose**: Page-level components representing routes

**Available Pages**:
- `LoginView.vue` - Admin login page
- `DashboardView.vue` - Main dashboard
- `BlogsView.vue` - Blog management
- `ResourcesView.vue` - Resources management
- `PartnersView.vue` - Partners management
- `UsersView.vue` - User management
- `SettingsView.vue` - Admin settings
- `DraftsView.vue` - Draft content management

### `/router`
**Purpose**: Vue Router configuration and navigation

**Key Features**:
- Route definitions
- Route guards for authentication
- Role-based access control
- Navigation middleware

### `/composables`
**Purpose**: Reusable composition functions (Vue 3)

**Examples**:
- `useAuth()` - Authentication logic
- `useApi()` - API communication
- `useNotifications()` - Toast notifications
- `useForm()` - Form handling

### `/utils`
**Purpose**: Helper functions and utilities

**Examples**:
- `api.js` - API client
- `constants.js` - App constants
- `validators.js` - Form validation
- `formatters.js` - Data formatting

### `/assets`
**Purpose**: Static files and styling

**Structure**:
- `main.css` - Global styles
- `sauti-logo.jpeg` - Logo image
- Other images and styling

## Component Structure

Each component typically includes:

```vue
<template>
  <!-- HTML structure -->
</template>

<script setup>
// Composition API with setup syntax
// Imports, state, methods, computed
</script>

<style scoped>
/* Scoped styling */
</style>
```

## State Management (Pinia)

### Example Store Structure
```javascript
// stores/example.js
import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

export const useExampleStore = defineStore('example', () => {
  // State
  const items = ref([]);

  // Computed
  const totalItems = computed(() => items.value.length);

  // Actions
  const fetchItems = async () => {
    // API call
  };

  return {
    items,
    totalItems,
    fetchItems
  };
});
```

### Using Stores in Components
```vue
<script setup>
import { useExampleStore } from '@/stores/example';

const exampleStore = useExampleStore();
// Access state: exampleStore.items
// Call actions: exampleStore.fetchItems()
</script>
```

## Routing

### Route Configuration
```javascript
// router/index.js
const routes = [
  {
    path: '/login',
    component: LoginView,
    meta: { requiresAuth: false }
  },
  {
    path: '/dashboard',
    component: DashboardView,
    meta: { requiresAuth: true, requiredRole: 'ADMIN' }
  }
];
```

### Protected Routes
- Dashboard: Admin access only
- Content management: Editor+ access
- Settings: Admin only
- User management: Admin only

## API Communication

### Making API Calls
```javascript
// In composables or stores
import { api } from '@/utils/api';

// GET request
const response = await api.get('/posts/');

// POST request
const response = await api.post('/posts/', { data });

// PUT request
const response = await api.put('/posts/1/', { data });

// DELETE request
await api.delete('/posts/1/');
```

### Authentication
```javascript
// Automatically includes token in all requests
// Token stored in localStorage or sessionStorage
```

## Form Handling

### Composable Usage
```vue
<script setup>
import { useForm } from '@/composables/useForm';

const { form, errors, submit } = useForm({
  title: '',
  content: ''
});

const onSubmit = async () => {
  const result = await submit('/api/posts/', 'POST');
  if (result) {
    // Success
  }
};
</script>
```

## Authentication Flow

1. **Login**: User enters credentials on LoginView
2. **Token Received**: API returns JWT token
3. **Token Storage**: Token stored in localStorage
4. **Protected Routes**: Token checked before accessing protected pages
5. **API Requests**: Token included in Authorization header
6. **Token Refresh**: Automatic refresh on expiration
7. **Logout**: Token cleared, redirect to login

## Styling

### Tailwind CSS
- Global styles with Tailwind classes
- Configuration in `tailwind.config.js`
- Responsive design utilities

### Scoped Styles
- Component-specific styling with `scoped` attribute
- CSS modules support available

### CSS Variables
- Theme colors defined in CSS
- Customizable through configuration

## Best Practices

### Component Organization
1. Keep components small and focused
2. Use meaningful names
3. Separate logic from presentation
4. Reuse components where possible

### State Management
1. Keep state in stores, not components
2. Use computed for derived state
3. Actions for async operations
4. Avoid storing UI state in stores

### Performance
1. Use `lazy` loading for routes
2. Implement pagination for lists
3. Avoid unnecessary re-renders
4. Use computed properties wisely

### Code Quality
1. Use TypeScript (optional)
2. Write tests for components
3. Follow ESLint rules
4. Document complex logic

## Development Workflow

### Running Development Server
```bash
npm run dev
```

### Building for Production
```bash
npm run build
```

### Preview Production Build
```bash
npm run preview
```

### Run Tests
```bash
npm run test
```

### Lint Code
```bash
npm run lint
```

## Common Tasks

### Create New Component
```vue
<!-- components/MyComponent.vue -->
<template>
  <div class="my-component">
    <!-- Component template -->
  </div>
</template>

<script setup>
import { ref } from 'vue';

const count = ref(0);
</script>

<style scoped>
.my-component {
  /* Styles */
}
</style>
```

### Create New Page
1. Create component in `views/` folder
2. Add route in `router/index.js`
3. Add navigation link in AppHeader
4. Implement functionality

### Add API Integration
1. Create store with API calls
2. Use composables for reusable logic
3. Implement error handling
4. Add loading states

## Troubleshooting

### Components Not Rendering
1. Check imports are correct
2. Verify component registration
3. Check scoped CSS conflicts

### State Not Updating
1. Ensure using proper store syntax
2. Check mutations/actions called correctly
3. Use Vue DevTools to debug

### API Calls Failing
1. Check token is sent
2. Verify API endpoint URL
3. Check network in browser DevTools
4. Review server logs

## Related Files

- `vite.config.js` - Build configuration
- `tailwind.config.js` - Tailwind CSS configuration
- `package.json` - Dependencies
- `index.html` - HTML template

## Related Documentation

- [Admin Dashboard README](../README.md)
- [CMS Backend API](../../sauti_cms/README.md)
- [Vue 3 Documentation](https://vuejs.org/)
- [Vite Documentation](https://vitejs.dev/)
- [Pinia Documentation](https://pinia.vuejs.org/)
- [Vue Router Documentation](https://router.vuejs.org/)

## Support

For questions about the admin dashboard source code:
- Check Vue documentation
- Review component examples
- Check store implementations
- Consult API documentation
