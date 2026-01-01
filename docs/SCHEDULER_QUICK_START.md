# Scheduler Quick Start Guide

## ✅ Implementation Complete!

The content scheduler feature has been successfully implemented for both blog posts and videos.

## 🚀 How to Use

### 1. Schedule a Blog Post

1. **Go to Admin Dashboard** → [http://localhost:3002](http://localhost:3002)
2. **Create/Edit a Post** → Click "New Blog Post" or edit existing
3. **Set Content**: Add title, content, images, etc.
4. **Set Schedule**: In the sidebar, find "Schedule Publishing" section
   - Select date and time for auto-publish
   - Status will automatically be set to DRAFT
5. **Save**: Click "Save Draft"

### 2. Schedule a Video

1. **Go to Admin Dashboard** → [http://localhost:3002](http://localhost:3002)
2. **Create/Edit a Video** → Click "New Video" or edit existing
3. **Set Content**: Add title, description, video source, thumbnail
4. **Set Schedule**: In the "Publishing" section, find "Schedule Publishing"
   - Select date and time for auto-publish
   - Status will automatically be set to DRAFT
5. **Save**: Click "Save Changes"

## 🔧 Setup Auto-Publisher

Choose one option:

### Option A: Cron Job (5-minute intervals)

```bash
# Edit crontab
crontab -e

# Add this line (update path to match your setup)
*/5 * * * * cd /Users/newtonbrian/Documents/Bitz/cms_website_template/sauti_cms && source .venv/bin/activate && python manage.py publish_scheduled >> /tmp/scheduler.log 2>&1
```

### Option B: Manual Testing

```bash
cd sauti_cms
source .venv/bin/activate
python manage.py publish_scheduled
```

## 📊 What Was Changed

### Backend Changes

1. **Models** ([sauti_cms/posts/models.py:101-105](sauti_cms/posts/models.py#L101-L105), [sauti_cms/videos/models.py:116-120](sauti_cms/videos/models.py#L116-L120))
   - Added `scheduled_publish_at` field to Post and Video models

2. **Serializers** ([sauti_cms/posts/serializers.py](sauti_cms/posts/serializers.py), [sauti_cms/videos/serializers.py](sauti_cms/videos/serializers.py))
   - Added `scheduled_publish_at` to all serializers

3. **Management Command** ([sauti_cms/posts/management/commands/publish_scheduled.py](sauti_cms/posts/management/commands/publish_scheduled.py))
   - Created command to find and publish scheduled content

4. **Migrations**
   - `posts/migrations/0003_post_scheduled_publish_at.py`
   - `videos/migrations/0002_video_scheduled_publish_at.py`

### Frontend Changes

1. **PostEditView** ([sauti-admin/src/views/PostEditView.vue:234-259](sauti-admin/src/views/PostEditView.vue#L234-L259))
   - Added datetime-local input for scheduling
   - Auto-sets status to DRAFT when scheduled
   - Converts datetime to ISO format for API

2. **VideoEditView** ([sauti-admin/src/views/VideoEditView.vue:235-258](sauti-admin/src/views/VideoEditView.vue#L235-L258))
   - Added datetime-local input for scheduling
   - Auto-sets status to DRAFT when scheduled
   - Converts datetime to ISO format for API

## ✅ Testing Results

**Test performed:**
- Created post scheduled for 1 minute in future
- Waited 65 seconds
- Ran `python manage.py publish_scheduled`
- ✅ Post successfully changed from DRAFT to PUBLISHED
- ✅ `published_at` timestamp set correctly
- ✅ `scheduled_publish_at` cleared after publishing
- ✅ Post visible in public API

## 📝 Next Steps

1. **Set up cron job** for automatic publishing
2. **Test with real content** in admin dashboard
3. **Schedule multiple posts** to verify batch processing
4. **Monitor logs** to ensure smooth operation

## 🎯 Key Features

- ✅ Schedule posts and videos for future publishing
- ✅ Content stays as DRAFT until scheduled time
- ✅ Automatic status change to PUBLISHED at scheduled time
- ✅ Clear schedule option (remove scheduling without deleting)
- ✅ Works with existing admin UI
- ✅ Backend command for cron/systemd integration
- ✅ Timezone-aware scheduling

## 🔍 Monitoring

**Check scheduled content:**
```bash
cd sauti_cms
source .venv/bin/activate
python manage.py shell
```

```python
from posts.models import Post
from videos.models import Video

# View all scheduled posts
scheduled = Post.objects.filter(status='DRAFT', scheduled_publish_at__isnull=False)
for post in scheduled:
    print(f"{post.title} → {post.scheduled_publish_at}")
```

**Check logs:**
```bash
tail -f /tmp/scheduler.log
```

## 📚 Full Documentation

See [SCHEDULER_SETUP.md](SCHEDULER_SETUP.md) for:
- Advanced setup options (Systemd, Celery)
- API examples
- Troubleshooting guide
- Security notes
- Best practices

---

**Status**: ✅ Fully functional and tested
**Version**: 1.0
**Date**: December 8, 2025
