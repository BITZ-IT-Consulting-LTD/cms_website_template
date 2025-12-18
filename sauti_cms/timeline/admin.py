from django.contrib import admin
from .models import TimelineEvent

@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'order', 'is_visible')
    list_filter = ('is_visible', 'year')
    search_fields = ('title', 'description', 'year')
    ordering = ('order',)
