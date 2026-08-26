from django.urls import path
from .views import (
    FeedbackCreateView, FeedbackListView, FeedbackDetailView,
    FeedbackExportPDFView, FeedbackExportCSVView,
)

urlpatterns = [
    path('feedback/', FeedbackCreateView.as_view(), name='feedback-create'),
    path('feedback/list/', FeedbackListView.as_view(), name='feedback-list'),
    path('feedback/export/csv/', FeedbackExportCSVView.as_view(), name='feedback-export-csv'),
    path('feedback/<int:pk>/export/pdf/', FeedbackExportPDFView.as_view(), name='feedback-export-pdf'),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='feedback-detail'),
]
