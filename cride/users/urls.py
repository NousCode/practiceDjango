"""Users URLs."""

# Django
from django.urls import path

# Views
from cride.users.views import UserLogin

urlpatterns = [
    path('users/login/', UserLogin.as_view(), name='login'),
]
