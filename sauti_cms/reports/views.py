from rest_framework import generics, permissions, status, serializers
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.conf import settings
from .models import Report, ReportFollowUp
from .serializers import (
    ReportCreateSerializer, ReportListSerializer, ReportDetailSerializer,
    ReportUpdateSerializer, ReportFollowUpCreateSerializer
)


class AllowAnyPost(permissions.BasePermission):
    """Allow anonymous POST, but require auth for other methods"""
    
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user.is_authenticated and request.user.is_editor


import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class ReportCreateView(generics.CreateAPIView):
    """
    POST /api/reports/ - Submit a report (anonymous allowed, no auth required)
    """
    queryset = Report.objects.all()
    serializer_class = ReportCreateSerializer
    permission_classes = [permissions.AllowAny]
    
    # Support file uploads
    # Support file uploads and JSON
    from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def perform_create(self, serializer):
        # Capture IP address and user agent for security
        request = self.request
        ip_address = self.get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        report = serializer.save(
            ip_address=ip_address,
            user_agent=user_agent
        )
        
        # Send notification email to admins
        self.send_notification_email(report)
    
    def get_client_ip(self, request):
        """Get client IP address"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def send_notification_email(self, report):
        """Send email notification about new report"""
        logger.info("Attempting to send notification email...")
        try:
            subject = f'New Report Submitted - {report.reference_number}'
            message = f'''
A new {report.get_category_display()} report has been submitted.

Reference Number: {report.reference_number}
Category: {report.get_category_display()}
Anonymous: {report.is_anonymous}
Location: {report.location or 'Not provided'}
Submitted: {report.created_at.strftime('%Y-%m-%d %H:%M')}

Please log in to the CMS to review this report.
            '''
            
            # Send to staff users with email
            from django.contrib.auth import get_user_model
            User = get_user_model()
            admin_emails = User.objects.filter(
                role__in=['ADMIN', 'EDITOR'],
                is_active=True,
                email__isnull=False
            ).values_list('email', flat=True)
            
            if admin_emails:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    list(admin_emails),
                    fail_silently=False,
                )
                logger.info("Notification email sent successfully.")
            else:
                logger.warning("No admin emails found to send notification.")
        except Exception as e:
            # Log error but don't fail the request
            logger.error(f"Failed to send notification email: {e}", exc_info=True)
    
    def create(self, request, *args, **kwargs):
        try:
            from django.db import transaction
            with transaction.atomic():
                serializer = self.get_serializer(data=request.data)
                if not serializer.is_valid():
                     logger.error(f"Validation Errors: {serializer.errors}")
                     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
                self.perform_create(serializer)
                
                # Database committed due to transaction block success
                
                # Return only reference number as per strict contract
                return Response({
                    'reference_number': serializer.instance.reference_number
                }, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Error creating report: {e}", exc_info=True)
            # Re-raise validation errors or handle gracefully
            if isinstance(e, (serializers.ValidationError, PermissionDenied)):
                 raise e
            return Response({"detail": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ReportListView(generics.ListAPIView):
    """
    GET /api/reports/ - List all reports (Editors/Admins only)
    """
    queryset = Report.objects.select_related('assigned_to')
    serializer_class = ReportListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if not self.request.user.is_editor:
            raise PermissionDenied("Only Editors and Admins can view reports.")
        
        queryset = super().get_queryset()
        
        # Filter by status
        status_filter = self.request.query_params.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        # Filter by category
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        
        # Filter by assigned user
        assigned_to_me = self.request.query_params.get('assigned_to_me')
        if assigned_to_me:
            queryset = queryset.filter(assigned_to=self.request.user)
        
        return queryset


class ReportDetailView(generics.RetrieveUpdateAPIView):
    """
    GET /api/reports/<id>/ - Get report detail (Editors/Admins only)
    PUT/PATCH /api/reports/<id>/ - Update report status (Editors/Admins only)
    """
    queryset = Report.objects.select_related('assigned_to')
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if not self.request.user.is_editor:
            raise PermissionDenied("Only Editors and Admins can view reports.")
        return super().get_queryset()
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ReportUpdateSerializer
        return ReportDetailSerializer

    def perform_update(self, serializer):
        from django.utils import timezone
        
        # Check for status changes
        instance = self.get_object()
        old_status = instance.status
        
        obj = serializer.save()
        
        if obj.status == Report.Status.ESCALATED and old_status != Report.Status.ESCALATED:
            obj.escalated_at = timezone.now()
            obj.save(update_fields=['escalated_at'])
            logger.info(f"Report {obj.reference_number} escalated by {self.request.user}")
            
        if obj.status == Report.Status.FORWARDED and old_status != Report.Status.FORWARDED:
            obj.forwarded_to_openchs_at = timezone.now()
            obj.save(update_fields=['forwarded_to_openchs_at'])
            logger.info(f"Report {obj.reference_number} forwarded to OpenCHS by {self.request.user}")


class ReportFollowUpCreateView(generics.CreateAPIView):
    """
    POST /api/reports/<report_id>/followup/ - Add follow-up action
    """
    queryset = ReportFollowUp.objects.all()
    serializer_class = ReportFollowUpCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        if not self.request.user.is_editor:
            raise PermissionDenied("Only Editors and Admins can add follow-ups.")
        serializer.save(created_by=self.request.user)


class PublicReportStatsView(generics.GenericAPIView):
    """
    GET /api/reports/stats/public/ - Public statistics for charts
    """
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        from django.db.models import Count
        from django.db.models.functions import TruncMonth
        from django.utils import timezone
        from datetime import timedelta
        
        # Cases by Category
        by_category = Report.objects.values('category').annotate(count=Count('id'))
        
        # Reports over time (last 6 months)
        six_months_ago = timezone.now() - timedelta(days=180)
        over_time = Report.objects.filter(created_at__gte=six_months_ago)\
            .annotate(month=TruncMonth('created_at'))\
            .values('month')\
            .annotate(count=Count('id'))\
            .order_by('month')
            
        return Response({
            'by_category': by_category,
            'over_time': over_time
        })


class NormalizedCallStatsView(generics.GenericAPIView):
    """
    GET /api/reports/stats/keypair/
    Consumes upstream SAUTI statistics and returns normalized key-pair JSON.
    Additive resource, safe for frontend consumption.
    """
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        from .services import fetch_normalized_call_stats
        data = fetch_normalized_call_stats()
        return Response(data)
