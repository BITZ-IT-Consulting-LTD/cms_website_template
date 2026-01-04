from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import SiteSetting, GlobalSettings, HomePageSettings, AboutPageSettings, OrganizationProfile

@admin.register(SiteSetting)
class SiteSettingAdmin(SimpleHistoryAdmin):
    list_display = ('page', 'key', 'value', 'description', 'last_updated')
    list_filter = ('page',)
    search_fields = ('page', 'key', 'value', 'description')
    readonly_fields = ('last_updated',)
    fieldsets = (
        (None, {
            'fields': ('page', 'key', 'value', 'description')
        }),
        ('Metadata', {
            'fields': ('last_updated',),
            'classes': ('collapse',)
        }),
    )

class BaseSettingsAdmin(SimpleHistoryAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(GlobalSettings)
class GeneralSettingsAdmin(BaseSettingsAdmin):
    fieldsets = (
        ('Site Identity', {
            'fields': ('site_name', 'site_description', 'hotline_number', 'primary_cta_text')
        }),
        ('Global Contact Text', {
            'fields': ('hotline_text', 'support_email_text', 'operating_hours_text')
        }),
        ('Footer & Legal', {
            'fields': ('footer_text', 'ministry_attribution_text', 'disclaimer_text', 'privacy_policy_url')
        }),
        ('Social Media & External Links', {
            'fields': (
                'social_facebook', 'social_twitter', 'social_whatsapp', 
                'social_instagram', 'social_linkedin', 'social_youtube', 
                'social_tiktok', 'social_ureport', 'social_safepal'
            )
        }),
        ('Contact Info', {
            'fields': ('contact_email_info', 'contact_email_sautichl', 'contact_website', 'contact_phone_main')
        }),
        ('SEO Defaults', {
            'fields': ('default_meta_title_suffix', 'default_meta_description')
        }),
        ('Environment', {
            'fields': ('environment_label',)
        }),
    )

@admin.register(HomePageSettings)
class HomePageSettingsAdmin(BaseSettingsAdmin):
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_value_prop', 'hero_badges')

        }),
        ('Intro Section', {
            'fields': ('intro_title', 'intro_description')
        }),
        ('Quick Access Section', {
            'fields': ('quick_access_title', 'quick_access_description', 'qa_child_protection_title', 'qa_child_protection_text', 'qa_child_protection_icon', 'qa_gbv_title', 'qa_gbv_text', 'qa_gbv_icon', 'qa_migrants_title', 'qa_migrants_text', 'qa_migrants_icon', 'qa_psea_title', 'qa_psea_text', 'qa_psea_icon')
        }),
        ('News Section', {
            'fields': ('news_title', 'news_description', 'news_link_text')
        }),
        ('Partners Section', {
            'fields': ('partners_title', 'partners_description')
        }),
    )

@admin.register(AboutPageSettings)
class AboutPageSettingsAdmin(BaseSettingsAdmin):
    fieldsets = (
        ('Mission & Vision', {
            'fields': ('mission', 'vision')
        }),
        # Add other about-page specific fields here if they exist in GlobalSettings
    )

@admin.register(OrganizationProfile)
class OrganizationProfileAdmin(BaseSettingsAdmin):
    fieldsets = (
        ('Basic Identity', {
            'fields': ('name', 'tagline', 'logo', 'favicon')
        }),
        ('Branding / Colors', {
            'fields': ('primary_color', 'secondary_color', 'accent_color')
        }),
        ('Contact Information', {
            'fields': ('address', 'primary_phone', 'primary_email', 'alternate_email')
        }),
        ('Legal & History', {
            'fields': ('registration_info', 'founded_date', 'about_us_summary')
        }),
        ('Social Media Defaults', {
            'fields': ('twitter_handle', 'facebook_page')
        }),
    )
