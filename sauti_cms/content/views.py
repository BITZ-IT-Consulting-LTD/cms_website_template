from rest_framework import viewsets, permissions
from .models import SiteContent, CoreValue, Contact, ProtectionApproach, TeamMember, WhoWeAreImage, OperationsImage
from .serializers import SiteContentSerializer, CoreValueSerializer, ContactSerializer, ProtectionApproachSerializer, TeamMemberSerializer, WhoWeAreImageSerializer, OperationsImageSerializer

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
    queryset = CoreValue.objects.all()
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

    def get_queryset(self):
        """
        Public site should only see active values. Admin site (authenticated)
        should see all, including hidden ones, so they can be re-activated.
        """
        queryset = CoreValue.objects.all()
        if not self.request.user.is_authenticated:
            return queryset.filter(is_active=True)
        return queryset


class ContactViewSet(OwnershipViewSetMixin, viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('order')
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

    def get_queryset(self):
        """
        Public site should only see visible contacts. Admin site (authenticated)
        should see all, including hidden ones, so they can be re-activated.
        """
        queryset = Contact.objects.all().order_by('order').prefetch_related('extra_values')
        if not self.request.user.is_authenticated:
            return queryset.filter(is_visible=True)
        return queryset


class ProtectionApproachViewSet(OwnershipViewSetMixin, viewsets.ModelViewSet):
    queryset = ProtectionApproach.objects.all().order_by('order')
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

    def get_queryset(self):
        """
        Public site should only see active approaches. Admin site (authenticated)
        should see all, including hidden ones, so they can be re-activated.
        """
        queryset = ProtectionApproach.objects.all().order_by('order')
        if not self.request.user.is_authenticated:
            return queryset.filter(is_active=True)
        return queryset


class TeamMemberViewSet(OwnershipViewSetMixin, viewsets.ModelViewSet):
    queryset = TeamMember.objects.all().order_by('order')
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

    def get_queryset(self):
        """
        Public site should only see active team members. Admin site (authenticated)
        should see all, including hidden ones, so they can be re-activated.
        """
        queryset = TeamMember.objects.all().order_by('order')
        if not self.request.user.is_authenticated:
            return queryset.filter(is_active=True)
        return queryset


class WhoWeAreImageViewSet(OwnershipViewSetMixin, viewsets.ModelViewSet):
    queryset = WhoWeAreImage.objects.all().order_by('position')
    serializer_class = WhoWeAreImageSerializer
    pagination_class = None
    lookup_field = 'position'

    def get_permissions(self):
        """
        Allow public read access, but require authentication for write access.
        """
        if self.action in ['list', 'retrieve', 'options']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """
        Public site should only see active images. Admin site (authenticated)
        should see all, including hidden ones, so they can be re-activated.
        """
        queryset = WhoWeAreImage.objects.all().order_by('position')
        if not self.request.user.is_authenticated:
            return queryset.filter(is_active=True)
        return queryset


class OperationsImageViewSet(OwnershipViewSetMixin, viewsets.ModelViewSet):
    queryset = OperationsImage.objects.all().order_by('position')
    serializer_class = OperationsImageSerializer
    pagination_class = None
    lookup_field = 'position'

    def get_permissions(self):
        """
        Allow public read access, but require authentication for write access.
        """
        if self.action in ['list', 'retrieve', 'options']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """
        Public site should only see active images. Admin site (authenticated)
        should see all, including hidden ones, so they can be re-activated.
        """
        queryset = OperationsImage.objects.all().order_by('position')
        if not self.request.user.is_authenticated:
            return queryset.filter(is_active=True)
        return queryset
