from rest_framework import generics, permissions
from .models import FeedbackMessage
from .serializers import FeedbackMessageSerializer

class FeedbackCreateView(generics.CreateAPIView):
    """
    POST /api/contact/feedback/ - Submit general feedback/inquiry
    Public endpoint.
    """
    queryset = FeedbackMessage.objects.all()
    serializer_class = FeedbackMessageSerializer
    permission_classes = [permissions.AllowAny]

class FeedbackListView(generics.ListAPIView):
    """
    GET /api/contact/feedback/list/ - List general feedback/inquiries
    Admin only.
    """
    queryset = FeedbackMessage.objects.all().order_by('-submitted_at')
    serializer_class = FeedbackMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET/PATCH/DELETE /api/contact/feedback/<id>/ - Manage individual feedback
    Admin only.
    """
    queryset = FeedbackMessage.objects.all()
    serializer_class = FeedbackMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        from django.utils import timezone

        instance = serializer.instance
        was_processed = instance.is_processed
        obj = serializer.save()

        # Stamp who reviewed it (and when) as it transitions to processed;
        # clear the stamp if it's moved back to unreviewed.
        if obj.is_processed and not was_processed:
            obj.reviewed_by = self.request.user
            obj.reviewed_at = timezone.now()
            obj.save(update_fields=['reviewed_by', 'reviewed_at'])
        elif not obj.is_processed and was_processed:
            obj.reviewed_by = None
            obj.reviewed_at = None
            obj.save(update_fields=['reviewed_by', 'reviewed_at'])
