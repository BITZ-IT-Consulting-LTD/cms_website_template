from django.urls import path
from .views import SiteContentViewSet

urlpatterns = [
    path('', SiteContentViewSet.as_view({'get': 'list', 'post': 'create'}), name='site-content-list'),
    path('<str:key>/', SiteContentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='site-content-detail'),
]
