# Admin UI - Blog Posts Stats Display Fix

**Date**: October 29, 2025
**Component**: Admin Dashboard - Posts View
**Status**: ✅ Complete

---

## Problem

The Blog Posts Management UI was not showing accurate counts for published and draft posts in the stats cards.

**User Report**: "the Blog Posts Management UI on admin does not show the count of published and drafts. How can that be fixed"

**Root Cause**: The frontend was filtering posts using lowercase status values ('published', 'draft', 'archived') but Django's Post model uses uppercase status values ('PUBLISHED', 'DRAFT', 'ARCHIVED') based on TextChoices definition.

---

## Changes Made

### File Modified: `sauti-admin/src/views/PostsView.vue`

#### 1. Stats Computed Property (Lines 297-298)

**Before**:
```javascript
const stats = computed(() => {
  const total = posts.value.length
  const published = posts.value.filter(p => p.status === 'published').length  // ❌ Wrong
  const draft = posts.value.filter(p => p.status === 'draft').length  // ❌ Wrong
  const totalViews = posts.value.reduce((sum, p) => sum + (p.views_count || 0), 0)
```

**After**:
```javascript
const stats = computed(() => {
  const total = posts.value.length
  const published = posts.value.filter(p => p.status === 'PUBLISHED').length  // ✅ Correct
  const draft = posts.value.filter(p => p.status === 'DRAFT').length  // ✅ Correct
  const totalViews = posts.value.reduce((sum, p) => sum + (p.views_count || 0), 0)
```

#### 2. Status Filter Dropdown (Lines 101-103)

**Before**:
```vue
<select v-model="statusFilter" class="form-select">
  <option value="">All Status</option>
  <option value="published">Published</option>  <!-- ❌ Wrong -->
  <option value="draft">Draft</option>  <!-- ❌ Wrong -->
  <option value="archived">Archived</option>  <!-- ❌ Wrong -->
</select>
```

**After**:
```vue
<select v-model="statusFilter" class="form-select">
  <option value="">All Status</option>
  <option value="PUBLISHED">Published</option>  <!-- ✅ Correct -->
  <option value="DRAFT">Draft</option>  <!-- ✅ Correct -->
  <option value="ARCHIVED">Archived</option>  <!-- ✅ Correct -->
</select>
```

#### 3. Status Badge CSS Classes (Lines 189-191)

**Before**:
```vue
<span
  class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
  :class="{
    'bg-green-100 text-green-800': post.status === 'published',  // ❌ Wrong
    'bg-yellow-100 text-yellow-800': post.status === 'draft',  // ❌ Wrong
    'bg-gray-100 text-gray-800': post.status === 'archived'  // ❌ Wrong
  }"
>
  {{ post.status }}
</span>
```

**After**:
```vue
<span
  class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
  :class="{
    'bg-green-100 text-green-800': post.status === 'PUBLISHED',  // ✅ Correct
    'bg-yellow-100 text-yellow-800': post.status === 'DRAFT',  // ✅ Correct
    'bg-gray-100 text-gray-800': post.status === 'ARCHIVED'  // ✅ Correct
  }"
>
  {{ post.status }}
</span>
```

#### 4. Preview Function (Line 360)

**Before**:
```javascript
const previewPost = (post) => {
  if (post.status === 'draft') {  // ❌ Wrong
    toast.warning('Cannot preview draft content')
    return
  }

  const url = `/blog/${post.slug}`
  window.open(url, '_blank')
}
```

**After**:
```javascript
const previewPost = (post) => {
  if (post.status === 'DRAFT') {  // ✅ Correct
    toast.warning('Cannot preview draft content')
    return
  }

  const url = `/blog/${post.slug}`
  window.open(url, '_blank')
}
```

#### 5. Duplicate Function (Line 376)

**Before**:
```javascript
const duplicatePost = async (post) => {
  try {
    const duplicateData = {
      ...post,
      title: `${post.title} (Copy)`,
      slug: `${post.slug}-copy-${Date.now()}`,
      status: 'draft'  // ❌ Wrong
    }

    await postsStore.createPost(duplicateData)
    toast.success(`"${post.title}" duplicated successfully`)
  } catch (err) {
    console.error('Duplicate error:', err)
    toast.error('Failed to duplicate post')
  }
}
```

**After**:
```javascript
const duplicatePost = async (post) => {
  try {
    const duplicateData = {
      ...post,
      title: `${post.title} (Copy)`,
      slug: `${post.slug}-copy-${Date.now()}`,
      status: 'DRAFT'  // ✅ Correct
    }

    await postsStore.createPost(duplicateData)
    toast.success(`"${post.title}" duplicated successfully`)
  } catch (err) {
    console.error('Duplicate error:', err)
    toast.error('Failed to duplicate post')
  }
}
```

---

## Django Backend Status Values

The Django Post model uses TextChoices with uppercase values:

```python
class StatusChoices(models.TextChoices):
    DRAFT = 'DRAFT', 'Draft'
    PUBLISHED = 'PUBLISHED', 'Published'
    ARCHIVED = 'ARCHIVED', 'Archived'
```

**API Response Example**:
```json
{
  "id": 1,
  "title": "Sample Post",
  "status": "PUBLISHED",  // ✅ Uppercase
  ...
}
```

---

## Impact

### Before Fix:
- **Published count**: Always showed 0
- **Draft count**: Always showed 0
- **Status filter**: Did not filter posts correctly
- **Status badges**: No color coding displayed

### After Fix:
- ✅ **Published count**: Shows accurate count of published posts
- ✅ **Draft count**: Shows accurate count of draft posts
- ✅ **Status filter**: Correctly filters posts by status
- ✅ **Status badges**: Proper color coding (green for published, yellow for draft, gray for archived)
- ✅ **Preview**: Correctly prevents preview of draft posts
- ✅ **Duplicate**: Creates copies as drafts correctly

---

## Deployment

**Container Rebuilt**: ✅ Admin container rebuilt with `--no-cache` flag

```bash
docker compose --env-file .env.docker -f docker-compose-full.yml build --no-cache admin
docker compose --env-file .env.docker -f docker-compose-full.yml restart admin
```

**Access**: http://localhost:3001
- Navigate to "Blog Posts"
- Stats cards now display correct counts
- Status filter dropdown works correctly
- Status badges show proper colors

---

## User Experience

### Stats Cards Display
1. **Total Posts**: Shows total number of posts (all statuses)
2. **Published**: Shows count of posts with status='PUBLISHED'
3. **Drafts**: Shows count of posts with status='DRAFT'
4. **Total Views**: Shows sum of views across all posts

### Status Filtering
- Select "Published" from dropdown → Shows only published posts
- Select "Draft" from dropdown → Shows only draft posts
- Select "Archived" from dropdown → Shows only archived posts
- Select "All Status" → Shows all posts

### Visual Indicators
- **Green badge**: Published posts
- **Yellow badge**: Draft posts
- **Gray badge**: Archived posts

---

## Benefits

1. **Accurate Statistics**: Stats cards now reflect real data from Django
2. **Consistent Filtering**: Status filter dropdown works as expected
3. **Visual Clarity**: Status badges correctly indicate post state
4. **Backend Consistency**: Frontend matches Django's uppercase status values
5. **Better UX**: Users can easily identify post status at a glance

---

## Related Files

No other files needed changes as this was isolated to the PostsView component. However, similar issues may exist in other views that handle status values:

**Potential Files to Check**:
- `sauti-admin/src/views/VideosView.vue` (may have similar status filtering)
- `sauti-admin/src/views/DraftsView.vue` (handles draft posts)
- Any other component that filters by status

---

**Status**: ✅ Complete and deployed
