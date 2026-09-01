from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_seed_roles_and_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role_fk',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='users', to='users.role',
                help_text='User role for access control',
            ),
        ),
    ]
