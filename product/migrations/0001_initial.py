# Generated by Django 4.2.7 on 2023-11-26 17:34

import common.utils.file_upload_paths
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Brand Name')),
                ('image', models.ImageField(upload_to=common.utils.file_upload_paths.brands_images_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp', 'gif', 'tiff', 'svg'])], verbose_name='Brand Image')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Category Name')),
                ('image', models.ImageField(upload_to=common.utils.file_upload_paths.categories_images_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp', 'gif', 'tiff', 'svg'])], verbose_name='Category Image')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='product.category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('sku', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='Product Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price')),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='Sale Price')),
                ('price_range_min', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='Price Range - Min')),
                ('price_range_max', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='Price Range - Max')),
                ('stock_quantity', models.IntegerField(default=0, verbose_name='Stock Quantity')),
                ('is_available', models.BooleanField(default=True, verbose_name='Is Available ?')),
                ('thumbnail', models.ImageField(upload_to=common.utils.file_upload_paths.product_images_path, verbose_name='Thumbnail')),
                ('image1', models.ImageField(blank=True, null=True, upload_to=common.utils.file_upload_paths.product_images_path, verbose_name='Image 1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to=common.utils.file_upload_paths.product_images_path, verbose_name='Image 2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to=common.utils.file_upload_paths.product_images_path, verbose_name='Image 3')),
                ('image4', models.ImageField(blank=True, null=True, upload_to=common.utils.file_upload_paths.product_images_path, verbose_name='Image 4')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Added On')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Edited On')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.brand', verbose_name='Brand')),
                ('category', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.category', verbose_name='Category')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Supplier')),
            ],
        ),
    ]
