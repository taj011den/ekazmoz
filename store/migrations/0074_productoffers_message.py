# Generated by Django 3.2.18 on 2023-05-01 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0073_alter_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoffers',
            name='message',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
