from rest_framework import serializers
from .models import Resource, ResourceCategory


class ResourceCategorySerializer(serializers.ModelSerializer):
    """Serializer for Resource Category"""
    
    class Meta:
        model = ResourceCategory
        fields = ['id', 'name', 'slug', 'description', 'icon']
        read_only_fields = ['slug']


class ResourceListSerializer(serializers.ModelSerializer):
    """Serializer for listing resources"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Resource
        fields = [
            'id', 'title', 'slug', 'description', 'category_name',
            'file', 'file_size', 'file_type', 'thumbnail', 'language',
            'status', 'download_count', 'is_featured', 'published_at'
        ]


class ResourceDetailSerializer(serializers.ModelSerializer):
    """Serializer for resource detail view"""
    category = ResourceCategorySerializer(read_only=True)
    
    class Meta:
        model = Resource
        fields = [
            'id', 'title', 'slug', 'description', 'category',
            'file', 'file_size', 'file_type', 'thumbnail', 'language', 'status',
            'download_count', 'is_featured', 'published_at', 'updated_at'
        ]


class ResourceCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating/updating resources"""
    
    class Meta:
        model = Resource
        fields = [
            'title', 'description', 'category', 'file', 'thumbnail', 
            'language', 'status', 'is_featured'
        ]
        extra_kwargs = {'slug': {'required': False}}
