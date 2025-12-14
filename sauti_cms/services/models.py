from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the service")
    description = models.TextField(help_text="Detailed description of the service")
    icon = models.CharField(max_length=50, blank=True, null=True, help_text="Name of the icon for the service (e.g., 'phone', 'walk-in')")
    order = models.IntegerField(unique=True, help_text="Order in which the service appears (lower numbers first)")
    is_visible = models.BooleanField(default=True, help_text="Whether this service should be visible")

    class Meta:
        ordering = ['order']
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title
