from django.db import models
from simple_history.models import HistoricalRecords

class TimelineEvent(models.Model):
    year = models.CharField(max_length=10, help_text="Year or specific date of the event (e.g., '2013', 'Aug 2013')")
    title = models.CharField(max_length=255, help_text="Title of the timeline event")
    description = models.TextField(help_text="Detailed description of the event")
    order = models.IntegerField(unique=True, help_text="Order in which the event appears on the timeline (lower numbers first)")
    is_visible = models.BooleanField(default=True, help_text="Whether this event should be visible on the timeline")

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
        ordering = ['order', 'year']
        verbose_name = "Timeline Event"
        verbose_name_plural = "Timeline Events"

    def __str__(self):
        return f"{self.year} - {self.title}"
