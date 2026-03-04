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
