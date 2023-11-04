from django.db import models
from areas.models import Area

# Create your models here.
class User(models.Model):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    userType = models.CharField(max_length=10)
    totalReviews = models.IntegerField()
    password = models.CharField(max_length=225, default='password')
    email = models.CharField(max_length=225, default='email')
    fName = models.CharField(max_length=225, default='fName')
    lName = models.CharField(max_length=225, default='lName')


class Review(models.Model):
    reviewID = models.AutoField(primary_key=True)
    #REF: Reference a PK as a FK with Django serializers (Sankalpjonna.com, 2023)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', default=None)
    areaID = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='reviews', default=None)
    imageYN =  models.BooleanField(default=False)
    #REF: Upload image using Django ImageField (Curry,2023)
    image = models.ImageField(upload_to='files/reviewImages')
    longitude = models.DecimalField(max_digits=50, decimal_places=30)
    latitude = models.DecimalField(max_digits=50, decimal_places=30)
    reviewText = models.CharField(max_length=300)
    reviewType = models.CharField(max_length=255)
    feelRating = models.DecimalField(max_digits=5, decimal_places=2)

    
    

"""
REFERENCES:

Sankalpjonna.com. (2023). Representing foreign key values in Django serializers. [online] Available at: https://www.sankalpjonna.com/learn-django/representing-foreign-key-values-in-django-serializers [Accessed 4 Nov. 2023].
Curry, C. (2022). How to Upload an Image Using Django ImageField (The RIGHT Way). YouTube. Available at: https://www.youtube.com/watch?v=fsVY66QBhwM [Accessed 4 Nov. 2023].

"""