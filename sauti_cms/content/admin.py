from django.contrib import admin
from .models import SiteContent

@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ('label', 'key', 'type', 'page', 'is_published', 'updated_at')
    list_filter = ('page', 'type', 'is_published')
    search_fields = ('label', 'key', 'value', 'description')
    readonly_fields = ('created_at', 'updated_at')
