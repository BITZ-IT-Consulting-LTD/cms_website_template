from rest_framework.routers import DefaultRouter
from .views import SiteSettingViewSet

router = DefaultRouter()
router.register(r'sitesettings', SiteSettingViewSet, basename='sitesetting')

urlpatterns = router.urls
