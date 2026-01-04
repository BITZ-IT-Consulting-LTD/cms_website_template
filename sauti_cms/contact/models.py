from django.db import models

class FeedbackMessage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = "Feedback Message"
        verbose_name_plural = "Feedback Messages"

    def __str__(self):
        return f"Feedback from {self.name or 'Anonymous'} - {self.submitted_at.strftime('%Y-%m-%d')}"
