from rest_framework import serializers
from .models import FAQ, FAQCategory


class FAQCategorySerializer(serializers.ModelSerializer):
    """Serializer for FAQ Category"""
    faq_count = serializers.SerializerMethodField()
    
    class Meta:
        model = FAQCategory
        fields = ['id', 'name', 'slug', 'description', 'order', 'faq_count']
    
    def get_faq_count(self, obj):
        return obj.faqs.filter(is_active=True).count()


class FAQSerializer(serializers.ModelSerializer):
    """Serializer for FAQ"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = FAQ
        fields = [
            'id', 'question', 'answer', 'category', 'category_name',
            'language', 'order', 'is_active', 'views_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['views_count', 'created_at', 'updated_at']


class FAQCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating/updating FAQs"""
    
    class Meta:
        model = FAQ
        fields = [
            'question', 'answer', 'category', 'language',
            'order', 'is_active'
        ]
