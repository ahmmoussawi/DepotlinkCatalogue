# Generated by Django 5.0.1 on 2024-01-22 01:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_brand_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brand',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
