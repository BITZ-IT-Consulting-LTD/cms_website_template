from django.db import models
from django.utils.translation import gettext_lazy as _

class SocialPost(models.Model):
    PLATFORM_CHOICES = [
        ('Facebook', 'Facebook'),
        ('Twitter (X)', 'Twitter (X)'),
        ('TikTok', 'TikTok'),
        ('Instagram', 'Instagram'),
        ('LinkedIn', 'LinkedIn'),
        ('YouTube', 'YouTube'),
    ]

    platform = models.CharField(_('Platform'), max_length=50, choices=PLATFORM_CHOICES)
    handle = models.CharField(_('Handle/Username'), max_length=100, help_text=_('e.g. @sauti116'))
    content = models.TextField(_('Content/Caption'), blank=True)
    image = models.ImageField(_('Image'), upload_to='social_media/', blank=True, null=True)
    video_url = models.URLField(_('Video URL'), blank=True, null=True, help_text=_('Optional link to video'))
    post_url = models.URLField(_('Post URL'), blank=True, null=True, help_text=_('Link to the original post'))

    likes_count = models.CharField(_('Likes Count'), max_length=20, default='0', help_text=_('e.g. 1.2k'))
    comments_count = models.CharField(_('Comments Count'), max_length=20, default='0', help_text=_('e.g. 45'))
    shares_count = models.CharField(_('Shares Count'), max_length=20, default='0', help_text=_('e.g. 12'))

    posted_at = models.DateTimeField(_('Posted At'), help_text=_('When was this posted on social media?'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text=_('Order in carousel'))

    class Meta:
        ordering = ['order', '-posted_at']
        verbose_name = _('Social Media Post')
        verbose_name_plural = _('Social Media Posts')

    def __str__(self):
        return f"{self.platform} - {self.handle} ({self.posted_at.strftime('%Y-%m-%d')})"


class SocialMediaChannels(models.Model):
    """Simple model to store 4 social media links that are displayed on the homepage"""

    channel_1_url = models.URLField(
        _('Channel 1 URL'),
        blank=True,
        null=True,
        help_text=_('Paste the link to your first social media post (TikTok, YouTube, Twitter, etc.)')
    )

    channel_2_url = models.URLField(
        _('Channel 2 URL'),
        blank=True,
        null=True,
        help_text=_('Paste the link to your second social media post')
    )

    channel_3_url = models.URLField(
        _('Channel 3 URL'),
        blank=True,
        null=True,
        help_text=_('Paste the link to your third social media post')
    )

    channel_4_url = models.URLField(
        _('Channel 4 URL'),
        blank=True,
        null=True,
        help_text=_('Paste the link to your fourth social media post')
    )

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Social Media Channels')
        verbose_name_plural = _('Social Media Channels')

    def __str__(self):
        return f"Social Media Channels (Updated: {self.updated_at.strftime('%Y-%m-%d %H:%M')})"

    @classmethod
    def get_channels(cls):
        """Get or create the single instance of social media channels"""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class ContactInformation(models.Model):
    """Store contact information displayed across the frontend"""

    # Email addresses
    primary_email = models.EmailField(
        _('Primary Email'),
        blank=True,
        null=True,
        help_text=_('Main contact email (e.g., info@sauti.org)')
    )

    support_email = models.EmailField(
        _('Support Email'),
        blank=True,
        null=True,
        help_text=_('Support/help email (e.g., support@sauti.org)')
    )

    # Phone numbers
    primary_phone = models.CharField(
        _('Primary Phone'),
        max_length=50,
        blank=True,
        null=True,
        help_text=_('Main contact phone (e.g., +256 116 or 116)')
    )

    whatsapp_number = models.CharField(
        _('WhatsApp Number'),
        max_length=50,
        blank=True,
        null=True,
        help_text=_('WhatsApp contact number')
    )

    # Physical address
    office_address = models.TextField(
        _('Office Address'),
        blank=True,
        null=True,
        help_text=_('Physical office address')
    )

    # DEPRECATED: These social media links are now governed by GlobalSettings.
    # Use sitesettings.GlobalSettings for authoritative configuration.
    facebook_url = models.URLField(
        _('Facebook URL (DEPRECATED)'),
        blank=True,
        null=True,
        help_text=_('DEPRECATED: Use GlobalSettings instead.')
    )
    twitter_url = models.URLField(
        _('Twitter URL (DEPRECATED)'),
        blank=True,
        null=True,
        help_text=_('DEPRECATED: Use GlobalSettings instead.')
    )
    instagram_url = models.URLField(
        _('Instagram URL (DEPRECATED)'),
        blank=True,
        null=True,
        help_text=_('DEPRECATED: Use GlobalSettings instead.')
    )
    linkedin_url = models.URLField(
        _('LinkedIn URL (DEPRECATED)'),
        blank=True,
        null=True,
        help_text=_('DEPRECATED: Use GlobalSettings instead.')
    )
    youtube_url = models.URLField(
        _('YouTube URL (DEPRECATED)'),
        blank=True,
        null=True,
        help_text=_('DEPRECATED: Use GlobalSettings instead.')
    )
    tiktok_url = models.URLField(
        _('TikTok URL (DEPRECATED)'),
        blank=True,
        null=True,
        help_text=_('DEPRECATED: Use GlobalSettings instead.')
    )

    # Working hours
    working_hours = models.CharField(
        _('Working Hours'),
        max_length=100,
        blank=True,
        null=True,
        help_text=_('e.g., 24/7 or Mon-Fri 8AM-5PM')
    )

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Contact Information')
        verbose_name_plural = _('Contact Information')

    def __str__(self):
        return f"Contact Information (Updated: {self.updated_at.strftime('%Y-%m-%d %H:%M')})"

    @classmethod
    def get_contact_info(cls):
        """Get or create the single instance of contact information"""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
