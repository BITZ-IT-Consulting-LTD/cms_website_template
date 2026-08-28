from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.SlugField(max_length=50, unique=True)),
                ('label', models.CharField(max_length=100)),
                ('category', models.CharField(help_text='Groups permissions in the admin UI, e.g. "Content"', max_length=50)),
            ],
            options={
                'ordering': ['category', 'label'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=50, unique=True)),
                ('is_default', models.BooleanField(default=False, help_text='Seeded role (admin/editor/author/viewer) -- cannot be deleted, but its permissions can still be edited.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('permissions', models.ManyToManyField(blank=True, related_name='roles', to='users.permission')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
