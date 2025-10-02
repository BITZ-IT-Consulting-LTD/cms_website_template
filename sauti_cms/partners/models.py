from django.db import models
from django.utils.text import slugify


class Partner(models.Model):
    """
    Partner organizations (MGLSD, UNICEF, SOS, etc.)
    """
    
    class PartnerType(models.TextChoices):
        GOVERNMENT = 'GOVERNMENT', 'Government Agency'
        UN_AGENCY = 'UN_AGENCY', 'UN Agency'
        NGO = 'NGO', 'NGO/CSO'
        PRIVATE = 'PRIVATE', 'Private Sector'
        OTHER = 'OTHER', 'Other'
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True)
    
    partner_type = models.CharField(
        max_length=15,
        choices=PartnerType.choices,
        default=PartnerType.NGO
    )
    
    logo = models.ImageField(
        upload_to='partners/logos/',
        help_text='Partner logo'
    )
    
    website_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    
    order = models.PositiveIntegerField(default=0, help_text='Display order')
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False, help_text='Show on homepage')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
