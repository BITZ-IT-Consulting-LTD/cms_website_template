from django.urls import path
from .views import FAQListCreateView, FAQDetailView, FAQCategoryListView

app_name = 'faqs'

urlpatterns = [
    path('', FAQListCreateView.as_view(), name='faq-list'),
    path('categories/', FAQCategoryListView.as_view(), name='category-list'),
    path('<int:pk>/', FAQDetailView.as_view(), name='faq-detail'),
]
