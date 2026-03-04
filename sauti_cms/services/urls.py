from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, HelpServiceViewSet, HelpStepViewSet

router = DefaultRouter()
router.register(r'help-services', HelpServiceViewSet, basename='help-service')
router.register(r'help-steps', HelpStepViewSet, basename='help-step')
router.register(r'', ServiceViewSet)

urlpatterns = router.urls
