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
    description = models.CharField(max_length=255, blank=True, null=True, help_text="Short description of the contact channel")
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


class ContactValue(models.Model):
    """
    Additional values for a Contact item (e.g. a second/third email or
    phone number for the same channel). Contact.value remains the primary
    value for backward compatibility.
    """
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='extra_values')
    value = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.value


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


class WhoWeAreImage(models.Model):
    """Images for the 'Who We Are' hero grid on the About page."""
    POSITION_CHOICES = [
        (1, '1. Left Column - Top (Community)'),
        (2, '2. Left Column - Middle (Helpline)'),
        (3, '3. Left Column - Bottom (Family)'),
        (4, '4. Center Grid - Top Left (Team Photo)'),
        (5, '5. Center Grid - Top Right (Happy Students)'),
        (6, '6. Center Grid - Bottom Left (Action)'),
        (7, '7. Center Grid - Bottom Right (Protection)'),
        (8, '8. Right Column - Top (Operations)'),
        (9, '9. Right Column - Middle (Inclusive)'),
    ]

    position = models.IntegerField(
        choices=POSITION_CHOICES,
        unique=True,
        help_text="Position in the hero grid layout"
    )
    title = models.CharField(
        max_length=100,
        help_text="Short title describing this image (e.g., 'Community Support')"
    )
    image = models.ImageField(
        upload_to='who_we_are/',
        help_text="Image to display in this grid position (recommended: 800x600px)"
    )
    alt_text = models.CharField(
        max_length=200,
        blank=True,
        help_text="Alternative text for accessibility"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this image is displayed on the site"
    )
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
        ordering = ['position']
        verbose_name = 'Who We Are Image'
        verbose_name_plural = 'Who We Are Images'

    def __str__(self):
        return f"{self.get_position_display()} - {self.title}"


class OperationsImage(models.Model):
    """Images for the Operations page sections."""
    POSITION_CHOICES = [
        ('journey_step_1', 'Journey Step 1 - Access'),
        ('journey_step_2', 'Journey Step 2 - Response'),
        ('journey_step_3', 'Journey Step 3 - Management'),
        ('journey_step_4', 'Journey Step 4 - Protection'),
        ('infrastructure', 'Infrastructure Section'),
        ('service_counseling', 'Service - Telephone Counseling'),
        ('service_walkin', 'Service - Walk-In Support'),
        ('service_media', 'Service - Media Response'),
        ('service_guidance', 'Service - Information & Guidance'),
        ('service_referral', 'Service - Essential Service Referrals'),
        ('service_community', 'Service - Community Sensitization'),
        ('service_chatbot', 'Service - MHPSS Chatbot'),
    ]

    position = models.CharField(
        max_length=50,
        choices=POSITION_CHOICES,
        unique=True,
        help_text="Position/section where this image will be displayed"
    )
    title = models.CharField(
        max_length=100,
        help_text="Short title describing this image"
    )
    image = models.ImageField(
        upload_to='operations/',
        help_text="Image to display (recommended: 800x600px for services, 400x500px for journey)"
    )
    alt_text = models.CharField(
        max_length=200,
        blank=True,
        help_text="Alternative text for accessibility"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this image is displayed on the site"
    )
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
        ordering = ['position']
        verbose_name = 'Operations Page Image'
        verbose_name_plural = 'Operations Page Images'

    def __str__(self):
        return f"{self.get_position_display()} - {self.title}"