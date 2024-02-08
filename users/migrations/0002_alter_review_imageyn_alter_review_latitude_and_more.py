# Generated by Django 4.2.6 on 2024-02-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='imageYN',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=30, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=30, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewType',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]