# Generated by Django 5.1.3 on 2025-01-12 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_desription',
            new_name='product_description',
        ),
    ]
