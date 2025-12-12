# Sauti CMS API Documentation

Complete reference for the Sauti 116 helpline CMS REST API.

## Base URL

```
Development: http://localhost:8000/api
Production: https://yourdomain.com/api
```

## Authentication

The API uses JWT (JSON Web Token) authentication for protected endpoints.

### Obtaining Tokens

**Endpoint**: `POST /api/auth/login/`

**Request**:
```json
{
  "username": "admin",
  "password": "your_password"
}
```

**Response**:
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Using Tokens

Include the access token in the Authorization header:

```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
```

### Refreshing Tokens

**Endpoint**: `POST /api/auth/token/refresh/`

**Request**:
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

## API Endpoints

### 1. Authentication & User Management

#### Register User (Admin Only)
```http
POST /api/auth/register/
Authorization: Bearer <token>
Content-Type: application/json

{
  "username": "newuser",
  "email": "user@example.com",
  "password": "SecurePass123!",
  "password2": "SecurePass123!",
  "first_name": "John",
  "last_name": "Doe",
  "role": "EDITOR",
  "organization": "MGLSD"
}
```

#### Get Current User Profile
```http
GET /api/auth/profile/
Authorization: Bearer <token>
```

#### Update Profile
```http
PUT /api/auth/profile/
Authorization: Bearer <token>
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe",
  "email": "newemail@example.com",
  "phone_number": "+256700000000"
}
```

### 2. Posts (Blog/News)

#### List Posts
```http
GET /api/posts/
```

**Query Parameters**:
- `search` - Search in title/content
- `category` - Filter by category slug
- `language` - Filter by language (en, lg, sw)
- `featured` - Show only featured posts (true)
- `page` - Page number
- `ordering` - Order by field (-published_at, views_count)

**Example**:
```http
GET /api/posts/?category=child-protection&language=en&page=1
```

**Response**:
```json
{
  "count": 45,
  "next": "http://localhost:8000/api/posts/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Understanding Child Rights in Uganda",
      "slug": "understanding-child-rights-uganda",
      "excerpt": "Every child has fundamental rights...",
      "author_name": "Jane Doe",
      "category_name": "Child Protection",
      "tags": [
        {"id": 1, "name": "Rights", "slug": "rights"}
      ],
      "featured_image": "/media/posts/images/2025/01/child-rights.jpg",
      "status": "PUBLISHED",
      "language": "en",
      "views_count": 245,
      "is_featured": true,
      "published_at": "2025-01-15T10:30:00Z",
      "created_at": "2025-01-10T08:00:00Z"
    }
  ]
}
```

#### Get Post Detail
```http
GET /api/posts/<slug>/
```

**Response**:
```json
{
  "id": 1,
  "title": "Understanding Child Rights in Uganda",
  "slug": "understanding-child-rights-uganda",
  "content": "<p>Full HTML content here...</p>",
  "excerpt": "Every child has fundamental rights...",
  "author": "Jane Doe (Editor)",
  "category": {
    "id": 1,
    "name": "Child Protection",
    "slug": "child-protection",
    "description": "Resources about child protection"
  },
  "tags": [
    {"id": 1, "name": "Rights", "slug": "rights"}
  ],
  "featured_image": "/media/posts/images/2025/01/child-rights.jpg",
  "status": "PUBLISHED",
  "language": "en",
  "views_count": 246,
  "is_featured": true,
  "published_at": "2025-01-15T10:30:00Z",
  "created_at": "2025-01-10T08:00:00Z",
  "updated_at": "2025-01-16T14:20:00Z"
}
```

#### Create Post (Editors/Admins Only)
```http
POST /api/posts/
Authorization: Bearer <token>
Content-Type: multipart/form-data

{
  "title": "New Child Protection Guidelines",
  "slug": "new-child-protection-guidelines",
  "content": "<p>Full HTML content...</p>",
  "excerpt": "Summary of the new guidelines",
  "category": 1,
  "tags": [1, 2, 3],
  "status": "DRAFT",
  "language": "en",
  "is_featured": false,
  "featured_image": <file>
}
```

#### Update Post
```http
PUT /api/posts/<slug>/
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Updated Title",
  "status": "PUBLISHED"
}
```

#### Delete Post (Admins Only)
```http
DELETE /api/posts/<slug>/
Authorization: Bearer <token>
```

#### List Categories
```http
GET /api/posts/categories/
```

#### List Tags
```http
GET /api/posts/tags/
```

### 3. Resources

#### List Resources
```http
GET /api/resources/
```

**Query Parameters**: Same as Posts (search, category, language, featured, page)

**Response**:
```json
{
  "count": 32,
  "results": [
    {
      "id": 1,
      "title": "Child Protection Policy Guide",
      "slug": "child-protection-policy-guide",
      "description": "Comprehensive guide for implementing child protection policies",
      "category_name": "Policy Documents",
      "file": "/media/resources/files/2025/01/cp-policy-guide.pdf",
      "file_size": 2547896,
      "file_type": "PDF",
      "thumbnail": "/media/resources/thumbnails/cp-guide-thumb.jpg",
      "language": "en",
      "download_count": 145,
      "is_featured": true,
      "published_at": "2025-01-10T09:00:00Z"
    }
  ]
}
```

#### Get Resource Detail
```http
GET /api/resources/<slug>/
```

#### Create Resource (Editors/Admins Only)
```http
POST /api/resources/
Authorization: Bearer <token>
Content-Type: multipart/form-data

{
  "title": "New Policy Document",
  "description": "Description here...",
  "category": 1,
  "file": <file>,
  "thumbnail": <file>,
  "language": "en",
  "is_featured": false
}
```

### 4. FAQs

#### List FAQs
```http
GET /api/faqs/
```

**Query Parameters**: search, category, language, page

**Response**:
```json
{
  "count": 24,
  "results": [
    {
      "id": 1,
      "question": "What is the Sauti helpline number?",
      "answer": "The Sauti helpline operates on the toll-free number 116...",
      "category": 1,
      "category_name": "General Information",
      "language": "en",
      "order": 1,
      "is_active": true,
      "views_count": 532,
      "created_at": "2025-01-05T10:00:00Z",
      "updated_at": "2025-01-15T11:30:00Z"
    }
  ]
}
```

#### Get FAQ Detail
```http
GET /api/faqs/<id>/
```

#### Create FAQ (Editors/Admins Only)
```http
POST /api/faqs/
Authorization: Bearer <token>
Content-Type: application/json

{
  "question": "How do I report a case?",
  "answer": "You can report through multiple channels...",
  "category": 1,
  "language": "en",
  "order": 5,
  "is_active": true
}
```

### 5. Partners

#### List Partners
```http
GET /api/partners/
```

**Query Parameters**: featured

**Response**:
```json
[
  {
    "id": 1,
    "name": "UNICEF Uganda",
    "slug": "unicef-uganda",
    "logo": "/media/partners/logos/unicef-logo.png",
    "website_url": "https://www.unicef.org/uganda/",
    "partner_type": "UN_AGENCY",
    "is_featured": true
  }
]
```

#### Get Partner Detail
```http
GET /api/partners/<slug>/
```

**Response**:
```json
{
  "id": 1,
  "name": "UNICEF Uganda",
  "slug": "unicef-uganda",
  "description": "UNICEF works in Uganda to promote child rights...",
  "partner_type": "UN_AGENCY",
  "logo": "/media/partners/logos/unicef-logo.png",
  "website_url": "https://www.unicef.org/uganda/",
  "email": "kampala@unicef.org",
  "phone": "+256-417-171-001",
  "order": 1,
  "is_active": true,
  "is_featured": true,
  "created_at": "2025-01-01T00:00:00Z",
  "updated_at": "2025-01-10T12:00:00Z"
}
```

### 6. Reports (Anonymous Submission)

#### Submit Report (NO AUTH REQUIRED)
```http
POST /api/reports/
Content-Type: multipart/form-data

{
  "category": "CHILD_PROTECTION",
  "description": "Description of the incident...",
  "is_anonymous": false,
  "contact_name": "John Doe",
  "contact_phone": "+256700000000",
  "contact_email": "john@example.com",
  "location": "Kampala",
  "attachment": <file>
}
```

**Categories**:
- `CHILD_PROTECTION` - Child Protection
- `GBV` - Gender-Based Violence
- `MIGRANT` - Migrant Worker
- `PSEA` - PSEA (Sexual Exploitation & Abuse)

**Response**:
```json
{
  "message": "Report submitted successfully",
  "reference_number": "SAUTI-CH-20250115143025",
  "status": "Your report has been received and will be reviewed by our team."
}
```

#### List Reports (Editors/Admins Only)
```http
GET /api/reports/list/
Authorization: Bearer <token>
```

**Query Parameters**:
- `status` - Filter by status (PENDING, IN_PROGRESS, RESOLVED, CLOSED)
- `category` - Filter by category
- `assigned_to_me` - Show only reports assigned to current user

**Response**:
```json
{
  "count": 15,
  "results": [
    {
      "id": 1,
      "reference_number": "SAUTI-CH-20250115143025",
      "category": "CHILD_PROTECTION",
      "category_display": "Child Protection",
      "status": "PENDING",
      "status_display": "Pending Review",
      "is_anonymous": false,
      "location": "Kampala",
      "assigned_to_name": null,
      "created_at": "2025-01-15T14:30:25Z",
      "updated_at": "2025-01-15T14:30:25Z"
    }
  ]
}
```

#### Get Report Detail (Editors/Admins Only)
```http
GET /api/reports/<id>/
Authorization: Bearer <token>
```

**Response**:
```json
{
  "id": 1,
  "reference_number": "SAUTI-CH-20250115143025",
  "category": "CHILD_PROTECTION",
  "category_display": "Child Protection",
  "description": "Full description of the incident...",
  "is_anonymous": false,
  "contact_name": "John Doe",
  "contact_phone": "+256700000000",
  "contact_email": "john@example.com",
  "location": "Kampala",
  "attachment": "/media/reports/attachments/2025/01/evidence.jpg",
  "status": "PENDING",
  "status_display": "Pending Review",
  "assigned_to": null,
  "notes": "",
  "followups": [],
  "created_at": "2025-01-15T14:30:25Z",
  "updated_at": "2025-01-15T14:30:25Z",
  "resolved_at": null
}
```

#### Update Report Status (Editors/Admins Only)
```http
PATCH /api/reports/<id>/
Authorization: Bearer <token>
Content-Type: application/json

{
  "status": "IN_PROGRESS",
  "assigned_to": 2,
  "notes": "Case assigned to field officer for investigation"
}
```

#### Add Follow-up (Editors/Admins Only)
```http
POST /api/reports/<report_id>/followup/
Authorization: Bearer <token>
Content-Type: application/json

{
  "report": 1,
  "action_taken": "Contacted local authorities and initiated investigation"
}
```

## Error Responses

### 400 Bad Request
```json
{
  "field_name": ["Error message for this field"]
}
```

### 401 Unauthorized
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 403 Forbidden
```json
{
  "detail": "You do not have permission to perform this action."
}
```

### 404 Not Found
```json
{
  "detail": "Not found."
}
```

### 500 Server Error
```json
{
  "detail": "Internal server error."
}
```

## Rate Limiting

No rate limiting is currently implemented, but it's recommended for production deployments.

## Pagination

All list endpoints support pagination:

**Parameters**:
- `page` - Page number (default: 1)
- `page_size` - Items per page (default: 20, max: 100)

**Response Format**:
```json
{
  "count": 150,
  "next": "http://api.example.com/endpoint/?page=2",
  "previous": null,
  "results": [...]
}
```

## Interactive API Documentation

Access the interactive Swagger UI documentation at:

```
http://localhost:8000/api/docs/
```

Or ReDoc format at:

```
http://localhost:8000/api/redoc/
```

## Code Examples

### Python (Requests)

```python
import requests

# Login
response = requests.post(
    'http://localhost:8000/api/auth/login/',
    json={'username': 'admin', 'password': 'password'}
)
token = response.json()['access']

# Get posts
headers = {'Authorization': f'Bearer {token}'}
response = requests.get(
    'http://localhost:8000/api/posts/',
    headers=headers
)
posts = response.json()

# Submit report (anonymous, no auth)
response = requests.post(
    'http://localhost:8000/api/reports/',
    json={
        'category': 'CHILD_PROTECTION',
        'description': 'Report description...',
        'is_anonymous': True
    }
)
print(response.json()['reference_number'])
```

### JavaScript (Fetch)

```javascript
// Login
const login = async () => {
  const response = await fetch('http://localhost:8000/api/auth/login/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({username: 'admin', password: 'password'})
  });
  const data = await response.json();
  return data.access;
};

// Get posts
const getPosts = async (token) => {
  const response = await fetch('http://localhost:8000/api/posts/', {
    headers: {'Authorization': `Bearer ${token}`}
  });
  return await response.json();
};

// Submit report (no auth required)
const submitReport = async (reportData) => {
  const response = await fetch('http://localhost:8000/api/reports/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(reportData)
  });
  return await response.json();
};
```

### cURL

```bash
# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password"}'

# Get posts with token
curl http://localhost:8000/api/posts/ \
  -H "Authorization: Bearer YOUR_TOKEN"

# Submit anonymous report
curl -X POST http://localhost:8000/api/reports/ \
  -H "Content-Type: application/json" \
  -d '{
    "category": "CHILD_PROTECTION",
    "description": "Report description...",
    "is_anonymous": true
  }'
```

---

For support: support@sauti.mglsd.go.ug
