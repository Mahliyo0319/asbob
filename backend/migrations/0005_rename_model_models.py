# Generated by Django 5.1.1 on 2024-10-10 18:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_product_options_product_amount_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Model',
            new_name='Models',
        ),
    ]
