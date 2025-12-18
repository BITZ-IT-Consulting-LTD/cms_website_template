from django.db import models

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
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"
        ordering = ['page', 'key']
        unique_together = ('page', 'key') # Ensure unique key per page

    def __str__(self):
        return f"{self.get_page_display()} - {self.key}"
