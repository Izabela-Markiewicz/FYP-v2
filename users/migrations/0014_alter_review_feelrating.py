# Generated by Django 4.2.6 on 2024-03-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_review_reviewtext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='feelRating',
            field=models.DecimalField(choices=[(0.5, 0.5), (1.0, 1.0), (1.5, 1.5), (2.0, 2.0), (2.5, 2.5), (3.0, 3.0), (3.5, 3.5), (4.0, 4.0), (4.5, 4.5), (5.0, 5.0)], decimal_places=1, max_digits=2, verbose_name='User Safety Rating (1-5)'),
        ),
    ]
