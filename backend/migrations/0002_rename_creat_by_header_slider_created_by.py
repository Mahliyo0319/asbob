# Generated by Django 5.1.1 on 2024-10-03 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='header_slider',
            old_name='creat_by',
            new_name='created_by',
        ),
    ]