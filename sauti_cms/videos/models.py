from django.db import models
from django.utils.text import slugify
from django.conf import settings


class VideoCategory(models.Model):
    """Categories for organizing videos"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Video Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Video(models.Model):
    """
    Video content model
    Supports YouTube URLs and file uploads
    """
    
    class Status(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        PUBLISHED = 'PUBLISHED', 'Published'
    
    class Language(models.TextChoices):
        ENGLISH = 'en', 'English'
        LUGANDA = 'lg', 'Luganda'
        SWAHILI = 'sw', 'Swahili'
    
    class VideoType(models.TextChoices):
        YOUTUBE = 'YOUTUBE', 'YouTube Video'
        UPLOAD = 'UPLOAD', 'Uploaded Video'
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    description = models.TextField(help_text='Video description')
    
    # Video source
    video_type = models.CharField(
        max_length=10,
        choices=VideoType.choices,
        default=VideoType.YOUTUBE
    )
    
    # For YouTube videos
    youtube_url = models.URLField(
        blank=True,
        null=True,
        help_text='YouTube video URL (e.g., https://www.youtube.com/watch?v=VIDEO_ID)'
    )
    
    # For uploaded videos
    video_file = models.FileField(
        upload_to='videos/files/%Y/%m/',
        blank=True,
        null=True,
        help_text='Upload video file (MP4, AVI, etc.)'
    )
    
    # Thumbnail
    thumbnail = models.ImageField(
        upload_to='videos/thumbnails/%Y/%m/',
        blank=True,
        null=True,
        help_text='Video thumbnail image'
    )
    
    # Metadata
    duration = models.DurationField(blank=True, null=True, help_text='Video duration')
    file_size = models.IntegerField(null=True, blank=True, help_text='File size in bytes')
    
    # Organization
    category = models.ForeignKey(
        VideoCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='videos'
    )
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='videos'
    )
    
    # Content settings
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT
    )
    
    language = models.CharField(
        max_length=2,
        choices=Language.choices,
        default=Language.ENGLISH
    )
    
    is_featured = models.BooleanField(default=False, help_text='Feature on homepage')
    views_count = models.PositiveIntegerField(default=0)

    # Timestamps
    published_at = models.DateTimeField(null=True, blank=True)
    scheduled_publish_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text='Schedule automatic publishing at this date/time'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['-published_at']),
            models.Index(fields=['status', '-published_at']),
            models.Index(fields=['video_type']),
        ]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        # Auto-set published_at when status changes to PUBLISHED
        if self.status == self.Status.PUBLISHED and not self.published_at:
            from django.utils import timezone
            self.published_at = timezone.now()
        
        super().save(*args, **kwargs)
    
    @property
    def is_published(self):
        return self.status == self.Status.PUBLISHED
    
    @property
    def youtube_id(self):
        """Extract YouTube video ID from URL"""
        if not self.youtube_url:
            return None
        
        import re
        # Match various YouTube URL formats
        patterns = [
            r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)',
            r'youtube\.com\/v\/([^&\n?#]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.youtube_url)
            if match:
                return match.group(1)
        return None
    
    @property
    def youtube_embed_url(self):
        """Get YouTube embed URL"""
        video_id = self.youtube_id
        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return None
    
    @property
    def youtube_thumbnail_url(self):
        """Get YouTube thumbnail URL"""
        video_id = self.youtube_id
        if video_id:
            return f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        return None
