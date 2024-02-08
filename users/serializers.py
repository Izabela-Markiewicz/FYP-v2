from rest_framework import serializers
from .models import *
from areas.models import *
from areas.serializers import *

# Environment
# User serializer
#REF: Serialisers used in Youtube Video Connecting PostgreSQL to Django (MrNick, 2023) "Building a CRUD API with Django Rest Framework and PostgreSQL - Tutorial for Beginners."
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userID', 'username', 'userType', 'totalReviews', 'password', 'email', 'fName', 'lName')

# Iteration 1
# Review serializer
class ReviewSerializer(serializers.ModelSerializer):
    #REF: Foreign Keys as part of serializer of other object (Dayne, 2022)
    userID = UserSerializer()
    areaID = AreaSerializer()

    class Meta:
        model = Review
        fields = ('reviewID', 'userID', 'imageYN', 'image', 'longitude', 'latitude', 'reviewText', 'reviewType', 'feelRating', 'publishDate')

"""
REFERENCES:

MrNick. “Building a CRUD API with Django Rest Framework and PostgreSQL - Tutorial for Beginners.” Www.youtube.com, Feb. 2023, www.youtube.com/watch?v=1YmfnQ8i9o8. Accessed 23 Oct. 2023.
Dayne, A. (2022). Create foreign key objects inside serializer. [online] Stack Overflow. Available at: https://stackoverflow.com/questions/73162763/create-foreign-key-objects-inside-serializer [Accessed 4 Nov. 2023].



"""