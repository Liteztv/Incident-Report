# Generated by Django 4.0.2 on 2022-08-02 00:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Report', '0002_alter_chemicalreport_debrief_commander_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecureReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date_and_time_of_incident_start', models.DateTimeField()),
                ('date_and_time_of_incident_end', models.DateTimeField()),
                ('cause_of_incident', models.TextField()),
                ('actions_taken', models.TextField()),
                ('equipment_used', models.TextField()),
                ('debrief_attendance', models.TextField()),
                ('positive_notes', models.TextField()),
                ('areas_of_improvement', models.TextField()),
                ('debrief_date_time', models.DateTimeField()),
                ('debrief_commander', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SecureDebriefCommander', to=settings.AUTH_USER_MODEL)),
                ('incident_commander', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SecureCommander', to=settings.AUTH_USER_MODEL)),
                ('incident_type', models.ForeignKey(help_text='IF OTHER PROVIDE DESCRIPTION', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Report.incidenttype')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SecureCreator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]