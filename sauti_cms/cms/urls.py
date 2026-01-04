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
    path('auth/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('videos/', include('videos.urls')),
    path('resources/', include('resources.urls')),
    path('faqs/', include('faqs.urls')),
    path('partners/', include('partners.urls')),
    path('reports/', include('reports.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('content/', include('content.urls')),
    path('social/', include('social_media.urls')),
    path('timeline/', include('timeline.urls')), 
    path('services/', include('services.urls')), 
    path('sitesettings/', include('sitesettings.urls')),
    path('contact/', include('contact.urls')),

    # V1 Additive Resources (Normalized Stats)
    path('v1/calls/stats/keypair/', include('reports.urls_v1')),
    
    # API Documentation (Swagger/OpenAPI)
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
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