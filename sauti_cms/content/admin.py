from django.contrib import admin
from .models import SiteContent, CoreValue, Contact

@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ('label', 'key', 'type', 'page', 'is_published', 'updated_at')
    list_filter = ('page', 'type', 'is_published')
    search_fields = ('label', 'key', 'value', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'color_from', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('order', 'is_active')
    ordering = ('order', 'title')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'type', 'order', 'is_visible', 'updated_at')
    list_filter = ('type', 'is_visible')
    search_fields = ('name', 'value')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('order', 'is_visible')
    ordering = ('order', 'name')
