# Generated by Django 5.0.1 on 2024-02-29 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_popularitems_validity_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='not_available',
            field=models.BooleanField(default=False),
        ),
    ]
