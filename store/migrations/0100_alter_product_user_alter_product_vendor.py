# Generated by Django 4.2.2 on 2023-10-16 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0046_alter_vendor_address_alter_vendor_city_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0099_auto_20230605_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor', to='vendor.vendor'),
        ),
    ]
