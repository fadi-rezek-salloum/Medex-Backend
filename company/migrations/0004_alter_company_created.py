# Generated by Django 5.0 on 2024-01-30 15:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_company_bio_alter_company_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Added On'),
        ),
    ]
