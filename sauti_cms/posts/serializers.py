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
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'excerpt', 'author_name',
            'category_name', 'tags', 'featured_image', 'status',
            'language', 'views_count', 'is_featured', 'published_at',
            'created_at'
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    """Serializer for post detail view"""
    author = serializers.StringRelatedField(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'content', 'excerpt', 'author',
            'category', 'tags', 'featured_image', 'status', 'language',
            'views_count', 'is_featured', 'published_at', 'created_at',
            'updated_at'
        ]


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
            'title', 'slug', 'content', 'excerpt', 'category',
            'tags', 'featured_image', 'status', 'language', 'is_featured'
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
