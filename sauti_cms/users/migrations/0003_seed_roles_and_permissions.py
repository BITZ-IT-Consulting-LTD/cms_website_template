from django.db import migrations

# codename, label, category
PERMISSIONS = [
    ('manage_users', 'Manage Users & Roles', 'Administration'),
    ('manage_settings', 'Manage Site Settings', 'Administration'),
    ('create_posts', 'Create Posts (own drafts)', 'Content'),
    ('manage_posts', 'Manage All Posts', 'Content'),
    ('manage_resources', 'Manage Resources', 'Content'),
    ('manage_partners', 'Manage Partners', 'Content'),
    ('manage_faqs', 'Manage FAQs', 'Content'),
    ('manage_videos', 'Manage Videos', 'Content'),
    ('manage_site_content', 'Manage Site Content & Pages', 'Content'),
    ('manage_reports', 'View & Manage Case Reports', 'Reports'),
    ('manage_feedback', 'Manage General Feedback', 'Reports'),
]

# slug, name, [permission codenames]. Reproduces the old is_admin/is_editor/
# is_author bundles exactly, except manage_site_content (see migration
# docstring below) which the old system never gated at all.
ROLES = [
    ('admin', 'Administrator', [codename for codename, _, _ in PERMISSIONS]),
    ('editor', 'Editor', [
        'create_posts', 'manage_posts', 'manage_resources', 'manage_partners',
        'manage_faqs', 'manage_videos', 'manage_site_content',
        'manage_reports', 'manage_feedback',
    ]),
    ('author', 'Author', ['create_posts']),
    ('viewer', 'Viewer', []),
]


def seed(apps, schema_editor):
    Permission = apps.get_model('users', 'Permission')
    Role = apps.get_model('users', 'Role')

    perm_by_codename = {}
    for codename, label, category in PERMISSIONS:
        perm, _ = Permission.objects.get_or_create(
            codename=codename, defaults={'label': label, 'category': category}
        )
        perm_by_codename[codename] = perm

    for slug, name, codenames in ROLES:
        role, _ = Role.objects.get_or_create(
            slug=slug, defaults={'name': name, 'is_default': True}
        )
        role.permissions.set([perm_by_codename[c] for c in codenames])


def unseed(apps, schema_editor):
    Role = apps.get_model('users', 'Role')
    Permission = apps.get_model('users', 'Permission')
    Role.objects.filter(slug__in=[slug for slug, _, _ in ROLES]).delete()
    Permission.objects.filter(codename__in=[c for c, _, _ in PERMISSIONS]).delete()


class Migration(migrations.Migration):
    """
    Seeds the fixed permission catalog and the 4 default roles.

    manage_site_content is a deliberate behavior change, not a preservation
    of prior behavior: the content app (SiteContent/CoreValue/Contact/
    ProtectionApproach/TeamMember/WhoWeAreImage/OperationsImage) previously
    had no role gate at all -- any authenticated account, including a bare
    Viewer, could write to it. Seeding it into the Editor bundle here closes
    that gap. Every other seeded permission exactly reproduces what
    is_admin/is_editor/is_author already granted, so nothing else changes
    the moment this migration runs.
    """

    dependencies = [
        ('users', '0002_permission_role'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
