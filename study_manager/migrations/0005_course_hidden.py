# Generated by Django 5.0.2 on 2025-03-23 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_manager', '0004_alter_course_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
