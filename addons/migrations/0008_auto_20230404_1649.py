# Generated by Django 3.2.18 on 2023-04-04 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0007_auto_20230402_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicaddon',
            name='service_fee',
        ),
        migrations.AddField(
            model_name='basicaddon',
            name='service_fee_percentage',
            field=models.IntegerField(default=5, help_text='NOTE: Numbers added here are in percentage (%)'),
        ),
    ]