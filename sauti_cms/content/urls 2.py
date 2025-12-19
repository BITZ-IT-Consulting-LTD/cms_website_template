from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SiteContentViewSet, CoreValueViewSet

router = DefaultRouter()
router.register(r'site-content', SiteContentViewSet, basename='site-content')
router.register(r'core-values', CoreValueViewSet, basename='core-values')

urlpatterns = [
    path('', include(router.urls)),
]
