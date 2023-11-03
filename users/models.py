from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    usertype = models.CharField(max_length=10)
    totalreviews = models.IntegerField()
    password = models.CharField(max_length=225, default='password')
    email = models.CharField(max_length=225, default='email')
    fname = models.CharField(max_length=225, default='fName')
    lname = models.CharField(max_length=225, default='lName')




"""
REFERENCES:


"""