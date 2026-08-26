from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Partner, PartnerPhone, PartnerEmail


class PartnerPhoneInline(admin.TabularInline):
    model = PartnerPhone
    extra = 1


class PartnerEmailInline(admin.TabularInline):
    model = PartnerEmail
    extra = 1


@admin.register(Partner)
class PartnerAdmin(SimpleHistoryAdmin):
    list_display = ['name', 'partner_type', 'order', 'is_featured', 'is_active']
    list_filter = ['partner_type', 'is_featured', 'is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['order', 'name']
    list_editable = ['order', 'is_featured', 'is_active']
    inlines = [PartnerPhoneInline, PartnerEmailInline]

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
        ('Audit', {
            'fields': ('created_by', 'last_updated_by'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['created_by', 'last_updated_by']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.last_updated_by = request.user
        super().save_model(request, obj, form, change)
