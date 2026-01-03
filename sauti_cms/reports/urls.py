from django.urls import path
from .views import (
    ReportCreateView, ReportListView, ReportDetailView, ReportFollowUpCreateView,
    PublicReportStatsView
)
from cms.views import HistoryAPIView
from .models import Report

app_name = 'reports'

urlpatterns = [
    path('', ReportCreateView.as_view(), name='report-create'),
    path('list/', ReportListView.as_view(), name='report-list'),
    path('<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('<int:pk>/history/', HistoryAPIView.as_view(model=Report), name='report-history'),
    path('<int:report_id>/followup/', ReportFollowUpCreateView.as_view(), name='followup-create'),
    path('stats/public/', PublicReportStatsView.as_view(), name='report-stats-public'),
]
