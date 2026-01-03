from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the service")
    description = models.TextField(help_text="Detailed description of the service")
    icon = models.CharField(max_length=50, blank=True, null=True, help_text="Name of the icon for the service (e.g., 'phone', 'walk-in')")
    order = models.IntegerField(unique=True, help_text="Order in which the service appears (lower numbers first)")
    is_visible = models.BooleanField(default=True, help_text="Whether this service should be visible")

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

    class Meta:
        ordering = ['order']
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title


class HelpService(models.Model):
    SERVICE_KEYS = [
        ('child-protection', 'Child Protection'),
        ('gbv', 'Gender Based Violence'),
        ('migrants', 'Migrant Workers'),
        ('psea', 'PSEA'),
    ]

    key = models.CharField(max_length=50, choices=SERVICE_KEYS, unique=True, help_text="Unique key for the service URL")
    title = models.CharField(max_length=255)
    intro_text = models.TextField(help_text="Introduction text for the service page")
    scope_items = models.JSONField(default=list, blank=True, help_text="List of items covered by this service (JSON array of strings)")
    
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
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    # New fields for Homepage consolidation
    summary = models.TextField(blank=True, help_text="Short summary for the homepage card")
    icon_name = models.CharField(max_length=50, default="ShieldCheckIcon", help_text="Heroicon name (e.g., UserGroupIcon)")
    homepage_display_order = models.IntegerField(default=0, help_text="Order on the homepage")

    class Meta:
        ordering = ['homepage_display_order', 'order']
        verbose_name = "Help Service"
        verbose_name_plural = "Help Services"

    def __str__(self):
        return self.title


class HelpStep(models.Model):
    service = models.ForeignKey(HelpService, related_name='steps', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    step_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['step_order']
        verbose_name = "Help Step"
        verbose_name_plural = "Help Steps"

    def __str__(self):
        return f"{self.service.title} - Step {self.step_order}"
