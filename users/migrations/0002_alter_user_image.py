# Generated by Django 4.2 on 2024-01-31 12:51

from django.db import migrations, models
import helpers.media_upload


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=helpers.media_upload.upload_user_images),
        ),
    ]
