from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ('title', 'description')
    ordering = ('order',)
