from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Resource, ResourceCategory


@admin.register(ResourceCategory)
class ResourceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'icon']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Resource)
class ResourceAdmin(SimpleHistoryAdmin):
    list_display = ['title', 'category', 'file_type', 'language', 'is_featured', 'download_count', 'published_at']
    list_filter = ['category', 'language', 'is_featured', 'published_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    ordering = ['-published_at']
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'description', 'category')
        }),
        ('File', {
            'fields': ('file', 'file_type', 'file_size', 'thumbnail')
        }),
        ('Settings', {
            'fields': ('language', 'status', 'is_featured')
        }),
        ('Stats', {
            'fields': ('download_count', 'created_by', 'last_updated_by'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['file_size', 'file_type', 'created_by', 'last_updated_by']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.last_updated_by = request.user
        super().save_model(request, obj, form, change)
