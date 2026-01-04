from rest_framework import serializers

class HistoricalRecordSerializer(serializers.Serializer):
    history_id = serializers.IntegerField()
    history_date = serializers.DateTimeField()
    history_change_reason = serializers.CharField()
    history_type = serializers.CharField()
    history_user_id = serializers.IntegerField()
    history_user_username = serializers.SerializerMethodField()
    history_user_fullname = serializers.SerializerMethodField()
    changes = serializers.SerializerMethodField()

    def get_history_user_username(self, obj):
        return obj.history_user.username if obj.history_user else "System"

    def get_history_user_fullname(self, obj):
        if obj.history_user:
            return f"{obj.history_user.first_name} {obj.history_user.last_name}".strip() or obj.history_user.username
        return "System"

    def get_changes(self, obj):
        changes = []
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)
            for change in delta.changes:
                changes.append({
                    'field': change.field,
                    'old': change.old,
                    'new': change.new
                })
        return changes
