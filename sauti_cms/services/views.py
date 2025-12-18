from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.filter(is_visible=True).order_by('order')
    serializer_class = ServiceSerializer
    lookup_field = 'pk' # Use 'pk' for primary key lookup
