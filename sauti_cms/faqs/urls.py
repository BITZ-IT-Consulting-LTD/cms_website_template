from django.urls import path
from .views import FAQListCreateView, FAQDetailView, FAQCategoryListView, FAQCategoryDetailView
from cms.views import HistoryAPIView
from .models import FAQ

app_name = 'faqs'

urlpatterns = [
    path('', FAQListCreateView.as_view(), name='faq-list'),
    path('categories/', FAQCategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', FAQCategoryDetailView.as_view(), name='category-detail'),
    path('<int:pk>/', FAQDetailView.as_view(), name='faq-detail'),
    path('<int:pk>/history/', HistoryAPIView.as_view(model=FAQ), name='faq-history'),
]
