# Generated by Django 3.2.18 on 2023-05-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0080_cartorder_original_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorderitem',
            name='applied_coupon',
            field=models.BooleanField(default=False),
        ),
    ]