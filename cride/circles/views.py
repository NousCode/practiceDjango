"""Circles views."""

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from cride.circles.models import Circle

# Serializer
from cride.circles.serializers import CircleSerializer, CreateCircleSerializer


@api_view(['GET', 'POST'])
def list_circles(request):
    """List circles or create a circle."""
    if request.method == 'GET':
        circles = Circle.objects.filter(is_public=True)
        serializer = CircleSerializer(circles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CreateCircleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        circle = serializer.save()
        return Response(CircleSerializer(circle).data)
