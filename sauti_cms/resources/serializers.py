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

    def _get_url(self, maybe_relative_url: str) -> str | None:
        """Return relative URL (frontend proxy handles it)"""
        if not maybe_relative_url:
            return None
        url_str = str(maybe_relative_url)
        # If already a full URL, return as-is
        if url_str.startswith('http://') or url_str.startswith('https://'):
            return url_str
        return url_str

    def get_file(self, obj):
        try:
            return obj.file.url if obj.file else None
        except Exception:
            return str(obj.file) if obj.file else None

    def get_thumbnail(self, obj):
        if not obj.thumbnail:
            return None
        try:
            return obj.thumbnail.url
        except Exception:
            return str(obj.thumbnail)


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

    def get_file(self, obj):
        """Return relative URL for file (frontend proxy handles it)"""
        try:
            return obj.file.url if obj.file else None
        except Exception:
            return str(obj.file) if obj.file else None

    def get_thumbnail(self, obj):
        """Return relative URL for thumbnail (frontend proxy handles it)"""
        if not obj.thumbnail:
            return None
        try:
            return obj.thumbnail.url
        except Exception:
            return str(obj.thumbnail)


class ResourceCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating/updating resources"""

    class Meta:
        model = Resource
        fields = [
            'title', 'description', 'category', 'file', 'thumbnail',
            'language', 'status', 'is_featured'
        ]
        extra_kwargs = {
            'slug': {'required': False},
            # 'file' is required when creating a new resource, but must stay
            # optional on update — the edit form (e.g. toggling visibility)
            # only re-sends a file when the editor chooses to replace it, and
            # PUT is not partial, so without this every metadata-only edit
            # (status, title, etc.) would 400 with "No file was submitted."
            'file': {'required': False},
        }

    def validate(self, attrs):
        if self.instance is None and not attrs.get('file'):
            raise serializers.ValidationError({'file': 'This field is required.'})
        return attrs
