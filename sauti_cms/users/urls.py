from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView, UserRegistrationView, UserProfileView,
    UserListView, UserDetailView,
    PermissionListView, RoleListCreateView, RoleDetailView
)

app_name = 'users'

urlpatterns = [
    # Authentication
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='register'),

    # User management
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Roles & permissions
    path('permissions/', PermissionListView.as_view(), name='permission-list'),
    path('roles/', RoleListCreateView.as_view(), name='role-list'),
    path('roles/<int:pk>/', RoleDetailView.as_view(), name='role-detail'),
]
