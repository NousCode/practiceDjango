"""Circle permissión classes."""

# Django REST framework
from rest_framework.permissions import BasePermission

# Models
from cride.circles.models import Membership


class IsCircleAdmin(BasePermission):
    """Allow access. Only to circle admins."""

    def has_object_permission(self, request, view, obj):
        """Check that the object and user are the same."""
        try:
            Membership.objects.get(
                user=request.user,
                circle=obj,
                is_admin=True,
                is_active=True
            )
        except Membership.DoesNotExist:
            return False
        return True
