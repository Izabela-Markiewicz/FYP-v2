# Generated by Django 4.2.6 on 2024-02-23 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_review_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='review',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='review',
            name='reviewType',
        ),
    ]
