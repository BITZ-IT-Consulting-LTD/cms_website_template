from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SocialPostViewSet, contact_information

router = DefaultRouter()
router.register(r'posts', SocialPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', contact_information, name='contact-information'),
]
