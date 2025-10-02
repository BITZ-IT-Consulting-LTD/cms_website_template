from django.contrib import admin
from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'language', 'is_featured', 'published_at', 'views_count']
    list_filter = ['status', 'language', 'is_featured', 'category', 'created_at']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    ordering = ['-published_at', '-created_at']
    filter_horizontal = ['tags']
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'excerpt', 'content', 'featured_image')
        }),
        ('Organization', {
            'fields': ('author', 'category', 'tags')
        }),
        ('Publication', {
            'fields': ('status', 'language', 'is_featured', 'published_at')
        }),
        ('Stats', {
            'fields': ('views_count',),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)
