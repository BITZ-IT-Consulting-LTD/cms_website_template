# Sauti Admin UI Components

This directory contains reusable admin UI components designed to create a consistent, dashboard-first experience across all views in the Sauti Admin application.

## Components

### PageHeader
Standardized page header with title, description, and optional primary action button.

**Usage:**
```vue
<PageHeader
  title="Blog Posts"
  description="Manage all blog posts and articles"
  action-label="Add New Post"
  :action-icon="PlusIcon"
  @action="openCreateModal"
/>
```

**Props:**
- `title` (String, required): Page title
- `description` (String, required): Contextual description
- `actionLabel` (String, optional): Primary action button label
- `actionIcon` (Component, optional): Heroicon component for button

**Events:**
- `@action`: Emitted when action button is clicked

---

### StatsGrid & StatCard
Mini dashboard for displaying key metrics at the top of each view.

**Usage:**
```vue
<StatsGrid>
  <StatCard
    label="Total Posts"
    :value="stats.total"
    :icon="DocumentTextIcon"
    color="blue"
  />
  <StatCard
    label="Published"
    :value="stats.published"
    :icon="CheckCircleIcon"
    color="green"
  />
  <StatCard
    label="Drafts"
    :value="stats.draft"
    :icon="PencilIcon"
    color="orange"
  />
  <StatCard
    label="Archived"
    :value="stats.archived"
    :icon="ArchiveBoxIcon"
    color="gray"
  />
</StatsGrid>
```

**StatCard Props:**
- `label` (String, required): Stat label
- `value` (String|Number, required): Stat value
- `icon` (Component, required): Heroicon component
- `color` (String, default: 'blue'): Color theme (blue, green, orange, red, purple, gray)
- `subtitle` (String, optional): Additional context

---

### FilterBar
Standardized filter bar with search, status, and custom filters.

**Usage:**
```vue
<FilterBar
  v-model="filters"
  search-placeholder="Search posts..."
  :status-options="[
    { value: 'published', label: 'Published' },
    { value: 'draft', label: 'Draft' }
  ]"
  status-label="All Status"
  :custom-options="categories"
  custom-label="All Categories"
/>
```

**Props:**
- `modelValue` (Object, required): Filter values object
- `searchPlaceholder` (String): Search input placeholder
- `statusOptions` (Array): Status filter options
- `statusLabel` (String): Status dropdown label
- `customOptions` (Array): Custom filter options
- `customLabel` (String): Custom dropdown label

**Slots:**
- `custom-filter`: Replace the default custom filter with your own

---

### FormModal
Modal for create/edit forms with proper keyboard handling and loading states.

**Usage:**
```vue
<FormModal
  :is-open="createModal.isOpen"
  title="Add New Post"
  submit-label="Create Post"
  :loading="saving"
  @close="createModal.close"
  @submit="handleCreate"
>
  <!-- Your form content here -->
  <div class="space-y-4">
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-2">Title</label>
      <input v-model="form.title" type="text" class="w-full px-4 py-2 border rounded-lg" />
    </div>
  </div>
</FormModal>
```

**Props:**
- `isOpen` (Boolean, required): Modal visibility state
- `title` (String, required): Modal title
- `submitLabel` (String, default: 'Save'): Submit button label
- `cancelLabel` (String, default: 'Cancel'): Cancel button label
- `loadingLabel` (String, default: 'Saving...'): Loading button label
- `loading` (Boolean): Loading state
- `submitDisabled` (Boolean): Disable submit button
- `size` (String, default: 'large'): Modal size (small, medium, large)

**Events:**
- `@close`: Emitted when modal should close
- `@submit`: Emitted when form is submitted

**Slots:**
- `default`: Modal content
- `footer-left`: Left side of footer (for destructive actions)

---

### ConfirmModal
Confirmation dialog for destructive actions.

**Usage:**
```vue
<ConfirmModal
  :is-open="deleteModal.isOpen"
  title="Delete Post?"
  message="Are you sure you want to delete this post? This action cannot be undone."
  confirm-label="Delete"
  variant="danger"
  :loading="deleting"
  @close="deleteModal.close"
  @confirm="handleDelete"
/>
```

**Props:**
- `isOpen` (Boolean, required): Modal visibility state
- `title` (String, required): Modal title
- `message` (String, required): Confirmation message
- `confirmLabel` (String, default: 'Confirm'): Confirm button label
- `cancelLabel` (String, default: 'Cancel'): Cancel button label
- `loadingLabel` (String, default: 'Processing...'): Loading label
- `loading` (Boolean): Loading state
- `variant` (String, default: 'danger'): Visual variant (danger, warning, info, success)

**Events:**
- `@close`: Emitted when modal should close
- `@confirm`: Emitted when action is confirmed

---

### EmptyState
Consistent empty state display.

**Usage:**
```vue
<EmptyState
  :icon="DocumentTextIcon"
  title="No posts found"
  message="Get started by creating your first blog post"
  action-label="Create Post"
  :action-icon="PlusIcon"
  @action="openCreateModal"
/>
```

**Props:**
- `icon` (Component, required): Heroicon component
- `title` (String, required): Empty state title
- `message` (String, required): Empty state message
- `actionLabel` (String, optional): Action button label
- `actionIcon` (Component, optional): Action button icon

**Events:**
- `@action`: Emitted when action button is clicked

**Slots:**
- `action`: Custom action content

---

### LoadingState
Consistent loading display.

**Usage:**
```vue
<LoadingState message="Loading posts..." />
```

**Props:**
- `message` (String, default: 'Loading...'): Loading message

---

## Composables

### useModal
Manage modal state consistently.

**Usage:**
```vue
<script setup>
import { useModal } from '@/composables'

const createModal = useModal()
const editModal = useModal()

const openEdit = (post) => {
  editModal.open(post) // Pass data to modal
}
</script>

<template>
  <button @click="createModal.open()">Create</button>
  <button @click="openEdit(post)">Edit</button>
  
  <FormModal
    :is-open="createModal.isOpen"
    @close="createModal.close"
  />
  
  <FormModal
    :is-open="editModal.isOpen"
    @close="editModal.close"
  >
    <!-- Access modal data via editModal.data -->
    <input v-model="editModal.data.title" />
  </FormModal>
</template>
```

**Returns:**
- `isOpen` (Ref<Boolean>): Modal visibility state
- `data` (Ref<any>): Modal data
- `open(data?)`: Open modal with optional data
- `close()`: Close modal
- `toggle()`: Toggle modal state

---

### useFilters
Manage filtering logic consistently.

**Usage:**
```vue
<script setup>
import { ref } from 'vue'
import { useFilters } from '@/composables'

const posts = ref([...])
const { filters, filteredItems, clearFilters, hasActiveFilters } = useFilters(posts)
</script>

<template>
  <FilterBar v-model="filters" />
  
  <div v-for="post in filteredItems" :key="post.id">
    {{ post.title }}
  </div>
</template>
```

**Parameters:**
- `items` (Ref<Array>): Reactive array to filter
- `initialFilters` (Object, optional): Initial filter values

**Returns:**
- `filters` (Ref<Object>): Filter values
- `filteredItems` (ComputedRef<Array>): Filtered items
- `clearFilters()`: Reset all filters
- `hasActiveFilters` (ComputedRef<Boolean>): Whether any filters are active

---

### useStats
Compute statistics from item lists.

**Usage:**
```vue
<script setup>
import { ref, computed } from 'vue'
import { useStats } from '@/composables'

const posts = ref([...])
const stats = useStats(posts)

// Custom stat
const todayPosts = stats.custom(post => {
  const today = new Date().toDateString()
  return new Date(post.created_at).toDateString() === today
})
</script>

<template>
  <StatsGrid>
    <StatCard label="Total" :value="stats.total" />
    <StatCard label="Published" :value="stats.published" />
    <StatCard label="Drafts" :value="stats.draft" />
    <StatCard label="Today" :value="todayPosts" />
  </StatsGrid>
</template>
```

**Parameters:**
- `items` (Ref<Array>): Reactive array to compute stats from

**Returns:**
- `total` (ComputedRef<Number>): Total items
- `active` (ComputedRef<Number>): Active items
- `inactive` (ComputedRef<Number>): Inactive items
- `published` (ComputedRef<Number>): Published items
- `draft` (ComputedRef<Number>): Draft items
- `archived` (ComputedRef<Number>): Archived items
- `featured` (ComputedRef<Number>): Featured items
- `urgent` (ComputedRef<Number>): Urgent items
- `custom(filterFn)`: Custom stat calculator

---

## Complete Example

Here's a complete example of a harmonized view:

```vue
<template>
  <div class="p-6">
    <!-- Page Header -->
    <PageHeader
      title="Blog Posts"
      description="Manage all blog posts and articles"
      action-label="Add New Post"
      :action-icon="PlusIcon"
      @action="createModal.open()"
    />

    <!-- Mini Dashboard -->
    <StatsGrid>
      <StatCard
        label="Total Posts"
        :value="stats.total"
        :icon="DocumentTextIcon"
        color="blue"
      />
      <StatCard
        label="Published"
        :value="stats.published"
        :icon="CheckCircleIcon"
        color="green"
      />
      <StatCard
        label="Drafts"
        :value="stats.draft"
        :icon="PencilIcon"
        color="orange"
      />
      <StatCard
        label="Archived"
        :value="stats.archived"
        :icon="ArchiveBoxIcon"
        color="gray"
      />
    </StatsGrid>

    <!-- Filters -->
    <FilterBar
      v-model="filters"
      search-placeholder="Search posts..."
      :status-options="statusOptions"
    />

    <!-- Loading State -->
    <LoadingState v-if="loading" message="Loading posts..." />

    <!-- Empty State -->
    <EmptyState
      v-else-if="filteredItems.length === 0"
      :icon="DocumentTextIcon"
      title="No posts found"
      message="Get started by creating your first blog post"
      action-label="Create Post"
      :action-icon="PlusIcon"
      @action="createModal.open()"
    />

    <!-- Content -->
    <div v-else class="space-y-4">
      <div v-for="post in filteredItems" :key="post.id" class="stats-card">
        <h3>{{ post.title }}</h3>
        <div class="flex gap-2">
          <button @click="editModal.open(post)">Edit</button>
          <button @click="confirmDelete(post)">Delete</button>
        </div>
      </div>
    </div>

    <!-- Create Modal -->
    <FormModal
      :is-open="createModal.isOpen"
      title="Add New Post"
      :loading="saving"
      @close="createModal.close"
      @submit="handleCreate"
    >
      <!-- Form fields -->
    </FormModal>

    <!-- Edit Modal -->
    <FormModal
      :is-open="editModal.isOpen"
      title="Edit Post"
      :loading="saving"
      @close="editModal.close"
      @submit="handleUpdate"
    >
      <!-- Form fields with editModal.data -->
    </FormModal>

    <!-- Delete Confirmation -->
    <ConfirmModal
      :is-open="deleteModal.isOpen"
      title="Delete Post?"
      message="This action cannot be undone."
      variant="danger"
      :loading="deleting"
      @close="deleteModal.close"
      @confirm="handleDelete"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useModal, useFilters, useStats } from '@/composables'
import {
  PageHeader,
  StatsGrid,
  StatCard,
  FilterBar,
  FormModal,
  ConfirmModal,
  EmptyState,
  LoadingState
} from '@/components/admin'
import {
  PlusIcon,
  DocumentTextIcon,
  CheckCircleIcon,
  PencilIcon,
  ArchiveBoxIcon
} from '@heroicons/vue/24/outline'

// Data
const posts = ref([])
const loading = ref(false)
const saving = ref(false)
const deleting = ref(false)

// Modals
const createModal = useModal()
const editModal = useModal()
const deleteModal = useModal()

// Filters & Stats
const { filters, filteredItems } = useFilters(posts)
const stats = useStats(posts)

// Status options
const statusOptions = [
  { value: 'published', label: 'Published' },
  { value: 'draft', label: 'Draft' }
]

// Actions
const handleCreate = async () => {
  // Create logic
}

const handleUpdate = async () => {
  // Update logic
}

const confirmDelete = (post) => {
  deleteModal.open(post)
}

const handleDelete = async () => {
  // Delete logic
}
</script>
```

---

## Design Principles

1. **Consistency**: All views should look and feel the same
2. **Clarity**: Actions should be obvious without documentation
3. **Efficiency**: Modals for speed, filters for control
4. **Accessibility**: Keyboard navigation, focus management, WCAG AA compliance

---

## Migration Checklist

When migrating a view to use these components:

- [ ] Replace custom header with `PageHeader`
- [ ] Add `StatsGrid` with 3-4 relevant stats
- [ ] Add `FilterBar` for list views
- [ ] Convert create/edit forms to `FormModal`
- [ ] Use `ConfirmModal` for delete actions
- [ ] Add `EmptyState` for empty lists
- [ ] Add `LoadingState` for loading states
- [ ] Use `useModal` composable for modal state
- [ ] Use `useFilters` for filtering logic
- [ ] Use `useStats` for statistics
- [ ] Test keyboard navigation
- [ ] Test mobile responsiveness
- [ ] Verify no functionality was lost
