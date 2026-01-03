from django.contrib import admin
from .models import Video, VideoCategory


@admin.register(VideoCategory)
class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_type', 'author', 'category', 'status', 'language', 'is_featured', 'published_at', 'views_count']
    list_filter = ['status', 'language', 'is_featured', 'video_type', 'category', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    ordering = ['-published_at', '-created_at']

    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'description', 'thumbnail')
        }),
        ('Video Source', {
            'fields': ('video_type', 'youtube_url', 'video_file')
        }),
        ('Metadata', {
            'fields': ('duration', 'file_size'),
            'classes': ('collapse',)
        }),
        ('Organization', {
            'fields': ('author', 'category')
        }),
        ('Publication', {
            'fields': ('status', 'language', 'is_featured', 'published_at')
        }),
        ('Stats', {
            'fields': ('views_count', 'created_by', 'last_updated_by'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_by', 'last_updated_by']

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        
        if not change:
            obj.created_by = request.user
        obj.last_updated_by = request.user
        super().save_model(request, obj, form, change)
