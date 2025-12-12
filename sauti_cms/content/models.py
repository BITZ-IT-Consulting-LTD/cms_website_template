from django.db import models

class SiteContent(models.Model):
    CONTENT_TYPES = (
        ('text', 'Text'),
        ('photo', 'Photo'),
        ('heading', 'Heading'),
        ('button', 'Button'),
        ('video', 'Video'),
        ('icon', 'Icon'),
    )

    PAGES = (
        ('home', 'Home'),
        ('about', 'About'),
        ('operations', 'Operations'),
        ('blog', 'Blog'),
        ('resources', 'Resources'),
        ('faqs', 'FAQs'),
        ('partners', 'Partners'),
        ('contact', 'Contact'),
        ('donate', 'Donate'),
        ('reports', 'Reports'),
        ('header', 'Header'),
        ('footer', 'Footer'),
    )

    key = models.CharField(max_length=100, unique=True, db_index=True, help_text="Unique identifier for this content")
    label = models.CharField(max_length=200, help_text="Human readable label")
    value = models.TextField(help_text="The actual content (text or image URL)")
    type = models.CharField(max_length=20, choices=CONTENT_TYPES, default='text')
    page = models.CharField(max_length=50, choices=PAGES, default='home')
    description = models.TextField(blank=True, null=True, help_text="Description of where this content is used")
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.label} ({self.key})"

    class Meta:
        ordering = ['page', 'key']
        verbose_name = 'Site Content'
        verbose_name_plural = 'Site Content'


class CoreValue(models.Model):
    """Core values displayed on the About page"""
    title = models.CharField(max_length=100, help_text="Value title (e.g., Confidentiality)")
    description = models.TextField(help_text="Description of this core value")
    icon = models.CharField(
        max_length=50,
        help_text="Icon name or SVG path identifier",
        blank=True,
        null=True
    )
    color_from = models.CharField(
        max_length=20,
        default='blue-500',
        help_text="Tailwind gradient start color (e.g., blue-500)"
    )
    color_to = models.CharField(
        max_length=20,
        default='blue-600',
        help_text="Tailwind gradient end color (e.g., blue-600)"
    )
    border_color = models.CharField(
        max_length=20,
        default='blue-100',
        help_text="Tailwind border color (e.g., blue-100)"
    )
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    is_active = models.BooleanField(default=True, help_text="Show this value on the site")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Core Value'
        verbose_name_plural = 'Core Values'
