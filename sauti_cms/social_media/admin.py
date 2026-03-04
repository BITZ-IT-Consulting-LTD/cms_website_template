from django.contrib import admin
from .models import SocialPost, SocialMediaChannels, ContactInformation

@admin.register(SocialPost)
class SocialPostAdmin(admin.ModelAdmin):
    list_display = ('platform', 'handle', 'posted_at', 'is_active', 'order')
    list_filter = ('platform', 'is_active')
    search_fields = ('handle', 'content')
    ordering = ('order', '-posted_at')

@admin.register(SocialMediaChannels)
class SocialMediaChannelsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()

@admin.register(ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('primary_email', 'support_email', 'primary_phone', 'whatsapp_number', 'office_address', 'working_hours')
        }),
        ('Social Media (DEPRECATED)', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'youtube_url', 'tiktok_url'),
            'description': 'These fields are deprecated. Please use Global Settings for social media configuration.',
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'youtube_url', 'tiktok_url')

    def has_add_permission(self, request):
        return not self.model.objects.exists()
