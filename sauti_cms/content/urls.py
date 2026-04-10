from rest_framework.routers import DefaultRouter
from .views import SiteContentViewSet, CoreValueViewSet, ContactViewSet, ProtectionApproachViewSet, TeamMemberViewSet, WhoWeAreImageViewSet, OperationsImageViewSet
from timeline.views import TimelineEventViewSet

router = DefaultRouter()
router.register(r'site-content', SiteContentViewSet, basename='site-content')
router.register(r'core-values', CoreValueViewSet, basename='core-value')
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'protection-approach', ProtectionApproachViewSet, basename='protection-approach')
router.register(r'team-members', TeamMemberViewSet, basename='team-member')
router.register(r'timeline-events', TimelineEventViewSet, basename='timeline-event')
router.register(r'who-we-are-images', WhoWeAreImageViewSet, basename='who-we-are-image')
router.register(r'operations-images', OperationsImageViewSet, basename='operations-image')

urlpatterns = router.urls