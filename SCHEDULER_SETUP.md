# Content Scheduler Setup Guide

The Sauti CMS now supports scheduled publishing for both blog posts and videos. Content can be created as drafts and scheduled to automatically publish at a future date and time.

## Features

- **Schedule Posts & Videos**: Set a specific date and time for automatic publishing
- **Draft Management**: Scheduled content stays in draft status until the scheduled time
- **Automatic Publishing**: Background job checks and publishes content at the scheduled time
- **Clear Scheduling**: Easy to view and clear scheduled publish times

## How to Use

### 1. Creating Scheduled Content (Admin Dashboard)

**For Blog Posts:**
1. Go to `/posts/create` or edit an existing post
2. Fill in the post details (title, content, images, etc.)
3. In the "Schedule Publishing" section, select a date and time
4. Keep the status as "Draft"
5. Click "Save Draft" or "Update Post"

**For Videos:**
1. Go to `/videos/create` or edit an existing video
2. Fill in the video details (title, description, video source, etc.)
3. In the "Schedule Publishing" section, select a date and time
4. Keep the status as "Draft"
5. Click "Save Changes"

### 2. What Happens Next

- The content remains as a **DRAFT** and is not visible on the public frontend
- At the scheduled time, the background job will:
  - Change the status from DRAFT to PUBLISHED
  - Set the `published_at` timestamp
  - Clear the `scheduled_publish_at` field
  - Make the content visible on the public website

### 3. Viewing Scheduled Content

- Scheduled posts appear in the "Drafts" section with a clock icon
- The scheduled publish time is displayed in the list view
- You can edit or delete scheduled content before it publishes

## Setting Up the Auto-Publisher

### Option 1: Cron Job (Recommended for Production)

Add this line to your crontab to run the publisher every 5 minutes:

```bash
# Edit crontab
crontab -e

# Add this line (adjust paths to match your setup)
*/5 * * * * cd /path/to/cms_website_template/sauti_cms && /path/to/venv/bin/python manage.py publish_scheduled >> /var/log/sauti_scheduler.log 2>&1
```

**For hourly checks:**
```bash
0 * * * * cd /path/to/cms_website_template/sauti_cms && /path/to/venv/bin/python manage.py publish_scheduled >> /var/log/sauti_scheduler.log 2>&1
```

### Option 2: Manual Execution (For Testing)

Run the publisher manually whenever needed:

```bash
cd sauti_cms
source .venv/bin/activate
python manage.py publish_scheduled
```

### Option 3: Systemd Timer (Linux)

Create `/etc/systemd/system/sauti-scheduler.service`:

```ini
[Unit]
Description=Sauti CMS Scheduled Publishing
After=network.target

[Service]
Type=oneshot
User=your_user
WorkingDirectory=/path/to/cms_website_template/sauti_cms
Environment="PATH=/path/to/venv/bin:/usr/bin"
ExecStart=/path/to/venv/bin/python manage.py publish_scheduled
```

Create `/etc/systemd/system/sauti-scheduler.timer`:

```ini
[Unit]
Description=Run Sauti CMS Scheduler every 5 minutes
Requires=sauti-scheduler.service

[Timer]
OnBootSec=5min
OnUnitActiveSec=5min
AccuracySec=1min

[Install]
WantedBy=timers.target
```

Enable and start:
```bash
sudo systemctl enable sauti-scheduler.timer
sudo systemctl start sauti-scheduler.timer
```

### Option 4: Celery (Advanced)

For high-traffic sites, use Celery with periodic tasks:

1. Install Celery and Redis:
```bash
pip install celery redis django-celery-beat
```

2. Configure in `settings.py`:
```python
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_BEAT_SCHEDULE = {
    'publish-scheduled-content': {
        'task': 'posts.tasks.publish_scheduled_content',
        'schedule': 300.0,  # Every 5 minutes
    },
}
```

3. Create `posts/tasks.py`:
```python
from celery import shared_task
from django.core.management import call_command

@shared_task
def publish_scheduled_content():
    call_command('publish_scheduled')
```

4. Run Celery worker and beat:
```bash
celery -A cms worker -l info
celery -A cms beat -l info
```

## Database Schema

### Added Fields

**posts.Post:**
- `scheduled_publish_at` (DateTimeField, nullable) - When to auto-publish the post

**videos.Video:**
- `scheduled_publish_at` (DateTimeField, nullable) - When to auto-publish the video

### Migrations

Run migrations to add the new fields:
```bash
cd sauti_cms
python manage.py migrate
```

## API Changes

### Updated Serializers

Both `PostCreateUpdateSerializer` and `VideoSerializer` now include:
- `scheduled_publish_at` field (ISO 8601 datetime string)

### Example API Request

**Create Scheduled Post:**
```json
{
  "title": "My Scheduled Post",
  "content": "This will publish automatically",
  "status": "DRAFT",
  "scheduled_publish_at": "2025-12-15T14:30:00Z"
}
```

**Create Scheduled Video:**
```json
{
  "title": "My Scheduled Video",
  "description": "This will publish automatically",
  "status": "DRAFT",
  "video_type": "YOUTUBE",
  "youtube_url": "https://youtube.com/watch?v=abc123",
  "scheduled_publish_at": "2025-12-15T14:30:00Z"
}
```

## Monitoring

### Check Scheduled Content

**Via Django Admin:**
```bash
python manage.py shell
```

```python
from posts.models import Post
from videos.models import Video
from django.utils import timezone

# View scheduled posts
scheduled_posts = Post.objects.filter(
    status='DRAFT',
    scheduled_publish_at__isnull=False
)

for post in scheduled_posts:
    print(f"{post.title} - Scheduled for: {post.scheduled_publish_at}")

# View scheduled videos
scheduled_videos = Video.objects.filter(
    status='DRAFT',
    scheduled_publish_at__isnull=False
)

for video in scheduled_videos:
    print(f"{video.title} - Scheduled for: {video.scheduled_publish_at}")
```

### Check Cron Logs

View the scheduler output:
```bash
tail -f /var/log/sauti_scheduler.log
```

## Troubleshooting

### Content Not Publishing

1. **Check cron is running:**
   ```bash
   systemctl status cron  # Linux
   ps aux | grep cron     # Check process
   ```

2. **Run publisher manually:**
   ```bash
   cd sauti_cms
   python manage.py publish_scheduled
   ```

3. **Check timezone settings:**
   - Ensure `TIME_ZONE = 'Africa/Kampala'` in `settings.py`
   - Ensure `USE_TZ = True`

4. **Verify scheduled time:**
   - Check that `scheduled_publish_at` is in the past
   - Check that status is `DRAFT`

### Permission Issues

Ensure the cron user has permissions:
```bash
chmod +x /path/to/cms_website_template/sauti_cms/manage.py
chown -R your_user:your_user /path/to/cms_website_template
```

## Best Practices

1. **Test First**: Always test with manual execution before setting up cron
2. **Monitor Logs**: Keep logs to track what gets published and when
3. **Timezone Awareness**: Use UTC or match server timezone in scheduling
4. **Backup Strategy**: Scheduled content is still in database, backed up normally
5. **Grace Period**: Consider running cron every 5-10 minutes for reliability

## UI Features

### Schedule Publishing Input
- **Date & Time Picker**: HTML5 datetime-local input for easy selection
- **Clear Schedule Button**: Remove scheduling and keep as regular draft
- **Auto-Draft**: When a schedule is set, status automatically becomes DRAFT
- **Visual Indicator**: Clock icon shows scheduled content in lists

### Admin Dashboard
- Scheduled posts visible in Drafts section
- Scheduled time displayed in post/video lists
- Easy editing of scheduled content before publish time

## Security Notes

- Only authenticated users with proper roles can schedule content
- Scheduled content follows same permission rules as manual publishing
- Editors and Admins can schedule content
- Authors can create scheduled drafts but may need approval

## Future Enhancements

Possible improvements for future versions:
- Email notifications when content is published
- Recurring publishing (weekly posts, etc.)
- Bulk scheduling interface
- Calendar view of scheduled content
- Social media auto-posting on publish
- Draft reminders for upcoming scheduled content

---

For questions or issues, check the main README.md or contact the development team.
