# Generated by Django 5.0.2 on 2025-03-19 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='code',
        ),
        migrations.AlterField(
            model_name='exam',
            name='description',
            field=models.CharField(blank=True, max_length=355, null=True),
        ),
    ]
