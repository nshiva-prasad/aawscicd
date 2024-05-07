# Generated by Django 5.0.2 on 2024-03-12 11:15

import ckeditor.fields
import django.db.models.deletion
import inventory.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('product_main_image', models.ImageField(upload_to=inventory.models.get_upload_path)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content')),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('actual_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('best_seller', models.BooleanField(default=False)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('number_reviews', models.PositiveIntegerField(blank=True, null=True)),
                ('stock', models.CharField(default='100', max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '12 Product',
                'verbose_name_plural': '12 Products',
            },
        ),
        migrations.CreateModel(
            name='ProductSubImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_image1', models.ImageField(blank=True, upload_to=inventory.models.ProductSubImage.get_upload_path)),
                ('sub_image2', models.ImageField(blank=True, upload_to=inventory.models.ProductSubImage.get_upload_path)),
                ('sub_image3', models.ImageField(blank=True, upload_to=inventory.models.ProductSubImage.get_upload_path)),
                ('sub_image4', models.ImageField(blank=True, upload_to=inventory.models.ProductSubImage.get_upload_path)),
                ('sub_image5', models.ImageField(blank=True, upload_to=inventory.models.ProductSubImage.get_upload_path)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_images', to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagname', models.CharField(blank=True, max_length=100)),
                ('tag', models.CharField(blank=True, choices=[('text', 'Text'), ('date_picker', 'Date Picker'), ('image', 'Image'), ('multiple_images', 'Multiple Images')], max_length=100)),
                ('has_color', models.BooleanField(blank=True, default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagsmain', to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTagEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_tagname', models.CharField(max_length=100)),
                ('custom_choice', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='inventory.product')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.producttag')),
            ],
        ),
    ]
