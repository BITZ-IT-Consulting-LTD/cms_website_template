from django.urls import path
from .views import GlobalSettingsView

# DEPRECATED: The router and SiteSettingViewSet are deprecated.
# from rest_framework.routers import DefaultRouter
# from .views import SiteSettingViewSet

# router = DefaultRouter()
# router.register(r'sitesettings', SiteSettingViewSet, basename='sitesetting')

urlpatterns = [
    path('settings/', GlobalSettingsView.as_view(), name='global-settings'),
]
