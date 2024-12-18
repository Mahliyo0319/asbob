# Generated by Django 5.1.1 on 2024-10-24 14:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0024_delete_product'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('producte_tags', models.TextField(max_length=300)),
                ('size', models.CharField(choices=[('s', 's'), ('l', 'l'), ('xs', 'xs'), ('xl', 'xl'), ('m', 'm')], max_length=15)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='products/products_img')),
                ('image_preview_small', models.ImageField(blank=True, null=True, upload_to='products/products_img/preview/small/')),
                ('image_preview_medium', models.ImageField(blank=True, null=True, upload_to='products/products_img/preview/medium/')),
                ('image_preview_large', models.ImageField(blank=True, null=True, upload_to='products/products_img/preview/large/')),
                ('selling_count', models.PositiveBigIntegerField()),
                ('review', models.PositiveBigIntegerField()),
                ('rating', models.PositiveIntegerField()),
                ('color', models.CharField(choices=[('Red', 'Red'), ('Green', 'Green'), ('Whit', 'Whit'), ('Black', 'Black')], max_length=15)),
                ('wishlist', models.BooleanField(default=False)),
                ('amount', models.PositiveBigIntegerField(default=0)),
                ('availability', models.CharField(choices=[('available', 'Availability'), ('unavailable', 'Unavailabile')], default='available', max_length=30)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('brand', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.brand')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('madel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.models')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'Main_Product',
                'ordering': ['selling_count', 'price', 'rating'],
                'unique_together': {('name', 'madel')},
            },
        ),
    ]
