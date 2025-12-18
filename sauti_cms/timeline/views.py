from rest_framework import viewsets
from .models import TimelineEvent
from .serializers import TimelineEventSerializer

class TimelineEventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TimelineEvent.objects.filter(is_visible=True).order_by('order', 'year')
    serializer_class = TimelineEventSerializer
    lookup_field = 'pk' # Use 'pk' for primary key lookup
