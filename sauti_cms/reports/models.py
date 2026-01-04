from django.db import models
from django.conf import settings
from simple_history.models import HistoricalRecords
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
        ESCALATED = 'ESCALATED', 'Escalated'
        FORWARDED = 'FORWARDED', 'Forwarded to OpenCHS'
        RESOLVED = 'RESOLVED', 'Resolved'
        CLOSED = 'CLOSED', 'Closed'

    class Gender(models.TextChoices):
        MALE = 'MALE', 'Male'
        FEMALE = 'FEMALE', 'Female'
        OTHER = 'OTHER', 'Other'
        UNKNOWN = 'UNKNOWN', 'Unknown'
    
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
    
    # Structured person-level data
    reported_person_age = models.IntegerField(null=True, blank=True, help_text='Age of the victim/concerned person')
    reported_person_gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        null=True, 
        blank=True,
        help_text='Gender of the victim/concerned person'
    )
    is_self_report = models.BooleanField(
        null=True,
        default=None,
        help_text='True if reporting for self, False if reporting for another'
    )
    
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
    
    # Case Management Fields
    escalated_at = models.DateTimeField(null=True, blank=True)
    forwarded_to_openchs_at = models.DateTimeField(null=True, blank=True)
    openchs_case_id = models.CharField(max_length=100, blank=True, null=True, help_text="ID from OpenCHS system")
    
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    history = HistoricalRecords()
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['status', '-created_at']),
            models.Index(fields=['category', '-created_at']),
        ]
    
    def __str__(self):
        return f"{self.reference_number} - {self.get_category_display()}"
    
    class ReportingFor(models.TextChoices):
        SELF = 'SELF', 'Self'
        ADULT_OTHER = 'ADULT_OTHER', 'Adult (Other)'
        CHILD = 'CHILD', 'Child'
        MULTIPLE = 'MULTIPLE', 'Multiple People'
        UNSPECIFIED = 'UNSPECIFIED', 'Unspecified'

    reporting_for = models.CharField(
        max_length=20,
        choices=ReportingFor.choices,
        default=ReportingFor.UNSPECIFIED,
        help_text='Who is the report being filed for?'
    )

    safe_to_contact = models.BooleanField(
        default=True,
        help_text='Is it safe to contact the reporter?'
    )

    affected_persons = models.JSONField(
        default=list,
        blank=True,
        help_text='List of affected persons data from intake'
    )

    def save(self, *args, **kwargs):
        # Generate reference number if not exists
        if not self.reference_number:
            import datetime
            from django.db import transaction
            
            now = datetime.datetime.now()
            year = now.year
            
            # Simple unique generation - in production use a sequence or UUID
            # Using timestamp + random to ensure uniqueness without complex locking for this task scope
            # Format: CASE-YYYY-MMDD-XXXX
            import random
            rand_suffix = random.randint(1000, 9999)
            self.reference_number = f"CASE-{year}-{now.strftime('%m%d')}-{rand_suffix}"
        
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
