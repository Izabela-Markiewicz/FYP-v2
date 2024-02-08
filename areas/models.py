from django.db import models

# Iteration 1:
# CREATING MODELS for all map-related objects

class Gradient(models.Model):
    gradientID = models.AutoField(primary_key=True)
    gradientName = models.CharField(max_length=50)
    HEX = models.CharField(max_length= 15)

class Country(models.Model):
    countryID = models.AutoField(primary_key=True)
    countryName = models.CharField(max_length=255)
    countryRating = models.DecimalField(max_digits=5, decimal_places=2)

class PoliceDivision(models.Model):
    policeID = models.AutoField(primary_key=True)
    policeName = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=50, decimal_places=15)
    latitude = models.DecimalField(max_digits=50, decimal_places=15)
    crimeRating = models.DecimalField(max_digits=10, decimal_places=2)

class City(models.Model):
    cityID = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=255)
    countryID = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    longitude = models.DecimalField(max_digits=50, decimal_places=30)
    latitude = models.DecimalField(max_digits=50, decimal_places=30)


class Area(models.Model):
    areaID = models.AutoField(primary_key=True)
    areaName = models.CharField(max_length=255)
    cityID = models.ForeignKey(City, on_delete=models.CASCADE, related_name='areas')
    policeID = models.ForeignKey(PoliceDivision, on_delete=models.CASCADE, related_name='areas')
    longitude = models.DecimalField(max_digits=50, decimal_places=30)
    latitude = models.DecimalField(max_digits=50, decimal_places=30)
    avgFeelRating = models.DecimalField(max_digits=5, decimal_places=2)
    gradientID = models.ForeignKey(Gradient, on_delete=models.CASCADE, related_name='areas')

class CrimeRecord(models.Model):
    recordID = models.AutoField(primary_key=True)  
    year = models.IntegerField()
    cityID = models.ForeignKey(City, on_delete=models.CASCADE, related_name='crime_records')
    policeID = models.ForeignKey(PoliceDivision, on_delete=models.CASCADE, related_name='crime_records')
    crimeType = models.CharField(max_length=255)
    value = models.IntegerField()


"""
REFERENCES:


"""