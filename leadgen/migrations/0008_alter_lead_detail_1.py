# Generated by Django 4.0.5 on 2023-01-26 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadgen', '0007_lead_detail_4_lead_detail_5_lead_detail_6_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='detail_1',
            field=models.CharField(blank=True, max_length=100, verbose_name='This is a test'),
        ),
    ]
