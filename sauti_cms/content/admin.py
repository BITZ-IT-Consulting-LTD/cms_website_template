from django.contrib import admin
from django.utils.html import format_html
from .models import SiteContent, CoreValue, Contact, ProtectionApproach, TeamMember, WhoWeAreImage, OperationsImage

class OwnershipAdminMixin:
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.last_updated_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(SiteContent)
class SiteContentAdmin(OwnershipAdminMixin, admin.ModelAdmin):
    list_display = ('label', 'key', 'type', 'page', 'is_published', 'updated_at')
    list_filter = ('page', 'type', 'is_published')
    search_fields = ('label', 'key', 'value', 'description')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'last_updated_by')


@admin.register(CoreValue)
class CoreValueAdmin(OwnershipAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'color_from', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'last_updated_by')
    list_editable = ('order', 'is_active')
    ordering = ('order', 'title')


@admin.register(Contact)
class ContactAdmin(OwnershipAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'value', 'type', 'order', 'is_visible', 'updated_at')
    list_filter = ('type', 'is_visible')
    search_fields = ('name', 'value')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'last_updated_by')
    list_editable = ('order', 'is_visible')
    ordering = ('order', 'name')


@admin.register(ProtectionApproach)
class ProtectionApproachAdmin(OwnershipAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'icon', 'color', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'last_updated_by')
    list_editable = ('order', 'is_active')
    ordering = ('order', 'title')


@admin.register(TeamMember)
class TeamMemberAdmin(OwnershipAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'role', 'order', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'role', 'bio')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'last_updated_by')
    list_editable = ('order', 'is_active')
    ordering = ('order', 'name')


@admin.register(WhoWeAreImage)
class WhoWeAreImageAdmin(OwnershipAdminMixin, admin.ModelAdmin):
    list_display = ('position_display', 'title', 'image_preview', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'alt_text')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'last_updated_by', 'image_preview_large')
    list_editable = ('is_active',)
    ordering = ('position',)

    fieldsets = (
        ('Image Position', {
            'fields': ('position',),
            'description': 'Select the position in the About page hero grid where this image will appear.'
        }),
        ('Image Details', {
            'fields': ('title', 'image', 'image_preview_large', 'alt_text'),
        }),
        ('Status', {
            'fields': ('is_active',),
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at', 'created_by', 'last_updated_by'),
            'classes': ('collapse',),
        }),
    )

    def position_display(self, obj):
        return obj.get_position_display()
    position_display.short_description = 'Grid Position'
    position_display.admin_order_field = 'position'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 80px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return '-'
    image_preview.short_description = 'Preview'

    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 200px; max-width: 300px; object-fit: cover; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />', obj.image.url)
        return 'No image uploaded'
    image_preview_large.short_description = 'Current Image'


@admin.register(OperationsImage)
class OperationsImageAdmin(OwnershipAdminMixin, admin.ModelAdmin):
    list_display = ('position_display', 'title', 'image_preview', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'alt_text', 'position')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'last_updated_by', 'image_preview_large')
    list_editable = ('is_active',)
    ordering = ('position',)

    fieldsets = (
        ('Image Position', {
            'fields': ('position',),
            'description': 'Select the position/section on the Operations page where this image will appear.'
        }),
        ('Image Details', {
            'fields': ('title', 'image', 'image_preview_large', 'alt_text'),
        }),
        ('Status', {
            'fields': ('is_active',),
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at', 'created_by', 'last_updated_by'),
            'classes': ('collapse',),
        }),
    )

    def position_display(self, obj):
        return obj.get_position_display()
    position_display.short_description = 'Section'
    position_display.admin_order_field = 'position'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 80px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return '-'
    image_preview.short_description = 'Preview'

    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 200px; max-width: 300px; object-fit: cover; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />', obj.image.url)
        return 'No image uploaded'
    image_preview_large.short_description = 'Current Image'
