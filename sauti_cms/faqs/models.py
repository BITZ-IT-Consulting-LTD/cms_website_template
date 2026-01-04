from django.db import models
from django.utils.text import slugify
from simple_history.models import HistoricalRecords


class FAQCategory(models.Model):
    """Categories for organizing FAQs"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0, help_text='Display order')
    
    class Meta:
        verbose_name = 'FAQ Category'
        verbose_name_plural = 'FAQ Categories'
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class FAQ(models.Model):
    """
    Frequently Asked Questions
    """
    
    class Language(models.TextChoices):
        ENGLISH = 'en', 'English'
        LUGANDA = 'lg', 'Luganda'
        SWAHILI = 'sw', 'Swahili'
    
    class Status(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        PUBLISHED = 'PUBLISHED', 'Published'
        ARCHIVED = 'ARCHIVED', 'Archived'

    question = models.CharField(max_length=500)
    answer = models.TextField()
    
    category = models.ForeignKey(
        FAQCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='faqs'
    )
    
    language = models.CharField(
        max_length=2,
        choices=Language.choices,
        default=Language.ENGLISH
    )
    
    order = models.PositiveIntegerField(default=0, help_text='Display order within category')
    is_active = models.BooleanField(default=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PUBLISHED
    )
    views_count = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
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
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['category', 'order', 'question']
        indexes = [
            models.Index(fields=['category', 'order']),
            models.Index(fields=['is_active', 'language']),
            models.Index(fields=['status', 'language']),
        ]
    
    def __str__(self):
        return self.question[:100]
