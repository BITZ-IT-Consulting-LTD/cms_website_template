from rest_framework import serializers
from .models import Video, VideoCategory


class VideoCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCategory
        fields = ['id', 'name', 'slug', 'description', 'created_at']


def _relative_file_url(file_field):
    """Return relative URL for a FileField/ImageField (frontend proxy handles it)"""
    if not file_field:
        return None
    file_str = str(file_field)
    if file_str.startswith('http://') or file_str.startswith('https://'):
        # It's already a full URL (external URL stored as string), return as-is
        return file_str
    try:
        return file_field.url
    except (ValueError, AttributeError):
        return None


def _author_name(user):
    """Full name if set, else fall back to username (avoids blank 'Unknown' author)"""
    if not user:
        return ''
    return user.get_full_name() or user.username


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
            'published_at', 'scheduled_publish_at', 'created_at', 'updated_at',
            'youtube_id', 'youtube_embed_url', 'youtube_thumbnail_url'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at', 'views_count']

    def to_representation(self, instance):
        # video_file/thumbnail must stay writable model fields (for uploads to save),
        # so the host-mismatch URL fix is applied here instead of via SerializerMethodField.
        data = super().to_representation(instance)
        data['thumbnail'] = _relative_file_url(instance.thumbnail)
        data['video_file'] = _relative_file_url(instance.video_file)
        data['author_name'] = _author_name(instance.author)
        # thumbnail_small is a server-generated derivative (see Video.save());
        # kept out of Meta.fields entirely (never writable) and added here,
        # falling back to the full thumbnail when no derivative exists yet.
        data['thumbnail_small_url'] = _relative_file_url(instance.thumbnail_small) or data['thumbnail']
        return data

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
            'views_count', 'published_at', 'scheduled_publish_at', 'created_at', 'updated_at',
            'youtube_id', 'youtube_thumbnail_url'
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['thumbnail'] = _relative_file_url(instance.thumbnail)
        data['video_file'] = _relative_file_url(instance.video_file)
        data['author_name'] = _author_name(instance.author)
        data['thumbnail_small_url'] = _relative_file_url(instance.thumbnail_small) or data['thumbnail']
        return data