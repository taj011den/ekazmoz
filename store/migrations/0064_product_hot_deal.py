# Generated by Django 3.2.18 on 2023-04-25 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0063_alter_product_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hot_deal',
            field=models.BooleanField(default=False),
        ),
    ]