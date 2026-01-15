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
    file = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    
    class Meta:
        model = Resource
        fields = [
            'id', 'title', 'slug', 'description', 'category_name',
            'file', 'file_size', 'file_type', 'thumbnail', 'language',
            'status', 'download_count', 'is_featured', 'published_at'
        ]

    def _build_absolute_url(self, request, maybe_relative_url: str) -> str | None:
        if not maybe_relative_url:
            return None

        url_str = str(maybe_relative_url)
        if url_str.startswith('http://') or url_str.startswith('https://'):
            return url_str

        # Normal file/image fields typically come through as "/sauti/media/..."
        if request:
            host = request.META.get('HTTP_X_FORWARDED_HOST', request.get_host())
            scheme = request.META.get('HTTP_X_FORWARDED_PROTO', request.scheme)
            if host == 'backend':
                host = 'localhost:8080'
                scheme = 'http'
            return f"{scheme}://{host}{url_str}"

        return f"http://localhost:8080{url_str}"

    def get_file(self, obj):
        try:
            file_url = obj.file.url
        except Exception:
            file_url = str(obj.file) if obj.file else None
        request = self.context.get('request')
        return self._build_absolute_url(request, file_url)

    def get_thumbnail(self, obj):
        if not obj.thumbnail:
            return None
        try:
            thumb_url = obj.thumbnail.url
        except Exception:
            thumb_url = str(obj.thumbnail)
        request = self.context.get('request')
        return self._build_absolute_url(request, thumb_url)


class ResourceDetailSerializer(serializers.ModelSerializer):
    """Serializer for resource detail view"""
    category = ResourceCategorySerializer(read_only=True)
    file = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    
    class Meta:
        model = Resource
        fields = [
            'id', 'title', 'slug', 'description', 'category',
            'file', 'file_size', 'file_type', 'thumbnail', 'language', 'status',
            'download_count', 'is_featured', 'published_at', 'updated_at'
        ]

    def _build_absolute_url(self, request, maybe_relative_url: str) -> str | None:
        if not maybe_relative_url:
            return None

        url_str = str(maybe_relative_url)
        if url_str.startswith('http://') or url_str.startswith('https://'):
            return url_str

        if request:
            host = request.META.get('HTTP_X_FORWARDED_HOST', request.get_host())
            scheme = request.META.get('HTTP_X_FORWARDED_PROTO', request.scheme)
            if host == 'backend':
                host = 'localhost:8080'
                scheme = 'http'
            return f"{scheme}://{host}{url_str}"

        return f"http://localhost:8080{url_str}"

    def get_file(self, obj):
        try:
            file_url = obj.file.url
        except Exception:
            file_url = str(obj.file) if obj.file else None
        request = self.context.get('request')
        return self._build_absolute_url(request, file_url)

    def get_thumbnail(self, obj):
        if not obj.thumbnail:
            return None
        try:
            thumb_url = obj.thumbnail.url
        except Exception:
            thumb_url = str(obj.thumbnail)
        request = self.context.get('request')
        return self._build_absolute_url(request, thumb_url)


class ResourceCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating/updating resources"""
    
    class Meta:
        model = Resource
        fields = [
            'title', 'description', 'category', 'file', 'thumbnail', 
            'language', 'status', 'is_featured'
        ]
        extra_kwargs = {'slug': {'required': False}}
