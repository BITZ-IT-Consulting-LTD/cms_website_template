from django.contrib.auth.models import AbstractUser
from django.db import models


class Permission(models.Model):
    """
    A single assignable capability (e.g. "manage_posts"). This is a fixed
    catalog seeded by a data migration -- codenames are referenced directly
    in view code via User.has_permission(codename), so this table is not
    meant to be created/renamed through the admin UI, only assigned to
    Roles. Deliberately separate from Django's built-in auth.Permission,
    which is per-model/content-type (and, with django-simple-history in this
    project, would include a flood of auto-generated "historical" rows) --
    this is a small curated set matching real app-level capabilities.
    """
    codename = models.SlugField(max_length=50, unique=True)
    label = models.CharField(max_length=100)
    category = models.CharField(max_length=50, help_text='Groups permissions in the admin UI, e.g. "Content"')

    class Meta:
        ordering = ['category', 'label']

    def __str__(self):
        return self.label


class Role(models.Model):
    """
    A named, editable bundle of Permissions. Four roles (admin/editor/
    author/viewer) are seeded as defaults matching this app's original
    hardcoded behavior, but unlike the old TextChoices enum, both their
    permission sets and the existence of additional custom roles are fully
    editable from the admin UI.
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    is_default = models.BooleanField(
        default=False,
        help_text='Seeded role (admin/editor/author/viewer) -- cannot be deleted, but its permissions can still be edited.'
    )
    permissions = models.ManyToManyField(Permission, blank=True, related_name='roles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class User(AbstractUser):
    """
    Custom User model with role-based access control. `role` points at a
    Role record whose Permission set determines what the user can do --
    see Role.has_permission() usage sitewide instead of the old fixed
    is_admin/is_editor/is_author properties.
    """

    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='users',
        help_text='User role for access control'
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    organization = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.username} ({self.role.name if self.role else 'No role'})"

    def has_permission(self, codename):
        """
        True if this user carries the named Permission via their Role, or
        if they're a Django superuser (superusers always bypass -- matches
        every existing call site's prior is_admin/is_editor/is_author
        behavior, which all treated is_superuser as an automatic pass).
        """
        if self.is_superuser:
            return True
        if not self.role_id:
            return False
        return self.role.permissions.filter(codename=codename).exists()

    @property
    def is_admin(self):
        # Kept only for the seeded-role's own admin-ness check in
        # views/serializers that still read it as a coarse label (e.g.
        # display purposes); permission GATES should call has_permission()
        # with a specific codename instead. Superusers always count.
        return self.is_superuser or self.has_permission('manage_users')

    def can_publish(self):
        """Check if user can publish content"""
        return self.has_permission('manage_posts')
