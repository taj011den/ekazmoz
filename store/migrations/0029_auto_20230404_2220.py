# Generated by Django 3.2.18 on 2023-04-05 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_alter_vendor_user'),
        ('store', '0028_auto_20230404_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartorder',
            name='vendor',
        ),
        migrations.AddField(
            model_name='cartorder',
            name='vendor',
            field=models.ManyToManyField(to='vendor.Vendor'),
        ),
    ]
