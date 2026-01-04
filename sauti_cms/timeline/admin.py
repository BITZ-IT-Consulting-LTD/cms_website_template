from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import TimelineEvent

@admin.register(TimelineEvent)
class TimelineEventAdmin(SimpleHistoryAdmin):
    list_display = ('year', 'title', 'order', 'is_visible')
    list_filter = ('is_visible', 'year')
    search_fields = ('title', 'description', 'year')
    ordering = ('order',)
    
    readonly_fields = ['created_by', 'last_updated_by']

    fieldsets = (
        (None, {
            'fields': ('year', 'title', 'description', 'order', 'is_visible')
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
