from rest_framework import viewsets
from .models import TimelineEvent
from .serializers import TimelineEventSerializer

class TimelineEventViewSet(viewsets.ModelViewSet):
    queryset = TimelineEvent.objects.all().order_by('order', 'year')
    serializer_class = TimelineEventSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, last_updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(last_updated_by=self.request.user)

    def get_queryset(self):
        """
        Public site should only see visible events.
        Admin site (authenticated) should see all.
        """
        queryset = TimelineEvent.objects.all().order_by('order', 'year')
        if not self.request.user.is_authenticated:
            return queryset.filter(is_visible=True)
        return queryset
