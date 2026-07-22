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


class FAQCategoryNestedSerializer(serializers.ModelSerializer):
    """Lightweight category serializer for nesting inside FAQ.

    Deliberately omits `faq_count` — computing it per FAQ row triggered an
    extra COUNT query for every FAQ in the list (N+1) and was the main cause
    of slow FAQ page loads. The public FAQ list only needs id/name/slug.
    """

    class Meta:
        model = FAQCategory
        fields = ['id', 'name', 'slug', 'description', 'order']


class FAQSerializer(serializers.ModelSerializer):
    """Serializer for FAQ"""
    category = FAQCategoryNestedSerializer(read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = FAQ
        fields = [
            'id', 'question', 'answer', 'category', 'category_name', 'language',
            'is_active', 'status', 'order', 'views_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['views_count', 'created_at', 'updated_at']


class FAQCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating/updating FAQs"""
    
    class Meta:
        model = FAQ
        fields = [
            'id', 'question', 'answer', 'category', 'language',
            'order', 'is_active', 'status'
        ]
        read_only_fields = ['id']