from django.urls import path
from .views import DashboardStatsView, TopContentView, HelplineStatsView, HelplineChartsView

urlpatterns = [
    path('stats/', DashboardStatsView.as_view(), name='dashboard-stats'),
    path('top-content/', TopContentView.as_view(), name='dashboard-top-content'),
    path('helpline-stats/', HelplineStatsView.as_view(), name='helpline-stats'),
    path('helpline-charts/', HelplineChartsView.as_view(), name='helpline-charts'),
]
