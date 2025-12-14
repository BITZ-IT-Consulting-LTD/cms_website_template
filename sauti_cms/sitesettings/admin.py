from django.contrib import admin
from .models import SiteSetting

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
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
