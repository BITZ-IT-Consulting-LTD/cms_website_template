from rest_framework import serializers
from .models import Video, VideoCategory


class VideoCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCategory
        fields = ['id', 'name', 'slug', 'description', 'created_at']


class VideoSerializer(serializers.ModelSerializer):
    category = VideoCategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, required=False)
    author_name = serializers.CharField(source='author.get_full_name', read_only=True)
    youtube_id = serializers.CharField(read_only=True)
    youtube_embed_url = serializers.CharField(read_only=True)
    youtube_thumbnail_url = serializers.CharField(read_only=True)
    thumbnail = serializers.SerializerMethodField()
    
    class Meta:
        model = Video
        fields = [
            'id', 'title', 'slug', 'description', 'video_type',
            'youtube_url', 'video_file', 'thumbnail', 'duration',
            'file_size', 'category', 'category_id', 'author_name',
            'status', 'language', 'is_featured', 'views_count',
            'published_at', 'scheduled_publish_at', 'created_at', 'updated_at',
            'youtube_id', 'youtube_embed_url', 'youtube_thumbnail_url'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at', 'views_count']
    
    def get_thumbnail(self, obj):
        """Return absolute URL for thumbnail"""
        if obj.thumbnail:
            # Check if the field contains a full URL (external URL stored as string)
            thumbnail_str = str(obj.thumbnail)
            if thumbnail_str.startswith('http://') or thumbnail_str.startswith('https://'):
                # It's already a full URL, return as-is
                return thumbnail_str
            
            # It's a file field, get the relative URL
            try:
                thumbnail_url = obj.thumbnail.url
            except (ValueError, AttributeError):
                return None
            
            request = self.context.get('request')
            if request:
                # Use X-Forwarded-Host if available (from nginx proxy), otherwise use request host
                host = request.META.get('HTTP_X_FORWARDED_HOST', request.get_host())
                scheme = request.META.get('HTTP_X_FORWARDED_PROTO', request.scheme)
                # If host is 'backend' (internal Docker), use localhost for browser access
                if host == 'backend':
                    host = 'localhost:8080'  # nginx proxy port
                    scheme = 'http'
                return f"{scheme}://{host}{thumbnail_url}"
            # Fallback if no request context
            return f"http://localhost:8080{thumbnail_url}" if thumbnail_url else None
        return None
    
    def create(self, validated_data):
        category_id = validated_data.pop('category_id', None)
        video = Video.objects.create(**validated_data)
        
        if category_id:
            try:
                category = VideoCategory.objects.get(id=category_id)
                video.category = category
                video.save()
            except VideoCategory.DoesNotExist:
                pass
        
        return video
    
    def update(self, instance, validated_data):
        category_id = validated_data.pop('category_id', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if category_id is not None:
            try:
                category = VideoCategory.objects.get(id=category_id)
                instance.category = category
            except VideoCategory.DoesNotExist:
                instance.category = None
        
        instance.save()
        return instance


class VideoListSerializer(serializers.ModelSerializer):
    category = VideoCategorySerializer(read_only=True)
    author_name = serializers.CharField(source='author.get_full_name', read_only=True)
    youtube_id = serializers.CharField(read_only=True)
    youtube_thumbnail_url = serializers.CharField(read_only=True)
    thumbnail = serializers.SerializerMethodField()
    
    class Meta:
        model = Video
        fields = [
            'id', 'title', 'slug', 'description', 'video_type',
            'youtube_url', 'video_file', 'thumbnail', 'duration', 'category',
            'author_name', 'status', 'language', 'is_featured',
            'views_count', 'published_at', 'scheduled_publish_at', 'created_at', 'updated_at',
            'youtube_id', 'youtube_thumbnail_url'
        ]
    
    def get_thumbnail(self, obj):
        """Return absolute URL for thumbnail"""
        if obj.thumbnail:
            # Check if the field contains a full URL (external URL stored as string)
            thumbnail_str = str(obj.thumbnail)
            if thumbnail_str.startswith('http://') or thumbnail_str.startswith('https://'):
                # It's already a full URL, return as-is
                return thumbnail_str
            
            # It's a file field, get the relative URL
            try:
                thumbnail_url = obj.thumbnail.url
            except (ValueError, AttributeError):
                return None
            
            request = self.context.get('request')
            if request:
                # Use X-Forwarded-Host if available (from nginx proxy), otherwise use request host
                host = request.META.get('HTTP_X_FORWARDED_HOST', request.get_host())
                scheme = request.META.get('HTTP_X_FORWARDED_PROTO', request.scheme)
                # If host is 'backend' (internal Docker), use localhost for browser access
                if host == 'backend':
                    host = 'localhost:8080'  # nginx proxy port
                    scheme = 'http'
                return f"{scheme}://{host}{thumbnail_url}"
            # Fallback if no request context
            return f"http://localhost:8080{thumbnail_url}" if thumbnail_url else None
        return None