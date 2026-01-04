from django.urls import path
from .views import GlobalSettingsView, OrganizationProfileView
from cms.views import SingletonHistoryAPIView
from .models import GlobalSettings, OrganizationProfile

urlpatterns = [
    path('', GlobalSettingsView.as_view(), name='global-settings'),
    path('history/', SingletonHistoryAPIView.as_view(model=GlobalSettings), name='global-settings-history'),
    path('organization/', OrganizationProfileView.as_view(), name='organization-profile'),
    path('organization/history/', SingletonHistoryAPIView.as_view(model=OrganizationProfile), name='organization-profile-history'),
]
