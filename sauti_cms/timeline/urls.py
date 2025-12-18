from rest_framework.routers import DefaultRouter
from .views import TimelineEventViewSet

router = DefaultRouter()
router.register(r'', TimelineEventViewSet)

urlpatterns = router.urls
