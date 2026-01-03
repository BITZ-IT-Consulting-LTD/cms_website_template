from django.db import models
from django.core.exceptions import ValidationError
from simple_history.models import HistoricalRecords


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
    site_name = models.CharField(max_length=255, default="Sauti 116")
    site_description = models.TextField(blank=True)
    mission = models.TextField(blank=True, help_text="Organization's mission statement.")
    vision = models.TextField(blank=True, help_text="Organization's vision statement.")
    hotline_number = models.CharField(max_length=20, default="116")
    primary_cta_text = models.CharField(max_length=50, default="Get Help Now")

    # Global Contact Text
    hotline_text = models.CharField(max_length=255, blank=True, help_text="Text displayed next to hotline number")
    support_email_text = models.CharField(max_length=255, blank=True)
    operating_hours_text = models.CharField(max_length=255, blank=True)

    # Footer Text
    footer_text = models.TextField(blank=True)
    ministry_attribution_text = models.TextField(blank=True)
    disclaimer_text = models.TextField(blank=True)
    privacy_policy_url = models.URLField(max_length=255, blank=True)
    terms_of_service_url = models.URLField(max_length=255, blank=True, help_text="Link to terms of service page")
    accessibility_url = models.URLField(max_length=255, blank=True, help_text="Link to accessibility statement")

    # SEO Defaults
    default_meta_title_suffix = models.CharField(max_length=255, blank=True)
    default_meta_description = models.TextField(blank=True)

    # Environment Label
    environment_label = models.CharField(max_length=50, blank=True,
                                         help_text="e.g., 'Development', 'Staging', 'Production'.")

    # 1. Hero Section
    hero_title = models.CharField(max_length=255, blank=True)
    hero_subtitle = models.TextField(blank=True)
    hero_value_prop = models.TextField(blank=True, help_text="Short 1-2 line value proposition")
    
    def default_hero_badges():
        return [
            {"label": "24/7 Available", "color": "blue", "is_active": True},
            {"label": "Multiple Languages", "color": "orange", "is_active": True},
            {"label": "Free & Confidential", "color": "teal", "is_active": True}
        ]

    hero_badges = models.JSONField(default=default_hero_badges, blank=True, help_text="List of hero badges. Each badge should have 'label', 'color' (blue, orange, teal), and 'is_active'.")


    # 2. Intro Section (formerly Journey)
    intro_title = models.CharField(max_length=255, blank=True, default="Who We Are")
    intro_description = models.TextField(blank=True, help_text="Short description of who Sauti is and what it does")

    # Services Section (Generic)
    services_title = models.CharField(max_length=255, blank=True, default="How Can We Help?")
    services_description = models.TextField(blank=True)

    # Note: Specific service content is now managed in the HelpService model (services app)

    # 4. Latest News / Blogs (Publications)
    news_title = models.CharField(max_length=255, blank=True, default="Latest News & Stories")
    news_description = models.TextField(blank=True)
    news_link_text = models.CharField(max_length=255, blank=True, default="View All Articles")

    # 5. Partner Logos (Trust Partners)
    partners_title = models.CharField(max_length=255, blank=True, default="Our Partners")
    partners_description = models.TextField(blank=True)

    # Social Media & External Links
    social_facebook = models.URLField(max_length=255, blank=True)
    social_twitter = models.URLField(max_length=255, blank=True)
    social_whatsapp = models.URLField(max_length=255, blank=True)
    social_instagram = models.URLField(max_length=255, blank=True)
    social_linkedin = models.URLField(max_length=255, blank=True)
    social_youtube = models.URLField(max_length=255, blank=True)
    social_tiktok = models.URLField(max_length=255, blank=True)
    social_ureport = models.URLField(max_length=255, blank=True)
    social_safepal = models.URLField(max_length=255, blank=True)

    # Contact Info
    contact_email_info = models.EmailField(max_length=255, blank=True)
    contact_email_sautichl = models.EmailField(max_length=255, blank=True)
    contact_website = models.URLField(max_length=255, blank=True)
    contact_phone_main = models.CharField(max_length=50, blank=True)
    office_address = models.TextField(blank=True, help_text="Physical office address.")

    # Resources Page (Legacy/Specific)
    resources_title = models.CharField(max_length=255, blank=True)
    resources_subtitle = models.TextField(blank=True)
    # ... (other resource fields kept for compatibility)
    resources_stats_title = models.CharField(max_length=255, blank=True)
    resources_stats_updated = models.CharField(max_length=255, blank=True)
    resources_downloads_title = models.CharField(max_length=255, blank=True)
    resources_downloads_subtitle = models.TextField(blank=True)
    resources_available = models.CharField(max_length=255, blank=True)
    resources_search_placeholder = models.CharField(max_length=255, blank=True)
    resources_all_categories = models.CharField(max_length=255, blank=True)
    resources_all_languages = models.CharField(max_length=255, blank=True)
    resources_loading = models.CharField(max_length=255, blank=True)
    resources_coming_soon = models.CharField(max_length=255, blank=True)
    resources_no_results = models.CharField(max_length=255, blank=True)
    resources_no_results_subtitle = models.TextField(blank=True)
    resources_previous = models.CharField(max_length=255, blank=True)
    resources_next = models.CharField(max_length=255, blank=True)

    def default_impact_stats():
        return [
            {"label": "Children Supported", "value": "12,000+", "order": 1, "is_active": True},
            {"label": "Districts Covered", "value": "135", "order": 2, "is_active": True},
            {"label": "Calls Answered", "value": "500K+", "order": 3, "is_active": True},
            {"label": "Partners", "value": "50+", "order": 4, "is_active": True}
        ]

    impact_stats = models.JSONField(default=default_impact_stats, blank=True, help_text="List of impact statistics. Each stat should have 'label', 'value', 'order', and 'is_active'.")

    def default_footer_links():
        return [
            # Navigation
            {"label": "Home", "to": "/", "type": "nav"},
            {"label": "About Us", "to": "/about", "type": "nav"},
            {"label": "Latest News", "to": "/blogs", "type": "nav"},
            {"label": "Resources", "to": "/resources", "type": "nav"},
            {"label": "FAQs", "to": "/faqs", "type": "nav"},
            # Legal
            {"label": "Privacy Policy", "to": "/privacy", "type": "legal"},
            {"label": "Terms of Service", "to": "/terms", "type": "legal"},
            {"label": "Accessibility", "to": "/accessibility", "type": "legal"}
        ]

    footer_links = models.JSONField(default=default_footer_links, blank=True, help_text="List of footer links. Each link should have 'label', 'to' (URL path), and 'type' ('nav' or 'legal').")
    
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if not self.pk and GlobalSettings.objects.exists():
            raise ValidationError('There can be only one GlobalSettings instance.')
        return super(GlobalSettings, self).save(*args, **kwargs)

    def __str__(self):
        return "Global Site Settings"

    class Meta:
        verbose_name = "Global Settings"
        verbose_name_plural = "Global Settings"

class HomePageSettings(GlobalSettings):
    class Meta:
        proxy = True
        verbose_name = "Home Page Settings"
        verbose_name_plural = "Home Page Settings"

class AboutPageSettings(GlobalSettings):
    class Meta:
        proxy = True
        verbose_name = "About Page Settings"
        verbose_name_plural = "About Page Settings"
