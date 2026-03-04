from django.urls import path
from .views import PartnerListCreateView, PartnerDetailView
from cms.views import HistoryAPIView
from .models import Partner

app_name = 'partners'

urlpatterns = [
    path('', PartnerListCreateView.as_view(), name='partner-list'),
    path('<slug:slug>/', PartnerDetailView.as_view(), name='partner-detail'),
    path('<int:pk>/history/', HistoryAPIView.as_view(model=Partner), name='partner-history'),
]
