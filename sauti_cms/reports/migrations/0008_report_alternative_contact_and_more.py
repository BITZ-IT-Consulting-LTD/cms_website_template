from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_historicalreport_escalated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalreport',
            name='alternative_contact',
            field=models.CharField(blank=True, help_text='Reporter-supplied alternative phone/contact for follow-up', max_length=100),
        ),
        migrations.AddField(
            model_name='historicalreport',
            name='incident_type',
            field=models.CharField(blank=True, help_text='Specific incident type chosen during intake', max_length=200),
        ),
        migrations.AddField(
            model_name='historicalreport',
            name='victim_location',
            field=models.CharField(blank=True, help_text='Where the victim/affected person is located (distinct from the incident location)', max_length=200),
        ),
        migrations.AddField(
            model_name='report',
            name='alternative_contact',
            field=models.CharField(blank=True, help_text='Reporter-supplied alternative phone/contact for follow-up', max_length=100),
        ),
        migrations.AddField(
            model_name='report',
            name='incident_type',
            field=models.CharField(blank=True, help_text='Specific incident type chosen during intake', max_length=200),
        ),
        migrations.AddField(
            model_name='report',
            name='victim_location',
            field=models.CharField(blank=True, help_text='Where the victim/affected person is located (distinct from the incident location)', max_length=200),
        ),
    ]
