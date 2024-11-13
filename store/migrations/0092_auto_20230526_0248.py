# Generated by Django 3.2.18 on 2023-05-26 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0091_auto_20230524_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, choices=[('draft', 'Draft'), ('disabled', 'Disabled'), ('rejected', 'Rejected'), ('in_review', 'In Review'), ('published', 'Published')], default='published', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='productoffers',
            name='status',
            field=models.CharField(choices=[('accepted', 'Accepted'), ('rejected', 'Rejected'), ('pending', 'Pending')], default='pending', max_length=10),
        ),
    ]
