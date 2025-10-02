from django.contrib import admin
from django.utils.html import format_html
from .models import Report, ReportFollowUp


class ReportFollowUpInline(admin.TabularInline):
    model = ReportFollowUp
    extra = 1
    fields = ['action_taken', 'created_by', 'created_at']
    readonly_fields = ['created_at']


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = [
        'reference_number', 'category', 'status', 'is_anonymous',
        'location', 'assigned_to', 'created_at_short', 'status_badge'
    ]
    list_filter = ['status', 'category', 'is_anonymous', 'created_at']
    search_fields = ['reference_number', 'description', 'contact_name', 'location']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    readonly_fields = [
        'reference_number', 'ip_address', 'user_agent',
        'created_at', 'updated_at', 'encrypted_description'
    ]
    inlines = [ReportFollowUpInline]
    
    fieldsets = (
        ('Report Details', {
            'fields': ('reference_number', 'category', 'description', 'location')
        }),
        ('Contact Information', {
            'fields': ('is_anonymous', 'contact_name', 'contact_phone', 'contact_email')
        }),
        ('Attachment', {
            'fields': ('attachment',)
        }),
        ('Status & Assignment', {
            'fields': ('status', 'assigned_to', 'notes', 'resolved_at')
        }),
        ('System Info', {
            'fields': ('ip_address', 'user_agent', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
        ('Security', {
            'fields': ('encrypted_description',),
            'classes': ('collapse',)
        }),
    )
    
    def created_at_short(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %H:%M')
    created_at_short.short_description = 'Submitted'
    
    def status_badge(self, obj):
        colors = {
            'PENDING': '#f39c12',
            'IN_PROGRESS': '#3498db',
            'RESOLVED': '#27ae60',
            'CLOSED': '#95a5a6'
        }
        color = colors.get(obj.status, '#95a5a6')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 3px;">{}</span>',
            color,
            obj.get_status_display()
        )
    status_badge.short_description = 'Status'
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Editors see all reports, but we could limit by assignment
        return qs.select_related('assigned_to')


@admin.register(ReportFollowUp)
class ReportFollowUpAdmin(admin.ModelAdmin):
    list_display = ['report', 'action_taken_short', 'created_by', 'created_at']
    list_filter = ['created_at']
    search_fields = ['report__reference_number', 'action_taken']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    readonly_fields = ['created_at']
    
    def action_taken_short(self, obj):
        return obj.action_taken[:100] + '...' if len(obj.action_taken) > 100 else obj.action_taken
    action_taken_short.short_description = 'Action'
