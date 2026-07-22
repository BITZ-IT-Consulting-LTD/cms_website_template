from django.db import migrations
from django.utils.text import slugify


# Baseline resource categories. Without at least one category the admin
# "Add Resource" form's required category dropdown is empty, which blocked
# creating any resource at all (production issue T20).
BASELINE_CATEGORIES = [
    ('Guides & Toolkits', 'Practical guides, toolkits and how-to materials.'),
    ('Reports & Research', 'Research reports, studies and data briefs.'),
    ('Policy & Legal', 'Policies, laws, frameworks and legal references.'),
    ('Awareness Materials', 'Posters, flyers and public-awareness content.'),
    ('Training Materials', 'Curricula, training decks and facilitation resources.'),
]


def seed_categories(apps, schema_editor):
    ResourceCategory = apps.get_model('resources', 'ResourceCategory')
    for name, description in BASELINE_CATEGORIES:
        ResourceCategory.objects.get_or_create(
            name=name,
            defaults={'slug': slugify(name), 'description': description},
        )


def unseed_categories(apps, schema_editor):
    # Only remove the baseline rows we added, and only if they carry no resources.
    ResourceCategory = apps.get_model('resources', 'ResourceCategory')
    for name, _ in BASELINE_CATEGORIES:
        ResourceCategory.objects.filter(name=name, resources__isnull=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_historicalresource'),
    ]

    operations = [
        migrations.RunPython(seed_categories, unseed_categories),
    ]
