from rest_framework import serializers
from .models import Report, ReportFollowUp


class ReportCreateSerializer(serializers.ModelSerializer):
    """Serializer for submitting reports (public, no auth required)"""
    
    class Meta:
        model = Report
        fields = [
            'category', 'description', 'is_anonymous',
            'contact_name', 'contact_phone', 'contact_email',
            'location', 'attachment'
        ]
    
    def validate(self, attrs):
        """Ensure contact info is provided if not anonymous"""
        if not attrs.get('is_anonymous'):
            if not any([
                attrs.get('contact_name'),
                attrs.get('contact_phone'),
                attrs.get('contact_email')
            ]):
                raise serializers.ValidationError(
                    "Please provide at least one contact method if not submitting anonymously."
                )
        return attrs


class ReportListSerializer(serializers.ModelSerializer):
    """Serializer for listing reports (Admin/Editor only)"""
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    assigned_to_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Report
        fields = [
            'id', 'reference_number', 'category', 'category_display',
            'status', 'status_display', 'is_anonymous', 'location',
            'assigned_to_name', 'created_at', 'updated_at'
        ]
    
    def get_assigned_to_name(self, obj):
        return obj.assigned_to.get_full_name() if obj.assigned_to else None


class ReportDetailSerializer(serializers.ModelSerializer):
    """Serializer for report detail view (Admin/Editor only)"""
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    assigned_to = serializers.StringRelatedField(read_only=True)
    followups = serializers.SerializerMethodField()
    
    class Meta:
        model = Report
        fields = [
            'id', 'reference_number', 'category', 'category_display',
            'description', 'is_anonymous', 'contact_name', 'contact_phone',
            'contact_email', 'location', 'attachment', 'status',
            'status_display', 'assigned_to', 'notes', 'followups',
            'created_at', 'updated_at', 'resolved_at'
        ]
    
    def get_followups(self, obj):
        return ReportFollowUpSerializer(
            obj.followups.all(),
            many=True
        ).data


class ReportUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating report status (Admin/Editor only)"""
    
    class Meta:
        model = Report
        fields = ['status', 'assigned_to', 'notes']


class ReportFollowUpSerializer(serializers.ModelSerializer):
    """Serializer for report follow-ups"""
    created_by_name = serializers.SerializerMethodField()
    
    class Meta:
        model = ReportFollowUp
        fields = ['id', 'action_taken', 'created_by_name', 'created_at']
        read_only_fields = ['created_at']
    
    def get_created_by_name(self, obj):
        return obj.created_by.get_full_name() if obj.created_by else None


class ReportFollowUpCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating follow-ups"""
    
    class Meta:
        model = ReportFollowUp
        fields = ['report', 'action_taken']
