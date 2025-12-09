"""
URL configuration for Sauti CMS project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/auth/', include('users.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/videos/', include('videos.urls')),
    path('api/resources/', include('resources.urls')),
    path('api/faqs/', include('faqs.urls')),
    path('api/partners/', include('partners.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('api/content/', include('content.urls')),
    path('api/social/', include('social_media.urls')),
    
    # API Documentation (Swagger/OpenAPI)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# Serve media files in development and production
# In production, nginx will proxy /media/ requests to Django
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Customize admin site
admin.site.site_header = "Sauti CMS Administration"
admin.site.site_title = "Sauti CMS"
admin.site.index_title = "Welcome to Sauti 116 helpline CMS"
