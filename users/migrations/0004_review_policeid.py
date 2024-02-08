# Generated by Django 4.2.6 on 2024-02-08 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0002_alter_policedivision_latitude_and_more'),
        ('users', '0003_alter_review_image_alter_review_imageyn'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='policeID',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='areas.policedivision'),
        ),
    ]