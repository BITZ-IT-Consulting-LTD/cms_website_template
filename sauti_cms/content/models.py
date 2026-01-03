from django.db import models

class SiteContent(models.Model):
    CONTENT_TYPES = (
        ('text', 'Text'),
        ('photo', 'Photo'),
        ('heading', 'Heading'),
        ('button', 'Button'),
        ('video', 'Video'),
        ('icon', 'Icon'),
    )

    PAGES = (
        ('home', 'Home'),
        ('about', 'About'),
        ('operations', 'Operations'),
        ('blog', 'Blog'),
        ('resources', 'Resources'),
        ('faqs', 'FAQs'),
        ('partners', 'Partners'),
        ('contact', 'Contact'),
        ('donate', 'Donate'),
        ('reports', 'Reports'),
        ('header', 'Header'),
        ('footer', 'Footer'),
        ('global', 'Global Settings'),
    )

    key = models.CharField(max_length=100, unique=True, db_index=True, help_text="Unique identifier for this content")
    label = models.CharField(max_length=200, help_text="Human readable label")
    value = models.TextField(help_text="The actual content (text or image URL)")
    type = models.CharField(max_length=20, choices=CONTENT_TYPES, default='text')
    page = models.CharField(max_length=50, choices=PAGES, default='home')
    description = models.TextField(blank=True, null=True, help_text="Description of where this content is used")
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
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

    def __str__(self):
        return f"{self.label} ({self.key})"

    class Meta:
        ordering = ['page', 'key']
        verbose_name = 'Site Content'
        verbose_name_plural = 'Site Content'


class CoreValue(models.Model):
    """Core values displayed on the About page"""
    title = models.CharField(max_length=100, help_text="Value title (e.g., Confidentiality)")
    description = models.TextField(help_text="Description of this core value")
    icon = models.CharField(
        max_length=50,
        help_text="Icon name or SVG path identifier",
        blank=True,
        null=True
    )
    color_from = models.CharField(
        max_length=20,
        default='blue-500',
        help_text="Tailwind gradient start color (e.g., blue-500)"
    )
    color_to = models.CharField(
        max_length=20,
        default='blue-600',
        help_text="Tailwind gradient end color (e.g., blue-600)"
    )
    border_color = models.CharField(
        max_length=20,
        default='blue-100',
        help_text="Tailwind border color (e.g., blue-100)"
    )
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    is_active = models.BooleanField(default=True, help_text="Show this value on the site")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Core Value'
        verbose_name_plural = 'Core Values'


class TimelineEvent(models.Model):
    """Events for the 'Our Journey' timeline on the About page."""
    title = models.CharField(max_length=200, help_text="Title of the timeline event")
    description = models.TextField(help_text="Detailed description of the event")
    date = models.DateField(help_text="Date of the event")
    icon = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Icon name (e.g., Heroicon name) for this event"
    )
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    is_active = models.BooleanField(default=True, help_text="Whether this event is visible on the site")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'order']
        verbose_name = 'Timeline Event'
        verbose_name_plural = 'Timeline Events'

    def __str__(self):
        return f"{self.title} ({self.date.year})"


class Contact(models.Model):
    """Contact information for the website"""
    CONTACT_TYPES = (
        ('phone', 'Phone Number'),
        ('email', 'Email Address'),
        ('location', 'Physical Location'),
        ('social', 'Social Media Link'),
        ('other', 'Other'),
    )

    name = models.CharField(max_length=100, help_text="Name of the contact item (e.g., 'Emergency Hotline', 'WhatsApp')")
    value = models.CharField(max_length=255, help_text="The contact detail (e.g., '116', 'info@example.com', 'Street Address')")
    type = models.CharField(max_length=20, choices=CONTACT_TYPES, default='phone', help_text="Type of contact information")
    icon = models.CharField(max_length=50, blank=True, null=True, help_text="Name of the icon for the contact (e.g., 'phone', 'envelope', 'location-marker')")
    order = models.IntegerField(default=0, help_text="Order in which the contact item appears")
    is_visible = models.BooleanField(default=True, help_text="Whether this contact item should be visible on the site")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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

    def __str__(self):
        return f"{self.name}: {self.value}"

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Contact Item'
        verbose_name_plural = 'Contact Items'


class ProtectionApproach(models.Model):
    """Sections detailing the organization's protection approach."""
    title = models.CharField(max_length=200, help_text="Title of the approach section or step")
    description = models.TextField(help_text="Detailed description of this approach section")
    icon = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Icon name (e.g., Heroicon name) for this approach section"
    )
    color = models.CharField(
        max_length=20,
        default='blue',
        help_text="Tailwind color class for styling (e.g., blue, teal, orange)"
    )
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    is_active = models.BooleanField(default=True, help_text="Whether this approach section is visible on the site")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
        ordering = ['order', 'title']
        verbose_name = 'Protection Approach'
        verbose_name_plural = 'Protection Approaches'

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    """Information about a team member."""
    name = models.CharField(max_length=100, help_text="Full name of the team member")
    role = models.CharField(max_length=100, help_text="Role or title of the team member")
    bio = models.TextField(blank=True, null=True, help_text="Short biography of the team member")
    image = models.ImageField(
        upload_to='team_members/',
        blank=True,
        null=True,
        help_text="Profile image of the team member"
    )
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    is_active = models.BooleanField(default=True, help_text="Whether this team member is visible on the site")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
        ordering = ['order', 'name']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return f"{self.name} ({self.role})"