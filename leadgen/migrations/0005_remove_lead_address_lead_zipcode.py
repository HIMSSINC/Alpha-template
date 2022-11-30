# Generated by Django 4.0.5 on 2022-11-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadgen', '0004_alter_lead_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='address',
        ),
        migrations.AddField(
            model_name='lead',
            name='zipcode',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]