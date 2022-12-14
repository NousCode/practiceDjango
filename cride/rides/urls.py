"""Rides url."""

# Django
from django.urls import path, include

# Django REST framework
from rest_framework.routers import DefaultRouter

# Views
from .views import rides as rides_views

router = DefaultRouter()
router.register(
    r'circles/(?P<slug_name>[-a-zA-Z0-9-]+)/rides',
    rides_views.RideViewSet,
    basename='ride'
)

urlpatterns = [
    path('', include(router.urls))
]

