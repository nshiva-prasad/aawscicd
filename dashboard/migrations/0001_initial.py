# Generated by Django 5.0.2 on 2024-03-16 14:20

import dashboard.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CircleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circle_image', models.ImageField(blank=True, help_text='Please upload an image with dimensions 1080x1080.', null=True, upload_to=dashboard.models.get_upload_path)),
                ('alt_text', models.CharField(help_text='Please provide the alternate text to display', max_length=100)),
                ('circle_category_name', models.CharField(help_text='This is the text that appears below the Circle', max_length=50)),
            ],
            options={
                'verbose_name': '4 Circle Category',
                'verbose_name_plural': '4 Circle Categories',
            },
        ),
        migrations.CreateModel(
            name='ImageContainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=dashboard.models.get_upload_path)),
                ('alternate_text', models.CharField(max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('side', models.CharField(choices=[('left', 'Left'), ('right', 'Right')], max_length=5)),
            ],
            options={
                'verbose_name': 'Image Container',
                'verbose_name_plural': 'Image Containers',
            },
        ),
        migrations.CreateModel(
            name='MainBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=dashboard.models.get_upload_path)),
                ('alternate_text', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '5 Main Banner',
                'verbose_name_plural': '5 Main Banners',
            },
        ),
        migrations.CreateModel(
            name='MobileBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=dashboard.models.get_upload_path)),
                ('alternate_text', models.CharField(max_length=255, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'MobileBanner',
                'verbose_name_plural': 'MobileBanner',
            },
        ),
        migrations.CreateModel(
            name='SubBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=dashboard.models.get_upload_path)),
                ('alternate_text', models.CharField(max_length=255, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'SubBanner',
                'verbose_name_plural': 'SubBanner',
            },
        ),
        migrations.CreateModel(
            name='SubImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=dashboard.models.get_upload_path)),
                ('alternate_text', models.CharField(max_length=255, null=True)),
                ('title', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.imagecontainer')),
            ],
            options={
                'verbose_name': 'Sub Image',
                'verbose_name_plural': 'Sub Images',
            },
        ),
    ]
