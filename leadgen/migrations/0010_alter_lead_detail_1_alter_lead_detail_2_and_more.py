# Generated by Django 4.0.5 on 2023-01-27 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadgen', '0009_alter_lead_detail_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='detail_1',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='lead',
            name='detail_2',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='lead',
            name='detail_3',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='lead',
            name='detail_4',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='lead',
            name='detail_5',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='lead',
            name='detail_6',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='lead',
            name='detail_7',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
