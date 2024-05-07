# Generated by Django 5.0.2 on 2024-03-16 14:42

import inventory.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_category_supercategory_alter_product_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsubimage',
            name='sub_image1',
        ),
        migrations.RemoveField(
            model_name='productsubimage',
            name='sub_image2',
        ),
        migrations.RemoveField(
            model_name='productsubimage',
            name='sub_image3',
        ),
        migrations.RemoveField(
            model_name='productsubimage',
            name='sub_image4',
        ),
        migrations.RemoveField(
            model_name='productsubimage',
            name='sub_image5',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='inventory.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategories',
            field=models.ManyToManyField(blank=True, to='inventory.subcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='supercategories',
            field=models.ManyToManyField(blank=True, to='inventory.supercategory'),
        ),
        migrations.AddField(
            model_name='productsubimage',
            name='image',
            field=models.ImageField(blank=True, upload_to=inventory.models.get_upload_path),
        ),
    ]