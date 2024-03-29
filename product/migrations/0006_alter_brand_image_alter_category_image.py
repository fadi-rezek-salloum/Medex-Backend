# Generated by Django 5.0 on 2024-01-08 06:17

import common.utils.file_upload_paths
import common.validators.image_extension_validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(default='uploads/images/placeholder/placeholder.png', upload_to=common.utils.file_upload_paths.brands_images_path, validators=[common.validators.image_extension_validator.image_extension_validator], verbose_name='Brand Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='uploads/images/placeholder/placeholder.png', upload_to=common.utils.file_upload_paths.categories_images_path, validators=[common.validators.image_extension_validator.image_extension_validator], verbose_name='Category Image'),
        ),
    ]
