from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import HistoricalRecordSerializer

class HistoryAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    serializer_class = HistoricalRecordSerializer

    def get_queryset(self):
        # We don't use the standard queryset here as we want the history of a specific object
        return self.model.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        history = instance.history.all().order_by('-history_date')
        serializer = self.get_serializer(history, many=True)
        return Response(serializer.data)

    @classmethod
    def as_view(cls, model, **initkwargs):
        cls.model = model
        return super().as_view(**initkwargs)

class SingletonHistoryAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    serializer_class = HistoricalRecordSerializer

    def get_object(self):
        return self.model.objects.first()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response([])
        history = instance.history.all().order_by('-history_date')
        serializer = self.get_serializer(history, many=True)
        return Response(serializer.data)

    @classmethod
    def as_view(cls, model, **initkwargs):
        cls.model = model
        return super().as_view(**initkwargs)
