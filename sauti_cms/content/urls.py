from rest_framework.routers import DefaultRouter
from .views import SiteContentViewSet, CoreValueViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'site-content', SiteContentViewSet, basename='site-content')
router.register(r'core-values', CoreValueViewSet, basename='core-value')
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = router.urls