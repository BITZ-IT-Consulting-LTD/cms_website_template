from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework.exceptions import PermissionDenied
from .serializers import (
    UserSerializer, UserCreateSerializer, UserProfileSerializer,
    RoleSerializer, PermissionSerializer
)
from .models import Role, Permission

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom serializer to include user data in token response
    """
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add user data to the response
        data['user'] = UserSerializer(self.user).data

        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom login view that returns tokens + user data
    """
    serializer_class = CustomTokenObtainPairSerializer


class UserRegistrationView(generics.CreateAPIView):
    """
    User registration endpoint (Admin only)
    POST /api/auth/register/
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        # Only admins can create users
        if not self.request.user.is_admin:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only administrators can register new users.")
        serializer.save()


class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    Get/Update current user profile
    GET/PUT /api/auth/profile/
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user


class UserListView(generics.ListAPIView):
    """
    List all users (Admin only)
    GET /api/auth/users/

    This is the admin user-management listing, distinct from the self-service
    `/api/auth/profile/` endpoint (UserProfileView) that any authenticated user
    already uses to view/edit their own account.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only admins can view the full user list.
        if not self.request.user.is_admin:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only administrators can view all users.")

        # Filter by role if specified (role is now a FK -- filter by slug)
        role = self.request.query_params.get('role')
        if role:
            return User.objects.filter(role__slug=role.lower())

        return User.objects.all().order_by('-created_at')


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get/Update/Delete user details (Admin only)
    GET/PUT/DELETE /api/auth/users/<id>/

    This is the admin user-management endpoint for managing *other* users'
    accounts, distinct from the self-service `/api/auth/profile/` endpoint
    (UserProfileView) that any authenticated user uses for their own account.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only admins can view, edit, or delete other users' accounts. This
        # gates GET/PUT/PATCH/DELETE uniformly, since DRF's get_object() is
        # built on top of get_queryset().
        if not self.request.user.is_admin:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only administrators can manage user accounts.")
        return User.objects.all()

    def perform_update(self, serializer):
        from rest_framework.exceptions import PermissionDenied
        request_user = self.request.user
        instance = self.get_object()
        # Protect the super-admin: only another superuser may modify a
        # superuser account (role, active flag, etc.).
        if instance.is_superuser and not request_user.is_superuser:
            raise PermissionDenied("Only a super administrator can modify a super-admin account.")
        # Only admins can change roles.
        if 'role' in serializer.validated_data and not request_user.is_admin:
            raise PermissionDenied("Only administrators can change user roles.")
        serializer.save()

    def perform_destroy(self, instance):
        from rest_framework.exceptions import PermissionDenied
        request_user = self.request.user
        # Only admins can delete users
        if not request_user.is_admin:
            raise PermissionDenied("Only administrators can delete users.")
        # A super-admin account cannot be deleted by a non-superuser.
        if instance.is_superuser and not request_user.is_superuser:
            raise PermissionDenied("Super-admin accounts cannot be deleted.")
        # Prevent deleting your own account.
        if instance.pk == request_user.pk:
            raise PermissionDenied("You cannot delete your own account.")
        instance.delete()


class HasManageUsers(permissions.BasePermission):
    """Gates the Roles & Permissions admin UI -- same capability as the
    hardcoded is_admin checks above, expressed as a dynamic permission."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.has_permission('manage_users')


class PermissionListView(generics.ListAPIView):
    """
    GET /api/auth/permissions/ - the fixed permission catalog (read-only;
    only which permissions belong to a Role is editable).
    """
    queryset = Permission.objects.all().order_by('category', 'label')
    serializer_class = PermissionSerializer
    permission_classes = [HasManageUsers]


class RoleListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/auth/roles/ - list roles (seeded defaults + custom)
    POST /api/auth/roles/ - create a custom role
    """
    queryset = Role.objects.all().order_by('name')
    serializer_class = RoleSerializer
    permission_classes = [HasManageUsers]


class RoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET/PUT/PATCH/DELETE /api/auth/roles/<id>/
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [HasManageUsers]

    def perform_destroy(self, instance):
        if instance.is_default:
            raise PermissionDenied("Default roles can't be deleted.")
        if instance.users.exists():
            raise PermissionDenied("This role is still assigned to users -- reassign them first.")
        instance.delete()
