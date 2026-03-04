from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ('title', 'description')
    ordering = ('order',)
    readonly_fields = ['created_by', 'last_updated_by']
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'icon', 'order', 'is_visible')
        }),
        ('Audit', {
            'fields': ('created_by', 'last_updated_by'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.last_updated_by = request.user
        super().save_model(request, obj, form, change)


from .models import HelpService

@admin.register(HelpService)
class HelpServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'key', 'order', 'is_active')
    list_filter = ('is_active', 'key')
    search_fields = ('title', 'intro_text')
    ordering = ('order',)
    readonly_fields = ['created_by', 'last_updated_by']

    fieldsets = (
        (None, {
            'fields': ('title', 'key', 'intro_text', 'scope_items', 'order', 'is_active')
        }),
        ('Audit', {
            'fields': ('created_by', 'last_updated_by'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.last_updated_by = request.user
        super().save_model(request, obj, form, change)
