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

    # Hero Section
    hero_title = models.CharField(max_length=255, blank=True)
    hero_subtitle = models.TextField(blank=True)
    hero_cta_call = models.CharField(max_length=255, blank=True)
    hero_cta_report = models.CharField(max_length=255, blank=True)

    # Quick Access Section
    quick_access_title = models.CharField(max_length=255, blank=True)
    quick_access_description = models.TextField(blank=True)
    card_report_title = models.CharField(max_length=255, blank=True)
    card_report_text = models.TextField(blank=True)
    card_resources_title = models.CharField(max_length=255, blank=True)
    card_resources_text = models.TextField(blank=True)
    card_faqs_title = models.CharField(max_length=255, blank=True)
    card_faqs_text = models.TextField(blank=True)
    card_partners_title = models.CharField(max_length=255, blank=True)
    card_partners_text = models.TextField(blank=True)

    # Journey Section
    journey_title = models.CharField(max_length=255, blank=True)
    journey_description = models.TextField(blank=True)

    # Publications Section
    publications_title = models.CharField(max_length=255, blank=True)
    publications_description = models.TextField(blank=True)
    publications_link = models.CharField(max_length=255, blank=True)

    # Trust Partners Section
    trust_partners_title = models.CharField(max_length=255, blank=True)
    trust_partners_description = models.TextField(blank=True)

    # Final CTA Section
    final_cta_title = models.CharField(max_length=255, blank=True)
    final_cta_text = models.TextField(blank=True)
    final_cta_call = models.CharField(max_length=255, blank=True)
    final_cta_report = models.CharField(max_length=255, blank=True)
    final_cta_contact = models.CharField(max_length=255, blank=True)

    # Social Media & External Links
    social_facebook = models.URLField(max_length=255, blank=True)
    social_twitter = models.URLField(max_length=255, blank=True)
    social_whatsapp = models.URLField(max_length=255, blank=True)
    social_ureport = models.URLField(max_length=255, blank=True)
    social_safepal = models.URLField(max_length=255, blank=True)

    # Contact Info
    contact_email_info = models.EmailField(max_length=255, blank=True)
    contact_email_sautichl = models.EmailField(max_length=255, blank=True)
    contact_website = models.URLField(max_length=255, blank=True)
    contact_phone_main = models.CharField(max_length=50, blank=True)

    # Resources Page
    resources_title = models.CharField(max_length=255, blank=True)
    resources_subtitle = models.TextField(blank=True)
    resources_stats_title = models.CharField(max_length=255, blank=True)
    resources_stats_updated = models.CharField(max_length=255, blank=True)
    resources_stats_loading = models.CharField(max_length=255, blank=True)
    resources_stats_error = models.CharField(max_length=255, blank=True)
    resources_total_reports = models.CharField(max_length=255, blank=True)
    resources_child_protection = models.CharField(max_length=255, blank=True)
    resources_gbv_cases = models.CharField(max_length=255, blank=True)
    resources_migrant_worker = models.CharField(max_length=255, blank=True)
    resources_cases_by_category = models.CharField(max_length=255, blank=True)
    resources_interactive = models.CharField(max_length=255, blank=True)
    resources_reports_over_time = models.CharField(max_length=255, blank=True)
    resources_last_6_months = models.CharField(max_length=255, blank=True)
    resources_status_distribution = models.CharField(max_length=255, blank=True)
    resources_pending = models.CharField(max_length=255, blank=True)
    resources_in_progress = models.CharField(max_length=255, blank=True)
    resources_resolved = models.CharField(max_length=255, blank=True)
    resources_closed = models.CharField(max_length=255, blank=True)
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


    def save(self, *args, **kwargs):
        if not self.pk and GlobalSettings.objects.exists():
            raise ValidationError('There can be only one GlobalSettings instance.')
        return super(GlobalSettings, self).save(*args, **kwargs)

    def __str__(self):
        return "Global Site Settings"

    class Meta:
        verbose_name = "Global Settings"
        verbose_name_plural = "Global Settings"
