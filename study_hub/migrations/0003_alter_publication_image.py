# Generated by Django 5.0.2 on 2024-03-01 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_hub', '0002_alter_publication_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='image',
            field=models.ImageField(blank=True, upload_to='study/publication/', verbose_name='Imagen para tu publicacion'),
        ),
    ]