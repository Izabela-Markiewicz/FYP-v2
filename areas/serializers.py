from rest_framework import serializers
from .models import *

#REF: Serialisers used in Youtube Video Connecting PostgreSQL to Django (MrNick, 2023) "Building a CRUD API with Django Rest Framework and PostgreSQL - Tutorial for Beginners."
# Gradient serializer
class GradientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gradient
        fields = ('gradientID', 'gradientName', 'HEX')


# Country serializer
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('countryID', 'countryName', 'countryRating')


# City serializer
class CitySerializer(serializers.ModelSerializer):
    #REF: Foreign Keys as part of serializer of other object (Dayne, 2022)
    countryID = CountrySerializer()

    class Meta:
        model = City
        fields = ('cityID', 'cityName', 'countryID', 'longitude', 'latitude')


# Police Divsion serializer
class PoliceDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceDivision
        fields = ('policeID', 'policeName', 'longitude', 'latitude', 'crimeRating')


# Area serializer
class AreaSerializer(serializers.ModelSerializer):
    cityID = CitySerializer()
    policeID = PoliceDivisionSerializer()
    gradientID = GradientSerializer() 

    class Meta:
        model = Area
        fields = ('areaID', 'areaName', 'cityID', 'policeID', 'longitude', 'latitude', 'avgFeelRating', 'gradientID')


# Crime Record serializer
class CrimeRecordSerializer(serializers.ModelSerializer):
    cityID = CitySerializer()
    policeID = PoliceDivisionSerializer()

    class Meta:
        model = CrimeRecord
        fields = ('recordID', 'year', 'cityID', 'policeID', 'crimeType', 'value')


"""
REFERENCES:

MrNick. “Building a CRUD API with Django Rest Framework and PostgreSQL - Tutorial for Beginners.” Www.youtube.com, Feb. 2023, www.youtube.com/watch?v=1YmfnQ8i9o8. Accessed 23 Oct. 2023.
Dayne, A. (2022). Create foreign key objects inside serializer. [online] Stack Overflow. Available at: https://stackoverflow.com/questions/73162763/create-foreign-key-objects-inside-serializer [Accessed 4 Nov. 2023].


"""