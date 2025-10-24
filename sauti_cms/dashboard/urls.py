from django.urls import path
from .views import DashboardStatsView, TopContentView

urlpatterns = [
    path('stats/', DashboardStatsView.as_view(), name='dashboard-stats'),
    path('top-content/', TopContentView.as_view(), name='dashboard-top-content'),
]
