# Generated by Django 4.0.5 on 2022-11-25 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadgen', '0005_remove_lead_address_lead_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='customer_email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='lead',
            name='customer_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
