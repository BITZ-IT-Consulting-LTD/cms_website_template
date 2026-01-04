from django.db import models
from django.utils.text import slugify
from simple_history.models import HistoricalRecords


class ResourceCategory(models.Model):
    """Categories for resources"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text='Icon class name')
    
    class Meta:
        verbose_name_plural = 'Resource Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Resource(models.Model):
    """
    Downloadable resources (PDFs, docs, guides, toolkits)
    """
    
    class Language(models.TextChoices):
        ENGLISH = 'en', 'English'
        LUGANDA = 'lg', 'Luganda'
        SWAHILI = 'sw', 'Swahili'
    
    class Status(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        PUBLISHED = 'PUBLISHED', 'Published'
        ARCHIVED = 'ARCHIVED', 'Archived'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    description = models.TextField(help_text='Brief description of the resource')
    
    category = models.ForeignKey(
        ResourceCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='resources'
    )
    
    file = models.FileField(
        upload_to='resources/files/%Y/%m/',
        help_text='Upload PDF, DOC, or other document'
    )
    
    file_size = models.IntegerField(null=True, blank=True, help_text='File size in bytes')
    file_type = models.CharField(max_length=10, blank=True, help_text='e.g., PDF, DOC')
    
    thumbnail = models.ImageField(
        upload_to='resources/thumbnails/',
        blank=True,
        null=True
    )
    
    language = models.CharField(
        max_length=2,
        choices=Language.choices,
        default=Language.ENGLISH
    )
    
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PUBLISHED
    )
    
    download_count = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_created'
    )
    last_updated_by = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_updated'
    )
    
    history = HistoricalRecords()
    
    class Meta:
        ordering = ['-published_at']
        indexes = [
            models.Index(fields=['-published_at']),
            models.Index(fields=['category', '-published_at']),
            models.Index(fields=['status', '-published_at']),
        ]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        # Auto-detect file type from filename
        if self.file and not self.file_type:
            self.file_type = self.file.name.split('.')[-1].upper()
        
        # Get file size
        if self.file and not self.file_size:
            self.file_size = self.file.size
        
        super().save(*args, **kwargs)
