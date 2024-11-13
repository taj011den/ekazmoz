# Generated by Django 3.2.18 on 2023-04-02 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20230402_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='town_city',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
