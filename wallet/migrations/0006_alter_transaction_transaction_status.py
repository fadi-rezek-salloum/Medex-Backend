# Generated by Django 5.0 on 2024-04-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_alter_transaction_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_status',
            field=models.CharField(blank=True, choices=[('A', 'Approved'), ('D', 'Denied'), ('P', 'Pending')], max_length=20, null=True),
        ),
    ]
