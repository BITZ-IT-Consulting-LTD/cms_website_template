from django.db import models
from django.utils.text import slugify
from simple_history.models import HistoricalRecords
import os
import time
import uuid


def partner_logo_path(instance, filename):
    """
    Generate a unique filename for partner logos to ensure cache invalidation.
    Format: partners/logos/name_slug_timestamp_uuid.ext
    """
    ext = filename.split('.')[-1]
    timestamp = int(time.time())
    unique_id = uuid.uuid4().hex[:6]
    slug = instance.slug or slugify(instance.name) or "partner"
    new_filename = f"{slug}_{timestamp}_{unique_id}.{ext}"
    return os.path.join('partners/logos/', new_filename)


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
        upload_to=partner_logo_path,
        blank=True,
        null=True,
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
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            
        # Handle old logo deletion if logo is being updated
        if self.pk:
            try:
                old_instance = Partner.objects.get(pk=self.pk)
                if old_instance.logo and self.logo and old_instance.logo != self.logo:
                    # Delete the old file from storage
                    if os.path.isfile(old_instance.logo.path):
                        os.remove(old_instance.logo.path)
            except Partner.DoesNotExist:
                pass
            except Exception as e:
                # Log or ignore errors related to file deletion (e.g. file not found)
                print(f"Error deleting old logo: {e}")

        super().save(*args, **kwargs)
