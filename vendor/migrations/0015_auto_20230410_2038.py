# Generated by Django 3.2.18 on 2023-04-11 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0014_vendor_paypal_email_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendor',
            options={'verbose_name_plural': 'Vendors'},
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='payout',
            new_name='total_payout_tracker',
        ),
        migrations.AddField(
            model_name='vendor',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP')], default='USD', max_length=10),
        ),
    ]
