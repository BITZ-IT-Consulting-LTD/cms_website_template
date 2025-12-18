"""
Management command to publish scheduled posts and videos.
Run this command via cron job every minute or hour to auto-publish scheduled content.

Usage:
    python manage.py publish_scheduled
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from posts.models import Post
from videos.models import Video


class Command(BaseCommand):
    help = 'Publish scheduled posts and videos that are due'

    def handle(self, *args, **options):
        now = timezone.now()
        published_count = 0

        # Find and publish scheduled posts
        scheduled_posts = Post.objects.filter(
            status=Post.Status.DRAFT,
            scheduled_publish_at__isnull=False,
            scheduled_publish_at__lte=now
        )

        for post in scheduled_posts:
            post.status = Post.Status.PUBLISHED
            post.published_at = now
            post.scheduled_publish_at = None  # Clear the schedule after publishing
            post.save()
            published_count += 1
            self.stdout.write(
                self.style.SUCCESS(f'✅ Published post: "{post.title}" (ID: {post.id})')
            )

        # Find and publish scheduled videos
        scheduled_videos = Video.objects.filter(
            status=Video.Status.DRAFT,
            scheduled_publish_at__isnull=False,
            scheduled_publish_at__lte=now
        )

        for video in scheduled_videos:
            video.status = Video.Status.PUBLISHED
            video.published_at = now
            video.scheduled_publish_at = None  # Clear the schedule after publishing
            video.save()
            published_count += 1
            self.stdout.write(
                self.style.SUCCESS(f'✅ Published video: "{video.title}" (ID: {video.id})')
            )

        if published_count == 0:
            self.stdout.write(
                self.style.WARNING('⏱️  No scheduled content due for publishing at this time.')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f'\n🎉 Total published: {published_count} item(s)')
            )
