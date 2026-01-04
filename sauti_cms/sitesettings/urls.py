from django.urls import path
from .views import GlobalSettingsView
from cms.views import SingletonHistoryAPIView
from .models import GlobalSettings

urlpatterns = [
    path('', GlobalSettingsView.as_view(), name='global-settings'),
    path('history/', SingletonHistoryAPIView.as_view(model=GlobalSettings), name='global-settings-history'),
]
