from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDelete

urlpatterns = [
    path('users', UserListCreate.as_view(), name="Create-User-List"), # Environment
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name="User-Details") # Environment
]




"""
REFERENCES:


"""