# Generated by Django 3.2.18 on 2023-04-21 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0060_auto_20230418_2200'),
        ('vendor', '0026_notification_seen'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VendoReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('block_vendor', models.BooleanField(default=False)),
                ('resolved', models.BooleanField(default=False)),
                ('vid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=20, prefix='', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor_reporting_user', to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor_report', to='vendor.vendor')),
            ],
            options={
                'verbose_name_plural': 'Vendor Report',
            },
        ),
        migrations.CreateModel(
            name='ProductReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('disable_product', models.BooleanField(default=False)),
                ('resolved', models.BooleanField(default=False)),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=20, prefix='', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_report', to='store.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_reporting_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Product Report',
            },
        ),
        migrations.CreateModel(
            name='OrderItemReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('block_vendor', models.BooleanField(default=False)),
                ('disable_product', models.BooleanField(default=False)),
                ('resolved', models.BooleanField(default=False)),
                ('oid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=20, prefix='', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_item_report', to='store.cartorderitem')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_item_reporting_user', to='vendor.vendor')),
            ],
            options={
                'verbose_name_plural': 'Order Item Report',
            },
        ),
        migrations.CreateModel(
            name='BiddingUserReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('block_user', models.BooleanField(default=False)),
                ('resolved', models.BooleanField(default=False)),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=20, prefix='', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product_bidding', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bidding_report', to='store.productbidders')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bidding_reporting_user', to='vendor.vendor')),
            ],
            options={
                'verbose_name_plural': 'Bidding User Report',
            },
        ),
    ]
