# Generated by Django 3.2.18 on 2023-04-18 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0013_regtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='registration_form',
            field=models.CharField(choices=[('classic', 'Classic'), ('dynamic', 'Dynamic')], default='classic', max_length=50),
        ),
    ]
