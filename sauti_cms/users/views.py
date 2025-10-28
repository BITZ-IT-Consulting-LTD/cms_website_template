from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import (
    UserSerializer, UserCreateSerializer, UserProfileSerializer
)

User = get_user_model()


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
    List all users (Admin/Editor)
    GET /api/auth/users/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Only admins and editors can view all users
        if not self.request.user.is_editor:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only administrators and editors can view all users.")
        
        # Filter by role if specified
        role = self.request.query_params.get('role')
        if role:
            return User.objects.filter(role=role.upper())
        
        return User.objects.all().order_by('-created_at')


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get/Update/Delete user details (Admin only for delete)
    GET/PUT/DELETE /api/auth/users/<id>/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_update(self, serializer):
        # Only admins can update user roles
        if 'role' in serializer.validated_data and not self.request.user.is_admin:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only administrators can change user roles.")
        serializer.save()
    
    def perform_destroy(self, instance):
        # Only admins can delete users
        if not self.request.user.is_admin:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only administrators can delete users.")
        instance.delete()
