# Generated by Django 5.0 on 2024-01-18 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_privatecategory_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatecategory',
            name='products',
            field=models.ManyToManyField(blank=True, to='product.product'),
        ),
    ]
