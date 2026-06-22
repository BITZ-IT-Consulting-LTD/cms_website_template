# Posts (Blog/News) Application

Manages blog posts, news articles, and stories for the Sauti 116 helpline platform.

## Overview

This Django app provides a complete blog/news management system with:
- Post creation and publishing workflow
- Multi-language support (English, Luganda, Swahili)
- Category and tag organization
- Featured posts support
- Draft/publish status
- View tracking

## Models

### Post
**Purpose**: Blog post or news article
**Fields**:
- `title` - Post title
- `slug` - URL-friendly title
- `content` - Full post content (HTML supported)
- `excerpt` - Short summary for listing
- `author` - User who created the post
- `category` - Post category
- `tags` - Multiple tags for organization
- `status` - Draft or Published
- `language` - en (English), lg (Luganda), sw (Swahili)
- `featured` - Boolean flag for featured posts
- `featured_image` - Cover image for post
- `views_count` - Track post popularity
- `published_at` - Publication timestamp
- `created_at` - Creation timestamp
- `updated_at` - Last modified timestamp

### Category
**Purpose**: Organize posts by topic
**Fields**:
- `name` - Category name
- `slug` - URL-friendly name
- `description` - Category description
- `icon` - Category icon/image

### Tag
**Purpose**: Tag posts for cross-category organization
**Fields**:
- `name` - Tag name
- `slug` - URL-friendly name

## API Endpoints

### List Posts
```
GET /api/posts/
```

**Query Parameters**:
- `search=keyword` - Search in title/content
- `category=slug` - Filter by category
- `tag=slug` - Filter by tag
- `language=en` - Filter by language (en, lg, sw)
- `featured=true` - Only featured posts
- `ordering=-published_at` - Sort by field
- `page=1` - Pagination

**Response**:
```json
{
  "count": 42,
  "next": "http://api/posts/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Post Title",
      "slug": "post-title",
      "excerpt": "Short summary...",
      "author": "Admin User",
      "category": "News",
      "tags": ["tag1", "tag2"],
      "status": "PUBLISHED",
      "language": "en",
      "featured": true,
      "views_count": 1234,
      "published_at": "2024-01-15T10:00:00Z"
    }
  ]
}
```

### Get Post Detail
```
GET /api/posts/{slug}/
```

**Response**: Full post object with all fields and content

### Create Post
```
POST /api/posts/
Authorization: Token {user_token}
```

**Required Fields** (Admin/Editor only):
```json
{
  "title": "New Post",
  "content": "<p>Post content</p>",
  "category": 1,
  "language": "en",
  "status": "DRAFT"
}
```

### Update Post
```
PUT /api/posts/{slug}/
Authorization: Token {user_token}
```

**Allowed for**: Post author, Editors, Admins

### Delete Post
```
DELETE /api/posts/{slug}/
Authorization: Token {user_token}
```

**Allowed for**: Admins only

### List Categories
```
GET /api/posts/categories/
```

### List Tags
```
GET /api/posts/tags/
```

## Filtering & Search

### By Status (Published/Draft)
```
GET /api/posts/?status=PUBLISHED
GET /api/posts/?status=DRAFT
```

### By Category
```
GET /api/posts/?category=news
```

### By Language
```
GET /api/posts/?language=en  # English
GET /api/posts/?language=lg  # Luganda
GET /api/posts/?language=sw  # Swahili
```

### By Featured Flag
```
GET /api/posts/?featured=true
```

### Search
```
GET /api/posts/?search=helpline
# Searches in title and content
```

### Combined Query
```
GET /api/posts/?search=help&category=news&language=en&featured=true&ordering=-published_at
```

## Management Commands

### Populate Blog Posts
**File**: `management/commands/populate_blog_posts.py`

Seed the database with initial blog posts and categories.

```bash
python manage.py populate_blog_posts
```

## Admin Interface

Access at `/admin/posts/`:
- **Posts**: Create, edit, publish, filter by status/category/language
- **Categories**: Manage post categories
- **Tags**: Manage tags

**Features**:
- Inline editing
- Search functionality
- Filter by status, category, language
- Bulk actions
- Preview functionality
- Status badges (Draft, Published)

## File Structure

```
posts/
├── migrations/           # Database migration files
├── management/
│   └── commands/
│       └── populate_blog_posts.py   # Seed data
├── models.py             # Post, Category, Tag models
├── serializers.py        # API serializers
├── views.py              # API viewsets
├── admin.py              # Admin interface
├── urls.py               # URL routing
├── apps.py               # App configuration
├── tests.py              # Unit tests
└── README.md             # This file
```

## Common Tasks

### Create a New Post
1. Go to `/admin/posts/post/`
2. Click "Add Post"
3. Fill in title, content, category
4. Set language and status
5. Save

Or via API:
```bash
curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Token abc123" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Post",
    "content": "Post content",
    "category": 1,
    "language": "en",
    "status": "DRAFT"
  }'
```

### Publish a Draft Post
```
PUT /api/posts/{slug}/
{
  "status": "PUBLISHED",
  "published_at": "2024-01-15T10:00:00Z"
}
```

### Search Posts
```
GET /api/posts/?search=keyword
```

### Get Post Statistics
- View count: Tracked automatically on API access
- Most viewed posts: Sort by `-views_count`

## Permissions

### Role-Based Access

| Action | Viewer | Author | Editor | Admin |
|--------|--------|--------|--------|-------|
| View Published | ✓ | ✓ | ✓ | ✓ |
| View Draft | ✗ | ✓ (own) | ✓ | ✓ |
| Create | ✗ | ✓ | ✓ | ✓ |
| Edit | ✗ | ✓ (own) | ✓ | ✓ |
| Publish | ✗ | ✗ | ✓ | ✓ |
| Delete | ✗ | ✗ | ✗ | ✓ |

## Database Schema

### Posts Table
```sql
CREATE TABLE posts_post (
  id BIGINT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  slug VARCHAR(255) UNIQUE NOT NULL,
  content LONGTEXT,
  excerpt TEXT,
  author_id BIGINT REFERENCES users_user(id),
  category_id BIGINT REFERENCES posts_category(id),
  status VARCHAR(20),
  language VARCHAR(5),
  featured BOOLEAN DEFAULT False,
  featured_image VARCHAR(255),
  views_count INTEGER DEFAULT 0,
  published_at TIMESTAMP,
  created_at TIMESTAMP AUTO_NOW_ADD,
  updated_at TIMESTAMP AUTO_NOW
);

CREATE TABLE posts_tag (
  id BIGINT PRIMARY KEY,
  name VARCHAR(255),
  slug VARCHAR(255) UNIQUE
);

CREATE TABLE posts_post_tags (
  id BIGINT PRIMARY KEY,
  post_id BIGINT REFERENCES posts_post(id),
  tag_id BIGINT REFERENCES posts_tag(id),
  UNIQUE(post_id, tag_id)
);
```

## Troubleshooting

### Post Not Appearing on Frontend
**Possible Causes**:
1. Status is DRAFT (set to PUBLISHED)
2. Language filter doesn't match (check language field)
3. Post is not included in API response (check pagination)

**Solution**:
```bash
# Check post status
python manage.py shell
from posts.models import Post
Post.objects.filter(slug='your-post-slug').values('status', 'language')
```

### Search Not Working
1. Ensure search field is in SEARCH_FIELDS in serializer
2. Try exact keyword match
3. Check PostgreSQL full-text search configuration

### Image Upload Issues
1. Check MEDIA_ROOT path in settings.py
2. Verify folder permissions
3. Check file size limits

## Performance Optimization

### Query Optimization
- Use `select_related()` for author and category
- Use `prefetch_related()` for tags

### Caching
- Cache category list (rarely changes)
- Cache featured posts
- Cache popular posts by view count

### Pagination
- Default: 20 posts per page
- Adjust in settings if needed

## Testing

### Run Tests
```bash
python manage.py test posts
```

### Test Coverage
```bash
coverage run --source='posts' manage.py test posts
coverage report
```

## Related Documentation

- [Main CMS README](../README.md)
- [API Documentation](../API_DOCUMENTATION.md)
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

## Support

For issues or questions about the posts app, refer to:
- Backend CMS documentation
- Admin interface help
- API documentation
