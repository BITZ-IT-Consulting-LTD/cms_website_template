from django.contrib import admin
from .models import SocialPost

@admin.register(SocialPost)
class SocialPostAdmin(admin.ModelAdmin):
    list_display = ('platform', 'handle', 'posted_at', 'is_active', 'order')
    list_filter = ('platform', 'is_active')
    search_fields = ('handle', 'content')
    ordering = ('order', '-posted_at')
