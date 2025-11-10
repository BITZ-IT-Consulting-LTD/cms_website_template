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
    
    class Meta:
        model = Video
        fields = [
            'id', 'title', 'slug', 'description', 'video_type',
            'youtube_url', 'video_file', 'thumbnail', 'duration',
            'file_size', 'category', 'category_id', 'author_name',
            'status', 'language', 'is_featured', 'views_count',
            'published_at', 'created_at', 'updated_at',
            'youtube_id', 'youtube_embed_url', 'youtube_thumbnail_url'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at', 'views_count']
    
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
    
    class Meta:
        model = Video
        fields = [
            'id', 'title', 'slug', 'description', 'video_type',
            'youtube_url', 'video_file', 'thumbnail', 'duration', 'category',
            'author_name', 'status', 'language', 'is_featured',
            'views_count', 'published_at', 'created_at',
            'youtube_id', 'youtube_thumbnail_url'
        ]
