from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SocialPostViewSet, social_channels, contact_information

router = DefaultRouter()
router.register(r'posts', SocialPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('channels/', social_channels, name='social-channels'),
    path('contact/', contact_information, name='contact-information'),
]
