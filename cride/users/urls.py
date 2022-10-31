"""Users URLs."""

# Django
from django.urls import path

# Views
from cride.users.views import (
    UserLogin,
    UserSignUp,
)

urlpatterns = [
    path('users/login/', UserLogin.as_view(), name='login'),
    path('users/signup/', UserSignUp.as_view(), name='signup'),
]
