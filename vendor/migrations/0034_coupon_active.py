# Generated by Django 3.2.18 on 2023-05-05 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0033_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
