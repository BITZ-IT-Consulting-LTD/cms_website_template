from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .serializers import HistoricalRecordSerializer

class HistoryMixin:
    @action(detail=True, methods=['get'], permission_classes=[IsAdminUser])
    def history(self, request, pk=None):
        instance = self.get_object()
        history = instance.history.all().order_by('-history_date')
        serializer = HistoricalRecordSerializer(history, many=True)
        return Response(serializer.data)
