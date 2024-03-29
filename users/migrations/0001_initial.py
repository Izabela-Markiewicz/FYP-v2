# Generated by Django 4.2.6 on 2024-02-08 12:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('userType', models.CharField(max_length=10)),
                ('totalReviews', models.IntegerField()),
                ('password', models.CharField(default='password', max_length=225)),
                ('email', models.CharField(default='email', max_length=225)),
                ('fName', models.CharField(default='fName', max_length=225)),
                ('lName', models.CharField(default='lName', max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviewID', models.AutoField(primary_key=True, serialize=False)),
                ('imageYN', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, upload_to='files/reviewImages')),
                ('longitude', models.DecimalField(decimal_places=30, max_digits=50, null=True)),
                ('latitude', models.DecimalField(decimal_places=30, max_digits=50, null=True)),
                ('reviewText', models.CharField(max_length=300)),
                ('reviewType', models.CharField(max_length=255, null=True)),
                ('feelRating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('publishDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('userID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='users.user')),
            ],
        ),
    ]
