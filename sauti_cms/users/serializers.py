from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, Role, Permission


class PermissionSerializer(serializers.ModelSerializer):
    """Read-only: the permission catalog is fixed (seeded by migration), only
    which permissions belong to a Role is editable."""
    class Meta:
        model = Permission
        fields = ['id', 'codename', 'label', 'category']


class RoleSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(many=True, queryset=Permission.objects.all())
    permission_details = PermissionSerializer(source='permissions', many=True, read_only=True)
    user_count = serializers.IntegerField(source='users.count', read_only=True)

    class Meta:
        model = Role
        fields = ['id', 'name', 'slug', 'is_default', 'permissions', 'permission_details', 'user_count']
        read_only_fields = ['id', 'slug', 'is_default']

    def create(self, validated_data):
        from django.utils.text import slugify
        validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)


class RoleBriefSerializer(serializers.ModelSerializer):
    """Lightweight nested representation for display in user lists (avoids
    shipping every role's full permission set with every user row)."""
    class Meta:
        model = Role
        fields = ['id', 'name', 'slug']


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    role_detail = RoleBriefSerializer(source='role', read_only=True)
    # Frontend nav/route gating (DashboardLayout's Users link, router guards)
    # used to check the old hardcoded role==='ADMIN' string; now that role is
    # a freely-editable FK, gating has to reflect actual granted permissions
    # instead of a role's name.
    is_admin = serializers.ReadOnlyField()
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'role', 'role_detail', 'phone_number', 'organization', 'is_active',
            'is_superuser', 'is_admin', 'permissions', 'created_at', 'updated_at'
        ]
        # is_superuser is exposed read-only so the admin UI can badge the
        # protected super-admin account; it can't be granted via the API.
        read_only_fields = ['id', 'is_superuser', 'created_at', 'updated_at']

    def get_permissions(self, obj):
        if obj.is_superuser:
            return list(Permission.objects.values_list('codename', flat=True))
        if not obj.role_id:
            return []
        return list(obj.role.permissions.values_list('codename', flat=True))


class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for user registration (Admin only)"""
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'password2',
            'first_name', 'last_name', 'role', 'phone_number',
            'organization'
        ]
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile (self)"""
    role_detail = RoleBriefSerializer(source='role', read_only=True)
    is_admin = serializers.ReadOnlyField()
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'role', 'role_detail', 'is_admin', 'permissions',
            'phone_number', 'organization', 'created_at'
        ]
        read_only_fields = ['id', 'username', 'role', 'created_at']

    def get_permissions(self, obj):
        if obj.is_superuser:
            return list(Permission.objects.values_list('codename', flat=True))
        if not obj.role_id:
            return []
        return list(obj.role.permissions.values_list('codename', flat=True))
