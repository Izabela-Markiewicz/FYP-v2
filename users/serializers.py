from rest_framework import serializers
from .models import User

# REF: Serialisers used in Youtube Video Connecting PostgreSQL to Django (MrNick, 2023) "Building a CRUD API with Django Rest Framework and PostgreSQL - Tutorial for Beginners."
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userid', 'username', 'usertype', 'totalreviews', 'password', 'email', 'fname', 'lname')


"""
REFERENCES:

MrNick. “Building a CRUD API with Django Rest Framework and PostgreSQL - Tutorial for Beginners.” Www.youtube.com, Feb. 2023, www.youtube.com/watch?v=1YmfnQ8i9o8. Accessed 23 Oct. 2023.



"""