from django.contrib import admin
from .models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'partner_type', 'order', 'is_featured', 'is_active']
    list_filter = ['partner_type', 'is_featured', 'is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['order', 'name']
    list_editable = ['order', 'is_featured', 'is_active']
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'slug', 'description', 'partner_type', 'logo')
        }),
        ('Contact', {
            'fields': ('website_url', 'email', 'phone')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_featured', 'is_active')
        }),
    )
