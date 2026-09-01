from rest_framework import serializers
from .models import Report, ReportFollowUp


class ReporterSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    phone = serializers.CharField(required=True)
    safe_to_contact = serializers.BooleanField(required=True)
    # The intake form has always sent this; it used to be silently dropped
    # because a plain Serializer discards undeclared keys.
    alternative_contact = serializers.CharField(
        required=False, allow_null=True, allow_blank=True
    )

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
            # victim_location and incident_type were previously absent here, so
            # the values the intake form posted never reached the database.
            'victim_location', 'incident_type',
            'reporter', 'affected_persons'
        ]
        extra_kwargs = {
            'victim_location': {'required': False, 'allow_blank': True},
            'incident_type': {'required': False, 'allow_blank': True},
        }

    def create(self, validated_data):
        reporter_data = validated_data.pop('reporter', {})

        # Map nested reporter data to flat model fields
        validated_data['contact_name'] = reporter_data.get('name') or ''
        validated_data['contact_phone'] = reporter_data.get('phone') or ''
        validated_data['safe_to_contact'] = reporter_data.get('safe_to_contact', True)
        validated_data['alternative_contact'] = reporter_data.get('alternative_contact') or ''
        # Determine anonymity based on whether name is provided
        validated_data['is_anonymous'] = not bool(reporter_data.get('name'))

        # Extract first affected person's data to flat fields for admin display
        affected_persons = validated_data.get('affected_persons', [])
        if affected_persons and len(affected_persons) > 0:
            first_person = affected_persons[0]
            # Map gender field - handle both uppercase (MALE/FEMALE) and title case (Male/Female)
            gender_value = first_person.get('gender', '').upper() if first_person.get('gender') else None
            if gender_value in ['MALE', 'FEMALE', 'OTHER']:
                validated_data['reported_person_gender'] = gender_value

            # Map age field
            age_value = first_person.get('age')
            if age_value:
                try:
                    validated_data['reported_person_age'] = int(age_value)
                except (ValueError, TypeError):
                    pass  # Skip if age is not a valid integer

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
            'openchs_case_id', 'incident_type', 'victim_location',
            'reported_person_age',
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
            'alternative_contact', 'victim_location', 'incident_type',
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
            'reporting_for', 'affected_persons', 'safe_to_contact',
            'category', 'description', 'contact_name', 'contact_phone',
            'contact_email', 'location',
            'alternative_contact', 'victim_location', 'incident_type'
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
