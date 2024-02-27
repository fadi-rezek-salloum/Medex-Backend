# Generated by Django 4.2.7 on 2023-11-26 17:34

import common.utils.file_upload_paths
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255, verbose_name='Product')),
                ('quantity', models.PositiveBigIntegerField(verbose_name='Quantity')),
                ('unit', models.CharField(choices=[('bag', 'Bag / Bags'), ('barrel', 'Barrel / Barrels'), ('bushel', 'Bushel / Bushels'), ('cubic', 'Cubic Meter / Cubic Meters'), ('dozen', 'Dozen / Dozens'), ('gallon', 'Gallon / Gallons'), ('gram', 'Gram / Grams'), ('kilogram', 'Kilogram / Kilograms'), ('kilometer', 'Kilometer / Kilometers'), ('long', 'Long Ton / Long Tons'), ('meter', 'Meter / Meters'), ('metric', 'Metric Ton / Metric Tons'), ('ounce', 'Ounce / Ounces'), ('pair', 'Pair / Pairs'), ('pack', 'Pack / Packs'), ('piece', 'Piece / Pieces'), ('pound', 'Pound / Pounds'), ('set', 'Set / Sets'), ('short', 'Short Ton / Short Tons'), ('square', 'Square Meter / Square Meters'), ('ton', 'Ton / Tons')], max_length=50, verbose_name='Unit')),
                ('requirements', models.TextField(verbose_name='Requirements')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
            ],
        ),
        migrations.CreateModel(
            name='QuoteOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, null=True)),
                ('brand', models.CharField(max_length=255, verbose_name='Brand')),
                ('quantity', models.PositiveBigIntegerField(verbose_name='Available Amount')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price (Per Product)')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price (Total)')),
                ('tax', models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name='TAX')),
                ('delivery_date', models.DateField()),
                ('payment_type', models.CharField(max_length=255, verbose_name='Payment Type')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('D', 'Denied')], default='P', max_length=2)),
                ('invoice_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('delivery_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.address', verbose_name='Delivery Address')),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote.quoterequest', verbose_name='Target Quote')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='QuoteAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(upload_to=common.utils.file_upload_paths.quote_files_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp', 'gif', 'tiff', 'svg', 'pdf'])], verbose_name='Attachment')),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote.quoterequest', verbose_name='Related Quote')),
            ],
        ),
    ]