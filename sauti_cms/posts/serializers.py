from rest_framework import serializers
from .models import Post, Category, Tag, PostImage


def _relative_image_url(image):
    """Return a relative URL for an image field (frontend proxy handles it)."""
    if not image:
        return None
    image_value = str(image)
    if image_value.startswith('http://') or image_value.startswith('https://'):
        return image_value
    try:
        return image.url
    except (ValueError, AttributeError):
        return None


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


class PostImageSerializer(serializers.ModelSerializer):
    """
    Serializer for a single gallery image belonging to a post.

    `image` is kept as a plain writable ModelSerializer field (required for
    multipart uploads to actually save the file) and rewritten to a relative
    URL in `to_representation` instead of being redeclared as a
    SerializerMethodField of the same name -- redeclaring it that way is
    exactly what silently made uploads read-only in videos/serializers.py.
    """
    class Meta:
        model = PostImage
        fields = ['id', 'post', 'image', 'caption', 'alt_text', 'order', 'created_at']
        read_only_fields = ['id', 'post', 'created_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['image'] = _relative_image_url(instance.image)
        # Derivatives generated on save (see Post model + imaging.derivatives).
        # Fall back to the original when a row predates this feature or
        # Pillow couldn't decode the source, so callers never get a blank URL.
        data['image_thumbnail'] = _relative_image_url(instance.image_thumbnail) or data['image']
        data['image_medium'] = _relative_image_url(instance.image_medium) or data['image']
        return data


class PostListSerializer(serializers.ModelSerializer):
    """Serializer for listing posts (summary view)"""
    author_name = serializers.SerializerMethodField()
    category_name = serializers.CharField(source='category.name', read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    featured_image = serializers.SerializerMethodField()
    featured_image_thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'post_type', 'excerpt', 'author_name',
            'category_name', 'tags', 'featured_image', 'featured_image_thumbnail',
            'status', 'language', 'views_count', 'is_featured', 'published_at',
            'scheduled_publish_at', 'created_at', 'updated_at'
        ]

    def get_author_name(self, obj):
        """Full name if set, else fall back to username (avoids blank 'Unknown' author)"""
        if not obj.author:
            return ''
        return obj.author.get_full_name() or obj.author.username

    def get_featured_image(self, obj):
        """Return relative URL for featured image (frontend proxy handles it)"""
        return _relative_image_url(obj.featured_image)

    def get_featured_image_thumbnail(self, obj):
        """
        Card/list-sized derivative of featured_image, generated on save.
        Falls back to the full-resolution original for rows saved before
        derivatives existed, or when Pillow couldn't decode the source --
        callers should never have to know which case they're in.
        """
        return _relative_image_url(obj.featured_image_thumbnail) or _relative_image_url(obj.featured_image)


class PostDetailSerializer(serializers.ModelSerializer):
    """Serializer for post detail view"""
    author = serializers.StringRelatedField(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    featured_image = serializers.SerializerMethodField()
    featured_image_thumbnail = serializers.SerializerMethodField()
    featured_image_medium = serializers.SerializerMethodField()
    secondary_image = serializers.SerializerMethodField()
    images = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'post_type', 'content', 'excerpt', 'author',
            'category', 'tags', 'featured_image', 'featured_image_thumbnail',
            'featured_image_medium', 'secondary_image', 'images', 'status', 'language',
            'views_count', 'is_featured', 'published_at', 'scheduled_publish_at',
            'created_at', 'updated_at'
        ]

    def get_featured_image(self, obj):
        return _relative_image_url(obj.featured_image)

    def get_featured_image_thumbnail(self, obj):
        """Falls back to the original when no derivative exists yet."""
        return _relative_image_url(obj.featured_image_thumbnail) or _relative_image_url(obj.featured_image)

    def get_featured_image_medium(self, obj):
        """Falls back to the original when no derivative exists yet."""
        return _relative_image_url(obj.featured_image_medium) or _relative_image_url(obj.featured_image)

    def get_secondary_image(self, obj):
        return _relative_image_url(obj.secondary_image)


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
            'tags', 'featured_image', 'secondary_image', 'status', 'language', 'is_featured',
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
