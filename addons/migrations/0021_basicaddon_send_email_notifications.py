# Generated by Django 3.2.18 on 2023-04-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0020_auto_20230421_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicaddon',
            name='send_email_notifications',
            field=models.BooleanField(default=False),
        ),
    ]