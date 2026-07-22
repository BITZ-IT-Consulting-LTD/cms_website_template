from django.conf import settings
from django.db import models

class FeedbackMessage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    # Archived messages are retained (never hard-deleted) for accountability,
    # but hidden from the default Pending/Reviewed admin views.
    is_archived = models.BooleanField(default=False)
    # Who reviewed the message and when, for accountability/tracking.
    reviewed_at = models.DateTimeField(null=True, blank=True)
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reviewed_feedback'
    )

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = "Feedback Message"
        verbose_name_plural = "Feedback Messages"

    def __str__(self):
        return f"Feedback from {self.name or 'Anonymous'} - {self.submitted_at.strftime('%Y-%m-%d')}"
