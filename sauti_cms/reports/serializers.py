from rest_framework import serializers
from .models import Report, ReportFollowUp


class ReporterSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    phone = serializers.CharField(required=True)
    safe_to_contact = serializers.BooleanField(required=True)

class ReportCreateSerializer(serializers.ModelSerializer):
    """Serializer for submitting reports (public, no auth required)"""
    
    intake_category = serializers.CharField(source='category')
    reporter = ReporterSerializer(write_only=True)
    affected_persons = serializers.ListField(child=serializers.DictField(), required=False)
    
    class Meta:
        model = Report
        fields = [
            'intake_category', 'description', 'reporting_for',
            'location', 
            'reporter', 'affected_persons'
        ]
    
    def create(self, validated_data):
        reporter_data = validated_data.pop('reporter', {})
        
        # Map nested reporter data to flat model fields
        validated_data['contact_name'] = reporter_data.get('name')
        validated_data['contact_phone'] = reporter_data.get('phone')
        validated_data['safe_to_contact'] = reporter_data.get('safe_to_contact', True)
        # Determine anonymity based on whether name is provided
        validated_data['is_anonymous'] = not bool(reporter_data.get('name'))
        
        return super().create(validated_data)


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
            'assigned_to_name', 'created_at', 'updated_at',
            'reporting_for', 'affected_persons', 'safe_to_contact',
            'openchs_case_id'
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
            'reported_person_age', 'reported_person_gender', 'is_self_report',
            'created_at', 'updated_at', 'resolved_at',
            'reporting_for', 'affected_persons', 'safe_to_contact',
            'escalated_at', 'forwarded_to_openchs_at', 'openchs_case_id'
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
        fields = [
            'status', 'assigned_to', 'notes',
            'reported_person_age', 'reported_person_gender', 'is_self_report',
            'reporting_for', 'affected_persons', 'safe_to_contact'
        ]


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
