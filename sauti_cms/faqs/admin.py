from django.contrib import admin
from .models import FAQ, FAQCategory


@admin.register(FAQCategory)
class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['order', 'name']


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'category', 'language', 'order', 'is_active', 'views_count']
    list_filter = ['category', 'language', 'is_active', 'created_at']
    search_fields = ['question', 'answer']
    ordering = ['category', 'order', 'question']
    list_editable = ['order', 'is_active']
    
    fieldsets = (
        ('Content', {
            'fields': ('question', 'answer')
        }),
        ('Organization', {
            'fields': ('category', 'language', 'order', 'status', 'is_active')
        }),
        ('Stats', {
            'fields': ('views_count', 'created_by', 'last_updated_by'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['created_by', 'last_updated_by']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.last_updated_by = request.user
        super().save_model(request, obj, form, change)
