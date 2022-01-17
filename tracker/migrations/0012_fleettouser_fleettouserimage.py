# Generated by Django 4.0 on 2021-12-28 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_rename_branding_id_brandsupplier_brand_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FleetToUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_no', models.PositiveIntegerField()),
                ('emirates', models.JSONField()),
                ('plate_code', models.JSONField()),
                ('km', models.CharField(max_length=10)),
                ('fueltank', models.CharField(max_length=50)),
                ('EntryDate', models.DateField()),
                ('Time', models.TimeField()),
                ('parts', models.JSONField()),
                ('license_code', models.JSONField()),
                ('comments', models.TextField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='tracker.employee')),
                ('subtask_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='tracker.subtask')),
            ],
        ),
        migrations.CreateModel(
            name='FleetToUserImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100)),
                ('takeover_image', models.TextField()),
                ('takeover_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='takeover', to='tracker.fleettouser')),
            ],
        ),
    ]