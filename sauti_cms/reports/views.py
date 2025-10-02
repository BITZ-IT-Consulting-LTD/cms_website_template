from rest_framework import generics, permissions, status
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


class ReportCreateView(generics.CreateAPIView):
    """
    POST /api/reports/ - Submit a report (anonymous allowed, no auth required)
    """
    queryset = Report.objects.all()
    serializer_class = ReportCreateSerializer
    permission_classes = [permissions.AllowAny]
    
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
                    fail_silently=True,
                )
        except Exception as e:
            # Log error but don't fail the request
            print(f"Failed to send notification email: {e}")
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Return only reference number to user
        return Response({
            'message': 'Report submitted successfully',
            'reference_number': serializer.instance.reference_number,
            'status': 'Your report has been received and will be reviewed by our team.'
        }, status=status.HTTP_201_CREATED)


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
