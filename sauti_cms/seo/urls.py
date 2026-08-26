from django.urls import path

from . import views

urlpatterns = [
    path('post/<slug:slug>/', views.post_og_preview, name='seo-post-og-preview'),
]
