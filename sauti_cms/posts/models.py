from django.db import models
from django.utils.text import slugify
from django.conf import settings
from simple_history.models import HistoricalRecords


class Category(models.Model):
    """Categories for organizing posts"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    """Tags for posts"""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    """
    Blog/News Post model
    Supports draft/published workflow
    """
    
    class Status(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        PUBLISHED = 'PUBLISHED', 'Published'
    
    class Language(models.TextChoices):
        ENGLISH = 'en', 'English'
        LUGANDA = 'lg', 'Luganda'
        SWAHILI = 'sw', 'Swahili'
    
    class PostType(models.TextChoices):
        NEWS = 'NEWS', 'News'
        BLOG = 'BLOG', 'Blog'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    post_type = models.CharField(
        max_length=10,
        choices=PostType.choices,
        default=PostType.NEWS,
        help_text='Type of content: Official News or Blog/Story'
    )
    content = models.TextField(help_text='Rich text content')
    excerpt = models.TextField(max_length=500, blank=True, help_text='Short summary')
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts'
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts'
    )
    
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    
    featured_image = models.ImageField(
        upload_to='posts/images/%Y/%m/',
        blank=True,
        null=True
    )
    
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
    
    views_count = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False, help_text='Feature on homepage')

    published_at = models.DateTimeField(null=True, blank=True)
    scheduled_publish_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text='Schedule automatic publishing at this date/time'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_created'
    )
    last_updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_updated'
    )
    
    history = HistoricalRecords()
    
    class Meta:
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['-published_at']),
            models.Index(fields=['status', '-published_at']),
            models.Index(fields=['post_type', '-published_at']),
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
