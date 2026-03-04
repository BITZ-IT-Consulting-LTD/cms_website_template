"""
Django management command to populate initial site content.
This command is idempotent - it safely clears old content and repopulates with fresh data.
"""

from django.core.management.base import BaseCommand
from content.models import SiteContent
import os
import django

class Command(BaseCommand):
    help = 'Populate initial site content'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear all existing content before populating',
        )

    def handle(self, *args, **options):
        clear_content = options.get('clear', False)

        if clear_content:
            self.stdout.write(
                self.style.WARNING(f'Clearing {SiteContent.objects.count()} existing content entries...')
            )
            SiteContent.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('✓ Content cleared'))

        # Run the populate script
        populate_script = os.path.join(os.path.dirname(__file__), '../../populate_initial_content.py')

        if os.path.exists(populate_script):
            self.stdout.write(self.style.SUCCESS(f'Running populate script: {populate_script}'))
            # Import and run the populate functions
            import sys
            sys.path.insert(0, os.path.dirname(__file__) + '/../../')

            from populate_initial_content import populate_initial_content, populate_global_settings

            try:
                populate_initial_content()
                populate_global_settings()
                self.stdout.write(self.style.SUCCESS('✓ Content populated successfully'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error populating content: {str(e)}'))
        else:
            self.stdout.write(
                self.style.WARNING(f'Populate script not found at {populate_script}')
            )
