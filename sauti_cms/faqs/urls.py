from django.urls import path
from .views import FAQListCreateView, FAQDetailView, FAQCategoryListView, FAQCategoryDetailView

app_name = 'faqs'

urlpatterns = [
    path('', FAQListCreateView.as_view(), name='faq-list'),
    path('categories/', FAQCategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', FAQCategoryDetailView.as_view(), name='category-detail'),
    path('<int:pk>/', FAQDetailView.as_view(), name='faq-detail'),
]
