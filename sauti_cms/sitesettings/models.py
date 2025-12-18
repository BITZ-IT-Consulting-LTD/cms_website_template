from django.db import models
from django.core.exceptions import ValidationError


# DEPRECATED: This model is deprecated and will be removed in a future version.
# The new GlobalSettings model should be used instead.
class SiteSetting(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home Page'),
        ('about', 'About Page'),
        ('contact', 'Contact Page'),
        # Add more pages as needed
    ]

    page = models.CharField(max_length=50, choices=PAGE_CHOICES, default='home',
                            help_text="The page this setting belongs to.")
    key = models.CharField(max_length=255,
                           help_text="Unique identifier for the setting (e.g., 'hero_title').")
    value = models.TextField(blank=True,
                             help_text="The configurable content for this setting.")
    description = models.TextField(blank=True,
                                   help_text="A brief explanation of what this setting controls.")
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Setting (Deprecated)"
        verbose_name_plural = "Site Settings (Deprecated)"
        ordering = ['page', 'key']
        unique_together = ('page', 'key') # Ensure unique key per page

    def __str__(self):
        return f"{self.get_page_display()} - {self.key}"


class GlobalSettings(models.Model):
    """
    A singleton model to store global site settings.
    """
    # Site Identity
    site_name = models.CharField(max_length=255, default="Sauti")
    site_description = models.TextField(blank=True)

    # Global Contact Text
    hotline_text = models.CharField(max_length=255, blank=True)
    support_email_text = models.CharField(max_length=255, blank=True)
    operating_hours_text = models.CharField(max_length=255, blank=True)

    # Footer Text
    footer_text = models.TextField(blank=True)
    ministry_attribution_text = models.TextField(blank=True)
    disclaimer_text = models.TextField(blank=True)

    # SEO Defaults
    default_meta_title_suffix = models.CharField(max_length=255, blank=True)
    default_meta_description = models.TextField(blank=True)

    # Environment Label
    environment_label = models.CharField(max_length=50, blank=True,
                                         help_text="e.g., 'Development', 'Staging', 'Production'. Will be displayed in the admin UI.")

    def save(self, *args, **kwargs):
        if not self.pk and GlobalSettings.objects.exists():
            raise ValidationError('There can be only one GlobalSettings instance.')
        return super(GlobalSettings, self).save(*args, **kwargs)

    def __str__(self):
        return "Global Site Settings"

    class Meta:
        verbose_name = "Global Settings"
        verbose_name_plural = "Global Settings"
