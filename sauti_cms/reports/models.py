from django.db import models
from django.conf import settings
import base64


class Report(models.Model):
    """
    Case reporting system for child protection, GBV, migrants, PSEA
    Supports anonymous reporting with encrypted storage
    """
    
    class Category(models.TextChoices):
        CHILD_PROTECTION = 'CHILD_PROTECTION', 'Child Protection'
        GBV = 'GBV', 'Gender-Based Violence'
        MIGRANT = 'MIGRANT', 'Migrant Worker'
        PSEA = 'PSEA', 'PSEA (Sexual Exploitation & Abuse)'
    
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending Review'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        RESOLVED = 'RESOLVED', 'Resolved'
        CLOSED = 'CLOSED', 'Closed'
    
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        help_text='Type of report'
    )
    
    description = models.TextField(help_text='Description of the incident/case')
    
    # Encrypted description storage (optional - for sensitive data)
    encrypted_description = models.TextField(blank=True, help_text='Encrypted version')
    
    is_anonymous = models.BooleanField(
        default=False,
        help_text='Report submitted anonymously'
    )
    
    # Optional contact information (if not anonymous)
    contact_name = models.CharField(max_length=200, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_email = models.EmailField(blank=True)
    location = models.CharField(max_length=200, blank=True, help_text='District/location')
    
    attachment = models.FileField(
        upload_to='reports/attachments/%Y/%m/',
        blank=True,
        null=True,
        help_text='Optional evidence file'
    )
    
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.PENDING
    )
    
    # Internal tracking
    reference_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        help_text='Auto-generated reference number'
    )
    
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_reports'
    )
    
    notes = models.TextField(blank=True, help_text='Internal notes (not visible to reporter)')
    
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['status', '-created_at']),
            models.Index(fields=['category', '-created_at']),
        ]
    
    def __str__(self):
        return f"{self.reference_number} - {self.get_category_display()}"
    
    def save(self, *args, **kwargs):
        # Generate reference number if not exists
        if not self.reference_number:
            import datetime
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            category_code = self.category[:2]
            self.reference_number = f"SAUTI-{category_code}-{timestamp}"
        
        # Encrypt description if encryption key is available
        if self.description and settings.ENCRYPTION_KEY and not self.encrypted_description:
            try:
                from cryptography.fernet import Fernet
                f = Fernet(settings.ENCRYPTION_KEY.encode())
                encrypted = f.encrypt(self.description.encode())
                self.encrypted_description = base64.b64encode(encrypted).decode()
            except Exception:
                pass  # Fail silently if encryption fails
        
        super().save(*args, **kwargs)
    
    def decrypt_description(self):
        """Decrypt the description if encrypted"""
        if self.encrypted_description and settings.ENCRYPTION_KEY:
            try:
                from cryptography.fernet import Fernet
                f = Fernet(settings.ENCRYPTION_KEY.encode())
                encrypted = base64.b64decode(self.encrypted_description.encode())
                return f.decrypt(encrypted).decode()
            except Exception:
                return self.description
        return self.description


class ReportFollowUp(models.Model):
    """
    Follow-up actions and communication for reports
    """
    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        related_name='followups'
    )
    
    action_taken = models.TextField(help_text='Description of action taken')
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Report Follow-up'
        verbose_name_plural = 'Report Follow-ups'
    
    def __str__(self):
        return f"Follow-up for {self.report.reference_number}"
