# Generated by Django 4.2.6 on 2024-02-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_review_imageyn_alter_review_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='files/reviewImages'),
        ),
        migrations.AlterField(
            model_name='review',
            name='imageYN',
            field=models.BooleanField(default=False),
        ),
    ]
