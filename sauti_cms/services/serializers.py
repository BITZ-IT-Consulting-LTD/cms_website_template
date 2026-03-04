from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

from .models import HelpService, HelpStep

class HelpStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpStep
        fields = ['id', 'title', 'description', 'step_order']

class HelpServiceSerializer(serializers.ModelSerializer):
    steps = HelpStepSerializer(many=True, required=False)

    class Meta:
        model = HelpService
        fields = ['id', 'key', 'title', 'summary', 'icon_name', 'intro_text', 'scope_items', 'is_active', 'order', 'homepage_display_order', 'steps']

    def create(self, validated_data):
        steps_data = validated_data.pop('steps', [])
        service = HelpService.objects.create(**validated_data)
        for step_data in steps_data:
            HelpStep.objects.create(service=service, **step_data)
        return service

    def update(self, instance, validated_data):
        steps_data = validated_data.pop('steps', None)
        
        # Update HelpService fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if steps_data is not None:
            # Simple approach: clear and recreation steps
            # In a more complex app, we'd match by ID
            instance.steps.all().delete()
            for step_data in steps_data:
                HelpStep.objects.create(service=instance, **step_data)
        
        return instance
