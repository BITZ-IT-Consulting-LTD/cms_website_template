from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SocialPostViewSet, contact_information, social_media_channels

router = DefaultRouter()
router.register(r'posts', SocialPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('channels/', social_media_channels, name='social-media-channels'),
    path('contact/', contact_information, name='contact-information'),
]
