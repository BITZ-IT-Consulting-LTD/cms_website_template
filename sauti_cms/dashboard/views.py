from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from posts.models import Post
from videos.models import Video
from resources.models import Resource
from faqs.models import FAQ
from partners.models import Partner
from reports.models import Report


class DashboardStatsView(APIView):
    """Dashboard statistics endpoint"""
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        # Get date ranges
        now = timezone.now()
        last_30_days = now - timedelta(days=30)
        last_7_days = now - timedelta(days=7)
        
        # Content counts
        total_posts = Post.objects.count()
        published_posts = Post.objects.filter(status='PUBLISHED').count()
        draft_posts = Post.objects.filter(status='DRAFT').count()
        
        total_videos = Video.objects.count()
        published_videos = Video.objects.filter(status='PUBLISHED').count()
        
        total_resources = Resource.objects.count()
        total_faqs = FAQ.objects.count()
        total_partners = Partner.objects.count()
        
        # Recent activity
        recent_posts = Post.objects.filter(created_at__gte=last_7_days).count()
        recent_videos = Video.objects.filter(created_at__gte=last_7_days).count()
        recent_resources = Resource.objects.filter(published_at__gte=last_7_days).count()
        
        # Reports (if user has access)
        total_reports = 0
        pending_reports = 0
        if request.user.is_staff:
            total_reports = Report.objects.count()
            pending_reports = Report.objects.filter(status='PENDING').count()
        
        # Popular content
        popular_posts = Post.objects.filter(status='PUBLISHED').order_by('-views_count')[:5]
        popular_videos = Video.objects.filter(status='PUBLISHED').order_by('-views_count')[:5]
        
        stats = {
            'content': {
                'posts': {
                    'total': total_posts,
                    'published': published_posts,
                    'draft': draft_posts,
                    'recent': recent_posts
                },
                'videos': {
                    'total': total_videos,
                    'published': published_videos,
                    'recent': recent_videos
                },
                'resources': {
                    'total': total_resources,
                    'recent': recent_resources
                },
                'faqs': {
                    'total': total_faqs
                },
                'partners': {
                    'total': total_partners
                }
            },
            'reports': {
                'total': total_reports,
                'pending': pending_reports
            },
            'activity': {
                'recent_posts': recent_posts,
                'recent_videos': recent_videos,
                'recent_resources': recent_resources
            }
        }
        
        return Response(stats)


class TopContentView(APIView):
    """Top performing content endpoint"""
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        # Get top posts by views
        top_posts = Post.objects.filter(
            status='PUBLISHED'
        ).order_by('-views_count')[:10]
        
        # Get top videos by views
        top_videos = Video.objects.filter(
            status='PUBLISHED'
        ).order_by('-views_count')[:10]
        
        # Get most downloaded resources
        top_resources = Resource.objects.order_by('-download_count')[:10]
        
        # Get most viewed FAQs
        top_faqs = FAQ.objects.filter(
            is_active=True
        ).order_by('-views_count')[:10]
        
        content = {
            'posts': [
                {
                    'id': post.id,
                    'title': post.title,
                    'slug': post.slug,
                    'views_count': post.views_count,
                    'published_at': post.published_at,
                    'author': post.author.get_full_name() if post.author else 'Unknown',
                    'category': post.category.name if post.category else None,
                    'type': 'post'
                }
                for post in top_posts
            ],
            'videos': [
                {
                    'id': video.id,
                    'title': video.title,
                    'slug': video.slug,
                    'views_count': video.views_count,
                    'published_at': video.published_at,
                    'author': video.author.get_full_name() if video.author else 'Unknown',
                    'category': video.category.name if video.category else None,
                    'video_type': video.video_type,
                    'youtube_url': video.youtube_url,
                    'type': 'video'
                }
                for video in top_videos
            ],
            'resources': [
                {
                    'id': resource.id,
                    'title': resource.title,
                    'slug': resource.slug,
                    'download_count': resource.download_count,
                    'published_at': resource.published_at,
                    'category': resource.category.name if resource.category else None,
                    'file_type': resource.file_type,
                    'type': 'resource'
                }
                for resource in top_resources
            ],
            'faqs': [
                {
                    'id': faq.id,
                    'question': faq.question,
                    'views_count': faq.views_count,
                    'category': faq.category.name if faq.category else None,
                    'language': faq.language,
                    'type': 'faq'
                }
                for faq in top_faqs
            ]
        }
        
        return Response(content)
