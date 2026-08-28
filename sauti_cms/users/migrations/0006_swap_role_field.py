from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_migrate_role_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='role_fk',
            new_name='role',
        ),
    ]
