from rest_framework import serializers
from .models import Post, Category, Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag model"""
    
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']
        read_only_fields = ['slug']


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model"""
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'created_at']
        read_only_fields = ['slug', 'created_at']


class PostListSerializer(serializers.ModelSerializer):
    """Serializer for listing posts (summary view)"""
    author_name = serializers.CharField(source='author.get_full_name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    featured_image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'post_type', 'excerpt', 'author_name',
            'category_name', 'tags', 'featured_image', 'status',
            'language', 'views_count', 'is_featured', 'published_at',
            'scheduled_publish_at', 'created_at', 'updated_at'
        ]
    
    def get_featured_image(self, obj):
        """Return absolute URL for featured image"""
        if obj.featured_image:
            # Check if it's already a full URL (external URL stored as string)
            image_value = str(obj.featured_image)
            if image_value.startswith('http://') or image_value.startswith('https://'):
                return image_value
            
            # It's a file field, get the relative URL
            try:
                image_url = obj.featured_image.url
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
                return f"{scheme}://{host}{image_url}"
            # Fallback if no request context
            return f"http://localhost:8080{image_url}" if image_url else None
        return None


class PostDetailSerializer(serializers.ModelSerializer):
    """Serializer for post detail view"""
    author = serializers.StringRelatedField(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    featured_image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'post_type', 'content', 'excerpt', 'author',
            'category', 'tags', 'featured_image', 'status', 'language',
            'views_count', 'is_featured', 'published_at', 'scheduled_publish_at',
            'created_at', 'updated_at'
        ]
    
    def get_featured_image(self, obj):
        """Return absolute URL for featured image"""
        if obj.featured_image:
            # Check if it's already a full URL (external URL stored as string)
            image_value = str(obj.featured_image)
            if image_value.startswith('http://') or image_value.startswith('https://'):
                return image_value
            
            # It's a file field, get the relative URL
            try:
                image_url = obj.featured_image.url
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
                return f"{scheme}://{host}{image_url}"
            # Fallback if no request context
            return f"http://localhost:8080{image_url}" if image_url else None
        return None


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating/updating posts"""
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        required=False
    )

    class Meta:
        model = Post
        fields = [
            'title', 'slug', 'post_type', 'content', 'excerpt', 'category',
            'tags', 'featured_image', 'status', 'language', 'is_featured',
            'scheduled_publish_at'
        ]
        extra_kwargs = {'slug': {'required': False}}
    
    def validate_status(self, value):
        """Validate that only editors can publish"""
        request = self.context.get('request')
        if value == Post.Status.PUBLISHED and request.user:
            if not request.user.can_publish():
                raise serializers.ValidationError(
                    "Only Editors and Admins can publish posts."
                )
        return value
