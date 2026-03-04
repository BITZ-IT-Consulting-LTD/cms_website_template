from django.urls import path
from .views import FeedbackCreateView, FeedbackListView, FeedbackDetailView

urlpatterns = [
    path('feedback/', FeedbackCreateView.as_view(), name='feedback-create'),
    path('feedback/list/', FeedbackListView.as_view(), name='feedback-list'),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='feedback-detail'),
]
