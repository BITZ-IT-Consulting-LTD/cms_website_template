#!/usr/bin/env python
"""
One-off backfill: generate thumbnail/medium image derivatives for existing
rows that predate the derivative fields (Post, PostImage, Partner,
TeamMember, Video). New/edited rows already get derivatives automatically
via each model's save() (see imaging/derivatives.py) -- this script only
needs to be run once after the migrations in this change are applied, to
catch rows that were already in the database.

Usage (matches the existing populate_*.py convention in this directory):

    python backfill_image_derivatives.py

Safe to re-run: sync_image_derivatives() skips any row that already has its
derivative(s), so running this twice is a no-op the second time. History-
tracked models (Post, Partner) are saved with skip_history_when_saving=True
so this doesn't create a wall of no-op HistoricalPost/HistoricalPartner rows.
"""
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings")
django.setup()

from content.models import TeamMember  # noqa: E402
from partners.models import Partner  # noqa: E402
from posts.models import Post, PostImage  # noqa: E402
from videos.models import Video  # noqa: E402


def _save_skipping_history(obj):
    """Save a row, skipping simple_history's HistoricalRecords snapshot when supported."""
    obj.skip_history_when_saving = True
    try:
        obj.save()
    finally:
        # Don't leak the flag if this instance object is reused by the caller.
        obj.skip_history_when_saving = False


def backfill_posts():
    updated = 0
    for post in Post.objects.filter(featured_image__isnull=False).exclude(featured_image=''):
        if post.featured_image_thumbnail and post.featured_image_medium:
            continue
        _save_skipping_history(post)
        updated += 1
    print(f"Posts: checked, {updated} row(s) updated")


def backfill_post_images():
    updated = 0
    for image in PostImage.objects.exclude(image=''):
        if image.image_thumbnail and image.image_medium:
            continue
        image.save()
        updated += 1
    print(f"PostImages: checked, {updated} row(s) updated")


def backfill_partners():
    updated = 0
    for partner in Partner.objects.filter(logo__isnull=False).exclude(logo=''):
        if partner.logo_thumbnail:
            continue
        _save_skipping_history(partner)
        updated += 1
    print(f"Partners: checked, {updated} row(s) updated")


def backfill_team_members():
    updated = 0
    for member in TeamMember.objects.filter(image__isnull=False).exclude(image=''):
        if member.image_thumbnail:
            continue
        member.save()
        updated += 1
    print(f"TeamMembers: checked, {updated} row(s) updated")


def backfill_videos():
    updated = 0
    for video in Video.objects.filter(thumbnail__isnull=False).exclude(thumbnail=''):
        if video.thumbnail_small:
            continue
        video.save()
        updated += 1
    print(f"Videos: checked, {updated} row(s) updated")


if __name__ == "__main__":
    backfill_posts()
    backfill_post_images()
    backfill_partners()
    backfill_team_members()
    backfill_videos()
    print("Done.")
