from rest_framework import serializers
from .models import FeedbackMessage

class FeedbackMessageSerializer(serializers.ModelSerializer):
    reviewed_by_name = serializers.SerializerMethodField()

    class Meta:
        model = FeedbackMessage
        # is_processed is now included so "Mark as reviewed" (a PATCH of
        # is_processed) actually persists instead of being silently dropped.
        fields = [
            'id', 'name', 'email', 'message', 'submitted_at',
            'is_processed', 'is_archived', 'reviewed_at', 'reviewed_by', 'reviewed_by_name'
        ]
        read_only_fields = ['id', 'submitted_at', 'reviewed_at', 'reviewed_by', 'reviewed_by_name']

    def get_reviewed_by_name(self, obj):
        if not obj.reviewed_by:
            return None
        return obj.reviewed_by.get_full_name() or obj.reviewed_by.username

    def validate_message(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message cannot be empty.")
        return value


class FeedbackCreateSerializer(serializers.ModelSerializer):
    """Public submission serializer — only accepts the submitter's own fields.

    Deliberately excludes is_processed / is_archived / reviewed_* so an anonymous
    POST to the AllowAny create endpoint cannot self-mark a message reviewed or
    archived (which would hide it from the accountability queue).
    """

    class Meta:
        model = FeedbackMessage
        fields = ['id', 'name', 'email', 'message', 'submitted_at']
        read_only_fields = ['id', 'submitted_at']

    def validate_message(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message cannot be empty.")
        return value
