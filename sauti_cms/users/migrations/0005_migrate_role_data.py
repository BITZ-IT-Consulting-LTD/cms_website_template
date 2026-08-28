from django.db import migrations


def migrate_data(apps, schema_editor):
    User = apps.get_model('users', 'User')
    Role = apps.get_model('users', 'Role')

    roles_by_slug = {r.slug: r for r in Role.objects.all()}
    # Old role CharField values were the TextChoices keys (ADMIN/EDITOR/
    # AUTHOR/VIEWER); the seeded Role slugs are their lowercase form.
    for user in User.objects.all():
        old_value = (user.role or '').strip().lower()
        role = roles_by_slug.get(old_value) or roles_by_slug.get('viewer')
        user.role_fk_id = role.id if role else None
        user.save(update_fields=['role_fk'])


def reverse(apps, schema_editor):
    User = apps.get_model('users', 'User')
    for user in User.objects.all():
        role = user.role_fk
        user.role = role.slug.upper() if role else 'VIEWER'
        user.save(update_fields=['role'])


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_role_fk'),
    ]

    operations = [
        migrations.RunPython(migrate_data, reverse),
    ]
