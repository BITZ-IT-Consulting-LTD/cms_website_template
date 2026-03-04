from rest_framework import viewsets, permissions
from .models import Service, HelpService, HelpStep
from .serializers import ServiceSerializer, HelpServiceSerializer, HelpStepSerializer

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.filter(is_visible=True).order_by('order')
    serializer_class = ServiceSerializer
    lookup_field = 'pk'

class HelpServiceViewSet(viewsets.ModelViewSet):
    queryset = HelpService.objects.all().order_by('homepage_display_order', 'order')
    serializer_class = HelpServiceSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class HelpStepViewSet(viewsets.ModelViewSet):
    queryset = HelpStep.objects.all().order_by('step_order')
    serializer_class = HelpStepSerializer
    permission_classes = [permissions.IsAuthenticated()]
