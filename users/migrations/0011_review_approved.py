# Generated by Django 4.2.6 on 2024-02-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_review_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]