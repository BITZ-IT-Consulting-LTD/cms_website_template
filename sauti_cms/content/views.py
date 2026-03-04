from rest_framework import viewsets, permissions
from .models import SiteContent, CoreValue, Contact, ProtectionApproach, TeamMember
from .serializers import SiteContentSerializer, CoreValueSerializer, ContactSerializer, ProtectionApproachSerializer, TeamMemberSerializer

class OwnershipViewSetMixin:
    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            last_updated_by=self.request.user
        )

    def perform_update(self, serializer):
        serializer.save(last_updated_by=self.request.user)

class SiteContentViewSet(OwnershipViewSetMixin, viewsets.ModelViewSet):
    queryset = SiteContent.objects.all()
    serializer_class = SiteContentSerializer
    lookup_field = 'key'
    pagination_class = None  # Disable pagination to return all content for admin filtering

    def get_permissions(self):
        """
        Allow public read access, but require authentication for write access.
        """
        if self.action in ['list', 'retrieve', 'options']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class CoreValueViewSet(OwnershipViewSetMixin, viewsets.ModelViewSet):
    queryset = CoreValue.objects.filter(is_active=True)
    serializer_class = CoreValueSerializer
    pagination_class = None  # Disable pagination

    def get_permissions(self):
        """
        Allow public read access, but require authentication for write access.
        """
        if self.action in ['list', 'retrieve', 'options']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class ContactViewSet(OwnershipViewSetMixin, viewsets.ModelViewSet):
    queryset = Contact.objects.filter(is_visible=True).order_by('order')
    serializer_class = ContactSerializer
    pagination_class = None

    def get_permissions(self):
        """
        Allow public read access, but require authentication for write access.
        """
        if self.action in ['list', 'retrieve', 'options']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class ProtectionApproachViewSet(OwnershipViewSetMixin, viewsets.ModelViewSet):
    queryset = ProtectionApproach.objects.filter(is_active=True).order_by('order')
    serializer_class = ProtectionApproachSerializer
    pagination_class = None

    def get_permissions(self):
        """
        Allow public read access, but require authentication for write access.
        """
        if self.action in ['list', 'retrieve', 'options']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class TeamMemberViewSet(OwnershipViewSetMixin, viewsets.ModelViewSet):
    queryset = TeamMember.objects.filter(is_active=True).order_by('order')
    serializer_class = TeamMemberSerializer
    pagination_class = None

    def get_permissions(self):
        """
        Allow public read access, but require authentication for write access.
        """
        if self.action in ['list', 'retrieve', 'options']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
