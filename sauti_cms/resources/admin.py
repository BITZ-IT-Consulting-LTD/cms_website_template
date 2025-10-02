from django.contrib import admin
from .models import Resource, ResourceCategory


@admin.register(ResourceCategory)
class ResourceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'icon']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
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
            'fields': ('language', 'is_featured')
        }),
        ('Stats', {
            'fields': ('download_count',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['file_size', 'file_type']
