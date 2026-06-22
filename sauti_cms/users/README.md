# Users Application

Manages user authentication, authorization, and role-based access control for the Sauti 116 CMS.

## Overview

This Django app provides:
- Custom user model with role-based access control
- JWT and Token-based authentication
- User registration and profile management
- Role-based permissions (Admin, Editor, Author, Viewer)
- User profile endpoints

## Models

### User (Custom)
**Purpose**: Custom user model extending Django's AbstractUser
**Fields**:
- `username` - Unique username
- `email` - User email address
- `password` - Hashed password
- `first_name` - User's first name
- `last_name` - User's last name
- `role` - User role (ADMIN, EDITOR, AUTHOR, VIEWER)
- `organization` - User's organization
- `phone_number` - Contact phone
- `is_active` - Account active status
- `is_staff` - Django staff status
- `created_at` - Account creation timestamp
- `updated_at` - Last modified timestamp

## User Roles

### ADMIN
**Permissions**:
- Full system access
- All CRUD operations
- User management
- Delete any content
- View and manage reports
- Access admin panel
- System settings configuration

### EDITOR
**Permissions**:
- Create, read, update content (posts, resources, FAQs)
- Cannot delete content
- Publish/unpublish posts
- Manage categories and tags
- View and manage reports
- Cannot access user management

### AUTHOR
**Permissions**:
- Create blog posts (as drafts)
- Edit own posts
- Cannot publish without approval
- Cannot delete posts
- Cannot manage content types
- Limited report access

### VIEWER
**Permissions**:
- Read-only access
- View published content
- View reports (read-only)
- Cannot create or edit content

## API Endpoints

### User Registration
```
POST /api/users/register/
```

**Required Fields**:
```json
{
  "username": "newuser",
  "email": "user@example.com",
  "password": "secure_password",
  "password2": "secure_password",
  "first_name": "John",
  "last_name": "Doe"
}
```

**Response**: User object with token

**Allowed for**: Admins only

### User Login
```
POST /api/auth/login/
```

**Request**:
```json
{
  "username": "user",
  "password": "password"
}
```

**Response**:
```json
{
  "token": "abc123xyz...",
  "user": {
    "id": 1,
    "username": "user",
    "email": "user@example.com",
    "role": "EDITOR",
    "first_name": "John",
    "last_name": "Doe"
  }
}
```

### Get User Profile
```
GET /api/auth/profile/
Authorization: Token {user_token}
```

**Response**: Current user's profile object

### Update User Profile
```
PUT /api/auth/profile/
Authorization: Token {user_token}
```

**Request**:
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "organization": "Organization Name",
  "phone_number": "+256701234567"
}
```

### List Users (Admin Only)
```
GET /api/users/
Authorization: Token {admin_token}
```

**Query Parameters**:
- `search=name` - Search by username/email
- `role=EDITOR` - Filter by role
- `is_active=true` - Filter by status

### Get User Detail (Admin Only)
```
GET /api/users/{id}/
Authorization: Token {admin_token}
```

### Update User (Admin Only)
```
PUT /api/users/{id}/
Authorization: Token {admin_token}
```

### Delete User (Admin Only)
```
DELETE /api/users/{id}/
Authorization: Token {admin_token}
```

### Change Password
```
POST /api/auth/change-password/
Authorization: Token {user_token}
```

**Request**:
```json
{
  "old_password": "current_password",
  "new_password": "new_password",
  "new_password2": "new_password"
}
```

### Logout
```
POST /api/auth/logout/
Authorization: Token {user_token}
```

## Authentication Methods

### Token-Based Authentication
**Header**: `Authorization: Token abc123xyz`

**Advantages**:
- Stateless
- Simple implementation
- Good for REST APIs

### JWT Authentication
**Header**: `Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...`

**Features**:
- Token expiration
- Refresh token support
- Claims-based authorization

### Session Authentication (Admin Only)
- Cookie-based
- Used for Django admin panel

## File Structure

```
users/
├── migrations/           # Database migrations
├── models.py             # Custom User model
├── serializers.py        # User serializers
├── views.py              # Auth viewsets
├── permissions.py        # Custom permissions
├── admin.py              # Admin interface
├── urls.py               # URL routing
├── apps.py               # App configuration
├── tests.py              # Unit tests
└── README.md             # This file
```

## Admin Interface

Access at `/admin/auth/user/`:
- **Users**: Create, edit, change role, deactivate users
- **User Groups**: Manage permission groups
- **Permissions**: View available permissions

**Features**:
- Filter by role, active status
- Search by username/email
- Change password for users
- Assign roles
- Bulk actions

## Common Tasks

### Create a New User
**Via Admin Panel**:
1. Go to `/admin/auth/user/`
2. Click "Add User"
3. Enter username and password
4. Save user
5. Edit user to set role

**Via API**:
```bash
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Authorization: Token admin_token" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "email": "user@example.com",
    "password": "secure_password",
    "password2": "secure_password",
    "role": "EDITOR"
  }'
```

### Change User Role
```bash
PUT /api/users/{id}/
{
  "role": "EDITOR"
}
```

### Reset User Password
**Via Admin**:
1. Go to `/admin/auth/user/`
2. Click user
3. Click "Change password" link

### Deactivate User
```bash
PUT /api/users/{id}/
{
  "is_active": false
}
```

## Permissions & Access Control

### Custom Permissions
- `posts.add_post` - Create posts
- `posts.change_post` - Edit posts
- `posts.delete_post` - Delete posts
- `reports.view_report` - View reports
- `reports.change_report` - Manage reports

### Role-Based Permissions

```python
# Check user role in views
if user.role == 'ADMIN':
    # Full access
elif user.role == 'EDITOR':
    # Content management
elif user.role == 'AUTHOR':
    # Limited creation
else:
    # Read-only
```

### Decorator Usage
```python
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@permission_classes([IsAuthenticated])
def my_view(request):
    # Only authenticated users
```

## Security Best Practices

### Password Requirements
- Minimum 8 characters
- Mix of letters, numbers, special characters
- Not similar to username/email

### Token Security
- Tokens stored securely (hashed)
- Expiration dates enforced
- Refresh token rotation

### Account Security
- Password hashing with PBKDF2
- Session timeout
- IP address tracking (optional)
- Login attempt limiting (optional)

## Database Schema

### Users Table
```sql
CREATE TABLE users_user (
  id BIGINT PRIMARY KEY,
  username VARCHAR(150) UNIQUE NOT NULL,
  email VARCHAR(254),
  password VARCHAR(128),
  first_name VARCHAR(150),
  last_name VARCHAR(150),
  role VARCHAR(20) DEFAULT 'VIEWER',
  organization VARCHAR(255),
  phone_number VARCHAR(20),
  is_active BOOLEAN DEFAULT True,
  is_staff BOOLEAN DEFAULT False,
  created_at TIMESTAMP AUTO_NOW_ADD,
  updated_at TIMESTAMP AUTO_NOW
);

CREATE TABLE authtoken_token (
  key VARCHAR(40) PRIMARY KEY,
  user_id BIGINT UNIQUE REFERENCES users_user(id),
  created TIMESTAMP AUTO_NOW_ADD
);
```

## Troubleshooting

### Login Fails
**Possible Causes**:
1. Wrong username/password
2. User account is deactivated (is_active=False)
3. User doesn't exist

**Check**:
```bash
python manage.py shell
from users.models import User
User.objects.filter(username='user').values('is_active')
```

### Token Invalid
1. Token expired
2. Token revoked
3. User deactivated

**Solution**:
- Login again to get new token
- Check token expiration in settings

### Permission Denied
1. Insufficient role permissions
2. Authentication token missing
3. Token invalid or expired

**Solution**:
- Check user role
- Include Authorization header
- Use valid token

### Email Not Sending
1. Email configuration in .env incorrect
2. SMTP server not accessible
3. Email validation failing

## Performance Optimization

### Query Optimization
- Cache user profile lookups
- Use select_related() for related objects

### Caching
- Cache user permissions
- Cache role-based access lists

## Testing

### Run Tests
```bash
python manage.py test users
```

### Test Coverage
```bash
coverage run --source='users' manage.py test users
coverage report
```

## Related Documentation

- [Main CMS README](../README.md)
- [API Documentation](../API_DOCUMENTATION.md)
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Authentication](https://www.django-rest-framework.org/api-guide/authentication/)

## Support

For authentication and user management issues, refer to:
- Django authentication documentation
- API documentation
- Django REST Framework auth guide
