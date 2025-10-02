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
    List all users (Admin only)
    GET /api/auth/users/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if not self.request.user.is_admin:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only administrators can view all users.")
        return super().get_queryset()
