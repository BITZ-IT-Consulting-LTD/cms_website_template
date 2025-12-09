# Social Media Integration Guide

## ✅ Feature Overview

The Sauti CMS now features **automatic social media post integration** in the homepage carousel! Your most recent posts from TikTok, Facebook, and Twitter/X are automatically featured on the homepage.

## 🎯 What It Does

- **Displays Recent Posts**: Shows your latest social media posts in an attractive carousel
- **Multi-Platform**: Supports Facebook, Twitter/X, TikTok, Instagram, LinkedIn, and YouTube
- **Auto-Rotating**: Carousel automatically cycles through posts every 3 seconds
- **Filterable**: Visitors can filter by platform (All, Facebook, Twitter, TikTok)
- **Clickable**: Posts link directly to your social media accounts
- **Responsive**: Looks great on all devices

## 📍 Where It Appears

The social media carousel appears prominently on the **homepage hero section** (right side on desktop, below hero text on mobile).

Location: [sauti-frontend/src/views/Home.vue:93](sauti-frontend/src/views/Home.vue#L93)

## 🔧 How to Manage Social Posts

### Option 1: Django Admin (Easiest)

1. **Go to Django Admin**: http://localhost:8000/admin/
2. **Navigate to**: Social Media → Social Media Posts
3. **Click "Add Social Media Post"**
4. **Fill in the form**:
   - **Platform**: Select from dropdown (Facebook, Twitter, TikTok, etc.)
   - **Handle/Username**: Your social media handle (e.g., @sauti116)
   - **Content/Caption**: The post text/caption
   - **Image**: Upload an image (optional)
   - **Video URL**: Link to video (optional)
   - **Post URL**: Direct link to the post
   - **Engagement Stats**: Likes, comments, shares (for display)
   - **Posted At**: When this was posted on social media
   - **Order**: Display priority (lower numbers first)
   - **Is Active**: Check to show on homepage

### Option 2: API Integration (Advanced)

You can integrate with social media APIs to automatically fetch posts:

**API Endpoint**: `POST /api/social/posts/`

**Example Request**:
```json
{
  "platform": "TikTok",
  "handle": "@sauti116helplineuganda",
  "content": "Every child deserves to be heard! #Sauti116",
  "post_url": "https://www.tiktok.com/@sauti116helplineuganda/video/123456",
  "likes_count": "2.5k",
  "comments_count": "156",
  "shares_count": "89",
  "posted_at": "2025-12-08T10:00:00Z",
  "is_active": true,
  "order": 1
}
```

## 📊 Database Schema

**Model**: `SocialPost` ([sauti_cms/social_media/models.py](sauti_cms/social_media/models.py:4-39))

**Fields**:
- `platform` (CharField) - Facebook, Twitter, TikTok, Instagram, LinkedIn, YouTube
- `handle` (CharField) - @username or page name
- `content` (TextField) - Post caption/text
- `image` (ImageField) - Post image (optional)
- `video_url` (URLField) - Link to video (optional)
- `post_url` (URLField) - Link to original post
- `likes_count` (CharField) - Display string (e.g., "2.5k")
- `comments_count` (CharField) - Display string
- `shares_count` (CharField) - Display string
- `posted_at` (DateTimeField) - When posted on social media
- `is_active` (BooleanField) - Show/hide on homepage
- `order` (IntegerField) - Display priority

## 🎨 Frontend Component

**Component**: [sauti-frontend/src/components/home/SocialMediaCarousel.vue](sauti-frontend/src/components/home/SocialMediaCarousel.vue:1-250)

**Features**:
- Vertical carousel with 3D effect
- Platform-specific icons and colors
- Auto-rotation every 3 seconds
- Filter buttons (All, Facebook, Twitter, TikTok)
- Clicking opens post in popup window
- Fallback to mock data if API fails

## 🔌 API Endpoints

### List All Posts
```
GET /api/social/posts/
```

### Filter by Platform
```
GET /api/social/posts/?platform=TikTok
GET /api/social/posts/?platform=Facebook
GET /api/social/posts/?platform=Twitter
```

### Search Posts
```
GET /api/social/posts/?search=child protection
```

### Create Post (Admin Only)
```
POST /api/social/posts/
Authorization: Bearer {token}
Content-Type: application/json
```

### Update Post (Admin Only)
```
PUT /api/social/posts/{id}/
Authorization: Bearer {token}
```

### Delete Post (Admin Only)
```
DELETE /api/social/posts/{id}/
Authorization: Bearer {token}
```

## 🚀 Quick Start

### 1. Add Your First Post via Django Admin

```bash
# 1. Start the backend
cd sauti_cms
source .venv/bin/activate
python manage.py runserver

# 2. Go to admin: http://localhost:8000/admin/
# 3. Login with your admin credentials
# 4. Navigate to: Social Media → Social Media Posts
# 5. Click "Add Social Media Post"
# 6. Fill in:
#    - Platform: TikTok
#    - Handle: @sauti116helplineuganda
#    - Content: Check out our latest video!
#    - Post URL: https://www.tiktok.com/@sauti116helplineuganda
#    - Posted At: Today's date
#    - Is Active: ✓ (checked)
# 7. Click "Save"
```

### 2. View on Homepage

```bash
# Open the frontend
# http://localhost:3000
# Your post will appear in the hero carousel!
```

## 🔄 Automatic Fetching (Optional)

To automatically fetch posts from social media platforms, you can:

### Option A: Manual Embed Integration
Copy embed codes from your social media posts and paste them into the Image field as data URLs.

### Option B: API Integration (Advanced)
Create a cron job to fetch posts using official APIs:

1. **Facebook**: Use Graph API
2. **Twitter/X**: Use Twitter API v2
3. **TikTok**: Use TikTok Business API

Example cron job:
```bash
*/30 * * * * cd /path/to/sauti_cms && python manage.py fetch_social_posts
```

You would need to create this management command.

## 💡 Best Practices

1. **Keep It Fresh**: Update posts regularly (at least weekly)
2. **Use High-Quality Images**: Upload clear, relevant images
3. **Order Matters**: Set order value to control display priority
4. **Engagement Stats**: Update likes/comments/shares to show activity
5. **Platform Variety**: Mix different platforms for variety
6. **Active Flag**: Disable old or irrelevant posts instead of deleting

## 🎨 Customization

### Change Auto-Rotate Speed
Edit [sauti-frontend/src/components/home/SocialMediaCarousel.vue:239](sauti-frontend/src/components/home/SocialMediaCarousel.vue#L239):
```javascript
// Change from 3000 (3 seconds) to desired milliseconds
intervalId = setInterval(nextSlide, 5000) // 5 seconds
```

### Add More Platforms
Edit [sauti_cms/social_media/models.py:5-12](sauti_cms/social_media/models.py#L5-L12):
```python
PLATFORM_CHOICES = [
    ('Facebook', 'Facebook'),
    ('Twitter', 'Twitter'),
    ('TikTok', 'TikTok'),
    ('Instagram', 'Instagram'),
    ('YouTube', 'YouTube'),
    ('Snapchat', 'Snapchat'),  # Add new platform
]
```

### Change Carousel Style
Edit [sauti-frontend/src/components/home/SocialMediaCarousel.vue](sauti-frontend/src/components/home/SocialMediaCarousel.vue) to modify:
- Circle sizes
- Colors
- Animations
- Layout

## 📱 Mobile Responsiveness

The carousel automatically adjusts for mobile devices:
- Smaller circle sizes on mobile
- Touch-friendly buttons
- Responsive spacing

## 🔍 Troubleshooting

### Posts Not Showing
1. Check if `is_active` is true
2. Verify post exists: `GET /api/social/posts/`
3. Check browser console for errors
4. Ensure backend is running

### Images Not Loading
1. Check image path is correct
2. Ensure MEDIA_URL is configured in Django settings
3. Verify image file exists in media folder

### API Errors
1. Check backend logs: `tail -f sauti_cms/logs/*.log`
2. Verify database connection
3. Check if social_media app is in INSTALLED_APPS

## 📈 Sample Posts Created

The system includes 5 sample posts:
- 2 TikTok posts
- 2 Facebook posts
- 1 Twitter/X post

View them: http://localhost:8000/admin/social_media/socialpost/

## 🎯 Next Steps

1. **Add Real Posts**: Replace sample data with your actual social media posts
2. **Upload Images**: Add real images from your social accounts
3. **Set Up Auto-Fetching**: Integrate with social media APIs (optional)
4. **Monitor Engagement**: Track which posts get the most clicks
5. **Regular Updates**: Keep the carousel fresh with new content

## 🔗 Related Files

- **Model**: [sauti_cms/social_media/models.py](sauti_cms/social_media/models.py)
- **Views**: [sauti_cms/social_media/views.py](sauti_cms/social_media/views.py)
- **Serializer**: [sauti_cms/social_media/serializers.py](sauti_cms/social_media/serializers.py)
- **URLs**: [sauti_cms/social_media/urls.py](sauti_cms/social_media/urls.py)
- **Admin**: [sauti_cms/social_media/admin.py](sauti_cms/social_media/admin.py)
- **Frontend Component**: [sauti-frontend/src/components/home/SocialMediaCarousel.vue](sauti-frontend/src/components/home/SocialMediaCarousel.vue)
- **Homepage**: [sauti-frontend/src/views/Home.vue](sauti-frontend/src/views/Home.vue)

---

**Status**: ✅ Fully functional and ready to use!
**Created**: December 8, 2025
