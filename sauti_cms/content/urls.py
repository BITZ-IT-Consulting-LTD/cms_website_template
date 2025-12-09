from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SiteContentViewSet

router = DefaultRouter()
router.register(r'', SiteContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
