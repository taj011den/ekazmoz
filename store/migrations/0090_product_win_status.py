# Generated by Django 3.2.18 on 2023-05-24 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0089_auto_20230523_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='win_status',
            field=models.CharField(choices=[('won', 'Won'), ('lost', 'Lost'), ('pending', 'pending')], default='pending', max_length=10),
        ),
    ]