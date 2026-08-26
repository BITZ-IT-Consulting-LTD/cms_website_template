from django.http import HttpResponse
from django.utils import timezone
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FeedbackMessage
from .serializers import FeedbackMessageSerializer, FeedbackCreateSerializer
from .exports import generate_feedback_pdf, write_feedback_csv

class FeedbackCreateView(generics.CreateAPIView):
    """
    POST /api/contact/feedback/ - Submit general feedback/inquiry
    Public endpoint.
    """
    queryset = FeedbackMessage.objects.all()
    # Use the restricted serializer so anonymous submitters can't set
    # is_processed/is_archived on their own message.
    serializer_class = FeedbackCreateSerializer
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


class FeedbackExportPDFView(APIView):
    """
    GET /api/contact/feedback/<id>/export/pdf/ - Single-message PDF download.
    Admin only.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            message = FeedbackMessage.objects.get(pk=pk)
        except FeedbackMessage.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=404)

        buffer = generate_feedback_pdf(message)
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = (
            f'attachment; filename="feedback-{message.id}.pdf"'
        )
        return response


class FeedbackExportCSVView(APIView):
    """
    GET /api/contact/feedback/export/csv/?status=pending|reviewed|archived|all
    Bulk CSV download, scoped to the active status filter. Admin only.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        status_filter = (request.query_params.get('status') or 'all').lower()
        queryset = FeedbackMessage.objects.all().order_by('-submitted_at')

        if status_filter == 'pending':
            queryset = queryset.filter(is_processed=False, is_archived=False)
        elif status_filter == 'reviewed':
            queryset = queryset.filter(is_processed=True, is_archived=False)
        elif status_filter == 'archived':
            queryset = queryset.filter(is_archived=True)
        # 'all' (or anything unrecognised) leaves the queryset unfiltered.

        date_str = timezone.localtime(timezone.now()).strftime('%Y-%m-%d')
        filename = f"general-feedback-{status_filter}-{date_str}.csv"

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return write_feedback_csv(response, queryset)
