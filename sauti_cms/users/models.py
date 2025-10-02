from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model with role-based access control.
    Roles: Admin, Editor, Author, Viewer
    """
    
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrator'
        EDITOR = 'EDITOR', 'Editor'
        AUTHOR = 'AUTHOR', 'Author'
        VIEWER = 'VIEWER', 'Viewer'
    
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.VIEWER,
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
        return f"{self.username} ({self.get_role_display()})"
    
    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN
    
    @property
    def is_editor(self):
        return self.role in [self.Role.ADMIN, self.Role.EDITOR]
    
    @property
    def is_author(self):
        return self.role in [self.Role.ADMIN, self.Role.EDITOR, self.Role.AUTHOR]
    
    def can_publish(self):
        """Check if user can publish content"""
        return self.role in [self.Role.ADMIN, self.Role.EDITOR]
    
    def can_delete(self):
        """Check if user can delete content"""
        return self.role == self.Role.ADMIN
