from django.urls import path
from .views import NormalizedCallStatsView

urlpatterns = [
    path('', NormalizedCallStatsView.as_view(), name='normalized-call-stats-v1'),
]
