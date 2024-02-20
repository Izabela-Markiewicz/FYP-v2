from django.urls import path
from . import views
from .views import UserListCreate, UserRetrieveUpdateDelete

urlpatterns = [
    path('users', UserListCreate.as_view(), name="Create-User-List"), # Environment
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name="User-Details"), # Environment
    path('login_user/', views.login_user, name="login_user"), # Iteration 5
    path('logout_user/', views.logout_user, name="logout_user"), # Iteration 5
    path('register_user/', views.register_user, name="register_user"), # Iteration 5
]




"""
REFERENCES:


"""