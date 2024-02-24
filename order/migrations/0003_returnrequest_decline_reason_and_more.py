# Generated by Django 5.0 on 2024-01-02 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_returnrequest_description_returnrequest_reason_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='returnrequest',
            name='decline_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='returnrequest',
            name='status',
            field=models.CharField(choices=[('AP', 'Applied'), ('DEC', 'Declined by Supplier'), ('APR', 'Approved by Supplier'), ('OTW', 'On the way'), ('CMP', 'Return Completed')], default='AP', max_length=15, verbose_name='Return Status'),
        ),
    ]
