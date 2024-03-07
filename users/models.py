from django.db import models
from areas.models import PoliceDivision
from django.utils import timezone
from datetime import datetime
from  django.contrib.auth.models import User
from django.conf import settings
from django.db import models


# Iteration 1:
# CREATING MODELS for all user-related objects
class User(models.Model):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    userType = models.CharField(max_length=10)
    totalReviews = models.IntegerField()
    password = models.CharField(max_length=225, default='pw')
    email = models.CharField(max_length=225, default='email')
    fName = models.CharField(max_length=225, default='fName')
    lName = models.CharField(max_length=225, default='lName')


class Review(models.Model):
    reviewID = models.AutoField(primary_key=True)
    policeID = models.ForeignKey(PoliceDivision, on_delete=models.CASCADE, related_name='reviews', null=True, default=None)
    author = models.IntegerField(blank=False, default=1)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    #REF: Reference a PK as a FK with Django serializers (Sankalpjonna.com, 2023)
    # userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', default=None)
    # areaID = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='reviews', null=True, default=None)
    imageYN =  models.BooleanField(default=False)
    #REF: Upload image using Django ImageField (Curry,2023)
    image = models.ImageField(upload_to='files/reviewImages', null=True, blank=True)
    #longitude = models.DecimalField(max_digits=50, decimal_places=30,null=True, blank=True)
    #latitude = models.DecimalField(max_digits=50, decimal_places=30, null=True, blank=True)
    reviewText = models.CharField(max_length=1500, null=True, blank=True)
    feelRating = models.DecimalField(max_digits=2, decimal_places=1, choices=[(i/2, i/2) for i in range(1, 11)])
    #reviewType = models.CharField(max_length=1500,null=True, blank=True)
    feelRating = models.DecimalField(max_digits=5, decimal_places=1)
    publishDate = models.DateTimeField(default=timezone.now) #Iteration 4:
    approved =  models.BooleanField(default=False) #Iteration 5:
  


    

    
    

"""
REFERENCES:

Sankalpjonna.com. (2023). Representing foreign key values in Django serializers. [online] Available at: https://www.sankalpjonna.com/learn-django/representing-foreign-key-values-in-django-serializers [Accessed 4 Nov. 2023].
Curry, C. (2022). How to Upload an Image Using Django ImageField (The RIGHT Way). YouTube. Available at: https://www.youtube.com/watch?v=fsVY66QBhwM [Accessed 4 Nov. 2023].

"""